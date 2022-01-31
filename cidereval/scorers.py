from cidereval import CiderD, Cider
from cidereval.tokenizer import PTBTokenizer

def _preprocess_for_cider(refs, preds):
    """
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
        gts[i] = [ { 'caption': cap } for cap in caps ]
        
        res.append({ 'image_id': i,
                    'caption': pred})
    return gts, res

def cider(refs, preds, df="corpus"):

    gts, res = _preprocess_for_cider(refs, preds)
    tokenizer_res = PTBTokenizer('res')
    tokenizer_gts = PTBTokenizer('gts')

    _gts = tokenizer_gts(gts)
    _res = tokenizer_res(res)

    scorer = Cider(df=df)

    score, scores = scorer.compute_score(_gts, _res)

    return { "avg_score": score, "scores": scores}


def ciderD(refs, preds, df="corpus"):

    gts, res = _preprocess_for_cider(refs, preds)
    tokenizer_res = PTBTokenizer('res')
    tokenizer_gts = PTBTokenizer('gts')

    _gts = tokenizer_gts(gts)
    _res = tokenizer_res(res)

    scorer = CiderD(df=df)

    score, scores = scorer.compute_score(_gts, _res)

    return { "avg_score": score, "scores": scores}