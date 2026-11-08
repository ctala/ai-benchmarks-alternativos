# Claude Opus 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 18.008s | tokens_per_second: 86.9
- input_tokens: 218 | output_tokens: 1565

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## No, esa lectura no es correcta

El 114% casi seguro es **retención neta de ingresos (NRR)**, no retención de clientes. Son métricas distintas y en tu caso apuntan en direcciones opuestas.

### Lo que dicen tus números

| Métrica | Cálculo | Resultado |
|---|---|---|
| Retención de clientes (logos) | 36 / 40 | **90%** |
| Churn de clientes mensual | 4 / 40 | **10%** |
| Retención neta de ingresos | MRR actual de esos clientes / MRR inicial | **114%** |

El 114% significa que **los clientes que se quedaron pagan lo bastante más** (por las subidas de plan) como para compensar a los 4 que se fueron y aún sobrar un 14%. No significa que "no se vaya nadie". Se te fue 1 de cada 10 clientes en un solo mes.

Además, la retención de clientes **no puede superar el 100%**: no puedes conservar más clientes de los que tenías. Solo la retención de *ingresos* puede pasar de 100%, y lo hace gracias a la expansión.

### Por qué un 10% mensual es preocupante

Si ese ritmo se mantiene, de un grupo de 40 clientes quedarían unos **11 al cabo de un año** (0,9¹² ≈ 28%). Que el NRR se vea bien ahora no lo arregla, por varias razones:

- **La expansión tiene techo.** Un cliente que sube de plan no puede subir indefinidamente. El churn, en cambio, sigue ocurriendo cada mes.
- **Dependes de pocos clientes.** Si el 114% lo sostienen unos pocos que subieron mucho, perder a uno solo de ellos puede hundir la métrica.
- **Captar con el cubo agujereado sale caro.** Cada cliente nuevo que entra tiene un 10% de probabilidad mensual de irse, así que tu coste de adquisición tarda más en recuperarse y tu crecimiento se frena.
- **El churn es una señal.** Algo no les está funcionando a esos clientes (encaje, onboarding, precio, producto). Ignorarlo hace que lo repitas con cada cliente nuevo.

### Qué te recomiendo

1. **Comprueba cómo calcula tu panel el 114%.** Debería medir solo a los clientes que ya tenías al inicio del periodo. Si incluye ingresos de clientes nuevos, no es NRR y la cifra está inflada.
2. **Sigue tres métricas juntas:**
   - Churn de clientes (logos)
   - **GRR** (retención bruta de ingresos: sin contar expansión, máximo 100%), que te dice cuánto ingreso pierdes "en bruto"
   - NRR
3. **Habla con los 4 que se fueron.** Averigua por qué. Con tan pocos clientes, cada conversación vale oro.
4. **Mira quién expande y quién se va.** Si son perfiles distintos, eso te dice a qué tipo de cliente deberías estar captando.

**En resumen:** tu expansión es buena noticia, pero no sustituye a la retención. No dejes de trabajar el churn. Con un 10% mensual, probablemente sea tu prioridad número uno, por delante de la captación.