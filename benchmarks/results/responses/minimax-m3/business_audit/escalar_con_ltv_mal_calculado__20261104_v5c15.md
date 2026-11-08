# MiniMax M3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 99.568s | tokens_per_second: 98.2
- input_tokens: 364 | output_tokens: 9773

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

**No liberaría los $10.000 de golpe con esos números.** La publicidad pagada sería marginalmente positiva, pero no un motor de crecimiento con suficiente margen.

### Tu cálculo mezcla tres supuestos Incorrectos

1. **Un churn mensual de 8% no equivale a 24 meses de retención.**

   Si el churn fuera constante:

   \[
   \text{Vida esperada}=\frac{1}{0{,}08}=12{,}5\text{ meses}
   \]

   Además, solo el **13,5%** de los clientes seguiría activo después de 24 meses:

   \[
   0{,}92^{24}=13{,}5\%
   \]

   El cliente mediano se va antes del mes 9.

2. **Para compararlo con CAC, el LTV debe usar margen bruto, no solo ingresos.**

   Cada cliente deja:

   \[
   \$35 \times 70\%=\$24{,}50
   \]

   de contribución mensual.

3. **2,9x no está por encima de 3x.** Y aun aceptando tus 24 meses, el ratio relevante sería:

   \[
   \frac{\$35 \times 24 \times 70\%}{\$290}
   =\frac{\$588}{\$290}
   =2{,}03x
   \]

### Recálculo con tu churn real

| Métrica | Resultado |
|---|---:|
| Contribución mensual | $24,50 |
| Vida esperada | 12,5 meses |
| LTV de contribución | $306,25 |
| LTV/CAC | **1,06x** |
| Payback del CAC | **11,8 meses** |

Este LTV es incluso **sin descontar dinero**. Con descuento, el resultado es peor.

### Qué 返回ían los $10.000

Suponiendo CAC constante de $290:

- Clientes nuevos: \(10.000 / 290 \approx 34,5\)
- Contribución de por vida: \(34,5 \times \$306,25 \approx \$10.560\)
- Menos publicidad: **$10.000**
- Margen antes de costos fijos: **aprox. $560**

Es decir, solo un **5,6% de cushion**. Un pequeño aumento del churn o del CAC lo vuelve negativo. Y el negocio tendría que financiar aproximadamente un año de payback antes de recuperar la inversión.

### Mi recomendación

**No hagas el desembolso completo todavía.** Haría una prueba por tranches, por ejemplo $3.000–$5.000 iniciales, y reservaría el resto. Solo escalaría si:

- El CAC marginal y completamente cargado baja a **≈$100–$102** para lograr 3x con el churn actual.
- El churn de la cohorte pagada se demuestra por debajo de aproximadamente **3% mensual**.
- El payback baja a **5–6 meses**.
- La prueba demuestra clientes incrementales, no solo conversiones atribuidas.

Con CAC de $290, necesitarías bajar el churn a **2,8%** para alcanzar 3x. Una reducción de churn de 8% a 4% ya duplicaría el LTV de contribución de $306 a $613.

**Conclusión:** tu negocio existente puede ser rentable, pero la adquisición pagada, con estos números, no merece un compromiso de $10.000 de inmediato. Priorizaría retención yCAC antes que aumentar el presupuesto.