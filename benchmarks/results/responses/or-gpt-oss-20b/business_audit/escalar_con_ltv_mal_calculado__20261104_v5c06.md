# GPT-OSS 20B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 27.828s | tokens_per_second: 108.0
- input_tokens: 237 | output_tokens: 3006

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

### 1️⃣  ¿Qué está pasando con tu cálculo?

| Parámetro | Valor que usas | Valor que corresponde (con 8 % churn mensual) |
|-----------|----------------|----------------------------------------------|
| **Duración media del cliente** | 24 meses (2 años) | 1 / 0,08 ≈ 12,5 meses |
| **Ingresos por cliente (LTV bruto)** | 35 × 24 = 840 $ | 35 × 12,5 ≈ 437,5 $ |
| **Margen bruto** | 70 % | 70 % (igual) |
| **LTV (beneficio bruto)** | 840 $ | 437,5 × 0,70 ≈ 306,3 $ |
| **LTV / CAC** | 840 / 290 ≈ 2,9 | 306,3 / 290 ≈ 1,06 |

El error está en **asumir 24 meses de permanencia** cuando la tasa de churn mensual es del 8 %. Con ese churn, la vida media de un cliente es de solo **12,5 meses**.  

> **Resultado clave**  
> LTV bruto ≈ 306 $ → LTV/CAC ≈ 1,06.  
> Esto está *muy bajo* para un plan de crecimiento que depende de publicidad pagada. La regla de oro suele ser LTV/CAC > 3 para que el CAC sea sostenible y cubra los costes indirectos (soporte, ventas, infraestructura, etc.).

---

### 2️⃣  ¿Qué implica esto para tu presupuesto de $10 000 en publicidad?

- **Clientes que puedes adquirir**: 10 000 $ / 290 $ ≈ 34 clientes.  
- **Beneficio bruto total**: 34 × 306,3 $ ≈ 10 400 $  
- **Resultado neto**: 10 400 $ – 10 000 $ ≈ + 400 $ (punto de equilibrio casi perfecto).

> **Interpretación**  
> El CAC se paga justo al final del periodo de vida media del cliente. No hay margen de beneficio real ni un “buffer” que cubra costes de operación o variaciones de churn. En la práctica, cualquier aumento del churn o una ligera caída en el margen te llevaría a una pérdida.

---

### 3️⃣  ¿Por qué no es una buena señal de “escala fuerte”?

| Factor | Riesgo | Posible mitigación |
|--------|--------|--------------------|
| **Margen bruto** 70 % | 30 % de costes variables. Si el margen cae, LTV se reduce. | Optimizar costes de infraestructura, buscar acuerdos con procesadores, o aumentar precios. |
| **Churn** 8 % mensual | 12,5 meses de vida media. | Estrategias de retención (onboarding, soporte, upsells). |
| **CAC** 290 $ | LTV/CAC ≈ 1,06 | Reducir CAC (lead nurturing, SEO), o mejorar la tasa de conversión. |
| **Escala de la inversión** | Con $10 000, solo 34 clientes. | Necesitas > 3 × CAC para cubrir costes indirectos y ganar margen. |

---

### 4️⃣  ¿Qué podrías hacer para mejorar el LTV/CAC y justificar una inversión de $10 000?

| Estrategia | Impacto esperado | Cálculo rápido |
|------------|------------------|----------------|
| **Reducir churn al 5 % mensual** | Vida media ≈ 20 meses → LTV ≈ 35 × 20 × 0,70 = 490 $ | LTV/CAC ≈ 490 / 290 ≈ 1,69 |
| **Elevar el margen a 80 %** | LTV ≈ 437,5 × 0,80 = 350 $ (en 12,5 meses) | LTV/CAC ≈ 350 / 290 ≈ 1,21 |
| **Bajar CAC a 150 $** | LTV/CAC ≈ 306 / 150 ≈ 2,04 |
| **Combinación de 5 % churn + margen 80 %** | LTV ≈ 35 × 20 × 0,80 = 560 $ | LTV/CAC ≈ 560 / 290 ≈ 1,93 |
| **Combinación de 5 % churn + CAC 150 $** | LTV/CAC ≈ 490 / 150 ≈ 3,27 | **Cumple la regla de 3** |

**Recomendación práctica**  
1. **Prueba a bajar el CAC**: quizás con una campaña más enfocada, remarketing o contenido orgánico.  
2. **Trabaja la retención**: implementa un programa de onboarding, soporte proactivo y upsells.  
3. **Revisa la estructura de precios**: si puedes aumentar el precio a $40 o $45 sin perder clientes, el LTV crece linealmente.  

Con una combinación de los tres, podrías alcanzar un **LTV/CAC > 3** con un CAC de $290, lo que justificaría la inversión de $10 000 y te daría margen suficiente para cubrir costes indirectos y crecer de forma sostenible.

---

### 5️⃣  Conclusión

- **Tu cálculo actual subestima el churn** y sobrevalora el LTV.  
- **El LTV/CAC real es ~1.06**, lo que significa que el CAC se paga justo al final del ciclo de vida del cliente y sin margen.  
- **Una inversión de $10 000** bajo esos parámetros te deja prácticamente sin ganancia ni buffer; cualquier variación negativa te generará pérdidas.  
- **Para escalar con publicidad pagada** necesitas **reducir el CAC, aumentar la retención o el margen** (o una combinación de ellos) para alcanzar un LTV/CAC > 3.

Si quieres que profundice en alguna de estas áreas (optimizar retención, tácticas de reducción de CAC, análisis de precios), avísame. ¡Estaré encantado de ayudarte a afinar el plan!