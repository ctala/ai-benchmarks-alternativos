# Muse Spark 1.3 — orchestration/complex_workflow_decomposition

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 4.48 | quality: 3.56
- latency_total: 3.567s | tokens_per_second: 137.7
- input_tokens: 1403 | output_tokens: 491
- judge_score: 2.0 | justificación: La respuesta es muy superficial y no detalla los pasos necesarios para automatizar el proceso de onboarding, careciendo de precisión y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente orquestador experto en automatizacion.
Descompone tareas complejas en pasos atomicos ejecutables.
Usa las herramientas disponibles para ejecutar cada paso.

**user:**

Automatiza este proceso de onboarding para un nuevo cliente:

1. El cliente envio sus datos por email (nombre: Andres Morales, empresa: DataPulse SpA, email: andres@datapulse.cl)
2. Hay que crear su cuenta en nuestro sistema (API endpoint: POST /api/v1/accounts)
3. Generar una API key para el
4. Enviarle un email de bienvenida con sus credenciales
5. Agendar una llamada de kickoff para la proxima semana
6. Notificar al equipo de Customer Success en Slack

Ejecuta los pasos en orden. Para cada paso, usa la herramienta apropiada.


## Respuesta completa

Arranco tu onboarding: ordeno los 6 pasos y preparo la cuenta de DataPulse.