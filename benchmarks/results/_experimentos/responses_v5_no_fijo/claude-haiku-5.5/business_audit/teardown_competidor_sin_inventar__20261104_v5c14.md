# Claude Haiku 5.5 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 6.14 | quality: 6.0
- latency_total: 16.133s | tokens_per_second: 185.5
- input_tokens: 288 | output_tokens: 2992

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

# Teardown: comunidad de automatización de pago

**Leyenda de certeza:** **[Dato]** = visible en la página · **[Inferencia]** = deducción razonable · **[Supuesto]** = hipótesis que no puedo verificar

## 1. Lo que sabes (Datos)

- **[Dato]** Comunidad de pago sobre automatización, en formato membresía.
- **[Dato]** "2.400 miembros" en portada. Es una cifra autodeclarada, no verificable.
- **[Dato]** Precio público: $39/mes. Sin plan anual visible ni descuentos visibles.
- **[Dato]** 3 posts/semana en el feed público.
- **[Dato]** Fundador con ~60.000 seguidores en una red social.
- **[Dato]** 12 cursos listados. No sabes cuántos están completos ni cuándo se actualizaron.

## 2. ¿Cuánto factura? Estimación con rango amplio

No puedo calcularlo con precisión. Lo que sí puedo hacer es acotarlo.

**Techo teórico** (si los 2.400 pagan $39/mes):
- 2.400 × $39 = **$93.600 MRR** → ~**$1,1M ARR**

**Escenarios más realistas:**

| Escenario | % miembros que pagan | Miembros pagos | MRR bruto |
|---|---|---|---|
| Bajo | 30% | ~720 | ~$28k |
| Medio | 60% | ~1.440 | ~$56k |
| Alto | 100% | 2.400 | ~$94k |

**Ajustes que reducen la cifra neta:**
- Miembros gratuitos o de prueba incluidos en el "2.400" **[Supuesto]**
- Descuentos por plan anual, cupones, lanzamientos **[Supuesto]**
- Comisiones de pasarela y plataforma (~5-10%) e IVA si aplica **[Inferencia]**

**Mi lectura honesta:** el rango razonable de MRR bruto está entre **$25k y $90k**. Dentro de ese rango, el dato más útil para acotar sería saber si la cifra de 2.400 incluye miembros gratuitos.

> **Certeza:** baja. Es un rango de orden de magnitud, no una cifra de facturación.

## 3. ¿Qué tan sano es el negocio?

No puedo medirlo: faltan churn, retención, LTV, CAC y tasa de conversión. Lo que sí puedo señalar:

**Señales positivas** (certeza media)
- **Activo de audiencia fuerte.** 60k seguidores es un canal de adquisición propio. **[Inferencia]** probablemente el principal motor de ventas.
- **Cadencia constante.** 3 posts/semana sugiere operación sostenida. **[Inferencia]**
- **Catálogo amplio.** 12 cursos da sensación de valor continuo, aunque no sabes si se usan.
- **Precio de entrada accesible.** $39/mes es fácil de aprobar sin fricción grande.

**Riesgos o incógnitas** (certeza media-baja)
- **Dependencia del fundador.** Si el contenido y la marca giran alrededor de una persona, el negocio es frágil ante burnout o cambios de algoritmo. **[Inferencia]**
- **Retención desconocida.** Las comunidades suelen caer en "suscripción sin uso" si la actividad interna es baja. No sabes si hay conversaciones reales, eventos en vivo o solo contenido unidireccional. **[Supuesto]**
- **Cursos sin señal de uso.** 12 cursos sin saber cuántos se terminan pueden ser más catálogo que producto. **[Inferencia]**
- **Sin plan anual visible.** Puede ser que no lo ofrezcan, o que esté oculto. Si no lo tienen, pierden previsibilidad de caja. **[Supuesto]**

**Veredicto provisional:** parece un negocio **con tracción de audiencia y probablemente rentable**, pero con **retención y dependencia del fundador como puntos ciegos**. Confianza: media-baja.

## 4. Cómo competirles

Lo que más les cuesta copiar, y dónde tendrías ventaja:

1. **Especialización o resultados medibles.** Si ellos son "automatización" en general, puedes ganar con un nicho concreto (p. ej., automatización para e-commerce, agencias o un stack específico) y prometer resultados verificables.
2. **Retención por comunidad real.** Si su fuerte es el contenido, tú puedes diferenciarte con sesiones en vivo, revisiones de proyectos, grupos pequeños o un canal de ayuda con respuesta rápida.
3. **Oferta anual y garantías.** Un plan anual con descuento y una garantía de 30 días les quita previsibilidad, pero te da caja y tracción frente a un mensual de $39.
4. **Precio como ancla, no como guerra.** Compite con valor, no con precio. Entrar más barato sin diferencial te obliga a una carrera de fondo que probablemente ganen por audiencia.
5. **Su punto débil es tu oportunidad:** si dependen del fundador, construye una voz de marca o un equipo de instructores visibles, o apóyate en casos de clientes en lugar de en una persona.

## 5. Cómo afinar el análisis (fuentes públicas baratas)

Para pasar de estimación a dato razonable:

- **Meta Ad Library / TikTok Creative Center:** ¿invierten en anuncios? ¿Qué mensajes repiten?
- **Wayback Machine (archive.org):** cómo ha crecido el conteo de miembros entre fechas. Es la mejor pista para estimar crecimiento neto.
- **Reseñas y testimonios:** en Trustpilot, Reddit, Discord o grupos de Facebook, mira menciones de cancelaciones, quejas o elogios sobre actividad.
- **Similarweb / Semrush:** tráfico estimado y fuentes de adquisición.
- **Fechas de los cursos:** si la mayoría no se ha tocado en 12+ meses, es señal de catálogo estancado.
- **LinkedIn:** tamaño del equipo y rotación; un equipo que crece o se reduce dice mucho.
- **Engagement del fundador:** no solo seguidores, sino comentarios y alcance real por post. 60k con bajo engagement vale menos de lo que parece.

Si me compartes capturas de precios, la fecha de los cursos o cualquier dato de reseñas, puedo refinar el rango de facturación y el veredicto de salud.