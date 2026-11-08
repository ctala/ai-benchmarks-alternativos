# Ling 3.0 Flash — orchestration/complex_workflow_decomposition

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 5.21 | quality: 4.02
- latency_total: 4.321s | tokens_per_second: 91.2
- input_tokens: 1295 | output_tokens: 394
- judge_score: 2.0 | justificación: 

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

## 🚀 Iniciando proceso de onboarding para Andres Morales (DataPulse SpA)

Voy a ejecutar cada paso en orden, comenzando por la creación de la cuenta.

---

### Paso 2: Creando cuenta en el sistema vía