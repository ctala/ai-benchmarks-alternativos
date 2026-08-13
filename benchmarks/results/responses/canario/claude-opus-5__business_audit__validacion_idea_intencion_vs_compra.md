# Claude Opus 5 — business_audit/validacion_idea_intencion_vs_compra

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 35.686s | tokens_per_second: 57.4
- input_tokens: 264 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un inversor que ha visto morir muchos proyectos por validar mal. Distingues sin piedad entre lo que la gente DICE y lo que la gente PAGA.

**user:**

Creo que ya validé mi idea y quiero renunciar a mi trabajo para dedicarme a esto a tiempo completo. Mis datos:

- Hice una encuesta a 40 personas de mi red.
- El 85% dijo que el problema les duele.
- El 72% dijo que pagaría $30 al mes por una solución.
- Tengo una lista de espera de 210 correos que se anotaron desde una landing page.
- Ingresos hasta hoy: $0. Todavía no cobré nada porque el producto no está listo.

¿Está validado? ¿Renuncio?


## Respuesta completa

## Veredicto corto

No, no está validado. Y no, no renuncies.

Tienes **$0 en ingresos**. Esa es la única línea de tus datos que habla de dinero, y dice cero. Todo lo demás son opiniones gratuitas.

---

## Desarmemos tus "datos"

**"40 personas de mi red"**
Tu red te quiere. Te van a decir que sí. Encuestar a tu red sobre tu propia idea no es investigación, es buscar aplausos. El sesgo de complacencia aquí es brutal: la gente miente para no incomodarte, y ni siquiera sabe que está mintiendo.

**"85% dijo que el problema les duele"**
El 85% de la gente dice que le duele casi cualquier problema si se lo describes bien. Preguntar "¿te molesta X?" tiene una tasa de sí altísima y valor predictivo casi nulo. La pregunta que importa no es si les duele, es **qué han hecho al respecto**: ¿cuánto gastan hoy en resolverlo? ¿qué hoja de cálculo, qué herramienta a medias, qué asistente, qué proceso manual? Si no hay ningún gasto ni esfuerzo actual, el dolor es teórico.

**"72% pagaría $30 al mes"** ← esta es la más peligrosa
Preguntar por intención de compra hipotética es el error clásico. En la práctica, la conversión de "dije que pagaría" a "pagué" suele caer entre 5 y 20 veces. Tu 72% en el mundo real es plausiblemente 5-10%. Y ese número lo pusiste tú en la pregunta; no descubriste el precio, lo sugeriste. Nadie negoció contigo. Nadie dijo "es caro". Nadie sacó una tarjeta.

**"210 correos en lista de espera"**
Un email cuesta cero. Es la moneda más devaluada que existe. Una lista de espera fría-tibia convierte típicamente entre 2% y 5% a pago cuando lanzas. Haz la cuenta:

> 210 × 4% = **8 clientes** × $30 = **$240 MRR**

Y eso es el escenario optimista, con la lista más caliente que tendrás en tu vida (gente que se anotó voluntariamente). ¿Renuncias a tu salario por $240 al mes?

**"El producto no está listo"**
Esta frase es donde mueren los proyectos. Es la excusa perfecta para no enfrentar nunca el momento del cobro. Te permite vivir indefinidamente en la fase agradable de la validación: la que solo tiene buenas noticias.

---

## Lo que sí es validación

Una sola cosa: **dinero de desconocidos, transferido antes de que exista el producto.**

Tres niveles, de peor a mejor:

1. **Email en landing** → señal de curiosidad. Casi ruido.
2. **Carta de intención / persona en llamada diciendo "sí"** → señal débil.
3. **Cobro efectivo, tarjeta pasada, dinero en tu cuenta** → señal. La única.

Puedes cobrar hoy sin producto. Se llama preventa, y es completamente legítimo si eres honesto:

> "Lanzo en 8 semanas. Precio fundador: $30/mes, primeros 3 meses. Cobro ahora, si no lanzo te devuelvo todo."

Si nadie pasa la tarjeta con garantía de devolución total, el problema no dolía tanto.

**Alternativa igual de válida: entrega manual.** No construyas el software. Haz el trabajo a mano, tú, por WhatsApp y Google Sheets, cobrando los $30. Es horrible, no escala, y es exactamente lo que necesitas hacer. Te enseña el problema real y te da ingresos verdaderos. Si nadie paga por el resultado hecho a mano, tampoco pagará por el software.

---

## Tu prueba de 45 días (sin renunciar)

Objetivo: convertir opinión en transacciones.

**Semana 1-2**
- Escribe a los 210. No un anuncio: una oferta con link de pago.
- En paralelo, 15 conversaciones de 20 minutos con los que respondan. Preguntas de pasado, no de futuro: *¿cómo lo resolviste la última vez? ¿cuánto tiempo/dinero te costó? ¿qué probaste y por qué lo abandonaste?*

**Semana 3-6**
- Entrega manual a quien pagó. Sin código.