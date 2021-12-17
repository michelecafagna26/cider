#!/usr/bin/env python
# 
# File Name : simpletokenizer.py
#
# Description : Yet another tokenizer.
#
# Creation Date : 12-11-2021

import spacy
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER
from spacy.lang.char_classes import CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from spacy.util import compile_infix_regex


# punctuations to be removed from the sentences
PUNCTUATIONS = ["''", "'", "``", "`", "-LRB-", "-RRB-", "-LCB-", "-RCB-",
                ".", "?", "!", ",", ":", "-", "--", "...", ";", " ", ""]

infixes = (
    LIST_ELLIPSES
    + LIST_ICONS
    + [
        r"(?<=[0-9])[+\-\*^](?=[0-9-])",
        r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
            al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
        ),
        r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
        # ✅ Commented out regex that splits on hyphens between letters:
        # r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
        r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
    ]
)


class SimpleTokenizer:
    """Simple Tokenizer"""

    def __init__(self, _source='gts'):
        self.source = _source

        # setting up the tokenizer
        self._nlp  = spacy.load("en_core_web_sm")
        infix_re = compile_infix_regex(infixes)
        self._nlp.tokenizer.infix_finditer = infix_re.finditer
        self._tokenizer = self._nlp.tokenizer

    def tokenize(self, captions_for_image):
        """Tokenize a sample

        Args:
            captions_for_image : 

                IF _source='gts' follows format:
                    dict: { str : [
                        { "caption" : str },
                        { "caption" : str },
                        ...
                            ],
                      str : [ ... ],
                      ...
                    }
                IF  _source='res' follows format:
                    list: [ {"image_id" : str,
                             "caption" : str,  
                            }, 
                            ...    
                            ]
        Returns:  
            final_tokenized_captions_for_index:
                list: [ {"image_id" : str,
                                    "caption" : str,  
                                    }, 
                                    ...    
                                    ]
        """   

        tokenized_captions = None

        if self.source == 'gts':
            tokenized_captions= {}

            for k in captions_for_image:

                if k not in tokenized_captions:
                    tokenized_captions[k] = []

                for item in captions_for_image[k]:

                    tokenized_captions[k].append(
                        " ".join([ tok.text.lower().strip() for tok in self._tokenizer(item['caption']) if tok.text.lower().strip() not in PUNCTUATIONS]))          

        elif self.source == 'res':

            tokenized_captions= []
            
            for item in captions_for_image:
                
                tokenized_captions.append(
                    { 'image_id' : item['image_id'], 
                      'caption' :  [" ".join([ tok.text.lower().strip() for tok in self._tokenizer(item['caption']) if tok.text.lower().strip() not in PUNCTUATIONS])]
                    })
        
        else:
            ValueError("source can be either 'gts' or 'res' ")
            
        return tokenized_captions