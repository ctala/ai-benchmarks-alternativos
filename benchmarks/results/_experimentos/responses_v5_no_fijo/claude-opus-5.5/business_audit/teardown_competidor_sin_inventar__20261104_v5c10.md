# Claude Opus 5.5 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 3.85 | quality: 4.0
- latency_total: 36.939s | tokens_per_second: 92.8
- input_tokens: 288 | output_tokens: 3429

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

# Teardown del competidor: comunidad de automatización a $39/mes

**Advertencia principal:** con datos públicos solo se puede estimar un **techo** de facturación y un **rango plausible**. La salud real del negocio depende de métricas que no ves desde fuera (churn, % de miembros que pagan, tendencia). Separo cada punto según lo que sabemos y lo que es inferencia.

**Escala de certeza:**
🟢 Alta (dato observado) · 🟡 Media (inferencia razonable) · 🔴 Baja (especulación informada)

---

## 1. Lo que SABEMOS (observado) 🟢

| Dato | Valor |
|---|---|
| Miembros mostrados | 2.400 |
| Precio de lista | $39/mes |
| Frecuencia de posts públicos | 3/semana |
| Audiencia del fundador | 60.000 seguidores (una red) |
| Cursos listados | 12 (sin saber cuántos están completos) |

Todo lo demás es inferencia.

---

## 2. ¿Cuánto factura?

### Techo teórico 🟢 (es aritmética, no realidad)
2.400 × $39 = **~$93.600/mes (~$1,12M/año)**

Esto **casi seguro sobreestima** la cifra real. Supone que todos pagan, todos al precio de lista y todos mensualmente.

### Por qué la cifra real es menor 🟡
- **No todos los "miembros" pagan.** El contador puede incluir cuentas gratuitas o de prueba, invitados, colaboradores, accesos regalados o miembros antiguos con precio congelado. Depende de la plataforma y de cómo configuraron el acceso.
- **El precio promedio suele estar por debajo del de lista.** Puede haber planes anuales con descuento, cupones de lanzamiento o precios "early bird" que no ves.
- **Comisiones.** La plataforma y la pasarela de pago se llevan algo, probablemente entre un 3% y un 10% combinado. Esto es una suposición genérica, no lo sé para su caso.

### Rango plausible 🔴

| Escenario | % que paga | Precio promedio efectivo | MRR bruto |
|---|---|---|---|
| Conservador | 50% | $30 | ~$36.000 |
| Medio | 70% | $34 | ~$57.000 |
| Optimista | 90% | $37 | ~$80.000 |

**Mi estimación:** probablemente **entre $35k y $80k MRR**, con certeza baja. Si tuviera que dar un número, diría $50–60k. Pero los porcentajes de la tabla son supuestos míos, no datos.

---

## 3. ¿Qué tan sano es el negocio?

### Señales positivas 🟡
- **Conversión de audiencia alta, si los miembros pagan.** 2.400 sobre 60.000 seguidores es un 4%. Para un producto de pago, eso es fuerte y sugiere que la audiencia confía en el fundador.
- **Ritmo de contenido constante.** 3 posts/semana en público indica que el negocio sigue activo y con mantenimiento.
- **Catálogo amplio.** 12 cursos dan sensación de "mucho valor por $39", lo que ayuda a vender.

### Señales de riesgo 🟡/🔴
- **Dependencia del fundador** 🟡. Si el crecimiento viene de una sola persona en una sola red, el negocio es frágil ante cambios de algoritmo, burnout o que el fundador se vaya.
- **Posible brecha entre promesa y entrega** 🔴. 12 cursos sin indicar cuántos están completos puede significar contenido a medias. Es la queja típica que alimenta el churn, pero no lo sé.
- **Nicho que se queda obsoleto rápido** 🟡. Las herramientas de automatización cambian mucho. Mantener 12 cursos actualizados es caro, y los desactualizados generan cancelaciones.
- **Modelo mensual** 🟡. Las comunidades a $39/mes suelen tener churn mensual relevante. Sin saber su churn, no puedo decir si crecen o solo reponen bajas.

### Lo que NO sabemos y más importa 🔴
1. **Churn mensual.** Es la métrica que define la salud y es invisible desde fuera.
2. **Tendencia.** ¿Los 2.400 están creciendo, estancados o bajando?
3. **Engagement interno.** ¿La comunidad está viva o es un "cementerio de cursos"?
4. **Canales de adquisición** fuera de la red del fundador.

**Veredicto provisional:** negocio probablemente rentable a esta escala, porque los costos de una comunidad son bajos. Su salud a largo plazo es **indeterminada**, y el mayor riesgo es la dependencia del fundador y el churn.

---

## 4. Cómo verificar (convertir 🔴 en 🟢)

| Acción | Qué revela | Costo |
|---|---|---|
| **Pagar 1 mes como miembro** | Engagement real, estado de los cursos, planes anuales, calidad | $39 (la mejor inteligencia por dólar) |
| Registrar el contador de miembros cada semana | Velocidad de crecimiento o estancamiento | Gratis |
| Revisar Wayback Machine (archive.org) | Contador y precio históricos | Gratis |
| Medir likes y comentarios en sus posts públicos | Nivel de actividad | Gratis |
| Buscar reseñas y menciones ("vale la pena X?") | Quejas recurrentes, posibles causas de churn | Gratis |
| Revisar si el fundador publica cifras | Muchos fundadores comparten MRR | Gratis |
| Registrar sus seguidores en el tiempo | Si su motor de adquisición crece | Gratis |

---

## 5. Cómo competirles

Estas son opciones estratégicas, no recomendaciones cerradas. La mejor depende de tus activos, que no conozco.

**1. Especializarte donde ellos son genéricos.**
"Automatización" es amplio. Puedes ganar en un vertical concreto, como automatización para agencias, e-commerce, inmobiliarias o equipos de ventas, o en una herramienta específica. Un nicho permite cobrar igual o más con menos audiencia.

**2. Profundidad frente a amplitud.**
Si sus 12 cursos resultan superficiales o incompletos (verifícalo pagando), tu ventaja puede ser "3 programas terminados y actualizados" frente a "12 a medias". Vende por resultados, no por volumen.

**3. Formato que ellos no tienen.**
Cohortes en vivo, implementación guiada, plantillas listas para usar o revisión de tus flujos. Son cosas que justifican un precio mayor y reducen el churn.

**4. No competir solo por precio.**
Bajar a $19 contra un competidor con audiencia de 60k suele ser una mala apuesta, porque ellos absorben mejor la guerra. Diferénciate por valor.

**5. Atacar su dependencia del fundador.**
Si ellos dependen de una sola red, tú puedes construir en canales que no dominan: SEO, YouTube, alianzas con herramientas o afiliados.

**6. Capturar a sus insatisfechos.**
Si las reseñas muestran quejas (contenido desactualizado, poca atención), posiciónate exactamente contra eso.

---

## Para afinar el análisis
Dime:
- ¿Qué plataforma usan? El contador de miembros se comporta distinto según cuál sea.
- ¿Tienes audiencia propia? ¿De qué tamaño y en qué canal?
- ¿Tienes un nicho o especialidad dentro de la automatización?
- ¿Estás dispuesto a pagar un mes para ver el interior?

Con eso puedo pasar de opciones genéricas a una estrategia concreta.