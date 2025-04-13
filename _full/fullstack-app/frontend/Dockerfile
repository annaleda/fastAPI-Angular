# Fase 1: Costruzione dell'app Angular
FROM node:14.21.3 AS builder

WORKDIR /app

# Copia package.json e package-lock.json per installare le dipendenze
COPY package*.json ./

# Installa le dipendenze
RUN npm install\
&& npm install --save-dev @types/node@16.11.7


# Copia il resto del codice sorgente
COPY . .

# Build dell'app Angular in modalità produzione
RUN npm run build --prod

# Fase 2: Servire l'app Angular con Nginx
FROM nginx:latest

# Copia il build di Angular nel container Nginx
COPY --from=builder /app/dist/frontend /usr/share/nginx/html

# Copia il file di configurazione nginx.conf personalizzato
COPY nginx.conf /etc/nginx/nginx.conf  

# Esponi la porta 80 (Nginx di default usa la porta 80)
EXPOSE 80

# Avvia Nginx
CMD ["nginx", "-g", "daemon off;"]

