# Tencent Hy3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `tencent/hy3`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 78.619s | tokens_per_second: 58.2
- input_tokens: 224 | output_tokens: 4579

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

Como analista, mi trabajo es ser el tipo que apaga las luces antes de que quemes la caja. Y aquí hay fuego.

**NO le des.** Tu plan no solo muere en la aritmética, está clínicamente muerto en ella. Tienes dos errores fatales que inflan tu LTV artificialmente y te van a secar el flujo de caja.

**Error 1: La matemática del Churn (El fantasma de los 2 años)**
Dices que el cliente se queda "unos 2 años" (24 meses). Pero también dices que tu churn mensual es 8%. Esas dos afirmaciones son mutuamente excluyentes. 
La vida media de un cliente no es una suposición, es una división: `1 / Churn Mensual`.
`1 / 0.08 = 12.5 meses`.
Con un 8% de churn mensual, pierdes casi el 64% de tu base cada año. El cliente promedio no se queda 2 años, se queda 1 año y poco.

**Error 2: El LTV no es Facturación, es Margen**
Calculaste el LTV con los $35 brutos. Pero tu margen bruto es 70%. El dinero real que genera un cliente por mes es:
`$35 * 0.70 = $24.50`

*(Y por cierto, 840 / 290 da 2.89, lo cual ya está **por debajo** de 3, no "por encima más o menos". Pero aún así, ese 2.89 es una alucinación óptica).*

**El LTV y Ratio Real**
Si corregimos ambos:
*   **LTV Real** = Margen mensual × Vida media = `$24.50 * 12.5 = $306.25`
*   **LTV/CAC Real** = `$306.25 / $290 = 1.05`

No estás en 2.9, estás en **1.05**. Un ratio saludable para escalar es >3. Aquí apenas estás rompiendo incluso a nivel de margen bruto (y ya estarías perdiendo a nivel de EBITDA porque no estás contando sueldos, software, contabilidad, etc.).

**El Peligro de los $10.000**
Si metes $10.000 a $290 de CAC, compras ~34 clientes.
*   Inversión hoy: -$10.000
*   Margen bruto generado en esos 12.5 meses de vida: 34 clientes * $306.25 = ~$10.412
*   **Ganancia neta de margen:** $412 dólares en más de un año. Mientras tanto, congelaste $10k de tu caja hoy.

Además, tu **Payback Period** (tiempo para recuperar el CAC con margen) es de `290 / 24.5 = 11.8 meses`. Tu cliente se va al mes 12.5. Estás al borde del abismo: si al escalar el CAC sube a $310 o el churn a 9% (cosa que pasa siempre al escalar presupuesto), cada cliente que traigas será una pérdida de capital garantizada.

**Veredicto:**
No le des. El motor de adquisición quema casi tanto como produce. Antes de invertir en paid media, tienes que:
1. Bajar el churn drásticamente (meta: <3% mensual).
2. Subir el precio o el margen.
3. Bajar el CAC a menos de $100.

Arregla la unidad primero. Escalar un modelo con LTV/CAC de 1 es escalar una hoguera de dinero.