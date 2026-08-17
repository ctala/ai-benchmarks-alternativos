# MiniMax M2.7 (directo) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 60.837s | tokens_per_second: 33.1
- input_tokens: 186 | output_tokens: 2016

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

# Tu aritmética tiene un problema grave

El error no está en la fórmula. Está en la vida del cliente.

---

## El error: 24 meses con 8% de churn mensual

Un churn de 8% mensual no significa que el cliente dure "unos 2 años". Significa esto:

| Mes | Clientes que quedan |
|-----|-------------------|
| Inicio | 100% |
| Mes 1 | 92% |
| Mes 6 | ~61% |
| Mes 12 | ~38% |
| Mes 24 | ~14% |

La **vida esperada real** es:

$$\frac{1}{0.08} = 12.5 \text{ meses}$$

No 24. Eso parte el cálculo.

---

## Tu LTV recalculado

Usando tu margen bruto del 70%:

$$\text{LTV} = 35 \times 0.70 \times 12.5 = \$306.25$$

| | Tu cálculo | Realidad |
|---|---|---|
| LTV | $840 | **$306** |
| CAC | $290 | $290 |
| LTV/CAC | 2.9 | **1.06** |

Un ratio de 1.06 significa: por cada dollar invertido en ads, ganas **$1.06 en margen bruto total antes de cualquier otro costo**.

Eso no es "por encima de 3". Eso es **apenas cubrir el costo de adquisición**.

---

## Qué significa en la práctica tu plan de $10k

Si metes $10,000 en ads:

- Nuevos clientes: ~34
- Ingreso total que generarán en su vida completa: **$10,412** (34 × $306)
- Ganancia neta sobre la inversión en ads: **$412**

Eso es un **4.1% de retorno sobre $10,000**.

Y eso asumiendo que tu CAC no suba cuando subas el gasto — lo cual casi siempre pasa.

---

## La pregunta que debes hacerte antes de escalar

No es si el ratio supera 3. Es si puedes justificar este gasto ahora:

| Prioridad | Pregunta |
|---|---|
| 1 | ¿Cuánto overhead operativo tienes todavía sin cubrir? (el margen bruto ≠ ganancia neta) |
| 2 | ¿Conoces tu CAC real a escala o solo en modo piloto? |
| 3 | ¿Has probado que el churn se mantiene en 8% con más volumen, o puede empeorar? |
| 4 | ¿Qué pasa si el CAC sube a $350 cuando Duplicas el gasto? |

---

## Opciones para mejorar la ecuación antes de quemar $10k

**Reducir churn es lo más poderoso:**

- Cada punto menos de churn = +1.56 meses de vida
- Si bajas de 8% a 5%, el LTV salta a $420, ratio sube a 1.45
- Si bajas a 3%, el LTV sube a $700, ratio a 2.41

**Subir precio cambia todo:**

- A $50/mes con 8% churn: LTV = $437, ratio = 1.51
- A $70/mes con 8% churn: LTV = $612, ratio = 2.11

**Reducir CAC:**

- Necesitas CAC de ~$102 para llegar a ratio 3.3 con los números actuales

---

## Mi recomendación

No digo que no escales. Digo que **no escales $10k así**:

1. **Sube el gasto gradualmente** — $1k, luego $2k, luego $4k — y mide el CAC a cada nivel
2. **Valida el churn** con el nuevo volumen de clientes (no asumas que se mantiene)
3. **Pide trial/plan barato** para bajar el CAC efectivo antes de comprometer $10k
4. **Calcula el payback period**: con $24.50 de margen mensual y $290 CAC, tardas ~12 meses en recuperar la inversión

Con un ratio de 1.06, estás operando en el filo. Un mes malo, un competitor, o un CAC que suba con el volumen y estás perdiendo dinero en la adquisición de clientes.

**La aritmética dice: no es "más o menos" por encima de 3. Es apenas positivo.**