[![PyPI - License](https://img.shields.io/hexpm/l/plug)](https://github.com/PrithivirajDamodaran/Gramformer/blob/main/LICENSE)
[![Visits Badge](https://badges.pufler.dev/visits/PrithivirajDamodaran/Parrot_Paraphraser)](https://badges.pufler.dev)

<p align="center">
    <img src="images/GLogo.png" width="35%" height="35%"/>
</p>

# Gramformer
Human and machine generated text often suffer from grammatical and/or typographical errors. It can be spelling, punctuation, grammatical or word choice errors. Gramformer is a library that exposes 3 seperate interfaces to a family of algorithms to **detect, highlight and correct** grammar errors. To make sure the corrections and highlights recommended are of high quality, it comes with a quality estimator. You can use Gramformer in one or more areas mentioned under the "use-cases" section below or any other usecase as you see fit. Gramformer stands on the shoulders of gaints, it combines some of the top notch researches in grammar correction. *Note: It works at **sentence levels** and has been trained on 128 length sentences, so not (yet) suitable for long prose or paragraphs (stay tuned for upcoming releases)*

## Table of contents
- [Usecases for Gramformer](#usecases-for-gramformer)
- [Installation](#installation)
- [Quick Start](#quick-start)
  * [Correction - [Available now]](#correction----available-now-)
  * [Challenge with generative models](#challenge-with-generative-models)
  * [Correction with QE estimator - [Coming soon !]](#correction-with-qe-estimator----coming-soon---)
  * [Highlight - [Coming soon !]](#highlight----coming-soon---)
  * [Detector - [Coming soon !]](#detector----coming-soon---)
- [Models](#models)
- [Dataset](#dataset)
- [Benchmark](#benchmark)
- [References](#references)
- [Citation](#citation)

## Usecases for Gramformer

**Area 1: Post-processing machine generated text**

Machine-Language generation is becoming mainstream so will post-processing machine generated text.

- Conditioned Text generation output(Text2Text generation).
    - NMT: Machine Translated output.
    - ASR or STT: Speech to text output.
    - HTR: Handwritten text recognition output.
    - Paraphrase generation output.
- Controlled Text generation output(Text generation with PPLM) **[TBD]**.
- Free-form text generation output(Text generation)**[TBD]**.

    
**Area 2:Human-In-The-Loop (HITL) text**
<ul>
    <li>Most Supervised NLU (Chatbots and Conversational) systems need humans/experts to enter or edit text that needs to be grammtical correct otherwise the quality of HITL data can degrade the model over a period of time </li>
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
pip install gramformer
```
## Quick Start

### Correcter - [Available now]
```python
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
```

```text
[Input]  Matt like fish
[Correction]  Matt likes fish
----------------------------------------------------------------------------------------------------
[Input]  the collection of letters was original used by the ancient Romans
[Correction]  The collection of letters was originally used by the ancient Romans.
----------------------------------------------------------------------------------------------------
[Input]  We enjoys horror movies
[Correction]  We enjoy horror movies
----------------------------------------------------------------------------------------------------
[Input]  Anna and Mike is going skiing
[Correction]  Anna and Mike are going skiing
----------------------------------------------------------------------------------------------------
[Input]  I walk to the store and I bought milk
[Correction]  I walked to the store and bought milk.
----------------------------------------------------------------------------------------------------
[Input]  We all eat the fish and then made dessert
[Correction]  We all ate the fish and then made dessert
----------------------------------------------------------------------------------------------------
[Input]  I will eat fish for dinner and drank milk
[Correction]  I'll eat fish for dinner and drink milk.
----------------------------------------------------------------------------------------------------
[Input]  what be the reason for everyone leave the company
[Correction]  what can be the reason for everyone to leave the company.
----------------------------------------------------------------------------------------------------
```

### Challenge with generative models
While Gramformer aims to post-process outputs from the generative models, Gramformer itself is a generative model. So the question arises, who will post-process the Gramformer outputs ? (I know, very meta :-)). In general all generative models have the tendency to generate spurious text sometimes, which we cannot control. So to make sure the gramformer grammar corrections (and highlights) are as accurate as possible, A quality estimator (QE) will be added. It can estimate a error correction quality score and use that as a filter on Top-N candidates to return only the best based on the score.

### Correcter with QE estimator - [Coming soon !]
```python
from gramformer import Gramformer
gf = Gramformer(models = 2, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
corrected_sentence = gf.correct(<your input sentence>, filter_by_qe=True, max_candidates=3)
```

### Highlighter - [Coming soon !]
```python
from gramformer import Gramformer
gf = Gramformer(models = 1, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
highlighted_sentence = gf.highlight(<your input sentence>)
```

```text
[Input]  Matt like fish
[Highlight]  Matt <e> like </e> fish
----------------------------------------------------------------------------------------------------
[Input]  the collection of letters was original used by the ancient Romans
[Highlight]  the collection of letters was <e> original used </e> by the ancient Romans
----------------------------------------------------------------------------------------------------
[Input]  We enjoys horror movies
[Highlight]  We <e> enjoys horror </e> movies
----------------------------------------------------------------------------------------------------
[Input]  Anna and Mike is going skiing
[Highlight]  Anna and Mike <e> is going </e> skiing
----------------------------------------------------------------------------------------------------
[Input]  I walk to the store and I bought milk
[Highlight]  I <e> walk to </e> the store and I bought milk
----------------------------------------------------------------------------------------------------
[Input]  We all eat the fish and then made dessert
[Highlight]  We all <e> eat the </e> fish and then made dessert
----------------------------------------------------------------------------------------------------
[Input]  I will eat fish for dinner and drank milk
[Highlight]  I will eat fish for dinner and <e> drank milk </e> 
----------------------------------------------------------------------------------------------------
[Input]  what be the reason for everyone leave the company
[Highlight]  <e> what be </e> the reason <e> for everyone </e> <e> leave the </e> company
----------------------------------------------------------------------------------------------------
[Input]  One of the most important issue is the lack of parking spaces at the local mall.
[Highlight]  One of the most important <e> issue is </e> the lack of parking spaces at the local mall.
----------------------------------------------------------------------------------------------------
[Input]  The survey we performed recently showed that most of customers are satisfied.
[Highlight]  The survey we performed recently showed that most <e> of customers </e> are satisfied.
----------------------------------------------------------------------------------------------------
[Input]  I’ve loved classical music ever since I was child.
[Highlight]  I’ve loved classical music ever since I <e> was child </e>.
----------------------------------------------------------------------------------------------------
```

### Detector - [Coming soon !]
```python
from gramformer import Gramformer
gf = Gramformer(models = 0, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
grammar_fluency_score = gf.detect(<your input sentence>)
```

## Models

|      Model          |Type                          |Return                         |status|
|----------------|-------------------------------|-----------------------------|-----------------------------|
|prithivida/grammar_error_detector |Classifier |Label                             |TBD (prithivida/parrot_fluency_on_BERT can be repurposed here, but I would recommend you wait :-))|
|prithivida/grammar_error_highlighter|Seq2Seq    |Grammar errors enclosed in ``` <e> and </e> ``` |Beta |
|prithivida/grammar_error_correcter  |Seq2Seq    |The corrected sentence              |Beta|


## Dataset
- First idea is to generate the dataset using the techniques mentioned in the first paper highlighted in reference section. You can use the technique on anyone of the publicy available [wikipedia edits datasets](https://snap.stanford.edu/data/wiki-meta.html#:~:text=Dataset%20information,Parsed%20Wikipedia%20edit%20history). Write some rules to filter only the grammatical edits, do some cleanup and thats it Bob's your uncle :-).
- Second and possibly [very complicated and $$$ way to get some 200M synthetic sentences](https://github.com/google-research-datasets/C4_200M-synthetic-dataset-for-grammatical-error-correction). This is based on the last paper under references section. Not recommended but by all means knock yourself out if you are interested :-)
- Third source is to repurpose the [GEC Task data](https://www.cl.cam.ac.uk/research/nl/bea2019st/)
- I combined sources 1 and 3 to get my training data (still working on source 2, will keep you posted)
- I ended up with ~1M records and after some heurtistics based filtering amounted to ~1/2M records.
- It took ~12 hours to train each of the above models.

## Benchmark
TBD (I will benchmark grammformer models against the following publicy available models: [salesken/grammar_correction](https://huggingface.co/salesken/grammar_correction) and [flexudy/t5-small-wav2vec2-grammar-fixer](flexudy/t5-small-wav2vec2-grammar-fixer) shortly.


## References

- [Corpora Generation for Grammatical Error Correction](https://www.aclweb.org/anthology/N19-1333.pdf)
- [Improving Grammatical Error Correction with Machine Translation Pairs](https://www.aclweb.org/anthology/2020.findings-emnlp.30.pdf)
- [Improving Grammatical Error Correction Models with Purpose-Built Adversarial Examples](https://www.aclweb.org/anthology/2020.emnlp-main.228.pdf) 
- [MaskGEC: Improving Neural Grammatical Error Correction via Dynamic Masking](https://aaai.org/ojs/index.php/AAAI/article/view/5476#:~:text=By%20adding%20random%20masks%20to,correction%20model%20without%20additional%20data.) 
- [Synthetic Data Generation for Grammatical Error Correction with Tagged Corruption Models](https://www.aclweb.org/anthology/2021.bea-1.4/)

## Citation
TBD


