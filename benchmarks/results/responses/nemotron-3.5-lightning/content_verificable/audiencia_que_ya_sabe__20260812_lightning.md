# Nemotron 3.5 Lightning — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.39 | quality: 10.0
- latency_total: 4.351s | tokens_per_second: 433.9
- input_tokens: 116 | output_tokens: 1888
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un experto en n8n, abordando el problema específico de los workflows que reportan éxito sin ejecución.

## Respuesta completa

If your n8n workflows report "success" while the intended downstream effects never materialize, you're encountering a classic completion-versus-execution disconnect. The platform marks a run successful as soon as the final node exits without an uncaught exception—regardless of whether data actually flowed through the defined paths.

Webhooks often trigger this symptom. If a webhook node responds before downstream nodes process the payload, n8n registers the run as finished while the real work stalls in a pending or skipped state. Similarly, conditional nodes where expressions consistently evaluate false, or Set/Resolve nodes that transform data without passing it forward, create a green checkmark with zero tangible output.

To detect these silent failures, stop trusting the summary status. Open the execution audit and trace node-by-node which branches actually received data. Look for entries where `{{ $json.length }}` is zero, or where the "Execute Workflow" node was triggered with empty input. Adding a debug node at the entry point, or inserting an early `IF` check that aborts or logs when the payload is absent, forces visibility before the run concludes.

Also, inspect your error workflow. Errors silently routed through a generic "Resolve" or "No-Op" node will let the main path report success while the data never exits the sandbox. The fix isn't more automation—it's stricter validation. Use execution breakpoints, verify payload integrity at each hop, and never accept a green checkmark without confirming the data trail.