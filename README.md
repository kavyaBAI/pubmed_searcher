# PubMed Searcher CLI Tool 

A command-line tool to search PubMed for research papers and extract data specifically about **non-academic author affiliations**, **publication metadata**, and **corresponding author email addresses**.

---

## Features

* Query PubMed directly from the command line
* Extract and filter **non-academic author affiliations**
* Detect and **remove duplicate affiliations**
* Extract **corresponding author emails** (if available)
* Capture **publication dates** and standardize format
* Export results to CSV with specified fields
* Helpful debug logs with `--debug`
* Clean CLI with `--help`, `--file` options

---

## Project Structure

```
pubmed_searcher/
|
├── pubmed_searcher/
│   ├── __init__.py
│   ├── cli.py          # CLI interface, argument parsing
│   ├── fetcher.py      # Handles PubMed API requests
│   ├── parser.py       # Parses MEDLINE text to structured format
│   └── utils.py        # CSV writing, helper functions
│
├── tests/
│   └── test_fetcher.py # Unit tests for fetcher logic
│
├── README.md           # Project documentation
├── pyproject.toml      # Poetry project setup
└── poetry.lock         # Poetry dependency lockfile
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kavyaBAI/pubmed_searcher.git
cd pubmed_searcher
```

### 2. Install with Poetry

```bash
poetry install
```

---

##  Usage

### Basic Query

```bash
poetry run get-papers-list "covid vaccine"
```

### With Debug and Output to CSV

```bash
poetry run get-papers-list "covid vaccine" --debug --file results.csv
```

---

## CLI Options

| Option        | Description                     |
| ------------- | ------------------------------- |
| `-h, --help`  | Show help and usage info        |
| `-d, --debug` | Enable debug logging to console |
| `-f, --file`  | Output CSV filename (optional)  |

---

## Example Output

| PubmedID | Title                      | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email                    |
| -------- | -------------------------- | ---------------- | ---------------------- | ---------------------- | --------------------------------------------- |
| 40699035 | A 20-month longitudinal... | 2025             | Maria Silva            | XYZ Biotech, USA       | [maria@example.com](mailto:maria@example.com) |

---

## 🔍 Parsing Logic Highlights

* **Duplicate affiliations** are removed using a Python `set`.
* **Publication Dates** are parsed as-is from MEDLINE (`DP -`) fields. Format consistency is maintained.
* **Emails** are extracted using regex pattern matching for any email-like structure.
* **Non-academic authors** are determined by excluding keywords like `university`, `hospital`, `institute`, `college`, etc.
* Results are stored **only if at least one non-academic author exists** in the paper.

---

## Running Tests

To ensure reliability, tests are included:

```bash
poetry run pytest
```

### Included test cases (in `tests/test_fetcher.py`):

* Validate API response structure
* Ensure parsing returns correct PubMed ID, title, date
* Check deduplication of affiliations
* Validate email extraction using sample data

---

## Author

**Kavya Bai R G**
