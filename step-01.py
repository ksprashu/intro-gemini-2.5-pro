# This is a simple program that invokes the gemini model and returns a response

# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gradio as gr
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Create the Gen AI client
# This uses the environment vars from .env file to initialise the client
# The GOOGLE_GENAI_USE_VERTEXAI value specifies that we'll create a Vertex AI client  
client = genai.Client()

def generate_text(prompt):
    """
    Generates text based on the given prompt using the Gemini model.

    Args:
        prompt (str): The text prompt to generate content from.

    Returns:
        str: The generated text, or an error message if something went wrong.
    """
    if not prompt:
        return "Please enter a prompt."
    try:
        response = client.models.generate_content(
            model=os.environ.get("GEMINI_MODEL"), 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"


# Gradio interface
demo = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs=gr.Textbox(lines=10, label="Generated Text"),
    title="Gemini 2.5 Pro Demo",
    description="Enter a prompt and click 'Submit' to generate text using the Gemini 2.5 Pro model.",
    flagging_options=None
)

if __name__ == "__main__":
    demo.launch()
