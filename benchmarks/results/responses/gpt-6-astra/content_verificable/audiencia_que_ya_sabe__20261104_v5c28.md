# GPT-6 Astra — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-6-astra`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 18.564s | tokens_per_second: 28.4
- input_tokens: 101 | output_tokens: 528

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## «Success» no significa «trabajo hecho»

El workflow termina en verde. No hay errores. Pero el CRM sigue igual y los registros que debían procesarse siguen pendientes.

No es una contradicción: **n8n puede confirmar una ejecución sin errores no controlados, no que se haya cumplido tu objetivo.**

Los sospechosos habituales:

- **Cero items a mitad del recorrido.** Una consulta devuelve vacío o un filtro descarta todo. Los nodos siguientes no reciben datos y la ejecución puede terminar correctamente.
- **Una rama que nunca se activa.** El workflow funciona exactamente como lo configuraste, pero la condición ya no coincide con los datos reales.
- **Errores tolerados.** Configuraste el nodo para continuar ante un fallo, pero no estás revisando ni contabilizando esos fallos.
- **Respuestas técnicamente válidas.** Un HTTP 200 puede incluir un rechazo funcional; un 202 solo confirma aceptación, no procesamiento.

### Detecta resultados, no solo ejecuciones

Define un contrato verificable: «por cada pedido elegible debe existir una factura con su identificador externo». Después instrumenta tres niveles:

**1. Contadores.** Registra items leídos, elegibles, intentados, confirmados y fallidos. Compara magnitudes que deban coincidir: diez intentos y cero confirmaciones requieren explicación.

**2. Comprobación del efecto.** No confundas «envié la petición» con «se guardó el cambio». Valida la respuesta funcional y, cuando importe, consulta el sistema destino o espera su confirmación asíncrona.

**3. Vigilancia independiente.** Guarda un resumen por ejecución con un `run_id`. Otro workflow debe detectar resúmenes ausentes, retrasos o resultados anómalos. Un nodo de alerta al final no te protege si nunca recibe items.

Y distingue el vacío legítimo del sospechoso: cero pedidos un domingo puede ser normal; cero durante toda una semana, probablemente no.

**El verde sirve para operar. La evidencia sirve para confiar.**