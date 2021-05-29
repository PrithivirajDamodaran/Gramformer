[![PyPI - License](https://img.shields.io/hexpm/l/plug)](https://github.com/PrithivirajDamodaran/Parrot/blob/main/LICENSE)
[![Visits Badge](https://badges.pufler.dev/visits/PrithivirajDamodaran/Parrot_Paraphraser)](https://badges.pufler.dev)

<p align="center">
    <img src="images/GLogo.png" width="35%" height="35%"/>
</p>

# Gramformer
Text, whether it is human generated or machine generated, suffers from grammatical and typograhical errors. It can be spelling, punctuation, grammatical or word choice errors. Gramformer is a family of algorithms which can help you detect, highlight and correct above errors.

## Quick Start
```python
from gramformer import Gramformer
gf = Gramformer(models = [], use_gpu=False)
corrected_sentence = gf.correct("you input sentence")
```

## Examples

## Applications of Gramformer
Gramformer exposes 3 seperate interfaces to detect, highlight or correct grammar errors and you can use them in one or more of the following areas:

### Use-cases:

**Machine-Language generation is becoming mainstream, so post processing for model generated text will come in handy.**

<ul>
    <li>NMT: Machine Translated text.</li>
    <li>ASR or STT: Speech to text.</li>
    <li>HTR: Handwritten text recognition.</li>
    <li>Paraphrase generation.</li>
    <li>Conditioned Text generation (Text2Text generation).</li>
    <li>Controlled Text generation (Text generation with PPLM).</li>
    <li>Free-form text generation (Text generation).</li>
</ul>
    
**Assisted writing for humans**
<ul>
    <li>Integrating into custom Text editors of your Apps.</li>
</ul>    

**Platform integration**
<ul>
<li>Today for authoring social contents (Post or Comments) platforms don’t have a lot of grammatical safety nets. The onus is on the author to install tools like grammarly to proof read. Instead, platforms could do an automatic style and grammar check and correct without altering the meaning or intent.
    Post-processing for automatically extracted/scraped text.</li>
</ul>    


## Citations

## References

[Corpora Generation for Grammatical Error Correction](https://www.aclweb.org/anthology/N19-1333.pdf)
[Improving Grammatical Error Correction with Machine Translation Pairs](https://www.aclweb.org/anthology/2020.findings-emnlp.30.pdf)
[Improving Grammatical Error Correction Models with Purpose-Built Adversarial Examples](https://www.aclweb.org/anthology/2020.emnlp-main.228.pdf) 
[MaskGEC: Improving Neural Grammatical Error Correction via Dynamic Masking](https://aaai.org/ojs/index.php/AAAI/article/view/5476#:~:text=By%20adding%20random%20masks%20to,correction%20model%20without%20additional%20data.) 




