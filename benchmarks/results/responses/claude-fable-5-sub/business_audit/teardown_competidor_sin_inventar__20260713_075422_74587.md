# Claude Fable 5 (suscripción) — business_audit/teardown_competidor_sin_inventar

- model_id: `claude-fable-5`
- success: True  | final: 3.28 | quality: 3.6
- latency_total: 109.43s | tokens_per_second: 56.2
- input_tokens: 2 | output_tokens: 6148

## Respuesta completa

# Teardown: comunidad de automatización a $39/mes

Antes de nada, separemos las capas. Tienes 6 datos duros y me pides 3 conclusiones (facturación, salud, cómo competir). Las dos primeras son **inferencias con rangos**, no cifras. Marco todo.

---

## 1. Lo que SABEMOS (datos duros)

| # | Dato | Fuente |
|---|---|---|
| 1 | "2.400 miembros" en portada | Página pública |
| 2 | Precio visible: $39/mes, sin anual visible | Página pública |
| 3 | 3 posts/semana en feed público | Observación tuya |
| 4 | Founder: 60.000 seguidores en una red | Página pública |
| 5 | 12 cursos listados | Página pública |
| 6 | Nicho: automatización, plataforma tipo membresía | Página pública |

Todo lo que sigue es inferencia.

---

## 2. ¿Cuánto factura?

**La pregunta que lo cambia TODO y que aún no está respondida: ¿los 2.400 son todos de pago, o hay tier gratis?** Tú lo describes como "comunidad de pago", pero el contador de portada en plataformas tipo Skool/Circle suele incluir a todos los miembros, gratis incluidos. Esto mueve la estimación en un factor de **10-30x**. Por eso van dos escenarios:

### Escenario A: paywall duro (todos pagan)
- 2.400 × $39 = **$93.600/mes bruto teórico** [ARITMÉTICA, no estimación]
- Ajuste realista: grandfathered a precios viejos, becados, equipo, anuales con descuento no visible → **$70K–90K MRR** [INFERENCIA — confianza media, condicionada a que A sea cierto]

### Escenario B: freemium (2.400 = total, pagan una fracción)
- Conversión free→paid típica en comunidades: 2–8%
- 48–192 pagando → **$1.9K–7.5K MRR** [INFERENCIA — confianza media, condicionada a B]

### ¿Cuál escenario es más probable?
Aquí hay una señal que juega **contra** el escenario A: la matemática de seguidores.

- 60.000 seguidores → 2.400 pagando = **4% de conversión seguidor→cliente**. El benchmark de creadores monetizando audiencia propia es 0.5–2% lifetime. 4% pagando es top-decile, posible pero raro. [INFERENCIA — confianza media]
- 60.000 seguidores → 2.400 miembros *gratis* = 4% a registro free. Eso es completamente normal. [INFERENCIA — confianza alta]

**Mi lectura: 60/40 a favor del escenario B o de un A "diluido"** (paywall pero con mucho legacy barato/trials). Salvo que tengan canales de adquisición fuertes fuera de esa red social (email, SEO, ads) — que NO SABEMOS.

**Cómo resolverlo en 10 segundos:** mira el botón de join. Si dice "Join for free" o similar → escenario B confirmado. Si dice "$39/month" como única puerta → escenario A. Este único dato vale más que todo el resto del análisis.

---

## 3. ¿Qué tan sano es el negocio?

**Verdicto corto: no se puede saber desde fuera. Pero hay 3 proxies, y dos huelen mal.**

**a) La rueda de churn (la matemática que no perdona).** A $39/mes, churn típico de comunidades pagas: 5–10% mensual. Para *mantener* 2.400 pagando necesitan 120–240 altas nuevas/mes, para siempre. Eso es 0.2–0.4% de su audiencia total cada mes, sostenido. Es una cinta de correr, no un activo. [INFERENCIA — confianza alta en la mecánica, media en las cifras de churn]

**b) 3 posts/semana en el feed público.** Dos lecturas posibles y NO SABEMOS cuál aplica:
- Si el feed público es solo un escaparate de marketing y el feed real está detrás del paywall → dato irrelevante.
- Si eso refleja la actividad real → para 2.400 miembros es **anémico**. Una comunidad paga sana de ese tamaño genera decenas de posts/día de los miembros, no 3/semana del equipo. Sería la señal de churn futuro más fuerte del teardown. [INFERENCIA — confianza baja hasta verificar cuál caso es]

**c) 12 cursos "listados", terminados desconocidos.** Patrón clásico de valor percibido inflado: publicar el outline como curso. Si 5 de 12 están a medias, eso genera la queja #1 que mata comunidades pagas: "pagué por cursos que no existen". Es tu punto de ataque más barato de verificar. [INFERENCIA — confianza baja, es hipótesis a testear]

**d) Lo que NO SABEMOS y importa:** antigüedad de la comunidad, tendencia del contador (¿creciendo o estancado?), churn real, si el founder tiene otros canales de adquisición, si su engagement en esos 60K seguidores es real (60K con <1% de interacción = audiencia muerta o comprada).

---

## 4. Cómo les compites

Contexto: tú tienes 1.000+ miembros con freemium a $35/mes Premium. Ellos aparentan más volumen. **No compitas por el contador — compite donde tu modelo ya es estructuralmente distinto:**

**1. No pelees tráfico, pelea conversión y retención.** Tu propia doctrina ya lo dice: el cuello es free→paid y el paid lo pone el warm. Si el competidor está en la cinta de correr de 120-240 altas/mes para no encogerse, su punto débil es retención. Tu anual a $249 (41% descuento) es un arma que ellos, visiblemente, no tienen: no muestran plan anual. Cash adelantado + churn estructuralmente menor. [Ventaja verificable]

**2. Prueba verificable vs. promesa listada.** Ellos: "12 cursos listados, no se sabe cuántos terminados". Tú: 24 cursos publicados + adjuntos accionables + sistemas vivos en producción (actor Apify, benchmark público, workflows reales). Contenido comparativo honesto tipo "qué mirar antes de pagar una comunidad de automatización" (sin nombrarlos) convierte esa asimetría en funnel. [Ventaja verificable]

**3. Si son anglo, el idioma es la cuña entera.** NO SABEMOS su mercado. Si es inglés, "lo mismo pero en español, con casos LATAM y pricing LATAM" no es competir, es otro mercado. Si es español, sube prioridad de los puntos 1-2.

**4. Roba el playbook, no la audiencia.** Sus 3 posts/semana públicos son su marketing destilado gratis: qué formatos, qué ganchos, qué CTAs. Eso va a tu content-spy, no a imitación.

---

## 5. Recon pendiente (barato, cierra los gaps grandes)

En orden de costo/valor:
1. **Botón de join** → resuelve freemium vs paywall. Gratis, 10 segundos.
2. **Wayback Machine sobre su página** → contador de miembros histórico = growth rate y churn neto real. Gratis, 15 minutos. Es el dato que convierte "2.400" de foto en película.
3. **Engagement del founder en su red** → likes/comments por post vs 60K seguidores. Gratis.
4. **Quejas públicas** (Reddit, X, Trustpilot, comunidades vecinas) → churn cualitativo. Gratis.
5. **Pagar 1 mes ($39)** → el research más barato que existe: cursos terminados reales, actividad real del feed, onboarding, churn visible en "last active" de miembros. Un mes de espionaje por el precio de un almuerzo.

Con los puntos 1, 2 y 5 este teardown pasa de rangos con factor 10x a una estimación con ±20%. Si quieres, cuando tengas esos datos lo formalizamos como teardown completo en `community-teardowns/` con el formato de los análisis previos.

**Resumen en una línea:** facturan entre $2K y $90K MRR (rango absurdo porque falta UN dato: el botón de join), su riesgo estructural es la cinta de churn sin anual visible, y tu jugada no es alcanzar su contador sino explotar retención + prueba verificable + (posiblemente) idioma.