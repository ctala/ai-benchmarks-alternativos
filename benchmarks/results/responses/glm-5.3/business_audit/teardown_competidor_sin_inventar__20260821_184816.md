# GLM 5.3 — business_audit/teardown_competidor_sin_inventar

- model_id: `z-ai/glm-5.3`
- success: True  | final: 2.61 | quality: 2.0
- latency_total: 99.992s | tokens_per_second: 69.0
- input_tokens: 191 | output_tokens: 6901

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

# Teardown competitivo

**Sistema de certeza que voy a usar:** [HECHO] = dato que me diste · [ALTA] / [MEDIA] / [BAJA] = inferencia con ese nivel de confianza · [?] = incognoscible desde fuera.

---

## 1. Cuánto factura

El cálculo ingenuo es 2.400 × $39 = $93.600/mes ≈ **$1,1M/año. Ese número casi seguro es falso.** [ALTA]

En plataformas tipo membresía (Skool, Circle, etc.), el contador de "miembros" suele incluir miembros acumulados históricos (churn incluido), usuarios en trial gratuito y a veces miembros de comunidades satélite gratuitas. El contador de portada es métrica de marketing, no de caja.

| Escenario | % del contador que paga activo | MRR | ARR bruto |
|---|---|---|---|
| Cara (número literal) | 100% | $93.600 | $1,12M |
| Realista | 40–60% | $37K–$56K | $450K–$675K |
| Conservador | 25–35% | $23K–$33K | $280K–$390K |

**Mi estimación central: $30–60K MRR bruto** [MEDIA]. Esto dibuja una operación de 1–3 personas con márgenes altos (el contenido ya está producido, el costo marginal de un miembro extra es ~cero), no una empresa escalada [MEDIA].

Matices:
- No se ve plan anual. Si existe pero está oculto, su base es más estable de lo que parece; si no existe, es más frágil [BAJA en ambos sentidos].
- El contador podría estar desactualizado o "redondeado" [BAJA, pero es práctica común].

Cualquiera que te dé un número único con estos datos te está mintiendo. El rango honesto es este.

## 2. Qué tan sano es

**Señales positivas:**
- 3 posts/semana consistentes = operación viva, alguien trabaja el marketing activamente [ALTA]
- 12 cursos listados = biblioteca de contenido sustancial [HECHO que existen]
- 60K seguidores del fundador = activo de distribución real [HECHO]
- 2.400 miembros mostrados = tracción al menos moderada [HECHO]

**Señales de riesgo (todo lo importante está aquí y no lo puedes ver):**
- **Churn [?]** — es LA variable de este modelo. Comunidades de pago a $39/mes típicamente pierden 5–15% mensual [ALTA como dinámica de la industria; ? la suya]. Con 1.000 activos y 10% de churn necesitan ~100 miembros nuevos/mes solo para quedarse planos. Es una cinta de correr.
- **12 cursos con finalización desconocida** — si varios están a medias, indica sobrepromesa o equipo saturado [BAJA–MEDIA]
- **Precio solo mensual (aparente)** — ingresos expuestos mes a mes [MEDIA]
- **Dependencia del fundador** — 60K seguidores sugiere distribución centrada en una persona: riesgo de key person y cuello de botella de contenido [MEDIA–ALTA]

Dato interesante: 2.400/60.000 = 4% de conversión aparente. Aunque los miembros vienen de varias fuentes, la oferta convierte decentemente [MEDIA]. **No asumas que su funnel es débil.**

## 3. Cómo competir

Advertencia: no sé cuál es tu negocio, así que esto es condicional.

1. **No compitas de frente a $39 con la misma oferta.** Es guerra de commodities contra un incumbente con biblioteca y audiencia.
2. **Contra-posiciónate**: hacia arriba (high-ticket orientado a resultados: cohortes, accountability, done-with-you) o hacia un nicho más filoso que "automatización" genérica.
3. **Ataca su debilidad estructural: la retención.** Su modelo vive o muere por churn. Si construyes mecánicas de retención superiores (cohortes, certificaciones, resultados medibles), ganas económicamente incluso con menos miembros.
4. **Explota el gap de finalización**: si sus cursos tienen incompletos, posiciona "menos cursos, terminados, con resultados".
5. **Gana el canal que probablemente descuidan**: 3 posts/semana en feed sugiere distribución social-first. Si están débiles en SEO/contenido evergreen, ahí hay demanda capturable.
6. **Wedge de valor gratis**: publica la información gratis, vende la comunidad y el acompañamiento. La información a $39/mes es difícil de defender; la comunidad es sticky.

## 4. Lo que más cambiaría este análisis (y cómo conseguirlo)

1. **Wayback Machine sobre su homepage** — gratis, 10 minutos. Si el contador pasó de 800→2.400 en 12 meses, crecen fuerte. Si estaba en 2.300 hace 6 meses, están estancados. **Este es el dato más valioso que te falta.**
2. **Paga $39 por un mes.** La inteligencia competitiva más barata que comprarás: actividad real interna, qué % de miembros postea, estado real de los cursos.
3. **Mira el engagement del fundador, no sus followers**: 60K con 200 likes/post ≠ 60K con 3.000.
4. **Identifica la plataforma exacta** — cambia radicalmente qué significa "miembros".
5. **Busca huella del churn**: reseñas, Reddit, quejas de ex-miembros.

---

Si me cuentas tu posicionamiento y recursos actuales, afino la estrategia competitiva de la sección 3 en algo accionable en lugar de condicional.