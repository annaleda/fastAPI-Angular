FROM python:3.12-slim

WORKDIR /app

# Copia i file necessari
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto dei file dell'app
COPY . .

# Esponi le porte necessarie
EXPOSE 8080 5005

# Comando per avviare l'app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]