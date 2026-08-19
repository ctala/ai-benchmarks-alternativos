# LongCat 2.0 — content_verificable/audiencia_que_ya_sabe

- model_id: `meituan/longcat-2.0`
- success: True  | final: 8.74 | quality: 10.0
- latency_total: 20.678s | tokens_per_second: 36.8
- input_tokens: 107 | output_tokens: 760

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# El workflow que dice "success" y no hizo nada

¿Te ha pasado? El webhook disparó, el cron se ejecutó a la hora exacta, el log muestra `success` en verde... pero el CRM no se actualizó, el email nunca salió, y el cliente sigue esperando.

No es un bug de n8n. Es un diseño silencioso que falla sin avisar.

**Por qué pasa**

Un workflow puede devolver `success` sin ejecutar nada útil por varias razones:

- **Condiciones que nunca se cumplen.** Tu nodo IF filtra el 100% de los datos porque el campo cambió de nombre en la API hace tres semanas. El workflow "funciona", pero no pasa nada.
- **Nodos deshabilitados en producción.** Activas el workflow sin darte cuenta de que tenías nodos pausados durante las pruebas.
- **Errores capturados por un nodo Error Trigger que los descarta silenciosamente.** Tienes manejo de errores, pero ese manejo es... no hacer nada.
- **Datos vacíos que llevan a un branch que no tiene nodos.** El workflow ejecuta el camino correcto, pero ese camino está en blanco.

**Cómo detectarlo**

1. **Añade un nodo Set al final de cada branch real** que marque `executed: true` con un timestamp. Si no ves ese campo en tus datos de salida, el branch murió antes.
2. **Usa el nodo Debug en modo "Complete"** al menos una vez por cada path crítico. No confíes en el resumen de ejecución; abre los items y verifica que tienen el payload esperado.
3. **Configura un nodo de notificación que se ejecute SIEMPRE**, incluso en branches de fallback. Si no recibiste ni el mensaje de éxito ni el de error, el workflow no llegó donde crees.
4. **Revisa el historial de ejecuciones con el filtro "Error" desactivado.** Ahí ves los `success` que en realidad fueron vacíos. Fíjate en la cantidad de items de salida: si es cero, algo filtró todo.

El `success` de n8n solo significa "no se rompió". No significa "hizo lo que necesitabas". Esa diferencia te la tienes que verificar tú.