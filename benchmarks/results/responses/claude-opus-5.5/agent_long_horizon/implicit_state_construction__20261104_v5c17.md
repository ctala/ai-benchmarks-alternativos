# Claude Opus 5.5 — agent_long_horizon/implicit_state_construction

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.79 | quality: 8.5
- latency_total: 159.408s | tokens_per_second: 107.6
- input_tokens: 29650 | output_tokens: 15752

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola, Camila! Sí, me queda claro. Este es el resumen de tu negocio:

**Tienda online en Colombia**, con Bogotá como único mercado por ahora.

**Productos:**
| Producto | Categoría | Rango de precio |
|---|---|---|
| **Aurora** | Set de cuidado facial | Premium |
| **Sol** | Kit de maquillaje natural | Medio |
| **Luna** | Crema corporal | Entrada |

**Competidores principales (ambos en Bogotá):**
- Botica Verde
- Skin Lab

Tienes una escalera de precios clara. **Luna** puede atraer clientes nuevos, **Sol** puede ser el producto intermedio y **Aurora** el de mayor margen. Eso abre opciones interesantes, como estrategias de *upselling* o paquetes combinados.

¿En qué quieres empezar a trabajar? Por ejemplo:
- Una campaña para un producto específico
- Una estrategia de diferenciación frente a Botica Verde y Skin Lab
- Un calendario de campañas por temporada (Amor y Amistad, Navidad, etc.)
- Ideas para redes sociales o pauta digital en Bogotá

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Aquí tienes una propuesta basada en lo que me contaste:

> **Cuidamos tu piel de pies a cabeza con una rutina completa de rostro, maquillaje y cuerpo pensada para el clima de Bogotá, con opciones para cada presupuesto, desde Luna hasta Aurora. Compras online, recibes en casa y encuentras en un solo lugar productos que funcionan juntos, sin tener que armar tu rutina con marcas distintas.**

**Por qué funciona:**
- **Rutina integral:** Ofreces rostro, maquillaje y cuerpo. Eso te diferencia si Botica Verde o Skin Lab se concentran en una sola categoría.
- **Bogotá:** Hablar del frío, la altura y la radiación UV de la ciudad crea cercanía y relevancia local.
- **Escalera de precios:** Deja ver que hay una puerta de entrada accesible (Luna) y un camino hacia el producto premium (Aurora).

**Supuestos que conviene validar:** No sé aún qué te diferencia concretamente de Botica Verde y Skin Lab. ¿Es lo natural (como sugiere Sol), los ingredientes, el origen colombiano, la asesoría personalizada o la rapidez de entrega? Si me lo dices, puedo afinar la propuesta para que sea más precisa y difícil de copiar.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Te recomiendo priorizar estos canales, en este orden, pensando en tu mercado en Bogotá y en tus tres niveles de precio:

### 1. Instagram (prioridad alta)
Es la principal vitrina de belleza en Colombia.
- **Reels** con antes y después, rutinas y texturas de producto.
- **Stories** con encuestas y preguntas para generar conversación.
- **Pauta geolocalizada** solo en Bogotá, para no desperdiciar presupuesto en otras ciudades.
- **Ideal para:** Aurora y Sol, que necesitan mostrar resultados visuales.

### 2. TikTok (prioridad alta)
Ofrece alcance orgánico barato y funciona muy bien con contenido de rutinas tipo *"Get Ready With Me"*.
- Contenido local y cercano, por ejemplo: *"Así protejo mi piel del frío bogotano"*.
- **Ideal para:** Luna y Sol, que tienen un precio de entrada accesible y favorecen la compra impulsiva.

### 3. WhatsApp Business (prioridad alta)
En Colombia es el canal de cierre de venta por excelencia.
- Catálogo con tus tres productos.
- Asesoría personalizada, clave para justificar el precio premium de Aurora.
- Mensajes de recompra y de *upselling* (de Luna a Sol, y de Sol a Aurora).

### 4. Google Search y Shopping (prioridad media)
Captura a quien ya está buscando.
- Palabras clave como *"crema corporal Bogotá"*, *"set facial"* o *"maquillaje natural"*.
- Pujar también por términos relacionados con **Botica Verde** y **Skin Lab** (revisa antes las políticas de marca de Google).

### 5. Microinfluenciadoras bogotanas (prioridad media)
Busca perfiles de 5.000 a 50.000 seguidores. Generan más confianza y cuestan menos que las grandes cuentas.
- Empieza con canje de producto (Luna o Sol) antes de invertir en pagos.

### 6. Email marketing (prioridad para fidelizar)
Úsalo para la recompra y para promociones de temporada. Es barato y se vuelve más valioso a medida que crece tu base de clientes.

### Recomendación práctica
Si tus recursos son limitados, **arranca con Instagram, TikTok y WhatsApp**: atraes en redes y cierras en WhatsApp. Además, revisa en la **Biblioteca de Anuncios de Meta** qué pautas están corriendo Botica Verde y Skin Lab. Así sabrás qué mensajes usan y dónde puedes diferenciarte.

Para afinar esta priorización me serviría conocer el perfil de tu cliente ideal (edad y estilo de vida). Por ejemplo, si tu público es mayor de 35, Facebook y el email ganan peso frente a TikTok.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Esta frecuencia es **realista para un equipo pequeño**. La constancia importa más que el volumen: es mejor publicar 3 veces por semana durante seis meses que 7 veces por semana durante un mes y luego desaparecer.

### Frecuencia recomendada por canal

| Canal | Frecuencia ideal | Mínimo sostenible |
|---|---|---|
| **Instagram: Reels** | 3-4 por semana | 2 por semana |
| **Instagram: Stories** | Diario (3-5 por día) | 4 días por semana |
| **Instagram: Carruseles/posts** | 1-2 por semana | 1 por semana |
| **TikTok** | 4-5 por semana | 3 por semana |
| **WhatsApp: Estados** | Diario | 3 por semana |
| **WhatsApp: Listas de difusión** | 1 por semana | Cada 15 días |
| **Email** | 1 cada 15 días | 1 al mes |

**Google** y las **microinfluenciadoras** no requieren publicación orgánica tuya, así que no aparecen en la tabla.

### Ejemplo de semana tipo

| Día | Instagram | TikTok | WhatsApp |
|---|---|---|---|
| **Lunes** | Reel: rutina facial con **Aurora** | Mismo video adaptado | Estado: tip de piel |
| **Martes** | Stories: encuesta | Tendencia + **Luna** | Estado |
| **Miércoles** | Carrusel educativo (ej. "Cómo afecta el frío bogotano a tu piel") | GRWM con **Sol** | Difusión semanal |
| **Jueves** | Reel: textura de **Luna** | Respuesta a comentarios | Estado: testimonio |
| **Viernes** | Reel: look con **Sol** | Contenido de fin de semana | Estado: promo |
| **Fin de semana** | Stories ligeras o descanso | 1 video opcional | — |

### Claves para que sea sostenible
- **Reutiliza:** un mismo video sirve para Reels, TikTok y Estados de WhatsApp, con ajustes mínimos de texto y audio.
- **Graba en bloque:** dedica medio día cada semana o cada quince días a grabar todo el contenido.
- **Rota los productos:** reparte el protagonismo entre Aurora, Sol y Luna. Una buena guía es dedicar el 40 % del contenido a educar sobre cuidado de la piel en Bogotá, el 40 % a mostrar los productos y el 20 % a vender de forma directa.
- **No satures WhatsApp:** más de una difusión por semana aumenta los bloqueos, y eso afecta tu canal de cierre de ventas.

### Ajusta con datos
Después de **4 a 6 semanas**, revisa qué formatos y productos generan más guardados, compartidos y mensajes a WhatsApp. Sube la frecuencia donde haya respuesta y bájala donde no la haya. También vale la pena observar con qué frecuencia publican Botica Verde y Skin Lab, para no quedarte muy por debajo en visibilidad.

¿Quieres que convierta esto en un calendario mensual con ideas concretas de contenido para cada producto?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Tus productos de skincare son **Aurora** (facial, premium) y **Luna** (corporal, entrada). Sol es maquillaje, así que lo menciono solo como complemento. En skincare, la clienta no puede tocar ni probar el producto, así que **el contenido tiene que reemplazar la experiencia en tienda**: mostrar textura, explicar por qué funciona y demostrar resultados creíbles.

### 1. Educativo: el que más se guarda y comparte
Posiciona tu marca como experta y justifica el precio de Aurora.
- **Problema + solución local:** *"Por qué tu piel se reseca en Bogotá aunque no haga calor"* o *"La altura y los rayos UV: lo que nadie te cuenta"*.
- **Ingredientes explicados:** qué hace cada activo de Aurora, en lenguaje simple.
- **Mitos vs. realidad:** *"¿Si llueve no necesito protegerme?"*
- **Formato ideal:** carruseles en Instagram y videos cortos hablando a cámara en TikTok.

### 2. Sensorial: texturas y aplicación
Es el contenido que más se acerca a probar el producto.
- Primeros planos de la textura de **Luna** al aplicarla, la absorción y el acabado en la piel.
- Videos tipo *ASMR*: abrir el set **Aurora**, presentación y sonidos.
- **Formato ideal:** Reels y TikTok de 7 a 15 segundos. Funcionan muy bien para la compra impulsiva de Luna.

### 3. Rutinas paso a paso
Muestra cómo se usa y conecta tus productos entre sí.
- *"Mi rutina de noche con Aurora"* (orden, cantidad, tiempos).
- *"Rutina completa: Aurora en el rostro, Luna en el cuerpo y Sol para salir"*. Esto refuerza tu propuesta de valor de rutina integral, de pies a cabeza.
- **Formato ideal:** GRWM en TikTok y Reels.

### 4. Prueba social y resultados reales
Es clave para vender el producto premium.
- Testimonios de clientas bogotanas, idealmente en video.
- **Seguimiento en el tiempo:** *"Día 1 vs. día 30 usando Aurora"*, con la misma luz y el mismo ángulo, sin filtros.
- Capturas de mensajes de WhatsApp de clientas satisfechas (con su permiso).
- Contenido de microinfluenciadoras reutilizado en tus cuentas.

### 5. Detrás de cámaras y cercanía
Humaniza la marca, algo que suele ser difícil de lograr para competidores más grandes.
- Tú, Camila, contando por qué creaste cada producto.
- Empaque de pedidos y envíos por Bogotá.
- Respuestas a preguntas reales de seguidoras.

### Qué tipo de contenido priorizar por producto

| Producto | Contenido prioritario | Objetivo |
|---|---|---|
| **Aurora** | Educativo, ingredientes, resultados a 30 días, testimonios | Generar confianza y justificar el precio premium |
| **Luna** | Texturas, sensorial, tendencias, rutina corporal en clima frío | Atraer clientas nuevas y provocar la compra impulsiva |
| **Sol** (complemento) | Rutinas completas que lo integren con Aurora | *Cross-selling* |

### Errores comunes que debes evitar
- **Prometer resultados médicos** como "elimina manchas" o "cura el acné". En Colombia, los cosméticos están regulados por el **INVIMA**, y las afirmaciones exageradas pueden traerte problemas legales y de credibilidad. Mejor usa frases como "ayuda a hidratar" o "mejora la apariencia".
- **Usar filtros en el contenido de resultados.** Destruye la confianza si alguien lo nota.
- **Atacar a Botica Verde o Skin Lab por nombre.** La publicidad comparativa en Colombia tiene reglas estrictas de la **SIC**. Es mejor diferenciarte resaltando lo tuyo, por ejemplo con *"Lo que buscamos en una crema para el frío bogotano"*, sin mencionar a terceros.
- **Hacer solo contenido de venta.** Mantén la proporción de 40 % educativo, 40 % de producto y 20 % de venta que vimos antes.

### Cómo saber qué funciona
- **Guardados y compartidos** muestran que el contenido educativo está aportando valor.
- **Mensajes a WhatsApp** muestran que el contenido está generando intención de compra.
- **Tiempo de visualización** muestra que los videos sensoriales y las rutinas están enganchando.

¿Quieres que te prepare 10 ideas concretas de contenido listas para grabar, repartidas entre Aurora y Luna?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

La clave es que la clienta **compare valor, no precio**. Si Botica Verde o Skin Lab bajan precios, tú respondes con más valor percibido, no con descuentos. Estas son las palancas que mejor encajan con tu negocio:

### 1. Posiciónate en la rutina integral para Bogotá
Ofreces rostro (**Aurora**), maquillaje (**Sol**) y cuerpo (**Luna**). Esa es tu ventaja estructural.
- **Mensaje central:** *"Tu rutina completa para el clima de Bogotá, en un solo lugar."*
- Si tus competidores se concentran en una sola categoría, tú dejas de competir producto contra producto y compites como solución completa.
- Habla siempre del frío, la altura y la radiación UV. Es un nicho local donde puedes ser referente.

### 2. Arma paquetes en lugar de dar descuentos
Los paquetes suben el ticket promedio sin bajar el precio unitario de cada producto.

| Paquete | Contenido | Para quién |
|---|---|---|
| **Kit de inicio** | Luna + Sol | Clienta nueva que quiere probar la marca |
| **Ritual completo** | Aurora + Sol + Luna | Clienta que busca la rutina de pies a cabeza |
| **Regalo premium** | Aurora + Luna con empaque especial | Fechas como Amor y Amistad, Día de la Madre o Navidad |

**Truco de anclaje:** muestra primero el Ritual completo con Aurora. Al lado, Sol y Luna se perciben más accesibles.

### 3. Ofrece asesoría personalizada por WhatsApp
Es difícil de copiar para una marca grande y justifica el precio de **Aurora**.
- **Mini diagnóstico de piel gratuito:** 4 o 5 preguntas por WhatsApp y una recomendación de rutina.
- Seguimiento a los 15 días: *"¿Cómo va tu piel con Aurora?"*. Genera confianza y abre la puerta a la recompra.

### 4. Diferénciate en la experiencia de compra
- **Entrega rápida en Bogotá**, el mismo día o al día siguiente en ciertas localidades. Al vender en una sola ciudad, puedes prometer algo que una marca nacional no puede.
- **Empaque cuidado** con una nota escrita a mano. Es barato y muy compartible en redes.
- **Muestras estratégicas:** incluye una muestra de Aurora en los pedidos de Luna. Así haces *upselling* sin presionar.

### 5. Reduce el riesgo de comprar
Una **garantía de satisfacción**, como *"Si Aurora no te convence en 30 días, te ayudamos a encontrar otra opción o te devolvemos tu dinero"*, elimina la principal barrera del producto premium: el miedo a pagar caro y que no funcione.

### 6. Fideliza para no depender de atraer clientas nuevas
- **Recordatorio de recompra** por WhatsApp cuando a la clienta se le esté acabando Luna.
- **Escalera de clienta:** quien compra Luna recibe contenido o beneficios para conocer Sol, y luego Aurora.
- **Beneficios en lugar de descuentos:** acceso anticipado a lanzamientos, regalos en la tercera compra o envío gratis para clientas frecuentes.

### 7. Usa tu cara y tu historia
Tú, Camila, contando por qué creaste Aurora, Sol y Luna. Una cadena o una marca más grande difícilmente puede competir con una fundadora cercana que responde mensajes y conoce a sus clientas.

### Si un competidor lanza una promoción agresiva

| En lugar de... | Haz esto |
|---|---|
| Bajar el precio de Aurora | Agregar un regalo, por ejemplo una Luna en tamaño viaje |
| Igualar su descuento | Ofrecer envío gratis o un paquete con más valor |
| Hacer descuentos constantes | Limitar las promociones a fechas clave y por tiempo corto |

**Evita sobre todo descontar Aurora con frecuencia.** Un producto premium que siempre está en promoción deja de percibirse como premium, y eso es muy difícil de recuperar.

### Paso práctico: auditoría rápida de la competencia
Dedica una tarde a revisar a Botica Verde y Skin Lab en sus redes, su web y la Biblioteca de Anuncios de Meta. Anota:
- Qué categorías venden y en qué rangos de precio
- Tiempos y costos de envío
- Tono de comunicación y mensajes principales
- Qué se quejan sus clientas en los comentarios (ahí están tus oportunidades)

Los vacíos que encuentres serán tu diferenciación más fuerte.

**Una pregunta pendiente que haría más precisa esta estrategia:** ¿qué tienen de especial tus productos en sí? Por ejemplo, ingredientes naturales, origen colombiano, formulación para el clima frío o producción artesanal. Con eso puedo ayudarte a construir un mensaje de diferenciación que tus competidores no puedan copiar fácilmente.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

En el primer trimestre el objetivo principal es **establecer tu línea base**: saber de dónde partes, qué canal vende y qué producto funciona como puerta de entrada. Por eso conviene medir **pocos KPIs, pero conectados con la venta**, no solo con la visibilidad.

### 1. KPI principal: ventas por producto
Si solo pudieras mirar un número, sería este.

| KPI | Qué te dice |
|---|---|
| **Ingresos totales y por producto** (Aurora, Sol, Luna) | Qué producto sostiene el negocio |
| **Número de pedidos** | Volumen real de ventas |
| **Ticket promedio** | Si los paquetes y el *upselling* están funcionando |
| **% de pedidos con paquete** (Kit de inicio, Ritual completo) | Si la estrategia de paquetes reemplaza a los descuentos |

### 2. Atracción: Instagram y TikTok
No te quedes con los *likes*. Mide señales de interés real.

| KPI | Por qué importa |
|---|---|
| **Alcance en Bogotá** | Confirma que llegas a tu único mercado, no a otras ciudades |
| **Guardados y compartidos** | Miden el valor del contenido educativo |
| **Tasa de retención de video** | Indica si los videos sensoriales de Luna y las rutinas enganchan |
| **Clics al enlace o a WhatsApp** | Conectan el contenido con la intención de compra |
| **Crecimiento de seguidores** | Es secundario; úsalo solo como referencia |

### 3. Conversión: WhatsApp y tienda online
WhatsApp es tu canal de cierre, así que es donde más atención debes poner.

| KPI | Cómo calcularlo |
|---|---|
| **Conversaciones nuevas por semana** | Total de chats iniciados |
| **Tasa de cierre en WhatsApp** | Ventas ÷ conversaciones |
| **Tiempo de respuesta** | Promedio desde el mensaje hasta tu respuesta (idealmente en minutos, no horas) |
| **Tasa de conversión de la web** | Pedidos ÷ visitas |
| **Origen de cada venta** | Pregunta o etiqueta: Instagram, TikTok, Google, influenciadora o recomendación |

**Tip práctico:** usa las **etiquetas de WhatsApp Business** (por ejemplo, "Lead TikTok", "Diagnóstico Aurora" o "Cliente Luna") para saber qué canal y qué producto genera cada conversación.

### 4. Rentabilidad de la pauta
Solo aplica si inviertes en anuncios en Meta, TikTok o Google.

| KPI | Para qué sirve |
|---|---|
| **Costo por adquisición (CPA)** por producto | Comprobar que no pagas más por conseguir una clienta de Luna de lo que te deja la venta |
| **ROAS** (ingresos ÷ inversión) | Saber qué campañas escalar y cuáles apagar |
| **Costo por conversación de WhatsApp** | Mide la eficiencia de los anuncios que dirigen al chat |

Ten especial cuidado con **Luna**: al ser de precio de entrada, su CPA debe ser bajo, o su valor debe recuperarse con la recompra o el paso a Sol y Aurora.

### 5. Fidelización: tu ventaja frente a la guerra de precios
En tres meses verás apenas las primeras señales, pero conviene empezar a medirlas desde ya.

| KPI | Qué te dice |
|---|---|
| **Tasa de recompra** | Qué % de clientas compra por segunda vez |
| **Escalera de clienta** | Cuántas clientas pasan de Luna a Sol o Aurora |
| **Conversión de muestras** | Cuántas clientas que recibieron una muestra de Aurora terminaron comprándolo |
| **Respuesta al seguimiento de 15 días** | Mide el engagement posventa |
| **Devoluciones o uso de la garantía** | Indica si Aurora cumple lo que promete |

### 6. Influenciadoras y email
- **Microinfluenciadoras:** ventas o conversaciones generadas por cada una. Usa un **código o enlace único** por perfil.
- **Email:** tasa de apertura, clics y ventas atribuidas a cada envío.

### Cómo organizar el trimestre

| Mes | Enfoque |
|---|---|
| **Mes 1** | Medir la línea base, sin juzgar todavía. Configura etiquetas, códigos y la hoja de seguimiento. |
| **Mes 2** | Comparar canales y productos. Detecta qué contenido y qué canal traen ventas, no solo vistas. |
| **Mes 3** | Optimizar. Sube la inversión y la frecuencia donde hay retorno, recorta donde no, y fija metas para el segundo trimestre. |

### Rutina de revisión
- **Semanal (15 minutos):** ventas, conversaciones de WhatsApp, tasa de cierre y gasto en pauta.
- **Mensual (1 hora):** todos los KPIs, comparación entre productos y canales, y decisiones de ajuste.
- **Trimestral:** repite la auditoría de Botica Verde y Skin Lab para ver si cambiaron precios, mensajes o promociones.

### Errores que conviene evitar
- **Medir demasiado:** con 8 a 10 KPIs bien seguidos es suficiente.
- **Obsesionarte con seguidores:** una cuenta pequeña con buena tasa de cierre en WhatsApp vale más que una grande que no vende.
- **No registrar el origen de cada venta:** sin ese dato no sabrás qué canal priorizar en el segundo trimestre.

¿Quieres que te arme una **plantilla de seguimiento en Google Sheets** con estos KPIs organizados por semana y por producto? Si me cuentas tus ventas mensuales actuales aproximadas, también puedo ayudarte a proponer metas realistas para el trimestre.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

# Campaña "Ritual Aurora": 4 semanas para tu set facial premium

**Producto:** Aurora, set de cuidado facial, precio premium
**Mercado:** Bogotá
**Principio clave:** Aurora no se descuenta. Se vende con confianza, asesoría y reducción del riesgo.

## 1. Objetivo

**Objetivo principal:** Aumentar las ventas de Aurora en Bogotá y posicionarlo como el set facial de referencia para el clima de la ciudad, sin bajar su precio.

**Objetivos específicos:**
1. Generar conversaciones calificadas sobre Aurora por WhatsApp mediante el diagnóstico de piel gratuito.
2. Convertir esas conversaciones en ventas de Aurora con asesoría personalizada.
3. Crear una base de testimonios y resultados reales de Aurora que siga sirviendo después de la campaña.

## 2. Audiencia

| Segmento | Descripción | Por qué es clave para Aurora |
|---|---|---|
| **Principal: nuevas clientas** | Mujeres en Bogotá que ya invierten en skincare, buscan resultados y valoran la asesoría | Pueden pagar un precio premium si confían en el producto |
| **Caliente: clientas actuales** | Quienes ya compraron Luna o Sol | Conocen tu marca, así que Aurora es su siguiente paso natural |
| **Retargeting** | Quienes vieron videos de Aurora, visitaron su página o escribieron por WhatsApp sin comprar | Ya mostraron interés y necesitan un empujón de confianza |

**Supuesto por validar:** asumo un rango de 25 a 45 años. Si tu clienta real es mayor de 35, conviene darle más peso a Instagram y Facebook que a TikTok.

## 3. Canales y su función

| Canal | Función en la campaña de Aurora |
|---|---|
| **Instagram** (Reels, carruseles, Stories y pauta en Bogotá) | Vitrina principal: educación, resultados y testimonios de Aurora |
| **TikTok** | Alcance: rutina nocturna con Aurora, texturas y unboxing |
| **WhatsApp Business** | Cierre: diagnóstico de piel, recomendación de Aurora y seguimiento |
| **Microinfluenciadoras bogotanas** (2 o 3) | Prueba social: uso real de Aurora durante la campaña |
| **Email / difusión a clientas actuales** | Invitar a clientas de Luna y Sol a conocer Aurora |
| **Google Search** (opcional) | Captar búsquedas como "set facial Bogotá" o "rutina facial piel seca frío" |

## 4. Mensaje principal

> **"Aurora: el ritual facial que tu piel necesita para el clima de Bogotá."**

**Mensajes de apoyo:**
- *"El frío, la altura y el sol de Bogotá afectan tu piel todos los días. Aurora fue pensado para eso."*
- *"No adivines qué necesita tu piel: escríbenos y te hacemos un diagnóstico gratis antes de comprar Aurora."*
- *"Prueba Aurora 30 días. Si no te convence, te acompañamos hasta encontrar una solución o te devolvemos tu dinero."*

**Cuidado con la regulación (INVIMA):** usa frases como "ayuda a hidratar" o "mejora la apariencia de la piel". Evita "elimina", "cura" o "borra manchas".

## 5. Plan semana a semana

### Semana 0 (previa, recomendada): preparación
Para mostrar resultados reales de Aurora durante la campaña, necesitas empezar antes:
- Entrega Aurora a 3 o 4 clientas reales y a 2 o 3 microinfluenciadoras, con el compromiso de documentar su uso con la misma luz, el mismo ángulo y sin filtros.
- Configura en WhatsApp las etiquetas "Diagnóstico Aurora", "Lead Aurora" y "Cliente Aurora", el guion del diagnóstico de 4 o 5 preguntas y un código único por influenciadora.
- Define por escrito las condiciones de la garantía de 30 días de Aurora.

### Semana 1: Despertar el problema
**Objetivo:** que tu audiencia reconozca que el clima de Bogotá afecta su piel.

| Canal | Acciones |
|---|---|
| Instagram | Carrusel: *"5 señales de que el clima de Bogotá está afectando tu piel"*. Reel: *"¿Por qué tu piel se reseca aunque no haga calor?"*, con cierre presentando Aurora |
| TikTok | 3 o 4 videos educativos hablando a cámara; Aurora aparece al final como solución |
| Stories | Encuestas: *"¿Sientes tu piel tirante en las mañanas?"* |
| WhatsApp | Estados con tips de piel y anuncio del diagnóstico gratuito de Aurora |
| Pauta | Alcance en Bogotá con el mejor video educativo |

**KPI de la semana:** alcance en Bogotá, guardados, compartidos y retención de video.

### Semana 2: Presentar Aurora como solución
**Objetivo:** mostrar qué es Aurora, cómo se usa y por qué funciona.

| Canal | Acciones |
|---|---|
| Instagram | Reel de la rutina nocturna con Aurora paso a paso. Carrusel de ingredientes de Aurora explicados de forma sencilla. Reel sensorial: textura y aplicación |
| TikTok | Unboxing estilo ASMR del set Aurora y GRWM nocturno con Aurora |
| Tú, Camila | Video contando por qué creaste Aurora |
| WhatsApp | Lanzamiento oficial del diagnóstico de piel gratuito, con Aurora como recomendación cuando aplique |
| Email / difusión | A clientas de Luna y Sol: *"Ya cuidas tu cuerpo; ahora conoce Aurora para tu rostro"* |
| Pauta | Anuncios con destino a WhatsApp para iniciar el diagnóstico de Aurora |

**KPI de la semana:** conversaciones nuevas sobre Aurora, diagnósticos realizados y clics a WhatsApp.

### Semana 3: Prueba social
**Objetivo:** eliminar la duda de si Aurora vale lo que cuesta.

| Canal | Acciones |
|---|---|
| Instagram | Avances de las testers: *"Semana 3 usando Aurora"*. Testimonios en video de clientas bogotanas. Capturas de WhatsApp con permiso |
| Microinfluenciadoras | Publican su experiencia con Aurora usando su código único |
| TikTok | Reacciones y respuestas a comentarios sobre Aurora |
| Stories | Preguntas frecuentes sobre Aurora: tipo de piel, orden de uso, duración del set |
| WhatsApp | Seguimiento a quienes hicieron el diagnóstico y no compraron, con un testimonio de Aurora |
| Pauta | Retargeting con testimonios de Aurora a quienes vieron videos o escribieron |

**KPI de la semana:** tasa de cierre en WhatsApp, ventas por código de influenciadora y retargeting.

### Semana 4: Cierre y garantía
**Objetivo:** convertir a las indecisas reduciendo el riesgo, sin descontar Aurora.

| Canal | Acciones |
|---|---|
| Instagram | Reel con el resultado final de las testers de Aurora (antes y después, sin filtros). Post destacando la garantía de 30 días |
| TikTok | *"Lo que aprendí después de un mes con Aurora"* |
| WhatsApp | Mensaje final a leads de Aurora: garantía y entrega rápida en Bogotá. Valor agregado opcional: empaque de regalo especial para Aurora o asesoría de seguimiento a los 15 días |
| Email / difusión | Último recordatorio a clientas de Luna y Sol |
| Pauta | Conversión dirigida al público más caliente |

**KPI de la semana:** ventas de Aurora, ingresos por Aurora y CPA de Aurora.

**Después de la campaña:** a cada compradora de Aurora, seguimiento a los 15 días (*"¿Cómo va tu piel con Aurora?"*) y solicitud de testimonio a los 30 días.

## 6. Métricas de éxito

Como aún no tengo tus cifras de ventas actuales, las metas están planteadas en términos relativos. Con tu línea base las convertimos en números exactos.

| Etapa | KPI | Meta sugerida |
|---|---|---|
| **Resultado** | Unidades e ingresos de Aurora | Crecimiento claro frente a tus 4 semanas anteriores (por ejemplo, +30 % a +50 %) |
| **Resultado** | Precio promedio de venta de Aurora | Igual al precio de lista, sin erosión por descuentos |
| **Conversión** | Diagnósticos de piel realizados | Meta semanal según tu capacidad de atención |
| **Conversión** | Tasa de cierre de Aurora en WhatsApp (ventas ÷ diagnósticos) | Referencia orientativa: 15 % a 25 % |
| **Conversión** | Tiempo de respuesta en WhatsApp | Menos de 30 minutos en horario laboral |
| **Pauta** | CPA de Aurora | Muy por debajo del margen de Aurora |
| **Pauta** | ROAS de la campaña de Aurora | Mayor a 3 como referencia inicial |
| **Atracción** | Guardados y compartidos del contenido de Aurora | En crecimiento semana a semana |
| **Atracción** | Retención de los videos de Aurora | Más del 30 % de visualización completa en Reels y TikTok |
| **Prueba social** | Testimonios de Aurora recolectados | Al menos 5 a 8 (video o texto) |
| **Escalera** | Clientas de Luna o Sol que compraron Aurora | Registrar la cifra como línea base |
| **Calidad** | Uso de la garantía de Aurora | Bajo (menos del 5 %); si es alto, revisa la promesa |

## 7. Distribución sugerida de la pauta

| Semana | % del presupuesto | Enfoque |
|---|---|---|
| Semana 1 | 20 % | Alcance educativo |
| Semana 2 | 30 % | Conversaciones de WhatsApp sobre Aurora |
| Semana 3 | 25 % | Retargeting con testimonios de Aurora |
| Semana 4 | 25 % | Conversión final de Aurora |

## 8. Reglas de la campaña
- **Nunca descontar Aurora.** Añade valor (diagnóstico, garantía, empaque, seguimiento), no rebajas.
- **Sin filtros** en ningún contenido de resultados de Aurora.
- **No mencionar a Botica Verde ni a Skin Lab.** Diferénciate por lo propio de Aurora.
- **Registrar el origen** de cada venta de Aurora con etiquetas y códigos.

**Para afinar el plan necesito:**
1. Los diferenciales concretos de Aurora (ingredientes, tipo de piel, origen), para fortalecer el mensaje.
2. Tus ventas actuales aproximadas de Aurora, para fijar metas en números.
3. Tu presupuesto de pauta, para convertir los porcentajes en montos.

¿Quieres que desarrolle ahora el guion del diagnóstico de piel por WhatsApp o los textos de los anuncios de Aurora para cada semana?


## Respuesta completa

# Campaña "Ritual Aurora": 4 semanas para tu set facial premium

**Producto:** Aurora, set de cuidado facial, precio premium
**Mercado:** Bogotá
**Principio clave:** Aurora no se descuenta. Se vende con confianza, asesoría y reducción del riesgo.

## 1. Objetivo

**Objetivo principal:** Aumentar las ventas de Aurora en Bogotá y posicionarlo como el set facial de referencia para el clima de la ciudad, sin bajar su precio.

**Objetivos específicos:**
1. Generar conversaciones calificadas sobre Aurora por WhatsApp mediante el diagnóstico de piel gratuito.
2. Convertir esas conversaciones en ventas de Aurora con asesoría personalizada.
3. Crear una base de testimonios y resultados reales de Aurora que siga sirviendo después de la campaña.

## 2. Audiencia

| Segmento | Descripción | Por qué es clave para Aurora |
|---|---|---|
| **Principal: nuevas clientas** | Mujeres en Bogotá que ya invierten en skincare, buscan resultados y valoran la asesoría | Pueden pagar un precio premium si confían en el producto |
| **Caliente: clientas actuales** | Quienes ya compraron Luna o Sol | Conocen tu marca, así que Aurora es su siguiente paso natural |
| **Retargeting** | Quienes vieron videos de Aurora, visitaron su página o escribieron por WhatsApp sin comprar | Ya mostraron interés y necesitan un empujón de confianza |

**Supuesto por validar:** asumo un rango de 25 a 45 años. Si tu clienta real es mayor de 35, conviene darle más peso a Instagram y Facebook que a TikTok.

## 3. Canales y su función

| Canal | Función en la campaña de Aurora |
|---|---|
| **Instagram** (Reels, carruseles, Stories y pauta en Bogotá) | Vitrina principal: educación, resultados y testimonios de Aurora |
| **TikTok** | Alcance: rutina nocturna con Aurora, texturas y unboxing |
| **WhatsApp Business** | Cierre: diagnóstico de piel, recomendación de Aurora y seguimiento |
| **Microinfluenciadoras bogotanas** (2 o 3) | Prueba social: uso real de Aurora durante la campaña |
| **Email / difusión a clientas actuales** | Invitar a clientas de Luna y Sol a conocer Aurora |
| **Google Search** (opcional) | Captar búsquedas como "set facial Bogotá" o "rutina facial piel seca frío" |

## 4. Mensaje principal

> **"Aurora: el ritual facial que tu piel necesita para el clima de Bogotá."**

**Mensajes de apoyo:**
- *"El frío, la altura y el sol de Bogotá afectan tu piel todos los días. Aurora fue pensado para eso."*
- *"No adivines qué necesita tu piel: escríbenos y te hacemos un diagnóstico gratis antes de comprar Aurora."*
- *"Prueba Aurora 30 días. Si no te convence, te acompañamos hasta encontrar una solución o te devolvemos tu dinero."*

**Cuidado con la regulación (INVIMA):** usa frases como "ayuda a hidratar" o "mejora la apariencia de la piel". Evita "elimina", "cura" o "borra manchas".

## 5. Plan semana a semana

### Semana 0 (previa, recomendada): preparación
Para mostrar resultados reales de Aurora durante la campaña, necesitas empezar antes:
- Entrega Aurora a 3 o 4 clientas reales y a 2 o 3 microinfluenciadoras, con el compromiso de documentar su uso con la misma luz, el mismo ángulo y sin filtros.
- Configura en WhatsApp las etiquetas "Diagnóstico Aurora", "Lead Aurora" y "Cliente Aurora", el guion del diagnóstico de 4 o 5 preguntas y un código único por influenciadora.
- Define por escrito las condiciones de la garantía de 30 días de Aurora.

### Semana 1: Despertar el problema
**Objetivo:** que tu audiencia reconozca que el clima de Bogotá afecta su piel.

| Canal | Acciones |
|---|---|
| Instagram | Carrusel: *"5 señales de que el clima de Bogotá está afectando tu piel"*. Reel: *"¿Por qué tu piel se reseca aunque no haga calor?"*, con cierre presentando Aurora |
| TikTok | 3 o 4 videos educativos hablando a cámara; Aurora aparece al final como solución |
| Stories | Encuestas: *"¿Sientes tu piel tirante en las mañanas?"* |
| WhatsApp | Estados con tips de piel y anuncio del diagnóstico gratuito de Aurora |
| Pauta | Alcance en Bogotá con el mejor video educativo |

**KPI de la semana:** alcance en Bogotá, guardados, compartidos y retención de video.

### Semana 2: Presentar Aurora como solución
**Objetivo:** mostrar qué es Aurora, cómo se usa y por qué funciona.

| Canal | Acciones |
|---|---|
| Instagram | Reel de la rutina nocturna con Aurora paso a paso. Carrusel de ingredientes de Aurora explicados de forma sencilla. Reel sensorial: textura y aplicación |
| TikTok | Unboxing estilo ASMR del set Aurora y GRWM nocturno con Aurora |
| Tú, Camila | Video contando por qué creaste Aurora |
| WhatsApp | Lanzamiento oficial del diagnóstico de piel gratuito, con Aurora como recomendación cuando aplique |
| Email / difusión | A clientas de Luna y Sol: *"Ya cuidas tu cuerpo; ahora conoce Aurora para tu rostro"* |
| Pauta | Anuncios con destino a WhatsApp para iniciar el diagnóstico de Aurora |

**KPI de la semana:** conversaciones nuevas sobre Aurora, diagnósticos realizados y clics a WhatsApp.

### Semana 3: Prueba social
**Objetivo:** eliminar la duda de si Aurora vale lo que cuesta.

| Canal | Acciones |
|---|---|
| Instagram | Avances de las testers: *"Semana 3 usando Aurora"*. Testimonios en video de clientas bogotanas. Capturas de WhatsApp con permiso |
| Microinfluenciadoras | Publican su experiencia con Aurora usando su código único |
| TikTok | Reacciones y respuestas a comentarios sobre Aurora |
| Stories | Preguntas frecuentes sobre Aurora: tipo de piel, orden de uso, duración del set |
| WhatsApp | Seguimiento a quienes hicieron el diagnóstico y no compraron, con un testimonio de Aurora |
| Pauta | Retargeting con testimonios de Aurora a quienes vieron videos o escribieron |

**KPI de la semana:** tasa de cierre en WhatsApp, ventas por código de influenciadora y retargeting.

### Semana 4: Cierre y garantía
**Objetivo:** convertir a las indecisas reduciendo el riesgo, sin descontar Aurora.

| Canal | Acciones |
|---|---|
| Instagram | Reel con el resultado final de las testers de Aurora (antes y después, sin filtros). Post destacando la garantía de 30 días |
| TikTok | *"Lo que aprendí después de un mes con Aurora"* |
| WhatsApp | Mensaje final a leads de Aurora: garantía y entrega rápida en Bogotá. Valor agregado opcional: empaque de regalo especial para Aurora o asesoría de seguimiento a los 15 días |
| Email / difusión | Último recordatorio a clientas de Luna y Sol |
| Pauta | Conversión dirigida al público más caliente |

**KPI de la semana:** ventas de Aurora, ingresos por Aurora y CPA de Aurora.

**Después de la campaña:** a cada compradora de Aurora, seguimiento a los 15 días (*"¿Cómo va tu piel con Aurora?"*) y solicitud de testimonio a los 30 días.

## 6. Métricas de éxito

Como aún no tengo tus cifras de ventas actuales, las metas están planteadas en términos relativos. Con tu línea base las convertimos en números exactos.

| Etapa | KPI | Meta sugerida |
|---|---|---|
| **Resultado** | Unidades e ingresos de Aurora | Crecimiento claro frente a tus 4 semanas anteriores (por ejemplo, +30 % a +50 %) |
| **Resultado** | Precio promedio de venta de Aurora | Igual al precio de lista, sin erosión por descuentos |
| **Conversión** | Diagnósticos de piel realizados | Meta semanal según tu capacidad de atención |
| **Conversión** | Tasa de cierre de Aurora en WhatsApp (ventas ÷ diagnósticos) | Referencia orientativa: 15 % a 25 % |
| **Conversión** | Tiempo de respuesta en WhatsApp | Menos de 30 minutos en horario laboral |
| **Pauta** | CPA de Aurora | Muy por debajo del margen de Aurora |
| **Pauta** | ROAS de la campaña de Aurora | Mayor a 3 como referencia inicial |
| **Atracción** | Guardados y compartidos del contenido de Aurora | En crecimiento semana a semana |
| **Atracción** | Retención de los videos de Aurora | Más del 30 % de visualización completa en Reels y TikTok |
| **Prueba social** | Testimonios de Aurora recolectados | Al menos 5 a 8 (video o texto) |
| **Escalera** | Clientas de Luna o Sol que compraron Aurora | Registrar la cifra como línea base |
| **Calidad** | Uso de la garantía de Aurora | Bajo (menos del 5 %); si es alto, revisa la promesa |

## 7. Distribución sugerida de la pauta

| Semana | % del presupuesto | Enfoque |
|---|---|---|
| Semana 1 | 20 % | Alcance educativo |
| Semana 2 | 30 % | Conversaciones de WhatsApp sobre Aurora |
| Semana 3 | 25 % | Retargeting con testimonios de Aurora |
| Semana 4 | 25 % | Conversión final de Aurora |

## 8. Reglas de la campaña
- **Nunca descontar Aurora.** Añade valor (diagnóstico, garantía, empaque, seguimiento), no rebajas.
- **Sin filtros** en ningún contenido de resultados de Aurora.
- **No mencionar a Botica Verde ni a Skin Lab.** Diferénciate por lo propio de Aurora.
- **Registrar el origen** de cada venta de Aurora con etiquetas y códigos.

**Para afinar el plan necesito:**
1. Los diferenciales concretos de Aurora (ingredientes, tipo de piel, origen), para fortalecer el mensaje.
2. Tus ventas actuales aproximadas de Aurora, para fijar metas en números.
3. Tu presupuesto de pauta, para convertir los porcentajes en montos.

¿Quieres que desarrolle ahora el guion del diagnóstico de piel por WhatsApp o los textos de los anuncios de Aurora para cada semana?