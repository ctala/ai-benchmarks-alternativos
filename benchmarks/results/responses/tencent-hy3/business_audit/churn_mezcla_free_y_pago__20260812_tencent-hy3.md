# Tencent Hy3 — business_audit/churn_mezcla_free_y_pago

- model_id: `tencent/hy3`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 185.594s | tokens_per_second: 25.4
- input_tokens: 199 | output_tokens: 4714

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa

Respira. Como analista de retención, mi primera regla antes de interpretar una métrica es **verificar qué población está midiendo realmente**. Y en tu caso, el panel te está dando un ataque al corazón innecesario porque está mezclando manzanas con peras.

Tu plataforma te arroja un **Churn Mezclado (Blended Churn)**. Es matemáticamente correcto (62/200 = 31%), pero operativamente engañoso porque no distingue entre quien te paga la luz y quien solo ocupa espacio en la base de datos.

Aquí está el desglose real de la población:

### 1. El Diagnóstico Real (Desglose por Población)
*   **Churn del Plan Gratuito:** 60 bajas / 178 usuarios = **33.7%**
*   **Churn del Plan de Pago:** 2 bajas / 22 usuarios = **9.1%**

### 2. ¿Qué tan grave es? (Evaluación de severidad)
**El pánico del 31%:** No es tan catastrófico como parece. El 97% de tus bajas (60 de 62) fueron usuarios gratuitos. No estás perdiendo dinero directo por ellos, pero sí estás perdiendo *potencial* de conversión.

**El Churn Gratuito (33.7%):** Es alto, pero común en modelos *freemium* si el embudo superior (top of funnel) es amplio o si el producto no entrega valor rápido. Tu "cubo" gratuito tiene una fuga grande: estás atrayendo a la gente equivocada o no logran el "Aha! moment" (momento de valor).

**El Churn Pagado (9.1%):** *Este es el número que te debe importar de verdad.* 
*   Un 9.1% mensual se traduce en una pérdida anualizada de ~66% de tus ingresos recurrentes. Eso sí es grave para la salud de un SaaS a largo plazo (el benchmark de excelencia es <10% anual).
*   **Pero ojo con la muestra:** Solo son 2 usuarios de una base de 22. La varianza es altísima. Si el mes que viene se van 0, tu churn pagado es 0%; si se van 3, sube a 13.6%. No es una hemorragia, es una gotera que debes tapar antes de que crezca.
*   *Sobre tu 5%:* Probablemente antes estabas midiendo solo pagos o tuviste un mes atípico. Tu nueva realidad para pagos es ~9%, no 31%.

---

### 3. El Plan de Acción (Paso a Paso)

**Paso 1: Arregla el Tablero (Segmentación Inmediata)**
En tu panel, separa las métricas. Nunca más mires el "Churn Total" sin un filtro de plan. Crea dos tarjetas visuales: *Churn Free* y *Churn Paid*. El churn mezclado es una métrica de vanidad peligrosa.

**Paso 2: Autopsia del Churn Pagado (Urgente - Los 2 usuarios)**
Como solo son 2, haz una autopsia 1-a-1 hoy mismo.
*   Escríbeles un correo personalizado o llámalos. ¿Por qué se fueron? ¿Precio? ¿Falta de una funcionalidad crítica? ¿No entendieron el producto?
*   Con una base de 22, cada baja es predecible si no hay seguimiento.

**Paso 3: Auditoría del Churn Gratuito (Los 60 usuarios)**
*   Revisa tus fuentes de adquisición de este mes. ¿Corriste alguna campaña, cambiaste el copy de la landing o apareciste en un medio que trajo tráfico de baja intención?
*   Revisa los primeros 7 días de vida de esos 60. ¿Llegaron a activarse (usaron la funcionalidad core)?

**Paso 4: Re-baseline de Expectativas**
Acepta que tu línea base de churn pagado es ~9% (no 5%). Si no tienes *expansion revenue* (upsells), necesitas bajar eso a <5% mensual rápido para no destruir tu LTV (Lifetime Value).

**Paso 5: Retención Proactiva (Los 20 que quedan)**
Haz un "health check" de los 20 usuarios pagos restantes. Identifica señales de riesgo (baja frecuencia de login, no usan features clave) y haz un outreach de "cuentas por cobrar humanas" para asegurar que están felices.

**Conclusión:** No estás muriendo, pero tu tablero te estaba ocultando la verdad. El problema real (churn pagado) es pequeño en volumen pero requiere atención inmediata para no escalar a un problema de caja.