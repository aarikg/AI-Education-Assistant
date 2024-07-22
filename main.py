import pathlib
import textwrap

import google.generativeai as genai
#from google.colab import userdata
from IPython.display import display
from IPython.display import Markdown
from dash import Dash, html, dcc, Input, Output, dash
import time
genai.configure(api_key="insert your key")
model = genai.GenerativeModel('gemini-pro')

def generate_question(topic):
    question = model.generate_content(f"You are now my education assistant. Please give me a question on the topic of {topic}. No weird (markdown,etc) syntax, only plaintext." )
    time.sleep(2)
    answer = model.generate_content(f"Answer this question and include an explanation which will be in brackets (no \\n). No weird (markdown,etc) syntax, only plaintext.: {question.text}")
    #print(answer.text)
    #print(answer.text)
    return [question.text, answer.text]

app = Dash(__name__, external_stylesheets=['styles.css'])

app.layout = html.Div([
    html.H1(children='AI Education Assistant'),
    dcc.Input(id='topic-input', type='text', placeholder='Enter a topic...'),
    html.Button('Ask Question', id='ask-button', n_clicks=0),
    html.Div(id='question-area', children='Question:'), 
    html.Div(id='answer-area', children='', style={'display': 'none'}),  # Initially hide answer
    html.Button('Show Answer', id='show-answer-button', n_clicks=0)
])


@app.callback(
    Output('question-area', 'children'),
    Output('answer-area', 'children'),
    Output('topic-input', 'value'),  # Clear the input
    Output('answer-area', 'style'),  # Control visibility of answer
    Input('ask-button', 'n_clicks'),
    Input('show-answer-button', 'n_clicks'),
    Input('topic-input', 'value')
)
def process_question(ask_clicks, show_clicks, topic):
    if ask_clicks > 0 and topic:
        generation = generate_question(topic)
        #print(generation)
        return f'Question: {generation[0]}', f'Answer: {generation[1]}', '', {'display': 'none'}  # Hide answer initially
    elif show_clicks > 0:  # Check if answer exists
        return dash.no_update, dash.no_update, dash.no_update, {'display': 'block'}  # Show answer
    else:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update

if __name__ == '__main__':
    app.run(debug=True)





