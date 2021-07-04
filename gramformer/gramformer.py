class Gramformer:

  def __init__(self, models=2, use_gpu=False):
    from transformers import AutoTokenizer
    from transformers import AutoModelForSeq2SeqLM
    import errant
    self.annotator = errant.load('en')

    if use_gpu:
        device= "cuda:0"
    else:
        device = "cpu"

    self.device    = device
    correction_model_tag = "prithivida/grammar_error_correcter_v1"
    
    if models == 1 or models == 2:
        self.correction_tokenizer = AutoTokenizer.from_pretrained(correction_model_tag)
        self.correction_model     = AutoModelForSeq2SeqLM.from_pretrained(correction_model_tag)
        self.correction_model     = self.correction_model.to(device)
        print("[Gramformer] Grammar error correction model loaded..")
    elif models == 3:
        self.correction_tokenizer = AutoTokenizer.from_pretrained(correction_model_tag)
        self.correction_model     = AutoModelForSeq2SeqLM.from_pretrained(correction_model_tag)
        self.correction_model     = self.correction_model.to(device)
        print("[Gramformer] All models loaded..")    
    

  def correct(self, input_sentence, max_corrections=1):
      correction_prefix = "gec: "
      input_sentence = correction_prefix + input_sentence
      input_ids = self.correction_tokenizer.encode(input_sentence, return_tensors='pt')
      input_ids = input_ids.to(self.device)

      preds = self.correction_model.generate(
          input_ids,
          do_sample=True, 
          max_length=128, 
          top_k=50, 
          top_p=0.95, 
          early_stopping=True,
          num_return_sequences=max_corrections)

      corrected = []
      for pred in preds:  
        corrected.append(self.correction_tokenizer.decode(pred, skip_special_tokens=True).strip())

      return corrected

  def highlight(self, input_sentence):
     # TO BE IMPLEMENTED
     pass

def _get_edits(self, orig, cor):
    orig = self.annotator.parse(orig)
    cor = self.annotator.parse(cor)
    alignment = self.annotator.align(orig, cor)
    edits = self.annotator.merge(alignment)

    if len(edits) == 0:  
        return []

    edit_annotations = []
    for e in edits:
        e = self.annotator.classify(e)
        edit_annotations.append((e.type[2:], e.o_str, e.o_start, e.o_end,  e.c_str, e.c_start, e.c_end))
            
    if len(edit_annotations) > 0:
        return edit_annotations
    else:    
        return []


def get_edits(self, input_sentence):
     correction_prefix = "gec: "
      input_sentence = correction_prefix + input_sentence
      input_ids = self.correction_tokenizer.encode(input_sentence, return_tensors='pt')
      input_ids = input_ids.to(self.device)

      preds = self.correction_model.generate(
          input_ids,
          do_sample=True, 
          max_length=128, 
          top_k=50, 
          top_p=0.95, 
          early_stopping=True,
          num_return_sequences=1)

      corrected = []
      for pred in preds:  
        corrected.append(self.correction_tokenizer.decode(pred, skip_special_tokens=True).strip())

      orig = input_sentence[5:].strip()
      cor  = corrected[0]   
      edits = _get_edits(orig, cor)

      return edits

   

  def detect(self, input_sentence):
      # TO BE IMPLEMENTED
      pass
