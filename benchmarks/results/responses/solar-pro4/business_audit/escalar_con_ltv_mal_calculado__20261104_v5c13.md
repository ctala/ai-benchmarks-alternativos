# Solar Pro 4 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 34.437s | tokens_per_second: 33.7
- input_tokens: 266 | output_tokens: 1161

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



No le doy. **Su plan tiene un error aritmético crítico que, si corrige, verá que escalar ahora es quemar cash.**

Usted está calculando el LTV como si fuera un contrato de dos años, cuando en realidad es una carrera contra el churn mensual. Aquí está la realidad de sus números:

### 1. El error en el LTV (La "Tasa de Descuento del Churn")
Usted calculó: $35 × 24 meses = $840.
**Esto está mal.** Con un churn del 8%, no hay ningún cliente que se quede exactamente 24 meses. La vida media (half-life) de su base es mucho menor.

*   **Vida media real:** $1 / 0.08 = 12.5$ meses.
*   **LTV Real (Ingreso):** $35 \times 12.5 = \$437.5$.
*   **LTV Real (Margen):** Usted aplicó el margen bruto (70%) al precio, pero no al LTV. El dinero que usted realmente conserva es el margen.
    *   LTV Real (Margen) = $437.5 \times 0.70 = \mathbf{\$306.25}$.

### 2. La relación LTV/CAC Real
*   **CAC:** $290.
*   **LTV (Margen):** $306.25.
*   **Ratio:** $306.25 / 290 = \mathbf{1.05}$.

**No es 2.9. Es 1.05.**

### 3. ¿Qué significa un ratio de 1.05?
Significa que por cada dólar que invierte en publicidad, recupera $1.05 en margen bruto a lo largo de la vida del cliente.
*   **No hay margen para operar:** Ese $0.05 no cubre sus costos fijos (RRHH, administración, impuestos, herramientas no incluidas en el margen bruto).
*   **Pérdida de cash:** Aunque el negocio sea "rentable" hoy (probablemente por clientes antiguos), cada nuevo cliente que adquiere con esos números **destruye valor**.
*   **Payback Period:** Si el margen mensual por cliente es $35 \times 0.70 = \$24.5$, y el CAC es $290, le tomará **11.8 meses** recuperar la inversión. Con un churn del 8%, el riesgo de que el cliente se vaya antes de pagarle su inversión es muy alto.

### 4. El riesgo de meter $10.000 ahora
Si invierte $10.000:
*   Adquiere **~34 clientes** nuevos ($10,000 / $290).
*   Genera **~$8,300** en margen bruto total a vida del cliente ($34 \times $306.25).
*   **Resultado:** Gasta $10,000 ahora para recibir $8,300 dispersos en el tiempo (y con riesgo de churn). Eso es una **pérdida neta de ~$1,700** en ese lote, sin contar los costos operativos de servir a esos 34 clientes nuevos.

### 5. El diagnóstico
Su producto tiene dos problemas estructurales visibles:
1.  **Churn muy alto (8% mensual):** Es ~66% anual. Esto mata la escalabilidad. Ningún negocio de suscripción escala bien con un churn así pagando un CAC de $290.
2.  **CAC alto para el ticket:** Un CAC de $290 para un producto de $35/mes requiere que el cliente sea extremadamente leal (años) o que tenga una tasa de upgrade muy alta. Con 8% de churn, la ecuación no cierra.

### 6. Mi recomendación
**No apruebo los $10.000 en publicidad.**

Antes de escalar, debe hacer ingeniería inversa:
1.  **Bajar el Churn:** Si baja el churn del 8% al 3%, la vida media sube a ~33 meses. El LTV (Margen) subiría a ~$800. Ahí sí sería escalable. El foco debe ser retención, no adquisición.
2.  **Bajar el CAC:** Con ese ticket, necesita un CAC menor a $150 para tener margen de maniobra con ese churn.
3.  **Validar el Payback:** ¿Puede pagar la inversión de $290 por cliente sin quebrarse de liquidez mientras espera los 12 meses de recuperación? Probablemente no.

**Veredicto:** Los números mueren en la aritmética. Con estos inputs, escalar publicidad es **escalar la pérdida**. Mejor use ese dinero en mejorar el producto o reducir el churn.