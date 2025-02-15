import requests
import pandas as pd
import re
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

# PubMed API Base URL
PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# List of keywords to identify non-academic institutions
NON_ACADEMIC_KEYWORDS = ["Inc", "Ltd", "Corporation", "Pharma", "Biotech", "Biomedical", "GmbH", "S.A.", "LLC", "Laboratories", "Sciences"]

def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[str]:
    """
    Fetches PubMed article IDs matching the query.
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(PUBMED_BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"].get("idlist", [])

def fetch_paper_details(pubmed_ids: List[str]) -> List[Dict[str, str]]:
    """
    Fetches detailed information for a list of PubMed article IDs.
    """
    papers = []
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(PUBMED_FETCH_URL, params=params)
    response.raise_for_status()
    
    root = ET.fromstring(response.text)
    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.find(".//PMID").text
        title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") else "N/A"
        pub_date = article.find(".//PubDate").text if article.find(".//PubDate") else "N/A"
        
        authors = []
        companies = []
        corresponding_email = "N/A"

        for author in article.findall(".//Author"):
            name = author.find("LastName").text if author.find("LastName") else "Unknown"
            affiliation = author.find("Affiliation").text if author.find("Affiliation") else ""
            
            if any(keyword in affiliation for keyword in NON_ACADEMIC_KEYWORDS):
                authors.append(name)
                companies.append(affiliation)
            
            if "@gmail.com" in affiliation or re.search(r"\bemail\b", affiliation, re.IGNORECASE):
                corresponding_email = affiliation

        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(authors),
            "Company Affiliation(s)": ", ".join(companies),
            "Corresponding Author Email": corresponding_email
        })

    return papers

def save_to_csv(papers: List[Dict[str, str]], filename: str):
    """
    Saves the list of research papers to a CSV file.
    """
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
