# Seed 2.1 Turbo — business_audit/churn_mezcla_free_y_pago

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 83.862s | tokens_per_second: 65.7
- input_tokens: 220 | output_tokens: 5507

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

### Primero: CALMA, el 31% es un número engañoso por un problema de definición de población, no una catástrofe de retención.
Vamos a desglosar paso a paso, como corresponde a un análisis de retención: primero validamos qué mide cada métrica, luego evaluamos la gravedad real, y después armamos el plan.

---

## 1. ¿Por qué la discrepancia entre el 31% reportado y tu expectativa de 5%?
El panel está calculando el churn de **TODA la base de usuarios (gratuitos + pago)**, una población mixta con comportamientos totalmente distintos. El cálculo matemático es correcto (62 bajas / 200 usuarios inicio = 31%), pero esta métrica es irrelevante para la mayoría de negocios freemium, donde el valor viene de los usuarios de pago.

Tu referencia de 5% casi seguro corresponde al churn de usuarios de pago, que es el que impacta directamente los ingresos recurrentes.

---

## 2. Métricas reales por segmento (para medir la gravedad de verdad)
No se puede mezclar una base de 178 usuarios gratuitos (sin compromiso económico) con 22 de pago (que invierten dinero). Vamos a separarlas:

| Segmento       | Usuarios inicio de mes | Bajas | Churn mensual |
|----------------|------------------------|-------|---------------|
| Total (reportado) | 200                   | 62    | 31%           |
| Plan gratuito  | 178                    | 60    | ~33,7%        |
| Plan de pago   | 22                     | 2     | ~9,1%         |

### ¿Qué tan grave es cada métrica?
#### a) Churn de gratuito del 33,7%
En modelos freemium es completamente normal: los usuarios gratuitos no tienen costo de salida, suelen probar y abandonar si no encuentran valor rápido. Valores de 30-60% mensual son comunes en sectores de consumo, y incluso en B2B suelen superar el 15%.
Solo es problemático si:
- Tu costo de adquisición de usuarios gratuitos es muy alto
- Tu tasa de conversión a pago es menor al 2-3% (y por lo tanto no compensa el churn)

#### b) Churn de pago del 9,1%
Aquí está la métrica que te importa, y sí es más alto que tu expectativa de 5%, pero está MUY lejos del 31% de pánico. Para contextualizar:
- Un churn de 5% mensual implica una vida útil del cliente (LTV) de ~20 meses
- Un churn de 9,1% implica una LTV de ~11 meses

⚠️ **Aclaración clave por tamaño de muestra**: Tu base de pago es muy chica (22 usuarios). Una sola baja extra cambia el churn en ~4,5 puntos porcentuales. La diferencia entre 5% y 9% puede ser solo ruido estadístico, no una tendencia real. No tomes decisiones drásticas por un solo mes de datos con una base tan pequeña.

---

## 3. Plan de acción estructurado
### Fase 1: Salir del pánico y arreglar la métrica (primeras 24h)
1. **Define cuál es la métrica de churn relevante para tu negocio**:
   - Si monetizas por suscripciones: la métrica principal es el **churn de ingresos (revenue churn)** (pesa por el valor de cada cliente, no por cantidad de usuarios), y secundariamente el churn de usuarios de pago. El churn total de base es irrelevante y lo puedes quitar de la vista principal del panel.
   - Si monetizas por publicidad en la base gratuita: medí el churn de gratuitos por separado, nunca mezclado con pago.
2. **Verifica por qué el panel muestra el churn total**: ¿es la configuración por defecto? ¿se rompió un filtro de segmentación? ¿el equipo tenía acordado medir solo pago y alguien cambió el reporte?
3. **Calcula el churn de ingresos para tener la medida real**: Si los 2 usuarios que se dieron de baja eran de planes baratos, el impacto en ingresos puede ser incluso menor al 5% que esperabas. Ejemplo: si tu ingreso total de pago a inicio de mes era de $500, y los 2 usuarios pagaban $10 cada uno, el revenue churn es de 20/500 = 4%, que está dentro de tu expectativa.

### Fase 2: Diagnosticar la desviación en churn de pago (3-5 días)
Tu único punto de alerta real es por qué el churn de pago se desvió de tu referencia de 5%. Con una base tan chica, primero descarta ruido estadístico:
1. **Compara con el historial de los últimos 3-6 meses**:
   - Si los churn anteriores eran 4%, 5%, 6% y ahora salta a 9%: es un pico, probablemente aleatorio.
   - Si los últimos 3 meses fueron 6%, 7,5%, 9%: sí hay una tendencia creciente que hay que atender.
2. **Analiza las 2 bajas en detalle**:
   - ¿Son clientes nuevos (menos de 30 días de alta) o antiguos? Si son nuevos, el problema está en el onboarding o en expectativas falsas generadas en la venta. Si son antiguos, revisa soporte, cambios de funcionalidades o subidas de precios.
   - ¿Qué plan tenían? Si son del plan más barato, el impacto es menor que si fueran de planes enterprise.
   - ¿Tienes registro del motivo de baja? Si no, envía una encuesta corta de 1 pregunta o incluso llama si son clientes de alto valor.
3. **Descarta errores de cálculo**: Asegúrate de que los 22 usuarios de pago de inicio de mes excluyen períodos de prueba gratuita (usuarios que nunca pagaron no deberían contar en la base de pago).

### Fase 3: Evaluar el churn de gratuito (si es relevante para tu modelo)
Si tu fuente principal de clientes de pago es la conversión de gratuitos:
1. Compara el 33,7% con el promedio de los últimos 3 meses: ¿es un valor normal o subió repentinamente?
2. Si subió: revisa si hubo cambios en el onboarding de gratuitos, en las funcionalidades a las que tienen acceso, o en la fuente de adquisición (ej: si este mes trajiste usuarios de una red que no es tu público objetivo, es normal que abandonen más).
3. Si es normal: no le dediques recursos, enfócate en medir la tasa de conversión a pago (esa es la métrica que importa de la base gratuita).

### Fase 4: Prevenir que vuelva a pasar la confusión (1 semana)
1. **Configura el panel correctamente**: Pon la métrica relevante (ej: churn de ingresos de pago) en la parte superior, y etiqueta TODAS las métricas con la población que miden (no pongas solo "churn", pon "churn de usuarios de pago mensual" o "churn de plan gratuito").
2. **Documenta las definiciones**: Escribe en un lugar accesible para todo el equipo qué mide cada métrica, qué población incluye y cuál es la métrica principal de retención.
3. **Agrupa métricas por segmento**: Nunca mezcles usuarios gratuitos y de pago en métricas de retención, ya que sus ciclos de vida son completamente distintos.

---

## Resumen de gravedad final
- ❌ Pánico por el 31%: Totalmente injustificado, es un error de definición de métrica.
- ⚠️ Alerta por churn de pago: Moderada, y probablemente en parte por ruido estadístico por la base chica. No es una crisis, pero hay que revisarla para confirmar que no es una tendencia.
- 🟢 Churn de gratuito: Dentro de lo normal para modelos freemium, a menos que tengas una desviación histórica.