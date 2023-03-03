# hackathon
## LCIT 
### Study assistant

TL;DR : An app that will record/upload an audio and get a transcription and a summary, also there is an option to translate it

![alt text](https://github.com/ijzepeda-LC/hackathon/raw/master/bot.jpeg)

# ============================


Introducing a groundbreaking new tool in the world of education - our Python-based web application that allows users to summarize lectures using cutting-edge technology. With four different parts 
- Whisper for speech-to-text, 
GPT for summarization,  (Generative Pre-trained Transformer)
Streamlit for frontend, and
Telegram integration for a chatbot - 
this program is a one-of-a-kind solution for anyone who wants to save time and effort while still retaining valuable information.

The application offers flexibility, allowing users to either record a lecture or upload an audio file, and supports four different language models for generating the summary. The user-friendly interface makes it easy to select the preferred model and language via radio buttons, which are stored in session state variables for easy retrieval.

Our program uses the Whisper libraries for recording and processing audio, and the OpenAI API for generating the summary. This ensures that the summary is accurate, concise, and perfectly suited to the user's needs.

One of the most exciting features of our program is the ability to save the transcript and summary in PDF format, making it easy to share and review the information at a later time.

We've put a lot of hard work into this program, and we're confident that it will assist the way people learn and retain information. Try it out for yourself and see how it can benefit you!


# ============================

This code implements a web application that allows users to summarize a lecture given by an audio file. It uses the Streamlit framework to build the interface and OpenAI's GPT-3 model to generate summaries.

The application allows users to either record a lecture or upload an audio file, and it supports four different language models to generate the summary. Users can select the model and language to use via radio buttons, and the selected options are stored in session state variables.

When a user records an audio file, the record_audio function is called, which records audio for a specified duration using the sounddevice and soundfile libraries, saves the file to disk, and sets the process_audio session state variable to True.

When a user uploads an audio file, the file is selected using a file uploader, and its data is stored in session state variables.

The get_summary function is used to generate the summary. It takes a prompt, a language, and a model as input and uses the OpenAI API to generate the summary. The prompt is constructed by adding the language and the input text to a template, and the model is selected based on the user's selection. The summary is returned as text and stored in a session state variable.

Finally, the save_pdf function is called to save the transcript and summary to a PDF file using the fpdf library. It retrieves the transcript and summary from the session state variables, formats them using the FPDF API, and saves them to a file.
