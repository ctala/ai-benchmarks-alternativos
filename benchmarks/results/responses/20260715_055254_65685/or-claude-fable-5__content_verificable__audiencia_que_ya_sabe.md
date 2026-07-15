# Claude Fable 5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 8.0 | quality: 10.0
- latency_total: 18.043s | tokens_per_second: 43.0
- input_tokens: 159 | output_tokens: 775
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**El "success" que no hizo nada**

Todos tenemos ese workflow que lleva meses en verde y del que nadie sospecha. Hasta que alguien pregunta por qué no llegaron los reportes de las últimas tres semanas.

El problema: n8n marca una ejecución como exitosa si ningún nodo lanza error. Pero "sin errores" no significa "hizo su trabajo". Los culpables habituales:

- **Cero items que fluyen en silencio.** Un filtro que de repente no matchea nada, un query que devuelve vacío. Los nodos siguientes simplemente no se ejecutan y la ejecución termina en verde.
- **APIs que responden 200 con errores dentro del body.** El HTTP Request está feliz; el `{"status": "failed"}` del payload nunca se lee.
- **`continueOnFail` activado y olvidado.** El error pasa como item normal y nadie lo mira río abajo.
- **Ramas de IF/Switch donde todo cae del lado que no hace nada**, por un cambio de formato en los datos de entrada.

Cómo detectarlo:

1. **Valida conteos, no solo ejecución.** Un IF después de pasos críticos: si `items.length === 0` donde no debería, lanza un Stop and Error explícito. Falla ruidosa > éxito falso.
2. **Parsea el body, no el status code.** Chequea el campo de estado real de la respuesta antes de continuar.
3. **Monitorea el resultado de negocio.** Un workflow aparte que verifique "¿se crearon registros hoy?" te avisa lo que el Error Workflow jamás verá, porque para n8n nunca hubo error.

Regla simple: si un workflow puede terminar en verde sin haber producido su efecto, todavía no está terminado.