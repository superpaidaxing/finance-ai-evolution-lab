---
license: cc-by-nc-4.0
dataset_info:
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  - name: reasoning
    dtype: bool
  - name: category
    dtype: string
  - name: references
    sequence: string
  - name: answer
    dtype: string
  - name: type
    dtype: string
  splits:
  - name: train
    num_bytes: 26474135
    num_examples: 5703
  download_size: 13097307
  dataset_size: 26474135
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# FinDER: Financial Dataset for Question Answering and Evaluating Retrieval-Augmented Generation

**FinDER** is a benchmark dataset designed for evaluating **Retrieval-Augmented Generation (RAG)** in financial question answering. It consists of **5,703 expert-annotated query–evidence–answer triplets** derived from real-world 10-K filings and ambiguous financial queries submitted by industry professionals.

This dataset captures the domain-specific challenges of financial QA, including short, acronym-heavy queries and the need for precise retrieval over lengthy, complex documents.

## 🔗 Paper  
[arXiv:2504.15800](https://arxiv.org/abs/2504.15800)  
```
@misc{choi2025finderfinancialdatasetquestion,
  title={FinDER: Financial Dataset for Question Answering and Evaluating Retrieval-Augmented Generation}, 
  author={Chanyeol Choi and Jihoon Kwon and Jaeseon Ha and Hojun Choi and Chaewoon Kim and Yongjae Lee and Jy-yong Sohn and Alejandro Lopez-Lira},
  year={2025},
  eprint={2504.15800},
  archivePrefix={arXiv},
  primaryClass={cs.IR},
  url={https://arxiv.org/abs/2504.15800}, 
}
```

## 📋 Terms of Use  
By using this dataset, you agree to:

- Provide **proper citation and attribution** to the original authors in any derived work or publication.
