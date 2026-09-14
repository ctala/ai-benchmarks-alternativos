# Muse Spark 1.3 — business_audit/churn_mezcla_free_y_pago

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 23.978s | tokens_per_second: 132.3
- input_tokens: 180 | output_tokens: 3172

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

Respira. No tienes un churn del 31%. Tienes un problema de tablero que mezcla dos poblaciones distintas.

Como analista de retención, regla #1: **antes de interpretar una métrica, verifica qué población está midiendo realmente.**

Tu panel lo hizo mal. Mezcló gratis + pago.

Vamos a separarlo:

### 1. El recálculo que te quita el pánico

Tu fórmula actual:
62 bajas / 200 usuarios inicio = **31% blended**. Matemáticamente correcto, empresarialmente inútil.

La realidad segmentada:

**Plan Gratuito:**
60 bajas / 178 usuarios = **33.7% de churn mensual free**

**Plan de Pago (lo que realmente te da de comer):**
2 bajas / 22 usuarios = **9.1% de logo churn mensual paid**

No perdiste el 31% de tu negocio. Perdiste 2 clientes de pago.

Tu 5% que recordabas era casi seguro solo de pago. Comparar 5% paid vs 31% blended es comparar peras con manzanas.

### 2. ¿Qué tan grave es entonces?

Grave: no. Para vigilar de cerca: sí.

1.  **No es una emergencia existencial.** El 31% es ruido de usuarios gratuitos. El free siempre churna a 30-40% mensual. Es normal, no pagan, no duele en caja.

2.  **El 9.1% paid sí es alto, pero no es 31%.** Un 9% mensual sostenido significa que en un año perderías ~68% de tus clientes de pago. Un 5% mensual ya implica perder ~46% al año. Ambos son altos para SaaS. Tienes que bajarlo a <3-5%, pero no te vas a morir este mes.

3.  **Con 22 clientes, todo es volátil.** Cada baja de pago te suma 4.5 puntos de churn (1/22). Pasar de 1 baja (4.5%) a 2 bajas (9.1%) parece que "se duplicó", pero estadísticamente es normal.

De hecho: si tu tasa real fuera 5%, la probabilidad de ver 2 o más bajas en un mes con 22 clientes es del **~30%**. O sea, 1 de cada 3 meses te va a pasar esto aunque nada haya empeorado. No puedes tomar decisiones drásticas con esta muestra.

Conclusión: No es para entrar en pánico, es para corregir el tablero y hablar con esos 2 clientes.

### 3. Tu plan en 3 tiempos

**HOY (en 2 horas): Arregla la métrica**

Deja de mirar el churn total. Crea 3 métricas separadas en tu panel:

1.  **Paid Logo Churn:** `bajas de pago / clientes de pago a inicio de mes` -> Hoy: 9.1%
2.  **Revenue Churn (MRR):** `MRR perdido por bajas / MRR a inicio de mes`. Esta es la más importante. Si esos 2 eran tus planes más baratos, tu daño real es aún menor.
3.  **Free Churn / Activación:** No lo llames churn. Mide `% de gratis que activan y % que convierten a pago`.

Y pon un filtro por defecto: `WHERE plan = 'paid'`. El blended que te asustó, bórralo del dashboard principal.

Comunicación para tu equipo: "No tuvimos 31% de churn. Tuvimos 9.1% en pago (2 cuentas) y 33.7% en free (60 cuentas). El panel estaba mezclando poblaciones."

**ESTA SEMANA: Investiga las 2 bajas que importan**

Con solo 2, no necesitas estadística, necesitas nombres y apellidos.

1.  ¿Quiénes eran? Tenure, plan, uso últimos 30 días, tickets.
2.  Contacto personal de salida (tú, no un email automático). Pregunta: ¿Qué esperabas lograr? ¿Qué falló? ¿A dónde te vas?
3.  Clasifica: ¿Fue evitable (soporte, onboarding, precio, falta feature) o inevitable (cerró empresa, dejó proyecto)?

Para los 60 gratis, no los llames. Segmenta el export:
¿Llevaban <7 días y nunca activaron? Eso no es churn, es fallo de activación. ¿Llevaban >3 meses activos? Esos sí míralos.

**ESTE MES: Evita el próximo susto**

1.  Define "baja" bien: Para free, un usuario inactivo no es baja. Solo cuenta baja si borró cuenta. Si no, mide retención por cohorte.
2.  Mide por cohortes, no por mes calendario. ¿Qué % de los pagos que entraron en Enero siguen en mes 1, 2, 3?
3.  Pon alertas inteligentes: Con n=22, no alertes por %. Alerta por "cada baja de pago > X MRR me avisa por Slack".

¿Quieres que lo hagamos juntos ahora? Pásame el MRR de esos 22 clientes y el MRR que perdiste con esas 2 bajas, y te calculo tu Revenue Churn real, que es el número que de verdad define qué tan grave fue este mes.