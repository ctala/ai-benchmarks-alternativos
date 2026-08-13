# Tencent Hy3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `tencent/hy3`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 60.947s | tokens_per_second: 80.5
- input_tokens: 224 | output_tokens: 4904

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

**Para:** Fundador  
**De:** Analista de Unit Economics  
**Asunto:** Veto a los $10.000 – Tu plan murió en la aritmética.

Como analista, mi trabajo es ser el tipo que apaga la música antes de que quemes la casa. Y con estos números, vas a incendiar tu caja rápido. **No le des.** Aquí está el parte forense de por qué tus números no cuadran:

### 1. Tu LTV es una fantasía (ignoras margen y churn)
Tu fórmula fue: Precio × Meses = 35 × 24 = $840.  
Cometiste dos errores mortales ahí:
*   **Olvidaste el margen bruto:** No ganas $35/mes, ganas el 70%. Tu beneficio bruto mensual real es **$24.50**.
*   **Inventaste la retención:** Dijiste "se queda unos 2 años". Pero con un churn del 8% mensual, la vida media matemática de un cliente es `1 / 0.08 = 12.5 meses`. Al mes 24, solo el 14% de tus clientes sigue contigo.

**LTV Real:**  
Beneficio mensual / Churn = 24.50 / 0.08 = **$306.25**

### 2. Tu ratio LTV/CAC está por los suelos
Tú creías que era 840 / 290 = 2.9 (que por cierto, ni siquiera es "más de 3", es menos).  
Pero el cálculo real es:  
306.25 / 290 = **1.05x**

Un ratio de 1.05 significa que por cada dólar que metes en publicidad, recuperas $1.05 en beneficio bruto a lo largo de **TODA** la vida del cliente. No queda ni un centavo para pagar tu salario, tu oficina o imprevistos. La regla de oro para escalar con paid media es 3x. Tú estás en 1x.

### 3. El Payback Period (Tiempo de recuperación) te mata
Para recuperar los $290 de CAC a razón de $24.50/mes, necesitas **11.8 meses**.  
El problema: con 8% de churn, a los 12 meses solo queda el 36% de esa cohorte. Básicamente recuperas tu inversión justo cuando la mayoría de los clientes ya canceló.

### 4. Autopsia de tus $10.000
Si metes $10.000 a $290 de CAC, compras ~34 clientes.
*   Beneficio bruto mes 1: $833
*   Beneficio bruto ACUMULADO en 12 meses (asumiendo el churn): **~$6.589**
*   **Resultado:** Pierdes $3.411 solo en el primer año de esa cohorte. Estarías pagando para regalar tu producto.

---

### Veredicto: NO LE DES.
Si escalas así, no estás comprando crecimiento, estás comprando deudas a plazo.

**Lo que tienes que hacer antes de aprobar ese gasto:**
1.  **Bajar el CAC:** Necesitas llevarlo a menos de $100 para que el negocio respire.
2.  **Matar el churn:** Si bajas el churn a 3%, la vida media sube a 33 meses y el LTV a $808 (ahí sí tendrías un ratio de 2.8x, cerca de salvable).
3.  **Subir el precio o hacer upsells:** A $35/mes con ese churn, el ticket es muy bajo para publicidad pagada agresiva.

Arregla la aritmética y vuelve. Hasta entonces, congelamos el presupuesto.