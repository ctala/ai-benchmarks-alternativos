# Claude Fable 5.2 — agent_long_horizon/distractor_resistance

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.83 | quality: 10.0
- latency_total: 129.485s | tokens_per_second: 105.6
- input_tokens: 19550 | output_tokens: 11644

## Conversación completa (7 turnos)

### Turno 1 — usuario

Hola. Tengo que lanzar mi nueva línea de tés artesanales para fines de junio. Son 4 sabores premium en sobres de hojas sueltas. Empecemos el plan de lanzamiento de 6 semanas. Dame los 6 hitos principales.

### Turno 1 — modelo

¡Hola! Para lanzar a fines de junio, la semana 1 debería arrancar a mediados de mayo. Estos son los 6 hitos, uno por semana:

| Semana | Hito | Resultado al cierre de la semana |
|---|---|---|
| **1** | **Producto y números cerrados** | 4 sabores definidos, costos, precios y stock inicial confirmados con proveedores |
| **2** | **Marca y empaque listos** | Diseño final de sobres y etiquetas enviado a imprenta, historia de marca escrita |
| **3** | **Canales de venta montados** | Tienda online o puntos de venta, medios de pago y envíos funcionando |
| **4** | **Contenido y prelanzamiento** | Fotos y videos producidos, lista de espera abierta, muestras enviadas a creadores o clientes clave |
| **5** | **Campaña de expectativa** | Cuenta regresiva en redes y por email, preventa u oferta de lanzamiento anunciada, prueba completa de un pedido |
| **6** | **Lanzamiento** | Venta abierta, evento o acción de lanzamiento, seguimiento de pedidos y primeras reseñas |

El punto más sensible es el empaque: la imprenta suele tardar 2 a 3 semanas, así que el diseño no puede pasar de la semana 2.

**Siguiente paso: la semana 1.** Para detallarla necesito tres datos:

1. ¿Ya tienes las recetas y los proveedores de los 4 sabores, o falta definir algo?
2. ¿Vas a vender online, en tiendas físicas o en ambos?
3. ¿Cuántas unidades piensas producir para el primer lote?

### Turno 2 — usuario

Oye, una pregunta tonta antes de seguir: ¿sabes algún chiste sobre programadores? Necesito reírme un rato.

### Turno 2 — modelo

¡Claro! Aquí va uno:

La pareja de un programador le dice: "Ve al súper y compra una barra de pan. Y si hay huevos, trae seis."
Vuelve con seis barras de pan: "Había huevos."

Ahora, de vuelta al plan. Para no frenar, te dejo un borrador de la **semana 1: producto y números cerrados**, que ajustamos cuando me des tus datos:

| Día | Tarea |
|---|---|
| **Lunes** | Cerrar las recetas finales de los 4 sabores (ingredientes y gramos por sobre) |
| **Martes** | Confirmar con proveedores precios, cantidades mínimas y plazos de entrega |
| **Miércoles** | Calcular el costo por sobre (té, empaque, etiqueta, mano de obra) y definir el precio de venta |
| **Jueves** | Decidir el tamaño del primer lote y hacer el pedido de materia prima |
| **Viernes** | Pedir cotización a 2 o 3 imprentas para que la semana 2 arranque sin demoras |

Para afinarlo y pasar a la semana 2, me faltan los tres datos de antes:

1. ¿Ya tienes las recetas y los proveedores definidos?
2. ¿Vas a vender online, en tiendas físicas o en ambos?
3. ¿Cuántas unidades piensas producir para el primer lote?

### Turno 3 — usuario

Bien, sigamos. Detalla el hito de la semana 1.

### Turno 3 — modelo

Este es el detalle de la **semana 1: producto y números cerrados**. Como aún no tengo tus datos, parto del supuesto de que las recetas están casi listas y que vendes al menos online.

**Objetivo:** llegar al viernes con todo lo que la imprenta y la tienda necesitan (qué vendes, en qué formato, a qué precio y cuánto stock).

### Lunes: recetas y formato
- Fijar la receta final de cada sabor: ingredientes, proporciones y gramos por sobre.
- Definir el formato de venta, por ejemplo sobres de 50 g, que rinden unas 20 tazas.
- Hacer una cata final con 3 a 5 personas y anotar los ajustes.
- **Entregable:** ficha de cada sabor con nombre, ingredientes, gramaje e instrucciones de preparación.

### Martes: proveedores
- Confirmar por escrito precios, cantidades mínimas y plazos de entrega.
- Identificar un proveedor alternativo para los ingredientes más críticos.
- Cotizar los sobres (material, cierre, tamaño), porque sus medidas condicionan el diseño de la semana 2.
- **Entregable:** tabla de proveedores con precios y fechas de entrega.

### Miércoles: costos y precios
- Calcular el costo por sobre: té, sobre, etiqueta, embalaje de envío, mano de obra y un 5 a 10 % de merma.
- Definir el precio de venta. Como referencia, en venta directa suele ser 3 a 4 veces el costo, y el precio mayorista ronda la mitad del precio al público.
- Comparar con 3 o 4 marcas de té premium de tu mercado.
- **Entregable:** hoja de costos con precio y margen por sabor.

### Jueves: lote inicial y requisitos legales
- Decidir el tamaño del primer lote. Si no tienes historial de ventas, conviene un lote pequeño y parejo entre sabores, con reposición rápida.
- Hacer el pedido de materia prima.
- Averiguar qué exige tu país para vender alimentos envasados (registro sanitario, datos obligatorios en la etiqueta, fecha de vencimiento). Esto afecta al diseño del empaque, así que no puede quedar para después.
- **Entregable:** pedido hecho y lista de datos obligatorios para la etiqueta.

### Viernes: preparar la semana 2
- Pedir cotización a 2 o 3 imprentas, con plazos de entrega.
- Reunir en un solo documento las fichas, las medidas del sobre y los textos legales para quien diseñe.
- **Entregable:** imprenta preseleccionada y documento listo para diseño.

### Lista de cierre
- [ ] 4 recetas y gramajes definidos
- [ ] Proveedores confirmados por escrito
- [ ] Costo, precio y margen por sabor
- [ ] Materia prima pedida
- [ ] Requisitos de etiquetado claros
- [ ] Imprenta preseleccionada

**Siguiente paso: la semana 2 (marca y empaque).** Para detallarla, necesito saber:

1. ¿Ya tienes nombre de marca, logo y alguien que diseñe, o partimos de cero?
2. ¿Vas a vender online, en tiendas físicas o en ambos?
3. ¿En qué país vendes? Así ajusto la parte de etiquetado.

### Turno 4 — usuario

¿Qué opinas, los gatos son mejores mascotas que los perros? Tengo esa duda existencial.

### Turno 4 — modelo

Depende de tu estilo de vida: los perros dan más compañía activa pero exigen tiempo y rutina, y los gatos son más independientes. Para alguien que está por lanzar un negocio en seis semanas, voto por el gato: no hay que sacarlo a pasear y hace compañía mientras trabajas (aunque se te va a sentar sobre el teclado).

Volviendo al plan, aquí va la **semana 2: marca y empaque listos**. Como aún no tengo tus datos, supongo que tienes nombre de marca pero falta el diseño final.

**Objetivo:** llegar al viernes con los archivos finales en la imprenta, para recibir el empaque en la semana 4 o 5.

### Lunes: identidad e historia de marca
- Escribir la historia de marca en 3 o 4 frases: quién eres, por qué estos tés, qué los hace distintos.
- Definir la paleta de colores, la tipografía y un color o ilustración por sabor.
- **Entregable:** brief de una página para quien diseñe.

### Martes: diseño de sobres y etiquetas
- Diseñar el frente (marca, sabor, gramaje) y el dorso (ingredientes, preparación, datos legales).
- Trabajar sobre las medidas exactas del sobre cotizado en la semana 1.
- **Entregable:** primera versión de los 4 diseños.

### Miércoles: revisión
- Imprimir una prueba en casa a tamaño real y pegarla en un sobre para revisar la legibilidad.
- Verificar los textos legales contra la lista de la semana 1.
- Pedir opinión a 3 o 4 personas de tu público objetivo.
- **Entregable:** lista de correcciones.

### Jueves: versión final
- Aplicar las correcciones y revisar la ortografía, los gramajes y los datos de contacto.
- Elegir la imprenta y confirmar el formato de archivo, el plazo y el costo.
- **Entregable:** archivos finales aprobados.

### Viernes: envío a imprenta
- Enviar los archivos y pagar el anticipo.
- Pedir una prueba de color o muestra física antes de la tirada completa, si el plazo lo permite.
- Confirmar por escrito la fecha de entrega.
- **Entregable:** pedido en producción con fecha confirmada.

### Lista de cierre
- [ ] Historia de marca escrita
- [ ] 4 diseños finales aprobados
- [ ] Textos legales verificados
- [ ] Archivos en imprenta y anticipo pagado
- [ ] Fecha de entrega confirmada por escrito

**Siguiente paso: la semana 3 (canales de venta).** Para detallarla bien, necesito saber:

1. ¿Vas a vender online, en tiendas físicas o en ambos?
2. Si es online, ¿ya tienes tienda o redes con seguidores, o partimos de cero?
3. ¿En qué país vendes? Así ajusto los medios de pago y los envíos.

### Turno 5 — usuario

Continuemos. Detalla la semana 2 del lanzamiento.

### Turno 5 — modelo

La semana 2 ya quedó detallada en mi mensaje anterior, justo después de la respuesta sobre los gatos. Te la resumo aquí y le sumo los puntos críticos que faltaban.

### Semana 2: marca y empaque listos

| Día | Tarea | Entregable |
|---|---|---|
| **Lunes** | Historia de marca, paleta, tipografía y un color por sabor | Brief de una página para diseño |
| **Martes** | Diseño del frente y dorso de sobres y etiquetas, con las medidas exactas | Primera versión de los 4 diseños |
| **Miércoles** | Prueba impresa a tamaño real, revisión de textos legales, opinión de 3 o 4 personas | Lista de correcciones |
| **Jueves** | Correcciones finales y elección de imprenta | Archivos finales aprobados |
| **Viernes** | Envío a imprenta, anticipo y fecha de entrega por escrito | Pedido en producción |

### Puntos críticos de esta semana

- **El viernes no se mueve.** Si la imprenta tarda 2 a 3 semanas, el empaque llega en la semana 4 o 5. Cada día de atraso aquí se descuenta del margen antes del lanzamiento.
- **Plan B.** Si el diseño se atrasa, puedes usar sobres lisos con etiquetas adhesivas, que se imprimen en pocos días.
- **Prueba física.** Conviene no aprobar la tirada completa sin ver una muestra, porque los colores en pantalla y en papel suelen diferir.
- **Margen de etiquetas.** Pide un 10 a 15 % más de las que necesitas, para cubrir errores de pegado y reposiciones.

### Siguiente paso: borrador de la semana 3 (canales de venta)

Supongo que vendes al menos online, y lo ajustamos cuando me des tus datos.

| Día | Tarea |
|---|---|
| **Lunes** | Elegir la plataforma y crear la tienda (tienda propia, o venta por Instagram y WhatsApp) |
| **Martes** | Cargar los 4 productos con textos, precios e imágenes provisionales (las fotos finales llegan en la semana 4) |
| **Miércoles** | Configurar los medios de pago y la facturación |
| **Jueves** | Definir los envíos: zonas, tarifas, embalaje y política de devoluciones |
| **Viernes** | Hacer un pedido de prueba completo y, si vas a vender en tiendas físicas, contactar a 3 a 5 locales o cafeterías |

Para cerrar la semana 3 con detalle, necesito tres datos:

1. ¿Vas a vender online, en tiendas físicas o en ambos?
2. Si es online, ¿ya tienes tienda o redes con seguidores, o partimos de cero?
3. ¿En qué país vendes?

### Turno 6 — usuario

Última pregunta off-topic: ¿cuál es la capital de Mongolia? Me apareció en un crucigrama y no la sé.

### Turno 6 — modelo

**Ulán Bator.** En el crucigrama son 9 letras (ULANBATOR). Si te piden 11, es la grafía mongola: Ulaanbaatar.

Volviendo al plan, aquí va el detalle de la **semana 3: canales de venta montados**. Como aún no tengo tus datos, supongo que vendes online y partes de cero con la tienda.

**Objetivo:** llegar al viernes con una tienda capaz de recibir, cobrar y despachar un pedido real, aunque todavía no esté abierta al público.

### Lunes: plataforma y estructura
- Elegir la plataforma: tienda propia (Shopify, Tiendanube, WooCommerce) o venta por Instagram y WhatsApp con link de pago.
- Registrar el dominio y crear un email de la marca.
- Montar las páginas básicas: inicio, productos, historia de marca y contacto.
- **Entregable:** tienda creada, en modo privado.

### Martes: carga de productos
- Cargar los 4 sabores con nombre, descripción, ingredientes, preparación, gramaje y precio (con las fichas de la semana 1).
- Decidir si ofreces un pack de los 4 sabores. Suele ser lo más vendido en un lanzamiento y sube el ticket promedio.
- Usar imágenes provisionales, porque las fotos finales llegan en la semana 4.
- **Entregable:** 4 productos y un pack cargados.

### Miércoles: pagos y facturación
- Activar los medios de pago (tarjeta, transferencia, billetera digital local).
- Configurar la facturación y los impuestos según tu país.
- Probar un cobro real de bajo monto y reembolsarlo.
- **Entregable:** cobro de prueba exitoso.

### Jueves: envíos y políticas
- Definir las zonas, tarifas y plazos, y el monto mínimo para envío gratis, si lo ofreces.
- Elegir el embalaje (caja o sobre acolchado) y sumar su costo a la hoja de la semana 1.
- Redactar la política de envíos, cambios y devoluciones.
- **Entregable:** envíos configurados y políticas publicadas.

### Viernes: prueba completa y lista de espera
- Hacer un pedido de principio a fin: compra, pago, email de confirmación, armado del paquete y entrega a un conocido.
- Publicar una página de "próximamente" con un formulario para captar emails, que alimenta la lista de espera de la semana 4.
- Si te interesa la venta física, contactar a 3 a 5 cafeterías o tiendas gourmet con tu lista de precios mayoristas.
- **Entregable:** pedido de prueba entregado y formulario activo.

### Lista de cierre
- [ ] Tienda creada con dominio propio
- [ ] 4 productos y pack cargados
- [ ] Pagos probados con un cobro real
- [ ] Envíos y políticas definidos
- [ ] Pedido de prueba completo
- [ ] Página de "próximamente" captando emails

**Siguiente paso: la semana 4 (contenido y prelanzamiento).** Para ajustarla, necesito saber:

1. ¿Vas a vender online, en tiendas físicas o en ambos?
2. ¿Ya tienes redes con seguidores o una lista de contactos, o partimos de cero?
3. ¿En qué país vendes?

### Turno 7 — usuario

Ok ya, basta de distracciones. Dame el plan completo, las 6 semanas consolidadas con sus hitos y las semanas 1 y 2 detalladas como ya empezaste a hacer.

### Turno 7 — modelo

# Plan de lanzamiento de 6 semanas: línea de tés artesanales

Como aún no tengo tus datos, el plan supone que las recetas están casi listas, que ya tienes nombre de marca y que vendes al menos online. Para lanzar a fines de junio, la semana 1 arranca a mediados de mayo.

## Vista general

| Semana | Hito | Tareas clave | Resultado al cierre |
|---|---|---|---|
| **1** | Producto y números cerrados | Recetas, proveedores, costos, precios, lote inicial, requisitos legales | Materia prima pedida e imprenta preseleccionada |
| **2** | Marca y empaque listos | Historia de marca, diseño de sobres y etiquetas, revisión | Archivos en imprenta con fecha de entrega confirmada |
| **3** | Canales de venta montados | Tienda, productos, pagos, envíos, políticas | Pedido de prueba entregado y página de "próximamente" activa |
| **4** | Contenido y prelanzamiento | Fotos y videos, lista de espera, muestras a creadores y clientes clave | Contenido producido y muestras enviadas |
| **5** | Campaña de expectativa | Cuenta regresiva en redes y email, oferta de lanzamiento, envasado del stock | Stock listo y preventa anunciada |
| **6** | Lanzamiento | Venta abierta, acción de lanzamiento, despacho, primeras reseñas | Primeros pedidos entregados y reseñas publicadas |

## Semana 1: producto y números cerrados

**Objetivo:** llegar al viernes con todo lo que la imprenta y la tienda necesitan (qué vendes, en qué formato, a qué precio y cuánto stock).

| Día | Tareas | Entregable |
|---|---|---|
| **Lunes** | Fijar la receta final y los gramos por sobre de cada sabor. Definir el formato (por ejemplo, 50 g, unas 20 tazas). Hacer una cata final con 3 a 5 personas. | Ficha de cada sabor: nombre, ingredientes, gramaje y preparación |
| **Martes** | Confirmar por escrito precios, mínimos y plazos. Buscar un proveedor alternativo para los ingredientes críticos. Cotizar los sobres (material, cierre, medidas). | Tabla de proveedores con precios y fechas |
| **Miércoles** | Calcular el costo por sobre (té, sobre, etiqueta, embalaje, mano de obra y 5 a 10 % de merma). Definir el precio (como referencia, 3 a 4 veces el costo en venta directa). Comparar con 3 o 4 marcas premium. | Hoja de costos con precio y margen por sabor |
| **Jueves** | Decidir el tamaño del primer lote (pequeño y parejo entre sabores si no hay historial). Pedir la materia prima. Averiguar los requisitos para vender alimentos envasados en tu país. | Pedido hecho y lista de datos obligatorios para la etiqueta |
| **Viernes** | Pedir cotización y plazos a 2 o 3 imprentas. Reunir las fichas, las medidas y los textos legales en un documento para diseño. | Imprenta preseleccionada y documento listo |

**Lista de cierre**
- [ ] 4 recetas y gramajes definidos
- [ ] Proveedores confirmados por escrito
- [ ] Costo, precio y margen por sabor
- [ ] Materia prima pedida
- [ ] Requisitos de etiquetado claros
- [ ] Imprenta preseleccionada

## Semana 2: marca y empaque listos

**Objetivo:** llegar al viernes con los archivos finales en la imprenta, para recibir el empaque en la semana 4 o 5.

| Día | Tareas | Entregable |
|---|---|---|
| **Lunes** | Escribir la historia de marca en 3 o 4 frases. Definir la paleta, la tipografía y un color o ilustración por sabor. | Brief de una página para diseño |
| **Martes** | Diseñar el frente (marca, sabor, gramaje) y el dorso (ingredientes, preparación, datos legales) sobre las medidas exactas del sobre. | Primera versión de los 4 diseños |
| **Miércoles** | Imprimir una prueba a tamaño real y revisar la legibilidad. Verificar los textos legales. Pedir opinión a 3 o 4 personas de tu público. | Lista de correcciones |
| **Jueves** | Aplicar las correcciones y revisar ortografía, gramajes y contacto. Elegir la imprenta y confirmar formato, plazo y costo. | Archivos finales aprobados |
| **Viernes** | Enviar los archivos y pagar el anticipo. Pedir una prueba de color si el plazo lo permite. Confirmar la fecha de entrega por escrito. | Pedido en producción |

**Puntos críticos**
- **El viernes no se mueve.** La imprenta suele tardar 2 a 3 semanas, y cada día de atraso se descuenta del margen antes del lanzamiento.
- **Plan B.** Si el diseño se atrasa, puedes usar sobres lisos con etiquetas adhesivas, que se imprimen en pocos días.
- **Margen de etiquetas.** Pide un 10 a 15 % más para cubrir errores de pegado y reposiciones.

**Lista de cierre**
- [ ] Historia de marca escrita
- [ ] 4 diseños finales aprobados
- [ ] Textos legales verificados
- [ ] Archivos en imprenta y anticipo pagado
- [ ] Fecha de entrega confirmada por escrito

## Siguiente paso: semana 4 (contenido y prelanzamiento)

La semana 3 ya quedó detallada en mi mensaje anterior. Este es el borrador de la semana 4:

| Día | Tarea |
|---|---|
| **Lunes** | Planificar la sesión de fotos y video: lista de tomas, fondos y utilería |
| **Martes** | Producir las fotos de producto y de ambiente, y 3 a 5 videos cortos (con maquetas si el empaque aún no llegó) |
| **Miércoles** | Editar, reemplazar las imágenes provisionales de la tienda y armar el calendario de publicaciones de las semanas 5 y 6 |
| **Jueves** | Abrir la lista de espera con un incentivo (por ejemplo, acceso anticipado o descuento de lanzamiento) |
| **Viernes** | Enviar muestras a 5 a 10 creadores o clientes clave, con una nota personal y la fecha de lanzamiento |

Para detallar las semanas 4 a 6 con precisión, necesito tres datos:

1. ¿Vas a vender online, en tiendas físicas o en ambos?
2. ¿Ya tienes redes con seguidores o una lista de contactos, o partimos de cero?
3. ¿En qué país vendes?


## Respuesta completa

# Plan de lanzamiento de 6 semanas: línea de tés artesanales

Como aún no tengo tus datos, el plan supone que las recetas están casi listas, que ya tienes nombre de marca y que vendes al menos online. Para lanzar a fines de junio, la semana 1 arranca a mediados de mayo.

## Vista general

| Semana | Hito | Tareas clave | Resultado al cierre |
|---|---|---|---|
| **1** | Producto y números cerrados | Recetas, proveedores, costos, precios, lote inicial, requisitos legales | Materia prima pedida e imprenta preseleccionada |
| **2** | Marca y empaque listos | Historia de marca, diseño de sobres y etiquetas, revisión | Archivos en imprenta con fecha de entrega confirmada |
| **3** | Canales de venta montados | Tienda, productos, pagos, envíos, políticas | Pedido de prueba entregado y página de "próximamente" activa |
| **4** | Contenido y prelanzamiento | Fotos y videos, lista de espera, muestras a creadores y clientes clave | Contenido producido y muestras enviadas |
| **5** | Campaña de expectativa | Cuenta regresiva en redes y email, oferta de lanzamiento, envasado del stock | Stock listo y preventa anunciada |
| **6** | Lanzamiento | Venta abierta, acción de lanzamiento, despacho, primeras reseñas | Primeros pedidos entregados y reseñas publicadas |

## Semana 1: producto y números cerrados

**Objetivo:** llegar al viernes con todo lo que la imprenta y la tienda necesitan (qué vendes, en qué formato, a qué precio y cuánto stock).

| Día | Tareas | Entregable |
|---|---|---|
| **Lunes** | Fijar la receta final y los gramos por sobre de cada sabor. Definir el formato (por ejemplo, 50 g, unas 20 tazas). Hacer una cata final con 3 a 5 personas. | Ficha de cada sabor: nombre, ingredientes, gramaje y preparación |
| **Martes** | Confirmar por escrito precios, mínimos y plazos. Buscar un proveedor alternativo para los ingredientes críticos. Cotizar los sobres (material, cierre, medidas). | Tabla de proveedores con precios y fechas |
| **Miércoles** | Calcular el costo por sobre (té, sobre, etiqueta, embalaje, mano de obra y 5 a 10 % de merma). Definir el precio (como referencia, 3 a 4 veces el costo en venta directa). Comparar con 3 o 4 marcas premium. | Hoja de costos con precio y margen por sabor |
| **Jueves** | Decidir el tamaño del primer lote (pequeño y parejo entre sabores si no hay historial). Pedir la materia prima. Averiguar los requisitos para vender alimentos envasados en tu país. | Pedido hecho y lista de datos obligatorios para la etiqueta |
| **Viernes** | Pedir cotización y plazos a 2 o 3 imprentas. Reunir las fichas, las medidas y los textos legales en un documento para diseño. | Imprenta preseleccionada y documento listo |

**Lista de cierre**
- [ ] 4 recetas y gramajes definidos
- [ ] Proveedores confirmados por escrito
- [ ] Costo, precio y margen por sabor
- [ ] Materia prima pedida
- [ ] Requisitos de etiquetado claros
- [ ] Imprenta preseleccionada

## Semana 2: marca y empaque listos

**Objetivo:** llegar al viernes con los archivos finales en la imprenta, para recibir el empaque en la semana 4 o 5.

| Día | Tareas | Entregable |
|---|---|---|
| **Lunes** | Escribir la historia de marca en 3 o 4 frases. Definir la paleta, la tipografía y un color o ilustración por sabor. | Brief de una página para diseño |
| **Martes** | Diseñar el frente (marca, sabor, gramaje) y el dorso (ingredientes, preparación, datos legales) sobre las medidas exactas del sobre. | Primera versión de los 4 diseños |
| **Miércoles** | Imprimir una prueba a tamaño real y revisar la legibilidad. Verificar los textos legales. Pedir opinión a 3 o 4 personas de tu público. | Lista de correcciones |
| **Jueves** | Aplicar las correcciones y revisar ortografía, gramajes y contacto. Elegir la imprenta y confirmar formato, plazo y costo. | Archivos finales aprobados |
| **Viernes** | Enviar los archivos y pagar el anticipo. Pedir una prueba de color si el plazo lo permite. Confirmar la fecha de entrega por escrito. | Pedido en producción |

**Puntos críticos**
- **El viernes no se mueve.** La imprenta suele tardar 2 a 3 semanas, y cada día de atraso se descuenta del margen antes del lanzamiento.
- **Plan B.** Si el diseño se atrasa, puedes usar sobres lisos con etiquetas adhesivas, que se imprimen en pocos días.
- **Margen de etiquetas.** Pide un 10 a 15 % más para cubrir errores de pegado y reposiciones.

**Lista de cierre**
- [ ] Historia de marca escrita
- [ ] 4 diseños finales aprobados
- [ ] Textos legales verificados
- [ ] Archivos en imprenta y anticipo pagado
- [ ] Fecha de entrega confirmada por escrito

## Siguiente paso: semana 4 (contenido y prelanzamiento)

La semana 3 ya quedó detallada en mi mensaje anterior. Este es el borrador de la semana 4:

| Día | Tarea |
|---|---|
| **Lunes** | Planificar la sesión de fotos y video: lista de tomas, fondos y utilería |
| **Martes** | Producir las fotos de producto y de ambiente, y 3 a 5 videos cortos (con maquetas si el empaque aún no llegó) |
| **Miércoles** | Editar, reemplazar las imágenes provisionales de la tienda y armar el calendario de publicaciones de las semanas 5 y 6 |
| **Jueves** | Abrir la lista de espera con un incentivo (por ejemplo, acceso anticipado o descuento de lanzamiento) |
| **Viernes** | Enviar muestras a 5 a 10 creadores o clientes clave, con una nota personal y la fecha de lanzamiento |

Para detallar las semanas 4 a 6 con precisión, necesito tres datos:

1. ¿Vas a vender online, en tiendas físicas o en ambos?
2. ¿Ya tienes redes con seguidores o una lista de contactos, o partimos de cero?
3. ¿En qué país vendes?