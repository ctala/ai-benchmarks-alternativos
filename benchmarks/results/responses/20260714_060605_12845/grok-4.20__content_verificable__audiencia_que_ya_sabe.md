# Grok 4.20 — content_verificable/audiencia_que_ya_sabe

- model_id: `x-ai/grok-4.20`
- success: True  | final: 9.16 | quality: 10.0
- latency_total: 4.923s | tokens_per_second: 101.0
- input_tokens: 277 | output_tokens: 497
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**Por qué tu workflow dice “success” pero no hizo absolutamente nada**

Si construyes workflows en n8n todos los días, seguro te ha pasado: el execution log marca **success** en verde, el webhook responde 200 OK, el cron terminó “sin errores”… y sin embargo no se creó ningún registro, no se envió ningún email, no se actualizó nada.

Esto no es un bug de n8n. Es un comportamiento esperado que casi nadie explica claramente.

Un nodo (o un workflow entero) se considera exitoso si **ninguno de los nodos que se ejecutaron** lanzó una excepción. Punto. n8n no valida por defecto que el resultado final fuera el que tú esperabas. Si un nodo If no entró por ninguna rama, si un Item Lists devolvió cero items, si un Set no modificó nada porque le llegaban datos vacíos… todo eso sigue siendo técnicamente “success”.

### Cómo detectarlo antes de que te vuelva loco

1. **Activa “Continue On Fail” solo donde realmente lo necesites** y revisa el output de los nodos que tienen error output. La mayoría de falsos positivos vienen de ahí.

2. **Usa el nodo “IF” + “NoOp” como guardia final.** Al final del workflow pon un IF que valide que realmente pasó algo (cantidad de items > 0, campo específico no vacío, etc.). Si no pasa, que vaya a un NoOp con un nombre claro: “Early Exit - No data to process”. Así ves en el historial exactamente qué ocurrió.

3. **Agrega un nodo “Set” o “Function Item” de validación** antes del último paso crítico. Devuelve un objeto `{ processed: true, items: $input.all().length }` y luego compáralo en el siguiente nodo. Si processed es false, ya sabes que el workflow se durmió.

4. **Revisa siempre el Execution Data → “Executed Nodes”**. Si ves muchos nodos en gris o directamente no aparecen, es señal de que el flujo murió antes sin tirar error.

El éxito técnico no es lo mismo que el éxito de negocio. Entrena a tus workflows para que sepan gritar cuando están haciendo ruido pero no avanzan.

¿Te ha pasado mucho esto últimamente? Cuéntame en los comentarios qué tipo de workflow te está volviendo loco con falsos positivos.

---

(248 palabras)