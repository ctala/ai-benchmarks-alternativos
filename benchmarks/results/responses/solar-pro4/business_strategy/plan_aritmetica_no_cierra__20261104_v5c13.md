# Solar Pro 4 — business_strategy/plan_aritmetica_no_cierra

- model_id: `upstage/solar-pro4`
- success: True  | final: 9.04 | quality: 10.0
- latency_total: 12.898s | tokens_per_second: 87.6
- input_tokens: 269 | output_tokens: 1130

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

**No lo aprobamos.** No porque los porcentajes sean irrealistas, sino porque la ecuación no cierra en el objetivo. Los porcentajes sanos no compensan una brecha estructural en la conversión monetaria.

Hacemos la multiplicación línea por línea, tal como la presentó tu socio:

| Paso | Input | Tasa | Resultado |
|------|-------|------|-----------|
| Visitas/mes | 200.000 | — | 200.000 |
| Captura → suscriptores | 200.000 | 1,5% | 3.000 suscriptores/mes |
| Suscriptores → compradores | 3.000 | 2% | 60 ventas/mes |
| Ticket | 60 | $30 | **$1.800/mes** |

**Brecha:** $1.800 vs $6.000 → **factor 3,3x**. El plan llega a $1.800, no a $6.000. La afirmación de “llegamos cómodos” es un error de aritmética, no de optimismo.

---

### Dónde se rompe la lógica del plan

1. **Confusión de “recurrente” vs “one-shot”.** Un curso de $30 suele ser venta única. Para que $1.800/mes sean *recurrentes*, necesitas either:
   - Suscripción mensual al curso/contenido, o
   - Upsell recurrente (comunidad, mentoring, 갱신, etc.).
   Si es venta única, el mes 1 ronda $1.800 y el mes 2 depende de captar 3.000 suscriptores *de nuevo*. El plan no modela acumulación ni retención.

2. **La tasa de compra es la válvula crítica.** 2% de la lista es plausible en sectores fríos o de producto bajo, pero para $6.000 necesitarías:
   - Ticket ~$100 con las mismas tasas, o
   - 6,7% de conversión de la lista (60 → 200 compradores), o
   - 10.000 suscriptores/mes (requiere conversión de visitas ~5% o más visitas).

3. **Visitas ≠ audiencia calificada.** 200k visitas es volumen, no intención. Si la captura es genérica, el 1,5% puede caer y el 2% de compra puede bajar aún más. Sin segmentación o lead magnet de alto intento, las tasas son aspiracionales.

---

### Lo que tendríamos que aprobamos (condiciones mínimas)

| Variable | Necesario para $6.000/mes | Comentario |
|----------|---------------------------|------------|
| Ticket | ~$100 (o paquete + suscripción) | Sin subir ticket, la lista debe ser 3,3x mayor o la conversión 3,3x mayor. |
| Conversión lista→venta | 6–7% (si ticket $30) | 2% no basta. Requiere funnel de venta activa, no solo envío de correos. |
| Flujo de suscriptores | Mantener/acumular ~10.000 efectivos | Si es venta única, necesitas retención o recompra. Si es suscripción, necesitas churn <5–7% mensual. |
| Visitas calificadas | 200k con intención de solución, no tráfico genérico | Si el 1,5% de captura es real, el problema está en la tasa de compra y el ticket. |

---

### Decisión

**No ejecutamos el plan tal como está.** No es cuestión de confianza en los porcentajes; es que la multiplicación no alcanza el objetivo y mezcla ingreso único con “recurrente” sin modelarlo.

Si quieres llegar a $6.000/mes en 6 meses con 200k visitas, el plan necesita al menos una de estas correcciones antes de lanzarse:
- Subir el ticket a ~$100 (o crear un paquete + componente recurrente).
- Diseñar un funnel de venta que pique la conversión de lista a 6%+ (secuencias de venta, webinars, prueba social, garantía, upsell).
- Aclarar si el $30 es entrada a una suscripción mensual (y modelar churn/acumulación) o es compra única (y entonces calcular cuántos suscriptores nuevos se necesitan por mes para sostener el objetivo).

Los porcentajes son “sanos” en el vacío, pero en la multiplicación el cuello de botella es el ticket y la tasa de compra, no la captura. Corrije eso, recalcula y entonces sí podemos aprobar y ejecutar.