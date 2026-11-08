# DeepSeek V4.1 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 30.239s | tokens_per_second: 123.9
- input_tokens: 228 | output_tokens: 3747

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

No. No lo aprobaría como plan de escalado. El error principal está en el LTV: con churn mensual de 8%, un cliente **no se queda 2 años en promedio**. Y además el LTV debe compararse contra CAC usando **margen bruto**, no precio.

### Tus números reales

| Concepto | Cálculo | Resultado |
|---|---:|---:|
| Contribución mensual por cliente | $35 × 70% | **$24,50** |
| Vida media del cliente | 1 / 8% | **12,5 meses** |
| LTV sobre margen bruto | $24,50 / 8% | **$306,25** |
| LTV/CAC | $306,25 / $290 | **1,06x** |
| Payback de CAC | $290 / $24,50 | **11,8 meses** |
| Margen bruto de por vida después de CAC | $306,25 − $290 | **$16,25 por cliente** |

Tu cálculo de LTV/CAC = 2,9 usa 24 meses de permanencia y $35 de ingreso sin margen. Con tus datos reales, el LTV/CAC es **1,06**, no 2,9. Incluso si usaras LTV sobre ingresos y no sobre margen: $35/8% = $437,50; contra $290 daría 1,51x, también lejos de 3x.

### Qué pasaría con $10.000

- Clientes adquiridos: $10.000 / $290 ≈ **34,5 clientes**.
- Margen bruto de por vida generado: ≈ $10.560.
- Ganancia después de CAC: ≈ **$560 en toda la vida del cliente**, antes de costos fijos, equipo, herramientas, creatividades, etc.
- Pero desembolsas $10.000 hoy y recuperas el CAC durante casi **12 meses**.
- Si el churn empeora, el CAC real sube o los clientes de pago retienen peor que los orgánicos, esto se vuelve negativo.

### Umbrales que necesitarías

Para que publicidad pagada sea atractiva:

- **CAC máximo para LTV/CAC = 3x:** ≈ **$102**.
- **CAC máximo para payback ≤ 6 meses:** ≈ **$147**.
- **CAC actual para no destruir valor:** $290 está apenas debajo del break-even ($306), con muy poco margen de error.
- Si mantienes CAC de $290 y quieres LTV/CAC = 3x, necesitarías:
  - Precio de ≈ **$99/mes** con 8% churn y 70% margen, o
  - Churn de ≈ **2,8% mensual** con precio $35 y margen 70%.

### Recomendación

**No metas $10.000 este mes como escalado.** La economía unitaria no lo soporta: cada cliente deja unos **$16 de margen bruto de por vida** después de pagar el CAC actual, y el payback es casi igual a la vida media del cliente.

Si quieres probar publicidad:

1. Empieza con un test chico: **$1.000–$2.000 máximo**, no $10.000.
2. Mide por cohorte:
   - CAC incremental real, incluyendo creatividades, herramientas y agencia.
   - Churn de los clientes pagados, separado del orgánico.
   - Payback real de CAC.
   - LTV sobre margen bruto.
3. Define antes un umbral de corte. Por ejemplo: si no logras payback ≤ 6–9 meses o LTV/CAC sobre margen ≥ 3x, no escalas.
4. Antes de escalar, mejora al menos una palanca: retención, precio, expansión/upsell, margen bruto o CAC.

**Veredicto:** con los números actuales, no. No estás listo para escalar fuerte con publicidad pagada; estás comprando clientes casi a break-even y con riesgo de caja. Primero corrige retención o baja el CAC.