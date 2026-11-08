# Kimi K2.7 Code — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 151.593s | tokens_per_second: 52.9
- input_tokens: 230 | output_tokens: 8012

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

**No. No le metas $10.000 en publicidad pagada con estos números.**  
Revisé la aritmética y el plan no se sostiene. Estás mezclando ingreso con margen y sobrestimando la vida del cliente.

### Tus errores de cálculo

| Concepto | Tu cálculo | El cálculo correcto | Diferencia clave |
|---|---|---|---|
| **Vida promedio** | ~24 meses | `1 / 0,08 = 12,5 meses` | Con 8% de churn mensual, la vida media no es 2 años. |
| **LTV** | `$35 × 24 = $840` | `$35 × 0,70 / 0,08 = $306` | El LTV debe usar el **margen bruto**, no el ingreso total. |
| **LTV / CAC** | `$840 / $290 = 2,9x` | `$306 / $290 = 1,06x` | No estás cerca de 3x; apenas cubres el CAC. |

**Tu CAC de $290 deja solo $16 de margen bruto por cliente en toda su vida**. Eso es casi un empate, antes de gastos operativos, soporte o cualquier imprevisto.

### Qué pasa si gastas $10.000 este mes

- Clientes adquiridos: `$10.000 / $290 ≈ 34 clientes`.
- Margen bruto esperado de toda esa cohorte: `34 × $306 ≈ $10.600`.
- **Ganancia neta esperada de la inversión: ~$560** en toda la vida de esos clientes.
- Payback simple: `$290 / $24,5 ≈ 12 meses`.
- Pero con churn del 8%, el payback real (probabilístico) se estira a **~38–39 meses**.

Resumen de caja:

| Tiempo | Recuperado (aprox.) | Caja del cohort |
|---|---|---|
| 12 meses | $6.600 | **-$3.400** |
| 24 meses | $9.000 | **-$1.000** |
| ~38 meses | $10.000 | Recién break-even |

Es decir: vas a tener que financiar ese agujero de caja casi 3 años para ganar **$560**. Si el CAC sube un poco o el churn empeora, pierdes plata.

### Por qué 8% de churn mensual es un problema grave

`1 - (1 - 0,08)^12 = 63%`  
Estás perdiendo **dos de cada tres clientes cada año**. Es un balde con agujero. Escalar publicidad pagada con esa fuga es echarle nafta a una fogata mal armada.

### Mi recomendación

1. **No escales todavía.** Un LTV/CAC de 1,1x no da margen de seguridad. La regla saludable suele ser ≥3x, y con churn alto deberías exigir un payback mucho menor.
2. **Reduce churn primero.** Bajar el churn a 4% mensual duplicaría tu LTV a ~$612 y te daría un ratio de ~2,1x. Eso ya es otra historia.
3. **Sube el precio o la monetización.** Con churn del 8%, necesitarías un precio de ~$100/mes para sostener un CAC de $290 con ratio 3x.
4. **Baja el CAC.** Si mantienes tus números actuales, tu CAC sostenible es ~$102, no $290.
5. **Si quieres validar, haz una prueba chica.** No $10.000 de golpe. Gasta $1.000–$2.000, mide cohortes reales y ajusta antes de escalar.

**Veredicto final:** aplazá el gasto de $10.000 hasta que el LTV/CAC real esté por encima de 3x y el payback caiga a menos de 12 meses con churn ajustado. Hoy no cumplís ninguna de las dos.