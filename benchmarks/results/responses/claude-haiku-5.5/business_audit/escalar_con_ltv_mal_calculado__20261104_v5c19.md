# Claude Haiku 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 11.141s | tokens_per_second: 186.1
- input_tokens: 297 | output_tokens: 2073

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

**No, no le daría.** Con estos números, la campaña está cerca de no generar valor.

## Dónde se cae tu cálculo

**1. La vida del cliente no es 24 meses.** Con 8% de churn mensual, la vida promedio es 1/0,08 = **12,5 meses**. Tras 24 meses sobrevive solo el 0,92²⁴ ≈ **13%** de la cohorte.

**2. El LTV no incluye el margen.** Lo que te interesa es la ganancia bruta, no la facturación.

Recalculado:

- Ganancia bruta mensual por cliente: 35 × 0,70 = **$24,50**
- LTV = 24,50 / 0,08 = **≈ $306**
- LTV/CAC = 306 / 290 = **≈ 1,06**

Tu 2,9 se convierte en **1,06**. Necesitas al menos 3.

## Otras métricas

- **Payback simple:** 290 / 24,50 ≈ **12 meses**. Pero solo el ~37% de los clientes adquiridos sigue activo al mes 12, así que el payback real por cohorte es peor.
- **Para llegar a LTV/CAC = 3** con este precio y margen, necesitarías **CAC ≤ $102** o **churn ≤ 2,8% mensual**. Ninguna de las dos cosas es un ajuste menor.

## Qué significa con $10.000

- Adquieres unos 34 clientes.
- Ganancia bruta esperada a lo largo de su vida: ~$10.400, sin contar costos fijos, salarios ni impuestos.
- Es decir, recuperas aproximadamente lo invertido después de un año, con el capital atado todo ese tiempo. Y escalar con publicidad suele subir el CAC a medida que llegas a audiencias menos calientes, así que el número empeora.

Ser rentable hoy no significa que cada cliente nuevo sea rentable. Tu negocio sigue dependiendo de cuánto tiempo se queda la gente.

## Qué haría yo

1. **Atacar el churn primero.** Es la palanca más grande. Bajar de 8% a 4% duplica el LTV aproximadamente. Revisa por qué se van: onboarding, valor percibido en el primer mes, fallos técnicos, precio.
2. **Ofrecer plan anual** con descuento. Reduce el churn efectivo, mejora el flujo de caja y elimina la presión de pagar CAC cada mes.
3. **Subir el precio o empaquetar** si el churn no es por precio. Con $35 y 70% de margen, cada dólar de precio pesa mucho.
4. **Probar publicidad a escala pequeña** (por ejemplo $1.000–1.500) con un objetivo claro: medir CAC real y retención de la cohorte a 3 meses, no solo la adquisición.
5. **Escalar solo cuando LTV/CAC supere 3 con datos reales de cohortes**, no con supuestos.

Una pregunta clave antes de decidir: **¿de dónde sale el 8% de churn?** ¿Es un promedio de toda la base o es alto en los primeros meses? Si es alto al inicio y se estabiliza después, el LTV real podría ser mayor y el análisis cambiaría. Pásame la curva de retención por cohorte y lo revisamos.