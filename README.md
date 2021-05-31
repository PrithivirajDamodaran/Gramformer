[![PyPI - License](https://img.shields.io/hexpm/l/plug)](https://github.com/PrithivirajDamodaran/Parrot/blob/main/LICENSE)
[![Visits Badge](https://badges.pufler.dev/visits/PrithivirajDamodaran/Parrot_Paraphraser)](https://badges.pufler.dev)

<p align="center">
    <img src="images/GLogo.png" width="35%" height="35%"/>
</p>

# Gramformer
Human and machine generated text often suffers from grammatical and/or typograhical errors. It can be spelling, punctuation, grammatical or word choice errors. Gramformer is a library that exposes 3 seperate interfaces to a family of algorithms to **detect, highlight and correct** grammar errors. You can use them in one or more areas mentioned under the "use-cases" section below or as you see fit.

## Table of contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Examples](#examples)
- [Usecases for Gramformer](#usecases-for-gramformer)
- [References](#references)
- [Citations](#citations)

## Installation
```python
pip install gramformer
```
## Quick Start
```python
from gramformer import Gramformer
gf = Gramformer(models = 2, use_gpu=False) # 0=detector, 1=highlighter, 2=corrector, 3=all 
corrected_sentence = gf.correct("you input sentence")
```

## Examples

## Usecases for Gramformer

**Area 1: Post-processing machine generated text**

Machine-Language generation is becoming mainstream so will post-processing

<ul>
    <li>NMT: Machine Translated output.</li>
    <li>ASR or STT: Speech to text output.</li>
    <li>HTR: Handwritten text recognition output.</li>
    <li>Paraphrase generation output.</li>
    <li>Conditioned Text generation output(Text2Text generation).</li>
    <li>Controlled Text generation output(Text generation with PPLM).</li>
    <li>Free-form text generation output(Text generation).</li>
</ul>
    
**Area 2:Human-In-The-Loop text
<ul>
    <li>Most Superised NLU (Chatbots and Conversational) systems need humans/experts to enter or edit text which need grammtical corrections</li>
</ul>    
    
**Area 3:Assisted writing for humans**
<ul>
    <li>Integrating into custom Text editors of your Apps. (A Poor man's grammarly, if you will) </li>
</ul>    

**Area 4:Custom Platform integration**

As of today grammatical safety nets for authoring social contents (Post or Comments) or text in messaging platforms is very little (word level correction) or non-existent.The onus is on the author to install tools like grammarly to proof read. 

<ul>
    <li> Messaging platforms can highlight / correct grammtical errors automatically without altering the meaning or intent.</li>
    <li> Social platforms can highlight / correct grammtical errors automatically without altering the meaning or intent.</li>
</ul>    

## Models

|      Model          |Type                          |Return                         |status|
|----------------|-------------------------------|-----------------------------|-----------------------------|
|prithivida/grammar_error_detector |Classifier |Label                             |TBD (prithivida/parrot_fluency_on_BERT can be repurposed here, but I would recommend you wait :-))|
|prithivida/grammar_error_highlighter|Seq2Seq    |The input with grammar errors enclosed in delimiters estart and eend |Available in HF|
|prithivida/grammar_error_correcter  |Seq2Seq    |The corrected sentence              |Available in HF|


## Dataset
The dataset was generated using the techniques mentioned in the first paper highlighted in reference section. 

## References

- [Corpora Generation for Grammatical Error Correction](https://www.aclweb.org/anthology/N19-1333.pdf)
- [Improving Grammatical Error Correction with Machine Translation Pairs](https://www.aclweb.org/anthology/2020.findings-emnlp.30.pdf)
- [Improving Grammatical Error Correction Models with Purpose-Built Adversarial Examples](https://www.aclweb.org/anthology/2020.emnlp-main.228.pdf) 
- [MaskGEC: Improving Neural Grammatical Error Correction via Dynamic Masking](https://aaai.org/ojs/index.php/AAAI/article/view/5476#:~:text=By%20adding%20random%20masks%20to,correction%20model%20without%20additional%20data.) 

## Citations
TBD


