FROM python:3.12.7-slim-bookworm
# Sin PyPI (9-nov-2026): las dependencias vienen como ruedas versionadas en el repo y pip
# queda configurado para no salir a internet, así la tarea se arma y se resuelve igual
# hoy y dentro de un año. El agente instala con `pip install` normal desde /opt/ruedas.
COPY wheels /opt/ruedas
ENV PIP_NO_INDEX=1 \
    PIP_FIND_LINKS=/opt/ruedas \
    PIP_DISABLE_PIP_VERSION_CHECK=1
RUN pip install --no-cache-dir requests==2.32.3
COPY proyecto /app/proyecto
# `.env` se guarda con otro nombre en el repo porque el .gitignore del benchmark lo excluye.
COPY env-proyecto /app/proyecto/.env
WORKDIR /app/proyecto
