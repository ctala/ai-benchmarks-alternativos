# Claude Fable 5.1 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 5.04 | quality: 6.0
- latency_total: 65.371s | tokens_per_second: 58.7
- input_tokens: 288 | output_tokens: 3836

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

Antes de nada: con seis datos públicos solo puedo darte **rangos y hipótesis**, no cifras. Voy a separar en todo momento *hecho* (lo que me diste), *inferencia* (lo que deduzco) y *supuesto* (lo que asumo para poder calcular). Si una inferencia tiene baja certeza, lo digo.

---

## 1. Lo que sabemos de verdad (hechos)

| Dato | Observación |
|---|---|
| "2.400 miembros" en portada | Es un número de **marketing**, no una métrica financiera. No sabes si incluye gratuitos, antiguos, pruebas, o si está desactualizado. |
| $39/mes visible | Único precio confirmado. La ausencia de plan anual visible **no significa que no exista** (muchas plataformas lo esconden en checkout). |
| 3 posts/semana en feed público | Cadencia moderada. No sabes quién los escribe ni qué engagement reciben. |
| Fundador: 60.000 seguidores | Activo de distribución. No sabes el engagement real ni cuánto de ese tráfico convierte. |
| 12 cursos listados | Catálogo. No sabes cuántos están completos ni cuándo se actualizaron. |

Todo lo que viene a partir de aquí es **inferencia**.

---

## 2. ¿Cuánto factura?

### Cálculo nominal (lo que la portada quiere que creas)
2.400 × $39 = **$93.600/mes** ≈ $1,1M/año.

**Certeza de que facture eso: baja.** Casi nadie que muestra "X miembros" tiene al 100% pagando el precio de lista.

### Escenarios con supuestos explícitos

| Escenario | % que paga | Precio medio real | MRR estimado | Cuándo es plausible |
|---|---|---|---|---|
| Pesimista | 35% | $30 | **~$25k** | El contador suma gratuitos + bajas históricas, hay anual con descuento fuerte, o cifra inflada. |
| Base | 60% | $34 | **~$49k** | Hay nivel gratuito o el número es acumulado "alguna vez entraron". Es lo más típico en plataformas tipo Skool/Circle. |
| Optimista | 90% | $37 | **~$80k** | El contador es honesto, miembros activos, poca gente en anual. |

**Mi apuesta (certeza media-baja): entre $40k y $60k MRR.** Razones:
- Plataformas de membresía suelen mostrar el número total acumulado o incluyen plan gratuito.
- Un negocio de $94k MRR reales con un solo fundador visible normalmente ya tiene equipo, más contenido y más señales de escala que "3 posts por semana".
- El ratio 2.400 miembros / 60.000 seguidores = 4%. Si todos fueran pagos, sería una conversión excepcionalmente alta para audiencia en redes (lo habitual que veo citado es 1–3%). Eso me hace pensar que una parte es gratuita o inactiva.

**Lo que NO sé y cambia todo:** churn, mezcla anual/mensual, si hay upsells (coaching, cohortes, afiliados). Un upsell de $500–2.000 a un 5% de miembros podría duplicar lo que calculo.

---

## 3. ¿Qué tan sano es el negocio?

Aquí la honestidad obliga: **con estos datos no puedes saberlo.** Lo que sí puedes hacer es leer señales y asignarles peso.

### Señales positivas (inferencia)
- **Dependencia del fundador = distribución gratuita.** 60k seguidores es un canal de adquisición propio. Mientras el fundador publique, el CAC tiende a cero. (Certeza media.)
- **$39/mes es un precio "serio".** No es el típico $9 de comunidad hobby. Sugiere que ha validado disposición a pagar. (Certeza media.)
- **12 cursos sugiere tiempo en el mercado.** Difícil producir eso en menos de 12–18 meses. (Certeza media.)

### Señales de riesgo (inferencia)
- **Riesgo de persona única.** Si el fundador es la cara, el tráfico y probablemente el contenido, el negocio es tan sano como su energía. (Certeza media-alta: casi siempre pasa en este modelo.)
- **12 cursos sin indicar estado = posible catálogo "fantasma".** Muchas membresías listan cursos a medio hacer para parecer más grandes. Si 4 de 12 están completos, el valor percibido se desinfla rápido en los primeros 30 días → churn alto. (Certeza baja; hay que verificar.)
- **3 posts/semana es poco para $39/mes** si eso es todo el contenido nuevo. Las membresías de automatización mueren cuando el miembro siente que "ya vio todo". (Certeza media.)
- **"Automatización" es una categoría muy saturada** y con herramientas que cambian cada 3 meses. El contenido se queda viejo rápido = presión constante de actualización. (Certeza alta.)

### Mi lectura general (certeza baja-media)
Parece un negocio **rentable pero no necesariamente robusto**: probablemente margen alto (costos casi cero), ingresos decentes, pero frágil ante churn y dependiente de una persona. El patrón típico es: crece mientras el fundador está en modo "lanzamiento", se estanca cuando deja de empujar.

---

## 4. Cómo verificar antes de decidir (lo más valioso de todo)

Por $39 obtienes más inteligencia que cualquier análisis externo. Entra un mes y mide:

1. **Engagement real:** ¿cuántos comentarios tiene cada post? ¿Cuántos miembros distintos postean en una semana? Si de 2.400 ves 40–80 activos, el número de pago real probablemente está en el escenario pesimista/base.
2. **Fechas de los cursos:** ¿cuándo se publicó cada módulo? ¿Hay cursos con 2 lecciones de 10 anunciadas?
3. **Checkout:** mira si aparece plan anual, prueba gratuita o descuento. Eso te dice el precio medio real.
4. **Preguntas sin responder:** señal de que el fundador no está o no escala.
5. **Wayback Machine:** mira cuántos miembros mostraban hace 6 y 12 meses. Si pasó de 2.000 a 2.400 en un año, está estancado. Si pasó de 800 a 2.400, está creciendo fuerte.
6. **Qué piden los miembros y nadie les da:** ahí está tu hueco.

---

## 5. Cómo competir

Lo que voy a proponer depende de lo que verifiques en el punto 4. Pero con lo que hay:

### No hagas esto
- **No compitas en volumen de cursos.** Ya tienen 12. Tú tendrías 2. Pierdes en una comparación de catálogo.
- **No compitas solo en precio.** Bajar a $19 te posiciona como la versión barata de algo que no has demostrado que iguales.
- **No intentes replicar la audiencia del fundador.** 60k seguidores son años. No es un atajo disponible.

### Ángulos con mejor probabilidad (ordenados por mi certeza)

**a) Resultado concreto en lugar de catálogo.** (Certeza media-alta de que funciona)
Su propuesta implícita es "aprende automatización" (amplia, vaga). La tuya puede ser "en 6 semanas tienes X automatizado para tu negocio de tipo Y". Nicho + resultado vence a catálogo cuando el comprador está cansado de ver videos.

**b) Atacar el punto débil estructural: contenido que envejece.** (Certeza media)
Si en el mes de prueba confirmas que hay cursos desactualizados, tu diferenciador es "siempre al día con la versión actual de las herramientas" + changelog público. Es barato de prometer y muy visible.

**c) Acceso, no información.** (Certeza media)
Si el fundador no responde (verifícalo), vende lo que ellos no pueden escalar: revisiones de automatizaciones, office hours reales, cohortes pequeñas. Puedes cobrar **más** que $39 por esto, no menos.

**d) Mismo precio, menor fricción.** (Certeza baja-media)
Si descubres que no tienen prueba gratuita ni garantía, ofrécelas. En membresías, reducir el riesgo de entrada suele importar más que el precio.

### Lo que necesitas para que cualquiera de estas funcione
Un canal de distribución propio. Sin eso, el mejor producto no se vende. Si no tienes audiencia, tu primera prioridad no es el producto: es decidir dónde vas a construir 5.000 personas que confíen en ti (newsletter, un nicho de una red, partnerships).

---

## Resumen en tres líneas

- **Facturación:** probablemente $40–60k MRR, no los $94k que insinúa la portada. Certeza baja; verificable por ~$39 y una tarde.
- **Salud:** rentable pero frágil: dependencia del fundador, contenido perecedero, riesgo de catálogo inflado. Certeza media.
- **Cómo competir:** no por volumen ni precio; por resultado concreto, actualización constante o acceso humano. Y antes de nada, construye tu propio canal.

Si entras un mes y me cuentas qué viste (actividad real, fechas, checkout), puedo afinar esto bastante.