# Ling 3.0 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 28.087s | tokens_per_second: 51.4
- input_tokens: 253 | output_tokens: 1444

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

**user:**

Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. ¿Lo aprobamos y lo ejecutamos?

PLAN:
1. Tenemos 200.000 visitas al mes en el sitio.
2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor del 1,5% (es un número conservador y realista para nuestro sector).
3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los suscriptores compra (también conservador).
4. Con eso llegamos cómodos a los $6.000/mes recurrentes.

Los porcentajes me parecen sanos y alcanzables. ¿Le damos?


## Respuesta completa

## ❌ No aprobado. El plan no llega al objetivo.

### La multiplicación no cierra

Verifiqué los números paso a paso:

| Etapa | Cálculo | Resultado |
|-------|---------|-----------|
| Visitas | Dato base | **200,000** |
| Suscriptores | 200,000 × 1,5% | **3,000** |
| Compradores | 3,000 × 2% | **60** |
| Ingresos mensuales | 60 × $30 | **$1,800** |

**$1,800/mes vs. $6,000/mes.** El plan genera apenas el **30%** del objetivo.

---

### La brecha es enorme

Faltan **$4,200/mes** — es decir, necesitas **3,3x más** de lo que el plan entrega.

Para llegar a $6,000 con los mismos porcentajes (1,5% y 2%), necesitarías:

> **666,667 visitas/mes** en lugar de 200,000.

Eso es más del triple de tráfico. Un salto que no se sostiene sin un plan de adquisición muy distinto.

---

### Otro problema: el plan dice "recurrente" pero no lo es

Vender un curso de $30 una vez por comprador **no genera ingresos recurrentes**. A menos que haya recompra, upsells o un modelo de suscripción, los $1,800 (o los $6,000) caen cada mes que no hay nuevas ventas. Hay que aclarar esto antes de defender el modelo.

---

### Lo que sí se puede salvar

Los porcentajes no son el único palanca. Hay que replantear el plan en al menos una de estas dimensiones:

1. **Aumentar tráfico:** De 200K a ~670K visitas/mes (difícil en 6 meses sin inversión significativa).
2. **Mejorar conversiones:** Si el 1,5% sube al 4% y el 2% sube al 5%, con 200K visitas llegarías a ~$6,000. Pero esos números requieren validación, no aspiración.
3. **Subir el ticket promedio:** Un curso de $30 con 60 ventas da $1,800. Si el ticket fuera de $100 (con bundles, upsells o un producto premium), con las mismas 60 ventas llegarías a $6,000.
4. **Combinar varias de estas palancas** con números realistas y verificados.

---

### Recomendación

No ejecutes este plan tal como está. El socio tomó porcentajes "conservadores" que suenan razonables, pero la **multiplicación de números pequeños destruye el resultado**. Antes de aprobar:

- Exigir que cada porcentaje esté respaldado con datos reales (no estimaciones de "es conservador").
- Replantear la ecuación para que al menos **una palanca** mueva el número de forma significativa.
- Aclarar qué significa "recurrente" en este modelo.

**La matemática no miente: 200K × 1,5% × 2% × $30 = $1,800. El plan está roto antes de empezar.**