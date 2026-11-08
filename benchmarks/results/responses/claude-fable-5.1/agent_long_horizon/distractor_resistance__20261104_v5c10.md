# Claude Fable 5.1 — agent_long_horizon/distractor_resistance

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 5.92 | quality: 7.5
- latency_total: 157.121s | tokens_per_second: 85.1
- input_tokens: 23653 | output_tokens: 11031

## Conversación completa (7 turnos)

### Turno 1 — usuario

Hola. Tengo que lanzar mi nueva línea de tés artesanales para fines de junio. Son 4 sabores premium en sobres de hojas sueltas. Empecemos el plan de lanzamiento de 6 semanas. Dame los 6 hitos principales.

### Turno 1 — modelo

¡Qué buen proyecto! Vamos directo al plan. Si el lanzamiento es a fines de junio, arrancamos a mediados de mayo. Estos son los 6 hitos principales, uno por semana:

**Semana 1 — Fundamentos del producto**
Definir nombres finales de los 4 sabores, fichas de producto (ingredientes, origen, notas de sabor, instrucciones de preparación), precio y márgenes. Confirmar proveedores de hojas y empaques.

**Semana 2 — Identidad y empaque**
Diseño final de etiquetas y sobres, fotografía de producto (packshots + fotos lifestyle), etiquetado legal (ingredientes, peso neto, lote, vencimiento). Pedido de producción del empaque.

**Semana 3 — Canales de venta y logística**
Tienda online lista (o marketplace), pasarela de pago, costos de envío, política de devoluciones. Definir stock inicial por sabor y punto de venta físico si lo hay.

**Semana 4 — Prelanzamiento y comunidad**
Lista de espera / preventa, calendario de contenidos para redes, contacto con micro-influencers o cafeterías aliadas, envío de muestras (kit de degustación con los 4 sabores).

**Semana 5 — Calentamiento**
Campaña de expectativa (teasers, cuenta regresiva), envío de muestras a prensa local o creadores, pruebas finales de compra en la tienda, preparación de materiales de lanzamiento (emails, posts, stories).

**Semana 6 — Lanzamiento**
Día L: publicación coordinada en todos los canales, email a la lista, oferta de lanzamiento (ej. pack de 4 sabores con descuento), atención a pedidos y soporte. Cierre de semana: métricas y ajustes.

**Siguiente paso:** empecemos por la Semana 1. ¿Me compartes los 4 sabores y una idea del precio que tienes en mente por sobre? Con eso armamos las fichas de producto y revisamos los márgenes.

### Turno 2 — usuario

Oye, una pregunta tonta antes de seguir: ¿sabes algún chiste sobre programadores? Necesito reírme un rato.

### Turno 2 — modelo

¡Claro, una pausa para reír siempre viene bien! 😄

¿Por qué los programadores confunden Halloween con Navidad?
Porque **OCT 31 = DEC 25**. (31 en octal es 25 en decimal… chiste de nerds, pero funciona).

Y uno más corto: un programador va al supermercado. Su pareja le dice: "Compra una barra de pan, y si hay huevos, trae 12". Volvió con 12 barras de pan. "¡Había huevos!".

Bueno, de vuelta al té. 🍵 Vamos con la **Semana 1 — Fundamentos del producto**. Para avanzar sin esperar, te dejo la plantilla de ficha de producto que vamos a llenar para cada uno de los 4 sabores:

**Ficha de producto (por sabor)**
- Nombre comercial
- Tipo de base (negro, verde, blanco, oolong, rooibos, infusión)
- Ingredientes y origen
- Notas de sabor (3 adjetivos clave)
- Preparación: cantidad por taza, temperatura del agua, tiempo de infusión
- Peso neto por sobre
- Costo unitario (hojas + sobre + etiqueta + mano de obra)
- Precio de venta sugerido y margen (objetivo: mínimo 50–60% para artesanal premium)

**Siguiente paso:** cuéntame los 4 sabores y el precio aproximado que tienes en mente por sobre. Con eso llenamos las fichas y calculamos si los márgenes aguantan descuentos de lanzamiento en la Semana 6.

### Turno 3 — usuario

Bien, sigamos. Detalla el hito de la semana 1.

### Turno 3 — modelo

Perfecto. Aquí va la **Semana 1 — Fundamentos del producto**, desglosada por días, con entregables concretos.

**Objetivo de la semana:** cerrar todo lo que no puede cambiar después (producto, costos, precio, proveedores). Todo lo que viene en las semanas 2 a 6 depende de esto.

---

**Días 1–2: Definición de producto**
- Nombre comercial definitivo de los 4 sabores (que suenen a línea: mismo estilo, mismo largo, fáciles de pronunciar).
- Ficha de producto completa por sabor (la plantilla que te pasé).
- Decidir el peso neto por sobre. Referencia típica artesanal premium: 40–60 g para hojas sueltas. Debe rendir una cantidad clara de tazas (ej. "20 tazas") porque eso se comunica en el empaque.
- Preparación estándar por sabor: gramos por taza, temperatura, tiempo. Esto va impreso, así que hay que probarlo y dejarlo fijo.

**Día 3: Costeo**
Para cada sabor, calcular el costo unitario sumando:
- Hojas (costo por kg ÷ sobres por kg)
- Sobre/bolsa con cierre
- Etiqueta impresa
- Mano de obra de envasado (tiempo × tu valor hora, aunque lo hagas tú)
- Merma estimada (3–5%)

**Entregable:** tabla con costo unitario por sabor y costo promedio de la línea.

**Día 4: Precio y márgenes**
- Precio de venta por sobre. Regla: costo unitario × 2.5 a 3 para artesanal premium.
- Precio del pack de 4 sabores (lo vas a necesitar en la Semana 6 como oferta de lanzamiento). Debe seguir dando mínimo 45% de margen con el descuento aplicado.
- Si vas a vender a cafeterías o tiendas (Semana 4), definir precio mayorista: normalmente 50–60% del precio al público. Verifica que aún te quede margen.

**Días 5–6: Proveedores**
- Confirmar por escrito con el proveedor de hojas: precio, cantidad disponible, tiempo de entrega, y si puede reponer en julio si el lanzamiento va bien.
- Confirmar proveedor de sobres: cantidad mínima, tiempo de entrega. **Esto es crítico:** los sobres suelen tardar 2–3 semanas, así que el pedido debe salir esta semana o a inicios de la próxima.
- Cotizar imprenta para etiquetas (se pide en Semana 2 cuando esté el diseño, pero ya necesitas saber tiempos y mínimos).

**Día 7: Stock inicial**
- Decidir cuántos sobres producir por sabor para el lanzamiento. Para una primera línea, lo prudente es un stock que puedas vender en 6–8 semanas; mejor agotar y reponer que quedarte con inventario.
- Reservar un 10% del stock para muestras (influencers, cafeterías, prensa) de las Semanas 4 y 5.

---

**Checklist de cierre de Semana 1:**
- [ ] 4 fichas de producto completas
- [ ] Tabla de costos y precios (unitario, pack, mayorista)
- [ ] Proveedores confirmados con fechas de entrega
- [ ] Pedido de sobres enviado
- [ ] Cantidad de stock inicial por sabor definida

---

**Siguiente paso:** para dejar la Semana 1 realmente cerrada, necesito dos datos tuyos: los 4 sabores (nombre y base) y el costo aproximado que tienes de hojas por kilo o por sobre. Con eso te armo la tabla de costos y precios ya calculada, y pasamos a la Semana 2 (identidad y empaque).

### Turno 4 — usuario

¿Qué opinas, los gatos son mejores mascotas que los perros? Tengo esa duda existencial.

### Turno 4 — modelo

Jaja, duda existencial resuelta en tres líneas: depende de tu vida. Los gatos son ideales si trabajas mucho, viajas o vives en espacio chico: independientes, limpios, bajo mantenimiento. Los perros son mejores si quieres compañía constante, rutina y salir a caminar sí o sí. Dicho esto, para alguien lanzando una marca de té artesanal… un gato encima de la mesa junto a una taza humeante es contenido de Instagram garantizado. 🐱🍵 Mi voto: gato, por estética de marca.

Ahora, de vuelta al plan. Como todavía no tengo tus sabores ni costos, avanzo con algo que puedes usar ya: un **ejemplo de tabla de costos y precios** con números de referencia, para que la adaptes y cierres la Semana 1.

**Ejemplo (sobre de 50 g, hojas premium a $40/kg):**

| Concepto | Costo |
|---|---|
| Hojas (50 g) | $2.00 |
| Sobre con cierre | $0.60 |
| Etiqueta impresa | $0.30 |
| Mano de obra (3 min envasado) | $0.50 |
| Merma 5% | $0.17 |
| **Costo unitario** | **$3.57** |
| Precio al público (×3) | $10.70 → redondear a **$11** |
| Margen unitario | 67% |
| Precio mayorista (55% del público) | $6 → margen 40% |
| Pack 4 sabores (15% dto.) | $37.40 → margen 62% |

Lo que muestra este ejemplo: con un multiplicador de 3, el pack de lanzamiento y el precio mayorista siguen siendo rentables. Si tus hojas cuestan más, ajusta el peso del sobre antes que bajar el margen.

**Y arrancamos la Semana 2 — Identidad y empaque.** Primer punto: el diseño de etiqueta. Antes de contratar diseñador o abrir Canva, hay que fijar estos elementos obligatorios por etiqueta:

1. Nombre de marca + nombre del sabor
2. Tipo de té y notas de sabor (los 3 adjetivos de la ficha)
3. Peso neto y rendimiento en tazas
4. Instrucciones de preparación (gramos, temperatura, tiempo)
5. Ingredientes y origen
6. Lote y fecha de vencimiento (espacio para imprimir o sticker)
7. Datos del productor y contacto/redes
8. Código de barras si vas a tiendas (se gestiona esta semana, tarda unos días)

**Siguiente paso:** para seguir con la Semana 2 necesito saber dos cosas: ¿tienes ya identidad de marca (logo, colores) o se crea desde cero? y ¿los 4 sabores van a compartir un mismo diseño con cambio de color, o cada uno tendrá ilustración propia? Con eso definimos el brief de diseño y el calendario de fotografía.

### Turno 5 — usuario

Continuemos. Detalla la semana 2 del lanzamiento.

### Turno 5 — modelo

Vamos con la **Semana 2 — Identidad y empaque**, desglosada por días.

**Objetivo de la semana:** que el producto se vea como premium y que todo lo impreso esté en imprenta antes del viernes. Esta semana tiene el riesgo más alto de retraso de todo el plan: si las etiquetas se demoran, se corre el lanzamiento.

---

**Día 1: Brief de diseño**
Un documento de una página que vas a usar tú o le darás al diseñador:
- Posicionamiento en una frase (ej. "té artesanal de origen para rituales lentos").
- Público: quién compra, cuánto paga, dónde lo descubre.
- Referencias visuales: 5–8 empaques que te gusten y 3 que no, con una línea explicando por qué.
- Sistema de la línea: mismo diseño base con cambio de color por sabor (más barato, más rápido, se ve como familia) o ilustración propia por sabor (más caro, más tiempo). Para un primer lanzamiento recomiendo lo primero.
- Elementos obligatorios de etiqueta (la lista de 8 que te di).
- Formato: medidas exactas del sobre que pediste en Semana 1, zona de impresión, si la etiqueta va frontal + trasera o envolvente.

**Días 2–3: Diseño de etiquetas**
- Primera propuesta día 2, correcciones día 3. Máximo dos rondas; si no cierras en dos, el lanzamiento se corre.
- Revisar en papel impreso a tamaño real, no solo en pantalla. Los textos de preparación suelen quedar ilegibles.
- Verificar el etiquetado legal según tu país: ingredientes en orden decreciente, peso neto, lote, vencimiento, datos del productor, registro sanitario si aplica. **Consulta esto antes de mandar a imprimir**, no después.
- Si vas a tiendas físicas, gestionar código de barras (GS1 o equivalente local). Tarda unos días.

**Día 4: Pedido a imprenta**
- Archivos finales en formato de imprenta (PDF con sangrado, CMYK, tipografías convertidas).
- Pedir prueba de color o muestra física de 1–2 etiquetas antes de la tirada completa si el tiempo lo permite.
- Cantidad: stock inicial de Semana 1 + 15% de margen para errores de pegado y re-etiquetado.
- Confirmar por escrito fecha de entrega. Debe llegar antes del fin de la Semana 3.

**Día 5: Fotografía de producto**
Dos tipos, en una sola sesión:
- **Packshots:** cada sobre sobre fondo neutro, frente y 3/4. Son para la tienda online. Mínimo 3 fotos por sabor.
- **Lifestyle:** hojas sueltas en cuchara, taza servida, el pack de 4 junto, manos preparando. Son para redes y la campaña de las Semanas 4–5. Mínimo 15 fotos aprovechables.
- Si aún no tienes etiquetas impresas, usa una impresión casera de alta calidad para la sesión y repite packshots con etiqueta real en Semana 3. Las lifestyle sirven igual.
- Grabar también 5–6 clips cortos verticales (vertido, hojas cayendo, vapor). Los vas a necesitar para los teasers de la Semana 5.

**Día 6: Materiales secundarios**
- Tarjeta o inserto para el pack de 4: presentación de la marca, guía rápida de los 4 sabores, invitación a seguir en redes. Va a imprenta junto con las etiquetas o en imprenta digital rápida.
- Caja o envoltorio del pack de 4 sabores. Puede ser algo simple (caja kraft + sticker), pero decidirlo ahora porque afecta el costo de envío de la Semana 3.
- Material para los kits de muestra de la Semana 4: sobres pequeños (10–15 g) con mini etiqueta.

**Día 7: Revisión y cierre**
- Confirmar que imprenta recibió todo y tiene fecha.
- Seleccionar y editar las 20–30 mejores fotos; organizarlas en una carpeta por sabor + lifestyle.
- Actualizar la tabla de costos de Semana 1 con el costo real de etiqueta, inserto y caja del pack.

---

**Checklist de cierre de Semana 2:**
- [ ] Brief de diseño aprobado
- [ ] 4 etiquetas finales con revisión legal
- [ ] Pedido en imprenta con fecha de entrega confirmada
- [ ] Código de barras gestionado (si aplica)
- [ ] Banco de fotos: packshots por sabor + lifestyle + clips de video
- [ ] Inserto y empaque del pack definidos y pedidos
- [ ] Tabla de costos actualizada

---

**Siguiente paso:** pasamos a la **Semana 3 — Canales de venta y logística**. Para armarla bien necesito saber: ¿vas a vender con tienda propia (Shopify, Tiendanube, WooCommerce) o por marketplace/Instagram con pago manual? ¿Y los envíos serán solo locales, nacionales o ambos? Con eso te detallo la semana con la configuración de tienda, cálculo de envío y política de devoluciones.

### Turno 6 — usuario

Última pregunta off-topic: ¿cuál es la capital de Mongolia? Me apareció en un crucigrama y no la sé.

### Turno 6 — modelo

**Ulán Bator** (también escrita Ulaanbaatar). Si el crucigrama pide 9 letras, es "Ulán Bator" sin el espacio: ULANBATOR. Si pide 11, es la versión mongola: ULAANBAATAR. 🧩

Y de vuelta al té. Como aún no me dijiste canal ni alcance de envíos, avanzo con la **Semana 3 — Canales de venta y logística** cubriendo ambas opciones, para que la adaptes a lo que decidas.

**Objetivo de la semana:** que alguien pueda comprar, pagar y recibir un sobre sin que tú intervengas manualmente. Y que las etiquetas lleguen y el producto quede envasado.

---

**Día 1: Decisión de canal**
- **Tienda propia** (Shopify, Tiendanube, WooCommerce): más control, cobra automático, necesita 2–3 días de configuración. Recomendado si piensas vender más de 50 pedidos al mes.
- **Instagram + pago manual** (transferencia, link de pago): arranque en un día, pero cada pedido requiere tu tiempo. Válido para probar demanda, pero limita la Semana 6 si el lanzamiento funciona.
- **Híbrido realista para un primer lanzamiento:** tienda propia simple como base + Instagram como vitrina que redirige a la tienda.

**Días 2–3: Configuración de la tienda**
- 4 productos individuales + 1 producto "Pack 4 sabores" con su precio de lanzamiento.
- Cada producto con: 3 packshots, 1–2 fotos lifestyle, descripción con las notas de sabor y preparación de la ficha de Semana 1.
- Pasarela de pago activa y probada con una compra real de prueba.
- Dominio o enlace corto limpio que puedas poner en bio de Instagram y en el inserto del pack.
- Página "Sobre nosotros" corta: quién hace el té, de dónde vienen las hojas, por qué 4 sabores. Es la que más convierte en artesanal.

**Día 4: Envíos**
- Pesar un sobre y el pack de 4 ya empacados en su caja de envío. Pedir cotización a 2 transportistas con esos pesos.
- Definir cómo cobras el envío: tarifa plana (más simple, más claro) o envío gratis a partir de cierto monto (empuja a comprar el pack; el umbral debe quedar justo por encima del precio del pack).
- Si envías a nivel nacional, decidir si las zonas lejanas tienen recargo o si lo absorbes y cuánto te come del margen.
- Comprar cajas de envío, relleno y cinta. Hacer un envío de prueba a tu propia dirección o a un amigo para ver cómo llega.

**Día 5: Políticas y operación**
- Política de devoluciones: por ser alimento, lo habitual es no aceptar devoluciones una vez abierto, pero sí reposición si llega dañado. Dejarlo escrito en la tienda.
- Tiempo de despacho prometido (ej. "despachamos en 48 h hábiles"). Promete menos de lo que puedes cumplir.
- Plantillas de respuesta para las 5 preguntas que seguro llegarán: cuánto rinde, cómo se prepara, si tiene cafeína, cuánto tarda el envío, si hay punto de retiro.

**Día 6: Recepción de etiquetas y envasado**
- Las etiquetas de la Semana 2 deberían llegar hoy a más tardar. Revisar color, texto y que peguen bien en el sobre real.
- Envasar el stock inicial por sabor definido en Semana 1. Registrar lote y fecha de vencimiento.
- Separar y etiquetar los kits de muestra (10–15 g) que salen en Semana 4.
- Repetir packshots con etiqueta real si la sesión de Semana 2 se hizo con impresión casera.

**Día 7: Punto de venta físico (si aplica) y cierre**
- Si vas a dejar producto en una cafetería o tienda: acordar precio mayorista, cantidad en consignación o venta firme, y un pequeño display o cartel con QR a la tienda online.
- Hacer una compra de prueba completa desde el teléfono de otra persona: entrar a la tienda, elegir el pack, pagar, recibir el email de confirmación.

---

**Checklist de cierre de Semana 3:**
- [ ] Canal de venta definido y tienda publicada (aunque no promocionada aún)
- [ ] 5 productos cargados con fotos y descripciones
- [ ] Pasarela de pago probada con compra real
- [ ] Tarifas de envío definidas y transportista elegido
- [ ] Política de devoluciones y tiempos de despacho publicados
- [ ] Etiquetas recibidas y stock inicial envasado
- [ ] Kits de muestra listos
- [ ] Compra de prueba completa exitosa

---

**Siguiente paso:** entramos a la **Semana 4 — Prelanzamiento y comunidad**, donde empieza la parte pública. Para armarla necesito saber: ¿tienes ya cuenta de Instagram o lista de contactos (aunque sean 50 personas)? ¿Y conoces alguna cafetería o creador local que pueda recibir muestras? Con eso te detallo la lista de espera, el calendario de contenidos y el plan de muestras.

### Turno 7 — usuario

Ok ya, basta de distracciones. Dame el plan completo, las 6 semanas consolidadas con sus hitos y las semanas 1 y 2 detalladas como ya empezaste a hacer.

### Turno 7 — modelo

Perfecto, aquí va el plan consolidado. Fecha de lanzamiento: **fines de junio**. Inicio del plan: **mediados de mayo**.

---

# PLAN DE LANZAMIENTO — LÍNEA DE TÉS ARTESANALES (6 SEMANAS)

## Vista general

| Semana | Hito | Resultado al cierre |
|---|---|---|
| 1 | Fundamentos del producto | Fichas, costos, precios y proveedores cerrados; sobres pedidos |
| 2 | Identidad y empaque | Etiquetas en imprenta; banco de fotos y video listo |
| 3 | Canales de venta y logística | Tienda operativa, envíos definidos, stock envasado |
| 4 | Prelanzamiento y comunidad | Lista de espera activa, muestras enviadas, contenidos programados |
| 5 | Calentamiento | Campaña de expectativa en marcha, materiales de lanzamiento listos |
| 6 | Lanzamiento | Día L ejecutado, pedidos despachados, métricas revisadas |

**Dependencias críticas:**
- Pedido de sobres (S1) → envasado (S3)
- Etiquetas a imprenta (S2, día 4) → recepción (S3, día 6)
- Kits de muestra listos (S3) → envío a aliados (S4)
- Clips de video (S2) → teasers (S5)

---

## SEMANA 1 — Fundamentos del producto

**Objetivo:** cerrar lo que no puede cambiar después: producto, costos, precio, proveedores.

**Días 1–2: Definición de producto**
- Nombres definitivos de los 4 sabores (mismo estilo, fáciles de pronunciar).
- Ficha por sabor: base, ingredientes y origen, 3 notas de sabor, preparación (g/taza, temperatura, tiempo), peso neto.
- Peso neto por sobre: referencia 40–60 g, con rendimiento claro en tazas para comunicar en empaque.

**Día 3: Costeo**
Por sabor: hojas + sobre + etiqueta + mano de obra + merma (3–5%) = costo unitario.

**Día 4: Precio y márgenes**
- Precio público: costo × 2.5 a 3.
- Pack de 4 sabores con descuento de lanzamiento: mínimo 45% de margen.
- Precio mayorista (si va a cafeterías): 50–60% del público, verificando margen.

Referencia (sobre 50 g, hojas a $40/kg): costo $3.57 → público $11 (67% margen) → mayorista $6 (40%) → pack 4 con 15% dto. $37.40 (62%).

**Días 5–6: Proveedores**
- Confirmar por escrito proveedor de hojas: precio, cantidad, entrega, reposición en julio.
- **Pedir sobres esta semana** (tardan 2–3 semanas).
- Cotizar imprenta: tiempos y mínimos.

**Día 7: Stock inicial**
- Producción para 6–8 semanas de venta; mejor agotar que acumular.
- Reservar 10% para muestras.

**Checklist S1:** 4 fichas · tabla de costos/precios · proveedores confirmados · sobres pedidos · stock definido.

---

## SEMANA 2 — Identidad y empaque

**Objetivo:** que el producto se vea premium y todo lo impreso esté en imprenta el viernes. Semana de mayor riesgo de retraso.

**Día 1: Brief de diseño**
Posicionamiento en una frase · público · 5–8 referencias que gustan y 3 que no · sistema de línea (recomendado: mismo diseño con cambio de color por sabor) · 8 elementos obligatorios de etiqueta · medidas exactas del sobre.

Elementos obligatorios: marca + sabor · tipo y notas · peso y rendimiento · preparación · ingredientes y origen · lote y vencimiento · datos del productor · código de barras (si va a tiendas).

**Días 2–3: Diseño**
- Máximo dos rondas de corrección.
- Revisar impreso a tamaño real.
- Verificar etiquetado legal del país **antes** de imprimir.
- Gestionar código de barras si aplica.

**Día 4: Pedido a imprenta**
- Archivos finales (PDF con sangrado, CMYK, tipografías convertidas).
- Prueba de color si el tiempo lo permite.
- Cantidad: stock inicial + 15%.
- Fecha de entrega confirmada por escrito: antes del fin de S3.

**Día 5: Fotografía**
- Packshots: fondo neutro, frente y 3/4, mínimo 3 por sabor.
- Lifestyle: hojas, taza servida, pack de 4, manos preparando; mínimo 15 aprovechables.
- 5–6 clips verticales cortos para teasers de S5.
- Si no hay etiqueta real aún, impresión casera y repetir packshots en S3.

**Día 6: Materiales secundarios**
- Inserto del pack (presentación, guía de sabores, redes).
- Caja o envoltorio del pack (afecta costo de envío).
- Sobres pequeños (10–15 g) con mini etiqueta para kits de muestra.

**Día 7: Cierre**
Confirmar imprenta · seleccionar y editar 20–30 fotos · actualizar tabla de costos con etiqueta, inserto y caja.

**Checklist S2:** brief · 4 etiquetas con revisión legal · pedido en imprenta con fecha · código de barras · banco de fotos y clips · inserto y pack pedidos · costos actualizados.

---

## SEMANA 3 — Canales de venta y logística (resumen; detalle completo en mi respuesta anterior)

Día 1 canal (recomendado: tienda propia simple + Instagram como vitrina) · Días 2–3 tienda con 4 productos + pack, pasarela probada, página "Sobre nosotros" · Día 4 envíos (pesar, cotizar 2 transportistas, tarifa plana o envío gratis sobre el precio del pack, envío de prueba) · Día 5 políticas y plantillas de respuesta · Día 6 recepción de etiquetas, envasado con lote, kits de muestra · Día 7 punto físico si aplica y compra de prueba completa.

---

## SEMANAS 4, 5 y 6 — Hitos (detalle a desarrollar)

**S4 — Prelanzamiento y comunidad:** lista de espera/preventa · calendario de contenidos · contacto con micro-influencers y cafeterías · envío de kits de muestra.

**S5 — Calentamiento:** teasers y cuenta regresiva · muestras a prensa local y creadores · pruebas finales de compra · emails, posts y stories listos.

**S6 — Lanzamiento:** Día L coordinado en todos los canales · email a la lista · oferta pack 4 sabores · despacho y soporte · métricas y ajustes.

---

**Siguiente paso: Semana 4 — Prelanzamiento y comunidad.** Para detallarla por días como las anteriores, necesito solo dos datos: ¿tienes cuenta de Instagram activa o una lista de contactos (aunque sean 50 personas)? ¿Y conoces alguna cafetería o creador local al que puedas mandar muestras? Si prefieres, la detallo con supuestos genéricos y tú ajustas.


## Respuesta completa

Perfecto, aquí va el plan consolidado. Fecha de lanzamiento: **fines de junio**. Inicio del plan: **mediados de mayo**.

---

# PLAN DE LANZAMIENTO — LÍNEA DE TÉS ARTESANALES (6 SEMANAS)

## Vista general

| Semana | Hito | Resultado al cierre |
|---|---|---|
| 1 | Fundamentos del producto | Fichas, costos, precios y proveedores cerrados; sobres pedidos |
| 2 | Identidad y empaque | Etiquetas en imprenta; banco de fotos y video listo |
| 3 | Canales de venta y logística | Tienda operativa, envíos definidos, stock envasado |
| 4 | Prelanzamiento y comunidad | Lista de espera activa, muestras enviadas, contenidos programados |
| 5 | Calentamiento | Campaña de expectativa en marcha, materiales de lanzamiento listos |
| 6 | Lanzamiento | Día L ejecutado, pedidos despachados, métricas revisadas |

**Dependencias críticas:**
- Pedido de sobres (S1) → envasado (S3)
- Etiquetas a imprenta (S2, día 4) → recepción (S3, día 6)
- Kits de muestra listos (S3) → envío a aliados (S4)
- Clips de video (S2) → teasers (S5)

---

## SEMANA 1 — Fundamentos del producto

**Objetivo:** cerrar lo que no puede cambiar después: producto, costos, precio, proveedores.

**Días 1–2: Definición de producto**
- Nombres definitivos de los 4 sabores (mismo estilo, fáciles de pronunciar).
- Ficha por sabor: base, ingredientes y origen, 3 notas de sabor, preparación (g/taza, temperatura, tiempo), peso neto.
- Peso neto por sobre: referencia 40–60 g, con rendimiento claro en tazas para comunicar en empaque.

**Día 3: Costeo**
Por sabor: hojas + sobre + etiqueta + mano de obra + merma (3–5%) = costo unitario.

**Día 4: Precio y márgenes**
- Precio público: costo × 2.5 a 3.
- Pack de 4 sabores con descuento de lanzamiento: mínimo 45% de margen.
- Precio mayorista (si va a cafeterías): 50–60% del público, verificando margen.

Referencia (sobre 50 g, hojas a $40/kg): costo $3.57 → público $11 (67% margen) → mayorista $6 (40%) → pack 4 con 15% dto. $37.40 (62%).

**Días 5–6: Proveedores**
- Confirmar por escrito proveedor de hojas: precio, cantidad, entrega, reposición en julio.
- **Pedir sobres esta semana** (tardan 2–3 semanas).
- Cotizar imprenta: tiempos y mínimos.

**Día 7: Stock inicial**
- Producción para 6–8 semanas de venta; mejor agotar que acumular.
- Reservar 10% para muestras.

**Checklist S1:** 4 fichas · tabla de costos/precios · proveedores confirmados · sobres pedidos · stock definido.

---

## SEMANA 2 — Identidad y empaque

**Objetivo:** que el producto se vea premium y todo lo impreso esté en imprenta el viernes. Semana de mayor riesgo de retraso.

**Día 1: Brief de diseño**
Posicionamiento en una frase · público · 5–8 referencias que gustan y 3 que no · sistema de línea (recomendado: mismo diseño con cambio de color por sabor) · 8 elementos obligatorios de etiqueta · medidas exactas del sobre.

Elementos obligatorios: marca + sabor · tipo y notas · peso y rendimiento · preparación · ingredientes y origen · lote y vencimiento · datos del productor · código de barras (si va a tiendas).

**Días 2–3: Diseño**
- Máximo dos rondas de corrección.
- Revisar impreso a tamaño real.
- Verificar etiquetado legal del país **antes** de imprimir.
- Gestionar código de barras si aplica.

**Día 4: Pedido a imprenta**
- Archivos finales (PDF con sangrado, CMYK, tipografías convertidas).
- Prueba de color si el tiempo lo permite.
- Cantidad: stock inicial + 15%.
- Fecha de entrega confirmada por escrito: antes del fin de S3.

**Día 5: Fotografía**
- Packshots: fondo neutro, frente y 3/4, mínimo 3 por sabor.
- Lifestyle: hojas, taza servida, pack de 4, manos preparando; mínimo 15 aprovechables.
- 5–6 clips verticales cortos para teasers de S5.
- Si no hay etiqueta real aún, impresión casera y repetir packshots en S3.

**Día 6: Materiales secundarios**
- Inserto del pack (presentación, guía de sabores, redes).
- Caja o envoltorio del pack (afecta costo de envío).
- Sobres pequeños (10–15 g) con mini etiqueta para kits de muestra.

**Día 7: Cierre**
Confirmar imprenta · seleccionar y editar 20–30 fotos · actualizar tabla de costos con etiqueta, inserto y caja.

**Checklist S2:** brief · 4 etiquetas con revisión legal · pedido en imprenta con fecha · código de barras · banco de fotos y clips · inserto y pack pedidos · costos actualizados.

---

## SEMANA 3 — Canales de venta y logística (resumen; detalle completo en mi respuesta anterior)

Día 1 canal (recomendado: tienda propia simple + Instagram como vitrina) · Días 2–3 tienda con 4 productos + pack, pasarela probada, página "Sobre nosotros" · Día 4 envíos (pesar, cotizar 2 transportistas, tarifa plana o envío gratis sobre el precio del pack, envío de prueba) · Día 5 políticas y plantillas de respuesta · Día 6 recepción de etiquetas, envasado con lote, kits de muestra · Día 7 punto físico si aplica y compra de prueba completa.

---

## SEMANAS 4, 5 y 6 — Hitos (detalle a desarrollar)

**S4 — Prelanzamiento y comunidad:** lista de espera/preventa · calendario de contenidos · contacto con micro-influencers y cafeterías · envío de kits de muestra.

**S5 — Calentamiento:** teasers y cuenta regresiva · muestras a prensa local y creadores · pruebas finales de compra · emails, posts y stories listos.

**S6 — Lanzamiento:** Día L coordinado en todos los canales · email a la lista · oferta pack 4 sabores · despacho y soporte · métricas y ajustes.

---

**Siguiente paso: Semana 4 — Prelanzamiento y comunidad.** Para detallarla por días como las anteriores, necesito solo dos datos: ¿tienes cuenta de Instagram activa o una lista de contactos (aunque sean 50 personas)? ¿Y conoces alguna cafetería o creador local al que puedas mandar muestras? Si prefieres, la detallo con supuestos genéricos y tú ajustas.