# Sakana Namazu — business_audit/churn_mezcla_free_y_pago

- model_id: `sakana/sakana-namazu`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 9.486s | tokens_per_second: 215.9
- input_tokens: 202 | output_tokens: 2048

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

El usuario está en pánico porque su plataforma reporta un churn del 31% y pensaba que estaba en 5%. Me da datos específicos y un detalle importante al exportar la tabla.

Primero, debo actuar como analista de retención. El prompt de sistema dice: "Antes de interpretar una métrica, verificas qué población está midiendo realmente." Esto es clave.

Datos proporcionados:
- Usuarios que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31% (62/200 = 0.31)

Detalle desagregado:
- Total usuarios: 200 (178 gratuito, 22 pago)
- Total bajas: 62 (60 gratuito, 2 pago)

Necesito verificar qué está midiendo realmente esta métrica.

Cálculos:
- Churn agregado: 62/200 = 31%. Correcto.
- Churn plan gratuito: 60/178 = 33.7% (aprox)
- Churn plan pago: 2/22 = 9.09%

Observaciones importantes:
1. La métrica de 31% es un churn agregado que mezcla usuarios gratuitos y pagos. Esto es problemático porque usualmente el churn de gratuitos no es directamente comparable al de pagos, y depende del modelo de negocio.
2. Si el negocio principal es monetización (SAAS), el churn relevante es el de pagos, que es 9.09%, no 31%.
3. Sin embargo, 33.7% de churn en gratuitos también puede ser preocupante si son leads o si el modelo freemium depende de convertirlos.
4. El usuario pensaba que estaba en 5%. ¿De dónde sacó ese 5%? Quizás era el churn de pagos históricamente, o un benchmark, o confundió churn de cliente con churn de revenue (dollar churn).
5. Si el negocio depende de usuarios gratuitos (comunidad, ads), entonces 31% sí es grave.
6. Si es freemium con foco en pagos, el churn de pagos es 9.09%. Eso sigue siendo más alto que 5%, pero no es 31%.
7. También podría calcularse churn sobre usuarios activos vs totales. No tenemos datos de activos, pero sí de inicio de mes.

Plan de respuesta:
1. **Calma y prioridad**: Bajar la ansiedad. Explicar que probablemente está mirando una métrica mezclada (gratuitos + pagos) que no refleja la salud del negocio si el modelo es freemium.
2. **Verificación de la población**: Mostrar el desglose. El 31% es matemáticamente correcto como churn agregado, pero engañoso. La pregunta clave: ¿Qué población le importa al negocio?
3. **Análisis de gravedad**:
   - Si busca monetización: Churn de pagos = 9.1%. No es 31%, pero es casi el doble del 5% esperado. Requiere atención pero no es pánico.
   - Si el plan gratuito es embudo de conversión: 33.7% de churn gratuito es alto y puede estar dañando el funnel. Hay que investigar si son "usuarios de prueba" que nunca activaron o usuarios comprometidos.
   - Revenue churn vs User churn: Si los 2 pagos que se fueron son los de mayor valor, podría ser peor.
4. **Plan de acción inmediato (qué hacer ahora)**:
   - Paso 1: Segmentar永远. No tomar decisiones con el agregado.
   - Paso 2: Calcular churn correcto según objetivo de negocio (pagos, revenue, cohortes).
   - Paso 3: Analizar el "momento" de las bajas de los 2 pagos (cuándo se fueron, triggers).
   - Paso 4: Revisar si hubo cambio este mes (precio, bugs, competencia).
5. **Plan de acción a corto plazo**:
   - Cohort analysis: ¿Se fueron en mes 1 o usuarios antiguos?
   - Cálculo de churn ajustado: Net churn, gross churn, revenue churn.
   - Análisis de los 60 gratuitos: ¿Son cuentas fantasmas/trial no convertidas? Si es inicio de mes y muchos se fueron rápido, es churn de "no activados", no de "clientes".
   - Encuestas de salida (exit survey).
6. **Recomendaciones sobre el dashboard**:
   - Separar métricas de gratuito vs pago.
   - Usar denominador correcto: ¿Bajas/Inicio de mes? ¿O bajas/promedio del mes? ¿O bajas de cohorte?
   - Destacar churn de pagos como North Star si es SAAS.
7. **Comunicación**:
   - No informar a inversores/stakeholders el 31% sin contexto.
   - Preparar un brief con la segmentación.

Estructura de respuesta:
- Tranquilizo: no es 31% de tu negocio core (probablemente).
- Muestro los números re-desagregados.
- Evalúo gravedad por segmento.
- Doy pasos concretos ordenados por urgencia (hoy, esta semana, este mes).
- Incluyo un "chequeo de sanity" para el próximo mes.

Debo ser muy claro con los cálculos:
- Churn Gratuito: 60/178 = 33.7%
- Churn Pago: 2/22 = 9.1%
- Churn Agregado: 31%

Y plantear la pregunta estratégica: ¿Son esos 178 gratuitos realmente parte de tu base "retenible"? Si muchos se registran y nunca usan, tu "churn real de clientes potenciales" puede ser diferente.

También podría mencionar el problema del denominador. El churn de 62/200 usa inicio de mes. ¿Y si hubo altas durante el mes? Los 2000? No, solo tenemos inicio. Es standard para simplified churn, pero si hubo altas masivas a fin de mes, no se reflejan como bajas aún. Sin embargo, con estos números, no hay evidencia de altas. Asumo es un cálculo estándar.

Voy a darle un tono profesional, calmado, directo y accionable.

Plan detallado:
**Hoy (en las próximas 2 horas):**
1. Respira. El 31% es matemático pero falso en términos de negocio si eres freemium.
2. Revisa si tu "churn esperado del 5%" era de usuarios pagos. Si sí, tu churn pagos es 9.1%.
3. Aísla los datos de los 2 clientes pagos que se fueron. ¿Cuánto MRR/revenue representan? ¿Cuánto tiempo llevaban? ¿Qué plan?

**Esta semana:**
4. Cálculo de Revenue Churn (dollar churn) vs User churn.
5. Análisis de actividad de los 178 gratuitos: ¿Cuántos iniciaron sesión alguna vez? Los "churns" de inactivos no son churn, son limpieza.
6. Cohorte de los 60 gratuitos dados de baja: ¿Fueron altas de este mismo mes? Si es así, es problema de onboarding, no de retención.
7. Exit survey a los 2 pagos (y si se puede, a una muestra de gratuitos).

**Dashboard/Procesos:**
8. Cambiar el reporte principal para que muestre:
   - Churn de Usuarios Pagos (User Churn)
   - Churn de Revenue (Gross y Net)
   - Churn de Gratuitos (separado, y con filtro de "activos")
9. Definir qué es un "usuario" para tu métrica: ¿alguien que se registró o alguien que realizó la acción de valor?

**Gravedad final:**
- Si eres freemium/SAAS: Moderada. 9.1% de churn pagos es preocupante y merece investigación, pero no es una hemorragia del 31%.
- Si tu monetización es proporcional a base gratuita (ads): Grave. 33.7% de churn en la base es muy alto.
- Si es limpieza de cuentas inactiv