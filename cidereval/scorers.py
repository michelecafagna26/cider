from cidereval import CiderD, Cider
from cidereval.tokenizer import PTBTokenizer

def _preprocess_for_cider(refs, preds):
    r"""
    Convert preds and refs to the cider data format
    
    refs: List[List[str]]
    preds : List[str]
    
    return gts: Dict[str : List[Dict['caption':str] : str ]],
           res: List[Dict['image_id':str]: 'caption':str]
    """
    
    assert len(refs) == len(preds)
    
    gts = {}
    res = []
    
    for i, (caps, pred) in enumerate(zip(refs, preds)):
        gts[i] = [{ 'caption': cap } for cap in caps ]
        
        res.append({ 'image_id': i,
                    'caption': pred})
    return gts, res

def cider(predictions, references, df="coco-val"):
    r"""
    Compute the cider score for the given predictions and references

    predictions : List[str], model's predictions
    references: List[List[str]], references
    df: str, either 'coco-val' or 'corpus' (default : 'coco-val'). If 'coco-val' the TF-IDF COCO validation split is \\
    used. If 'corpus' the TF-IDF is computed over the reference set provided.

    returns {"avg_score": mp.float, "scores": np.array(np.float)}
    """
    gts, res = _preprocess_for_cider(references, predictions)
    tokenizer_res = PTBTokenizer('res')
    tokenizer_gts = PTBTokenizer('gts')

    _gts = tokenizer_gts.tokenize(gts)
    _res = tokenizer_res.tokenize(res)

    scorer = Cider(df=df)

    score, scores = scorer.compute_score(_gts, _res)

    return {"avg_score": score, "scores": scores}


def ciderD(predictions, references, df="coco-va"):
    r"""
    Compute the ciderD score for the given predictions and references

    predictions : List[str], model's predictions
    references: List[List[str]], references
    df: str, either 'coco-val' or 'corpus' (default : 'coco-val'). If 'coco-val' the TF-IDF COCO validation split is \\
    used. If 'corpus' the TF-IDF is computed over the reference set provided.

    returns {"avg_score": mp.float, "scores": np.array(np.float)}
    """

    gts, res = _preprocess_for_cider(references, predictions)
    tokenizer_res = PTBTokenizer('res')
    tokenizer_gts = PTBTokenizer('gts')

    _gts = tokenizer_gts.tokenize(gts)
    _res = tokenizer_res.tokenize(res)

    scorer = CiderD(df=df)

    score, scores = scorer.compute_score(_gts, _res)

    return { "avg_score": score, "scores": scores}
