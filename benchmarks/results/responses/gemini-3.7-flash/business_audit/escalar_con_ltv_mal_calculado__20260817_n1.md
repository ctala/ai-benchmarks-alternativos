# Gemini 3.7 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 13.443s | tokens_per_second: 152.0
- input_tokens: 192 | output_tokens: 2044

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

**No. Frena en seco.** Si metes esos $10.000 hoy, vas a quemar el dinero. 

Tu cálculo tiene dos errores matemáticos graves que distorsionan por completo la viabilidad del negocio. Vamos a recalcular tus Unit Economics reales:

---

### 1. Los dos errores en tu cálculo

* **Error 1: El tiempo de vida (Lifespan).**
  Un churn mensual del 8% no da 2 años de vida. La fórmula estándar de vida media de un cliente es $1 / \text{Churn}$. 
  $$1 / 0,08 = \mathbf{12,5 \text{ meses (no 24)}}$$
  *(A los 24 meses, con un churn del 8%, ya habrá desaparecido el 86% de tu cohorte).*

* **Error 2: Calculaste el LTV sobre ingresos brutos, no sobre margen.**
  El LTV no se calcula sobre la facturación, sino sobre la contribución marginal (tu margen bruto del 70%). El procesador de pagos y los servidores no son gratis.

---

### 2. Tus números reales

* **Margen de contribución mensual por cliente:** $\$35 \times 70\% = \mathbf{\$24,50}$
* **LTV Real:** $\$24,50 \times 12,5 \text{ meses} = \mathbf{\$306,25}$
* **CAC:** $\$290,00$

$$\text{LTV / CAC Real} = \frac{\$306,25}{\$290} = \mathbf{1,05x}$$

*(Un ratio saludable en B2B/B2C SaaS pagado debe ser de **3,0x a 4,0x**).*

---

### 3. El tiempo de recuperación (CAC Payback)

* **Meses para recuperar el CAC:** $\frac{\$290}{\$24,50} = \mathbf{11,8 \text{ meses}}$

Tardas **12 meses en recuperar lo que te costó adquirir al cliente**. Como la vida media es de 12,5 meses, el cliente se va prácticamente en el momento exacto en que empatas el gasto publicitario. Peor aún: **más del 60% de los clientes que adquieras habrán cancelado antes de que logres recuperar su CAC individual**.

---

### 4. Qué pasaría si gastas los $10.000 este mes:

1. Adquieres **34 clientes** ($\$10.000 / \$290$).
2. A lo largo de toda su vida útil, esos 34 clientes te generarán un margen bruto total de **$10.412**.
3. **Ganancia bruta total tras más de un año:** **+$412**.
4. Una vez que descuentes costos fijos, nóminas, soporte y atención al cliente, **habrás perdido dinero**.

---

### Diagnóstico y qué hacer antes de escalar:

Tu plan no funciona porque tu **churn es demasiado alto (8%)** para un ticket tan bajo ($35) y un CAC tan caro ($290).

Para que la pauta publicitaria funcione, debes mover al menos una de estas palancas:
1. **Bajar el Churn:** Si bajas del 8%