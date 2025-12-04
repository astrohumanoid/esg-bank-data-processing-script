# esg-bank-data-processing-script

# ESG Data Processing Pipeline

This repository provides a modular pipeline for downloading, preprocessing, and analyzing ESG-related textual data derived from the Hugging Face dataset:

**Dataset source:**
[https://huggingface.co/datasets/astrohumanoid/esg_bank](https://huggingface.co/datasets/astrohumanoid/esg_bank)

The workflow is designed to support large-scale document collection, sentence-level processing, relevance filtering, and post-annotation analysis.

---

## 1. Overview of the Main Templates

### 1.1 `template_downloading_file.py`

This script is responsible for:

* Downloading ESG-related documents based on a list of URLs.
* Organizing the downloaded files into year-specific folders.
* Ensuring reproducibility of data collection across different time periods.

It uses a CSV file containing document URLs (e.g., `list_url_trf(2004).csv`) as input and stores the raw documents locally for downstream processing.

---

### 1.2 `template_chunking_sentences.py`

This script performs sentence-level preprocessing:

* Loads the raw downloaded documents.
* Splits long documents into individual sentences or smaller text chunks.
* Outputs structured sentence-level data suitable for annotation and NLP modeling.

This step is crucial for enabling fine-grained sentiment and relevance labeling.

---

### 1.3 `template_filter_relevant_sentences.py`

This script is used to:

* Filter out irrelevant or low-quality sentences.
* Retain only ESG-relevant or target-topic-related content.
* Reduce noise before the annotation and modeling stages.

The result is a cleaned dataset focused on analytically meaningful content.

---

## 2. How to Use the Templates

To run the pipeline for a specific year:

1. Open each template script and change the **year** variable to the target year you want to process.
2. Make sure that all required input and output folders exist before running the scripts.
3. A sample URL list file named
   `list_url_trf(2004).csv`
   is provided in the GitHub repository as a reference format for your own yearly URL lists.
4. Run the scripts in the following order:

   1. `template_downloading_file.py`
   2. `template_chunking_sentences.py`
   3. `template_filter_relevant_sentences.py`

This ensures that data flows correctly from raw documents to filtered sentence-level samples.

---

## 3. Post-Annotation Analysis

After annotation and labeling are completed, the following analysis scripts are provided:

* **`train_test_split.ipynb`**
  Used to create consistent training and testing splits from the labeled dataset.

* **`agreement_analysis.ipynb`**
  Used to analyze inter-annotator agreement and labeling consistency.

These notebooks support dataset validation and preparation for machine learning experiments.

---

## 4. Dataset Reference

All data processing scripts in this repository are designed to work with and are derived from the following dataset:

[https://huggingface.co/datasets/astrohumanoid/esg_bank](https://huggingface.co/datasets/astrohumanoid/esg_bank)

Please refer to the original dataset page for licensing, data structure, and citation requirements.

---

## 5. Typical Workflow Summary

1. Prepare yearly URL list CSV files.
2. Download raw documents using `template_downloading_file.py`.
3. Chunk documents into sentences using `template_chunking_sentences.py`.
4. Filter relevant sentences using `template_filter_relevant_sentences.py`.
5. Annotate and label the filtered data.
6. Run post-processing and evaluation using:

   * `train_test_split.ipynb`
   * `agreement_analysis.ipynb`

---
