from annotated_text import annotated_text
from bs4 import BeautifulSoup
from gramformer import Gramformer
import streamlit as st
import pandas as pd
import torch
import math
import re

def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
set_seed(1212)

class GramformerDemo:

    def __init__(self):
        st.set_page_config(
            page_title="Gramformer Demo",
            initial_sidebar_state="expanded",
            layout="wide"
            )
        self.model_map = {
            'Corrector': 1,
            'Detector - coming soon': 2
            }
        self.examples = [
            "what be the reason for everyone leave the comapny",
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
            ]

    @st.cache(show_spinner=False, suppress_st_warning=True, allow_output_mutation=True)
    def load_gf(self, model: int):
        """
            Load Gramformer model
        """
        gf = Gramformer(models=model, use_gpu=False)
        return gf
    
    def show_highlights(self, gf: object, input_text: str, corrected_sentence: str):
        """
            To show highlights
        """
        try:
            strikeout = lambda x: '\u0336'.join(x) + '\u0336'
            highlight_text = gf.highlight(input_text, corrected_sentence)
            color_map = {'d':'#faa', 'a':'#afa', 'c':'#fea'}
            tokens = re.split(r'(<[dac]\s.*?<\/[dac]>)', highlight_text)
            annotations = []
            for token in tokens:
                soup = BeautifulSoup(token, 'html.parser')
                tags = soup.findAll()
                if tags:
                    _tag = tags[0].name
                    _type = tags[0]['type']
                    _text = tags[0]['edit']
                    _color = color_map[_tag]

                    if _tag == 'd':
                        _text = strikeout(tags[0].text)

                    annotations.append((_text, _type, _color))
                else:
                    annotations.append(token)
            args = {
                'height': 45*(math.ceil(len(highlight_text)/100)),
                'scrolling': True
            }
            annotated_text(*annotations, **args)
        except Exception as e:
            st.error('Some error occured!')
            st.stop()
    
    def show_edits(self, gf: object, input_text: str, corrected_sentence: str):
        """
            To show edits
        """
        try:
            edits = gf.get_edits(input_text, corrected_sentence)
            df = pd.DataFrame(edits, columns=['type','original word', 'original start', 'original end', 'correct word', 'correct start', 'correct end'])
            df = df.set_index('type')
            st.table(df)
        except Exception as e:
            st.error('Some error occured!')
            st.stop()
    
    def main(self):
        github_repo = 'https://github.com/PrithivirajDamodaran/Gramformer'
        st.title("Gramformer")
        st.write(f'GitHub Link - [{github_repo}]({github_repo})')
        st.markdown('A framework for detecting, highlighting and correcting grammatical errors on natural language text')

        model_type = st.sidebar.selectbox(
            label='Choose Model',
            options=list(self.model_map.keys())
            )
        if model_type == 'Corrector':
            max_candidates = st.sidebar.number_input(
                label='Max candidates',
                min_value=1,
                max_value=10,
                value=1
                )
        else:
            # NOTE: 
            st.warning('TO BE IMPLEMENTED !!')
            st.stop()

        with st.spinner('Loading model..'):
            gf = self.load_gf(self.model_map[model_type])
    
        input_text = st.selectbox(
            label="Choose an example",
            options=self.examples
            )
        input_text = st.text_input(
            label="Input text",
            value=input_text
        )

        if input_text.strip():
            results = gf.correct(input_text, max_candidates=max_candidates)
            corrected_sentence, score = results[0]
            st.markdown(f'#### Output:')
            st.write('')
            st.success(corrected_sentence)
            exp1 = st.beta_expander(label='Show highlights', expanded=True)
            with exp1:
                self.show_highlights(gf, input_text, corrected_sentence)
            exp2 = st.beta_expander(label='Show edits')
            with exp2:
                self.show_edits(gf, input_text, corrected_sentence)

        else:
            st.warning("Please select/enter text to proceed")
        
if __name__ == "__main__":
    obj = GramformerDemo()
    obj.main()