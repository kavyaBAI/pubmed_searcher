from typing import List
from Bio import Entrez

Entrez.email = "kavyaadithi8787@gmail.com"  

def search_papers(query: str, max_results: int = 10) -> List[str]:
    """
    Search PubMed for papers matching the query.
    Returns a list of PubMed IDs.
    """
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    results = Entrez.read(handle)
    return results["IdList"]

def fetch_paper_details(paper_ids: List[str]) -> str:
    """
    Fetch full paper details for a list of PubMed IDs.
    Returns raw MEDLINE text data.
    """
    handle = Entrez.efetch(db="pubmed", id=paper_ids, rettype="medline", retmode="text")
    return handle.read()

