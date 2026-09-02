# Tencent Hy4 preview — business_audit/teardown_competidor_sin_inventar

- model_id: `tencent/hy4-preview`
- success: True  | final: 5.31 | quality: 6.0
- latency_total: 380.595s | tokens_per_second: 52.0
- input_tokens: 213 | output_tokens: 19798

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

# Teardown externo: comunidad de pago de automatización ($39/mes)

**Aviso de analista:** con solo página pública, **no puedo darte su facturación real**. Puedo darte **aritmética directa** a partir de lo que me diste y **escenarios** basados en supuestos típicos del modelo de membresías. Todo lo que no es un dato tuyo lo marco con nivel de certeza.

## Leyenda de certeza

- 🟩 **Hecho / aritmética directa**: dato que me diste o cálculo matemático simple.
- 🟨 **Certeza alta**: supuesto estándar de la industria (comisiones de tarjeta, plataformas de membresía).
- 🟧 **Certeza media**: inferencia plausible, pero no verificada (que los 2.400 sean activos, churn típico).
- 🟥 **Certeza baja / especulación**: escenario o hipótesis débil (mix anual, CAC, equipo, impuestos).
- ⬛ **Desconocido**: no se puede estimar con lo que hay.

---

## 1. Veredicto rápido

| Pregunta | Respuesta estimada | Certeza |
|---|---:|---|
| **Facturación bruta (billings)** | **$93.600/mes → ~$1,12M/año** si los 2.400 son miembros activos y todos pagan $39/mes | 🟩 inputs / 🟧 interpretación |
| **Ingresos netos tras comisiones** | **$84.000–$90.000/mes → ~$1,01M–$1,08M/año** | 🟨 |
| **Beneficio operativo probable** | Muy alto en superficie: quizá **$50.000–$85.000/mes** antes de impuestos y salario del fundador, si los miembros son activos | 🟧 |
| **Salud del negocio** | Sano en caja y margen, pero frágil en retención: ticket bajo, sin plan anual visible, 12 cursos sin confirmar | 🟧 |
| **Rango realista de facturación** | **$0,5M–$1,1M ARR** dependiendo de si 2.400 es activos, acumulados o hay anual oculto | 🟧 |

---

## 2. Hechos vs. inferencias

| Dato público | Qué significa | Certeza |
|---|---|---|
| Comunidad de pago sobre automatización | Venden recurrencia, no un curso único | 🟩 |
| “2.400 miembros” en portada | Puede ser **miembros activos**, **totales históricos**, o incluir gratuitos/pruebas | 🟩 el número / 🟧 su significado |
| Precio visible: **$39/mes** | ARPU bajo; fácil de comprar, pero sensible al churn | 🟩 |
| No se ve plan anual ni descuentos | O no lo tienen, o lo ocultan en el checkout | 🟩 lo visible / 🟧 lo oculto |
| 3 posts/semana en feed público | Motor de contenido y marketing; pero si el feed es público, parte del valor se regala | 🟩 / 🟧 |
| Fundador con 60.000 seguidores | Distribución propia; CAC probablemente bajo si convierte desde ahí | 🟩 / 🟧 |
| 12 cursos listados | Biblioteca es activo de retención **si están terminados**; si no, riesgo de decepción | 🟩 listados / ⬛ finalización |

**Inferencia clave 🟧:**  
2.400 miembros / 60.000 seguidores = **4% de conversión**. Eso es alto para una comunidad de pago. Posibles explicaciones:

1. Audiencia muy cualificada.
2. Tienen más fuentes de tráfico además de esa red social (SEO, YouTube, referidos, anuncios).
3. El número de “miembros” está inflado o incluye no pagados.

---

## 3. Estimación de facturación

### Supuestos de costes

- **Procesamiento de tarjeta:** ~2,9% + $0,30 por transacción 🟨  
  En $39 → comisión ≈ **$1,43**, es decir **96,3% neto** antes de plataforma.
- **Plataforma de membresía:** 🟨/🟧  
  - Si están en Skool/Circle/Kajabi/Mighty con plan de pago: normalmente **fee fijo bajo** ($99–$399/mes) y **0% de comisión**.  
  - Si están en plan gratuito/creator de Teachable/Podia/Memberful o similar: podrían pagar **5–10%** de comisión.
- **No incluido:** reembolsos, impuestos, equipo, publicidad, herramientas. ⬛

### Escenario A — Base: 2.400 activos, todos mensuales, sin anual

| Métrica | Valor | Certeza |
|---|---:|---|
| MRR bruto | 2.400 × $39 = **$93.600** | 🟩 |
| ARR bruto | **$1.123.200** | 🟩 |
| Comisión tarjeta (~3,7%) | **–$3.434/mes** | 🟨 |
| Plataforma (fee fijo o 0–5%) | **–$0 a –$4.700/mes** | 🟨/🟧 |
| **MRR neto estimado** | **$84.000–$90.000** | 🟨 |
| **ARR neto estimado** | **$1,01M–$1,08M** | 🟨 |

### Escenario B — Anual oculto (hipótesis)

Supongamos que el 30% elige plan anual con 2 meses gratis: $390/año = **$32,50/mes** equivalente.

- 70% mensual: 1.680 × $39 = $65.520  
- 30% anual: 720 × $32,50 = $23.400  
- **MRR normalizado:** **$88.920**  
- **ARR normalizado:** **~$1,07M bruto**  
- **Caja inicial del mes 1:** 720 × $390 + 1.680 × $39 = **$346.320 brutos** 🟧  
- **MRR neto tras fees:** **~$80.000–$86.000** 🟧

### Escenario C — Conservador: “2.400” es acumulado/vanity o hay churn alto

Si los **activos reales** fueran 1.200–1.800:

| Activos | MRR bruto | ARR bruto | MRR neto aprox. |
|---:|---:|---:|---:|
| 1.800 | $70.200 | $842.400 | $67.000–$68.000 |
| 1.500 | $58.500 | $702.000 | $56.000–$57.000 |
| 1.200 | $46.800 | $561.600 | $45.000–$46.000 |

Certeza: 🟧/🟟.

### Escenario D — Pesimista: solo 1.000 activos

- MRR bruto: **$39.000**
- ARR bruto: **$468.000**
- MRR neto: **~$37.000–$38.000**

Certeza: 🟥.

> **Conclusión de facturación:**  
> Si el número es real y activo, están en **$0,9M–$1,1M ARR brutos**.  
> Si hay trampa de métricas o churn alto, podrían estar en **$0,5M–$0,8M ARR**.  
> No sé cuál es el caso real. ⬛

---

## 4. Salud del negocio

### Unit economics por miembro

| Concepto | Valor | Certeza |
|---|---:|---|
| ARPU | $39/mes | 🟩 |
| Margen tras tarjeta | ~$37,57/mes (**96,3%**) | 🟨 |
| Coste marginal de servir a 1 miembro más | Muy bajo (plataforma + soporte) | 🟨 |
| Coste fijo plataforma | $0–$500/mes si es SaaS fijo | 🟨 |

### LTV según churn mensual

| Churn mensual | Vida media | LTV bruto | LTV neto aprox. | Miembros que pierden/mes |
|---:|---:|---:|---:|---:|
| 3% | 33 meses | $1.287 | ~$1.240 | 72 |
| 5% | 20 meses | $780 | ~$750 | 120 |
| 8% | 12,5 meses | $487 | ~$470 | 192 |
| 10% | 10 meses | $390 | ~$376 | 240 |

Certeza: 🟧 (churn típico de comunidades de ticket bajo; no tengo su dato real).

Además, en suscripciones de $39/mes existe **churn involuntario** por tarjetas caducadas: suele sumar **1–3% mensual** adicional. 🟧

### Necesidad de reposición

Para mantener 2.400 miembros:

- Al 5% churn: necesitan **~120 altas/mes**.
- Al 8% churn: **~192 altas/mes**.
- Al 10% churn: **~240 altas/mes**.

Con 60.000 seguidores, eso implica convertir roughly **0,2%–0,4% de su audiencia cada mes**. Es posible si la audiencia está muy caliente, pero no es trivial. 🟧

### Veredicto de salud

**Sobre el papel: muy sano.**  
Márgenes altísimos, ingresos recurrentes, CAC probablemente bajo por audiencia propia y punto de equilibrio muy bajo (probablemente <200 miembros). 🟨

**Pero con banderas amarillas:**

1. **Ticket bajo ($39)** → atrae curiosos; sin implementación, churn alto. 🟧  
2. **Sin plan anual visible** → más churn voluntario/involuntario y caja menos predecible. 🟧  
3. **12 cursos sin confirmar finalización** → riesgo de “vendí humo” si están a medias. 🟧  
4. **Feed público** → si el contenido es lo principal y es gratis, la propuesta de pago se debilita. 🟧  
5. **Dependencia del fundador** → riesgo de persona clave y de escalado. 🟧  

**Salud superficial: 8/10. Salud ajustada por riesgo de retención/métricas infladas: 5–6/10.** 🟧

---

## 5. Fortalezas y vulnerabilidades inferidas

### Fortalezas del competidor

| Fortaleza | Certeza |
|---|---|
| Audiencia propia de 60k → distribución barata | 🟨 |
| Ingresos recurrentes y predecibles si los miembros son activos | 🟨 |
| 12 cursos = biblioteca que retiene si está completa | 🟧 |
| Cadencia constante de contenido (3 posts/semana) | 🟨 |
| Precio bajo = baja fricción de compra | 🟨 |

### Vulnerabilidades del competidor

| Vulnerabilidad | Certeza |
|---|---|
| Ticket bajo sin anual → churn alto y caja frágil | 🟧 |
| Cursos posiblemente sin terminar | 🟧 |
| Feed público puede canibalizar la conversión | 🟧 |
| Marca personal dependiente del fundador | 🟧 |
| Automatización es un tema amplio y muy commoditizado | 🟨 |
| No se ven tiers ni upsells → dejan dinero sobre la mesa | 🟧 |

---

## 6. Cómo competirles

La regla: **no compitas por ser “otra comunidad generalista de automatización de $39”**. Ahí ya tienen escala, audiencia y contenido. Compite por **enfoque, implementación, retención y pricing**.

### Jugada 1: Nicho vertical (la más recomendable)

Ellos son generalistas. Tú puedes ser específico.

Ejemplos:

- “Automatización con IA para ecommerce”.
- “Automatizaciones de Make/Zapier para agencias”.
- “Automatización de reporting financiero para pymes”.
- “n8n para equipos de operaciones”.

Ventaja: puedes cobrar **$79–$199/mes** o **$500–$2.000/año** porque resuelves un dolor concreto con ROI claro.  
Certeza de que esto funciona mejor que un generalista: 🟨.

### Jugada 2: Vende implementación, no solo contenido

Su debilidad probable: 12 cursos, feed público, poco acompañamiento.

Tu propuesta:

> “No es otra biblioteca de cursos. Es un programa para que tengas 3 automatizaciones funcionando en 30 días.”

Incluye:

- Auditoría inicial.
- Plantillas/listas de verificación.
- Retos semanales.
- Llamadas de co-working o soporte.
- Garantía de implementación.

Esto ataca directamente la deserción por “pagué y no hice nada”. 🟧

### Jugada 3: Gana en retención

Si ellos churnan al 8–10%, tú puedes ganar con menos miembros pero más LTV.

Tácticas:

- Onboarding en los primeros 7 días.
- Rituales semanales: lunes de objetivos, viernes de demos.
- Accountability partners.
- Office hours con expertos.
- Publicar tus métricas de engagement: “85% de miembros activos cada semana”.

Si su métrica es vanidosa (2.400 miembros poco activos), tú compites con “comunidad pequeña pero viva”. 🟧

### Jugada 4: Pricing y packaging

Ellos no muestran anual ni tiers. Tú sí:

- **Plan anual:** 2 meses gratis → mejora caja y reduce churn.
- **Tiers:**
  - $19–$29: solo comunidad.
  - $49–$79: comunidad + cursos/templates.
  - $199+: mentoría/implementación.
- **Upsells:** auditorías, plantillas premium, setup hecho por ti.

Así capturas tanto al que quiere barato como al que quiere resultados. 🟨

### Jugada 5: Distribución multicanal

Ellos dependen mucho de una red social y 60k seguidores. Tú reduce ese riesgo:

- SEO long-tail: “cómo automatizar X con n8n”.
- YouTube tutorials.
- Marketplaces de plantillas (Zapier, Make, Gumroad).
- Newsletter y alianzas.
- Reddit / comunidades técnicas.

Si su fundador pierde alcance o se quema, ellos sufren; tú no. 🟧

### Jugada 6: Ataca a sus insatisfechos

Busca señales públicas de queja: “no terminé los cursos”, “no implementé nada”, “es mucho contenido y poco acompañamiento”.

Mensaje posible:

> “Si ya pagaste por una comunidad de automatización y no pasó nada, esto es para ti: implementación acompañada, no más videos.”

Certeza: 🟧 (depende de que existan esas quejas).

---

## 7. Matriz rápida de competencia

| Si tu ventaja es… | Ataca con… | Certeza |
|---|---|---|
| Conocimiento técnico profundo | Nicho vertical + precio premium | 🟨 |
| Buenos procesos / consultoría | Programa de implementación “done-with-you” | 🟨 |
| Comunidad pequeña pero fiel | Retención alta + métricas de engagement públicas | 🟧 |
| Capacidad de crear contenido | SEO/YouTube + lead magnet gratuito | 🟨 |
| Capital para anuncios | Plan anual agresivo + equipo de soporte para bajar churn | 🟧 |
| Producto/tool propio | Plantillas, integraciones o software añadido a la membresía | 🟨 |

---

## 8. Qué validar para reducir la incertidumbre

Checklist externo:

1. **¿2.400 son activos o totales?**  
   Mira la plataforma: si es Skool/Circle, busca “online now”, fechas de comentarios, actividad real. 🟧

2. **¿Hay plan anual oculto?**  
   Revisa el checkout o inspecciona la página buscando “annual”, “yearly”, “12 meses”. A veces no está en pricing pero sí en el carrito. 🟨

3. **¿Cuántos cursos están terminados?**  
   Abre los 12 cursos; cuenta lecciones publicadas vs. “próximamente”. 🟨

4. **¿Qué plataforma usan?**  
   BuiltWith / Wappalyzer. Si es Skool/Kajabi/Circle con plan pago, sus fees son bajos → márgenes aún mayores. 🟨

5. **¿Tienen equipo o es solo el fundador?**  
   LinkedIn, página “About”, ofertas de empleo. Más equipo = más costes fijos. 🟧

6. **¿De dónde viene su tráfico?**  
   SimilarWeb / SEMrush / Ubersuggest. ¿Redes, SEO, anuncios? 🟧

7. **¿La audiencia del fundador es real?**  
   Social Blade / engagement rate. 60k con poco engagement = menos conversiones de lo que parece. 🟧

8. **Sentimiento público**  
   Reddit, X/Twitter, Trustpilot, comentarios. Busca quejas de churn o cursos incompletos. 🟧

9. **Cambios de precio**  
   Wayback Machine para ver si antes valía más/menos. 🟨

10. **Emails de onboarding y retención**  
   Si es ético y no viola sus Términos, date de alta con una cuenta real o de prueba para ver su funnel, upsells y emails de cancelación. ⚠️ Revisa antes las condiciones legales de la plataforma. 🟧

---

## 9. Lo que necesito de ti para afinar el ataque

Para pasar de “teardown general” a **posicionamiento exacto**, dime:

1. ¿Tu producto es comunidad, curso, SaaS, consultoría o mezcla?
2. ¿Tu precio actual o objetivo?
3. ¿Tu tamaño de audiencia y canal principal?
4. ¿Tu ventaja real: contenido, técnica, soporte, nicho, herramienta?
5. ¿Quieres competir en volumen o en margen premium?

Con eso te armo el **encaje competitivo** y el **pricing de ataque**.

---

### Resumen final en una frase

**Sé que piden $39 y muestran 2.400 miembros; infiero que facturan probablemente entre $0,9M y $1,1M ARR brutos si esos miembros son activos, con márgenes muy altos pero un modelo frágil por churn y falta de anual; y mi recomendación es no competirles en precio generalista, sino ganarles por nicho, implementación acompañada, retención y mejor packaging.** 🟨/🟧