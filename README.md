# Python News Article Analyzer

A simple project to analyze a news article using spaCy and python-docx.

## Overview

This repository includes:
- `pythonAssessment.ipynb`: main notebook implementing `NewsArticleAnalyzer`
- `News Article for Python Assessment.docx`: sample input text document

The analyzer computes:
- word count (target word)
- most common word
- average word length
- paragraph count
- sentence count

## Requirements

- Python 3.8+
- spaCy
- python-docx

Install dependencies:

```bash
pip install spacy python-docx
python -m spacy download en_core_web_sm
```

## Usage

Run the notebook `pythonAssessment.ipynb` in Jupyter/VS Code (or convert to script). It loads `News Article for Python Assessment.docx`, analyzes the text, and prints metrics.

## Notes

- Ensure `en_core_web_sm` is installed before running.
- If using a different spaCy model, change `spacy.load("en_core_web_sm")` in the notebook.
