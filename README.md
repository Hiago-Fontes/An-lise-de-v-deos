### Este script automatiza o processo de análise de vídeos do YouTube. Ele realiza as seguintes etapas:

1. Baixa o áudio de um vídeo do YouTube usando o yt-dlp.

2. Transcreve o áudio localmente usando o modelo Whisper da OpenAI, gerando o texto falado do vídeo.

3. Resume automaticamente a transcrição usando o modelo BART (facebook/bart-large-cnn) da biblioteca Hugging Face Transformers.

4. Exibe no terminal tanto a transcrição completa quanto o resumo do conteúdo do vídeo.
