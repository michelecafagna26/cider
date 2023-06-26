Consensus-based Image Description Evaluation metric (CIDEr Code) for Image Captioning.
===================

Evaluation code for CIDEr metric. Provides CIDEr as well as
CIDEr-D (CIDEr Defended) which is more robust to gaming effects

## System requirements for running ##
- python 3.6 

## System requirements for testing and PTBTokenizer
- python 3.6
- java 1.8.0

## Installation

clone this repository then:

```bash
pip install .

python3 -m spacy download en_core_web_sm

```

or install it in your environment from github:

```bash
pip install git+https://github.com/michelecafagna26/cider.git#egg=cidereval
```

***


## Quick usage (PTBTokenizer by default)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1x6YNmHz87mwX6fmZwjbsRpCJcvbzbmst?authuser=1#scrollTo=QVHvbzgugq6D)

```python
from cidereval import cider, ciderD

# refs and preds are lists of strings, the method will re-format them for you

cider(predictions=preds, references=refs)
#cider_scores is a dict-like object with "avg_score" and "scores"

```
By default, it uses the **coco-val idf**. To compute the idfs on your references pass df='corpus'.


## Important Note

In this implementations, we provide an alternative tokenizer to the PTBtokenizer in order to remove the java dependency.
The new tokenizer is based on Spacy (SimpleTokenizer.py)

However, we suggest using the original PTBTokenizer as the tokenization is not exactly the same and the former is also faster (about 3x faster) than the spacy tokenizer.

For detail regarding performance look [here](important_note.md).
For more detail this implementation look [here](detail.md).

## References ##

- PTBTokenizer: We use the [Stanford Tokenizer](http://nlp.stanford.edu/software/tokenizer.shtml) which is included in [Stanford CoreNLP 3.4.1](http://nlp.stanford.edu/software/corenlp.shtml).
- CIDEr: [CIDEr: Consensus-based Image Description Evaluation] (http://arxiv.org/pdf/1411.5726.pdf)
- python3 adaptation of the original repo: https://github.com/daqingliu/cider

## Developers ##
- Ramakrishna Vedantam (Virgina Tech) (origianl repo)

## Acknowledgments ##
- MS COCO Caption Evaluation Team
