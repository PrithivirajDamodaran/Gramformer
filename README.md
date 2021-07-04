[![PyPI - License](https://img.shields.io/hexpm/l/plug)](https://github.com/PrithivirajDamodaran/Gramformer/blob/main/LICENSE)
[![Visits Badge](https://badges.pufler.dev/visits/PrithivirajDamodaran/Gramformer)](https://badges.pufler.dev)

<p align="center">
    <img src="images/GLogo.png" width="35%" height="35%"/>
</p>

# Gramformer
Human and machine generated text often suffer from grammatical and/or typographical errors. It can be spelling, punctuation, grammatical or word choice errors. Gramformer is a library that exposes 3 seperate interfaces to a family of algorithms to **detect, highlight and correct** grammar errors. To make sure the corrections and highlights recommended are of high quality, it comes with a quality estimator. You can use Gramformer in one or more areas mentioned under the "use-cases" section below or any other usecase as you see fit. Gramformer stands on the shoulders of giants, it combines some of the top notch researches in grammar correction. *Note: It works at **sentence levels** and has been trained on 128 length sentences, so not (yet) suitable for long prose or paragraphs (stay tuned for upcoming releases)*

## Table of contents
- [Usecases for Gramformer](#usecases-for-gramformer)
- [Installation](#installation)
- [Quick Start](#quick-start)
  * [Correcter - [Available now]](#correcter----available-now-)
  * [Challenge with generative models](#challenge-with-generative-models)
  * [Correcter with QE estimator - [Coming soon !]](#correcter-with-qe-estimator----coming-soon---)
  * [Get Edits - [Coming soon !]](#get-edits----coming-soon---)
  * [Highlighter - [Coming soon !]](#highlighter----coming-soon---)
  * [Detector - [Coming soon !]](#detector----coming-soon---)
- [Models](#models)
- [Dataset](#dataset)
- [Note on commercial uses and release versions](#note-on-commercial-uses-and-release-versions)
- [Benchmark](#benchmark)
- [References](#references)
- [Citation](#citation)


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
pip3 install -U git+https://github.com/PrithivirajDamodaran/Gramformer.git
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
    "He are moving here.",
    "the collection of letters was original used by the ancient Romans",
    "We enjoys horror movies",
    "Anna and Mike is going skiing",
    "I will eat fish for dinner and drink milk",
    "what be the reason for everyone leave the company",
]   

for influent_sentence in influent_sentences:
    corrected_sentence = gf.correct(influent_sentence)
    print("[Input] ", influent_sentence)
    print("[Correction] ",corrected_sentence[0])
    print("-" *100)
```

```text
[Input]  He are moving here.
[Correction]  He is moving here.
----------------------------------------------------------------------------------------------------
[Input]  the collection of letters was original used by the ancient Romans
[Correction]  the collection of letters originally used by the ancient Romans.
----------------------------------------------------------------------------------------------------
[Input]  We enjoys horror movies
[Correction]  We enjoy horror movies.
----------------------------------------------------------------------------------------------------
[Input]  Anna and Mike is going skiing
[Correction]  Anna and Mike are skiing.
----------------------------------------------------------------------------------------------------
[Input]  I will eat fish for dinner and drank milk
[Correction]  I will eat fish for dinner and drank milk.
----------------------------------------------------------------------------------------------------
[Input]  what be the reason for everyone leave the company
[Correction]  what is the reason for everyone leaving the company?
----------------------------------------------------------------------------------------------------
```

### Challenge with generative models
While Gramformer aims to post-process outputs from the generative models, Gramformer itself is a generative model. So the question arises, who will post-process the Gramformer outputs ? (I know, very meta :-)). In general all generative models have the tendency to generate spurious text sometimes, which we cannot control. So to make sure the gramformer grammar corrections (and highlights) are as accurate as possible, A quality estimator (QE) will be added. It can estimate a error correction quality score and use that as a filter on Top-N candidates to return only the best based on the score.

### Correcter with QE estimator - [Available now]
Update: QE estimator is now built-in, gf.correct itself generates top N candidates, scores, ranks and returns the top ranked result.    
<s> 
```python 
from gramformer import Gramformer
gf = Gramformer(models = 2, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
corrected_sentence = gf.correct(<your input sentence>, filter_by_quality=True, max_candidates=3) 
```
</s>  


### Get Edits - [Coming soon !]
```python
from gramformer import Gramformer
gf = Gramformer(models = 1, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
edits = gf.get_edits("Norton like to fishing ")
```

```
[('OTHER', 'like', 1, 2, 'likes', 1, 2), ('PREP', 'to', 2, 3, '', 2, 2), ('PUNCT', '', 4, 4, '.', 3, 4)]
```


### Highlighter - [Coming soon !]
```python
from gramformer import Gramformer
gf = Gramformer(models = 1, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
highlighted_sentence = gf.highlight(<your input sentence>)
```

```text
[Input]  Norton like fish
[Highlight] Norton <c type=OTHER edit=likes>like</c> <d type=PREP edit=''>to</d> <a type=PUNCT edit=.>fishing</a>
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
|prithivida/grammar_error_detector |Classifier |Label                             |WIP (Reuse prithivida/parrot_fluency_on_BERT ? but I would'd say you wait :-))|
|<s>prithivida/grammar_error_highlighter</s>|Seq2Seq    |Grammar errors enclosed in ``` <e> and </e> ``` |<s>WIP</s> Turns out there is no need for a model  |
|[<s>prithivida/grammar_error_correcter</s>](https://huggingface.co/prithivida/grammar_error_correcter)|Seq2Seq    |The corrected sentence              |Beta / Pre-release (**Not available anymore**)|
|[prithivida/grammar_error_correcter_v1](https://huggingface.co/prithivida/grammar_error_correcter_v1)  |Seq2Seq    |The corrected sentence              |Stable|


## Dataset
- First idea is to generate the dataset using the techniques mentioned in the first paper highlighted in reference section. You can use the technique on anyone of the publicy available [wikipedia edits datasets](https://github.com/snukky/wikiedits). Write some rules to filter only the grammatical edits, do some cleanup and thats it Bob's your uncle :-).
- Second and possibly [very complicated and $$$ way to get some 200M synthetic sentences](https://github.com/google-research-datasets/C4_200M-synthetic-dataset-for-grammatical-error-correction). This is based on the last paper under references section. Not recommended but by all means knock yourself out if you are interested :-) (Update: I got my hands on all the 200M of them) - Available under CC-BY-4.0 License 
- Third source is to repurpose the [GEC Task data](https://www.cl.cam.ac.uk/research/nl/bea2019st/) 
- Fourth source is from the paper "Parallel Iterative Edit Models for Local Sequence Transduction" (EMNLP-IJCNLP 2019) - Available under  MIT License
- For the beta / pre-release experiments, I generated error edit pairs from 1st source and on top of that used W&I+LOCNESS from the 3rd source to filter the pairs with grammatical edits only. W&I+LOCNESS was used to harvest different patterns of grammar errors and is available as a [Huggingface dataset](https://huggingface.co/datasets/wi_locness).
- I ended up with ~1M records and after some heurtistics based filtering amounted to ~1/2M records.
- [Update] In the stable release I am using slices of data from sources 1, 2 and 4 listed above. Because sources 2 and 4 have large volume/variety and doesn't need expensive filtering process like in the case of source 1. (The stable model is the one in the above table with a suffix v1). 
- In the stable release the wiki edit pairs from source 1 are filtered using the ERRANT tool. The source sentences that yielded a **noop** on the ERRANT output i.e. the m2 format are filtered out.


## Note on commercial uses and release versions
- Any releases <= v1.0 is **NOT** intended for any commercial usage.
- Stable releases > v1.0 and current release is v1.2

## Benchmark
TBD (I will benchmark grammformer models against the following publicy available models: [salesken/grammar_correction](https://huggingface.co/salesken/grammar_correction), [Grammarly GECTOR](https://github.com/grammarly/gector) and [flexudy/t5-small-wav2vec2-grammar-fixer](flexudy/t5-small-wav2vec2-grammar-fixer) shortly.

## References

- [Corpora Generation for Grammatical Error Correction](https://www.aclweb.org/anthology/N19-1333.pdf)
- [Improving Grammatical Error Correction with Machine Translation Pairs](https://www.aclweb.org/anthology/2020.findings-emnlp.30.pdf)
- [Improving Grammatical Error Correction Models with Purpose-Built Adversarial Examples](https://www.aclweb.org/anthology/2020.emnlp-main.228.pdf) 
- [MaskGEC: Improving Neural Grammatical Error Correction via Dynamic Masking](https://aaai.org/ojs/index.php/AAAI/article/view/5476#:~:text=By%20adding%20random%20masks%20to,correction%20model%20without%20additional%20data.) 
- [Synthetic Data Generation for Grammatical Error Correction with Tagged Corruption Models](https://www.aclweb.org/anthology/2021.bea-1.4/)
- [Grammatical Error Detection and Correction Using Tagger Disagreement](https://www.aclweb.org/anthology/W14-1706.pdf)

## Citation
TBD


