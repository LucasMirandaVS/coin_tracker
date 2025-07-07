# Imagem base do Python
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do projeto para o container
COPY . .

# Instala as dependências
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Define a variável de ambiente com o caminho da credencial
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/secrets/projeto-estudando-gcp-42d17426c4e1.json

# Comando padrão para executar a aplicação Flask via main.py
CMD ["python", "main.py"]
