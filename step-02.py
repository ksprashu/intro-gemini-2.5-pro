# This is a program that demonstrates streaming response from gemini

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

def generate_text_streaming(prompt, history=[]):
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
        full_text = ""

        response_stream = client.models.generate_content_stream(
            model=os.environ.get("GEMINI_MODEL"), 
            contents=prompt
        )

        for chunk in response_stream:
            print(chunk.text, end="")
            full_text += chunk.text
            yield full_text
    except Exception as e:
        yield f"An error occurred: {e}"


# Define some example prompts
example_prompts = [
    ["Write a story about a robot who learns to paint."],
    ["Explain the history of the internet, starting from ARPANET to the modern web, covering key milestones, technologies, and societal impacts."],
    ["Create a plot for a Sci-Fi movie where AI and Humans defeat an alien attack on Earth"]
]

# Gradio interface
demo = gr.Interface(
    fn=generate_text_streaming,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here which will generate a long response..."),
    outputs=gr.Textbox(lines=10, label="Generated Text"),
    title="Gemini 2.5 Pro Demo - Streaming Response",
    description="Enter a prompt and click 'Submit' to generate text using the Gemini 2.5 Pro model.",
    examples=example_prompts,    
    flagging_mode="never",
)


if __name__ == "__main__":
    demo.launch(debug=True)
