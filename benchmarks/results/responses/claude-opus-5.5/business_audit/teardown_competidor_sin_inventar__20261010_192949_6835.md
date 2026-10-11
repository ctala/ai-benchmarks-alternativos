# Claude Opus 5.5 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 3.81 | quality: 4.0
- latency_total: 46.763s | tokens_per_second: 87.8
- input_tokens: 288 | output_tokens: 4108

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

# Teardown: comunidad de automatización ($39/mes, 2.400 miembros)

**Advertencia general:** con datos de página pública **no se puede saber cuánto factura**. Sí se puede acotar un rango y saber qué datos lo afinarían. Etiqueto cada afirmación:

- 🟢 **Dato**: lo viste directamente
- 🟡 **Inferencia razonable**: deducción lógica con supuestos explícitos
- 🔴 **Especulación**: hipótesis plausible sin respaldo directo

---

## 1. Lo que sabemos vs. lo que no

| Aspecto | Lo que viste 🟢 | Lo que NO sabemos |
|---|---|---|
| Miembros | "2.400" en portada | Cuántos pagan, si incluye gratuitos, trials, cortesías o precios antiguos |
| Precio | $39/mes visible | Plan anual, descuentos, cupones de afiliados, precio de entrada histórico |
| Contenido | 12 cursos listados | Cuántos están completos, su calidad, si se actualizan |
| Actividad | 3 posts/semana públicos | Actividad en el área privada, engagement real |
| Audiencia | 60k seguidores del fundador | Engagement, cuánta es audiencia real vs. inflada, otros canales (email, YouTube, ads) |

---

## 2. ¿Cuánto factura?

### Techo teórico 🟢 (aritmética pura)
2.400 × $39 = **$93.600/mes ≈ $1,12M/año**.

Esto es un **techo, no una estimación**. Supone que todos pagan precio completo, mensual y sin descuento, algo casi nunca cierto.

### Por qué el número real es menor 🟡
- **No todos pagan.** Es común que comunidades que empezaron gratis y luego cobraron mantengan a los primeros miembros sin costo. También suele haber accesos de cortesía, colaboradores y trials.
- **Precios heredados.** Muchas comunidades suben el precio con el tiempo y respetan el anterior a los primeros.
- **Descuentos anuales y cupones** bajan el ingreso por miembro.
- **Comisiones** de plataforma y procesador de pago, típicamente un porcentaje de un dígito 🟡.
- **El contador puede estar inflado o desactualizado** según cómo lo calcule la plataforma 🔴.

### Rango estimado 🟡 (certeza baja-media)

| Escenario | Supuesto | Ingreso mensual bruto |
|---|---|---|
| Conservador | ~40% paga, ingreso medio ~$32 | ~$30k/mes |
| Medio | ~65% paga, ingreso medio ~$35 | ~$55k/mes |
| Optimista | ~90% paga, ingreso medio ~$38 | ~$80k/mes |

**Mi lectura: probablemente entre $30k y $80k/mes bruto, con el centro alrededor de $50–55k.** El rango es amplio a propósito: el porcentaje de pagadores es la variable que más mueve el resultado y no la conocemos.

---

## 3. ¿Qué tan sano es el negocio?

### La variable crítica que no vemos: el churn (bajas)
En comunidades de pago mensuales, perder entre 5% y 15% de miembros al mes es frecuente 🟡. Lo que eso implica:

| Churn mensual | Bajas/mes (sobre 2.400) | Altas necesarias solo para no decrecer |
|---|---|---|
| 5% | 120 | 120/mes |
| 10% | 240 | 240/mes |
| 15% | 360 | 360/mes |

### Qué dice eso de su embudo 🟡
Con 10% de churn necesitan ~240 altas al mes. Si todas vinieran de los 60k seguidores, convertirían **~0,4% de su audiencia cada mes, todos los meses**. Esa tasa es exigente de sostener con una sola audiencia. Una de estas tres cosas es probablemente cierta:
1. Tienen otros canales que no ves (email, YouTube, ads, afiliados) 🔴
2. Su churn es bajo porque el producto retiene bien 🔴
3. Están cerca de su techo y estancados o decreciendo 🔴

**No puedo decirte cuál con estos datos.** El experimento de la sección 5 lo resuelve.

### Señales e interpretación

| Señal | Lectura posible | Certeza |
|---|---|---|
| Fundador con 60k seguidores | Fuerte dependencia de una persona. Si él baja el ritmo, el embudo se resiente. | 🟡 |
| 3 posts/semana públicos | Ritmo moderado. Puede que el valor esté dentro, o que haya poco esfuerzo de adquisición. | 🔴 |
| 12 cursos sin estado visible | Posible promesa mayor que la entrega. Si hay cursos a medias, es un punto de insatisfacción. | 🔴 |
| Nicho "automatización" | Las herramientas cambian rápido (sobre todo con IA). El contenido envejece en meses y exige mantenimiento constante. | 🟡 |
| $39/mes | Precio medio. Suficientemente bajo para impulso, suficientemente alto para que se cuestione cada mes. | 🟡 |

### Diagnóstico provisional 🟡
Probablemente es **un negocio rentable para un equipo pequeño** (incluso el escenario conservador es buen ingreso para 1–3 personas). Sus riesgos estructurales serían la **dependencia del fundador**, el **contenido que caduca rápido** y un **churn desconocido**. Sano, pero frágil en esos tres puntos, que son justo donde puedes atacar.

---

## 4. Cómo competirles

**No compitas en su terreno.** Ellos tienen audiencia y prueba social (2.400 miembros). Pelear "otra comunidad de automatización general a precio similar" es pelear con desventaja.

### Ángulos de diferenciación (de más a menos prometedor, según mi criterio)

1. **Nicho vertical.** "Automatización para agencias", "para inmobiliarias", "para ecommerce". Una comunidad general no puede hablarle igual de bien a cada sector, y tú puedes cobrar más por especificidad.
2. **Resultado sobre contenido.** Si ellos venden cursos y comunidad, tú vende implementación: sesiones en vivo construyendo flujos, plantillas listas, revisión de automatizaciones de los miembros. Atacas la debilidad típica de "12 cursos que nadie termina".
3. **Contenido siempre actualizado como promesa central.** Si su contenido envejece (🟡 probable en este nicho), "lo actualizamos cada mes" es un mensaje diferenciador.
4. **Posicionamiento de precio, en una de dos direcciones:**
   - **Premium** ($99–200/mes, menos miembros, más acompañamiento). Necesitas menos clientes y te alejas de la comparación directa.
   - **Entrada barata** para captar a quien no quiere pagar $39. Es más difícil, con menos margen y más volumen necesario.
5. **No depender de una persona.** Si construyes con varios expertos o una comunidad entre pares, ofreces algo estructuralmente distinto.

**Lo que no recomiendo:** bajar precio en la misma propuesta. Es fácil de igualar y erosiona tu margen sin crear ventaja.

---

## 5. Cómo convertir inferencias en datos (barato y rápido)

Esto vale más que cualquier estimación mía:

1. **Únete un mes ($39).** Es la inteligencia competitiva más barata que existe. Mira cuántos cursos están completos, la actividad real del feed privado, cuántos miembros participan activamente y de qué se quejan.
2. **Registra el contador de miembros cada semana** durante 4–8 semanas. El crecimiento neto te dice si están creciendo, estancados o decreciendo. Es el mejor indicador de salud disponible desde fuera.
3. **Busca su página en Wayback Machine** (web.archive.org). Puedes ver el contador y el precio históricos y estimar ritmo de crecimiento y subidas de precio.
4. **Mide el engagement del fundador.** Mira likes y comentarios por post frente a sus 60k seguidores. Un 1–3% sugiere audiencia real; muy por debajo, audiencia de menor calidad.
5. **Busca códigos de descuento o afiliados.** Busca "[nombre] descuento" o "código". Si hay muchos, el ingreso medio por miembro es menor que $39.
6. **Habla con miembros o exmiembros.** Busca reseñas y menciones. Las razones por las que la gente se va son tu mapa de oportunidades.

---

## Resumen

- **Facturación:** probablemente $30k–80k/mes bruto, con el centro en ~$50k. 🟡 Certeza baja-media; el techo de $93,6k es casi seguro una sobreestimación.
- **Salud:** probablemente rentable pero frágil por dependencia del fundador, contenido perecedero y churn desconocido. 🟡
- **Cómo competir:** no de frente. Nicho vertical, foco en implementación y resultado, y precio que no invite a la comparación directa.
- **Siguiente paso:** pagar un mes y registrar el contador semanalmente. En 30 días tendrás datos reales en lugar de mis supuestos.