# Claude Sonnet 5.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 10.97s | tokens_per_second: 106.7
- input_tokens: 161 | output_tokens: 1171

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# Verde no significa hecho

Tu ejecución sale en verde, pero el CRM sigue sin el lead. n8n no miente: el workflow terminó sin errores. Que no fallara no significa que hiciera algo.

## Los sospechosos habituales

- **Cero items aguas arriba.** Un Get Many, un Filter o un IF devuelven vacío y todo lo que viene después simplemente no se ejecuta. Resultado: success.
- **On Error: Continue.** Silencia el fallo y sigues con un item de error que nadie mira.
- **200 con error en el body.** Muchas APIs responden `200` con `{"ok": false}`. El HTTP Request lo da por bueno.
- **Respond to Webhook anticipado.** El cliente recibe su 200 antes de que el trabajo termine, o aunque falle después.
- **Sub-workflows que devuelven vacío.** El padre sigue como si nada.

## Cómo detectarlo

1. **Aserciones explícitas.** Al final de la rama importante, un IF que compruebe lo que debería ser cierto (`{{$items().length}} > 0`, ID devuelto, campo esperado). Si no se cumple, **Stop and Error**.
2. **Valida el body, no el status.** Tras cada HTTP crítico, comprueba el campo que confirma la operación.
3. **Heartbeat invertido.** Haz ping a Healthchecks o Uptime Kuma solo al final del camino feliz. Si no llega, salta la alerta. Así detectas también lo que nunca se ejecutó.
4. **Métricas por ejecución.** Registra items procesados y alerta si baja de lo normal durante N ejecuciones.

El Error Workflow solo avisa de lo que revienta. Para lo silencioso, tienes que definir qué es "hecho" y comprobarlo.