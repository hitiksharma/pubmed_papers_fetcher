import click
from pubmed_fetcher import fetch_pubmed_papers, fetch_paper_details, save_to_csv

@click.command()
@click.argument("query")
@click.option("-d", "--debug", is_flag=True, help="Print debug information")
@click.option("-f", "--file", default=None, help="Specify filename to save results")
def main(query, debug, file):
    """
    Command-line tool to fetch PubMed papers based on a query.
    """
    if debug:
        click.echo(f"Fetching papers for query: {query}")

    pubmed_ids = fetch_pubmed_papers(query)
    if debug:
        click.echo(f"Found {len(pubmed_ids)} papers.")

    papers = fetch_paper_details(pubmed_ids)

    if file:
        save_to_csv(papers, file)
        click.echo(f"Results saved to {file}")
    else:
        for paper in papers:
            click.echo(paper)

if __name__ == "__main__":
    main()
