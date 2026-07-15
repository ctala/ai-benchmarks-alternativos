# Claude Fable 5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 8.03 | quality: 10.0
- latency_total: 27.69s | tokens_per_second: 52.5
- input_tokens: 295 | output_tokens: 1453
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación detallada y práctica de los cálculos de LTV y CAC.

## Respuesta completa

No le des todavía. Tu cálculo tiene dos errores que, combinados, convierten un negocio "rentable" en uno que pierde plata con cada cliente pagado.

## Error 1: La vida del cliente no son 24 meses

Con churn mensual del 8%, la vida promedio del cliente es:

**1 / 0,08 = 12,5 meses**

No 24. De dónde salieron los 2 años no lo sé, pero con 8% de churn pierdes la mitad de tu cohorte en unos 8-9 meses. Casi nadie llega a los 2 años.

## Error 2: El LTV se calcula sobre margen, no sobre ingresos

Los $35/mes no son tuyos: $10,50 se van en infraestructura y pagos. Lo que te queda por cliente por mes es:

**$35 × 70% = $24,50**

## El LTV real

$$LTV = 24,50 × 12,5 = \$306{,}25$$

No $840. Tu ratio real es:

$$LTV/CAC = 306,25 / 290 = \mathbf{1{,}06}$$

Estás básicamente en break-even *antes* de contar tu tiempo, herramientas, soporte, y cualquier costo fijo. Cada cliente que compras con publicidad te devuelve $16 de margen... a lo largo de un año.

## El otro problema: payback

$$Payback = 290 / 24,50 ≈ \textbf{12 meses}$$

Necesitas casi un año para recuperar el CAC en caja, pero tu vida media de cliente es 12,5 meses. Estás financiando 12 meses de flujo negativo para ganar medio mes de margen. Si metes $10.000 este mes, ese dinero vuelve (apenas) en un año, si el churn no empeora — y el churn de clientes adquiridos por ads suele ser *peor* que el de tu base orgánica actual.

## Qué números necesitarías

Para llegar a LTV/CAC = 3 tienes dos palancas:

- **Con tu CAC actual ($290):** necesitas LTV ≈ $870, o sea ~35 meses de vida → churn de **~2,8%** mensual. Es bajar el churn a un tercio.
- **Con tu churn actual (8%):** necesitas CAC ≤ **~$100**. Es bajarlo a un tercio.
- **Mixto y más realista:** churn al 5% (vida = 20 meses, LTV = $490) + CAC a ~$160.

## Mi recomendación

1. **No metas los $10.000 aún.** A 1,06x no estás comprando crecimiento, estás comprando trabajo.
2. **Ataca el churn primero.** 8% mensual (~63% anual) es la fuga que mata todo lo demás. Cada punto de churn que bajes mejora el LTV más que cualquier optimización de ads.
3. **Si quieres testear publicidad, hazlo con $1.000-2.000** para validar si el CAC de $290 se sostiene a escala (normalmente sube) y medir el churn específico de esa cohorte.
4. Tu regla de "3 o más" está bien — pero aplícala sobre margen y vida real, no sobre ingresos y una vida inventada.

Eres rentable hoy porque tu adquisición actual (probablemente orgánica) es barata. Ese es el negocio que tienes. El de crecer con ads a $290 de CAC todavía no existe.