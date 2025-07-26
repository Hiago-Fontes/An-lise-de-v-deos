### This script automates the process of analyzing YouTube videos. It performs the following steps:

Downloads the audio from a YouTube video using yt-dlp.

Transcribes the audio locally using OpenAI's Whisper model, generating the spoken text from the video.

Automatically summarizes the transcription using the BART model (facebook/bart-large-cnn) from the Hugging Face Transformers library.

Displays both the full transcription and the summary of the video content in the terminal.
