# DeepSeek V4 Pro (0813) — business_audit/teardown_competidor_sin_inventar

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 4.13 | quality: 4.0
- latency_total: 157.743s | tokens_per_second: 51.9
- input_tokens: 272 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa

# Teardown del competidor — comunidad de automatización

⚠️ **Límite del análisis**  
Solo tengo datos públicos. No tengo acceso a su checkout, churn, costes, equipo ni actividad interna real.  
Voy a marcar lo que es **hecho**, lo que es **inferencia** y lo que es **supuesto de escenario**.

---

## 1. Qué sabemos vs. qué asumimos

**[HECHO]**
- Comunidad de pago sobre automatización.
- Muestra “2.400 miembros” en portada.
- Precio visible: **39 USD/mes**.
- No se ve plan anual ni descuento.
- Publican **3 posts/semana** en feed público.
- Fundador con **60.000 seguidores** en una red social.
- Tienen **12 cursos listados**. No se ve cuántos están terminados.

**[INFERENCIA]**
- Los “2.400 miembros” probablemente son miembros de pago, pero **no está confirmado**. Podría incluir usuarios gratis, inactivos o miembros antiguos.
- Si no se ve plan anual, es probable que la mayoría pague mensual, aunque pueden existir descuentos ocultos, cupones o planes anuales no visibles.
- Publicar 3 veces/semana y tener 12 cursos indica una operación activa, no un proyecto abandonado.

**[NO TENGO]**
- Churn mensual/anual.
- CAC real.
- LTV.
- Tamaño del equipo.
- Márgenes.
- Actividad real dentro de la comunidad.

---

## 2. Estimación de facturación

La cuenta base es simple:

**2.400 × 39 USD = 93.600 USD/mes → 1,12 M USD/año**

Ese sería el techo si:
- Los 2.400 son todos de pago.
- Todos pagan 39 USD/mes.
- No hay descuentos anuales ni miembros con precio especial.

### Escenarios razonables

| Escenario | Supuesto | MRR estimado | ARR estimado |
|---|---:|---:|---:|
| Techo | 2.400 pagando, sin descuento | ~93,6k USD | ~1,12 M USD |
| Moderado | 2.400 pagando, pero 15% de descuento anual/blended | ~79,6k USD | ~955k USD |
| Conservador | Solo 60% de 2.400 paga, con 15% descuento | ~47,7k USD | ~573k USD |

**Mi estimación central razonable:**  
Si el contador de portada es de miembros de pago reales, está probablemente entre **75k y 93k USD/mes** y en torno a **0,9-1,1 M USD/año**.

Si el número incluye no pagadores, podría caer a **0,55-0,75 M USD/año**.

**Conclusión de facturación:**  
Es muy probable que sea un negocio de **6-7 cifras anuales**, con una facturación recurrente estimada de **0,6-1,1 M USD/año**, con punto central cercano a **~1 M USD/año** si el contador es honesto.

---

## 3. ¿Qué tan sano es el negocio?

### Señales de salud positivas

- **Ingresos recurrentes:** 39 USD/mes por miembro es un modelo predecible.
- **Margen bruto digital alto:** probablemente 85-95% si no hay coste de bienes físicos.
- **Audiencia del fundador:** 60.000 seguidores pueden reducir mucho el CAC.
- **Contenido activo:** 3 posts/semana sugiere operación viva.
- **Catálogo amplio:** 12 cursos, aunque no sepamos si terminados, indica apuesta por producto.

### La conversión seguidor → cliente

Si 60.000 seguidores generaron 2.400 miembros:

**2.400 / 60.000 = 4% de conversión de audiencia a cliente**

Eso es plausible para una audiencia nicho, pero **no es bajo**. Sugiere una de estas cosas:
- Audiencia muy comprometida.
- Buena lista de email intermedia.
- El “2.400” incluye también personas no pagadoras.
- Hay tráfico adicional: SEO, afiliados, partnerships.

### El punto más importante: churn

Sin churn no podemos saber la salud real. Con 39 USD/mes, el LTV depende de cuánto se quedan.

| Churn mensual estimado | LTV por miembro |
|---|---:|
| 3% | ~1.300 USD |
| 5% | ~780 USD |
| 7% | ~557 USD |
| 10% | ~390 USD |

**Interpretación:**
- Si su churn mensual es 3-5%, es un negocio muy sano.
- Si es 7-10%, sigue siendo aceptable si el CAC es bajo.
- Si el CAC supera 200-300 USD y el churn es alto, el negocio empieza a estar tensionado.

Dado que el fundador tiene audiencia propia, es probable que el CAC sea bajo en comparación con un competidor que depende de ads.

### Mi veredicto de salud

**Probablemente es un negocio sano y rentable**, siempre que:
- El equipo sea pequeño: fundador + 1-3 personas/contratistas.
- El churn mensual no supere 6-7%.
- No estén gastando agresivamente en ads