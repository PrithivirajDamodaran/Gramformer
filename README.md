[![PyPI - License](https://img.shields.io/npm/l/express?style=flat-square)](https://github.com/PrithivirajDamodaran/Gramformer/blob/main/LICENSE)
[![visitors](https://visitor-badge.glitch.me/badge?page_id=Gramformer.count_visitors)](https://visitor-badge.glitch.me)

<p align="center">
    <img src="./images/GLogov1.png" width="35%" height="35%"/>
</p>


# Gramformer

Human and machine generated text often suffer from grammatical and/or typographical errors. It can be spelling, punctuation, grammatical or word choice errors. Gramformer is a library that exposes 3 seperate interfaces to a family of algorithms to **detect, highlight and correct** grammar errors. To make sure the corrections and highlights recommended are of high quality, it comes with a quality estimator. You can use Gramformer in one or more areas mentioned under the "use-cases" section below or any other usecase as you see fit. Gramformer stands on the shoulders of giants, it combines some of the top notch researches in grammar correction. *Note: It works at **sentence levels** and has been trained on 64 length sentences, so not (yet) suitable for long prose or paragraphs (stay tuned for upcoming releases)*

**Fine-tuning for this model is done on relatively smaller models with not-so-much of data due to compute budget constraints. So take the results with a pinch of salt and consider this as a proof-of-concept for novel method for generating grammar error correction dataset. I am working on a version based on a larger base model and lot more data if someone might want to use this in producution setup**

## Table of contents
- [Usecases for Gramformer](#usecases-for-gramformer)
- [Installation](#installation)
- [Quick Start](#quick-start)
  * [Correcter - Available now](#correcter---available-now)
  * [Challenge with generative models](#challenge-with-generative-models)
  * [Correcter with QE estimator - Available now](#correcter-with-qe-estimator---available-now)
  * [Get Edits - Available now](#get-edits---available-now)
  * [Highlighter - Available now](#highlighter---available-now)
  * [Detector - Coming soon](#detector---coming-soon)
- [Models](#models)
- [Dataset](#dataset)
- [Note on commercial uses and release versions](#note-on-commercial-uses-and-release-versions)
- [Benchmark](#benchmark)
- [References](#references)
- [How to cite Gramformer](#how-to-cite-gramformer)

## Usecases for Gramformer

**Area 1: Post-processing machine generated text**

Machine-Language generation is becoming mainstream, so will post-processing machine generated text.

- Conditioned Text generation output(Text2Text generation).
    - **NMT**: Machine Translated output.
    - **ASR or STT**: Speech to text output.
    - **HTR**: Handwritten text recognition output.
    - **Text Summarisation** output.
    - **Image caption** output.
    - **Data or key** to Text output.
    - **Paraphrase** generation output.
- Controlled Text generation output(Text generation with PPLM) **[TBD]**.
- Free-form text generation output(Text generation)**[TBD]**.

    
**Area 2:Human-In-The-Loop (HITL) text**
<ul>
    <li>Most Supervised NLU (Chatbots and Conversational) systems need humans/experts to enter or edit text that needs to be grammatically correct otherwise the quality of HITL data can degrade the model over a period of time </li>
</ul>    
    
**Area 3:Assisted writing for humans**
<ul>
    <li>Integrating into custom Text editors of your Apps. (A Poor man's grammarly, if you will) </li>
</ul>    

**Area 4:Custom Platform integration**

As of today grammatical safety nets for authoring social contents (Post or Comments) or text in messaging platforms is very little (word level correction) or non-existent.The onus is on the author to install tools like grammarly to proof read. 

- Messaging platforms and Social platforms can highlight / correct grammtical errors automatically without altering the meaning or intent.

## Installation
```python
pip install -U git+https://github.com/PrithivirajDamodaran/Gramformer.git
```
## Quick Start

~~```python
[IMPORTANT]
If you are using in notebook, use the below line to login:
       from huggingface_hub import notebook_login
       notebook_login()
else use:
       huggingface-cli login```~~

### Correcter - Available now
```python

from gramformer import Gramformer
import torch

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1212)


gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector

influent_sentences = [
    "He are moving here.",
    "I am doing fine. How is you?",
    "How is they?",
    "Matt like fish",
    "the collection of letters was original used by the ancient Romans",
    "We enjoys horror movies",
    "Anna and Mike is going skiing",
    "I walk to the store and I bought milk",
    " We all eat the fish and then made dessert",
    "I will eat fish for dinner and drink milk",
    "what be the reason for everyone leave the company",
]   

for influent_sentence in influent_sentences:
    corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
    print("[Input] ", influent_sentence)
    for corrected_sentence in corrected_sentences:
      print("[Correction] ",corrected_sentence)
    print("-" *100)
```

```text
[Input]  He are moving here.
[Correction]  He is moving here.
----------------------------------------------------------------------------------------------------
[Input]  I am doing fine. How is you?
[Correction]  I am doing fine. How are you?
----------------------------------------------------------------------------------------------------
[Input]  How is they?
[Correction]  How are they?
----------------------------------------------------------------------------------------------------
[Input]  Matt like fish
[Correction]  Matt likes to fish.
----------------------------------------------------------------------------------------------------
[Input]  the collection of letters was original used by the ancient Romans
[Correction]  the collection of letters was originally used by the ancient Romans.
----------------------------------------------------------------------------------------------------
[Input]  We enjoys horror movies
[Correction]  We enjoy horror movies.
----------------------------------------------------------------------------------------------------
[Input]  Anna and Mike is going skiing
[Correction]  Anna and Mike are going skiing.
----------------------------------------------------------------------------------------------------
[Input]  I walk to the store and I bought milk
[Correction]  I walked to the store and I bought milk.
----------------------------------------------------------------------------------------------------
[Input]   We all eat the fish and then made dessert
[Correction]  We all ate the fish and then made dessert.
----------------------------------------------------------------------------------------------------
[Input]  I will eat fish for dinner and drink milk
[Correction]  I will eat fish for dinner and drink milk.
----------------------------------------------------------------------------------------------------
[Input]  what be the reason for everyone leave the company
[Correction]  what are the reasons why everyone left the company?
----------------------------------------------------------------------------------------------------
```

### Challenge with generative models
While Gramformer aims to post-process outputs from the generative models, Gramformer itself is a generative model. So the question arises, who will post-process the Gramformer outputs ? (I know, very meta :-)). In general all generative models have the tendency to generate spurious text sometimes, which we cannot control. So to make sure the gramformer grammar corrections (and highlights) are as accurate as possible, A quality estimator (QE) will be added. It can estimate a error correction quality score and use that as a filter on Top-N candidates to return only the best based on the score.

### Correcter with QE estimator - Available now
QE Estimator support has been rolled back due to version conflicts lm-scorer poses
<del>  Update: QE estimator is now built-in, gf.correct generates top N candidates, scores, ranks and returns the top ranked result.   </del>


### Get Edits - Available now
For edit, call ```gf.correct``` and pass original and corrected sentence to ```gf.get_edits``` method.

```python
from gramformer import Gramformer

set_seed(1212)

gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector

influent_sentences = [
    "He are moving here.",
    "the collection of letters was original used by the ancient Romans",
    "We enjoys horror movies",
    "Anna and Mike is going skiing",
    "I will eat fish for dinner and drank milk",
    "what be the reason for everyone leave the comapny"
]   

for influent_sentence in influent_sentences:
    corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
    print("[Input] ", influent_sentence)
    for corrected_sentence in corrected_sentences:
      print("[Edits] ", gf.get_edits(influent_sentence, corrected_sentence))
    print("-" *100)
```

```
[Input]  He are moving here.
[Edits]  [('VERB:SVA', 'are', 1, 2, 'is', 1, 2)]
----------------------------------------------------------------------------------------------------
[Input]  the collection of letters was original used by the ancient Romans
[Edits]  [('MORPH', 'original', 5, 6, 'originally', 5, 6)]
----------------------------------------------------------------------------------------------------
[Input]  We enjoys horror movies
[Edits]  [('VERB:SVA', 'enjoys', 1, 2, 'enjoy', 1, 2), ('NOUN', 'movies', 3, 4, 'movies.', 3, 4)]
----------------------------------------------------------------------------------------------------
[Input]  Anna and Mike is going skiing
[Edits]  [('VERB:SVA', 'is', 3, 4, 'are', 3, 4), ('OTHER', 'skiing', 5, 6, 'skiing!', 5, 6)]
----------------------------------------------------------------------------------------------------
[Input]  I will eat fish for dinner and drank milk
[Edits]  [('VERB:TENSE', 'will eat', 1, 3, 'ate', 1, 2), ('MORPH', 'drank', 7, 8, 'drink', 6, 7), ('NOUN', 'milk', 8, 9, 'milk.', 7, 8)]
----------------------------------------------------------------------------------------------------
[Input]  what be the reason for everyone leave the comapny
[Edits]  [('ORTH', 'what', 0, 1, 'What', 0, 1), ('VERB:TENSE', 'be', 1, 2, 'was', 1, 2), ('VERB:FORM', 'leave', 6, 7, 'leaving', 6, 7), ('SPELL', 'comapny', 8, 9, 'company?', 8, 9)]
----------------------------------------------------------------------------------------------------
```


### Highlighter - Available now
For highlight, call ```gf.correct``` and pass original and corrected sentence to ```gf.highlight``` method.

```python
from gramformer import Gramformer

set_seed(1212)

gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector


influent_sentences = [
    "He are moving here.",
    "the collection of letters was original used by the ancient Romans",
    "We enjoys horror movies",
    "Anna and Mike is going skiing",
    "I will eat fish for dinner and drank milk",
    "what be the reason for everyone leave the comapny"
]   

for influent_sentence in influent_sentences:
    corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
    print("[Input] ", influent_sentence)
    for corrected_sentence in corrected_sentences:
      print("[Edits] ", gf.highlight(influent_sentence, corrected_sentence))
    print("-" *100)
```

```text
[Input]  He are moving here.
[Edits]  He <c type='VERB:SVA' edit='is'>are</c> moving <c type='NOUN' edit='on.'>here.</c>
----------------------------------------------------------------------------------------------------
[Input]  the collection of letters was original used by the ancient Romans
[Edits]  the collection of letters was <c type='MORPH' edit='originally'>original</c> used by the ancient Romans
----------------------------------------------------------------------------------------------------
[Input]  We enjoys horror movies
[Edits]  We <c type='VERB:SVA' edit='enjoy'>enjoys</c> horror <c type='NOUN' edit='movies.'>movies</c>
----------------------------------------------------------------------------------------------------
[Input]  Anna and Mike is going skiing
[Edits]  Anna and Mike <c type='VERB:SVA' edit='are'>is</c> going <c type='OTHER' edit='skiing.'>skiing</c>
----------------------------------------------------------------------------------------------------
[Input]  I will eat fish for dinner and drank milk
[Edits]  I <c type='VERB:TENSE' edit='ate'>will eat</c> fish for dinner and drank <c type='NOUN' edit='milk.'>milk</c>
----------------------------------------------------------------------------------------------------
[Input]  what be the reason for everyone leave the comapny
[Edits]  what <d type='VERB' edit=''>be</d> the reason for <a type='VERB:FORM' edit='everyone to'>everyone</a> leave the <c type='SPELL' edit='company?'>comapny</c>
----------------------------------------------------------------------------------------------------
```

### Detector - Coming soon
```python
from gramformer import Gramformer
gf = Gramformer(models = 2, use_gpu=False) # 1=corrector, 2=detector
grammar_fluency_score = gf.detect(<your input sentence>)
```

## Models

|      Model          |Type                          |Return                         |status|
|----------------|-------------------------------|-----------------------------|-----------------------------|
|prithivida/grammar_error_detector |Classifier |Label                             |WIP (Reuse prithivida/parrot_fluency_on_BERT ? but I would'd say you wait :-))|
|<s>prithivida/grammar_error_highlighter</s>|Seq2Seq    |Grammar errors enclosed in ``` <e> and </e> ``` |<s>WIP</s> |
|[<s>prithivida/grammar_error_correcter</s>](https://huggingface.co/prithivida/grammar_error_correcter)|Seq2Seq    |The corrected sentence              |Beta / Pre-release (**Not available anymore**)|
|[prithivida/grammar_error_correcter_v1](https://huggingface.co/prithivida/grammar_error_correcter_v1)  |Seq2Seq    |The corrected sentence              |Stable|


## Dataset
The following techniques were used to generate datasets for fine-tunning the model prithivida/grammar_error_correcter_v1
- Download, convert and filter WikiEdits - (This is based on corpora generaion techniques mentioned in reference paper 1 below)
    - Harvest WikiEdits from a publicly available wikipedia edits [like this](https://github.com/snukky/wikiedits).
    - Convert WikiText edits to <orig, edit> pairs using a custom script.
    - Filter out grammatical pairs using a ERRANT (last paper in the reference) based custom script.
- Download C4 based synthetic pairs available [here](https://github.com/google-research-datasets/C4_200M-synthetic-dataset-for-grammatical-error-correction).
- Download PIE synthetic pairs available [here](https://github.com/awasthiabhijeet/PIE).


## Note on commercial uses and release versions
- Any releases <= v1.0 is **NOT** intended for any commercial usage.
- Stable releases > v1.0

## Benchmark
TBD (I will benchmark grammformer models against the following publicy available models: 
- [salesken/grammar_correction](https://huggingface.co/salesken/grammar_correction), 
- [Grammarly GECTOR](https://github.com/grammarly/gector) 
- [flexudy/t5-small-wav2vec2-grammar-fixer](flexudy/t5-small-wav2vec2-grammar-fixer) shortly.

## References

- [Corpora Generation for Grammatical Error Correction](https://www.aclweb.org/anthology/N19-1333.pdf)
- [Improving Grammatical Error Correction with Machine Translation Pairs](https://www.aclweb.org/anthology/2020.findings-emnlp.30.pdf)
- [Improving Grammatical Error Correction Models with Purpose-Built Adversarial Examples](https://www.aclweb.org/anthology/2020.emnlp-main.228.pdf) 
- [MaskGEC: Improving Neural Grammatical Error Correction via Dynamic Masking](https://aaai.org/ojs/index.php/AAAI/article/view/5476#:~:text=By%20adding%20random%20masks%20to,correction%20model%20without%20additional%20data.) 
- [Synthetic Data Generation for Grammatical Error Correction with Tagged Corruption Models](https://www.aclweb.org/anthology/2021.bea-1.4/)
- [Grammatical Error Detection and Correction Using Tagger Disagreement](https://www.aclweb.org/anthology/W14-1706.pdf)
- [Automatic Annotation and Evaluation of Error Types for Grammatical Error Correction](https://aclanthology.org/P17-1074.pdf)
    

## How to cite Gramformer
TBD


