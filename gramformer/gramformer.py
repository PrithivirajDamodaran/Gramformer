class Gramformer:

    def __init__(self, models=2, use_gpu=False):
        from transformers import AutoTokenizer
        from transformers import AutoModelForSeq2SeqLM

        if use_gpu:
            device = "cuda:0"
        else:
            device = "cpu"

        self.device = device
        correction_model_tag = "prithivida/grammar_error_correcter_v1"

        if models == 2:
            self.correction_tokenizer = AutoTokenizer.from_pretrained(correction_model_tag)
            self.correction_model = AutoModelForSeq2SeqLM.from_pretrained(correction_model_tag)
            self.correction_model = self.correction_model.to(device)
            print("[Gramformer] Grammar error correction model loaded..")
        elif models == 1:
            print("[Gramformer] Highlight model not supported, yet")
        elif models == 3:
            self.correction_tokenizer = AutoTokenizer.from_pretrained(correction_model_tag)
            self.correction_model = AutoModelForSeq2SeqLM.from_pretrained(correction_model_tag)
            self.correction_model = self.correction_model.to(device)
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

    def highlight(self, input_sentence: str, max_corrections: int = 1) -> str:
        from difflib import ndiff
        
        highlighted = []
        changes = list(ndiff(
            input_sentence,
            self.correct(input_sentence, max_corrections=max_corrections)[0]
        ).__iter__())
        
        for i, p_e in enumerate(changes):
            n_i, b_i = [(i + m) % len(changes) for m in [1, -1]]
            b_i = 0 if b_i > i else b_i
            n_i = -1 if n_i < i else n_i
            mode = 'a' if p_e[0] == "+" else 'd'
            
            if p_e[0] != " ":
                if n_i == -1:
                    if changes[b_i][0] == p_e[0]:
                        highlighted.append(f"{p_e[2]}</{mode}>")
                    else:
                        highlighted.append(f"<{mode}>{p_e[2]}</{mode}>")
                elif i != 0 and changes[b_i][0] == p_e[0]:
                    if changes[n_i][0] == p_e[0]:
                        highlighted.append(f"{p_e[2]}")
                    else:
                        highlighted.append(f"{p_e[2]}</{mode}>")
                elif i != 0:
                    if changes[n_i][0] == p_e[0]:
                        highlighted.append(f"<{mode}>{p_e[2]}")
                    else:
                        highlighted.append(f"<{mode}>{p_e[2]}</{mode}>")
                elif i == 0:
                    if changes[n_i][0] == p_e[0]:
                        highlighted.append(f"<{mode}>{p_e[2]}")
                    else:
                        highlighted.append(f"<{mode}>{p_e[2]}</{mode}>")
            else:
                highlighted.append(p_e[2])
                
        return "".join(highlighted)

    def detect(self, input_sentence):
        # TO BE IMPLEMENTED
        pass
