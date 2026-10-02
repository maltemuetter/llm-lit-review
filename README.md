# llm-lit-review

Using large language models to screen the scientific literature on drug
combinations.

**Question:** how often do papers treat a "synergistic" drug interaction as a
sign that a combination is good? This matters because synergy says little about
whether a combination is actually better for treatment.

## How it works

1. **Find papers**: query PubMed for every paper from 2010-2025 whose title or
   abstract uses a *synerg\** word (`synergy_gate.py`).
2. **Sample**: draw a random sample of 1,000 papers with complete abstracts
   (`sampling.py`).
3. **Screen with LLMs**: each abstract is classified by two models (Mistral
   Large and Claude Sonnet) with five prompts, each a slightly different reading
   of the question (`run_sample.py`, `prompts.py`). Outputs follow a fixed
   schema.
4. **Analyse**: rates per model and prompt are scaled to the whole pool,
   overall, per research domain and per year (`analyse_screening.py`,
   `plot_results.py`).

Running several models and prompts, instead of one, shows how much the answer
depends on how the question is read. `DECISIONS.md` explains the design choices,
including approaches that were tried and dropped.

## Running it

The pipeline runs in Docker; see `DOCKER.md`. Copy `.env.example` to `.env` and
add API keys for Mistral and Anthropic (only needed for the LLM steps).

## Folders

- `code/`: pipeline scripts
- `data/`: PubMed snapshots and screening results
- `figures/`, `report/`: figures and an automated summary report

## Status

Manuscript in preparation.
