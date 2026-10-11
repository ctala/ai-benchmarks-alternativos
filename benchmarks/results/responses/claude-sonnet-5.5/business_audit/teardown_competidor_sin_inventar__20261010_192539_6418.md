# Claude Sonnet 5.5 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 5.55 | quality: 6.0
- latency_total: 27.468s | tokens_per_second: 115.7
- input_tokens: 288 | output_tokens: 3179

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

# Teardown: comunidad de pago sobre automatización

## 1. Lo que SÉ (observado directamente)

| Dato | Certeza |
|---|---|
| Comunidad de pago, plataforma de membresía | Alta |
| Cifra de "2.400 miembros" en portada | Alta (que se muestra), **no** que sea fiable |
| $39/mes visible | Alta |
| ~3 posts/semana en el feed público | Alta |
| Fundador con 60.000 seguidores | Alta |
| 12 cursos listados | Alta |

Es todo lo que tienes. Lo demás es inferencia.

## 2. Facturación: estimación, no dato

**Techo teórico:** 2.400 × $39 = **~$93.600/mes (~$1,12M/año)**. Es un máximo poco probable, porque asume que todos los miembros pagan el precio completo.

**Por qué probablemente sea menor** (ninguna de estas causas está confirmada):
- "Miembros" puede incluir cuentas gratuitas, pruebas, becas o miembros históricos.
- Puede haber precios anteriores más bajos (*grandfathering*), descuentos o planes anuales con precio mensual efectivo menor.
- La cifra puede ser acumulada o estar desactualizada.

| Escenario | Supuestos | MRR estimado | Certeza |
|---|---|---|---|
| Bajo | 55% de pago, ticket medio $30 | ~$40K | Baja |
| Medio | 70% de pago, ticket medio $35 | ~$59K | Baja |
| Alto | 90% de pago, $39 | ~$84K | Baja |

**Mi estimación central es $40–85K/mes brutos.** Los porcentajes de pago y los tickets medios son supuestos míos, no datos. Descuenta entre un 3% y un 10% en comisiones de pago y plataforma, según cuál usen, para obtener el neto.

## 3. Salud del negocio: lo que NO se puede saber desde fuera

Las variables que determinan la salud no son observables:
- **Churn mensual** (la más importante)
- Coste de adquisición y canales reales
- Tasa de actividad real de los miembros
- Reembolsos
- Si la cifra de 2.400 sube, baja o está estancada

**Prueba de estrés (matemática, no dato sobre ellos):** con un churn de 8–12% mensual, que es un rango habitual en comunidades de bajo ticket pero que es un benchmark general y no su cifra, tendrían que captar **~190–290 miembros nuevos al mes** solo para mantenerse. Si el churn fuera de 4–5%, serían ~100–120. La diferencia entre ambos casos es la diferencia entre un negocio frágil y uno sólido, y no puedes verla desde fuera.

## 4. Inferencias sobre señales concretas

- **60K seguidores → 2.400 miembros (4%).** *Certeza baja.* Si todos vinieran de esa audiencia, sería una conversión alta para el sector. Puede significar que tienen otros canales (SEO, alianzas, boca a boca), que la cifra de miembros incluye gratuitos o está inflada, o que la audiencia es muy cualificada. No sé cuál es.
- **3 posts/semana públicos.** *Certeza baja.* Es una cadencia moderada. Puede indicar que el motor de captación no es el contenido público, o que el valor se concentra dentro de la comunidad. Es una lectura plausible, no un hecho.
- **12 cursos.** *Certeza baja.* Sugiere que apuestan por la biblioteca como argumento de valor y de retención. Que no se vea cuántos están terminados puede significar una oferta menos sólida de lo que aparenta, pero también que simplemente no lo muestran.
- **Precio de $39 sin plan anual visible.** *Certeza media-baja.* Si de verdad no hay plan anual, dependen del cobro mensual, que implica más exposición a churn y menos caja por adelantado. Puede que exista y no se vea.

## 5. Cómo competirles (recomendaciones basadas en hipótesis)

Como no conoces sus puntos débiles reales, tu primer movimiento es **descubrirlos**, no atacar a ciegas.

**A. Verificar antes de decidir (bajo coste, alto valor)**
1. Únete un mes ($39). Mide actividad real: respuestas, antigüedad de los posts, quién contesta y en cuánto tiempo.
2. Revisa cuántos cursos tienen contenido real y cuándo se actualizaron por última vez.
3. Mira el checkout: ¿hay plan anual, trial, upsells?
4. Busca reseñas, quejas y menciones en foros y redes (Reddit, X, LinkedIn). Las quejas dicen más que la portada.
5. Comprueba si la cifra de miembros cambia en el tiempo (capturas periódicas, Wayback Machine).

**B. Ángulos de diferenciación (a validar con lo anterior)**
- **Nicho vertical:** "automatización" es amplio. Una comunidad para un perfil concreto (agencias, e-commerce, contables, etc.) suele ganar en relevancia aunque sea más pequeña.
- **Resultado sobre biblioteca:** si ellos venden volumen de cursos, compite con implementación guiada, plantillas, revisiones o casos reales.
- **Estructura de precio:** plan anual con descuento para mejorar caja y retención. Evalúa precio premium con más soporte frente a precio similar con mejor onboarding.
- **Retención:** onboarding en los primeros 7 días, retos o hitos. Es donde las comunidades de bajo ticket suelen perder gente, aunque no sé si es su caso.

**C. Lo que no haría:** competir solo en precio, ni intentar igualar a su fundador en audiencia. Con 60K seguidores, tienen una ventaja de distribución que no se replica a corto plazo. Es mejor ganar en nicho y en resultados.

## 6. Resumen

| Pregunta | Respuesta | Certeza |
|---|---|---|
| ¿Cuánto facturan? | Probablemente $40–85K/mes brutos (techo ~$94K) | Baja |
| ¿Qué tan sano es el negocio? | **No determinable** sin churn, CAC y actividad | — |
| ¿Cómo competir? | Nicho, resultados, retención y precio anual, tras validar sus debilidades | Media (como enfoque), baja (como diagnóstico) |

Si me das los resultados de la verificación del punto 5 (sobre todo actividad real, plan anual y quejas), puedo afinar la estimación y convertirla en un plan de posicionamiento concreto.