# Define a imagem base a ser usada
FROM python:latest

# Define o diretório de trabalho da aplicação dentro do contêiner
WORKDIR /app

# Copia os arquivos da aplicação para o diretório de trabalho do contêiner
COPY . /app

# Instala as dependências necessárias
RUN pip install Flask

# Define a variável de ambiente FLASK_APP
ENV FLASK_APP=calculadora.py

# Define o comando para iniciar a aplicação
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

## docker run -p 5000:5000 nome_da_sua_imagem