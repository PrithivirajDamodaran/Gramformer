from gramformer import Gramformer
import torch

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1212)


gf = Gramformer(models = 2, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 

influent_sentences = [
    "Matt like fish",
    "the collection of letters was original used by the ancient Romans",
    "We enjoys horror movies",
    "Anna and Mike is going skiing",
    "I walk to the store and I bought milk",
    "We all eat the fish and then made dessert",
    "I will eat fish for dinner and drank milk",
    "what be the reason for everyone leave the company",
]   

for influent_sentence in influent_sentences:
    corrected_sentence = gf.correct(influent_sentence)
    print("[Input] ", influent_sentence)
    print("[Correction] ",corrected_sentence[0])
    print("-" *100)
