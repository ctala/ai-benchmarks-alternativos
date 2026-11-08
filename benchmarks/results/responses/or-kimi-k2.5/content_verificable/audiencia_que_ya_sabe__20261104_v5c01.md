# Kimi K2.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 95.137s | tokens_per_second: 27.9
- input_tokens: 120 | output_tokens: 2650

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

El peor bug en n8n no es rojo. Es verde.

Cuando revisas el execution log y todo está en success, es fácil pensar que la noche fue tranquila. Pero n8n solo marca error cuando algo explota. Si tu workflow no hizo absolutamente nada y terminó limpio, también será verde.

Conozco tres formas en las que esto pasa en producción. Primera: una expresión falló silenciosamente y devolvió undefined, pero el nodo siguiente no recibió items y simplemente no operó. Segunda: un nodo IF mandó todo por la rama false que dejaste vacía. Tercera: un filtro o una query que, por un cambio externo, dejó de traer datos. El workflow corrió perfecto; solo que sobre cero items.

El panel de executions te miente por omisión. No confíes en él.

Para detectarlo, cambia qué monitoreas. En lugar de preguntar "¿terminó en verde?", pregunta "¿cuántos items produjo?". Si esperas movimiento diario, un execution de 200ms con 0 operations en nodos clave es tu verdadera alarma. Usa nodos de logging explícitos al final de ramas false o vacías. Si un filtro deja pasar cero items, que un nodo posterior te avise, no que calle. Y si corres workflows scheduled, revisa regularmente el execution log buscando outputs vacíos repetidos: el patrón es más revelador que el color.

En resumen: diseña para que el silencio sea ruidoso. Si tu workflow puede terminar sin tocar datos y nadie se entera, no tienes un workflow. Tienes un amuleto.