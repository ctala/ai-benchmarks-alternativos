# Imagen y dependencias FIJAS. Una etiqueta flotante (python:3.12-slim) hace que la
# tarea cambie de comportamiento sin que nadie la toque — el mismo problema de
# comparabilidad que este repo persigue en sus propias mediciones. Lo marcó la rúbrica
# de `harbor check`.
FROM python:3.12.7-slim-bookworm
WORKDIR /app
COPY tarifario.csv reglas.md encargo.md /app/
