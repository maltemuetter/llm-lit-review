# The problem with synergy: literature review

Code and data for the automated literature review in "The problem with synergy" (Muetter, Angst, Bonhoeffer and Regoes; submitted to *Philosophical Transactions of the Royal Society B*).
The review estimates how many PubMed papers present drug synergy as desirable.

## Pipeline

| Step | Script | Output |
|---|---|---|
| 1. Find all papers from 2010–2025 whose title or abstract uses a *synerg\** word, dated by their latest publication date | `synergy_gate.py` | `data/synerg_gate_pmids.json`, `data/synerg_paper_years.json`, `data/synerg_papers_per_year.json` |
| 2. Draw a random sample of 1,000 papers with complete abstracts (seed 42) | `sampling.py` | `data/screening_sample_v5.json` |
| 3. Classify each paper's domain and, under five prompts, whether it presents synergy as desirable, with Mistral Large and Claude Sonnet | `run_sample.py`, `prompts.py` | `data/screening_v5/domain.jsonl`, `data/screening_v5/outcome.jsonl` |
| 4. Analyse the rates per configuration, domain and year | `analyse_screening.py`, `plot_results.py` | `data/analysis_v5.txt`, `figures/` |
| 5. Export the supplementary tables and the prompt appendix | `export_tables.py`, `export_prompts.py` | `.tex` files in a sibling `supplementary/` folder |

Running ten model–prompt configurations instead of one shows how much the result depends on how the question is read.
`DECISIONS.md` explains the design choices, including approaches that were tried and dropped.

## Reproducing the results

Steps 4 and 5 need only the data in this repository:

```
pip install -r requirements.txt
cd code
python analyse_screening.py
python plot_results.py
```

Steps 1–3 query PubMed and the model APIs.
They run in Docker (see `DOCKER.md`); copy `.env.example` to `.env` and add API keys for Mistral and Anthropic.
The PubMed queries for the published results were run on 23 September 2026.

## Abstracts

PubMed abstracts may be under publisher copyright, so they are not included.
`data/screening_sample_v5.json` lists the PMID, title and year of each sampled paper.
To rerun the classification, re-fetch the abstracts into a local cache first:

```
python code/fetch_abstracts.py
```

Re-fetched abstracts can differ slightly from those classified, because PubMed records are occasionally corrected.

## Data

- `data/screening_v5/*.jsonl`: one record per paper, model and task, holding either the answer or the error.
- `data/synerg_dates.jsonl`, `data/score1_dates.jsonl`, `data/gated_v3_dates.jsonl`: publication dates fetched from PubMed, reused by `synergy_gate.py` as a cache.
- `data/analysis_v5.txt`: the analysis report behind the numbers in the article and its supplement.

## Licence

The code is released under the MIT licence (`LICENSE`).
Data generated in this project (model answers, analyses and figures) are released under CC BY 4.0.
PubMed metadata (PMIDs, titles and publication dates) come from the US National Library of Medicine and are not covered by these licences.

## Citation

Please cite the article and this repository via its Zenodo DOI.
