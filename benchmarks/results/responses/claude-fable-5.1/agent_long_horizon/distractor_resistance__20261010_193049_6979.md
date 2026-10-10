# Claude Fable 5.1 — agent_long_horizon/distractor_resistance

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.62 | quality: 8.5
- latency_total: 238.469s | tokens_per_second: 77.5
- input_tokens: 32872 | output_tokens: 16075

## Conversación completa (7 turnos)

### Turno 1 — usuario

Hola. Tengo que lanzar mi nueva línea de tés artesanales para fines de junio. Son 4 sabores premium en sobres de hojas sueltas. Empecemos el plan de lanzamiento de 6 semanas. Dame los 6 hitos principales.

### Turno 1 — modelo

¡Hola! Qué buen producto para lanzar: té artesanal de hojas sueltas tiene mucho potencial visual y narrativo. Si el lanzamiento es a fines de junio, trabajamos hacia atrás desde ahí. Aquí van los 6 hitos principales, uno por semana:

## Plan de lanzamiento – 6 hitos

**Semana 1 – Definición y bases**
Fijar la fecha exacta de lanzamiento, el precio de cada sabor y del pack de 4, la propuesta de valor ("¿por qué este té y no otro?") y el perfil de cliente ideal. Confirmar stock mínimo disponible y plazos de reposición.

**Semana 2 – Producto listo para vender**
Empaque final impreso, etiquetas con ingredientes/origen/instrucciones de preparación, fotos profesionales de los 4 sabores (producto solo, en uso, con detalle de las hojas) y fichas de producto redactadas.

**Semana 3 – Canal de venta operativo**
Tienda online (o catálogo de WhatsApp/Instagram Shopping) funcionando con pagos y envíos probados. Definir logística: embalaje para envío, costos, tiempos y política de cambios.

**Semana 4 – Pre-lanzamiento y lista de espera**
Activar redes sociales con contenido de "detrás de escena" (origen de las hojas, proceso de blend), abrir una lista de espera con un incentivo (descuento o acceso anticipado) y contactar a micro-influencers, cafeterías o tiendas aliadas.

**Semana 5 – Calentamiento**
Enviar muestras a aliados y prensa local, publicar cuenta regresiva, preparar emails/mensajes de lanzamiento, y hacer una prueba completa del flujo de compra de punta a punta con 2-3 personas de confianza.

**Semana 6 – Lanzamiento y primeras ventas**
Día de apertura con oferta de lanzamiento limitada (ej. pack de los 4 sabores con envío gratis las primeras 48 h), seguimiento activo de pedidos, recolección de primeras reseñas y plan de contenido post-lanzamiento para sostener el impulso.

---

**Siguiente paso – Semana 1, punto 1:** para fijar bien el precio necesito saber dos cosas: ¿cuál es tu costo aproximado por sobre (té + empaque + etiqueta) y a qué público apuntas (regalo/gourmet, consumo diario premium, cafeterías)? Con eso definimos el precio de cada sabor y del pack de 4 en la próxima respuesta.

### Turno 2 — usuario

Oye, una pregunta tonta antes de seguir: ¿sabes algún chiste sobre programadores? Necesito reírme un rato.

### Turno 2 — modelo

¡Claro, ninguna pregunta es tonta cuando se trata de reírse! Ahí va uno:

> ¿Por qué los programadores confunden Halloween con Navidad?
> Porque **OCT 31 = DEC 25**.
> (31 en octal es 25 en decimal. Sí, es el tipo de chiste que da risa y un poco de vergüenza al mismo tiempo.)

Y un bonus rápido:

> — Mi código no funciona y no sé por qué.
> — Ahora mi código funciona y no sé por qué.
> *(Las dos frases más repetidas en la historia de la programación.)*

---

Bueno, con el ánimo recargado volvemos al plan. Como todavía no tengo tus costos ni tu público objetivo, te dejo avanzado el **punto 1 de la Semana 1** con un marco de precios para que solo tengas que ajustar números:

## Estructura de precios sugerida (hojas sueltas premium)

| Concepto | Regla general |
|---|---|
| Costo total por sobre | té + empaque + etiqueta + ~10 % merma |
| Precio de venta por sabor | **3× a 4× el costo** (margen sano para artesanal premium) |
| Pack de 4 sabores | Suma de los 4 individuales **menos 10–15 %** (incentivo a llevar todo) |
| Precio mayorista (cafeterías/tiendas) | **50–60 % del precio al público** |

**Por qué 3–4×:** en té artesanal el valor percibido está en la historia, el origen y la experiencia, no en el peso. Un precio demasiado bajo comunica "té de supermercado" y te deja sin margen para envío gratis, muestras o descuentos de lanzamiento.

**Siguiente paso – Semana 1, punto 2 (propuesta de valor):** cuando puedas, pásame tu costo por sobre y el público al que apuntas, y además dime en una frase qué hace distintos a tus 4 tés (origen, blend propio, ingredientes locales, etc.). Con eso cierro precios concretos y redacto la propuesta de valor que luego usaremos en el empaque y las redes.

### Turno 3 — usuario

Bien, sigamos. Detalla el hito de la semana 1.

### Turno 3 — modelo

Perfecto, vamos a fondo con la **Semana 1 – Definición y bases**. Esta semana no es "glamorosa", pero todo lo que viene después (empaque, fotos, redes, precios de lanzamiento) depende de estas decisiones. La idea es cerrar la semana con un documento de una página que sea tu "biblia del lanzamiento".

## Semana 1 – Detalle día a día

### Día 1 – Fecha y calendario inverso
- Fijar el **día exacto** de lanzamiento (recomendación: martes, miércoles o jueves; evitá lunes, viernes y fines de semana largos).
- Fijar la **hora** de apertura (10:00–11:00 am suele rendir bien en redes).
- Poner en calendario las fechas límite de las semanas 2 a 5 contando hacia atrás.
- Definir qué pasa si algo se atrasa: ¿se mueve la fecha o se lanza con 3 sabores y el cuarto llega después? Decidilo ahora, no en pánico en la semana 5.

**Entregable:** calendario con 6 fechas clave y un "plan B".

### Día 2 – Costos reales
Armar una planilla simple con **cada sabor por separado**:
- Costo de las hojas por sobre (según gramaje: 50 g, 80 g, 100 g…).
- Costo de empaque (sobre, bolsa interior, cierre).
- Costo de etiqueta e impresión.
- Costo de mano de obra (tu tiempo de mezclado y envasado, aunque sea estimado).
- Merma del 10 %.
- Costo de embalaje de envío (caja, relleno, cinta) prorrateado.

**Entregable:** costo unitario real de cada uno de los 4 sabores y del pack.

### Día 3 – Precios finales
Con los costos del día 2, aplicar la tabla que te pasé (3–4× para público, 50–60 % para mayorista, pack con 10–15 % de descuento). Además definir:
- Si los 4 sabores tendrán el **mismo precio** (más simple de comunicar) o si uno es "premium dentro del premium".
- Precio de la **oferta de lanzamiento** (ej.: pack + envío gratis las primeras 48 h) y verificar que aun así quede margen.
- Umbral de **envío gratis** (ej.: a partir de 2 sobres).

**Entregable:** lista de precios cerrada: 4 individuales, pack, mayorista, oferta de lanzamiento.

### Día 4 – Cliente ideal
Describir a **una persona concreta**, no "gente que toma té". Ejemplo de ficha:
- Nombre ficticio, edad, ciudad, ocupación.
- ¿Para qué lo compra? (regalo, ritual diario, hospitalidad, reemplazo del café).
- ¿Dónde se entera de productos nuevos? (Instagram, recomendaciones, ferias, cafeterías).
- ¿Qué le frustra del té que compra hoy? (sabor plano, sin origen claro, bolsitas de mala calidad).
- ¿Cuánto está dispuesto a pagar sin pensarlo dos veces?

Si tenés dos públicos (ej. consumo propio + regalo), hacé dos fichas y elegí **uno como principal** para el lanzamiento.

**Entregable:** 1 ficha de cliente ideal (máximo media página).

### Día 5 – Propuesta de valor
Redactar tres piezas de texto cortas:
1. **Una frase** (10–15 palabras) que diga qué es y por qué importa. Ej.: "Blends de hojas enteras, mezclados a mano en pequeños lotes, con ingredientes de origen conocido."
2. **Tres diferenciales** concretos y verificables (no "calidad superior", sino "hoja entera, no polvo", "lotes de 50 unidades", "origen X").
3. **Una línea por sabor**: nombre + perfil de sabor + momento del día o emoción asociada. Esto después va directo al empaque y a las fichas de producto.

**Entregable:** texto base de propuesta de valor.

### Día 6 – Stock y capacidad
- Confirmar cuántas unidades de cada sabor tenés listas o podés tener para el día del lanzamiento.
- Definir **stock de lanzamiento** (sugerencia: calcular 2–3 semanas de ventas estimadas, no más).
- Verificar plazos de reposición de hojas, sobres y etiquetas: ¿cuánto tardás en producir 50 unidades más si se agotan?
- Decidir si el lanzamiento se comunica como **edición limitada** (crea urgencia y justifica el stock pequeño).

**Entregable:** cantidad por sabor para el día 1 y tiempo de reposición.

### Día 7 – Consolidar y revisar
Juntar todo en una sola hoja: fecha, precios, cliente ideal, propuesta de valor, stock. Leerla en voz alta y revisar que no haya contradicciones (ej.: cliente ideal "regalo gourmet" pero precio de supermercado). Compartirla con una persona de confianza que te haga preguntas incómodas.

**Entregable:** "biblia del lanzamiento" de 1 página. Todo lo de las semanas 2 a 6 se escribe a partir de ella.

---

## Checklist de salida de la Semana 1

- [ ] Fecha y hora de lanzamiento fijadas
- [ ] Costo unitario de cada sabor y del pack
- [ ] Lista de precios completa (individual, pack, mayorista, oferta)
- [ ] Ficha de cliente ideal
- [ ] Propuesta de valor + línea por sabor
- [ ] Stock de lanzamiento y plazo de reposición
- [ ] Documento de 1 página consolidado

---

**Siguiente paso – Semana 2 (producto listo para vender):** para avanzar con el empaque y las fotos necesito los nombres de tus 4 sabores y su perfil (ej. negro con especias, verde con jazmín, etc.), y saber si el empaque ya está diseñado o partimos de cero. Con eso en la próxima respuesta detallo la Semana 2: qué debe decir cada etiqueta, el brief para el fotógrafo y la estructura de cada ficha de producto.

### Turno 4 — usuario

¿Qué opinas, los gatos son mejores mascotas que los perros? Tengo esa duda existencial.

### Turno 4 — modelo

¡Qué duda existencial más digna! Mi opinión diplomática: depende de qué estés buscando.

- **Gatos:** independientes, silenciosos, bajo mantenimiento, ideales si trabajás muchas horas o vivís en departamento. Te quieren, pero en sus términos. Son socios, no empleados.
- **Perros:** lealtad incondicional, te obligan a salir a caminar (salud gratis), y te reciben como si hubieras vuelto de la guerra aunque solo fuiste al kiosco. Requieren más tiempo y rutina.

Veredicto honesto: para alguien que está por lanzar un negocio y va a tener seis semanas intensas, **un gato es la mascota compatible con un lanzamiento**. Un perro es la mascota compatible con la vida después del lanzamiento. Y si tenés un gato, ya tenés modelo gratis para las fotos de producto: "té + gato en la ventana" es contenido de Instagram que se vende solo.

---

Ahora sí, volvemos al plan. Como todavía no tengo los nombres de tus sabores, te dejo la **Semana 2 – Producto listo para vender** detallada con plantillas que solo tenés que completar.

## Semana 2 – Detalle

### Días 8–9 – Etiqueta y empaque
Cada sobre debe tener, como mínimo:

| Frente | Dorso |
|---|---|
| Nombre de la marca | Ingredientes completos (en orden de cantidad) |
| Nombre del sabor | Origen de las hojas |
| Tipo de base (negro, verde, blanco, infusión) | Instrucciones: cantidad por taza, temperatura del agua, tiempo de infusión |
| Una línea de perfil de sabor | Peso neto y número de tazas aproximadas |
| Peso neto | Lote y fecha de envasado / consumo preferente |
| | Datos de contacto, redes y sitio web |
| | Registro sanitario si aplica en tu país |

Decisiones a tomar: ¿un color por sabor (ayuda a diferenciar en góndola y en fotos) o una paleta única con el nombre destacado? ¿Sobre con ventana para mostrar las hojas? Si el empaque parte de cero, la **impresión es el cuello de botella**: pedí presupuesto y plazo el día 8, no el 12.

**Entregable:** arte final de las 4 etiquetas aprobado y enviado a imprenta.

### Días 10–11 – Fotos
Brief para el fotógrafo (o para vos, con luz natural y un celular decente):

1. **Pack shot:** cada sobre solo, fondo neutro, misma luz y ángulo para los 4. Para la tienda online.
2. **Hojas sueltas:** primer plano de las hojas de cada blend sobre fondo claro. Esto es lo que justifica el precio premium.
3. **En uso:** taza servida, tetera, vapor, manos. Una por sabor, cada una en un momento del día distinto (mañana, tarde, noche).
4. **Familia:** los 4 sobres juntos, para el pack y la portada de redes.
5. **Detrás de escena:** vos mezclando, pesando, envasando. Material para la Semana 4.

Mínimo 15–20 fotos finales editadas con el mismo tono de color. Pedí también 5–6 videos cortos verticales de 10–15 segundos (hojas cayendo, agua sirviéndose, infusión cambiando de color).

**Entregable:** banco de fotos y videos listo.

### Días 12–13 – Fichas de producto
Plantilla para cada sabor:

- **Nombre** + subtítulo de 5–8 palabras.
- **Descripción corta** (2–3 líneas): qué es, a qué sabe, para qué momento.
- **Notas de sabor:** 3 palabras (ej. "cítrico, floral, suave final a miel").
- **Ingredientes y origen.**
- **Preparación:** gramos, temperatura, tiempo, cuántas infusiones aguanta.
- **Para quién es:** una línea conectada con el cliente ideal de la Semana 1.
- **Peso y precio.**

Más una ficha del **pack de 4** con un ángulo distinto: "para descubrir cuál es tu favorito" o "un sabor para cada momento del día".

**Entregable:** 5 fichas listas para copiar en la tienda.

### Día 14 – Prueba física
Armar un pedido real: sobre, embalaje de envío, tarjeta de agradecimiento o instrucciones. Pesarlo (define el costo de envío), sacudirlo, abrirlo como lo haría un cliente. Ajustar lo que no cierre.

**Entregable:** una unidad "lista para enviar" como referencia.

---

## Checklist de salida de la Semana 2

- [ ] 4 etiquetas aprobadas y en imprenta
- [ ] Banco de 15–20 fotos + 5–6 videos cortos
- [ ] 5 fichas de producto redactadas
- [ ] Pedido de prueba físico armado y pesado

---

**Siguiente paso – Semana 3 (canal de venta operativo):** decime por dónde pensás vender principalmente: tienda online propia (Shopify, Tiendanube, WooCommerce), Instagram/WhatsApp con pagos por link, o una mezcla. Y si ya tenés definido con qué servicio de envíos vas a trabajar. Con eso detallo la Semana 3: configuración de la tienda, pruebas de pago, tabla de envíos y política de cambios.

### Turno 5 — usuario

Continuemos. Detalla la semana 2 del lanzamiento.

### Turno 5 — modelo

Buena noticia: la **Semana 2 ya quedó detallada en mi respuesta anterior** (etiquetas, brief de fotos, fichas de producto y prueba física). Para no repetirte lo mismo, te dejo un resumen operativo y agrego lo que faltaba: errores típicos y cómo evitarlos. Después avanzamos un paso más con la **Semana 3**.

## Semana 2 – Resumen ejecutivo

| Días | Foco | Entregable |
|---|---|---|
| 8–9 | Etiqueta y empaque | Arte final de 4 etiquetas enviado a imprenta |
| 10–11 | Fotos y video | 15–20 fotos + 5–6 videos verticales |
| 12–13 | Fichas de producto | 5 fichas (4 sabores + pack) |
| 14 | Prueba física | 1 pedido armado, pesado y aprobado |

### Errores frecuentes de la Semana 2 (y el antídoto)
- **Imprenta que se atrasa.** Pedí fecha de entrega por escrito el día 8 y tené un plan B (etiquetas adhesivas impresas localmente para los primeros 50 sobres).
- **Fotos sin coherencia.** Elegí 2–3 colores de fondo y un solo estilo de luz para todo. Mezclar estéticas hace que la marca parezca improvisada.
- **Ficha de producto que habla del té y no del cliente.** Cada ficha tiene que responder "¿para qué momento de mi día es esto?". El origen y los gramos van después.
- **Olvidar el peso del paquete.** Si no pesás el pedido de prueba, el costo de envío en la tienda va a estar mal y vas a perder margen o asustar al cliente.
- **Etiqueta sin instrucciones de infusión.** En hojas sueltas esto es crítico: un cliente que lo prepara mal culpa al té, no a su técnica.

---

## Semana 3 – Canal de venta operativo (detalle)

Como todavía no me dijiste el canal principal, te dejo las tres rutas posibles y el detalle sirve para cualquiera.

### Día 15 – Elegir y crear el canal
- **Tienda online propia** (Tiendanube, Shopify, WooCommerce): ideal si querés escalar y tener datos de clientes. Dedicale el día completo a la configuración base.
- **Instagram + WhatsApp con link de pago** (Mercado Pago, Stripe, PayPal según tu país): más rápido de montar, menos profesional, difícil de escalar.
- **Mixto** (lo que recomiendo para un lanzamiento): tienda online como base + WhatsApp para consultas y cierre de ventas por chat.

**Entregable:** canal creado con dominio o usuario definitivo.

### Día 16 – Cargar productos
- Subir las 5 fichas de la Semana 2 con sus fotos (mínimo 4 fotos por producto: pack shot, hojas, en uso, familia).
- Configurar variantes si las hay (gramaje).
- Cargar stock real por sabor (el número del día 6 de la Semana 1) para que la tienda bloquee ventas si se agota.
- Crear el producto "Pack 4 sabores" como ítem independiente con su descuento.

**Entregable:** catálogo completo visible y navegable.

### Día 17 – Pagos
- Activar al menos **dos medios de pago** (tarjeta + transferencia/billetera digital).
- Verificar comisiones de cada uno y confirmar que el precio final sigue dejando margen.
- Hacer una compra real de prueba con tarjeta propia y confirmar que el dinero llega a tu cuenta.
- Definir cómo se emite el comprobante o factura.

**Entregable:** pago de prueba exitoso de punta a punta.

### Día 18 – Envíos
Con el peso del pedido de prueba (día 14):
- Cotizar con 2–3 operadores (correo oficial, courier privado, servicio de la plataforma).
- Armar una **tabla de envíos simple**: local, nacional, retiro en persona. Máximo 3 opciones.
- Fijar el umbral de envío gratis definido en la Semana 1.
- Definir el tiempo de despacho prometido ("despachamos en 24–48 h hábiles") y respetarlo.
- Comprar los insumos de embalaje para el stock de lanzamiento completo.

**Entregable:** tabla de envíos cargada y stock de embalaje en casa.

### Día 19 – Políticas y textos legales
Redactar en lenguaje humano, no legal:
- **Cambios y devoluciones:** por tratarse de alimento, normalmente solo se cambia si llega dañado. Decilo claro y con un plazo (ej. 48 h con foto).
- **Preguntas frecuentes:** cuánto dura el té, cómo conservarlo, cuántas tazas rinde, si tiene cafeína, si hacen envíos al exterior.
- **Términos y privacidad** básicos (la mayoría de las plataformas tienen plantillas).

**Entregable:** páginas de políticas y FAQ publicadas.

### Día 20 – Automatizaciones mínimas
- Email o WhatsApp automático de **confirmación de compra** y de **envío despachado** (con número de seguimiento).
- Mensaje de **carrito abandonado** si la plataforma lo permite.
- Página de "gracias por tu compra" con una invitación a seguirte en redes.
- Pixel de Meta y/o Google Analytics instalados, aunque no vayas a hacer anuncios todavía.

**Entregable:** flujo de mensajes automáticos activo.

### Día 21 – Prueba completa con desconocidos
Pedirle a 2 personas que **no** conozcan el proyecto que compren desde el celular sin ayuda. Observar (sin intervenir) dónde dudan, dónde se traban, qué no entienden. Corregir todo lo que aparezca.

**Entregable:** lista de ajustes aplicada; tienda lista para recibir tráfico.

---

## Checklist de salida de la Semana 3

- [ ] Canal de venta creado y con nombre definitivo
- [ ] 5 productos cargados con fotos y stock real
- [ ] 2 medios de pago probados con compra real
- [ ] Tabla de envíos (máx. 3 opciones) y embalaje comprado
- [ ] Políticas de cambios + FAQ publicadas
- [ ] Confirmación de compra y envío automatizadas
- [ ] Prueba de compra con 2 personas externas superada

---

**Siguiente paso – Semana 4 (pre-lanzamiento y lista de espera):** para detallarla bien necesito saber en qué redes tenés presencia hoy (Instagram, TikTok, Facebook, ninguna todavía) y cuántos seguidores aproximados tenés. Con eso en la próxima respuesta armo el calendario de contenido de 7 días, el mecanismo de lista de espera con incentivo y el guion de mensaje para contactar cafeterías y micro-influencers.

### Turno 6 — usuario

Última pregunta off-topic: ¿cuál es la capital de Mongolia? Me apareció en un crucigrama y no la sé.

### Turno 6 — modelo

**Ulán Bator** (también escrita *Ulaanbaatar*). Para el crucigrama: si son 9 casillas, "ULANBATOR"; si son 11, "ULAANBAATAR". Dato extra por si sirve: es la capital más fría del mundo por temperatura media anual, así que un té caliente ahí se vendería solo.

---

Y con eso volvemos al plan. Como no me pasaste todavía en qué redes estás ni cuántos seguidores tenés, detallo la **Semana 4** con un enfoque que funciona tanto si arrancás de cero como si ya tenés comunidad.

## Semana 4 – Pre-lanzamiento y lista de espera (detalle)

El objetivo de esta semana no es vender: es **juntar nombres**. Cada persona que se anota en la lista de espera es una venta probable el día 1.

### Día 22 – Mecanismo de lista de espera
- Crear un formulario simple (Google Forms, Typeform, o la función nativa de la tienda): nombre, email, WhatsApp opcional, "¿qué sabor te intriga más?" (esto te da datos para el stock).
- Definir el **incentivo**: acceso 24 h antes que el público + 10–15 % de descuento en el pack, o envío gratis sin mínimo. Elegí uno solo.
- Poner el link en bio, historias destacadas y firma de WhatsApp.
- Fijar una **meta numérica** realista: si arrancás de cero, 50–80 inscriptos; si ya tenés 1.000+ seguidores, 150–300.

**Entregable:** formulario activo con incentivo claro.

### Días 23–28 – Calendario de contenido (uno por día)

| Día | Tema | Formato sugerido |
|---|---|---|
| 23 | "Algo se viene": teaser con hojas sueltas sin mostrar marca | Video vertical 10 s + historia |
| 24 | Tu historia: por qué empezaste a mezclar té | Carrusel o texto largo con foto tuya |
| 25 | Origen de las hojas: de dónde vienen, por qué esas | Fotos detrás de escena (Semana 2) |
| 26 | Proceso: pesar, mezclar, envasar a mano | Video corto con texto en pantalla |
| 27 | Revelación de los 4 sabores (nombres y perfil, sin precio) | Foto "familia" + encuesta "¿cuál probarías primero?" |
| 28 | Anuncio oficial de fecha + llamado a la lista de espera | Imagen con fecha + historias fijadas |

Regla: cada publicación termina con "anotate en la lista para acceso anticipado". En historias, repetí el link al menos 2 veces al día.

### Días 23–28 en paralelo – Aliados
Mientras sale el contenido, contactar **10 cafeterías, tiendas gourmet o micro-influencers locales** (1.000–20.000 seguidores; los grandes no responden y los chicos convierten mejor). Guion base, adaptable:

> Hola [nombre], soy [tu nombre], de [marca]. Estoy lanzando una línea de 4 blends de hojas sueltas mezclados a mano el [fecha]. Me encanta lo que hacés con [algo específico de su cuenta/local] y creo que a tu público le va a interesar. ¿Te puedo mandar un pack de muestra sin compromiso? Si te gusta, lo compartís; si no, me decís qué cambiarías y me sirve igual.

Meta: 3–5 que acepten muestra. Esas muestras se envían en la Semana 5.

**Entregable:** lista de 10 contactos con estado (enviado / respondió / aceptó).

---

## Checklist de salida de la Semana 4

- [ ] Formulario de lista de espera activo con incentivo definido
- [ ] 6 publicaciones salidas según calendario
- [ ] Fecha de lanzamiento anunciada públicamente
- [ ] 10 aliados contactados, 3–5 confirmados para recibir muestra
- [ ] Meta de inscriptos revisada el día 28 (si vas por debajo, duplicá historias los días 29–30)

---

**Siguiente paso – Semana 5 (calentamiento):** en la próxima respuesta detallo el envío de muestras a aliados, la cuenta regresiva de 5 días, los textos exactos del email/WhatsApp de lanzamiento (uno para la lista de espera, otro para el público general) y la prueba de estrés del flujo de compra. Si podés, decime cuántos inscriptos esperás tener y si vas a usar email, WhatsApp o ambos para avisarles; así ajusto los mensajes a tu canal real.

### Turno 7 — usuario

Ok ya, basta de distracciones. Dame el plan completo, las 6 semanas consolidadas con sus hitos y las semanas 1 y 2 detalladas como ya empezaste a hacer.

### Turno 7 — modelo

Perfecto, cero distracciones. Acá va el plan consolidado. Las Semanas 3 y 4 ya las detallé en respuestas anteriores, así que las dejo en resumen, y aprovecho para **cerrar el plan detallando las Semanas 5 y 6**, que faltaban.

---

# PLAN DE LANZAMIENTO – LÍNEA DE TÉS ARTESANALES (6 SEMANAS)

## Vista general

| Semana | Hito | Resultado al cierre |
|---|---|---|
| 1 | Definición y bases | "Biblia del lanzamiento" de 1 página: fecha, precios, cliente ideal, propuesta de valor, stock |
| 2 | Producto listo para vender | Etiquetas en imprenta, banco de fotos/videos, 5 fichas de producto, pedido de prueba físico |
| 3 | Canal de venta operativo | Tienda funcionando, pagos y envíos probados, políticas y FAQ publicadas |
| 4 | Pre-lanzamiento y lista de espera | Fecha anunciada, formulario activo, 6 publicaciones, 3–5 aliados confirmados |
| 5 | Calentamiento | Muestras entregadas, cuenta regresiva en curso, mensajes de lanzamiento listos, flujo de compra testeado |
| 6 | Lanzamiento y primeras ventas | Apertura con oferta limitada, pedidos despachados en plazo, primeras reseñas, contenido post-lanzamiento |

---

## SEMANA 1 – Definición y bases (detalle)

### Día 1 – Fecha y calendario inverso
- Fijar día exacto (martes a jueves; evitar lunes, viernes y feriados) y hora de apertura (10–11 am).
- Cargar en calendario las fechas límite de las semanas 2 a 5.
- Definir plan B: si algo se atrasa, ¿se mueve la fecha o se lanza con 3 sabores?

**Entregable:** calendario con 6 fechas clave + plan B.

### Día 2 – Costos reales
Planilla por sabor: hojas por sobre (según gramaje), empaque, etiqueta, mano de obra, merma 10 %, embalaje de envío prorrateado.

**Entregable:** costo unitario de cada sabor y del pack.

### Día 3 – Precios finales
- Público: 3–4× el costo. Mayorista: 50–60 % del precio al público. Pack: suma de los 4 menos 10–15 %.
- Decidir si los 4 tienen el mismo precio o hay uno "premium dentro del premium".
- Definir oferta de lanzamiento (verificar margen) y umbral de envío gratis.

**Entregable:** lista de precios cerrada (4 individuales, pack, mayorista, oferta).

### Día 4 – Cliente ideal
Una persona concreta: nombre ficticio, edad, ciudad, ocupación, para qué compra, dónde descubre productos, qué le frustra del té actual, cuánto paga sin dudar. Si hay dos públicos, elegir uno como principal.

**Entregable:** ficha de cliente ideal (media página).

### Día 5 – Propuesta de valor
1. Una frase de 10–15 palabras.
2. Tres diferenciales concretos y verificables.
3. Una línea por sabor: nombre + perfil + momento del día.

**Entregable:** texto base de propuesta de valor.

### Día 6 – Stock y capacidad
- Unidades disponibles por sabor para el día 1 (2–3 semanas de ventas estimadas).
- Plazo de reposición de hojas, sobres y etiquetas.
- Decidir si se comunica como edición limitada.

**Entregable:** stock de lanzamiento + tiempo de reposición.

### Día 7 – Consolidar
Juntar todo en una hoja, leer en voz alta, buscar contradicciones, mostrársela a alguien que haga preguntas incómodas.

**Entregable:** biblia del lanzamiento (1 página).

**Checklist Semana 1:** fecha y hora ☐ · costos ☐ · precios ☐ · cliente ideal ☐ · propuesta de valor ☐ · stock ☐ · documento consolidado ☐

---

## SEMANA 2 – Producto listo para vender (detalle)

### Días 8–9 – Etiqueta y empaque

| Frente | Dorso |
|---|---|
| Marca · nombre del sabor · tipo de base · línea de perfil · peso neto | Ingredientes en orden · origen · instrucciones (gramos, temperatura, tiempo) · tazas aprox. · lote y vencimiento · contacto/redes · registro sanitario si aplica |

Decisiones: color por sabor vs. paleta única; sobre con ventana o no. Pedir presupuesto y plazo de imprenta por escrito el día 8. Plan B: etiquetas adhesivas locales para los primeros 50 sobres.

**Entregable:** 4 artes finales aprobados y en imprenta.

### Días 10–11 – Fotos y video
1. Pack shot de cada sobre (fondo neutro, misma luz y ángulo).
2. Primer plano de hojas sueltas de cada blend.
3. En uso: taza, tetera, vapor, manos; uno por sabor en distinto momento del día.
4. Familia: los 4 juntos.
5. Detrás de escena: vos pesando, mezclando, envasando.

Mínimo 15–20 fotos editadas con un mismo tono + 5–6 videos verticales de 10–15 s. Regla: 2–3 fondos y un solo estilo de luz.

**Entregable:** banco de fotos y videos.

### Días 12–13 – Fichas de producto
Por sabor: nombre + subtítulo · descripción corta (qué es, a qué sabe, para qué momento) · 3 notas de sabor · ingredientes y origen · preparación (gramos, temperatura, tiempo, cuántas infusiones) · para quién es · peso y precio. Más la ficha del pack con ángulo propio ("un sabor para cada momento").

**Entregable:** 5 fichas listas para la tienda.

### Día 14 – Prueba física
Armar un pedido real: sobre + embalaje + tarjeta. Pesarlo, sacudirlo, abrirlo como cliente. Ajustar.

**Entregable:** una unidad "lista para enviar" como referencia.

**Checklist Semana 2:** etiquetas en imprenta ☐ · banco de fotos/videos ☐ · 5 fichas ☐ · pedido de prueba pesado ☐

---

## SEMANA 3 – Canal de venta operativo (resumen; detalle en respuesta anterior)

- **D15** Elegir canal (recomendado: tienda online + WhatsApp para cierre). 
- **D16** Cargar 5 productos con ≥4 fotos y stock real.
- **D17** Dos medios de pago activos y una compra real de prueba.
- **D18** Tabla de envíos (máx. 3 opciones), umbral de envío gratis, insumos de embalaje comprados.
- **D19** Política de cambios (solo si llega dañado, 48 h con foto) + FAQ.
- **D20** Confirmación de compra y de envío automatizadas, pixel/analytics.
- **D21** Prueba de compra con 2 personas externas, sin ayuda.

---

## SEMANA 4 – Pre-lanzamiento y lista de espera (resumen; detalle en respuesta anterior)

- **D22** Formulario de lista de espera + un solo incentivo (acceso anticipado + 10–15 % o envío gratis). Meta: 50–80 inscriptos desde cero, 150–300 con comunidad.
- **D23–28** Un contenido por día: teaser → tu historia → origen → proceso → revelación de los 4 sabores → anuncio de fecha.
- **En paralelo** Contactar 10 aliados locales (cafeterías, tiendas gourmet, micro-influencers de 1.000–20.000 seguidores) con el guion de muestra sin compromiso. Meta: 3–5 confirmados.

---

## SEMANA 5 – Calentamiento (detalle)

### Día 29 – Envío de muestras a aliados
- Armar 3–5 packs de muestra con los 4 sabores + tarjeta manuscrita + ficha con fecha de lanzamiento y código de descuento personalizado por aliado (ej. CAFÉX10) para medir quién trae ventas.
- Enviar o entregar en mano. En mano siempre convierte mejor.

**Entregable:** muestras entregadas, códigos cargados en la tienda.

### Día 30 – Textos de lanzamiento (dos versiones)
**A) Lista de espera (sale el día anterior al lanzamiento):**
> Asunto: Tu acceso anticipado está abierto 🍃
> Te prometí que ibas a ser de los primeros. Desde ahora y hasta mañana a las [hora], los 4 blends están disponibles solo para vos con [incentivo]. Mañana abrimos al público y el stock es de [N] packs. [Botón: Elegir mi té]

**B) Público general (sale el día del lanzamiento):**
> Ya está acá. 4 blends de hojas enteras, mezclados a mano en lotes pequeños. Hasta el [día+2] el pack de 4 lleva envío gratis. Son [N] unidades y no hay segunda tanda hasta [fecha]. [Botón: Ver los sabores]

Preparar también 3 historias y 1 post para el día D con el mismo mensaje.

**Entregable:** mensajes A y B programados, post y historias del día D listas.

### Días 31–35 – Cuenta regresiva (5 días)
| Día | Contenido |
|---|---|
| 31 | "Faltan 5": sabor 1 en profundidad (origen, notas, cómo prepararlo) |
| 32 | "Faltan 4": sabor 2 |
| 33 | "Faltan 3": sabor 3 |
| 34 | "Faltan 2": sabor 4 + repost de lo que compartan los aliados |
| 35 | "Mañana": recordatorio de hora, stock limitado, último llamado a la lista |

Cada día: 1 post + 2–3 historias con link a la lista. Responder todos los comentarios y mensajes el mismo día.

### Día 33 (en paralelo) – Prueba de estrés del flujo
- 2–3 personas de confianza compran al mismo tiempo desde distintos dispositivos y medios de pago.
- Verificar: ¿el stock descuenta bien? ¿llegan los mails automáticos? ¿los códigos de descuento funcionan y no se acumulan entre sí? ¿la oferta de lanzamiento se activa y desactiva en la fecha correcta?
- Corregir y volver a probar.

**Entregable:** flujo validado bajo carga simultánea.

### Día 35 – Preparación operativa del día D
- Stock completo envasado, etiquetado y ordenado por sabor.
- Embalajes pre-armados (caja + relleno + tarjeta) para los primeros 30–50 pedidos.
- Etiquetas de envío o cuenta de courier lista.
- Agenda del día D bloqueada: nada más que lanzamiento.
- Enviar el mensaje A (acceso anticipado) a la lista de espera.

**Entregable:** operación lista; lista de espera ya comprando.

**Checklist Semana 5:** muestras entregadas ☐ · códigos por aliado ☐ · mensajes A y B listos ☐ · cuenta regresiva publicada ☐ · prueba de estrés superada ☐ · stock envasado y embalajes pre-armados ☐ · acceso anticipado enviado ☐

---

## SEMANA 6 – Lanzamiento y primeras ventas (detalle)

### Día 36 – DÍA D
- **Hora de apertura:** publicar post + historias, enviar mensaje B, actualizar link en bio.
- **Durante el día:** cada 2–3 horas una historia con avance ("ya salieron X packs", repost de clientes, "quedan Y del sabor Z"). Responder cada mensaje en menos de 30 minutos.
- **Tarde:** despachar o preparar todos los pedidos del día; mandar aviso de despacho con seguimiento.
- **Noche:** historia de cierre agradeciendo y recordando que la oferta dura hasta el día 38.

### Días 37–38 – Sostener la oferta
- Recordatorio de "últimas horas" de la oferta.
- Compartir cada foto o mensaje de cliente que llegue (pedir permiso con una pregunta rápida).
- Enviar a la lista de espera que **no compró** un único mensaje: "¿te quedaste con ganas? La oferta cierra hoy".
- Revisar stock por sabor: si uno se agota, comunicarlo como noticia, no como problema.

### Días 39–40 – Primeras reseñas
- A quienes compraron el día 36 (ya debería haberles llegado), enviar mensaje: "¿Ya lo probaste? Me encantaría saber qué te pareció, y si te animás, una foto de tu taza". Ofrecer un código de 10 % para la próxima compra a cambio de reseña con foto.
- Cargar las reseñas en la tienda y guardarlas en una historia destacada.

### Día 41 – Revisión de números
Planilla con: ventas por sabor, ventas de pack vs. individual, ticket promedio, conversión de la lista de espera, ventas por código de aliado, costo de envío real vs. cobrado, mensajes/preguntas más repetidas. Esto define qué reponer primero y qué ajustar en la tienda.

### Día 42 – Plan post-lanzamiento (2 semanas siguientes)
- Calendario de contenido liviano: 3 publicaciones por semana (recetas o rituales con cada té, reseñas, detrás de escena de la reposición).
- Agradecer a aliados con resultados concretos y proponer continuidad (reventa o colaboración).
- Fijar fecha de reposición y comunicarla.
- Elegir **una** mejora para la próxima tanda (empaque, un quinto sabor, suscripción mensual) y no más.

**Checklist Semana 6:** apertura ejecutada ☐ · todos los pedidos despachados en plazo ☐ · oferta cerrada en fecha ☐ · ≥5 reseñas recolectadas ☐ · planilla de resultados ☐ · calendario post-lanzamiento ☐

---

Con esto el plan queda completo de punta a punta. **Siguiente paso:** ahora que tenés la estructura, lo que falta es ponerle tus datos reales. Cuando puedas, pasame los nombres y perfiles de los 4 sabores y tu costo aproximado por sobre, y en la próxima respuesta te devuelvo la **biblia del lanzamiento (Día 7) ya redactada** con precios concretos, propuesta de valor y la línea de cada sabor lista para etiqueta.


## Respuesta completa

Perfecto, cero distracciones. Acá va el plan consolidado. Las Semanas 3 y 4 ya las detallé en respuestas anteriores, así que las dejo en resumen, y aprovecho para **cerrar el plan detallando las Semanas 5 y 6**, que faltaban.

---

# PLAN DE LANZAMIENTO – LÍNEA DE TÉS ARTESANALES (6 SEMANAS)

## Vista general

| Semana | Hito | Resultado al cierre |
|---|---|---|
| 1 | Definición y bases | "Biblia del lanzamiento" de 1 página: fecha, precios, cliente ideal, propuesta de valor, stock |
| 2 | Producto listo para vender | Etiquetas en imprenta, banco de fotos/videos, 5 fichas de producto, pedido de prueba físico |
| 3 | Canal de venta operativo | Tienda funcionando, pagos y envíos probados, políticas y FAQ publicadas |
| 4 | Pre-lanzamiento y lista de espera | Fecha anunciada, formulario activo, 6 publicaciones, 3–5 aliados confirmados |
| 5 | Calentamiento | Muestras entregadas, cuenta regresiva en curso, mensajes de lanzamiento listos, flujo de compra testeado |
| 6 | Lanzamiento y primeras ventas | Apertura con oferta limitada, pedidos despachados en plazo, primeras reseñas, contenido post-lanzamiento |

---

## SEMANA 1 – Definición y bases (detalle)

### Día 1 – Fecha y calendario inverso
- Fijar día exacto (martes a jueves; evitar lunes, viernes y feriados) y hora de apertura (10–11 am).
- Cargar en calendario las fechas límite de las semanas 2 a 5.
- Definir plan B: si algo se atrasa, ¿se mueve la fecha o se lanza con 3 sabores?

**Entregable:** calendario con 6 fechas clave + plan B.

### Día 2 – Costos reales
Planilla por sabor: hojas por sobre (según gramaje), empaque, etiqueta, mano de obra, merma 10 %, embalaje de envío prorrateado.

**Entregable:** costo unitario de cada sabor y del pack.

### Día 3 – Precios finales
- Público: 3–4× el costo. Mayorista: 50–60 % del precio al público. Pack: suma de los 4 menos 10–15 %.
- Decidir si los 4 tienen el mismo precio o hay uno "premium dentro del premium".
- Definir oferta de lanzamiento (verificar margen) y umbral de envío gratis.

**Entregable:** lista de precios cerrada (4 individuales, pack, mayorista, oferta).

### Día 4 – Cliente ideal
Una persona concreta: nombre ficticio, edad, ciudad, ocupación, para qué compra, dónde descubre productos, qué le frustra del té actual, cuánto paga sin dudar. Si hay dos públicos, elegir uno como principal.

**Entregable:** ficha de cliente ideal (media página).

### Día 5 – Propuesta de valor
1. Una frase de 10–15 palabras.
2. Tres diferenciales concretos y verificables.
3. Una línea por sabor: nombre + perfil + momento del día.

**Entregable:** texto base de propuesta de valor.

### Día 6 – Stock y capacidad
- Unidades disponibles por sabor para el día 1 (2–3 semanas de ventas estimadas).
- Plazo de reposición de hojas, sobres y etiquetas.
- Decidir si se comunica como edición limitada.

**Entregable:** stock de lanzamiento + tiempo de reposición.

### Día 7 – Consolidar
Juntar todo en una hoja, leer en voz alta, buscar contradicciones, mostrársela a alguien que haga preguntas incómodas.

**Entregable:** biblia del lanzamiento (1 página).

**Checklist Semana 1:** fecha y hora ☐ · costos ☐ · precios ☐ · cliente ideal ☐ · propuesta de valor ☐ · stock ☐ · documento consolidado ☐

---

## SEMANA 2 – Producto listo para vender (detalle)

### Días 8–9 – Etiqueta y empaque

| Frente | Dorso |
|---|---|
| Marca · nombre del sabor · tipo de base · línea de perfil · peso neto | Ingredientes en orden · origen · instrucciones (gramos, temperatura, tiempo) · tazas aprox. · lote y vencimiento · contacto/redes · registro sanitario si aplica |

Decisiones: color por sabor vs. paleta única; sobre con ventana o no. Pedir presupuesto y plazo de imprenta por escrito el día 8. Plan B: etiquetas adhesivas locales para los primeros 50 sobres.

**Entregable:** 4 artes finales aprobados y en imprenta.

### Días 10–11 – Fotos y video
1. Pack shot de cada sobre (fondo neutro, misma luz y ángulo).
2. Primer plano de hojas sueltas de cada blend.
3. En uso: taza, tetera, vapor, manos; uno por sabor en distinto momento del día.
4. Familia: los 4 juntos.
5. Detrás de escena: vos pesando, mezclando, envasando.

Mínimo 15–20 fotos editadas con un mismo tono + 5–6 videos verticales de 10–15 s. Regla: 2–3 fondos y un solo estilo de luz.

**Entregable:** banco de fotos y videos.

### Días 12–13 – Fichas de producto
Por sabor: nombre + subtítulo · descripción corta (qué es, a qué sabe, para qué momento) · 3 notas de sabor · ingredientes y origen · preparación (gramos, temperatura, tiempo, cuántas infusiones) · para quién es · peso y precio. Más la ficha del pack con ángulo propio ("un sabor para cada momento").

**Entregable:** 5 fichas listas para la tienda.

### Día 14 – Prueba física
Armar un pedido real: sobre + embalaje + tarjeta. Pesarlo, sacudirlo, abrirlo como cliente. Ajustar.

**Entregable:** una unidad "lista para enviar" como referencia.

**Checklist Semana 2:** etiquetas en imprenta ☐ · banco de fotos/videos ☐ · 5 fichas ☐ · pedido de prueba pesado ☐

---

## SEMANA 3 – Canal de venta operativo (resumen; detalle en respuesta anterior)

- **D15** Elegir canal (recomendado: tienda online + WhatsApp para cierre). 
- **D16** Cargar 5 productos con ≥4 fotos y stock real.
- **D17** Dos medios de pago activos y una compra real de prueba.
- **D18** Tabla de envíos (máx. 3 opciones), umbral de envío gratis, insumos de embalaje comprados.
- **D19** Política de cambios (solo si llega dañado, 48 h con foto) + FAQ.
- **D20** Confirmación de compra y de envío automatizadas, pixel/analytics.
- **D21** Prueba de compra con 2 personas externas, sin ayuda.

---

## SEMANA 4 – Pre-lanzamiento y lista de espera (resumen; detalle en respuesta anterior)

- **D22** Formulario de lista de espera + un solo incentivo (acceso anticipado + 10–15 % o envío gratis). Meta: 50–80 inscriptos desde cero, 150–300 con comunidad.
- **D23–28** Un contenido por día: teaser → tu historia → origen → proceso → revelación de los 4 sabores → anuncio de fecha.
- **En paralelo** Contactar 10 aliados locales (cafeterías, tiendas gourmet, micro-influencers de 1.000–20.000 seguidores) con el guion de muestra sin compromiso. Meta: 3–5 confirmados.

---

## SEMANA 5 – Calentamiento (detalle)

### Día 29 – Envío de muestras a aliados
- Armar 3–5 packs de muestra con los 4 sabores + tarjeta manuscrita + ficha con fecha de lanzamiento y código de descuento personalizado por aliado (ej. CAFÉX10) para medir quién trae ventas.
- Enviar o entregar en mano. En mano siempre convierte mejor.

**Entregable:** muestras entregadas, códigos cargados en la tienda.

### Día 30 – Textos de lanzamiento (dos versiones)
**A) Lista de espera (sale el día anterior al lanzamiento):**
> Asunto: Tu acceso anticipado está abierto 🍃
> Te prometí que ibas a ser de los primeros. Desde ahora y hasta mañana a las [hora], los 4 blends están disponibles solo para vos con [incentivo]. Mañana abrimos al público y el stock es de [N] packs. [Botón: Elegir mi té]

**B) Público general (sale el día del lanzamiento):**
> Ya está acá. 4 blends de hojas enteras, mezclados a mano en lotes pequeños. Hasta el [día+2] el pack de 4 lleva envío gratis. Son [N] unidades y no hay segunda tanda hasta [fecha]. [Botón: Ver los sabores]

Preparar también 3 historias y 1 post para el día D con el mismo mensaje.

**Entregable:** mensajes A y B programados, post y historias del día D listas.

### Días 31–35 – Cuenta regresiva (5 días)
| Día | Contenido |
|---|---|
| 31 | "Faltan 5": sabor 1 en profundidad (origen, notas, cómo prepararlo) |
| 32 | "Faltan 4": sabor 2 |
| 33 | "Faltan 3": sabor 3 |
| 34 | "Faltan 2": sabor 4 + repost de lo que compartan los aliados |
| 35 | "Mañana": recordatorio de hora, stock limitado, último llamado a la lista |

Cada día: 1 post + 2–3 historias con link a la lista. Responder todos los comentarios y mensajes el mismo día.

### Día 33 (en paralelo) – Prueba de estrés del flujo
- 2–3 personas de confianza compran al mismo tiempo desde distintos dispositivos y medios de pago.
- Verificar: ¿el stock descuenta bien? ¿llegan los mails automáticos? ¿los códigos de descuento funcionan y no se acumulan entre sí? ¿la oferta de lanzamiento se activa y desactiva en la fecha correcta?
- Corregir y volver a probar.

**Entregable:** flujo validado bajo carga simultánea.

### Día 35 – Preparación operativa del día D
- Stock completo envasado, etiquetado y ordenado por sabor.
- Embalajes pre-armados (caja + relleno + tarjeta) para los primeros 30–50 pedidos.
- Etiquetas de envío o cuenta de courier lista.
- Agenda del día D bloqueada: nada más que lanzamiento.
- Enviar el mensaje A (acceso anticipado) a la lista de espera.

**Entregable:** operación lista; lista de espera ya comprando.

**Checklist Semana 5:** muestras entregadas ☐ · códigos por aliado ☐ · mensajes A y B listos ☐ · cuenta regresiva publicada ☐ · prueba de estrés superada ☐ · stock envasado y embalajes pre-armados ☐ · acceso anticipado enviado ☐

---

## SEMANA 6 – Lanzamiento y primeras ventas (detalle)

### Día 36 – DÍA D
- **Hora de apertura:** publicar post + historias, enviar mensaje B, actualizar link en bio.
- **Durante el día:** cada 2–3 horas una historia con avance ("ya salieron X packs", repost de clientes, "quedan Y del sabor Z"). Responder cada mensaje en menos de 30 minutos.
- **Tarde:** despachar o preparar todos los pedidos del día; mandar aviso de despacho con seguimiento.
- **Noche:** historia de cierre agradeciendo y recordando que la oferta dura hasta el día 38.

### Días 37–38 – Sostener la oferta
- Recordatorio de "últimas horas" de la oferta.
- Compartir cada foto o mensaje de cliente que llegue (pedir permiso con una pregunta rápida).
- Enviar a la lista de espera que **no compró** un único mensaje: "¿te quedaste con ganas? La oferta cierra hoy".
- Revisar stock por sabor: si uno se agota, comunicarlo como noticia, no como problema.

### Días 39–40 – Primeras reseñas
- A quienes compraron el día 36 (ya debería haberles llegado), enviar mensaje: "¿Ya lo probaste? Me encantaría saber qué te pareció, y si te animás, una foto de tu taza". Ofrecer un código de 10 % para la próxima compra a cambio de reseña con foto.
- Cargar las reseñas en la tienda y guardarlas en una historia destacada.

### Día 41 – Revisión de números
Planilla con: ventas por sabor, ventas de pack vs. individual, ticket promedio, conversión de la lista de espera, ventas por código de aliado, costo de envío real vs. cobrado, mensajes/preguntas más repetidas. Esto define qué reponer primero y qué ajustar en la tienda.

### Día 42 – Plan post-lanzamiento (2 semanas siguientes)
- Calendario de contenido liviano: 3 publicaciones por semana (recetas o rituales con cada té, reseñas, detrás de escena de la reposición).
- Agradecer a aliados con resultados concretos y proponer continuidad (reventa o colaboración).
- Fijar fecha de reposición y comunicarla.
- Elegir **una** mejora para la próxima tanda (empaque, un quinto sabor, suscripción mensual) y no más.

**Checklist Semana 6:** apertura ejecutada ☐ · todos los pedidos despachados en plazo ☐ · oferta cerrada en fecha ☐ · ≥5 reseñas recolectadas ☐ · planilla de resultados ☐ · calendario post-lanzamiento ☐

---

Con esto el plan queda completo de punta a punta. **Siguiente paso:** ahora que tenés la estructura, lo que falta es ponerle tus datos reales. Cuando puedas, pasame los nombres y perfiles de los 4 sabores y tu costo aproximado por sobre, y en la próxima respuesta te devuelvo la **biblia del lanzamiento (Día 7) ya redactada** con precios concretos, propuesta de valor y la línea de cada sabor lista para etiqueta.