# Nemotron 3 Super — business_audit/retention_sobre_100_interpretacion

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 6.9 | quality: 7.2
- latency_total: 25.339s | tokens_per_second: 82.4
- input_tokens: 147 | output_tokens: 2088

## Respuesta completa

**Respuesta breve:**  
No, no puedes asumir que “no se te va nadie” solo porque el **Retención de Ingresos** (NRR – Net Revenue Retention) está por encima del 100 %. Ese indicador ya incluye el efecto positivo de las ampliaciones de plan (upsell, cross‑sell, precios más altos) y puede enmascarar una pérdida real de clientes o de ingresos brutos. En tu caso, el número de clientes pasó de 40 a 36 (‑10 %), lo que indica churn; el NRR de 114 % solo te dice que, pese a esa pérdida, los clientes que se quedaron generaron suficiente ingreso extra para más que compensarla.

---

## 1. Qué mide realmente el “Retención de Ingresos: 114 %”

| Métrica | Fórmula | Qué captura |
|---------|---------|-------------|
| **GRR – Gross Revenue Retention** (Retención bruta de ingresos) | \(\frac{\text{Ingresos recurrentes del mes M‑1 provenientes de clientes que siguieron pagando en M}}{\text{Ingresos recurrentes del mes M‑1}}\) | Solo cuenta la pérdida de ingresos por churn o downgrades; **ignora** cualquier expansión. |
| **NRR – Net Revenue Retention** (Retención neta de ingresos) | \(\frac{\text{Ingresos recurrentes del mes M provenientes de los mismos clientes que estaban en M‑1 (incluye upsell/downsell)}}{\text{Ingresos recurrentes del mes M‑1}}\) | Incluye tanto la pérdida (churn/downgrade) como la ganancia (upsell/cross‑sell, price increase). |

Cuando ves **NRR > 100 %**, lo que realmente está diciendo es:  

> *Los ingresos que obtuvimos este mes de la cohorte de clientes del mes anterior, después de aplicar tanto pérdidas como ganancias, superaron los ingresos que esa misma cohorte generó el mes anterior.*

Por lo tanto, NRR puede estar por encima del 100 % incluso si **GRR** está por debajo del 100 % (es decir, si hay churn o downgrades).

---

## 2. Qué nos dice tu situación concreta

- **Clientes:** 40 → 36 (‑10 %).  
  → Hay churn de 4 clientes (o bien algunos se fueron y otros se quedaron pero con planes menores).  
- **NRR:** 114 % → Los ingresos de los 36 clientes que permanecieron (más los que subieron de plan) son un 14 % mayores que los ingresos que esos mismos 40 clientes tenían el mes pasado.

Para que el NRR llegue a 114 % con una pérdida del 10 % en cuenta de clientes, la expansión promedio por cliente que se quedó debe haber sido algo así como:

\[
\text{Ingresos M} = \text{Ingresos M‑1} \times (1 - \text{churn}) \times (1 + \text{expansión})
\]

\[
1.14 = (1 - 0.10) \times (1 + \text{expansión}) \Rightarrow 1.14 = 0.90 \times (1 + \text{expansión})
\]

\[
1 + \text{expansión} = \frac{1.14}{0.90} = 1.2667 \Rightarrow \text{expansión} \approx 26.7\%
\]

En otras palabras, **los clientes que se quedaron aumentaron su gasto en un ~27 % de media** (upsell, upgrades, añadidos de módulos, etc.). Ese aumento es lo que “compensó” y más la pérdida de los 4 clientes.

---

## 3. Por qué no puedes dejar de preocuparte por el churn

1. **El churn sigue costando dinero**  
   - Cada cliente que se va representa un costo de adquisición (CAC) que ya no se amortiza.  
   - Incluso si la expansión cubre el ingreso perdido, sigues pagando por adquirir esos clientes y por el esfuerzo de soporte que ya no recibes retorno.

2. **La expansión no es infinita**  
   - Los upsells tienen un techo (plan máximo, límite de usuarios, etc.). Si sigues perdiendo clientes, eventualmente no habrá suficiente base para seguir expandiendo y el NRR caerá.

3. **Riesgo de concentración**  
   - Si pocos clientes representan la mayor parte del ingreso (porque los que se quedan pagan mucho más), tu negocio se vuelve vulnerable a la pérdida de uno de esos “whales”.

4. **Señal de salud del producto**  
   - Un alto churn puede indicar problemas de ajuste producto‑mercado, falta de valor percibido, o deficiencias en onboarding/soporte. Ignorarlo puede llevar a una deterioro de la reputación y a un aumento del CAC futuro.

5. **Métricas de crecimiento sostenible**  
   - Los inversores y analistas miran tanto GRR como NRR. Un GRR bajo (por ejemplo, < 90 %) es una señal de alerta incluso si el NRR está alto por ahora.

---

## 4. Qué deberías hacer ahora

| Acción | Por qué | Cómo implementarla |
|--------|---------|--------------------|
| **Calcular y monitorizar GRR** | Te muestra la pérdida pura de ingresos por churn/downgrade. | GRR = (Ingresos recurrentes del mes M de clientes que estaban en M‑1 y siguen pagando) / (Ingresos recurrentes del mes M‑1). Hazlo mensual y por cohortes. |
| **Segmentar el churn** | No todos los churn son iguales; algunos pueden ser por precio, otros por falta de uso, etc. | Etiqueta cada baja: “plan demasiado caro”, “falta de feature X”, “competidor”, “uso bajo”. Analiza patrones. |
| **Mejorar onboarding y éxito del cliente** | Reduce churn temprano (mes 1‑3) y aumenta la probabilidad de upsell. | Implementa check‑list de adopción, sesiones de entrenamiento, métricas de salud (login frequency, feature usage). |
| **Crear un programa de expansión estructurado** | Aprovecha la base que sí está contenta para aumentar LTV de forma predecible. | Define niveles de upsell (ej. +10 % por añadir módulo Y, +20 % por pasar a plan Enterprise). Asigna CSMs o equipos de expansión con cuotas claras. |
| **Probar ajustes de precio o planes** | Si el churn está ligado a sensibilidad de precio, prueba planes intermedios o descuentos por compromiso anual. | A/B test de precios en un subconjunto de clientes nuevos; mide efecto en churn y expansión. |
| **Revisar el CAC y el payback period** | Asegúrate de que el costo de adquirir esos 4 clientes perdidos no esté erosionando tu rentabilidad. | CAC = Gastos de ventas y marketing / Nuevos clientes adquiridos. Payback = CAC / (Margen bruto mensual por cliente). |
| **Crear un dashboard de salud** | Tener una visión única de GRR, NRR, churn, expansión, NPS, usage score. | Herramientas como ChartMogul, ProfitWell, Baremetrics o un simple Google Data Studio con tus datos de Stripe/Chargebee + CRM. |

---

## 5. Resumen ejecutivo para tu equipo

- **NRR = 114 %** → Los ingresos de la cohorte del mes pasado crecieron un 14 % gracias a upsells que más que compensaron la pérdida de clientes.  
- **GRR** (que aún no has visto) está probablemente **por debajo del 100 %** porque perdiste 4 de 40 clientes (‑10 % de cuenta).  
- **Conclusión:** No puedes dejar de trabajar en churn; la expansión está ocultando una fuga que, si sigue, agotará tu base de clientes y hará que el NRR caiga.  
- **Próximo paso:** Calcula GRR, segmenta las causas de churn, refuerza onboarding/éxito del cliente y sigue impulsando upsells de forma sistemática, pero siempre con la mira puesta en reducir la pérdida pura de clientes.

Con esa visión equilibrada podrás seguir creciendo de forma sostenible, sin depender exclusivamente de “más ventas nuevas” para tapar los agujeros del churn. ¡Éxito en el análisis!