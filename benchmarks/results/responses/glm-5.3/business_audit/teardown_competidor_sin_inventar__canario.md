# GLM 5.3 — business_audit/teardown_competidor_sin_inventar

- model_id: `z-ai/glm-5.3`
- success: True  | final: 2.65 | quality: 2.0
- latency_total: 86.468s | tokens_per_second: 63.7
- input_tokens: 191 | output_tokens: 5509

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

# Teardown competitivo — Comunidad de automatización

**Nota metodológica:** etiqueto cada afirmación como **[DATO]** (lo que viste), **[INF. ALTA]** (inferencia bien fundamentada), **[INF. MEDIA]** (razonable pero sin confirmar) o **[ESPEC]** (especulación). La diferencia entre estas etiquetas es la diferencia entre un análisis y una historia.

---

## 1. Lo que realmente tienes (reframe de tus datos)

Ninguno de esos números es un dato de negocio. Son **artefactos de marketing**:

| Lo que ves | Lo que probablemente es |
|---|---|
| "2.400 miembros" | **[INF. ALTA]** En plataformas tipo membresía (Skool, Circle, etc.), ese contador suele mostrar **miembros acumulados históricos**, no pagantes activos. Incluye trials, gente que entró y se fue. |
| $39/mes | **[INF. MEDIA]** Precio ancla. Podría haber descuentos perpetuos, plan anual oculto hasta el checkout, o precio de lanzamiento. El precio *de lista* rara vez es el precio *realizado*. |
| 12 cursos | **[DATO → INF. MEDIA]** Es un techo, no un piso de valor. Bibliotecas con cursos sin terminar son un patrón común de sobre-promesa. |
| 60K seguidores | **[DATO]** Distribución decente pero no dominante. Y **[INF. ALTA]**: sugiere negocio dependiente del fundador. |
| 3 posts/semana | **[DATO]** Cadencia de top-of-funnel. No dice si es sostenible, si es un empuje de lanzamiento, ni quién lo produce. |

**El punto crítico:** todos tus datos son métricas de *stock* (acumulados). Cero métricas de *flujo* (crecimiento, churn, engagement). Eso es exactamente lo que ves cuando un negocio no muestra sus flujos — o simplemente lo que las plataformas muestran por defecto. No puedes distinguirlo desde fuera. Todavía.

---

## 2. Facturación: escenarios con el math visible

El número que la web quiere que calcules: 2.400 × $39 = **$93.600 MRR (~$1,1M/año)**. Ese es tu techo. Trátalo como marketing, no como realidad.

| Escenario | Supuesto | MRR | Anual |
|---|---|---|---|
| **A. Techo ingenuo** | 2.400 activos, precio lleno | $93.600 | ~$1,1M |
| **B. Activos pero precio realizado menor** | 2.400 activos, ~$28-32 promedio (descuentos, mix anual) | $67-77K | ~$800-920K |
| **C. Acumulados, no activos** | ~40% activos (churn 8-12%/mes típico en comunidades), 950-1.200 activos | $37-47K | ~$450-560K |
| **D. Contador inflado** | Incluye free/lapsed; activos reales 500-800 | $20-31K | ~$240-370K |

**Mi apuesta central [INF. MEDIA]:** entre **$40K y $70K MRR** ($500-850K/año) por membresía, con el escenario C como el más probable si es una plataforma tipo Skool.

**Lo que probablemente te falta [INF. MEDIA]:** en nichos de automatización, los **affiliates de herramientas** (Zapier, Make, n8n, etc. pagan comisiones recurrentes) pueden sumar 10-30% sobre la membresía. Podría haber talleres pagados, cohortes o consultoría. El $39 podría ser solo una fracción del negocio.

**Lo que NO sé y domina todo:** churn, edad de la comunidad, mix mensual/anual, tamaño del equipo (burn rate).

---

## 3. Qué tan sano es

**Honestamente: no puedo decirte si está sano. Pero sí puedo decirte dónde están sus riesgos estructurales, y todos aplican:**

🔴 **Riesgo 1 — Churn temático (el más grave).** Las comunidades sobre un *tema* ("automatización") retienen peor que las comunidades sobre una *identidad o carrera*. La gente entra para resolver un problema concreto, lo resuelve (o se rinde), y se va. Con churn del 10%+ mensual, este negocio es una bañera con el desagüe abierto: necesitan captar ~240 miembros nuevos al mes solo para no encoger. **[INF. ALTA]**

🟡 **Riesgo 2 — Treadmill de contenido.** 3 posts/semana públicos + contenido interno + 12 cursos + moderación. Si esto lo sostiene el fundador (probable, dado el tamaño), el negocio es un trabajo, no un activo. **[INF. MEDIA]**

🟡 **Riesgo 3 — Dependencia del fundador.** 60K seguidores = el canal de adquisición ES el fundador. Si él baja el ritmo, el funnel se seca. **[INF. ALTA]**

🟡 **Riesgo 4 — Commoditización del contenido.** El contenido de automatización envejece rápido (cambian las herramientas, la IA se come workflows). Un catálogo de 12 cursos es un pasivo que se deprecia. **[INF. MEDIA]**

**Señal ambigua que importa:** 60K seguidores → 2.400 miembros (aunque sean acumulados) = conversión ~4% histórica. Si la comunidad tiene 2+ años, es un funnel mediocre. Si tiene 8 meses, es excelente. **No sabes la edad. Ese dato lo cambia todo.**

---

## 4. Cómo competir

### Paso 0: consigue los datos que sí puedes conseguir (esto convierte mi especulación en análisis)

1. **Wayback Machine sobre su portada.** ¿Cuánto ha movido el contador "2.400" en 6-12 meses? Si hace un año decía 2.200, están creciendo ~17/mes neto — están *sangrando* en términos relativos. Si hace un año decía 800, están duplicando. **Este es el dato más valioso que existe y es gratis.**
2. **Llega hasta el checkout.** Ahí verás si hay plan anual, descuentos aplicados, trials.
3. **Ratio de engagement:** comentarios por post en el feed público. Una comunidad de 2.400 con 5 comentarios por post es un cementerio; con 50+ está viva.
4. **Engagement del fundador en redes:** respuestas reales vs. fantasma. Los 60K pueden ser comprados o muertos.
5. **Busca menciones en Reddit, reseñas, quejas de reembolso.**
6. **Si hay trial o tier gratis, entra y mira el estado real de los 12 cursos.**

### Estrategia (condicionada a lo que encuentres)

**No compitas en su terreno. Ataca sus riesgos estructurales:**

1. **Contra el churn temático → compite por resultados, no por permanencia.** Modelo tipo "resuelve tu automatización en 90 días" con inicio y fin. Contraintuitivo, pero los compromisos cortos con final ganan contra suscripciones infinitas que la gente cancela con culpa.

2. **Contra el contenido horizontal → verticaliza.** "Automatización" genérica retiene mal. "Automatización para agencias" o "para e-commerce" crea identidad, y la identidad retiene. Es el mismo conocimiento, posicionado donde el churn baja.

3. **Contra el precio de $39 → no lo iguales.** Igualarlo te convierte en clon barato. O significativamente más barato ($19-25) con un wedge muy estrecho, o premium ($79-99) con prueba de outcomes (cohortes, resultados medibles). El medio es la muerte.

4. **Contra la dependencia del fundador → construye marca de producto.** Si su distribución es una persona, tu ventaja a 3 años es que la tuya no lo sea.

5. **Si verificas cursos sin terminar → ataca con curación.** "12 cursos, 6 terminados" es munición. Posiciónate en calidad completada sobre cantidad listada.

---

## 5. Qué cambiaría mi análisis

- **Wayback Machine mostrando crecimiento rápido** → sube mi estimación de MRR y de salud; compite por diferenciación, no por sus debilidades.
- **Plan anual visible en checkout** → están optimizando LTV; negocio más maduro de lo que parece; mi escenario C baja de probabilidad.
- **Engagement alto en el feed** → la comunidad está viva; el churn probablemente es bajo; no ataques con "resultado en 90 días", ataca verticalizando.
- **Contador estático por meses** → están en meseta o declive; es tu ventana para capturar su audiencia con el fundador como fuente de tráfico (su audience es tu TAM).

**En una frase:** probablemente factura entre $500K y $850K/año, tiene los riesgos estructurales clásicos de las comunidades temáticas de pago, y tu primera jugada no es competir — es pasar 2 horas en Wayback Machine y en su checkout. Vuelve con esos datos y este teardown pasa de probabilidad a diagnóstico.