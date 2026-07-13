# Kimi K2.7 Code — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.59 | quality: 8.4
- latency_total: 9.94s | tokens_per_second: 202.2
- input_tokens: 231 | output_tokens: 2010

## Respuesta completa

 No. No le doy, y por una razón aritmética, no de opinión.

Tu cálculo tiene tres errores graves:

1. **Confundes “tiempo máximo” con “vida útil esperada”.**
   Un churn del 8 % mensual no significa que todos se queden 24 meses. Significa que, en promedio, un cliente se queda:

\[
   \text{Vida media} = \frac{1}{\text{churn mensual}} = \frac{1}{0,08} = 12{,}5 \text{ meses}
   \]

A los 12 meses solo queda el **37 %** de la cohorte; a los 24 meses, el **8 %**. No puedes multiplicar $35 × 24.

2. **Usas ingreso bruto en lugar de margen bruto.**
   Lo que recuperas por cliente es el margen, no el precio. A 70 % de margen:

\[
   \text{Margen mensual por cliente} = 35 \times 0{,}70 = \$24{,}50
   \]

3. **El ratio LTV/CAC real no llega a 3.**
   Con la fórmula correcta:

\[
   \text{LTV} = \frac{\text{ARPU} \times \text{Margen bruto}}{\text{Churn mensual}}
   = \frac{35 \times 0{,}70}{0{,}08}
   = \$306{,}25
   \]

\[
   \frac{\text{LTV}}{\text{CAC}} = \frac{306{,}25}{290} = 1{,}06
   \]

Ni siquiera llegas a 1,5. Estás **justo** por encima de 1, lo cual es básicamente comprar clientes a precio de costo.

Además, el **periodo de recuperación del CAC** es:

\[
\frac{290}{24{,}50} \approx 11{,}8 \text{ meses}
\]

Con un churn del 8 % mensual, gran parte de esos clientes se irá antes de que recuperes lo invertido.

### Veredicto

**No metas los $10.000 en publicidad pagada con estos números.** Aunque la empresa sea rentable globalmente, este canal específico quemaría capital. Cada cliente te deja, en valor esperado, solo \~$16 de margen bruto a lo largo de su vida, y eso sin contar costos de soporte, éxito del cliente, herramientas, etc.

### Para aprobarlo, necesitarías acercarte a algo como:

| Métrica | Tu número | Umbral saludable |
|---|---|---|
| LTV/CAC | 1,06 | ≥ 3 |
| Payback CAC | 11,8 meses | ≤ 6-12 meses |
| Churn mensual | 8 % | bajar a 4-5 % o menos |
| CAC | $290 | bajar o subir ARPU |

### Recomendación inmediata

1. **No escales.** Haz un test controlado con un presupuesto pequeño (p. ej., $1.000-$2.000) y mide cohortes reales.
2. **Ataca el churn.** Bajarlo a 4 % duplica la vida media y el LTV.
3. **Sube el precio o el margen.** A $50/mes con el mismo margen, el LTV sube a ~$438 y el ratio a 1,5; aún no es 3, pero empieza a respirar.
4. **Baja el CAC.** Optimiza funnel, creatividades, segmentación y canales antes de poner más dinero.

Hasta que el cálculo correcto dé LTV/CAC ≥ 2,5-3 y payback < 9-12 meses, este plan de crecimiento pagado es una máquina de quemar dólares.