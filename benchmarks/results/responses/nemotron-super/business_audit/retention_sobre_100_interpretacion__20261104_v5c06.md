# Nemotron 3 Super — business_audit/retention_sobre_100_interpretacion

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 24.229s | tokens_per_second: 73.1
- input_tokens: 147 | output_tokens: 1770

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, esa lectura no es correcta. Un **114 % de retención de ingresos** no significa que no tengas churn de clientes, ni que puedas ignorar la fuga de logos para enfocarte solo en captar.

Aquí está la lectura precisa de tu situación:

### 1. Qué mide realmente ese 114 %
Es muy probable que ese número sea **NRR (Net Revenue Retention)**: los ingresos que generó un grupo de clientes el mes pasado, comparados con lo que genera ese mismo grupo este mes, después de sumar upsells y restar downgrades y cancelaciones.

En tu caso:
- **Mes pasado:** 40 clientes pagando.
- **Este mes:** 36 de esos clientes siguen (4 se fueron).
- **Resultado:** los 36 restantes pagan lo suficiente más (subieron de plan) como para que los ingresos netos de esa cohorte sean un **14 % superiores** a los del mes anterior.

Eso es expansión de ingresos, no ausencia de churn.

### 2. Tu churn de clientes es real y es del 10 %
Pasaste de 40 a 36 clientes de pago. Eso es un **logo churn mensual del 10 %** (o una retención de clientes del 90 %).

La retención de ingresos puede estar por encima del 100 % mientras la retención de clientes esté por debajo, porque unos pocos clientes que pagan mucho más pueden ocultar la salida de muchos clientes que pagan menos.

### 3. Por qué no puedes dejar de preocuparte por el churn
Incluso con un NRR de 114 %, un churn de logos del 10 % mensual es una señal de alerta si se mantiene:

- **Agotas tu mercado:** si cada mes pierdes el 10 % de tu base, necesitas reponer esos 4 clientes solo para mantener el tamaño actual, antes de crecer.
- **CAC insostenible:** captar clientes cuesta dinero. Si los pierdes a corto plazo, el coste de adquisición se come el margen.
- **Señal de producto o experiencia:** que alguien se vaya aunque otros suban de plan sugiere que parte de tu oferta no está reteniendo. El churn puede estar concentrado en un segmento, un plan o un tipo de uso.
- **GRR puede estar cayendo:** el 114 % es *neto*. No te dice cuánto ingreso perdiste por cancelaciones y downgrades antes de sumar los upsells. Esa métrica se llama **GRR (Gross Revenue Retention)** y no puede superar el 100 %. Si tu GRR es bajo, tu crecimiento depende enteramente de hacer que los clientes restantes paguen más, lo cual tiene un techo.

### 4. Qué deberías vigilar además del NRR
| Métrica | Qué te dice | ¿Por qué importa en tu caso? |
|---------|-------------|------------------------------|
| **Logo Retention** | % de clientes que siguen | Tienes un 90 %. ¿Es estable o empeora? |
| **GRR** | Ingresos retenidos sin contar expansión | Te muestra la fuga "pura" de ingresos. |
| **Churn por segmento/plan** | Quiénes se van | Quizás los clientes de bajo plan se van y los de alto plan se expanden. |
| **NRR descompuesto** | Expansión vs. contracción vs. churn | Sabes cuánto del 114 % es upsell real y cuánto es compensar pérdidas. |

### Conclusión
El 114 % es una buena noticia sobre **expansión**, pero no es un permiso para descuidar la retención de clientes. Tienes un churn de logos del 10 % mensual; si no lo atacas, eventualmente necesitarás captar clientes cada vez más rápido solo para mantener el negocio estable.

**Recomendación:** celebra el upsell, pero dedica recursos a entender por qué 4 de cada 40 clientes se van cada mes.