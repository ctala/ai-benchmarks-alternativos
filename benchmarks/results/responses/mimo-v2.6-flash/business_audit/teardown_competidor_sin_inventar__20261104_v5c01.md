# MiMo V2.6 Flash — business_audit/teardown_competidor_sin_inventar

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 5.88 | quality: 6.0
- latency_total: 127.561s | tokens_per_second: 33.8
- input_tokens: 203 | output_tokens: 4314

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

# Teardown del competidor

Primero la regla de la casa: separo lo que **sé**, lo que **infiero** y lo que **no puedo saber**. Donde no hay dato, no invento número.

---

## 1. Mapa epistémico: qué hay realmente en esa página

| Dato | Estado |
|---|---|
| Comunidad de pago sobre automatización | **SABIDO** |
| Precio $39/mes | **SABIDO** (solo lo que muestra la landing) |
| "2.400 miembros" | **SABIDO como claim** — no sabemos si son pagantes, free-tier o acumulado histórico |
| 3 posts/semana en feed público | **SABIDO** — pero es feed *público*, no actividad interna |
| 60.000 seguidores del fundador | **SABIDO** |
| 12 cursos listados | **SABIDO** — no se ve finalización, ni si están incluidos en la membresía o se venden aparte |
| MRR, churn, LTV, CAC, retención, margen, tamaño de equipo | **NO SE SABE. Ninguno.** |

La pregunta "¿cuánto factura?" **no tiene respuesta directa desde fuera**. Todo lo que sigue es una caja acotada con supuestos explícitos.

---

## 2. Facturación: rango acotado

**SABIDO (aritmética pura):** 2.400 × $39 = **$93.600/mes** = **$1.123.200/año**.

Ese es el **techo absoluto**, y solo si los 2.400 son pagantes activos al precio de lista sin descuentos. Probablemente no lo sean.

**Supuesto crítico (INFERIDO — certeza MEDIA):** los "miembros" que se muestran en portada suelen ser **signups acumulados**, incluyendo free-tier y gente que ya canceló. Es un número de marketing, no un número contable. Ninguna plataforma pública muestra MRR real en la landing.

| % de los 2.400 que pagan | MRR | Facturación bruta anual |
|---|---|---|
| 100% (techo) | $93.600 | **$1.123k** |
| 75% | $70.200 | **$842k** |
| 50% | $46.800 | **$562k** |
| 35% | $32.760 | **$393k** |
| 25% (2.400 = acumulado histórico) | $23.400 | **$281k** |

**SABIDO (estructura de costos):** sobre eso restá **8–13%** por fees de plataforma + procesamiento de pagos. Neto = 87–92% de la cifra bruta.

**Lectura (INFERIDO — certeza MEDIA):** el rango honesto de facturación anual es **~$280k a ~$1.12M**, con el escenario más probable en **$400k–$650k**. No voy a afinar más porque cualquier punto más preciso sería invención.

**Ojo, hay una segunda línea de ingreso invisible (INFERIDO — certeza BAJA):** 12 cursos podrían venderse también por fuera de la membresía. Si sí, todo el cuadro anterior está incompleto.

---

## 3. Salud del negocio

### Señales observables (SABIDO)
- **Precio visible y estable:** $39/mes es punto medio de mercado para comunidades de automatización/IA. Ni premium ni low-end.
- **Cadencia de 3 posts/semana:** hay motor de contenido y disciplina de publicación.
- **Catálogo de 12 cursos:** volumen de producción alto.
- **Audiencia del fundador de 60k:** tiene canal de adquisición propio, no depende 100% de pago por tráfico.

### Señales inferidas (marcadas)

**a) Modelo mensual-only visible → exposición al churn.**
INFERIDO — certeza **MEDIA**. Que no se vea plan anual no significa que no exista (puede estar en el checkout o en la página de precios interna). Pero si realmente es solo mensual, el negocio es más frágil de lo que la cifra de miembros sugiere.

**b) 12 cursos sin prueba de finalización → patrón de "contenido sobre completado".**
INFERIDO — certeza **MEDIA**. La base rate conocida de finalización en cursos online es 10–20%. Un catálogo grande sin indicador de progreso suele señalar que la retención se apoya en la novedad del contenido, no en resultados. Es el síntoma más peligroso que vi en esta página.

**c) El negocio es al fundador, no al producto.**
INFERIDO — certeza **ALTA**. 60k seguidores + 3 posts/semana públicos + solo un nombre visible = **riesgo clave-persona alto**. Si el fundador para de publicar, el funnel se corta. No hay evidencia de comunidad auto-sostenida.

**d) Los 2.400 podrían ser acumulados, no activos.**
INFERIDO — certeza **MEDIA**. Si el proyecto lleva 2–3 años, 2.400 signups acumulados con ~35–50% pagando sería cifra perfectamente normal y nada espectacular.

### Veredicto de salud
**No se puede decir si es sano.** Lo que sí se puede decir: **no tiene ningún indicador público de retención ni de resultados**. Un negocio de membresía que comunica "cuánta gente entró" y no "cuánta gente se queda o termina" está evitando la métrica que más le dolería. Eso es información en sí misma.

---

## 4. Cómo compito

No compitas donde es fuerte (contenido, catálogo, audiencia del fundador). Compite donde es **invisible**.

**1. Ataca la métrica que esconde.**
Ellos muestran 12 cursos; tú muestra **automatizaciones enviadas a producción, horas ahorradas, casos con números**. Prueba de finalización > cantidad de módulos. Es el hueco más grande de su página.

**2. Rompe la dependencia del fundador.**
Su modelo es broadcast: 3 posts/semana de una sola persona. Tú construye valor **entre pares**: biblioteca de plantillas de los miembros, peer review de flujos, oficinas de horario. Si tu comunidad funciona cuando tú no publicas, ganas estructuralmente.

**3. El nicho mata al generalista.**
$39/mes de "automatización" genérica es amplio y defendible a duras penas. Elige **un segmento** (agencias / e-commerce / creadores / ops internos) donde puedas cobrar **$79–$149/mes** con prueba de ROI. A mayor precio, menos volumen necesario para igualar su facturación.

**4. Empaqueta el año.**
Si ellos son mensual-only (supuesto medio), ofrece **anual con ahorro visible** y una garantía de resultado. Capturas el sensible al precio y reduces tu propio churn.

**5. No pelees por cursos, pelea por implementación.**
Su riesgo es el abandono tras comprar. Ofrece *done-with-you*: el miembro sale con algo funcionando en 14 días. Eso es impagable frente a 12 cursos vistos.

---

## 5. Cómo dejar de adivinar: el plan de inteligencia por $39

Es la mejor inversión de toda esta análisis.

- **Suscríbete un mes ($39).** Es más barato que cualquier herramienta de scraping y te da la verdad.
  - ¿Hay onboarding real o te sueltan en un foro vacío?
  - ¿Cuántos posts hay en el feed **interno** vs. el público? Si el interno está muerto, el negocio es peor de lo que parece.
  - ¿Los cursos muestran % de finalización?
  - **Flujo de cancelación:** si te ofrecen descuento o plan anual ahí, tu supuesto del punto 4 se derrumba.
- **Mide el feed público 4 semanas seguidas.** 3 posts/semana puede ser cadencia real o picos de lanzamiento.
- **archive.org sobre su landing** → evolución de precios y claims de miembros.
- **Meta Ad Library** → si paga tráfico, su CAC no es cero y su audiencia no es solo orgánica.
- **Busca quejas:** Reddit, X, Trustpilot, "nombre + estafa/cancelar".
- **Ofertas de empleo y sus herramientas** → tamaño de equipo real.
- **Determina la plataforma** (Skool, Circle, Kajabi...) → revela fees, features y límites.

---

**Resumen honesto:** de esta página sé el precio, el claim de miembros y el catálogo. **No sé su facturación** (rango probable $400k–$650k anuales), **no sé si está sano**, y el único dato de salud que me dan —12 cursos sin evidencia de finalización— es más bien una señal de riesgo. Tu ventaja no está en tener más cursos que ellos: está en **probar lo que ellos no muestran**.