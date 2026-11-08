# DeepSeek V4.1 Flash — business_audit/teardown_competidor_sin_inventar

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 3.06 | quality: 2.0
- latency_total: 101.779s | tokens_per_second: 103.0
- input_tokens: 219 | output_tokens: 10484

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

**Teardown del competidor — solo con datos públicos**

## 0. Nivel de certeza
- **Hechos duros:** alta. Son los 5 datos que ves.
- **Matemática directa:** alta. Si todos pagan y pagan $39/mes, la cuenta es exacta.
- **Facturación real:** media-baja. No sabemos cuántos de los 2.400 son pagos, ni churn, descuentos, anuales, refunds.
- **Salud del negocio:** media-baja. Depende de churn, CAC, equipo y concentración en el fundador.
- **Cómo competir:** opinión estratégica, no dato.

---

## 1. Hechos duros
- Comunidad de pago sobre automatización.
- Muestra **2.400 miembros** en portada.
- Precio visible: **$39/mes**.
- Publican **3 posts/semana** en feed público.
- Fundador con **60.000 seguidores** en una red social.
- **12 cursos listados**, estado de finalización desconocido.

---

## 2. Facturación estimada

### Escenario base: si todos los miembros pagan
- **MRR bruto:** 2.400 × $39 = **$93.600/mes**
- **ARR bruto:** $93.600 × 12 = **$1.123.200/año**

Pero “miembros” no siempre significa “pagando”. Puede incluir free, trials, lifetime, comps o inactivos. Escenarios:

| % que realmente paga | Miembros pagos | MRR bruto | ARR bruto |
|---|---:|---:|---:|
| 100% | 2.400 | $93.600 | $1,12M |
| 85% | 2.040 | $79.560 | $954.720 |
| 70% | 1.680 | $65.520 | $786.240 |
| 50% | 1.200 | $46.800 | $561.600 |

### Ajustes probables
- **Plan anual con descuento:** si parte paga anual con ~20% off, el ARPU baja. Ejemplo: 30% anual → ARPU ~$36,6 → MRR ~$88.000 en el escenario 100%.
- **Fees de plataforma + pasarela:** 5–10% típico.
- **Refunds:** 1–5%.
- **Afiliados:** si pagan 20–40% por ventas afiliadas, el ingreso neto baja bastante.
- **Neto antes de costos operativos:** en el escenario 85% pagando, podrías estar en **$65.000–$75.000/mes** después de fees/refunds.

**Mi estimación central:**  
**MRR bruto: $65.000–$94.000/mes**  
**ARR bruto: $0,8M–$1,1M/año**  
**Certeza: media-baja.** Si solo la mitad paga, cae a **$0,5M–$0,6M ARR**.

---

## 3. Salud del negocio

### Lo que más importa: churn
Con 2.400 miembros, necesitan reemplazar cancelaciones cada mes solo para no encoger.

| Churn mensual | Cancelaciones/mes | Vida media | LTV bruto a $39 |
|---:|---:|---:|---:|
| 5% | 120 | 20 meses | $780 |
| 8% | 192 | 12,5 meses | $487 |
| 10% | 240 | 10 meses | $390 |
| 15% | 360 | 6,7 meses | $260 |

Si su churn es 8%, necesitan **192 nuevos pagos/mes** para mantenerse planos. Si es 10%, **240/mes**. Con 3 posts/semana y 60k seguidores, es posible, pero no automático. Si no generan eso, están cayendo aunque la portada siga diciendo 2.400.

### Señales de salud
- **Fundador con 60k seguidores:** activo fuerte. Pero 2.400/60.000 = **4% de sus seguidores**. Si son pagos, es una conversión alta; si incluye free, es normal. Riesgo: dependencia extrema del fundador.
- **3 posts/semana:** cadencia decente, no agresiva. Puede ser suficiente si la audiencia es muy nicho, pero no parece una máquina de adquisición agresiva.
- **12 cursos listados:** si están terminados y actualizados, es un moat de contenido. Si están a medias o desactualizados, es debilidad y oportunidad para ti.
- **Precio $39/mes:** bajo para automatización B2B. Si venden a empresas, están dejando dinero en la mesa. Si venden a individuos/prosumers, es estándar.
- **Equipo desconocido:** si es solo el fundador, con $65k–$94k MRR es muy sano. Si son 5+ personas con ads fuertes, el margen puede ser mucho menor.
- **Plataforma:** si es tipo Skool/Circle, los fees son bajos, pero el contador de miembros puede inflarse.

**Veredicto de salud probable:**  
Si los 2.400 pagan en su mayoría, churn <8% y costos bajos: **negocio muy sano, de 6–7 cifras, probablemente rentable**.  
Si 2.400 incluyen free, churn >12% y dependen solo del fundador: **negocio frágil, más de marketing que de producto**.  
**Certeza: media-baja.**

---

## 4. Cómo competir

No compitas frontalmente en “más cursos” o “más barato”. Ese es su terreno. Gánale por **nicho, implementación y resultados**.

### A. Posicionamiento
- Ellos: comunidad general de automatización + 12 cursos.
- Tú: **“Automatización para [nicho específico] con resultados en 30 días”**.
- Ejemplos: agencias, ecommerce, inmobiliaria, clínicas, consultores, operaciones, soporte.
- Promesa concreta: “Automatiza X proceso en 7 días sin código” o “Ahorra 10 horas/semana en [tarea]”.

### B. Oferta
- Menos cursos, más implementación.
- Incluye: plantillas específicas del nicho, auditorías, retos, live Q&A, accountability, certificación, job board o directorio.
- Precio: no necesitas ir a $19. Puedes ir a **$49–$99/mes** por nicho, o **$149–$299/mes** si incluyes done-with-you/implementación.
- Añade plan anual con descuento para mejorar cash flow y retención.

### C. Adquisición
- Contenido founder-led: LinkedIn, YouTube, X, TikTok.
- SEO: “automatización para [nicho]”, “alternativa a [competidor] para [nicho]”.
- Webinars/talleres gratuitos → oferta paid.
- Partnerships con herramientas, agencias, consultores.
- Afiliados/referidos.
- Comparativas: “Competidor vs [tu marca] para [nicho]”.
- Ataca a su audiencia con contenido de migración: “Si estás en [competidor] y quieres implementar, esto te sirve”.

### D. Retención
- Onboarding con quick win en 7 días.
- Activación: que publiquen su primera automatización en la comunidad.
- Accountability: grupos pequeños, retos mensuales.
- Live Q&A semanal.
- Casos de éxito medibles.
- Certificación o insignias.
- Comunidad más activa y soporte más rápido.

### E. Flanqueo probable
Su debilidad más probable: **contenido genérico, biblioteca de cursos y poca implementación**.  
Tu ataque: **especialización, soporte, plantillas, resultados medibles y comunidad activa**.  
No intentes tener 12 cursos. Ten 1 transformación que funcione.

### F. Métricas que tú debes vigilar
- Churn mensual <8%.
- Activación >60% en 7 días.
- LTV/CAC >3.
- Payback <6 meses.
- NPS >50.
- % de miembros que obtienen un resultado en 30 días.

---

## 5. Qué verificar antes de mover ficha
- **Wayback Machine:** mira la evolución de “2.400 miembros”.  
  - Si hace 6 meses tenían 2.000 y hoy 2.400: crecimiento neto ~20% total, ~3% mensual.  
  - Si tenían 1.800 y hoy 2.400: ~33% total, ~5% mensual.  
  - Si está plano: churn alto o adquisición estancada.
- **¿Pagan o no?** Busca checkout, términos, reviews, quejas. Si el contador incluye free, el revenue real es mucho menor.
- **Plan anual:** historial de precios. Si nunca han subido precio, puede ser debilidad.
- **Ads:** Facebook Ad Library, Google Ads. Si gastan fuerte, su CAC puede ser alto.
- **Afiliados:** comisión. Si es 30–50%, su margen neto es menor.
- **Equipo:** LinkedIn. ¿Es solo el fundador o hay 10 personas?
- **Engagement:** ratio de comentarios/likes. 60k seguidores con poco engagement no impresiona.
- **Cursos:** fechas de actualización, reviews. Si están viejos, oportunidad.

---

## 6. Bottom line
- **Facturación probable:** $0,8M–$1,1M ARR bruto si la mayoría paga. Si solo la mitad paga, $0,5M–$0,6M.
- **Salud:** probablemente rentable si es solo/small team y churn <8%. Frágil si depende del fundador, tiene churn >12% o muchos miembros no pagos.
- **Cómo competir:** nicho vertical + implementación + resultados medibles. No compitas por precio ni por cantidad de cursos.
- **Certeza:** alta en la matemática, media-baja en la facturación real. Cualquier cifra exacta es inventada.