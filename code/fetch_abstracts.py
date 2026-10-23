"""Re-fetch the sample's abstracts from PubMed into the local, untracked cache."""

import json

from sampling import SAMPLE_PATH, fetch_records, save_abstracts


def main():
    """Fetch the abstracts of all sampled PMIDs and cache them."""
    pmids = [paper["pmid"] for paper in json.loads(SAMPLE_PATH.read_text())["papers"]]
    records = fetch_records(pmids)
    save_abstracts(records.values())
    print(f"cached {len(records)} of {len(pmids)} abstracts")


if __name__ == "__main__":
    main()
