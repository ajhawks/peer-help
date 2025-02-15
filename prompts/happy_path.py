import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def happy_path_model(string):
    """ To evaluate a product's intended happy path

    Args:
        string (str): section of text extracted from Notion

    Returns:
        str: GPT's evaluation of the text
    """
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = f"The following paragraph is the happy path section of a product specification. Evaluate how well the happy path has been written and give specific feedback on what can be improved. Write several in-depth sentences.\n{string}",
            temperature = 0.1,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return f"happy_path: {e}" # placeholder for now

# for internal testing

""" TEST_INPUT = "1. Prompt-engineering GPT-3 to numerically evaluate sections to determine the prompt that is given to the GPT-3 model for feedback generation.\
2. Prompt-engineering GPT-3 to generate feedback based on numerical scores given by the scoring method.\
3. Extracting and parsing text from Notion product specs into individual sections (problem statement, solution, etc.)\
4. Backend to feed sections to the scoring method to the GPT-3 model using a bot command and generating an embed."

print(happy_path_model(TEST_INPUT)) """
