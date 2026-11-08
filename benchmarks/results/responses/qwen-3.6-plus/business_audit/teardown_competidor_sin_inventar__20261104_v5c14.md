# Qwen 3.6 Plus — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 2.87 | quality: 2.0
- latency_total: 68.521s | tokens_per_second: 57.8
- input_tokens: 193 | output_tokens: 3961

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

Como analista competitivo, aplicaré un marco explícito: **separaré cada dato observable de cada deducción**, y asignaré un **nivel de certeza** a cada afirmación no verificable directamente. Usaré esta escala:
- 🔴 **BAJA (<50%)**: Suposición basada en patrones del sector, alta variabilidad posible.
- 🟡 **MEDIA (50-79%)**: Probable según benchmarks, pero requiere validación.
- 🟢 **ALTA (80-95%)**: Consistente con datos observables y estándares de la industria.
- ⚫ **HECHO (100%)**: Extraído directamente de tu observación pública.

---

### 🔍 1. HECHOS vs. INFERENCIAS (con certeza)

| Elemento | Clasificación | Detalle | Certeza |
|----------|---------------|---------|---------|
| Comunidad de pago sobre automatización en plataforma de membresía | ⚫ HECHO | Modelo de negocio y nicho confirmados | ⚫ |
| "2.400 miembros" visible en portada | ⚫ HECHO | Cifra pública exacta | ⚫ |
| Precio visible: $39/mes | ⚫ HECHO | Tarifa pública única | ⚫ |
| No se ve plan anual ni descuentos | ⚫ HECHO | Observación de interfaz | ⚫ |
| 3 posts/semana en feed público | ⚫ HECHO | Cadencia observable | ⚫ |
| Fundador con 60k seguidores | ⚫ HECHO | Activo social verificable | ⚫ |
| 12 cursos listados, sin estado de finalización | ⚫ HECHO | Catálogo público | ⚫ |
| Los 2.400 son miembros activos pagando | 🔴 INFERENCIA | En comunidades, esta cifra suele incluir bajas, trials, cuentas inactivas o grandfathered. | 🔴 BAJA |
| Churn mensual típico para este ticket | 🟡 INFERENCIA | Comunidades low-ticket en automatización suelen tener 5-9% mensual. | 🟡 MEDIA |
| Conversión del fundador (60k → pagos) | 🔴 INFERENCIA | Depende de engagement real, funnels, y si los seguidores son orgánicos/comprados. | 🔴 BAJA |
| Los 12 cursos son el core del producto | 🟡 INFERENCIA | Podrían ser lead magnets, upsells, o contenido legacy. La opacidad en finalización sugiere posible baja retención o decisión estratégica. | 🟡 MEDIA |
| Costos operativos (plataforma + pasarela) | 🟢 INFERENCIA | Plataformas tipo Skool/Circle/Mighty + Stripe suelen cobrar 5-10% + 2.9%+$0.30. | 🟢 ALTA |

---

### 💰 2. ESTIMACIÓN DE FACTURACIÓN

**Cálculo base (bruto):**  
`2.400 miembros × $39 = $93.600/mes`

**Ajustes realistas (inferidos):**
- 🟡 **Miembros activos reales:** 60-75% del total (1.440 - 1.800)
- 🟡 **Descuentos/trials/fallos de pago:** -5% a -10%
- 🟢 **Fees de plataforma + pasarela:** ~10-12%
- 🟡 **Ingresos netos estimados:** `$48.000 - $68.000/mes`
- 🟡 **Anualizado:** `$576.000 - $816.000/año`

🔍 **Nivel de certeza global de la estimación:** 🟡 **MEDIA**  
*Nota:* Si el 2.400 incluye cuentas inactivas o precios legacy ($19-$29), la facturación real podría estar 20-40% por debajo. Si tienen B2B o upsells no visibles, podría estar por encima.

---

### 📊 3. SALUD DEL NEGOCIO (indicadores inferidos)

| Dimensión | Evaluación | Certeza | Comentario |
|-----------|------------|---------|------------|
| **Adquisición** | 🟢 Fuerte top-of-funnel orgánico (60k seguidores) | 🟢 ALTA | CAC probablemente bajo si convierte >1.5% de audiencia |
| **Retención/Churn** | 🟡 Riesgo moderado-alto | 🟡 MEDIA | Sin plan anual, sin descuentos por compromiso, y opacidad en finalización de cursos sugieren fricción en LTV |
| **Engagement/Contenido** | 🟡 Sostenible pero no escalable | 🟡 MEDIA | 3 posts/semana mantiene presencia, pero no genera virilidad ni profundidad técnica constante |
| **Dependencia** | 🔴 Alta en fundador | 🔴 BAJA | Si el 60k es personal y no hay equipo/branding institucional, el negocio es frágil ante cambios de algoritmo o burnout |
| **Escalabilidad** | 🟡 Media | 🟡 MEDIA | 12 cursos indican productización, pero sin métricas de finalización o ROI visible, el upsell/cross-sell es limitado |
| **Margen operativo** | 🟢 Alto (>70% neto) | 🟢 ALTA | Modelo digital low-touch, sin inventario, costos fijos bajos |

📌 **Veredicto de salud:** 🟡 **Negocio viable y rentable a corto plazo, con riesgos estructurales de retención y dependencia de marca personal.** No muestra señales de escalabilidad sistémica ni defensibilidad a largo plazo.

---

### 🎯 4. ESTRATEGIA COMPETITIVA (cómo competir)

| Eje | Acción concreta | Por qué funciona | Certeza de impacto |
|-----|----------------|------------------|---------------------|
| **1. Diferenciación por resultados, no por contenido** | Publica casos reales con métricas (horas ahorradas, $ generados, flujos desplegados) | La automatización está saturada de teoría; el mercado paga por ejecución verificable | 🟢 ALTA |
| **2. Arquitectura de precios con LTV optimizado** | Ofrece plan anual (-20%), tier "Pro" con soporte 1:1 o templates premium, y garantía de ROI | Captura mayor valor, reduce churn, y crea barrera de salida | 🟢 ALTA |
| **3. Transparencia radical como ventaja** | Muestra % de finalización, dashboards de progreso, y testimonios con datos duros | Contrarresta la opacidad del competidor y genera confianza institucional | 🟡 MEDIA |
| **4. Cadencia y formato de contenido** | 1 post/semana de profundidad técnica + 2 interactivos (Q&A, audits en vivo, challenges) | Mayor valor percibido sin saturar; genera comunidad activa vs. feed pasivo | 🟡 MEDIA |
| **5. Adquisición alternativa al founder** | Partnerships con vendors de herramientas (Zapier, Make, n8n), webinars co-branded, lead magnets con flujos descargables | Reduce dependencia de audiencia personal; abre canales B2B/B2C mixtos | 🟢 ALTA |
| **6. Retención sistémica** | Onboarding guiado, milestones, comunidad peer-to-peer (no solo founder-led), y rituales mensuales (hackathons, reviews) | Ataca el churn estructural de comunidades low-ticket | 🟡 MEDIA |

⚠️ **Riesgos a evitar:** 
- Competir en precio ($39 es difícil de bajar sin quemar margen).
- Imitar la cadencia de contenido sin diferenciación clara.
- Construir otra comunidad "fundador-céntrica" sin procesos de retención.

---

### 🔎 PRÓXIMOS PASOS PARA REDUCIR INCERTIDUMBRE

1. **Validar membresía activa:** Únete como trial o compra 1 mes. Observa: % de posts con interacción real, frecuencia de actualizaciones de cursos, tono de soporte.
2. **Rastrear precios legacy:** Busca en foros, Reddit, o Twitter menciones de precios anteriores o descuentos ocultos.
3. **Auditar funnel:** Usa herramientas como BuiltWith o SimilarWeb para ver tráfico, fuentes, y si usan pixel de conversión o retargeting.
4. **Entrevistar a ex-miembros:** Busca en redes o grupos afines a usuarios que cancelaron. El churn real suele estar ahí.
5. **Mapear stack tecnológico:** Identifica la plataforma (Skool, Circle, Podia, etc.) para estimar costos reales y limitaciones técnicas.

---

📌 **Resumen ejecutivo:**  
Facturan probablemente **$50k-$70k/mes netos**, con margen alto pero **retención vulnerable** y **dependencia crítica del fundador**. Tu ventaja competitiva no está en copiar su modelo, sino en **industrializar la retención, transparentar resultados, y diversificar adquisición**. Si ejecutas con disciplina en LTV y defensibilidad de marca, puedes capturar su mercado de usuarios insatisfechos con contenido teórico y churn alto.

¿Quieres que profundice en algún eje (pricing, funnel de adquisición, métricas de retención, o arquitectura de comunidad)?