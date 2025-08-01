# Imagem base enxuta com Python 3.12
FROM python:3.12-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Define o caminho para a chave de autenticação do GCP
# ENV GOOGLE_APPLICATION_CREDENTIALS=/app/secrets/gcp-key.json

# Comando padrão
CMD ["python", "main.py"]
