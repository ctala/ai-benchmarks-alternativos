# Tencent Hy3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `tencent/hy3`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 56.663s | tokens_per_second: 72.7
- input_tokens: 224 | output_tokens: 4121

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

Como analista de unit economics, mi trabajo es ser el tipo que apaga las luces de la fiesta antes de que quemes la casa. Y con estos números, la casa se incendia.

**Veredicto: No le das. El plan ya murió en la aritmética.**

Vamos a destripar tu cálculo paso a paso, porque tienes tres errores gravísimos que te están haciendo ver fantasmas:

### 1. Error de Margen (El LTV no se calcula con ingresos, sino con utilidad)
Dices que el precio es $35, pero aclaraste que tu margen bruto es del 70% (después de infra y procesador). Eso significa que tu ganancia real por cliente al mes es:
**$35 × 0.70 = $24.50/mes**
En tu cálculo usaste los $35 enteros para el LTV. Ya de entrada estás sobreestimando tu rentabilidad en un 30%.

### 2. Error de Retención (El churn no es una suposición, es matemática pura)
Asumiste que el cliente se queda 24 meses (2 años). Pero dijiste que tu churn mensual es del 8%. 
La vida útil promedio de un cliente no se adivina, se calcula así:
**Vida útil = 1 / Churn mensual = 1 / 0.08 = 12.5 meses**
No son 24 meses. Con un 8% de churn mensual, al mes 12 solo queda viva el 37% de tu base, y al mes 24 solo el 13%. Tu suposición de 2 años duplica la realidad.

### 3. El LTV y el Ratio Real
Hagamos la aritmética correcta con los datos reales:
*   **LTV real** = Utilidad mensual × Vida útil promedio
*   **LTV real** = $24.50 × 12.5 = **$306.25**

Ahora el ratio LTV/CAC que tanto te importa:
*   $306.25 / $290 = **1.05**

Lejos de estar "por encima de 3 más o menos" (y ojo, 2.9 tampoco es estar por encima de 3), estás en **1.05**. 

### Por qué esto es una trampa mortal al escalar
1. **No hay margen para gastos operativos:** Un LTV/CAC de 1.05 significa que apenas y recuperas el costo de adquisición con tu margen bruto. ¿Y los sueldos de tu equipo? ¿Y las licencias? ¿Y los impuestos? Con ese ratio, **estás perdiendo dinero neto en cada cliente que compras.**
2. **Payback period (Tiempo de recuperación):** Tardas $290 / $24.5 = **11.8 meses** en recuperar lo que gastaste en ads. Como el cliente promedio se va a los 12.5 meses, básicamente recuperas la inversión justo cuando el cliente está haciendo las maletas. No te da tiempo de generar utilidad neta.
3. **La inflación del CAC:** Quieres meter $10,000 de golpe ("escalar fuerte"). Al aumentar abruptamente el gasto en paid media, el CAC casi siempre sube por saturación de audiencia. Si tu CAC pasa de $290 a $350 (muy común al escalar), tu ratio cae a 0.87. Por cada $1 que inviertes, pierdes 13 centavos de margen bruto.

### Conclusión y recomendación
No metas los $10,000 en publicidad pagada todavía. Antes de pedirme que apruebe un plan de crecimiento, tienes que arreglar la base:
* **Baja el churn:** Un 8% mensual es altísimo. Si lo bajas al 4%, tu vida útil se duplica a 25 meses y tu LTV sube a $612 (ratio 2.1, mucho más sano).
* **Sube el precio o mejora el margen:** Un pequeño aumento de precio cambia las matemáticas drásticamente a tu favor.
* **Prueba canales más baratos:** Con un CAC de $290, necesitas eficiencia extrema. Busca SEO, referidos o venta directa (outbound) antes de pagarle a Meta o Google.

El plan de crecimiento no se aprueba. Vuelve a la pizarra.