# Kimi K2.6 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 45.827s | tokens_per_second: 82.5
- input_tokens: 231 | output_tokens: 3779

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

 **No. No le doy.** Con estos números no estás viendo una oportunidad de escalar; estás viendo una máquina de quemar efectivo en cámara lenta. Hagamos la autopsia matemática.

---

### Error 1: Tu cliente no se queda 2 años
Dijiste que el churn es **8% mensual**. Eso significa que la vida útil esperada de un cliente es:

> **Vida útil = 1 / Churn = 1 / 0.08 = 12.5 meses**

No 24 meses. A 8% de fugas mensuales, la *mediana* es aún peor: la mitad de tus clientes se habrán ido antes del mes 9. La suposición de 2 años no es optimista; es fantasía.

### Error 2: Estás mezclando ingreso bruto con costo de adquisición
Tu CAC ($290) es un costo 100% real que pagas **hoy en efectivo**. El LTV debe calcularse sobre el **margen bruto** que realmente te queda, no sobre el precio de lista. Con un margen del 70%, tu flujo de caja mensual neto por cliente es:

> **Margen mensual = $35 × 70% = $24.50**

Entonces, el LTV real es:

> **LTV = $24.50 / 0.08 = $306.25**

### Error 3: Tu ratio LTV/CAC no es 2,9
Es esto:

> **LTV / CAC = $306.25 / $290 = 1.06**

Ni siquiera estás duplicando tu inversión. Estás recuperando a duras penas lo que pusiste, y eso solo en valor esperado a lo largo del tiempo. Si usaras ingreso bruto (incorrecto), el ratio sería **1,5x** ($437 / $290), todavía muy lejos del 3x que exige un modelo SaaS sano.

### Error 4: El payback period es suicida
Con esos números, tardas **11.8 meses** en recuperar el CAC ($290 / $24.50). Como tu churn es del 8%, la probabilidad de que un cliente promedio sobreviva lo suficiente para pagar su propia adquisición es solo del **37%**. Es decir, **63% de los clientes que compres con publicidad se irán antes de que recuperes los $290**.

---

### Qué pasa si metes esos $10,000

- Adquirirías aproximadamente **34 clientes**.
- Esa cohorte te generaría un valor esperado de **~$10,400 en margen acumulado** (en meses, mientras se van muriendo).
- Pero el flujo de caja es catastrófico: este mes pusiste $10,000 y apenas recuperarás ~$800 el primer mes. Tu capital queda preso casi un año para un retorno de equilibrio.

Básicamente, le prestarías dinero a tu propio negocio a tasa de interés casi nula y con alto riesgo de default.

---

### El verdadero problema: 8% de churn mensual

Ese es el elefante en la habitación. En SaaS, 8% mensual es una hemorragia (equivale a ~63% de churn anual). **No escales lo que no retiene.** Cada dólar que inviertas en publicidad con esa fuga saldrá por la puerta meses después.

| Métrica | Tu Número | ¿Qué necesitas? |
|---------|-----------|-----------------|
| Churn mensual | **8%** | < 3% (ideal < 2%) |
| LTV/CAC | **1.06x** | > 3.0x |
| Payback | **11.8 meses** | < 12 meses (ideal < 6) |

### Mi recomendación

1. **Congela la inversión en paid ads** hasta que el churn baje. Si lo bajas a 3% mensual, tu vida útil salta a 33 meses, tu LTV a ~$808 y tu ratio a 2,8x. Ahí ya podemos hablar de un piloto controlado.
2. **Baja el CAC o sube el ticket promedio.** $290 es caro para un producto de $35/mes con esa retención.
3. **Si quieres forzar una prueba, usa $1,000, no $10,000.** Y mide cohortes reales a 6 meses, no proyecciones a 24 meses.

**Veredicto final:** Tu negocio actual puede ser rentable con tráfico orgánico o canales de bajo CAC, pero con publicidad pagada estos números no son escalables. Son inflamables. Arregla la retención primero.