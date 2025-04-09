# Intro to Gemini 2.5 Pro

[Gemini 2.5 Pro](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) is Google's strongest model for coding and world knowledge.

With the 2.5 series, the Gemini models are now hybrid reasoning models! Gemini 2.5 Pro can apply an extended amount of thinking across tasks, and use tools in order to maximize response accuracy.

Gemini 2.5 Pro is:

+ A significant improvement from previous models across capabilities including coding, reasoning, and multimodality
+ Industry-leading in reasoning with state of the art performance in Math & STEM benchmarks
+ An amazing model for code, with particularly strong web development
+ Particularly good for complex prompts, while still being well rounded, including #1 on LMSys

## Objectives
In this tutorial, you will learn how to use the Gemini API and the Google Gen AI SDK for Python with the Gemini 2.5 Pro model.

You will complete the following tasks:

+ Generate text from text prompts
    + Generate streaming text
    + Start multi-turn chats
    + Use asynchronous methods

+ Configure model parameters
+ Set system instructions
+ Use safety filters
+ Use controlled generation
+ Count tokens
+ Process multimodal (audio, code, documents, images, video) data
+ Use automatic and manual function calling
+ Code execution
+ Thinking mode examples

## Getting Started
Use your preferred python environment to get started. You can use your local development environment, use [Colab](https://colab.google/), use [Google Cloud Shell](https://cloud.google.com/shell/docs), or use [Cloud Workstations](https://cloud.google.com/workstations?hl=en).  

For ease of use, we will use the Cloud Shell environment for this tutorial. Please follow the instructions in [Getting Started with Cloud Shell and gcloud](https://codelabs.developers.google.com/codelabs/cloud-shell#0) to activate your Cloud Shell.

1. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Google Gen AI SDK for Python
```bash
pip install google-genai
```

3. Setup application default credentials
[Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) allows you to invoke Google Cloud APIs from a local development environment. 

Follow the instructions in the link, or use the following commands for a quick start. 

```bash
gcloud init
gcloud auth application-default login
```



