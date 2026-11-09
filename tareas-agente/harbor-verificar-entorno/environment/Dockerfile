FROM python:3.12.7-slim-bookworm
RUN pip install --no-cache-dir requests==2.32.3
COPY proyecto /app/proyecto
# `.env` se guarda con otro nombre en el repo porque el .gitignore del benchmark lo excluye.
COPY env-proyecto /app/proyecto/.env
WORKDIR /app/proyecto
