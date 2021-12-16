# Important Note

**The SimpleTokenizer (Spacy) and PTBTokenize do not produce the same tokenization**

**This has consequences in the final scores**

I tryed to keep the tokenization as close as possible but at the moment there are small differences:

- PTB Tokenizer does not tokenize 'word/word' (word separated by slashes)

- PTB Tokenizer tokenize '(word)' (words in brackets) with special tokens like '-lrb-'

- In both the cases Spacy tokenize them as 3 separate tokens

Other differenes are not excluded.

---

## Test Results

###  Cider

#### df in corpus mode 

corpus: 
- refName = 'pascal50S.json'
- candName = 'pascal_candsB.json'

spacy tokenizer : 0.5870925361541144

PTB tokenizer: 0.5876485026978251
    
**diff: 0.0005559665437107064**

#### df in coco-val mode 

PTB tokenizer = 0.5580180601041953

spacy tokenizer = 0.557550429560831


**diff = 0.00046763054336429466**

###  CiderD

#### df in corpus mode 

corpus: 
- refName = 'pascal50S.json'
- candName = 'pascal_candsB.json'

spacy tokenizer : 0.48387229928700376

PTB tokenizer: 0.48439138950913807
    
**diff: 0.0005190902221343108**

#### df in coco-val mode 

PTB tokenizer = 0.4594128636973375

spacy tokenizer = 0.45890712727870175


**diff = 0.0005057364186357716**