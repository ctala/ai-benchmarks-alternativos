# LongCat 2.0 — content_verificable/audiencia_que_ya_sabe

- model_id: `meituan/longcat-2.0`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 41.222s | tokens_per_second: 35.1
- input_tokens: 107 | output_tokens: 1447

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Ese momento en que miras el historial de ejecuciones, ves el check verde de "Success" y piensas: "Todo bien". Hasta que te das cuenta de que el lead nunca entró a la CRM, la factura no se envió o el registro sigue intacto. El workflow *no falló*, simplemente no hizo nada. 

¿Por qué ocurre este silencioso desastre? Tres culpables habituales:

1. **Arrays vacíos que enmascaran la lógica:** Tu nodo de filtrado o búsqueda devuelve `[]`. El nodo siguiente itera cero veces, no lanza error y n8n lo marca como exitoso.
2. **Rutas condicionales sin destino:** Un nodo IF evalúa a `false` y esa rama muere porque no tiene conectado ningún nodo de acción. El flujo sigue por la rama verdadera (o termina) sin ejecutar la tarea.
3. **El vicio de "Continue on Fail":** Configuraste el nodo para que continúe si falla. El workflow ignora el error 429 o 500 de la API, sigue su camino y termina en "Success".

**¿Cómo cazar estos fantasmas?**

*   **Audita los nodos "fantasma":** En el log de ejecución, si un nodo no tiene el borde de ejecución, significa que nunca se activó. Ahí está tu pista.
*   **Añade validaciones post-acción:** Después de tu nodo crítico (ej. *Crear Registro*), conecta un IF que verifique si el ID de respuesta existe. Si no, dispara un error manual o una alerta.
*   **Desactiva "Continue on Fail" en desarrollo:** Oblígate a ver el rojo. Solo actívalo en producción si tienes un plan de contingencia real.

El verde en n8n significa que el motor no se rompió, no que tu negocio avanzó. Revisa tus salidas.