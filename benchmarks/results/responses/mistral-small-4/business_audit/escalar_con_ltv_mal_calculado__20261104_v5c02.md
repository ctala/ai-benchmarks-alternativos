# Mistral Small 4 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 6.89 | quality: 6.67
- latency_total: 5.086s | tokens_per_second: 166.7
- input_tokens: 224 | output_tokens: 848

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

Vamos a desglosar los números con rigor antes de aprobar el gasto en publicidad. Aquí hay varios ajustes críticos que podrían cambiar la decisión:

---

### **1. Corrección del LTV (no es $840)**
El cálculo simplista de LTV = Precio × Vida útil (2 años) ignora:
- **Churn real acumulado**: No todos los clientes duran 2 años. Con un churn del 8% mensual, la vida útil promedio real es:
  \[
  \text{Vida útil} = \frac{1}{1 - 0.08} \approx 12.5 \text{ meses}
  \]
  (No 24 meses). Esto reduce el LTV a:
  \[
  \text{LTV} = 35 \times 12.5 = \$437.5
  \]

- **Margen bruto recurrente**: El 70% es correcto, pero el LTV debe calcularse sobre el margen neto (no el ingreso bruto). Si hay otros costos fijos (ej. soporte, servidores), ajusta el LTV aún más.

---

### **2. LTV/CAC real (no 2.9)**
Con el LTV corregido:
\[
\text{LTV/CAC} = \frac{437.5}{290} \approx 1.51
\]
Esto está **por debajo del umbral mínimo de 3** (regla de oro para escalar con publicidad). Un ratio < 3 indica que el negocio no es sostenible a largo plazo con estos números.

---

### **3. Sensibilidad del CAC**
- **¿El CAC de $290 incluye impuestos, fees de agencia o escalará con la inversión?** Si no es escalable, el ratio empeorará.
- **¿El margen bruto del 70% se mantiene con el crecimiento?** A veces el soporte o infraestructura no escala linealmente (ej. servidores).

---

### **4. Alternativas antes de escalar**
- **Optimizar el churn**: Reducir del 8% al 5% aumenta el LTV a ~$538 (vida útil = 20 meses), mejorando el LTV/CAC a 1.85.
- **Reducir el CAC**: Pruebas con canales orgánicos o referidos podrían bajarlo a $200, llevando el ratio a 2.19.
- **Aumentar el precio**: Si el mercado lo permite, subir a $40/mes mejora el LTV a $500 (con vida útil de 12.5 meses), dando un ratio de 1.72.

---

### **5. Prueba controlada (no $10K de golpe)**
En lugar de invertir $10K inmediatamente:
- **Prueba con $1K-2K**: Valida si el CAC se mantiene con volumen. Si el ratio no mejora, el plan de escalar con publicidad es insostenible.
- **Modelo de cohortes**: Seguimiento de los clientes adquiridos para ajustar churn y LTV en tiempo real.

---

### **Conclusión**
**No apruebes $10K en publicidad aún.** Los números actuales muestran un LTV/CAC < 3, lo que significa que cada dólar invertido en adquirir clientes está generando menos de $1.5 en retorno. Esto no es escalable y quemará caja rápidamente.

**Recomendación:**
1. Reducir el churn (prioridad absoluta).
2. Mejorar el LTV o reducir el CAC antes de escalar.
3. Si los ajustes no son posibles, considera pivotar el modelo (ej. aumentar precios, enfocarte en clientes B2B con menor churn).

*Muchos planes mueren en la aritmética... pero esta vez se puede salvar con ajustes.*