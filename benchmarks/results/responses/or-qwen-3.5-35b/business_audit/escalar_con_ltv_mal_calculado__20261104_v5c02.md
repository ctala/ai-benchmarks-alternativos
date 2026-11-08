# Qwen 3.5 35B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 15.113s | tokens_per_second: 173.8
- input_tokens: 217 | output_tokens: 2627

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

**Veredicto: NO.**

No presiones el botón de los $10.000. Tu cálculo de LTV es incorrecto y tu estructura de costos oculta un riesgo financiero grave. Si ejecutas este plan, quemarás efectivo sin recuperar la inversión antes de que tus clientes se vayan.

Aquí está el análisis forense de por qué tu aritmética está fallando y por qué este plan te llevará a la quiebra operativa, aunque seas "rentable" hoy.

### 1. El error del LTV (Vida del Cliente)
Estás calculando el LTV como si fuera un contrato fijo de 24 meses. Con un churn del 8% mensual, esa suposición es falsa.

*   **Tu cálculo:** 24 meses.
*   **La realidad:** $1 / 0.08 = 12.5$ meses de vida promedio.
*   **Impacto:** La mitad de tus ingresos proyectados desaparecen en la hoja de cálculo.

### 2. El error del Margen (Ingresos vs. Flujo de Caja)
Calculas el LTV sobre el precio bruto ($35). Pero para escalar con publicidad, necesitas saber cuánto **flujo de caja neto** genera cada cliente después de cubrir sus costos directos.

*   **Precio:** $35
*   **Margen Bruto:** 70%
*   **Contribución Mensual Real:** $35 × 0.70 = **$24.50**

Nunca recuperas $35. Solo recuperas $24.50 mes a mes.

### 3. La cuenta real (El LTV Correcto)
Rehagamos la fórmula con los datos reales de churn y margen:

*   **LTV Real (Flujo de Caja):** $24.50 (contribución) × 12.5 (meses de vida) = **$306.25**
*   **Tu CAC:** $290
*   **Tu Ratio LTV/CAC Real:** $306.25 / $290 = **1.05**

Un ratio de 1.05 es **punto muerto**. Significa que apenas recuperas lo invertido al final de la vida del cliente. Un negocio saludable necesita un ratio de **3x o superior**.

### 4. El problema silencioso: Payback Period (Recuperación)
Este es el punto donde mueren las startups más rápido. ¿Cuánto tardas en recuperar los $290 que gastaste en publicidad?

*   **Costo de Adquisición:** $290
*   **Entrada mensual neta:** $24.50
*   **Meses para recuperar CAC:** $290 / 24.50 ≈ **11.8 meses**

**El peligro:** Tardarás casi **1 año entero** en recuperar lo que gastaste en adquirir a ese cliente. Mientras tanto, estás pagando infraestructura, salarios y el propio CAC desde tu bolsillo o caja acumulada. Si escalas $10.000 hoy, necesitarás una línea de crédito o capital de trabajo masivo porque no verás retorno hasta dentro de un año.

### 5. El Churn del 8% es una alarma roja
Para un modelo B2B/SaaS de $35/mes, un churn mensual del 8% es altísimo.
*   Esto indica que tu producto no retiene valor suficiente o que estás comprando tráfico mal segmentado.
*   Al escalar publicidad, el churn suele empeorar ligeramente porque atraes a usuarios menos cualificados.
*   Si el churn sube solo 1% (a 9%), tu vida media baja a 11 meses y tu LTV cae a **$269.50**. En ese escenario, **estás perdiendo dinero por cada cliente nuevo ($20 pérdidas)**.

---

### Mi recomendación directa:

1.  **Bloquea el gasto de $10.000:** No inviertas un centavo más hasta cambiar estas métricas.
2.  **Reduce el Churn:** Antes de vender más, asegúrate de que los clientes actuales se queden. Baja el churn mensual al menos al 3-4%. Eso duplicará tu LTV automáticamente.
3.  **Negocia o reduce el CAC:** O busca canales orgánicos. Si no puedes bajar el CAC a menos de $100, la matemática no cierra.
4.  **Prueba de Concepto:** Invierte $500 en prueba. Mide el **payback period real**. Es muy probable que descubras que tardas 12 meses en recuperar el costo, lo cual invalida la estrategia de crecimiento agresivo.

**Resumen:** Eres rentable hoy probablemente porque tienes bajo volumen o bajos costos operativos fijos. Escalar con estas unidades económicas significa **quemar caja linealmente**. Corrige la unidad económica antes de apalancarte.