import argparse
from pubmed_searcher.fetcher import search_papers, fetch_paper_details
from pubmed_searcher.parser import parse_medline
from pubmed_searcher.utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", help="PubMed search query (in quotes)")
    parser.add_argument("-f", "--file", help="Filename to save CSV results", default=None)
    parser.add_argument("-d", "--debug", help="Enable debug messages", action="store_true")
    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Searching for query: {args.query}")

    # Step 1: Search papers
    ids = search_papers(args.query, max_results=15)
    if args.debug:
        print(f"[DEBUG] Found {len(ids)} paper IDs.")

    # Step 2: Fetch details
    raw_data = fetch_paper_details(ids)
    if args.debug:
        print(f"[DEBUG] Fetched raw MEDLINE data.")

    # Step 3: Parse and filter
    papers = parse_medline(raw_data)
    if args.debug:
        print(f"[DEBUG] Parsed {len(papers)} papers with non-academic authors.")

    # Step 4: Output
    if args.file:
        save_to_csv(papers, args.file)
        print(f"✅ Results saved to: {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()

