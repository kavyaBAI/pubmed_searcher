import csv
from typing import List, Dict

def save_to_csv(data: List[Dict], filename: str) -> None:
    """
    Saves the list of paper dictionaries to a CSV file.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow([
            "PubmedID",
            "Title",
            "Publication Date",
            "Non-academic Author(s)",
            "Company Affiliation(s)",
            "Corresponding Author Email"
        ])

        for row in data:
            writer.writerow([
                row.get("PubmedID", ""),
                row.get("Title", ""),
                row.get("Publication Date", ""),
                "; ".join(row.get("Non-academic Author(s)", [])),
                "; ".join(row.get("Company Affiliation(s)", [])),
                row.get("Corresponding Author Email", "")
            ])
