from typing import List, Dict
import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "institute", "school", "hospital", "center", "faculty", "department"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def parse_medline(raw_data: str) -> List[Dict]:
    papers = []
    entries = raw_data.strip().split("\n\n")  # Each paper is separated by a double newline

    for entry in entries:
        lines = entry.split("\n")
        paper = {
            "PubmedID": "",
            "Title": "",
            "Publication Date": "",
            "Non-academic Author(s)": [],
            "Company Affiliation(s)": [],
            "Corresponding Author Email": ""
        }

        for line in lines:
            if line.startswith("PMID- "):
                paper["PubmedID"] = line.replace("PMID- ", "").strip()
            elif line.startswith("TI  - "):
                paper["Title"] = line.replace("TI  - ", "").strip()
            elif line.startswith("DP  - "):
                paper["Publication Date"] = line.replace("DP  - ", "").strip()
            elif line.startswith("AD  - "):  # Author affiliation
                affiliation = line.replace("AD  - ", "").strip()
                if is_non_academic(affiliation):
                    if affiliation not in paper["Company Affiliation(s)"]:
                        paper["Company Affiliation(s)"].append(affiliation)

                    # Try to extract a name
                    name_match = re.search(r'([A-Z][a-z]+ [A-Z][a-z]+)', affiliation)
                    if name_match and name_match.group(1) not in paper["Non-academic Author(s)"]:
                        paper["Non-academic Author(s)"].append(name_match.group(1))

            # Check any line for an email, fallback
            if not paper["Corresponding Author Email"]:
                email_match = re.search(r'[\w\.-]+@[\w\.-]+', line)
                if email_match:
                    paper["Corresponding Author Email"] = email_match.group()

        if paper["Company Affiliation(s)"]:
            paper["Company Affiliation(s)"] = list(set(paper["Company Affiliation(s)"]))
            paper["Non-academic Author(s)"] = list(set(paper["Non-academic Author(s)"]))
            papers.append(paper)

    return papers
