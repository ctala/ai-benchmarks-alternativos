# Ling 3.0 Flash VL — business_audit/retention_sobre_100_interpretacion

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 12.553s | tokens_per_second: 140.8
- input_tokens: 165 | output_tokens: 1767

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, no puedes dejar de preocuparte por el churn. La métrica que citas y la realidad que describes son dos historias completamente distintas, y la confusión es más peligrosa de lo que parece.

---

## Lo que realmente dice tu panel

**Retención de ingresos del 114%** es un **Net Revenue Retention (NRR)**. Mide los ingresos del mes pasado ajustados por expansiones y pérdidas:

$$\text{NRR} = \frac{\text{Ingresos del mes anterior} + \text{Expansiones} - \text{Churn} - \text{Downgrades}}{\text{Ingresos del mes anterior}} = 114\%$$

Eso significa que las subidas de plan de tus clientes existentes **superaron en un 14%** las pérdidas por clientes que se fueron y los que bajaron de plan. Es una señal positiva de expansión, sí, pero **no dice absolutamente nada sobre cuántos clientes conservaste**.

## Lo que dice tu contexto

Pasaste de 40 a 36 clientes de pago. Eso es:

$$\text{Retención de clientes} = \frac{36}{40} = 90\% \quad \Longrightarrow \quad \text{Churn de clientes} = 10\%$$

Perdiste **el 10% de tu base de clientes** en un mes. Esa no es una cifra para ignorar; es una cifra para investigar de inmediato.

## Por qué la confusión es peligrosa

Estás haciendo una **apuesta silenciosa y costosa**: que la expansión de los que se quedan siga compensando la fuga de los que se van. Eso puede funcionar un mes, dos, tal vez seis... pero tiene un límite estructural:

1. **Cada cliente solo puede subir de plan un número finito de veces.** Eventualmente la curva de expansión se aplana; la de churn no.
2. **El churn de clientes afecta tu capacidad de upsell.** Menos clientes = menos candidatos para upgrade = menos ingresos futuros por expansión.
3. **El coste de adquisición (CAC) no desaparece.** Si captas gente nueva para sustituir a los que se van, estás gastando dos veces: una en adquisición y otra en mantener ingresos. Si el 10% de tu base se escapa cada mes, necesitas captar ~11-12 nuevos clientes mensuales solo para mantener el nivel.
4. **El NRR alto puede enmascarar segmentos críticos.** Quizás tus clientes enterprise se quedan y suben, pero tus clientes SMB se van en masa. Sin segmentar, no lo verás.

## Lo que deberías hacer

| Acción | Por qué |
|---|---|
| **Calcular tu churn de clientes (ya lo tienes: ~10%)** | Es la métrica que mide la salud real de tu base. |
| **Calcular tu Gross Revenue Retention (GRR)** | Elimina las expansiones del cálculo. Te dice cuánto ingreso realmente conservaste sin ningún upgrade. Probablemente está por debajo del 100%. |
| **Analizar por qué se fueron esos 4 clientes** | ¿Producto? Precio? Soporte? ¿Un segmento específico? 4 clientes perdidos con datos cualitativos valen más que 114% de NRR. |
| **No dejar de captar, pero tampoco ignorar la fuga** | La captación es el motor, pero **retener es la transmisión**. Un motor potente con una transmisión rota no lleva a ningún sitio. |

## En resumen

Tu retención de ingresos del 114% es una buena noticia: los clientes que se quedan gastan más. Pero tu retención de clientes del 90% es una mala noticia: se va gente. **Una métrica no anula a la otra.** Dejar de preocuparte por el churn porque el NRR es alto es como ignorar que tu coche pierde aceite porque el velocímetro marca 160 km/h.