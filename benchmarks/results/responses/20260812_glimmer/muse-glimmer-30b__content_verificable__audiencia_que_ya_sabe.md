# Muse Glimmer 30B — content_verificable/audiencia_que_ya_sabe

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 14.475s | tokens_per_second: 66.8
- input_tokens: 118 | output_tokens: 967
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia objetivo, proporcionando soluciones prácticas y detalladas.

## Respuesta completa

El peor bug en n8n es el silencioso: ejecución en verde, `success`, y cero impacto real.

n8n marca éxito si ningún nodo lanza error. No si tu negocio se cumplió. Eso pasa todo el tiempo.

**Por qué ocurre**

* **Cero items entrando.** Un trigger devuelve vacío, un Read de Postgres no encuentra filas, y el resto del flujo simplemente no corre. Todo verde.
* **Un IF que se traga todo.** Filtraste mal una condición y el branch verdadero nunca se activa. El flujo termina sin hacer nada y sin quejarse.
* **Continue On Fail activado.** Tu HTTP Request falla, pero el nodo está en modo continuar. El siguiente nodo recibe `null` y sigue.
* **Operaciones idempotentes.** Upsert a Notion/Airtable/Sheets donde no hay cambios. El nodo responde 200, pero no se creó ni actualizó nada. No hay error, no hay trabajo.

**Cómo detectarlo**

1. **Asserts de items.** Al final de cada bloque crítico pon un Code node: `if (!items.length) throw new Error('Sin items')`. Falla rápido y visible.
2. **Valida el resultado, no el status.** Después de un HTTP o DB, revisa `affectedRows`, `created`, `response.body`. Un 200 no es suficiente.
3. **Contadores.** Usa un Set node al inicio para guardar `items_in` y otro al final para `items_out`. Si son 0 o iguales a 0, dispara alerta.
4. **No dejes ramas muertas.** Activa "Always Output Data" en el IF y logea el branch que no se tomó. O mejor, manda a un nodo de alerta cuando el camino esperado no se ejecuta.
5. **Error Workflow para silencio.** Crea un workflow de monitoreo que lea las ejecuciones vía API y busque éxitos con duración < X segundos o con 0 items procesados.

Éxito técnico ≠ éxito de negocio. Si no mides lo segundo, tu workflow puede estar funcionando perfectamente... y sin hacer nada.