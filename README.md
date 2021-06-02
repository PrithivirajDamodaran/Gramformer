[![PyPI - License](https://img.shields.io/hexpm/l/plug)](https://github.com/PrithivirajDamodaran/Gramformer/blob/main/LICENSE)
[![Visits Badge](https://badges.pufler.dev/visits/PrithivirajDamodaran/Parrot_Paraphraser)](https://badges.pufler.dev)

<p align="center">
    <img src="images/GLogo.png" width="35%" height="35%"/>
</p>

# Gramformer
Human and machine generated text often suffer from grammatical and/or typographical errors. It can be spelling, punctuation, grammatical or word choice errors. Gramformer is a library that exposes 3 seperate interfaces to a family of algorithms to **detect, highlight and correct** grammar errors. You can use them in one or more areas mentioned under the "use-cases" section below or as you see fit. *Note: It works at **sentence levels** and has been trained on 128 length sentences, so not suitable for long prose or paragraphs, YET (stay tuned for upcomign releases)*

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

### Correction - [Available now]
```python
from gramformer import Gramformer
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
```

### Challenge with generative models
While as proposed Gramformer can help post-process outputs from the generative models, Gramformer by in itself a generative model (I know very meta :-)). All generative models have the tendency to generate spurious text sometimes which we cannot control. So to make sure the gramformer grammar corrections (highlight and detection) are as accurate as possible, It will soon come with a quality estimator (QE) to filter the Top-N candidates and return only the best based on a QE score.

### Correction with QE estimator - [Coming soon !]
```python
from gramformer import Gramformer
gf = Gramformer(models = 2, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
corrected_sentence = gf.correct(<your influent_sentence>)
```

### Highlight - [Coming soon !]
```python
from gramformer import Gramformer
gf = Gramformer(models = 1, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
highlighted_sentence = gf.highlight("your input sentence")
```
### Detector - [Coming soon !]
```python
from gramformer import Gramformer
gf = Gramformer(models = 0, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
grammar_fluency_score = gf.detect("your input sentence")
```

## Models

|      Model          |Type                          |Return                         |status|
|----------------|-------------------------------|-----------------------------|-----------------------------|
|prithivida/grammar_error_detector |Classifier |Label                             |TBD (prithivida/parrot_fluency_on_BERT can be repurposed here, but I would recommend you wait :-))|
|prithivida/grammar_error_highlighter|Seq2Seq    |Grammar errors enclosed in ``` <e> and </e> ``` |Beta |
|prithivida/grammar_error_correcter  |Seq2Seq    |The corrected sentence              |Stable|


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


