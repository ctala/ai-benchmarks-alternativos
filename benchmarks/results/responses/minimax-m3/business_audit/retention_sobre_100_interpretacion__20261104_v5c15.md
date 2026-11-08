# MiniMax M3 — business_audit/retention_sobre_100_interpretacion

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 63.529s | tokens_per_second: 79.9
- input_tokens: 306 | output_tokens: 5074

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **Retención de ingresos y retención de clientes son métricas distintas**, y una puede superar el 100% mientras la otra cae.

### Qué significa “retención de ingresos: 114%”

Si la métrica es **retención neta de ingresos (NRR)**:

\[
NRR=\frac{MRR\ inicial - churn - contracciones + expansión}{MRR\ inicial}
\]

Significa que la cohorte inicial de clientes genera ahora un **114% de sus ingresos recurrentes iniciales**. Es decir, las ampliaciones de plan han compensado las bajas y downregulated y han dejado un crecimiento neto del 14%.

No permite saber cuánto churn hubo por separado. Podría ser:

- 10% de churn + 24% de expansión, o
- 30% de churn + 44% de expansión.

Ambos casos darían 114%.

Si tu panel llama a esto **retención bruta de ingresos (GRR)**, la definición estándar excluye las ampliaciones y suele estar limitada a 100%. Por tanto, deberías revisar la fórmula: posiblemente sea NRR o una métrica que incluya expansión y/o nuevos clientes.

### Qué dicen tus cifras de clientes

Pasar de 40 a 36 clientes implica:

- **Variación neta de clientes:** −10%.
- Si no entró ningún cliente nuevo, 4 clientesGone = **10% de churn de clientes** y 90% de retención.
- Si entraron clientes nuevos durante el mes, el churn real fue **mayor que 10%**, porque parte de los 36 clientes actuales no estaba en la cohorte anterior.

La retención de clientes de una cohorte normalmente **no puede superar el 100%**.

### Un ejemplo compatible con ambas cifras

| Movimiento | Clientes | MRR |
|---|---:|---:|
| Inicio | 40 | 10.000 € |
| Churn | −4 | −500 € |
| Ampliaciones de plan | — | +1.900 € |
| Cohorte final | 36 | 11.400 € |

Resultado:

- Retención de clientes: **90%**
- Retención bruta de ingresos: **90%**
- Retención neta de ingresos: **114%**

Por tanto, es perfectamente posible tener **114% de retención de ingresos y, al mismo tiempo, perder el 10% de los clientes**.

### ¿Debes centeringte solo en captar clientes?

No deberías hacerlo solo por ese indicador. Conviene seguir por separado:

- Churn bruto de clientes por cohorte.
- Retención de clientes.
- GRR y NRR.
- Ingresos de nuevas altas y CAC.
- Payback del CAC y LTV:CAC.
- Concentración de ingresos: si el 114% depende de unos pocos upgrades, es frágil.

Si el NRR se mantiene por encima de 100% durante varios meses y el churn bruto está controlado, sí podría tener sentido Increer la inversión en captación. Pero con una base de solo 40 clientes y una caída neta del 10%, primero conviene verificar qué calcula exactamente el panel y reconciliar MRR, churn y expansión.