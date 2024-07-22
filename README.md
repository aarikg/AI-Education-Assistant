# AI Education Assistant

This project is an AI-powered education assistant that generates questions and answers on a given topic using the Google Generative AI model. The application is built using the Dash framework for an interactive web interface.

## Features

- Generate questions on a specified topic using AI.
- Display the generated question and allow the user to reveal the answer.
- Simple and clean user interface for easy interaction.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `dash` library
- `google-generativeai` library

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ai-education-assistant.git
    cd ai-education-assistant
    ```

2. **Install the required libraries:**
    ```bash
    pip install requests beautifulsoup4 dash google-generativeai
    ```

3. **Set up the Google Generative AI API:**
    - Obtain an API key from Google Generative AI.
    - Insert your API key in the code:
      ```python
      genai.configure(api_key="insert your key")
      ```

## Usage

1. **Run the application:**
    ```bash
    python app.py
    ```

2. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8050/`.

3. **Interact with the application:**
    - Enter a topic in the input field and click the "Ask Question" button to generate a question on the specified topic.
    - The generated question will be displayed.
    - Click the "Show Answer" button to reveal the answer to the generated question.

