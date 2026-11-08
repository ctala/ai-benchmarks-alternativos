# Claude Fable 5.1 — agent_long_horizon/implicit_state_construction

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.62 | quality: 8.5
- latency_total: 174.543s | tokens_per_second: 74.3
- input_tokens: 24859 | output_tokens: 11682

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Hola, Camila. Sí, me queda claro el contexto. Te lo resumo para confirmar que lo tengo bien:

**Tu negocio:**
- Tienda online en Colombia
- Mercado actual: Bogotá (único por ahora)

**Tus tres productos:**
1. **Aurora** – set de cuidado facial, precio premium
2. **Sol** – kit de maquillaje natural, precio medio
3. **Luna** – crema corporal, precio entrada

**Competidores principales (ambos en Bogotá):**
- Botica Verde
- Skin Lab

Lo tengo guardado. Cuando me hables de "el producto premium", "la crema", "tu competidor X" o "tu ciudad", sabré a qué te refieres. ¿Por dónde quieres empezar con la planificación de campañas?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Aquí tienes una propuesta de valor general, basada en lo que me contaste (asumo que el eje de "natural" de Sol aplica a toda la marca; si no es así, ajustamos):

**Propuesta de valor:**

1. Somos una marca colombiana de belleza que ofrece una rutina completa —rostro, maquillaje y cuerpo— con productos que combinan ingredientes naturales y resultados visibles, para que cuides tu piel sin elegir entre eficacia y naturalidad.

2. Con tres niveles de precio (Luna, Sol y Aurora), cualquier persona en Bogotá puede empezar con nosotros y crecer en su rutina a su propio ritmo, con entrega directa y sin intermediarios.

**Por qué esta estructura:** la primera oración define *qué eres y qué prometes*; la segunda convierte tu escalera de precios en un diferenciador frente a Botica Verde y Skin Lab, posicionándote como marca accesible pero con techo premium.

¿Quieres que la afine hacia un tono más emocional, más técnico, o que la adapte a un producto en particular?

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Para una tienda online de belleza en Bogotá, con tres productos en distintos niveles de precio, priorizaría así:

**Prioridad 1 – Instagram**
Es el canal natural para belleza en Colombia: visual, con Reels para demostraciones y Stories para interacción diaria. Úsalo como tu "vitrina principal". Ideal para Sol (maquillaje se vende viendo el resultado) y para construir la imagen aspiracional de Aurora.

**Prioridad 2 – TikTok**
Mayor alcance orgánico a bajo costo y donde más crecen las marcas de cuidado de la piel. Perfecto para Luna como producto de entrada: contenido tipo "antes/después", texturas, rutinas rápidas. Es el canal donde más fácil puedes ganarle visibilidad a Botica Verde y Skin Lab sin gran presupuesto.

**Prioridad 3 – WhatsApp Business**
En Colombia es clave para cerrar ventas: catálogo, respuesta a dudas, seguimiento de pedidos y recompra. Muchas clientas bogotanas prefieren confirmar por WhatsApp antes de pagar en línea.

**Prioridad 4 – Meta Ads (Instagram/Facebook) con segmentación geográfica en Bogotá**
Como tu mercado es solo Bogotá, puedes concentrar todo el presupuesto pagado ahí y lograr costos por resultado muy eficientes. Empieza con campañas de tráfico hacia Luna (menor fricción de compra) y retargeting hacia Sol y Aurora.

**Prioridad 5 – Google (Shopping + búsqueda de marca)**
Secundario por ahora, pero útil para captar a quien ya busca "crema corporal Bogotá" o compara con tus competidores. Y asegúrate de tener Google Business Profile aunque seas solo online.

**Lo que dejaría para después:** email marketing (vale la pena cuando tengas base de clientas), YouTube largo, y marketplaces como Mercado Libre (podrían canibalizar tu margen premium en Aurora).

**Regla práctica:** TikTok e Instagram para *atraer*, WhatsApp para *convertir*, Meta Ads para *escalar*.

¿Quieres que arme un plan de contenido semanal para los dos canales prioritarios, o que definamos presupuesto para Meta Ads?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Te doy una frecuencia realista para una emprendedora que probablemente gestiona esto sola o con un equipo pequeño. Mejor consistencia sostenible que un arranque fuerte que no puedas mantener.

**Instagram (vitrina principal)**
- **Reels:** 3 a 4 por semana. Es lo que más alcance te da. Alterna entre tus tres productos: por ejemplo, lunes Luna (textura/rutina rápida), miércoles Sol (demostración de maquillaje), viernes Aurora (resultado/ritual premium).
- **Posts en feed (carrusel o foto):** 2 por semana. Úsalos para contenido que "se queda": beneficios de ingredientes, comparativas de tu escalera de precios, testimonios.
- **Stories:** todos los días, 3 a 5 por día. Aquí va lo informal: detrás de cámaras, encuestas, preguntas, reposts de clientas, recordatorios de promos. Es tu canal de confianza diaria con las bogotanas.

**TikTok (alcance y descubrimiento)**
- **Videos:** 4 a 5 por semana, idealmente 1 al día de lunes a viernes. El algoritmo premia volumen y no castiga la imperfección, así que no necesitas producción alta. Luna debería llevarse la mayor parte aquí: es tu gancho de entrada y el que más fácil se viraliza con "antes/después" y texturas.
- Reutiliza: casi todo Reel sirve como TikTok y viceversa. Graba una vez, publica en ambos.

**WhatsApp Business (conversión y recompra)**
- **Estados:** 3 a 4 por semana. Novedades, stock, promos cortas. No más, porque cansa.
- **Mensajes de difusión (broadcast):** máximo 2 al mes a tu base de clientas. Reserva uno para lanzamientos o descuentos y otro para contenido de valor (tips de uso). Más que eso y te bloquean.
- **Catálogo:** actualizado siempre que cambie precio o stock de Aurora, Sol o Luna.

**Google Business Profile**
- 1 publicación por semana con oferta, novedad o foto de producto. Poco esfuerzo, pero ayuda a aparecer cuando alguien busca "cuidado facial Bogotá" y te compara con Botica Verde o Skin Lab.

**Resumen semanal aproximado:**
- Instagram: 3–4 Reels + 2 posts + Stories diarias
- TikTok: 4–5 videos (reciclados de los Reels en gran parte)
- WhatsApp: 3–4 estados + 2 difusiones al mes
- Google Business: 1 post

**Dos consejos para que sea viable:**
1. Dedica un día a grabar en lote (batch): en 3 horas sacas contenido para toda la semana con tus tres productos.
2. Si tienes que recortar, mantén las Stories diarias y los Reels/TikToks; sacrifica primero los posts de feed.

¿Quieres que convierta esto en un calendario semanal concreto, con el tema de cada pieza asignado a Aurora, Sol o Luna?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para skincare, el contenido que mejor funciona es el que **demuestra** (no el que afirma). En tu caso aplica sobre todo a Aurora y Luna; Sol entra parcialmente porque "maquillaje natural" se vende también como cuidado de la piel.

**1. Antes / después y resultados en el tiempo**
Es el formato que más convierte en skincare. Muestra piel real, con buena luz y sin filtros, a los 7, 14 y 30 días. Para Aurora, documenta un "reto de 30 días" con una clienta bogotana: justifica el precio premium con evidencia. Para Luna, bastan resultados inmediatos (hidratación, brillo) grabados en el momento.

**2. Texturas y aplicación (ASMR / satisfying)**
Primeros planos de la crema extendiéndose, el sérum cayendo, el producto absorbiéndose. Funciona muy bien en TikTok y Reels, especialmente para Luna, que es tu producto más "sensorial" y fácil de viralizar.

**3. Rutinas paso a paso**
"Mi rutina de mañana / noche" con Aurora como protagonista. Enseña el orden, la cantidad y el tiempo entre pasos. Puedes cerrar con Luna para el cuerpo y mostrar la rutina completa de tu marca.

**4. Educación sobre ingredientes y tipos de piel**
Explicar qué hace cada ingrediente (y qué *no* hace) genera confianza y te posiciona como experta frente a Botica Verde y Skin Lab. Formato carrusel en Instagram: "3 ingredientes de Aurora y por qué están ahí", "¿Tu piel es grasa, mixta o seca? Así eliges". Incluye el contexto local: clima de Bogotá (altura, sol fuerte, aire seco), que afecta la piel y es un ángulo que tus competidores probablemente no explotan.

**5. Mitos y errores comunes**
"5 errores que cometes al aplicar crema corporal", "Esto no es acné, es…". Alta tasa de guardados y compartidos, y te permite introducir Luna o Aurora como solución sin vender de frente.

**6. Testimonios y contenido generado por clientas (UGC)**
Videos reales de clientas usando el producto, con su voz, en su baño o su cuarto. Es el contenido más creíble para un precio premium como Aurora. Pide a quien compre que te envíe un video corto a cambio de un descuento en su próxima compra (ideal: Luna → Sol → Aurora, siguiendo tu escalera).

**7. Detrás de cámaras y origen**
Cómo se produce, por qué elegiste esos ingredientes, tu historia como emprendedora colombiana. Humaniza la marca y la diferencia de competidores más "clínicos" como Skin Lab.

**8. Comparativas y "cuál me conviene"**
"¿Luna o Aurora? Depende de esto". Ayuda a decidir, reduce dudas por WhatsApp y empuja hacia el producto de mayor valor cuando corresponde.

**Lo que funciona menos:** fotos de producto solo sobre fondo bonito, textos largos de beneficios sin demostración, y promesas tipo "elimina arrugas" (además de ser poco creíbles, pueden traerte problemas regulatorios con el INVIMA).

**Mezcla sugerida por semana:** 40 % demostración (texturas, antes/después, rutinas), 30 % educación (ingredientes, mitos, tipo de piel), 20 % testimonios/UGC, 10 % marca y detrás de cámaras.

¿Quieres que te arme 10 ideas concretas de video listas para grabar, separadas por Aurora, Sol y Luna?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Buena pregunta, porque con Luna a precio de entrada es tentador competir bajando, y con Aurora premium es donde más te dolería. Las guerras de precio las gana quien tiene más margen o más capital, y probablemente ni Botica Verde ni Skin Lab ni tú quieren eso. La diferenciación tiene que venir de otro lado:

**1. Posiciónate como "la rutina completa", no como productos sueltos**
Tu ventaja estructural es tener rostro (Aurora), maquillaje (Sol) y cuerpo (Luna). Vende el *sistema*: "una sola marca para todo tu cuidado". Crea combos (Luna + Sol, o el "ritual completo" con los tres) con un valor percibido mayor que la suma de las partes, sin descontar cada producto por separado. Así compites en *valor por rutina*, no en precio por unidad.

**2. Apropiate de un territorio que tus competidores no ocupen**
Observa cómo se presentan Botica Verde (el nombre sugiere "herbolario/natural") y Skin Lab ("científico/clínico"). Tú puedes ocupar el punto medio que ninguno domina: **natural con resultados visibles**, o un ángulo local muy concreto: **piel adaptada al clima de Bogotá** (altura, radiación, sequedad). Ese posicionamiento es específico, defendible y no depende del precio.

**3. Usa la escalera de precios como estrategia, no como descuento**
Luna no es un producto barato: es la *puerta de entrada* a tu marca. Diseña el recorrido Luna → Sol → Aurora: quien compra Luna recibe una muestra o un beneficio para probar Sol; quien compra Sol recibe un incentivo para Aurora. Vendes más por clienta sin tocar el precio de lista de ninguno.

**4. Experiencia y servicio que ellos no dan**
- Asesoría personalizada por WhatsApp: "¿qué tipo de piel tienes?" → recomendación concreta. Para una compra premium como Aurora, eso vale más que un 10 % de descuento.
- Empaque y unboxing memorable, con una nota escrita o instrucciones de uso.
- Entrega en Bogotá rápida y confiable (mismo día o 24 h), que es algo que una marca enfocada en una sola ciudad puede prometer mejor que un competidor más grande.
- Seguimiento posventa: mensaje a los 7 días preguntando cómo va.

**5. Garantía y confianza en lugar de descuento**
"Si Aurora no te gusta en 15 días, te cambiamos por Sol o Luna". Reduce el riesgo percibido del precio premium y te posiciona como marca segura de su producto. Suena caro, pero las devoluciones reales suelen ser muy bajas.

**6. Comunidad y contenido como activo**
Educación constante (como vimos: ingredientes, mitos, rutinas) hace que la gente te siga *antes* de comprarte. Cuando confían en ti, el precio deja de ser la primera variable. Ni Botica Verde ni Skin Lab pueden copiarte la relación que construyes con tu audiencia.

**7. Programa de fidelidad y recompra**
Puntos, "compra 3 Luna y la cuarta va con regalo", acceso anticipado a lanzamientos para clientas frecuentes. Premias la lealtad, no la oportunidad; eso es muy distinto de regalar margen a cualquiera.

**8. Tu historia como fundadora**
Una marca con rostro y origen (Camila, emprendedora colombiana) genera una conexión que una empresa anónima no logra. Es gratis y es irrepetible.

**Qué evitar:**
- Responder a cada promo de ellos con una tuya: entrena a tu clienta a esperar descuentos.
- Comparaciones directas de precio en tu contenido: te mete en su terreno.
- Bajar Aurora "para probar": una vez baja el precio percibido del premium, es muy difícil recuperarlo.

**Regla simple:** si alguna vez usas descuento, que sea *con condición* (primera compra, combo, fidelidad, fecha específica) y nunca como precio permanente.

¿Quieres que definamos el posicionamiento específico en una frase (el "territorio" del punto 2) y el diseño del recorrido Luna → Sol → Aurora?

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para un primer trimestre, el error común es medir demasiado. Te propongo un set corto, organizado por etapa del embudo (atraer → convertir → retener), alineado con los canales que definimos. La meta del trimestre no es optimizar todo, sino **establecer tu línea base** para comparar después.

**1. Atracción (Instagram y TikTok)**
- **Alcance mensual** (cuentas únicas alcanzadas), no seguidores. Los seguidores son vanidad; el alcance te dice si el contenido está saliendo de tu círculo.
- **Tasa de guardados y compartidos** por pieza. En skincare, un contenido guardado vale más que un like: indica intención. Úsalo para saber qué formatos (texturas de Luna, rutinas con Aurora, demos de Sol) repetir.
- **Crecimiento de seguidores** como dato secundario, solo para detectar picos y entender qué los causó.

**2. Interés (tráfico y conversaciones)**
- **Clics al enlace / visitas a la tienda** desde cada canal. Es el primer indicador de que el contenido mueve a la acción.
- **Conversaciones iniciadas por WhatsApp** por semana. En tu modelo, WhatsApp es donde se cierra la venta, así que este número es tu "pipeline".
- **Tasa de respuesta y tiempo de respuesta** en WhatsApp. Si tardas más de una hora en horario comercial, pierdes ventas, sobre todo de Aurora, donde la clienta duda más.

**3. Conversión (ventas)**
- **Número de pedidos** y **ventas totales** por mes. Obvio, pero sepáralo por producto: cuántos Luna, cuántos Sol, cuántos Aurora.
- **Tasa de conversión de WhatsApp a pedido** (pedidos ÷ conversaciones). Te dice si el problema está en atraer gente o en cerrar.
- **Ticket promedio**. Es el KPI que más te interesa vigilar si no quieres competir por precio: debe subir conforme funcionen los combos y el recorrido Luna → Sol → Aurora.
- **Mix de ventas por producto**: qué porcentaje de ingresos viene de cada uno. Si Luna es el 80 % de los pedidos pero el 30 % del ingreso, sabes que tu trabajo del segundo trimestre es empujar la escalera.

**4. Eficiencia de pauta (Meta Ads)**
- **CPM y CPC** en tu segmentación de Bogotá, para saber cuánto te cuesta llegar y traer tráfico.
- **Costo por conversación de WhatsApp** o **costo por compra**, según el objetivo de campaña. Este es el número que decide si escalas presupuesto.
- **ROAS** (ingresos ÷ gasto en pauta). En el primer trimestre no esperes maravillas; busca que mejore mes a mes.

**5. Retención (desde el mes 2)**
- **Tasa de recompra**: de quienes compraron en el mes 1, cuántas vuelven en los meses 2 o 3. Con una crema corporal como Luna, la recompra natural debería aparecer a los 30–45 días.
- **Clientas que suben de escalón**: cuántas pasaron de Luna a Sol o de Sol a Aurora. Pocas al inicio, pero es el dato que valida tu estrategia de diferenciación.
- **Testimonios/UGC recibidos**: cuántos videos o reseñas conseguiste. Es un KPI de contenido, pero alimenta directamente las ventas de Aurora.

**6. Un KPI de mercado (opcional, cualitativo)**
- **Menciones y búsquedas de marca**: si alguien ya busca tu nombre en Google o te menciona en Stories, estás empezando a existir junto a Botica Verde y Skin Lab en la mente de la bogotana. No necesitas herramienta cara: revisa Google Search Console y las menciones en Instagram.

**Cómo organizarlo**
- **Semanal** (15 minutos): conversaciones WhatsApp, pedidos, tiempo de respuesta, mejor pieza de contenido.
- **Mensual** (1 hora): todo lo demás, en una hoja de cálculo simple con una fila por mes.
- **Al cierre del trimestre:** compara mes 1 vs. mes 3 en ticket promedio, tasa de conversión y costo por compra. Esas tres líneas te dicen si la estrategia va bien.

**Los 5 que miraría si solo pudieras mirar 5:** conversaciones de WhatsApp, tasa de conversión a pedido, ticket promedio, mix por producto y costo por compra en Meta Ads.

**Qué no medir todavía:** likes, número de publicaciones, LTV (aún no tienes histórico) ni comparaciones con benchmarks de la industria; tu primera referencia válida eres tú misma en el mes 1.

¿Quieres que te arme la plantilla de la hoja de cálculo con estas métricas y columnas por Aurora, Sol y Luna?

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Tu producto más caro es **Aurora**, el set de cuidado facial premium. Aquí va el plan de 4 semanas.

---

## Campaña: "30 días con Aurora"

**Concepto:** Aurora no se vende con descuento, se vende con evidencia. La campaña gira alrededor de un reto público de 30 días en el que mostramos resultados reales en piel bogotana, y usamos ese contenido para justificar el precio premium y convertir.

---

### Objetivo

**Principal:** Vender un número definido de unidades de Aurora en 4 semanas sin bajar su precio de lista. Fija la cifra según tu capacidad: si hoy vendes, por ejemplo, 10 Aurora al mes, la meta razonable es duplicar (20) durante la campaña.

**Secundarios:**
- Posicionar a Aurora como el producto "insignia" de tu marca, por encima de Luna y Sol en percepción, no solo en precio.
- Generar un banco de testimonios y UGC de Aurora que sirva después de la campaña.
- Subir el ticket promedio de la tienda empujando clientas actuales de Luna y Sol hacia Aurora.

---

### Audiencia

**Segmento 1 – Clientas actuales de Luna y Sol (prioridad alta)**
Ya confían en ti; el salto a Aurora es menos riesgoso para ellas. Es el grupo con mayor probabilidad de compra y menor costo de adquisición.

**Segmento 2 – Mujeres en Bogotá, 28 a 45 años, interesadas en skincare**
Con capacidad de pago para un producto premium y preocupación concreta por su piel: resequedad, manchas por el sol de altura, primeras líneas de expresión. Intereses en Meta: cuidado facial, sérum, rutinas de skincare, marcas de dermocosmética.

**Segmento 3 – Audiencia de retargeting**
Quienes visitaron la página de Aurora, interactuaron con contenido de Aurora o escribieron por WhatsApp sin comprar en los últimos 60 días.

**Segmento 4 – Seguidoras o interesadas en Botica Verde y Skin Lab** (secundario)
No las atacas de frente; las captas con contenido comparativo de valor ("natural con resultados visibles") y el ángulo del clima bogotano.

---

### Mensaje principal

**Idea central:** *"Aurora: la rutina facial pensada para la piel de Bogotá, con resultados que se ven en 30 días."*

**Tres pilares que sostienen el mensaje:**
1. **Evidencia:** antes/después reales, sin filtros, documentados semana a semana.
2. **Contexto local:** altura, radiación y aire seco de Bogotá; Aurora responde a eso. Es un territorio que ni Botica Verde ni Skin Lab ocupan.
3. **Riesgo cero:** "Si Aurora no te convence en 15 días, te lo cambiamos por Sol o Luna." Elimina la objeción del precio sin tocar el precio.

**Tono:** seguro, cercano, sin promesas médicas (nada de "elimina arrugas"; sí "piel más hidratada, luminosa y uniforme").

---

### Canales y rol de cada uno

- **Instagram:** canal principal de la narrativa. Reels con el reto, carruseles educativos sobre los ingredientes de Aurora, Stories diarias con avances.
- **TikTok:** alcance frío. Texturas de Aurora, rutina paso a paso, "por qué cuesta lo que cuesta" (desglose honesto del valor).
- **WhatsApp Business:** conversión. Difusión a clientas actuales, asesoría personalizada por tipo de piel, cierre de venta.
- **Meta Ads (solo Bogotá):** amplificación del mejor contenido orgánico y retargeting.
- **Google Business Profile:** 1 publicación semanal de Aurora para captar búsquedas tipo "cuidado facial Bogotá".

---

### Plan semana a semana

**Semana 1 – Lanzamiento del reto y calentamiento**
- Anuncia el "Reto 30 días con Aurora": tú misma (o 2–3 clientas voluntarias) lo empiezan públicamente. Foto base de piel día 0.
- Contenido: Reel de presentación de Aurora y por qué existe; carrusel "Qué hace cada producto del set Aurora"; TikTok de texturas.
- WhatsApp: difusión #1 a clientas de Luna y Sol: "Estás invitada a probar Aurora con garantía de cambio de 15 días." Incluye un beneficio de transición no monetario (ej. muestra de Luna de regalo o envío prioritario), no descuento.
- Meta Ads: campaña de alcance/tráfico a Segmentos 2 y 4 con el Reel de presentación. Presupuesto bajo, para aprender.
- Google Business: post de lanzamiento de Aurora.

**Semana 2 – Educación y autoridad**
- Contenido: "Lo que el clima de Bogotá le hace a tu piel y cómo Aurora lo compensa"; "3 mitos sobre skincare premium"; "¿Luna, Sol o Aurora? Cuál te conviene según tu piel"; Stories con el avance del día 7 del reto.
- WhatsApp: estado con el primer avance del reto; en cada conversación, pregunta tipo de piel antes de recomendar.
- Meta Ads: activa retargeting (Segmento 3) con el carrusel educativo; mantén la campaña fría con el contenido que mejor rindió en la semana 1.
- Pide a las primeras compradoras de Aurora que envíen un video corto de su primera aplicación.

**Semana 3 – Prueba social y empuje**
- Contenido: resultados del día 14 del reto (antes/después real); primeros testimonios de Aurora; Reel "Por qué Aurora cuesta lo que cuesta" (ingredientes, concentración, tamaño, proceso).
- WhatsApp: difusión #2 con el antes/después del día 14 y recordatorio de la garantía. Seguimiento a quienes preguntaron en semana 1 y no compraron.
- Meta Ads: sube presupuesto en el conjunto de anuncios con menor costo por conversación; usa el antes/después como creativo principal.
- Lanza el combo "Ritual completo" (Aurora + Sol + Luna) con valor agregado (ej. estuche o guía de rutina), para subir el ticket sin descontar Aurora.

**Semana 4 – Cierre y conversión final**
- Contenido: compilado del reto (día 0 vs. día 30 cuando aplique, o día 21), testimonios en bloque, Stories en vivo respondiendo preguntas sobre Aurora.
- Mensaje de cierre con **condición de tiempo**, no de precio: "La garantía ampliada de 15 días en Aurora aplica para compras hasta el [fecha]."
- WhatsApp: mensajes personalizados uno a uno a todas las conversaciones abiertas sobre Aurora.
- Meta Ads: concentra todo el presupuesto restante en retargeting y en clientas de Luna/Sol (lista de clientes subida a Meta).
- Google Business: post de cierre con testimonio.

---

### Frecuencia durante la campaña
- Instagram: 4 Reels/semana (al menos 3 sobre Aurora) + 2 posts + Stories diarias con el reto.
- TikTok: 5 videos/semana, 4 sobre Aurora.
- WhatsApp: 2 difusiones en el mes (semanas 1 y 3) + estados 3 veces por semana.
- Luna y Sol no desaparecen: aparecen como "puerta" hacia Aurora o como parte del combo.

---

### Métricas de éxito

**Resultado (al cierre de la campaña):**
- Unidades de Aurora vendidas vs. meta fijada (ej. 20).
- Ingresos por Aurora y participación de Aurora en el total de ventas del mes (meta: que suba frente a tu línea base del trimestre).
- Ticket promedio del mes vs. mes anterior (meta: aumento claro gracias a Aurora y al combo).
- Clientas de Luna/Sol que compraron Aurora (meta orientativa: 30–40 % de las ventas de Aurora deberían venir de este grupo).

**Proceso (semanal):**
- Conversaciones de WhatsApp que mencionan Aurora.
- Tasa de conversión de conversación sobre Aurora a pedido.
- Tiempo de respuesta en WhatsApp (meta: menos de 1 hora en horario comercial).
- Costo por conversación y costo por compra de Aurora en Meta Ads, semana a semana (deben bajar de la semana 1 a la 4).
- ROAS de la campaña de Aurora.

**Contenido:**
- Guardados y compartidos de las piezas de Aurora (indicador de intención).
- Alcance de las piezas del reto en Bogotá.
- Testimonios y videos UGC de Aurora recibidos (meta: mínimo 5 utilizables).

**Señales de alerta para corregir en marcha:**
- Muchas conversaciones y pocas ventas → objeción de precio o de confianza: refuerza garantía y testimonios, revisa el guion de WhatsApp.
- Mucho alcance y pocas conversaciones → el llamado a la acción no está claro: haz más explícito el "escríbenos por WhatsApp".
- Costo por compra alto en frío pero bajo en retargeting → mueve presupuesto al retargeting y a clientas actuales.

---

### Qué no hacer en esta campaña
- Descontar Aurora. Toda la campaña está diseñada para que no sea necesario.
- Comparar precios con Botica Verde o Skin Lab.
- Prometer resultados médicos.
- Dejar conversaciones de WhatsApp sin cerrar más de 24 horas.

¿Quieres que escriba los guiones de las dos difusiones de WhatsApp y el guion de respuesta para cuando alguien pregunte "¿por qué Aurora es tan caro?"?


## Respuesta completa

Tu producto más caro es **Aurora**, el set de cuidado facial premium. Aquí va el plan de 4 semanas.

---

## Campaña: "30 días con Aurora"

**Concepto:** Aurora no se vende con descuento, se vende con evidencia. La campaña gira alrededor de un reto público de 30 días en el que mostramos resultados reales en piel bogotana, y usamos ese contenido para justificar el precio premium y convertir.

---

### Objetivo

**Principal:** Vender un número definido de unidades de Aurora en 4 semanas sin bajar su precio de lista. Fija la cifra según tu capacidad: si hoy vendes, por ejemplo, 10 Aurora al mes, la meta razonable es duplicar (20) durante la campaña.

**Secundarios:**
- Posicionar a Aurora como el producto "insignia" de tu marca, por encima de Luna y Sol en percepción, no solo en precio.
- Generar un banco de testimonios y UGC de Aurora que sirva después de la campaña.
- Subir el ticket promedio de la tienda empujando clientas actuales de Luna y Sol hacia Aurora.

---

### Audiencia

**Segmento 1 – Clientas actuales de Luna y Sol (prioridad alta)**
Ya confían en ti; el salto a Aurora es menos riesgoso para ellas. Es el grupo con mayor probabilidad de compra y menor costo de adquisición.

**Segmento 2 – Mujeres en Bogotá, 28 a 45 años, interesadas en skincare**
Con capacidad de pago para un producto premium y preocupación concreta por su piel: resequedad, manchas por el sol de altura, primeras líneas de expresión. Intereses en Meta: cuidado facial, sérum, rutinas de skincare, marcas de dermocosmética.

**Segmento 3 – Audiencia de retargeting**
Quienes visitaron la página de Aurora, interactuaron con contenido de Aurora o escribieron por WhatsApp sin comprar en los últimos 60 días.

**Segmento 4 – Seguidoras o interesadas en Botica Verde y Skin Lab** (secundario)
No las atacas de frente; las captas con contenido comparativo de valor ("natural con resultados visibles") y el ángulo del clima bogotano.

---

### Mensaje principal

**Idea central:** *"Aurora: la rutina facial pensada para la piel de Bogotá, con resultados que se ven en 30 días."*

**Tres pilares que sostienen el mensaje:**
1. **Evidencia:** antes/después reales, sin filtros, documentados semana a semana.
2. **Contexto local:** altura, radiación y aire seco de Bogotá; Aurora responde a eso. Es un territorio que ni Botica Verde ni Skin Lab ocupan.
3. **Riesgo cero:** "Si Aurora no te convence en 15 días, te lo cambiamos por Sol o Luna." Elimina la objeción del precio sin tocar el precio.

**Tono:** seguro, cercano, sin promesas médicas (nada de "elimina arrugas"; sí "piel más hidratada, luminosa y uniforme").

---

### Canales y rol de cada uno

- **Instagram:** canal principal de la narrativa. Reels con el reto, carruseles educativos sobre los ingredientes de Aurora, Stories diarias con avances.
- **TikTok:** alcance frío. Texturas de Aurora, rutina paso a paso, "por qué cuesta lo que cuesta" (desglose honesto del valor).
- **WhatsApp Business:** conversión. Difusión a clientas actuales, asesoría personalizada por tipo de piel, cierre de venta.
- **Meta Ads (solo Bogotá):** amplificación del mejor contenido orgánico y retargeting.
- **Google Business Profile:** 1 publicación semanal de Aurora para captar búsquedas tipo "cuidado facial Bogotá".

---

### Plan semana a semana

**Semana 1 – Lanzamiento del reto y calentamiento**
- Anuncia el "Reto 30 días con Aurora": tú misma (o 2–3 clientas voluntarias) lo empiezan públicamente. Foto base de piel día 0.
- Contenido: Reel de presentación de Aurora y por qué existe; carrusel "Qué hace cada producto del set Aurora"; TikTok de texturas.
- WhatsApp: difusión #1 a clientas de Luna y Sol: "Estás invitada a probar Aurora con garantía de cambio de 15 días." Incluye un beneficio de transición no monetario (ej. muestra de Luna de regalo o envío prioritario), no descuento.
- Meta Ads: campaña de alcance/tráfico a Segmentos 2 y 4 con el Reel de presentación. Presupuesto bajo, para aprender.
- Google Business: post de lanzamiento de Aurora.

**Semana 2 – Educación y autoridad**
- Contenido: "Lo que el clima de Bogotá le hace a tu piel y cómo Aurora lo compensa"; "3 mitos sobre skincare premium"; "¿Luna, Sol o Aurora? Cuál te conviene según tu piel"; Stories con el avance del día 7 del reto.
- WhatsApp: estado con el primer avance del reto; en cada conversación, pregunta tipo de piel antes de recomendar.
- Meta Ads: activa retargeting (Segmento 3) con el carrusel educativo; mantén la campaña fría con el contenido que mejor rindió en la semana 1.
- Pide a las primeras compradoras de Aurora que envíen un video corto de su primera aplicación.

**Semana 3 – Prueba social y empuje**
- Contenido: resultados del día 14 del reto (antes/después real); primeros testimonios de Aurora; Reel "Por qué Aurora cuesta lo que cuesta" (ingredientes, concentración, tamaño, proceso).
- WhatsApp: difusión #2 con el antes/después del día 14 y recordatorio de la garantía. Seguimiento a quienes preguntaron en semana 1 y no compraron.
- Meta Ads: sube presupuesto en el conjunto de anuncios con menor costo por conversación; usa el antes/después como creativo principal.
- Lanza el combo "Ritual completo" (Aurora + Sol + Luna) con valor agregado (ej. estuche o guía de rutina), para subir el ticket sin descontar Aurora.

**Semana 4 – Cierre y conversión final**
- Contenido: compilado del reto (día 0 vs. día 30 cuando aplique, o día 21), testimonios en bloque, Stories en vivo respondiendo preguntas sobre Aurora.
- Mensaje de cierre con **condición de tiempo**, no de precio: "La garantía ampliada de 15 días en Aurora aplica para compras hasta el [fecha]."
- WhatsApp: mensajes personalizados uno a uno a todas las conversaciones abiertas sobre Aurora.
- Meta Ads: concentra todo el presupuesto restante en retargeting y en clientas de Luna/Sol (lista de clientes subida a Meta).
- Google Business: post de cierre con testimonio.

---

### Frecuencia durante la campaña
- Instagram: 4 Reels/semana (al menos 3 sobre Aurora) + 2 posts + Stories diarias con el reto.
- TikTok: 5 videos/semana, 4 sobre Aurora.
- WhatsApp: 2 difusiones en el mes (semanas 1 y 3) + estados 3 veces por semana.
- Luna y Sol no desaparecen: aparecen como "puerta" hacia Aurora o como parte del combo.

---

### Métricas de éxito

**Resultado (al cierre de la campaña):**
- Unidades de Aurora vendidas vs. meta fijada (ej. 20).
- Ingresos por Aurora y participación de Aurora en el total de ventas del mes (meta: que suba frente a tu línea base del trimestre).
- Ticket promedio del mes vs. mes anterior (meta: aumento claro gracias a Aurora y al combo).
- Clientas de Luna/Sol que compraron Aurora (meta orientativa: 30–40 % de las ventas de Aurora deberían venir de este grupo).

**Proceso (semanal):**
- Conversaciones de WhatsApp que mencionan Aurora.
- Tasa de conversión de conversación sobre Aurora a pedido.
- Tiempo de respuesta en WhatsApp (meta: menos de 1 hora en horario comercial).
- Costo por conversación y costo por compra de Aurora en Meta Ads, semana a semana (deben bajar de la semana 1 a la 4).
- ROAS de la campaña de Aurora.

**Contenido:**
- Guardados y compartidos de las piezas de Aurora (indicador de intención).
- Alcance de las piezas del reto en Bogotá.
- Testimonios y videos UGC de Aurora recibidos (meta: mínimo 5 utilizables).

**Señales de alerta para corregir en marcha:**
- Muchas conversaciones y pocas ventas → objeción de precio o de confianza: refuerza garantía y testimonios, revisa el guion de WhatsApp.
- Mucho alcance y pocas conversaciones → el llamado a la acción no está claro: haz más explícito el "escríbenos por WhatsApp".
- Costo por compra alto en frío pero bajo en retargeting → mueve presupuesto al retargeting y a clientas actuales.

---

### Qué no hacer en esta campaña
- Descontar Aurora. Toda la campaña está diseñada para que no sea necesario.
- Comparar precios con Botica Verde o Skin Lab.
- Prometer resultados médicos.
- Dejar conversaciones de WhatsApp sin cerrar más de 24 horas.

¿Quieres que escriba los guiones de las dos difusiones de WhatsApp y el guion de respuesta para cuando alguien pregunte "¿por qué Aurora es tan caro?"?