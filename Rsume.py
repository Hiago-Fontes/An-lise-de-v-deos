import subprocess
import os

try:
    import whisper
except ImportError:
    print("O pacote 'whisper' não está instalado. Instale com: pip install openai-whisper")
    exit(1)

try:
    from transformers import pipeline
except ImportError:
    print("O pacote 'transformers' não está instalado. Instale com: pip install transformers torch")
    exit(1)

def baixar_audio(url, saida_mp3):
    # Tenta usar yt-dlp diretamente, se não funcionar, usa via python -m yt_dlp
    comando = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "-o", saida_mp3,
        url
    ]
    try:
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if resultado.returncode != 0:
            raise FileNotFoundError
    except FileNotFoundError:
        # Tenta via python -m yt_dlp se yt-dlp não estiver no PATH
        comando_py = [
            "python", "-m", "yt_dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", saida_mp3,
            url
        ]
        resultado = subprocess.run(comando_py, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if resultado.returncode != 0:
            print("Erro ao baixar áudio:")
            print(resultado.stderr.decode())
            raise RuntimeError("Erro ao baixar áudio")

def transcrever_local(caminho_audio):
    if not os.path.exists(caminho_audio):
        raise FileNotFoundError(f"O arquivo {caminho_audio} não foi encontrado.")
    model = whisper.load_model("base")
    result = model.transcribe(caminho_audio)
    return result["text"]

def resumir_texto_local(texto):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # O modelo tem limite de tokens, então pode ser necessário dividir textos grandes
    if len(texto) > 1000:
        partes = [texto[i:i+1000] for i in range(0, len(texto), 1000)]
        resumos = [summarizer(parte, max_length=130, min_length=30, do_sample=False)[0]['summary_text'] for parte in partes]
        return "\n".join(resumos)
    else:
        resumo = summarizer(texto, max_length=130, min_length=30, do_sample=False)
        return resumo[0]['summary_text']

def main():
    url = input("URL do vídeo do YouTube: ").strip()
    audio_file = "audio.mp3"
    try:
        baixar_audio(url, audio_file)
        texto = transcrever_local(audio_file)
        print("\nTranscrição:\n", texto)
        resumo = resumir_texto_local(texto)
        print("\nResumo:\n", resumo)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == "__main__":
    main()
    
