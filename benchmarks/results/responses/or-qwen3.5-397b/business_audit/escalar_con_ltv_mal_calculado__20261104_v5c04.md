# Qwen 3.5 397B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.42 | quality: 10.0
- latency_total: 46.792s | tokens_per_second: 61.0
- input_tokens: 217 | output_tokens: 2856

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

**No le des. Detén esa inversión inmediatamente.**

Tu plan no muere en la estrategia, muere en la aritmética. Has cometido dos errores fundamentales en tu cálculo que ocultan una realidad peligrosa: estás comprando dólares a 95 centavos y perdiendo efectivo cada mes.

Aqu está el recálculo real:

### 1. El error de la vida útil del cliente
Asumes que el cliente se queda 24 meses fijos. Con un **churn mensual del 8%**, eso es matemáticamente imposible.
*   **Fórmula correcta de vida media:** `1 / Tasa de Churn Mensual`
*   **Tu vida media real:** `1 / 0.08` = **12.5 meses** (no 24).
*   *Realidad:* Pierdes casi la mitad de tu base de clientes cada año. Tienes un "balde agujereado".

### 2. El error del Margen Bruto
El LTV para comparar con CAC debe basarse en el **beneficio bruto**, no en ingresos totales. El CAC se paga con caja real, no con facturación bruta.
*   **Margen bruto por cliente/mes:** `$35 * 70%` = **$24.50**.

### 3. Tus números reales (Unit Economics Corregidos)

| Concepto | Tu cálculo | Cálculo Real |
| :--- | :--- | :--- |
| **Vida media del cliente** | 24 meses | **12.5 meses** |
| **Contribución mensual** | $35.00 | **$24.50** |
| **LTV (Gross Margin)** | $840 | **$306** (`$24.5 / 0.08`) |
| **CAC** | $290 | **$290** |
| **Ratio LTV:CAC** | 2.9x | **1.05x** |
| **Payback Period** | ~8 meses | **11.9 meses** |

### El Veredicto

1.  **Ratio LTV:CAC de 1.05x:** Esto es zona de muerte para escalar con publicidad. Por cada $1 que inviertes en ads, recuperas $1.05 en margen bruto *a lo largo de toda la vida del cliente*. Esto no cubre tus costos fijos (sueldos, oficina, software, tu tiempo). **Estás operando casi al punto de equilibrio variable, lo que significa pérdida neta.**
2.  **Payback de 12 meses:** Tardas un año en recuperar el costo de adquisición. Si inviertes $10,000 hoy, no ves ese cash flow de vuelta hasta dentro de un año. Mientras tanto, el churn se come tu base. Necesitarías un capital de trabajo enorme para sostener esto.
3.  **Churn del 8% mensual:** Ninguna estrategia de adquisición funciona con un churn tan alto. Estás intentando llenar una piscina con una manguera mientras el desagüe está abierto al máximo.

### Recomendación

**No gastes los $10,000 en publicidad.**

1.  **Prioridad 1 (Retención):** Tu foco debe ser bajar ese churn del 8% al menos al 3-4%. Si bajas el churn al 4%, tu vida media sube a 25 meses y tu LTV se duplica a ~$612. Ahí sí tendrías un ratio saludable (~2.1x) y podrías pensar en escalar.
2.  **Prioridad 2 (CAC):** Si el churn no se puede bajar rápido, necesitas reducir el CAC de $290 a algo más cercano a $100-$150 para que los números cierren con tu margen actual.

**Conclusión:** Escalar ahora solo acelerará tu quema de caja sin construir valor sostenible. Arregla el producto o la retención primero.