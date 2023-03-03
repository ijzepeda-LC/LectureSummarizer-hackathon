# hackathon
## LCIT 
### Study assistant

TL;DR : An app that will record/upload an audio and get a transcription and a summary, also there is an option to translate it



This code implements a web application that allows users to summarize a lecture given by an audio file. It uses the Streamlit framework to build the interface and OpenAI's GPT-3 model to generate summaries.

The application allows users to either record a lecture or upload an audio file, and it supports four different language models to generate the summary. Users can select the model and language to use via radio buttons, and the selected options are stored in session state variables.

When a user records an audio file, the record_audio function is called, which records audio for a specified duration using the sounddevice and soundfile libraries, saves the file to disk, and sets the process_audio session state variable to True.

When a user uploads an audio file, the file is selected using a file uploader, and its data is stored in session state variables.

The get_summary function is used to generate the summary. It takes a prompt, a language, and a model as input and uses the OpenAI API to generate the summary. The prompt is constructed by adding the language and the input text to a template, and the model is selected based on the user's selection. The summary is returned as text and stored in a session state variable.

Finally, the save_pdf function is called to save the transcript and summary to a PDF file using the fpdf library. It retrieves the transcript and summary from the session state variables, formats them using the FPDF API, and saves them to a file.
