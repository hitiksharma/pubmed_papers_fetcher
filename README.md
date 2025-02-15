
# PubMed Papers Fetcher

This project is a command-line tool designed to fetch academic papers from PubMed based on user queries. The tool provides detailed information about the papers, including non-academic authors and their affiliations, and allows saving the results to a CSV file.

---

## **Approach and Methodology**

### **Project Structure**
- **`cli.py`**: Main command-line interface using `click` to handle user inputs and display results.
- **`pubmed_fetcher.py`**: Core module that interacts with the PubMed API, processes fetched data, and saves it to a CSV file.
- **`pyproject.toml`**: Defines project dependencies and setup using Poetry.

### **Methodology**
1. **Querying PubMed API**:
   - The tool sends an HTTP request to the PubMed API with the user-provided query.
   - Retrieves up to 10 PubMed IDs based on the query.

2. **Fetching Paper Details**:
   - Another API call fetches detailed XML data for the obtained PubMed IDs.
   - Parses XML to extract key information such as title, publication date, authors, and affiliations.

3. **Identifying Non-Academic Institutions**:
   - Uses a list of keywords (`Inc`, `Ltd`, `GmbH`, etc.) to identify non-academic affiliations.
   - Extracts author names and their corresponding non-academic institutions.

4. **Saving Results**:
   - Outputs results directly to the console or saves them as a CSV file using `pandas`.

---

## **Results**
- Successfully fetched and displayed PubMed papers for sample queries.
- Identified non-academic authors and their company affiliations.
- Exported data to CSV format for further analysis.

---

## **Usage**
Run the tool from the command line:
```bash
poetry run python cli.py "cancer research" --debug -f output.csv
```

---

## **Dependencies**
- Python 3.11+
- Requests
- Pandas
- Click

---

## **Installation Instructions**
1. Clone the repository.
2. Install Poetry.
3. Run `poetry install` to set up dependencies.

---

## **Execution Instructions**
Use the command:
```bash
poetry run python cli.py "cancer research" --debug -f output.csv
```

---

## **Tools Used**
- **OpenAI LLM** for code assistance.

---


## **Author**
Hitik Sharma
