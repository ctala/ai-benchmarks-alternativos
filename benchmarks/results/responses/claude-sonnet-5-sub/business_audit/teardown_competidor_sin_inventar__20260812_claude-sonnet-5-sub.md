# Claude Sonnet 5 (suscripción) — business_audit/teardown_competidor_sin_inventar

- model_id: `claude-sonnet-5`
- success: True  | final: 2.37 | quality: 2.0
- latency_total: 139.721s | tokens_per_second: 74.2
- input_tokens: 2 | output_tokens: 10361

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

# Teardown: competidor de automatización (comunidad de pago)

Antes de los números, una advertencia de método: con 7 datos públicos puedo darte un **rango razonado**, no una cifra. Marco todo con nivel de certeza. Si querés que esto se convierta en documento formal, el repo tiene `community-teardowns/` para justo este tipo de análisis — te lo dejo al final.

## 1. El dato que falta y que mueve todo 6x

No decís si "2.400 miembros" incluye un tier gratuito o si el 100% son pagadores. Esto no es un detalle menor: es la variable que más mueve la estimación de revenue. El patrón "vanity metric de portada = total de miembros, no de pagadores" es extremadamente común (el propio proyecto en el que trabajo lo hace: CAR muestra "1.000+" en público pero el mix real es Free/Premium/VIP). Aplico el mismo escepticismo al competidor por defecto.

**[INFERENCIA — confianza media]:** si dicen "comunidad de pago" sin mencionar tier free, es más probable que sea 100% de pago que freemium. Pero no lo doy por hecho.

## 2. Qué sé, qué infiero, qué no sé

| Dato | Categoría | Certeza |
|---|---|---|
| Precio $39/mes | DATO | Alta — visible |
| "2.400 miembros" en portada | DATO (pero ambiguo qué mide) | Alta el número, baja lo que representa |
| 3 posts/semana en feed público | DATO (pero ambiguo si es feed total o solo del fundador) | Alta el número, baja la interpretación |
| Fundador con 60k seguidores | DATO | Alta |
| 12 cursos listados | DATO | Alta el conteo, cero sobre completitud |
| Cuántos de los 2.400 pagan | NO SÉ | — |
| Si hay plan anual | NO SÉ (no visible ≠ no existe) | — |
| Churn / retención | NO SÉ — punto ciego total desde afuera | — |
| MRR real | INFERENCIA | Baja |
| Si los 12 cursos están terminados | NO SÉ | — |

## 3. Estimación de MRR (con supuestos explícitos)

**Escenario A — 100% pagadores, sin legacy pricing:**
2.400 × $39 = **$93.600/mes** (techo teórico, poco realista)

Casi ninguna comunidad de este tamaño cobra el mismo precio a todos. Si escaló con el tiempo, hay cohortes tempranas con precio legacy más bajo (grandfathering — es lo que CAR mismo hace con su founders cohort a $25). Ajustando -15% a -25% por mezcla de precios:

**→ $70.000–$80.000/mes** si el escenario A es correcto.

**Escenario B — "2.400" incluye tier gratuito:**
Usando benchmarks de industria para conversión free→paid en comunidades de nicho B2B (10%-25%, **esto es un benchmark general, no un dato de esta comunidad**):

- 15% conversión → 360 pagadores × $39 ≈ **$14.000/mes**
- 25% conversión → 600 pagadores × $39 ≈ **$23.400/mes**

**Rango total honesto: $14.000–$80.000/mes.** Es un rango de 6x, lo cual te dice que este teardown, tal como está, no sirve para decidir presupuesto de contraataque — sirve para decidir **qué preguntar después** (sección 6).

Si tuviera que apostar con lo que hay: **$20.000–$35.000/mes**, porque la combinación "fundador con audiencia propia + precio único sin anual visible" suena más a comunidad de tamaño medio-alto en crecimiento que a una madura con pricing tiers complejos. Esto es una apuesta, no un hallazgo — confianza baja.

## 4. Salud del negocio

**Señales positivas [INFERENCIA — confianza media]:**
- 60k seguidores propios = canal de adquisición con CAC bajo, no depende 100% de paid ads.
- Precio único y estable en portada (sin cupón/urgencia) sugiere que no están en modo desesperado por vender.
- 12 cursos es oferta de producto amplia, aunque no dice nada de calidad.

**Señales de riesgo [INFERENCIA — marco confianza por cada una]:**

- **Cadencia de posts baja.** [confianza media, depende de una ambigüedad que no resolviste]: si "3 posts/semana" es el feed TOTAL de una comunidad de 2.400, es una señal de alarma — comunidad grande pero dormida, típico precursor de churn silencioso. Si es la cadencia de contenido oficial del fundador/equipo, es normal y no dice nada. **Necesito que verifiques esto: ¿contaste TODOS los posts visibles o solo los del fundador?**
- **Sin plan anual visible.** [confianza baja]: o no lo tienen (dejan cash y retención en la mesa) o lo tienen pero no lo muestran en la landing pública (algunas plataformas lo esconden hasta checkout). No se puede saber sin ver el checkout.
- **Completitud de cursos desconocida.** [confianza baja]: 12 cursos "listados" es una cifra de marketing. Sin ver el classroom no sé si son 12 completos o 3 completos + 9 en promesa — patrón común en comunidades que priorizan adquisición sobre producto.
- **Punto ciego total en retención.** No hay forma de inferir churn desde una landing pública. Este es el dato que más determina si el negocio es sano o es una fuga con la llave de agua abierta (adquisición fuerte tapando cancelaciones).
- **Dependencia de una sola persona.** Si el fundador es el motor de adquisición (60k seguidores) y no hay señal de un segundo canal, es un single point of failure: si deja de postear, el funnel se seca. No sé si tienen paid ads o SEO como respaldo — no hay dato.

## 5. Cómo competir (con lo que sabemos, no con lo que asumimos)

1. **Anual como palanca de cash + retención.** Si de verdad no tienen plan anual, es una brecha explotable directamente: vos ofrecés un anual con descuento fuerte (ancla de valor + lock-in), ellos no. Antes de construir mensaje sobre esto, confirmá en su checkout que de verdad no existe (landing ≠ checkout).
2. **"Comunidad viva" vs "comunidad grande".** Si la cadencia de 3 posts/semana resulta ser feed total (confirmalo), tu ángulo competitivo es la diferencia entre tamaño y actividad — 2.400 "miembros" con feed dormido pierde contra una comunidad más chica pero con engagement real. Esto es exactamente lo que mide el propio Discovery de Skool internamente (engagement 15-19% en canales orgánicos vs comunidades infladas).
3. **Completitud como diferenciador honesto.** Si al investigar confirmás que varios de los 12 cursos están incompletos, el mensaje "menos cursos, todos terminados y accionables" es un ángulo de venta legítimo — pero solo si lo verificás primero, no lo asumas.
4. **No pelees en precio sin saber el mix real.** $39/mes sin saber cuánto de eso es legacy pricing es un ancla poco confiable. Competir en precio contra un rango de $14K-$80K de MRR estimado es apostar a ciegas.
5. **No ataques churn/retención en tu mensaje público** — no lo sabés, y si te equivocás públicamente es un golpe a tu propia credibilidad, no a la de ellos.

## 6. Qué investigar antes de decidir estrategia (baja la incertidumbre real)

Esto es investigación externa gratis o casi gratis, antes de construir nada (research-before-build):

- **Wayback Machine** de su landing: ver evolución del contador de miembros y del precio en el tiempo → dice si crecen, están estancados, o subieron precio (señal de pricing power real).
- **Si es Skool**: el leaderboard público a veces es visible sin login y da señal de actividad real de miembros (no solo del fundador).
- **Búsqueda de menciones del fundador en podcasts/entrevistas**: muchos founders de info-productos revelan MRR como flex — buscar "[nombre] MRR" o "[nombre] revenue" en YouTube/podcasts.
- **Reviews públicas** (Trustpilot, grupos de Facebook, comentarios en su propio contenido social) buscando quejas de cursos incompletos o cancelaciones.
- **Tráfico** (Similarweb/SEMrush) de su dominio — da una segunda señal independiente del tamaño real de la operación, cruzable contra los "2.400 miembros".
- **Checkout real**: entrar hasta el paso de pago (sin pagar) para confirmar si existe plan anual oculto.

Con esos 5 puntos el rango de $14K-$80K debería bajar a algo con un factor de 2x, no de 6x — ahí sí vale la pena construir estrategia de precio sobre el número.

---

¿Querés que formalice esto como doc en `community-teardowns/` siguiendo el patrón del repo, o preferís que primero verifiques los 2-3 puntos ambiguos (feed total vs fundador, tier free sí/no) y lo recalculamos con datos más firmes?