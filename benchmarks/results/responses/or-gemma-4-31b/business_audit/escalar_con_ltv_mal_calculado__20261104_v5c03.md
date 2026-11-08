# Gemma 4 31B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 13.505s | tokens_per_second: 65.2
- input_tokens: 210 | output_tokens: 881

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

**No. Detente.**

Como analista de unit economics, mi trabajo es matar los planes que parecen buenos en un Excel pero que quiebran la caja en la realidad. Tu cálculo tiene tres errores críticos de aritmética y flujo de caja que convertirían esos $10,000 en un agujero negro.

Aquí está la autopsia de tus números:

### 1. El error del LTV "Nominal" vs. LTV "Marginal"
Calculaste el LTV basándote en el precio ($35), pero el LTV debe calcularse sobre el **Margen Bruto**. No puedes pagar publicidad con dinero que ya se fue en infraestructura y comisiones.

*   **Tu margen bruto por cliente:** $35 × 70% = **$24.50/mes**.
*   **Tu LTV Real (Marginal):** $24.50 / 0.08 (churn) = **$306.25**.

Tu LTV no es $840, es **$306**.

### 2. La falacia de la "Vida Útil" (Lifetime)
Dices que un cliente se queda "unos 2 años". Matemáticamente, con un churn del 8%, la vida media de un cliente es:
$1 / 0.08 = \mathbf{12.5 \text{ meses}}$.

Estás sobreestimando la retención por casi un año entero. Estás calculando el éxito basándote en un escenario optimista, no en la realidad de tu churn actual.

### 3. El Ratio LTV/CAC Real
Recalculemos el ratio con los números reales:
$$\text{LTV Marginal } (\$306.25) / \text{CAC } (\$290) = \mathbf{1.05}$$

Un ratio de **1.05 es una zona de peligro**. En el mundo del SaaS, un ratio < 3 es ineficiente; un ratio cercano a 1 significa que básicamente estás intercambiando dólares por dólares, pero después de pagar salarios, alquiler y costos operativos (OPEX), **estás perdiendo dinero por cada cliente que traes**.

---

### El golpe de gracia: El Payback Period (Tiempo de recuperación)
Aquí es donde muere tu flujo de caja. El Payback Period es cuánto tardas en recuperar el CAC usando el margen bruto mensual.

$$\text{CAC } (\$290) / \text{Margen Mensual } (\$24.50) = \mathbf{11.8 \text{ meses}}$$

**Esto es insostenible.** Tardas casi un año en recuperar la inversión de un solo cliente. 

Si metes $10,000 hoy:
1. Adquieres aproximadamente 34 clientes.
2. Gastas $10,000 hoy.
3. Esos clientes te devuelven $833 al mes (en margen bruto).
4. Tardarás **12 meses** solo para recuperar esos $10,000, asumiendo que ninguno se vaya antes (pero sabemos que el 8% se va cada mes).

### Veredicto Final: NO APROBADO.

Si escalas ahora, vas a quemar tu rentabilidad actual para alimentar un crecimiento que no se paga a sí mismo. Estarás "comprando" crecimiento muy caro y poniendo en riesgo la supervivencia de la empresa.

**¿Qué tienes que hacer antes de invertir un solo dólar más en Ads?**
1. **Bajar el Churn:** Si bajas el churn del 8% al 4%, tu LTV se duplica y el plan empieza a tener sentido.
2. **Subir el Precio:** Si subes a $50/mes, el Payback Period cae drásticamente.
3. **Optimizar el CAC:** Tienes que encontrar una forma de adquirir clientes por debajo de $150 para que el negocio sea saludable.

**No escales un problema; escala una máquina que ya funcione.**