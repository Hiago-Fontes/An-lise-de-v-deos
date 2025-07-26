### This script automates the process of analyzing YouTube videos. It performs the following steps:

1. Downloads the audio from a YouTube video using yt-dlp.

2. Transcribes the audio locally using OpenAI's Whisper model, generating the spoken text from the video.

3. Automatically summarizes the transcription using the BART model (facebook/bart-large-cnn) from the Hugging Face Transformers library.

4. Displays both the full transcription and the summary of the video content in the terminal.
