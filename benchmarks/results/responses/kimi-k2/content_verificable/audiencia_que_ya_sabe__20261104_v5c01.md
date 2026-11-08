# Kimi K2 — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 11.769s | tokens_per_second: 38.4
- input_tokens: 121 | output_tokens: 452

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Cuando el check verde te miente**

El peor bug es el que no parece bug.

Tu workflow devuelve 200 OK. El nodo final se pinta de verde. Pero el registro no existe en la base de datos. El email nunca salió. El archivo sigue en S3.

¿Qué pasó? Probablemente un filtro que descartó todo, una búsqueda que no encontró coincidencias, o un merge que recibió datos vacíos. n8n ejecutó lo que le pediste. Simplemente no había nada que procesar.

**Cómo detectarlo antes de que te lo reporte el cliente**

1. **Contadores explícitos**: después de nodos de filtro, búsqueda o split, añade un Set que guarde `{{ $input.all().length }}`. Si llega 0, algo va mal.

2. **Validación de salida**: no verifiques solo que el nodo corrió. Verifica que *produjo* algo. Un HTTP Request que devuelve 200 con body vacío es fallo, no éxito.

3. **Rutas de vacío**: conecta siempre el output "no matches" de filtros y switches. Que termine en un nodo de alerta o log. El silencio es información.

4. **Métricas de negocio, no técnicas**: tu monitoreo debe medir "órdenes procesadas", no "workflows ejecutados". Un dashboard de ejecuciones exitosas que no correlaciona con transacciones reales es inútil.

5. **Stop on error estándar**: desactívalo en desarrollo para ver dónde fluyen los datos vacíos. Actívalo en producción, pero con notificación previa de los contadores mencionados.

El check verde es el peor enemigo del debugging. Diseña para que el éxito real sea visible, no asumido.