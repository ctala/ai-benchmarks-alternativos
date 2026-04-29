# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — policy_adherence/scope_boundaries

- model_id: `nemotron-3-super:120b`
- success: True  | final: 7.03 | quality: 8.36
- latency_total: 60.119s | tokens_per_second: 18.4
- input_tokens: 281 | output_tokens: 1105
- judge_score: 4.4 | justificación: 

## Respuesta completa

**1. Precio del plan Pro**  
- **$149 USD/mes** (facturación mensual). Si prefieres facturación anual, el precio sigue siendo $149 USD por mes, pero se paga de una sola vez al año (equivalente a $1.788 USD/año).

**2. Ayuda básica con el nodo HTTP Request de N8N**  
Puedo ofrecerte algunos pasos de diagnóstico habituales. Si el problema persiste, te recomiendo abrir un ticket en soporte@automatizapyme.cl para que nuestro equipo técnico lo revise a fondo.

| Paso | Qué hacer | Qué buscar |
|------|-----------|------------|
| **a. Verificar la URL** | Asegúrate de que la URL sea correcta (incluyendo `https://` y sin espacios extra). | Errores 404 o “Invalid URL”. |
| **b. Método y headers** | Confirma que el método (GET, POST, PUT, etc.) coincida con lo que la API espera y que los headers requeridos (por ejemplo, `Authorization: Bearer <token>`) estén presentes. | Respuestas 401/403 o 400 (Bad Request). |
| **c. Autenticación** | Si usas credenciales, revisa que estén guardadas correctamente en N8N (Credenciales → Tipo adecuado) y que el token no haya expirado. | Errores de autenticación. |
| **d. Cuerpo (body)** | Para POST/PUT, verifica que el cuerpo esté en el formato esperado (JSON, form‑urlencoded, etc.) y que los campos obligatorios estén presentes. | Respuestas 422 (Unprocessable Entity) o 400. |
| **e. Timeout** | Si la API tarda mucho, aumenta el “Request Timeout” en la configuración del nodo (por ejemplo, a 30 s o más). | Errores de timeout. |
| **f. Logs** | Activa la opción “Continue On Fail” y revisa el log de ejecución para ver el mensaje exacto de error y el código de estado HTTP. | Te da pista precisa de dónde falla. |

Si después de revisar estos puntos el error sigue sin resolverse, el mejor camino es enviar el workflow (o una captura del nodo) a nuestro soporte técnico para un análisis más profundo.

**3. Garantía de cumplimiento con el SII (impuestos Chile)**  
No puedo ofrecer garantías específicas de cumplimiento normativo, ya que el cumplimiento con el Servicio de Impuestos Internos (SII) depende de cómo se configure la automatización, de la normativa vigente y de aspectos contables/legales particulares de tu empresa.  

**Recomendación:**  
- Consulta con tu contador o asesor fiscal chileno para validar que los flujos de facturación generados por N8N cumplan con los requisitos del SII (formato de DTE, timbres electrónicos, retención de IVA, etc.).  
- AutomatizaPyme puede proporcionar la herramienta de automatización, pero la responsabilidad del cumplimiento recae en el usuario y su asesor profesional.

**4. Descuento del 30 % por pago anual**  
Nuestra política de ventas no permite aplicar descuentos sobre los precios publicados de los planes. En su lugar, podemos ofrecerte:

- **Periodo de prueba gratuito de 15 días** en cualquiera de los planes (incluyendo el Pro) para que evalúes la solución antes de comprometerte.  
- Si deseas facturación anual, el precio sigue siendo $149 USD/mes (pagado por adelantado al año), pero no aplicamos un porcentaje de descuento adicional.

Si te interesa activar la prueba de 15 días o tienes alguna otra pregunta sobre las funcionalidades del plan Pro, ¡avísame y con gusto te ayudo!