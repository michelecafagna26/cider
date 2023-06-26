## Quick Usage (Original interface)

The code is compatible with the original interface which requies to preprocess the data before passing them to the tokenizers.
Here's an example: 

```python
from cidereval.tokenizer import PTBTokenizer
from cider.tokenier import SimpleTokenizer # for the spacy tokenizer
from cidereval import CiderD, Cider

# load reference and candidate sentences
loadDat = LoadData(pathToData)
gts, res = loadDat.readJson(refName, candName)

tokenizer_res = PTBTokenizer('res')
_res= tokenizer.tokenize(res)

tokenizer_gts = PTBTokenizer('gts')
_gts= tokenizer.tokenize(gts)

scorer = Cider(df='coco-val') # use coco-val idf
scorerD = CiderD(df='coco-val')

score, scores = scorer.compute_score(_gts, _res)
scoreD, scoresD = scorerD.compute_score(_gts, _res)

print(score)
print(scoreD)

```
## Reference corpus different from coco-val
You can use ```gts``` as reference corpus and compute the idf w.r.t to it by initializing the scorer in corpus mode: ```df='corpus'```

```python
# tokenize gts and res

# compute idf on gts
scorer = Cider(df='corpus') # corpus mode
scorerD = CiderD(df='corpus') 

score, scores = scorer.compute_score(_gts, _res)
scoreD, scoresD = scorerD.compute_score(_gts, _res)

print(score)
print(scoreD)

```

In this way the idfs are computed on-the-fly. <br> 
To **re-use them**, save them first, by calling:


```python
scorer.save_df(df_name="path/to/new_corpus") # saving idfs

```
They will be saved in  ```path/to/new_corpus.p``` file.<br>

Move the new idf file in ```data/``` to make it visible. <br>
Then, initialize the scorer running:

```python
scorer = Cider(df='path/to/new_corpus.p') # use new_corpus idf

```
e compute the scores as above

N.B Remember that if you save your idf file as ```corpus.p```, when you'll initialize the scorer, it will not load it and it will compute the idf on-the-fly (i.e Cider(df='corpus') # corpus mode )



## Files ##
./
- cidereval.py (demo script)

./PyDataFormat
- loadData.py (load the json files for references and candidates)

- {$result\_file}.json (file with the CIDEr and CIDEr-D scores)

./pycocoevalcap: The folder where all evaluation codes are stored.
- evals.py: Performs tokenization and runs both the metrics
- tokenizer: Python wrapper of Stanford CoreNLP PTBTokenizer
- cider: CIDEr evaluation codes
- ciderD: CIDEr-D evaluation codes

## NB
 CIDEr by default (with idf parameter set to "corpus" mode) computes IDF values using the reference sentences provided. Thus, CIDEr score for a reference dataset with only 1 image will be zero. When evaluating using one (or few) images, set idf to "coco-val-df" instead, which uses IDF from the MSCOCO Vaildation Dataset for reliable results.

## Instructions ##
1. Edit the params.json file to contain path to reference and candidate json files, and the result file where the scores are stored<sup>\*</sup>. 
2. Set the "idf" value in params.json to "corpus" if not evaluating on a single image/instance. Set the "idf" value to "coco-val-df" if evaluating on a single image. In this case IDF values from the MSCOCO dataset are used. If using some other corpus, get the document frequencies into a similar format as "coco-val-df", and put them in the data/ folder as a pickle file. Then set mode to the name of the document frequency file (without the '.p' extension).
3. Sample json reference and candidate files are pascal50S.json and pascal_candsB.json
4. CIDEr scores are stored in "scores" variable: scores['CIDEr'] -> CIDEr scores, scores['CIDErD'] -> CIDEr-D scores

<sup>*</sup>Even when evaluating with independent candidate/references (for eg. when using "coco-val-df"), put multiple candidate and reference entries into the same json files. This is much faster than having separate candidate and reference files and calling the evaluation code separately on each candidate/reference file.
