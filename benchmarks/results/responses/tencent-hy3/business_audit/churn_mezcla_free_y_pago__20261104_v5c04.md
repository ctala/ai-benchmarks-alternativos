# Tencent Hy3 — business_audit/churn_mezcla_free_y_pago

- model_id: `tencent/hy3`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 71.092s | tokens_per_second: 58.9
- input_tokens: 199 | output_tokens: 4190

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

Respira. Como analista de retención, lo primero que hago ante un número que salta así de repente es hacer una pausa y preguntar: **¿Qué población está midiendo realmente este 31%?**

El panel te está arrojando el **Churn de la Base Total** (Free + Paid). Es matemáticamente correcto (62 bajas / 200 usuarios = 31%), pero es una métrica "caja negra" que mezcla realidades comerciales completamente distintas. Antes de decretar la muerte del producto, vamos a verificar las poblaciones porque no es lo mismo perder usuarios que no te pagan nada, que perder clientes que generan ingresos.

### 1. Verificación de Poblaciones (El Desglose Real)
Si separamos las poblaciones con tus datos, la historia cambia por completo:

*   **Plan Gratuito:** 178 usuarios al inicio. 60 bajas.
    *   *Churn Gratuito:* 60 / 178 = **33.7%**
*   **Plan de Pago:** 22 usuarios al inicio. 2 bajas.
    *   *Churn de Pago (El que importa para tu supervivencia):* 2 / 22 = **9.09%**

### 2. ¿Qué tan grave es? (Diagnóstico)
*   **El 31% es una distracción estadística:** Si tu modelo es Freemium o tienes pruebas gratuitas, un churn alto en la base free es esperado (gente que se registra, curiosea y se va). El 33.7% en free merece atención en tu funnel de activación, pero no es una emergencia de liquidez.
*   **Tu 5% vs el 9.09%:** Probablemente tu "5%" era una intuición del churn de pagos (esperabas perder 1 de cada 20). Terminaste perdiendo 2 de 22. **Subió, pero ojo con el tamaño de muestra:** Con solo 22 usuarios de pago, **1 solo cliente que se va equivale a 4.5 puntos de churn**. Perder 2 en vez de 1 dispara el porcentaje, pero en volumen absoluto son solo 2 personas. Es una métrica volátil.

### 3. Plan de Acción Inmediato

**Paso 1: Reconfigura tu Dashboard (Segmentación)**
Pide al equipo de datos o configura tú mismo el panel para que el "Churn Principal" sea **exclusivamente de usuarios de pago** (Paid Logo Churn). El churn de free debe ir en un panel aparte de "Adquisición/Activación". Nunca mezcles ambas poblaciones en una sola métrica de retención.

**Paso 2: Autopsia de los 2 usuarios de pago (Root Cause Analysis)**
Contacta a esos 2 usuarios que se dieron de baja. ¿Fue por precio? ¿Por falta de una funcionalidad crítica? ¿O fue churn involuntario (tarjeta vencida)? Con una base de solo 22 usuarios, una conversación telefónica o encuesta de salida te dará más información que cualquier gráfico predictivo.

**Paso 3: Investiga el contexto del Free (¿De dónde vino el volumen?)**
Revisa tus cohortes de entrada. ¿Tuviste una campaña masiva el mes pasado que trajo 100 usuarios gratuitos que nunca volvieron a loguearse? Si el churn gratuito es de "inactividad", es normal; si son bajas activas (se dan de baja del todo), revisa tu onboarding.

**Paso 4: No actúes por pánico con el volumen**
No cambies toda tu estrategia de precios o producto por 2 bajas. Mira la tendencia de los últimos 6 meses. Si el churn de pago viene subiendo 1% cada mes, entonces sí hay una tendencia peligrosa; si fue un salto aislado de 5% a 9%, es ruido estadístico por tener una base pequeña.

**Paso 5: Cruza con Ingresos (MRR Churn)**
Si esos 2 usuarios que se fueron eran los planes más baratos, el impacto en tu caja es menor que si eran tus clientes más grandes. Asegúrate de saber qué porcentaje de tu MRR (Monthly Recurring Revenue) se fue volando con esas 2 bajas.

**Resumen:** No estás en 31%, estás en **9.09% de churn de pagos**. Es un aumento respecto a tu estimado del 5%, pero es manejable y el bajo volumen (2 usuarios) te permite hacer una acción quirúrgica en lugar de una reestructuración desesperada.