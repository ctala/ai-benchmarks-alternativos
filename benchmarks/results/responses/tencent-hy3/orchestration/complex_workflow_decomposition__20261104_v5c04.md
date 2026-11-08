# Tencent Hy3 — orchestration/complex_workflow_decomposition

- model_id: `tencent/hy3`
- success: True  | final: 7.8 | quality: 8.6
- latency_total: 45.545s | tokens_per_second: 60.1
- input_tokens: 1152 | output_tokens: 2736
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y bien estructurada, con una planificación detallada que identifica las dependencias entre pasos, lo que la hace muy útil para un emprendedor.

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

Voy a ejecutar el proceso de onboarding paso a paso. Primero descompongo las tareas y luego ejecuto cada una con la herramienta correspondiente, respetando las dependencias (la API key y el email dependen de la cuenta creada).

**Plan de ejecución:**
1. ✅ Datos recibidos (nombre, empresa, email) — provistos en el mensaje.
2. 🔄 Crear cuenta → `http_request` (POST /api/v1/accounts)
3. 🔄 Generar API key → `http_request` (depende de la respuesta del paso 2)
4. 🔄 Email de bienvenida → `send_email` (depende de 2 y 3)
5. 🔄 Agendar kickoff → `create_calendar_event`
6. 🔄 Notificar CS en Slack → `http_request` (webhook)

> ⚠️ Nota: No me proporcionaste la **URL base de la API** ni el **webhook de Slack**. Usaré valores placeholder razonables (`https://api.nuestrosistema.com` y un webhook de Slack estándar). Si difieren, corrígeme y reejecuto.

Empiezo con el **Paso 2: crear la cuenta**.