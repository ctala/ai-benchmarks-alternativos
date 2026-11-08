# Claude Opus 5.5 — agent_long_horizon/implicit_state_construction

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.8 | quality: 8.5
- latency_total: 150.86s | tokens_per_second: 106.6
- input_tokens: 28117 | output_tokens: 14569

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola, Camila! Sí, me queda claro. Este es el resumen:

**Tu tienda online**
- **Mercado:** Bogotá, Colombia (único mercado por ahora)

**Productos**
| Producto | Categoría | Posicionamiento de precio |
|---|---|---|
| **Aurora** | Set de cuidado facial | Premium |
| **Sol** | Kit de maquillaje natural | Medio |
| **Luna** | Crema corporal | Entrada |

**Competidores principales (ambos en Bogotá)**
- Botica Verde
- Skin Lab

Tienes una gama escalonada: **Luna** puede servir como puerta de entrada para nuevos clientes, **Sol** como paso intermedio y **Aurora** como producto aspiracional y de mayor margen. Esto da mucho juego para estrategias de venta cruzada y fidelización.

¿Por dónde quieres empezar? Por ejemplo, podemos trabajar en una campaña para un producto concreto, una estrategia para diferenciarte de Botica Verde y Skin Lab, o un calendario de campañas para los próximos meses.

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

**Propuesta de valor:**

*Cuidado facial, corporal y maquillaje natural pensado para la mujer bogotana, con una línea completa que crece contigo: desde Luna para tu rutina diaria, pasando por Sol para realzar tu belleza natural, hasta Aurora para una experiencia premium. Te ofrecemos calidad en cada nivel de precio con la comodidad de comprar online y recibir en tu puerta en Bogotá.*

**Por qué funciona:**
- **Cercanía local:** hablarle directamente a Bogotá te da una ventaja de identidad frente a Botica Verde y Skin Lab.
- **Gama escalonada:** convierte tus tres niveles de precio en un camino de crecimiento para la clienta, no solo en opciones sueltas.
- **Conveniencia:** refuerza tu fortaleza como tienda online.

Si me cuentas qué te diferencia realmente de Botica Verde y Skin Lab (ingredientes, origen colombiano, sostenibilidad, rapidez de entrega, asesoría personalizada), puedo afinarla para que sea más distintiva.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Te recomiendo priorizar cuatro canales, en este orden:

**1. Instagram (canal principal)**
Es la vitrina natural para belleza y cuidado personal en Colombia.
- **Sol:** reels con tutoriales de maquillaje natural y antes/después.
- **Aurora:** contenido aspiracional con rutinas completas, texturas y empaque.
- **Luna:** contenido cotidiano y cercano.
- Usa la **Biblioteca de Anuncios de Meta** para ver qué están pautando Botica Verde y Skin Lab y encontrar huecos donde diferenciarte.

**2. TikTok (adquisición y alcance)**
Ideal para atraer clientas nuevas a bajo costo.
- **Luna** es tu mejor gancho aquí: precio de entrada, compra impulsiva y fácil de probar.
- Trabaja con **microinfluencers bogotanas** (5.000–50.000 seguidores). Son más creíbles y económicas que las grandes, y refuerzan tu ventaja local.

**3. WhatsApp Business (conversión y fidelización)**
En Colombia es el canal donde muchas compras se cierran.
- Es clave para **Aurora**: una compra premium suele necesitar asesoría personalizada antes de decidir.
- Úsalo para seguimiento posventa y para sugerir el siguiente paso: de Luna a Sol, y de Sol a Aurora.

**4. Pauta en Meta y Google (segmentada solo a Bogotá)**
- **Meta Ads:** segmentación geográfica estricta a Bogotá para no gastar presupuesto donde no entregas.
- **Google Search:** captura a quien ya busca algo como "crema corporal natural Bogotá" o "set cuidado facial". Esta búsqueda con intención de compra es especialmente valiosa para Aurora.

**Complemento: email marketing.** No es prioritario al inicio, pero conviene empezar a construir tu base desde ya para recompras y lanzamientos.

**Resumen por producto:**
| Producto | Canal estrella | Rol |
|---|---|---|
| Luna | TikTok + Meta Ads | Atraer clientas nuevas |
| Sol | Instagram | Mostrar resultados visuales |
| Aurora | WhatsApp + Google | Asesorar y cerrar ventas premium |

**Un punto para confirmar:** en la propuesta de valor asumí que tu público es principalmente femenino. ¿Es así? ¿Y qué rango de edad tiene? Si tu clienta tiene entre 18 y 30 años, le daría más peso a TikTok. Si tiene entre 30 y 45, Instagram y WhatsApp ganan relevancia. Con ese dato puedo ayudarte a repartir el presupuesto entre canales.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Aquí tienes una frecuencia realista, pensada para una tienda que probablemente gestionas con un equipo pequeño. Meta Ads y Google no aparecen porque son canales pagos y no de contenido orgánico.

| Canal | Frecuencia recomendada | Mínimo viable si estás sola |
|---|---|---|
| **Instagram (feed/reels)** | 4 por semana | 3 por semana |
| **Instagram (stories)** | Diario, 3-5 stories | 4-5 días por semana |
| **TikTok** | 4-5 videos por semana | 3 por semana |
| **WhatsApp (estados)** | 3-4 por semana | 2 por semana |
| **WhatsApp (listas de difusión)** | 2-3 al mes | 2 al mes |
| **Email** | Quincenal | 1 al mes |

**Cómo repartir el contenido entre tus productos**

- **Instagram:** alterna los tres. Por ejemplo, 2 reels de **Sol** (tutoriales), 1 carrusel de **Aurora** (rutina o ingredientes) y 1 publicación de **Luna** o de comunidad.
- **TikTok:** que la mayoría sea de **Luna** (unos 3 de cada 5 videos) por su rol de gancho. El resto, tutoriales rápidos de **Sol**.
- **WhatsApp:** usa los estados para novedades y testimonios. Reserva las difusiones para contenido de valor o lanzamientos, sobre todo de **Aurora**. Enviar más de 1 difusión por semana suele generar bloqueos.
- **Email:** recompra de **Luna**, venta cruzada hacia **Sol** y **Aurora**, y lanzamientos.

**Ejemplo de semana tipo**

| Día | Instagram | TikTok | WhatsApp |
|---|---|---|---|
| Lunes | Reel Sol | Video Luna | Estado |
| Martes | Stories | Video Sol | — |
| Miércoles | Carrusel Aurora | Video Luna | Estado |
| Jueves | Stories | — | — |
| Viernes | Reel Sol | Video Luna | Estado |
| Sábado | Post Luna / testimonio | Video Sol | — |
| Domingo | Stories ligeras | — | — |

**Tres consejos clave**
1. **La constancia importa más que el volumen.** Es mejor publicar 3 veces por semana durante seis meses que 7 veces durante tres semanas y abandonar.
2. **Reutiliza contenido.** Un mismo video vertical sirve para un reel de Instagram, un TikTok y un estado de WhatsApp, con pequeños ajustes de texto. Así reduces mucho la carga de trabajo.
3. **Revisa los datos cada mes.** Mira qué producto y qué formato generan más mensajes por WhatsApp o más ventas, y ajusta la frecuencia según eso. Observa también con qué ritmo publican Botica Verde y Skin Lab para no quedarte por debajo en visibilidad.

Cuando me confirmes el rango de edad de tu clienta, puedo ajustar el peso entre TikTok e Instagram. También puedo armarte un calendario editorial del primer mes con ideas concretas de contenido para Aurora, Sol y Luna.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

En tu catálogo, el skincare corresponde a **Aurora** (cuidado facial) y **Luna** (crema corporal). **Sol**, al ser maquillaje, sigue la lógica de tutoriales que ya vimos. En skincare la clienta no ve un resultado inmediato como con el maquillaje, así que el contenido tiene que **generar confianza, educar y hacer tangible la experiencia**.

## Los formatos que mejor funcionan

**1. Contenido educativo (el más importante)**
- Qué hace cada ingrediente y por qué está en la fórmula.
- Errores comunes: "3 errores al aplicar tu crema facial".
- Mitos vs. realidades: "¿La piel grasa necesita hidratación?".
- Formato ideal: carruseles en Instagram y videos cortos a cámara en TikTok.

**2. Rutinas paso a paso**
- Rutina de mañana y de noche con **Aurora**, mostrando el orden de uso.
- "Get ready with me" relajado aplicando **Luna** después de la ducha.
- Muestra a la clienta cómo integrar el producto en su vida diaria.

**3. Contenido sensorial (texturas y ASMR)**
- Primeros planos de la textura, cómo se absorbe, el sonido del empaque al abrirse.
- Muy efectivo para **Aurora**, porque justifica el precio premium con una sensación de lujo.
- También funciona para **Luna**: "así se absorbe en 10 segundos".

**4. Resultados reales con línea de tiempo**
- "Día 1 vs. día 30" usando **Aurora**, con la misma luz y el mismo ángulo.
- Que sea honesto: el skincare tarda semanas en mostrar cambios, y exagerar destruye la credibilidad.

**5. Testimonios y contenido de clientas (UGC)**
- Videos de clientas reales en Bogotá contando su experiencia.
- Capturas de mensajes de WhatsApp con reseñas, siempre con su permiso.
- Para **Aurora** es casi obligatorio: nadie paga precio premium sin prueba social.

**6. Contenido con aval experto**
- Colaboración con una dermatóloga o cosmetóloga bogotana que explique ingredientes o rutinas.
- Esto te puede diferenciar mucho de Botica Verde y Skin Lab si ellos no lo hacen.

**7. Detrás de cámaras**
- Cómo empacas los pedidos, de dónde vienen los ingredientes, quién está detrás de la marca.
- Humaniza la tienda y refuerza la cercanía local.

## Un ángulo local que puedes aprovechar

El clima de Bogotá afecta la piel: el frío, la altitud y la alta radiación UV provocan resequedad y sensibilidad. Contenido como *"Por qué tu piel se reseca en Bogotá y cómo cuidarla"* conecta directamente con tu clienta y posiciona a **Luna** como solución diaria y a **Aurora** como tratamiento completo. Es un mensaje que una marca no local difícilmente puede igualar.

## Qué formato usar para cada producto

| Formato | Aurora | Luna |
|---|---|---|
| Educativo | ✅✅ Ingredientes y beneficios | ✅ Hidratación y clima |
| Rutinas | ✅✅ Rutina completa | ✅ Hábito diario |
| Sensorial / texturas | ✅✅ Experiencia de lujo | ✅ Absorción rápida |
| Resultados en el tiempo | ✅✅ Clave | ✅ Piel suave en X días |
| Testimonios | ✅✅ Imprescindible | ✅ Volumen de reseñas |
| Experta | ✅✅ Justifica el precio | Opcional |

## Una precaución importante

En Colombia, los cosméticos se rigen por la normativa andina y el **INVIMA**. Tu contenido **no debe hacer afirmaciones médicas o terapéuticas**, como "cura el acné", "elimina manchas" o "trata la dermatitis". Usa en cambio expresiones como "ayuda a hidratar", "mejora la apariencia" o "piel visiblemente más suave". Así proteges tu marca y evitas problemas con la pauta en Meta, que también rechaza este tipo de afirmaciones.

¿Quieres que convierta esto en un calendario editorial del primer mes con ideas concretas de publicaciones para Aurora, Sol y Luna?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

La clave es que la clienta te compare por **valor, experiencia y especialización**, no por precio. Así puedes hacerlo frente a Botica Verde y Skin Lab.

## Paso 1: Mapea a tus competidores (antes de decidir nada)

Revisa sus redes, su web y la Biblioteca de Anuncios de Meta, y completa esta tabla:

| Aspecto | Botica Verde | Skin Lab | Tú |
|---|---|---|---|
| Mensaje principal | | | |
| Rango de precios | | | |
| Tiempo de entrega en Bogotá | | | |
| ¿Ofrecen asesoría? | | | |
| Tono de comunicación | | | |
| Qué critican sus clientas en reseñas | | | |

**Una hipótesis para validar:** por sus nombres, Botica Verde probablemente se posiciona como "natural/herbal" y Skin Lab como "científico/clínico". Si es así, hay un espacio libre en el medio: **natural, pero con respaldo y resultados explicados**. Confírmalo con tu investigación antes de construir sobre eso.

**Las reseñas negativas de tus competidores son oro:** te dicen exactamente qué necesidades están dejando sin atender.

## Paso 2: Elige tus palancas de diferenciación

**1. Especialista en la piel bogotana**
Es tu ventaja más difícil de copiar. Conviértela en tu identidad: "cuidado pensado para el frío, la altitud y el sol de Bogotá". Si tus competidores hablan de piel en general, tú hablas de *la piel de tu clienta, en su ciudad*.

**2. Asesoría personalizada por WhatsApp**
Ofrece un diagnóstico de piel gratuito por WhatsApp antes de la compra. Para **Aurora** esto cambia la conversación: la clienta deja de preguntarse "¿por qué es más caro?" y empieza a pensar "me recomendaron exactamente lo que necesito".

**3. Experiencia de entrega y unboxing**
Al vender solo en Bogotá puedes prometer lo que una marca nacional no puede, por ejemplo entrega en 24-48 horas. Súmale un empaque cuidado, una nota escrita a mano o una tarjeta con la rutina de uso. Esto pesa mucho en **Aurora**.

**4. Ecosistema de rutina, no productos sueltos**
Tus tres productos funcionan como un camino: **Luna → Sol → Aurora**. Vende rutinas y kits, no unidades. Un kit no se puede comparar directamente con el precio de un producto suelto de la competencia.

**5. Transparencia**
Explica cada ingrediente, de dónde viene y por qué está en la fórmula. Si eres una marca colombiana o usas ingredientes locales, comunícalo con orgullo.

**6. Aval experto**
Una alianza con una dermatóloga o cosmetóloga bogotana te da una credibilidad que justifica tus precios sin bajarlos.

## Paso 3: Promociones sin descuentos

Cuando necesites un empujón comercial, **agrega valor en lugar de restar precio**:

| En vez de... | Haz esto |
|---|---|
| 20% de descuento en Aurora | Aurora + muestra de Luna de regalo |
| Rebajar Sol | Sol + tutorial personalizado por videollamada |
| Bajar el precio de Luna | Luna en presentación doble o suscripción de recompra con envío gratis |
| Descuentos generales | Beneficios exclusivos para clientas recurrentes |

Así proteges tu margen y la percepción de calidad. Los descuentos frecuentes enseñan a la clienta a esperar rebajas.

## Cómo aplicarlo a cada producto

- **Luna:** es la que más se compara por precio, porque está en el nivel de entrada. Diferénciala por especialización ("la crema para el frío bogotano") y por comodidad de recompra, no por ser la más barata.
- **Sol:** diferénciala con educación. Tus tutoriales le enseñan a la clienta a usarlo, y eso tiene valor.
- **Aurora:** diferénciala con experiencia completa: asesoría, empaque, aval experto y resultados documentados.

## Lo que debes evitar

- Atacar o mencionar a Botica Verde o Skin Lab en tu comunicación. Enfócate en lo tuyo.
- Prometer de todo: elige 2 o 3 palancas y sé la mejor en ellas.
- Copiar sus promociones. Si ellos bajan precios, tú refuerzas valor.

**Mi recomendación para empezar:** combina **especialista en la piel bogotana + asesoría por WhatsApp + rutinas en kit**. Las tres son coherentes con tu propuesta de valor, aprovechan tus canales y son difíciles de imitar.

¿Qué tienes hoy que tus competidores no tengan? Por ejemplo, ingredientes, origen, rapidez de entrega o tu historia como fundadora. Con eso puedo afinar tu diferenciación y ajustar la propuesta de valor para que sea mucho más distintiva.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Mide pocos indicadores, pero que estén conectados con tus decisiones. En el primer trimestre el objetivo es **establecer tu línea base**: saber de dónde vienen tus clientas, qué producto las atrae y si vuelven a comprar.

## 1. KPIs de negocio (los más importantes)

| KPI | Qué te dice | Cómo calcularlo |
|---|---|---|
| **Ventas totales y por producto** | Qué peso tienen Aurora, Sol y Luna en tus ingresos | Ingresos de cada producto ÷ ingresos totales |
| **Ticket promedio** | Si estás logrando vender kits y rutinas | Ingresos ÷ número de pedidos |
| **Costo de adquisición (CAC)** | Cuánto te cuesta conseguir una clienta nueva | Inversión en marketing ÷ clientas nuevas |
| **Margen por pedido** | Si tus promociones de valor agregado son rentables | Ingreso − costo del producto, del envío y de los regalos |
| **ROAS** | Rentabilidad de la pauta en Meta y Google | Ventas atribuidas ÷ inversión en anuncios |

## 2. KPIs por canal

| Canal | KPI principal | KPI secundario |
|---|---|---|
| **Instagram** | Tasa de interacción (guardados y compartidos pesan más que los likes) | Clics al enlace o a WhatsApp |
| **TikTok** | Visualizaciones y retención promedio del video | Seguidores nuevos y visitas al perfil |
| **WhatsApp** | **Tasa de conversión de conversación a venta** | Tiempo promedio de respuesta |
| **Meta Ads** | Costo por compra o por conversación iniciada | CTR y frecuencia |
| **Google Search** | Costo por conversión | Tasa de conversión de las búsquedas |
| **Email** | Tasa de clics | Ventas generadas por email |

Para saber de dónde viene cada venta, usa **enlaces con UTM** en tu web y pregunta en WhatsApp "¿cómo nos conociste?". Es simple, pero en el primer trimestre es la mejor fuente de verdad.

## 3. KPIs de tu estrategia de producto

Estos miden si tu escalera **Luna → Sol → Aurora** funciona:

- **Tasa de recompra de Luna** a 30, 60 y 90 días. Confirma si Luna cumple su papel de gancho y hábito.
- **Tasa de paso entre productos**: el porcentaje de clientas de Luna que compran Sol y el de clientas de Sol que compran Aurora.
- **Porcentaje de pedidos que son kits o rutinas.** Mide la palanca de "ecosistema, no productos sueltos".
- **Conversión de Aurora con asesoría vs. sin asesoría.** Si el diagnóstico por WhatsApp eleva claramente las ventas de Aurora, tienes la prueba para invertir más en él.

## 4. KPIs de diferenciación

Así sabrás si te estás distinguiendo de Botica Verde y Skin Lab sin bajar precios:

- **Cumplimiento de entrega en 24-48 h en Bogotá** (% de pedidos a tiempo).
- **Cantidad y calificación de reseñas**, sobre todo de Aurora.
- **Porcentaje de ventas sin descuento.** Si sube, la clienta te está comprando por valor y no por precio.
- **Menciones espontáneas**: clientas que hablan del clima de Bogotá, de la asesoría o del unboxing en reseñas y mensajes.

## Plan para el trimestre

| Mes | Enfoque | Acción clave |
|---|---|---|
| **Mes 1** | Medir la línea base | Configurar UTM, Meta Pixel, Google Analytics y un registro de conversaciones de WhatsApp. No juzgues resultados todavía. |
| **Mes 2** | Optimizar | Pasar presupuesto a los anuncios y formatos con mejor costo por venta. Probar 2 o 3 variantes de contenido de Luna en TikTok. |
| **Mes 3** | Evaluar y decidir | Revisar la recompra de Luna, el paso hacia Sol y Aurora y el CAC por canal. Definir las metas del segundo trimestre con datos reales. |

## Tu tablero mínimo (si solo puedes medir 6)

1. Ventas por producto (Aurora, Sol, Luna)
2. Ticket promedio
3. CAC
4. Conversión de WhatsApp a venta
5. Tasa de recompra de Luna
6. Porcentaje de pedidos que son kits

Revísalos en una hoja de cálculo una vez por semana y analízalos a fondo una vez al mes.

**Sobre las referencias del mercado:** como orientación, una tienda online suele convertir entre el 1% y el 3% de sus visitas, y WhatsApp suele convertir bastante más porque la clienta ya llega con interés. Aun así, tus propios números del primer mes son mejor referencia que cualquier promedio del sector.

¿Ya tienes ventas o datos de pauta de meses anteriores? Con eso puedo proponerte metas numéricas concretas para cada KPI. Y si me confirmas el rango de edad de tu clienta, ajusto qué métricas de TikTok o de Instagram deberían pesar más.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

# Campaña Aurora: "Tu piel, a la altura de Bogotá"

**Duración:** 4 semanas
**Producto:** Aurora, set de cuidado facial premium
**Mercado:** solo Bogotá

## 1. Objetivo

**Objetivo principal:** aumentar las ventas de **Aurora** y posicionarlo como el set de cuidado facial pensado para la piel bogotana, sin recurrir a descuentos.

**Objetivos específicos:**
1. Generar conversaciones calificadas por WhatsApp mediante el **diagnóstico de piel gratuito para Aurora**.
2. Convertir clientas actuales de **Sol** y **Luna** en compradoras de **Aurora**.
3. Conseguir reseñas y testimonios de **Aurora** que sirvan como prueba social para campañas futuras.

## 2. Audiencia

| Segmento | Descripción | Por qué es clave para Aurora |
|---|---|---|
| **Principal: clientas actuales** | Compradoras de Sol y Luna en tu base de WhatsApp y email | Ya confían en tu marca. El paso a Aurora es el último escalón de tu escalera Luna → Sol → Aurora |
| **Secundario: prospecto premium** | Mujeres en Bogotá interesadas en skincare, rutinas faciales y cosmética natural, con poder adquisitivo medio-alto | Valoran la asesoría y la experiencia por encima del precio |
| **Retargeting** | Personas que visitaron la página de Aurora, vieron sus videos o escribieron por WhatsApp sin comprar | Ya mostraron interés y necesitan un empujón |

**Segmentación en Meta Ads:** solo Bogotá; intereses en skincare, cuidado facial, cosmética natural y dermatología; audiencias similares (lookalike) a partir de tus compradoras.

> Asumo un rango de **28 a 45 años**, que suele ser el perfil más afín a un set facial premium. Si tu clienta real es más joven, ajustaría la mezcla para darle más peso a TikTok.

## 3. Mensaje principal

> **"El frío, la altitud y el sol de Bogotá le piden más a tu piel. Aurora es la rutina facial completa que responde a eso, con asesoría personalizada para que sepas exactamente cómo usarla."**

**Mensajes de apoyo:**
- **Especialización:** "Aurora, pensado para la piel que vive a 2.600 metros."
- **Asesoría:** "Antes de comprar Aurora, te hacemos un diagnóstico de piel gratis por WhatsApp."
- **Experiencia:** "Aurora llega a tu puerta en Bogotá en 24-48 horas, con tu rutina explicada paso a paso."
- **Resultados honestos:** "Aurora no es magia: es constancia. Te acompañamos en tus primeros 30 días."

## 4. Canales y su rol

| Canal | Rol en la campaña de Aurora | Peso sugerido en presupuesto |
|---|---|---|
| **Instagram** | Contenido aspiracional, sensorial y educativo de Aurora | Orgánico |
| **WhatsApp Business** | Diagnóstico de piel, asesoría y cierre de venta de Aurora | Orgánico |
| **Meta Ads** | Alcance a prospectos y retargeting hacia el diagnóstico de Aurora | ~55% |
| **Google Search** | Capturar búsquedas como "set cuidado facial Bogotá" y "rutina facial piel seca" | ~30% |
| **Microinfluencer o experta** | Aval de una dermatóloga o cosmetóloga bogotana sobre Aurora | ~15% |
| **Email** | Invitación exclusiva a clientas de Sol y Luna para conocer Aurora | Orgánico |
| **TikTok** | Apoyo con 1-2 videos semanales de texturas de Aurora | Orgánico |

## 5. Plan semana a semana

### Semana 1: Despertar interés ("Tu piel en Bogotá")
**Meta:** educar sobre el problema antes de presentar a Aurora como solución.

- **Instagram:** carrusel "Por qué tu piel sufre en Bogotá: frío, altitud y radiación UV". Cierra presentando Aurora.
- **Instagram y TikTok:** reel sensorial de Aurora con primeros planos de texturas, apertura del empaque y aplicación.
- **Stories:** encuesta "¿Sientes tu piel tirante en Bogotá?" para generar interacción.
- **Meta Ads:** campaña de alcance con el reel sensorial de Aurora.
- **Google Search:** activar palabras clave de intención de compra.
- **Preparación interna:** guion del diagnóstico de piel de Aurora por WhatsApp (3-5 preguntas sobre tipo de piel, rutina actual y preocupaciones).

### Semana 2: Generar confianza ("Aurora, explicado")
**Meta:** justificar el valor premium de Aurora con educación y autoridad.

- **Colaboración con la experta:** video o live donde la dermatóloga o cosmetóloga explique los ingredientes de Aurora y su función en la rutina.
- **Instagram:** carrusel "Rutina de mañana y noche con Aurora, paso a paso".
- **Instagram:** reel "Qué hay dentro de Aurora y por qué", con transparencia total de ingredientes.
- **Email a clientas de Sol y Luna:** "Ya conoces nuestra calidad. Te presentamos Aurora, el siguiente paso en tu rutina."
- **Meta Ads:** campaña de interacción con el video de la experta, dirigida a quienes vieron el reel de la semana 1.

### Semana 3: Convertir ("Tu diagnóstico Aurora")
**Meta:** llevar conversaciones a WhatsApp y cerrar ventas de Aurora. Es la semana más intensa.

- **Lanzamiento del diagnóstico de piel gratuito** con llamado a la acción en todos los canales: "Escríbenos 'AURORA' por WhatsApp y te decimos si esta rutina es para ti."
- **Promoción de valor agregado (sin descuento):** quien compre Aurora esta semana recibe **una crema Luna de regalo** y una tarjeta con su rutina personalizada escrita a mano.
- **Instagram:** testimonios de las primeras clientas de Aurora (capturas de WhatsApp con permiso).
- **Meta Ads:** campaña de conversación hacia WhatsApp + retargeting a quienes interactuaron con contenido de Aurora.
- **WhatsApp, lista de difusión:** un solo envío a tu base con la invitación al diagnóstico de Aurora.

### Semana 4: Cerrar y fidelizar ("Tus primeros 30 días con Aurora")
**Meta:** aprovechar el impulso final y convertir compradoras en embajadoras de Aurora.

- **Urgencia honesta:** "Últimos días para recibir Aurora con Luna de regalo."
- **Retargeting final** en Meta y Google para quienes iniciaron conversación o visitaron la página de Aurora sin comprar.
- **Posventa por WhatsApp:** mensaje a los 3-5 días de la entrega: "¿Cómo te va con Aurora? ¿Tienes dudas sobre la rutina?"
- **Solicitud de reseñas:** pedir a cada compradora de Aurora una reseña o un video corto de su experiencia.
- **Instagram:** reel de unboxing real de Aurora hecho por una clienta o la microinfluencer.
- **Cierre interno:** recopilar los datos de la campaña para el análisis final.

## 6. Métricas de éxito

| KPI | Qué mide en la campaña de Aurora | Meta orientativa |
|---|---|---|
| **Unidades vendidas de Aurora** | Resultado principal | Definir según tu histórico (ej.: +30-50% vs. un mes normal) |
| **Conversaciones de WhatsApp iniciadas con "AURORA"** | Interés real generado | Definir según tu base actual |
| **Conversión de diagnóstico a compra de Aurora** | Efectividad de la asesoría | 20-30% como referencia inicial |
| **Clientas de Sol/Luna que compran Aurora** | Funcionamiento de la escalera de productos | Al menos 10% de las contactadas por email |
| **Costo por compra de Aurora (Meta + Google)** | Rentabilidad de la pauta | Inferior al margen de un set Aurora |
| **ROAS de la campaña de Aurora** | Retorno de la inversión publicitaria | Mínimo 3x como referencia |
| **Margen por pedido de Aurora (con Luna de regalo)** | Rentabilidad de la promoción de valor agregado | Que el regalo no se coma más del 15-20% del margen |
| **Reseñas nuevas de Aurora** | Prueba social para el futuro | Al menos 1 reseña por cada 3 compras |
| **Guardados y compartidos del contenido de Aurora** | Calidad del contenido educativo | Superior al promedio de tus publicaciones |

**Cómo medirlo:** usa UTM específicos (ej.: `utm_campaign=aurora_bogota`), la palabra clave "AURORA" en WhatsApp para rastrear el origen y la pregunta "¿cómo nos conociste?" en cada venta.

## 7. Precauciones

- **Normativa INVIMA:** en ningún contenido de Aurora digas que "elimina manchas", "cura el acné" o "quita arrugas". Usa "mejora la apariencia", "ayuda a hidratar" o "piel visiblemente más luminosa". Esto también evita que Meta rechace tus anuncios.
- **Sin mencionar a Botica Verde ni a Skin Lab:** la campaña de Aurora habla de tu clienta y de su piel, no de la competencia.
- **Capacidad operativa:** asegúrate de poder responder rápido en WhatsApp durante la semana 3. Un diagnóstico de Aurora que tarda horas en responderse pierde la venta.

Para convertir las metas orientativas en cifras concretas, necesito el **precio de Aurora**, tu **presupuesto disponible para pauta** y, si lo tienes, **cuántos sets de Aurora vendes en un mes normal**. Con eso te calculo el CAC máximo aceptable y la meta exacta de ventas de la campaña.


## Respuesta completa

# Campaña Aurora: "Tu piel, a la altura de Bogotá"

**Duración:** 4 semanas
**Producto:** Aurora, set de cuidado facial premium
**Mercado:** solo Bogotá

## 1. Objetivo

**Objetivo principal:** aumentar las ventas de **Aurora** y posicionarlo como el set de cuidado facial pensado para la piel bogotana, sin recurrir a descuentos.

**Objetivos específicos:**
1. Generar conversaciones calificadas por WhatsApp mediante el **diagnóstico de piel gratuito para Aurora**.
2. Convertir clientas actuales de **Sol** y **Luna** en compradoras de **Aurora**.
3. Conseguir reseñas y testimonios de **Aurora** que sirvan como prueba social para campañas futuras.

## 2. Audiencia

| Segmento | Descripción | Por qué es clave para Aurora |
|---|---|---|
| **Principal: clientas actuales** | Compradoras de Sol y Luna en tu base de WhatsApp y email | Ya confían en tu marca. El paso a Aurora es el último escalón de tu escalera Luna → Sol → Aurora |
| **Secundario: prospecto premium** | Mujeres en Bogotá interesadas en skincare, rutinas faciales y cosmética natural, con poder adquisitivo medio-alto | Valoran la asesoría y la experiencia por encima del precio |
| **Retargeting** | Personas que visitaron la página de Aurora, vieron sus videos o escribieron por WhatsApp sin comprar | Ya mostraron interés y necesitan un empujón |

**Segmentación en Meta Ads:** solo Bogotá; intereses en skincare, cuidado facial, cosmética natural y dermatología; audiencias similares (lookalike) a partir de tus compradoras.

> Asumo un rango de **28 a 45 años**, que suele ser el perfil más afín a un set facial premium. Si tu clienta real es más joven, ajustaría la mezcla para darle más peso a TikTok.

## 3. Mensaje principal

> **"El frío, la altitud y el sol de Bogotá le piden más a tu piel. Aurora es la rutina facial completa que responde a eso, con asesoría personalizada para que sepas exactamente cómo usarla."**

**Mensajes de apoyo:**
- **Especialización:** "Aurora, pensado para la piel que vive a 2.600 metros."
- **Asesoría:** "Antes de comprar Aurora, te hacemos un diagnóstico de piel gratis por WhatsApp."
- **Experiencia:** "Aurora llega a tu puerta en Bogotá en 24-48 horas, con tu rutina explicada paso a paso."
- **Resultados honestos:** "Aurora no es magia: es constancia. Te acompañamos en tus primeros 30 días."

## 4. Canales y su rol

| Canal | Rol en la campaña de Aurora | Peso sugerido en presupuesto |
|---|---|---|
| **Instagram** | Contenido aspiracional, sensorial y educativo de Aurora | Orgánico |
| **WhatsApp Business** | Diagnóstico de piel, asesoría y cierre de venta de Aurora | Orgánico |
| **Meta Ads** | Alcance a prospectos y retargeting hacia el diagnóstico de Aurora | ~55% |
| **Google Search** | Capturar búsquedas como "set cuidado facial Bogotá" y "rutina facial piel seca" | ~30% |
| **Microinfluencer o experta** | Aval de una dermatóloga o cosmetóloga bogotana sobre Aurora | ~15% |
| **Email** | Invitación exclusiva a clientas de Sol y Luna para conocer Aurora | Orgánico |
| **TikTok** | Apoyo con 1-2 videos semanales de texturas de Aurora | Orgánico |

## 5. Plan semana a semana

### Semana 1: Despertar interés ("Tu piel en Bogotá")
**Meta:** educar sobre el problema antes de presentar a Aurora como solución.

- **Instagram:** carrusel "Por qué tu piel sufre en Bogotá: frío, altitud y radiación UV". Cierra presentando Aurora.
- **Instagram y TikTok:** reel sensorial de Aurora con primeros planos de texturas, apertura del empaque y aplicación.
- **Stories:** encuesta "¿Sientes tu piel tirante en Bogotá?" para generar interacción.
- **Meta Ads:** campaña de alcance con el reel sensorial de Aurora.
- **Google Search:** activar palabras clave de intención de compra.
- **Preparación interna:** guion del diagnóstico de piel de Aurora por WhatsApp (3-5 preguntas sobre tipo de piel, rutina actual y preocupaciones).

### Semana 2: Generar confianza ("Aurora, explicado")
**Meta:** justificar el valor premium de Aurora con educación y autoridad.

- **Colaboración con la experta:** video o live donde la dermatóloga o cosmetóloga explique los ingredientes de Aurora y su función en la rutina.
- **Instagram:** carrusel "Rutina de mañana y noche con Aurora, paso a paso".
- **Instagram:** reel "Qué hay dentro de Aurora y por qué", con transparencia total de ingredientes.
- **Email a clientas de Sol y Luna:** "Ya conoces nuestra calidad. Te presentamos Aurora, el siguiente paso en tu rutina."
- **Meta Ads:** campaña de interacción con el video de la experta, dirigida a quienes vieron el reel de la semana 1.

### Semana 3: Convertir ("Tu diagnóstico Aurora")
**Meta:** llevar conversaciones a WhatsApp y cerrar ventas de Aurora. Es la semana más intensa.

- **Lanzamiento del diagnóstico de piel gratuito** con llamado a la acción en todos los canales: "Escríbenos 'AURORA' por WhatsApp y te decimos si esta rutina es para ti."
- **Promoción de valor agregado (sin descuento):** quien compre Aurora esta semana recibe **una crema Luna de regalo** y una tarjeta con su rutina personalizada escrita a mano.
- **Instagram:** testimonios de las primeras clientas de Aurora (capturas de WhatsApp con permiso).
- **Meta Ads:** campaña de conversación hacia WhatsApp + retargeting a quienes interactuaron con contenido de Aurora.
- **WhatsApp, lista de difusión:** un solo envío a tu base con la invitación al diagnóstico de Aurora.

### Semana 4: Cerrar y fidelizar ("Tus primeros 30 días con Aurora")
**Meta:** aprovechar el impulso final y convertir compradoras en embajadoras de Aurora.

- **Urgencia honesta:** "Últimos días para recibir Aurora con Luna de regalo."
- **Retargeting final** en Meta y Google para quienes iniciaron conversación o visitaron la página de Aurora sin comprar.
- **Posventa por WhatsApp:** mensaje a los 3-5 días de la entrega: "¿Cómo te va con Aurora? ¿Tienes dudas sobre la rutina?"
- **Solicitud de reseñas:** pedir a cada compradora de Aurora una reseña o un video corto de su experiencia.
- **Instagram:** reel de unboxing real de Aurora hecho por una clienta o la microinfluencer.
- **Cierre interno:** recopilar los datos de la campaña para el análisis final.

## 6. Métricas de éxito

| KPI | Qué mide en la campaña de Aurora | Meta orientativa |
|---|---|---|
| **Unidades vendidas de Aurora** | Resultado principal | Definir según tu histórico (ej.: +30-50% vs. un mes normal) |
| **Conversaciones de WhatsApp iniciadas con "AURORA"** | Interés real generado | Definir según tu base actual |
| **Conversión de diagnóstico a compra de Aurora** | Efectividad de la asesoría | 20-30% como referencia inicial |
| **Clientas de Sol/Luna que compran Aurora** | Funcionamiento de la escalera de productos | Al menos 10% de las contactadas por email |
| **Costo por compra de Aurora (Meta + Google)** | Rentabilidad de la pauta | Inferior al margen de un set Aurora |
| **ROAS de la campaña de Aurora** | Retorno de la inversión publicitaria | Mínimo 3x como referencia |
| **Margen por pedido de Aurora (con Luna de regalo)** | Rentabilidad de la promoción de valor agregado | Que el regalo no se coma más del 15-20% del margen |
| **Reseñas nuevas de Aurora** | Prueba social para el futuro | Al menos 1 reseña por cada 3 compras |
| **Guardados y compartidos del contenido de Aurora** | Calidad del contenido educativo | Superior al promedio de tus publicaciones |

**Cómo medirlo:** usa UTM específicos (ej.: `utm_campaign=aurora_bogota`), la palabra clave "AURORA" en WhatsApp para rastrear el origen y la pregunta "¿cómo nos conociste?" en cada venta.

## 7. Precauciones

- **Normativa INVIMA:** en ningún contenido de Aurora digas que "elimina manchas", "cura el acné" o "quita arrugas". Usa "mejora la apariencia", "ayuda a hidratar" o "piel visiblemente más luminosa". Esto también evita que Meta rechace tus anuncios.
- **Sin mencionar a Botica Verde ni a Skin Lab:** la campaña de Aurora habla de tu clienta y de su piel, no de la competencia.
- **Capacidad operativa:** asegúrate de poder responder rápido en WhatsApp durante la semana 3. Un diagnóstico de Aurora que tarda horas en responderse pierde la venta.

Para convertir las metas orientativas en cifras concretas, necesito el **precio de Aurora**, tu **presupuesto disponible para pauta** y, si lo tienes, **cuántos sets de Aurora vendes en un mes normal**. Con eso te calculo el CAC máximo aceptable y la meta exacta de ventas de la campaña.