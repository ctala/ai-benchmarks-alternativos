# Qwen 3.8 27B — agent_long_horizon/implicit_state_construction

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.81 | quality: 10.0
- latency_total: 765.732s | tokens_per_second: 16.8
- input_tokens: 21524 | output_tokens: 12264

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo



Sí, Camila, me queda claro el contexto:

- **Negocio:** tienda online en Colombia.  
- **Mercado actual:** solo **Bogotá**.  
- **Productos:**
  1. **Aurora**: set de cuidado facial, **precio premium**.
  2. **Sol**: kit de maquillaje natural, **precio medio**.
  3. **Luna**: crema corporal, **precio entrada**.
- **Competidores principales:** **Botica Verde** y **Skin Lab**, ambos también en Bogotá.

Cuando quieras, podemos empezar a planificar campañas, segmentación, mensajes, presupuesto, embudo o estrategia de lanzamiento.

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo



Somos una tienda online bogotana que combina cuidado facial, maquillaje natural y cuidado corporal en una misma experiencia, con opciones desde precio de entrada hasta premium. Ayudamos a cada cliente a elegir y armar su rutina de belleza ideal de forma cercana, práctica y confiable.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo



Te recomendaría priorizar estos canales, en este orden, porque son los más efectivos para una tienda online de belleza que vende en Bogotá y tiene productos de entrada, medio y premium:

| Prioridad | Canal | Por qué priorizarlo | Cómo usarlo para tus productos |
|---|---|---|---|
| 1 | **Instagram + Meta Ads** | Es el canal visual principal para belleza, skincare y maquillaje. Además, puedes segmentar por Bogotá, intereses, comportamiento y retargeting. | **Aurora**: contenido educativo, testimonios, rutinas premium y retargeting. **Sol**: reels de maquillaje natural, antes/después y tips. **Luna**: promociones, combos y compra impulsiva. |
| 2 | **WhatsApp Business** | Es clave en Colombia para cerrar ventas, dar atención cercana y convertir interés en compra. | Catálogo con tus 3 productos, etiquetas por interés, listas para promos y mensajes segmentados: “interesada en skincare”, “busca maquillaje natural”, “busca precio de entrada”. |
| 3 | **TikTok** | Bueno para descubrimiento, especialmente si tu público busca rutinas, tips, unboxings y maquillaje natural. | Reels cortos con tips de skincare, maquillaje natural, uso de **Luna**, comparativas suaves con necesidades reales y contenido tipo “cómo armar tu rutina”. |
| 4 | **Google Shopping / SEO local** | Captura a personas que ya están buscando productos específicos. | Anunciar o indexar productos como “crema corporal”, “kit de maquillaje natural”, “set de cuidado facial”, con enfoque en Bogotá. |
| 5 | **Email / CRM** | Es el canal más barato para retención y recompra. | Seguimiento postventa, recordatorios de recompra, ofertas exclusivas, lanzamientos y segmentación por producto comprado. |

Mi recomendación concreta sería:

- **Canal principal de descubrimiento y venta:** Instagram.
- **Canal principal de conversión y atención:** WhatsApp Business.
- **Canal para atraer nuevo público:** TikTok.
- **Canal para capturar búsquedas activas:** Google Shopping/SEO.
- **Canal para fidelizar:** email.

Para empezar, yo concentraría el esfuerzo así:

- **50% Instagram/Meta Ads**
- **25% WhatsApp Business**
- **15% TikTok**
- **10% Google/SEO + email**

Y por producto:

- **Luna**, al ser precio de entrada: Instagram, WhatsApp y Google Shopping para compras rápidas.
- **Sol**, al ser precio medio y maquillaje natural: Instagram y TikTok para educación y demostración.
- **Aurora**, al ser premium: Instagram, WhatsApp y email para construir confianza, mostrar resultados y ofrecer una experiencia más cuidada.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo



Para tu caso, yo no te recomendaría publicar todos los días en todos los canales, porque puedes saturarte. Mejor te enfocarías en **constancia realista** y en que cada canal tenga un rol claro.

Mi recomendación sería así:

| Canal | Frecuencia orgánica recomendada | Formato ideal | Enfoque por producto |
|---|---:|---|---|
| **Instagram** | **4 a 5 publicaciones por semana** | 2-3 reels, 1-2 carruseles, 1 historia diaria o casi diaria | **Aurora**: rutinas premium, resultados, confianza. **Sol**: maquillaje natural, tips, looks. **Luna**: combos, promo, compra fácil. |
| **TikTok** | **3 a 4 videos por semana** | Reels cortos de 15 a 45 segundos | **Sol**: maquillaje natural y antes/después. **Luna**: rutina rápida, unboxing, tips. **Aurora**: educación de skincare, mitos, resultados. |
| **WhatsApp Business** | **1 mensaje promocional por semana + 2-3 estados/días** | Mensajes segmentados, estados, catálogo actualizado | **Luna**: oferta rápida. **Sol**: tips + producto. **Aurora**: seguimiento personalizado y atención cercana. |
| **Google / SEO** | **1 contenido nuevo o actualización por semana** | Artículos, landing pages, descripciones de producto, preguntas frecuentes | **Aurora**: “set de cuidado facial premium”, “rutina facial completa”. **Sol**: “maquillaje natural”, “kit de maquillaje natural”. **Luna**: “crema corporal”, “crema corporal para todo el cuerpo”. |
| **Email** | **1 correo por semana o 2 por quincena** | Newsletter, lanzamiento, promo, postventa | **Luna**: recompra y combos. **Sol**: educación y novedades. **Aurora**: experiencia premium, testimonios y seguimiento. |

Si apenas estás empezando y tienes poco tiempo, usaría este **mínimo viable**:

- **Instagram:** 3 publicaciones por semana + historias diarias.
- **TikTok:** 3 videos por semana.
- **WhatsApp:** 1 mensaje promocional por semana + 3 estados.
- **Google/SEO:** 1 contenido o actualización de producto por semana.
- **Email:** 1 correo por semana.

Un calendario semanal simple podría ser:

**Lunes**
- Instagram: reel educativo sobre skincare o maquillaje natural.
- TikTok: tip corto para rutina facial o maquillaje natural.
- WhatsApp: estado con producto destacado.

**Martes**
- Instagram: historia con encuesta, pregunta o testimonio.
- TikTok: video de rutina rápida.
- Google/SEO: actualizar descripción de producto o publicar artículo.

**Miércoles**
- Instagram: carrusel con beneficios de **Aurora**, **Sol** o **Luna**.
- WhatsApp: mensaje promocional segmentado.

**Jueves**
- Instagram: reel de producto, unboxing o antes/después.
- TikTok: video de “cómo usar” alguno de tus productos.
- Email: newsletter con producto destacado o tip.

**Viernes**
- Instagram: historia o reel con oferta, combo o prueba social.
- TikTok: video corto de venta suave.
- WhatsApp: estado con prueba social o última oportunidad de compra.

**Sábado**
- Instagram: historia con contenido local, por ejemplo entregas en Bogotá, testimonios o preguntas frecuentes.
- TikTok: video más cercano, detrás de cámaras o respuesta a comentarios.

**Domingo**
- Descanso o solo historias ligeras.

Para tus tres productos, yo priorizaría así el contenido:

- **Luna**, por ser precio de entrada: contenido más frecuente de venta, combos, promos y compra rápida.
- **Sol**, por ser maquillaje natural: contenido demostrativo, tips, looks y educación.
- **Aurora**, por ser premium: contenido de confianza, rutinas, resultados, testimonios y atención personalizada.

Mi consejo sería que no intentes competir por cantidad con **Botica Verde** o **Skin Lab**, sino por **claridad y cercanía**: que en Bogotá te reconozcan como la tienda donde cada cliente sabe qué producto comprar según su necesidad, presupuesto y tipo de piel.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo



Para **skincare**, el contenido que mejor funciona es el que combina **educación + confianza + resultados visibles**. En tu caso, especialmente para **Aurora**, que es tu set premium de cuidado facial, y también para **Luna**, como crema corporal de entrada, yo priorizaría estos tipos de contenido:

### 1. Contenido educativo

Este es el más importante para skincare porque la gente necesita entender qué necesita antes de comprar.

Ejemplos:

- “¿Cómo saber si tu piel necesita hidratación o limpieza?”
- “Errores comunes al usar skincare en Bogotá”
- “Orden correcto para usar una rutina facial”
- “¿Para qué sirve cada paso de una rutina de cuidado facial?”
- “¿Puedes usar maquillaje natural después de tu rutina de skincare?”
- “¿Qué crema corporal elegir según tu piel?”

Para **Aurora**, este contenido debe transmitir conocimiento, cuidado y experiencia premium.  
Para **Luna**, debe ser más simple y práctico: “cómo usarla”, “cuándo usarla”, “qué beneficios da”.

---

### 2. Rutinas paso a paso

A la gente le encanta ver cómo se usa el producto.

Ejemplos:

- “Rutina facial nocturna con Aurora”
- “Rutina matutina en 5 pasos”
- “Cómo aplicar Aurora para piel sensible, mixta o grasa”
- “Rutina corporal rápida con Luna”
- “Rutina facial + maquillaje natural con Sol”

Esto ayuda a que el cliente imagine usando tu producto y reduce la incertidumbre antes de comprar.

---

### 3. Antes y después

Este contenido es muy potente, pero debe usarse con cuidado y honestidad.

Ejemplos:

- “Piel antes y después de 4 semanas usando Aurora”
- “Mi piel antes y después de una rutina de hidratación”
- “Así cambió mi piel al usar skincare constante”

No siempre se puede mostrar un antes/después inmediato, pero sí puedes mostrar:

- Testimonios con fotos reales.
- Resultados a 2, 4 o 8 semanas.
- Cambios en textura, luminosidad, hidratación o sensación de la piel.

Para **Aurora**, este tipo de contenido es clave porque justifica el precio premium.

---

### 4. Testimonios y prueba social

En skincare, la confianza es fundamental. La gente quiere saber que otros clientes realmente lo usan y les funciona.

Ejemplos:

- “Lo que dicen nuestras clientas en Bogotá”
- “Testimonio de una clienta que usó Aurora por 30 días”
- “Preguntas frecuentes de nuestras clientas”
- “Capturas de WhatsApp o reseñas”
- “UGC: clientas mostrando su rutina”

También puedes usar contenido tipo:

- “Esta clienta buscaba hidratación y eligió Luna”
- “Esta clienta quería una rutina facial premium y usó Aurora”
- “Esta clienta buscaba maquillaje natural y eligió Sol”

Esto te ayuda a posicionar tu tienda como una opción cercana y confiable frente a **Botica Verde** y **Skin Lab**.

---

### 5. Educación sobre ingredientes

Aunque no todos los clientes entienden química, sí les gusta saber qué llevan los productos.

Ejemplos:

- “Ingredientes que ayudan a hidratar la piel”
- “¿Qué significa piel sensible?”
- “Ingredientes suaves para rutinas de cuidado facial”
- “¿Por qué la hidratación es importante en el clima de Bogotá?”
- “Ingredientes que pueden ayudar con piel opaca”

Para **Aurora**, puedes hacer contenido más premium y detallado.  
Para **Luna**, puedes hacerlo más simple: “hidrata”, “suaviza”, “deja la piel confortable”.

---

### 6. Mitos y verdades

Este contenido funciona muy bien porque genera interacción.

Ejemplos:

- “Mito: si tienes piel grasa no necesitas hidratación”
- “Mito: el skincare solo es para personas con muchos problemas”
- “Mito: una crema corporal de precio entrada no puede ser buena”
- “Verdad: la constancia es más importante que usar muchos productos”
- “Mito: el maquillaje natural no necesita rutina previa”

Esto posiciona a tu marca como experta, pero cercana.

---

### 7. Contenido de rutina y estilo de vida

No todo debe ser producto. También funciona mostrar el momento de autocuidado.

Ejemplos:

- “Mi rutina nocturna en Bogotá”
- “Momento de autocuidado antes de dormir”
- “Rutina facial después de un día largo”
- “Cómo armar una rutina facial según tu presupuesto”
- “Skincare para quienes no tienen mucho tiempo”

Esto conecta emocionalmente con tu audiencia.

---

### 8. Contenido comparativo suave

No ataques a **Botica Verde** ni a **Skin Lab** directamente, pero sí puedes ayudar a la clienta a elegir.

Ejemplos:

- “¿Set de cuidado facial o rutina individual?”
- “¿Cremas corporales de precio entrada, medio o premium?”
- “¿Cómo elegir entre skincare básico y premium?”
- “¿Maquillaje natural sí o no?”
- “¿Qué producto elegir según tu necesidad?”

Esto es muy útil porque muchas personas no saben qué comprar.

---

### 9. Contenido de preguntas frecuentes

Este contenido ayuda a reducir objeciones antes de la compra.

Ejemplos:

- “¿Aurora sirve para piel sensible?”
- “¿Luna se puede usar todos los días?”
- “¿Sol es apto para principiantes en maquillaje natural?”
- “¿Hacen envíos en Bogotá?”
- “¿Cómo sé si un producto es para mí?”
- “¿Puedo combinar Aurora con Sol?”

Esto también te sirve para WhatsApp y email.

---

### 10. Contenido de venta suave

No siempre tienes que vender directamente. A veces funciona mejor mostrar el producto en contexto.

Ejemplos:

- “Así se ve Aurora en una rutina nocturna”
- “Mi favorito para hidratar el cuerpo: Luna”
- “Si quieres algo natural, mira Sol”
- “Combo ideal para empezar en skincare”
- “Producto recomendado para piel opaca”

Para **Luna**, que es precio de entrada, puedes usar más venta directa:

- “Perfecta para empezar”
- “Precio accesible”
- “Fácil de incorporar a tu rutina”

Para **Aurora**, la venta debe ser más emocional y premium:

- “Rutina completa”
- “Cuidado facial premium”
- “Experiencia de autocuidado”
- “Resultados visibles con constancia”

---

## Mi recomendación por producto

### Para **Aurora** — set de cuidado facial premium

El contenido debe transmitir:

- Confianza.
- Profesionalismo.
- Resultados.
- Experiencia premium.
- Cuidado.

Mejores formatos:

- Rutinas paso a paso.
- Testimonios.
- Antes y después.
- Educación sobre piel.
- Contenido de “experiencia de uso”.
- Mensajes personalizados en WhatsApp.

Ejemplo de mensaje:

> “Si buscas una rutina facial completa que hidrate, ilumine y deje tu piel con mejor textura, Aurora está diseñado para eso.”

---

### Para **Sol** — kit de maquillaje natural precio medio

El contenido debe transmitir:

- Naturalidad.
- Fácil uso.
- Belleza cercana.
- Producto para el día a día.

Mejores formatos:

- Antes y después de maquillaje.
- Tips de maquillaje natural.
- Looks fáciles.
- Reels de aplicación.
- Contenido tipo “cómo usarlo”.
- Testimonios de clientas que quieren algo natural.

Ejemplo de mensaje:

> “Si quieres verte bien sin maquillaje pesado, Sol es tu kit ideal.”

---

### Para **Luna** — crema corporal precio entrada

El contenido debe transmitir:

- Accesibilidad.
- Hidratación.
- Uso diario.
- Compra fácil.
- Buen precio.

Mejores formatos:

- Tips rápidos.
- Rutina corporal.


### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo



Para diferenciarte de **Botica Verde** y **Skin Lab** sin entrar en guerra de precios, tu ventaja no debería ser “ser más barata”, sino **ser más clara, cercana y útil** para la clienta bogotana que quiere elegir skincare, maquillaje natural o cuidado corporal sin sentirse perdida.

Tu diferenciación puede basarse en **experiencia, educación, servicio y posicionamiento por necesidad**, no solo en precio.

---

## 1. Posiciona tu tienda como “la que te ayuda a elegir”

En vez de vender solo productos, puedes posicionarte como una tienda que ayuda a armar una rutina según la necesidad, el presupuesto y el estilo de vida de la clienta.

Tu diferenciador podría ser:

> “En Bogotá, te ayudamos a elegir tu rutina de belleza ideal: skincare, maquillaje natural y cuidado corporal, con opciones desde entrada hasta premium.”

Esto te separa de competidores que solo venden producto. Tú vendes **claridad**.

### Ejemplo de mensaje

> “No necesitas más productos, necesitas saber cuáles son los correctos. En nuestra tienda te ayudamos a elegir entre Aurora, Sol y Luna según tu piel, tu presupuesto y tu rutina.”

Esto es poderoso porque muchas clientas no saben qué comprar.

---

## 2. Diferénciate por experiencia, no por precio

Si **Aurora** es premium, no lo defiendas solo por calidad. Defiéndelo por la experiencia que ofrece.

### Para Aurora

Puedes comunicar que no es solo un set de cuidado facial, sino una **rutina completa de autocuidado**.

Mensajes posibles:

> “Aurora es una rutina facial premium pensada para quienes quieren cuidar su piel de forma constante, con pasos claros y una experiencia de uso más cuidada.”

> “No vendemos solo productos: te damos una rutina completa para que sepas qué usar, cuándo usarlo y en qué orden.”

Esto justifica el precio premium sin entrar en comparación directa.

### Para Sol

Puedes posicionarte como la opción de **maquillaje natural fácil y cercano**.

> “Sol es para quienes quieren verse bien sin cargar con maquillaje pesado. Natural, práctico y pensado para el día a día en Bogotá.”

### Para Luna

Puedes posicionarte como la **opción accesible para empezar**.

> “Luna es perfecta si quieres hidratar tu cuerpo sin complicaciones y con un precio de entrada.”

Así cada producto tiene un rol claro:

- **Aurora:** premium, rutina completa, experiencia.
- **Sol:** natural, práctico, día a día.
- **Luna:** accesible, entrada, hidratación básica.

---

## 3. Ofrece asesoría cercana en WhatsApp

Un gran diferenciador para una tienda online en Bogotá es la **atención personalizada**.

Tus competidores pueden tener productos similares, pero tú puedes ofrecer una experiencia más humana.

### Ejemplo de diferenciador

> “Escríbenos por WhatsApp y te ayudamos a elegir el producto ideal según tu tipo de piel, tu presupuesto y tu rutina.”

Puedes crear etiquetas como:

- Piel seca.
- Piel grasa.
- Piel sensible.
- Busca skincare premium.
- Busca maquillaje natural.
- Busca producto de entrada.
- Primera compra.
- Clienta recurrente.

Esto te permite enviar mensajes más personalizados:

> “Hola, vi que te interesa una rutina facial. Si buscas algo más completo y premium, Aurora puede ser ideal. Si prefieres empezar con algo más sencillo, Luna puede ser una buena opción para hidratación corporal.”

Esto no es solo venta, es **asesoría**.

---

## 4. Crea contenido que eduque, no solo que venda

Tus competidores pueden mostrar productos, pero tú puedes mostrar **cómo resolver problemas de belleza**.

Contenido que te diferencia:

- “¿Cómo saber si tu piel necesita hidratación o limpieza?”
- “¿Qué rutina facial usar si tienes poco tiempo?”
- “¿Maquillaje natural sí o no?”
- “¿Cómo elegir una crema corporal según tu piel?”
- “Rutina facial para Bogotá: clima seco, frío o húmedo”
- “¿Aurora, Sol o Luna? Te ayudamos a elegir”
- “Errores comunes al empezar una rutina de skincare”
- “Skincare para principiantes”
- “Maquillaje natural para el día a día”

Esto posiciona a tu tienda como una marca que **entiende a la clienta**, no solo que vende producto.

---

## 5. Usa comparativas suaves, sin atacar a la competencia

No necesitas mencionar directamente a **Botica Verde** ni a **Skin Lab**. Puedes crear contenido comparativo entre necesidades, presupuestos o estilos.

### Ejemplos

> “¿Prefieres una rutina facial completa o productos sueltos?”

> “¿Buscas algo premium o quieres empezar con una opción de entrada?”

> “¿Quieres maquillaje natural o skincare más enfocado en la piel?”

> “¿Cómo elegir entre una crema corporal básica y una rutina facial premium?”

Esto ayuda a la clienta a decidir sin que tú tengas que decir quién es mejor.

---

## 6. Crea combos estratégicos

Los combos te permiten subir el ticket promedio sin bajar precios.

### Combos posibles

#### Combo “Inicio”
- **Luna**
- Ideal para: primera compra, precio de entrada, hidratación corporal.
- Mensaje:
  > “Empieza tu rutina de cuidado corporal con Luna, nuestra opción de entrada.”

#### Combo “Rutina Natural”
- **Sol + Luna**
- Ideal para: clientas que quieren maquillaje natural y cuidado corporal.
- Mensaje:
  > “Arma tu rutina natural: maquillaje con Sol e hidratación corporal con Luna.”

#### Combo “Premium Facial”
- **Aurora**
- Ideal para: clientas que buscan una rutina facial completa.
- Mensaje:
  > “Si quieres una experiencia facial más completa, Aurora es tu rutina premium.”

#### Combo “Rutina Completa”
- **Aurora + Luna**
- Ideal para: clientas que quieren cuidar rostro y cuerpo.
- Mensaje:
  > “Cuida tu rostro con Aurora y tu cuerpo con Luna. Una rutina completa para tu autocuidado.”

#### Combo “Natural Completo”
- **Aurora + Sol + Luna**
- Ideal para: ticket alto, regalo, lanzamiento, temporada.
- Mensaje:
  > “Tu rutina completa: skincare facial, maquillaje natural e hidratación corporal.”

Esto te permite competir por **valor percibido**, no por precio.

---

## 7. Ofrece una experiencia postventa

Muchas tiendas online venden y desaparecen. Tú puedes diferenciarte por lo que pasa después de la compra.

### Acciones postventa

- Mensaje de agradecimiento.
- Guía rápida de uso.
- Recordatorio para aplicar el producto.
- Pregunta por resultados a los 7, 14 o 30 días.
- Solicitud de testimonio.
- Oferta para recompra.
- Sugerencia de próximo producto.

### Ejemplo para Aurora

> “Hola, tu Aurora llegó. Para obtener mejores resultados, úsalo por la noche durante 4 semanas. En unos días te escribimos para saber cómo te está sintiendo tu piel.”

### Ejemplo para Luna

> “Hola, tu Luna llegó. Aplícala después de la ducha. Si te gusta, en 2-3 meses te recordamos que es momento de recomprar.”

### Ejemplo para Sol

> “Hola, tu Sol llegó. Si quieres, te enviamos un tip para usarlo en el día a día. ¿Te gustaría un look natural o más definido?”

Esto crea cercanía y fidelización.

---

## 8. Aprovecha que estás en Bogotá

Aunque sea online, puedes usar la cercanía local como diferenciador.

### Mensajes locales

> “Tienda online de belleza en Bogotá.”

> “Entregamos en Bogotá.”

> “Rutinas de belleza pensadas para el día a día bogotano.”

> “Atención cercana para clientas en Bogotá.”

Puedes usar contenido como:

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo



Para el **primer trimestre**, no te recomendaría medir todo desde el día uno. Lo ideal es que midas lo suficiente para tomar decisiones, pero sin complicarte. Tu objetivo en Q1 debería ser:

1. **Validar qué producto funciona mejor.**
2. **Identificar qué canal trae mejor retorno.**
3. **Construir una base de clientes y datos.**
4. **Medir si tu propuesta de valor realmente convierte.**
5. **Entender tu rentabilidad inicial.**

Te dejo los KPIs que te recomiendo medir, organizados por área.

---

# 1. KPIs de ventas

Estos son los más importantes para saber si el negocio está funcionando.

| KPI | Fórmula | Por qué medirlo |
|---|---|---|
| **Ingresos totales** | Suma de ventas | Para saber si estás generando flujo. |
| **Ventas por producto** | Ingresos de Aurora, Sol y Luna por separado | Para saber cuál es tu motor de ventas. |
| **Ticket promedio** | Ingresos totales / número de pedidos | Te dice cuánto gasta en promedio una clienta. |
| **Número de pedidos** | Total de compras realizadas | Te permite entender volumen real. |
| **Unidades vendidas por producto** | Cantidad vendida de Aurora, Sol y Luna | Te ayuda a ver si un producto es popular pero de bajo valor o viceversa. |
| **Tasa de conversión web** | Pedidos / visitas al sitio | Te dice cuántas personas que llegan realmente compran. |
| **Tasa de conversión por canal** | Pedidos atribuidos a cada canal / tráfico o interacción del canal | Para saber qué canal convierte mejor. |
| **Tasa de abandono de carrito** | Carritos abandonados / carritos iniciados | Te ayuda a detectar fricción en la compra. |
| **Recompra en 30 días** | Clientas que compran de nuevo en 30 días / total clientas nuevas | Muy importante para skincare y cuidado corporal. |
| **Recompra en 60 días** | Clientas que compran de nuevo en 60 días / total clientas | Te da una idea más real de retención. |

---

# 2. KPIs de adquisición

Estos te dicen si estás llegando a la gente correcta y a qué costo.

| KPI | Fórmula | Por qué medirlo |
|---|---|---|
| **Tráfico total** | Visitas al sitio | Para entender alcance. |
| **Tráfico por canal** | Visitas desde Instagram, TikTok, Google, WhatsApp, email, etc. | Para saber qué canal te trae gente. |
| **Costo por clic** | Inversión en pauta / clics | Para medir eficiencia de Meta, Google u otros. |
| **Costo por adquisición** | Inversión en pauta / ventas atribuidas | Es clave para saber si la pauta es rentable. |
| **ROAS** | Ingresos atribuidos a pauta / inversión en pauta | Te dice cuántos pesos recuperas por cada peso invertido. |
| **CTR de anuncios** | Clics / impresiones | Te dice si tu creativo o mensaje interesa. |
| **CTR de contenido orgánico** | Clics / impresiones o interacciones | Para saber qué contenido realmente genera interés. |
| **Costo por lead** | Inversión / leads generados | Si usas WhatsApp, formularios o capturas de email. |
| **Costo por lead por canal** | Inversión en canal / leads del canal | Para saber qué canal trae mejores prospectos. |

---

# 3. KPIs de contenido y redes

Como vas a usar Instagram, TikTok, WhatsApp y quizá email, necesitas medir si el contenido está generando interés.

| KPI | Fórmula | Por qué medirlo |
|---|---|---|
| **Alcance orgánico** | Personas que vieron tu contenido | Para saber cuánta gente te está descubriendo. |
| **Seguidores nuevos** | Nuevos seguidores en el periodo | Para medir crecimiento de audiencia. |
| **Tasa de interacción** | Likes + comentarios + guardados + compartidos / alcance | Te dice si el contenido resuena. |
| **Guardados por publicación** | Total de guardados | Muy importante en belleza y skincare. |
| **Compartidos por publicación** | Total de compartidos | Indica que el contenido tiene valor o resuena. |
| **Clics en perfil** | Personas que fueron a tu perfil | Muestra interés en conocer más. |
| **Clics a enlace en bio** | Clics al link | Indica intención de compra. |
| **Vistas de reels/TikTok** | Total de vistas | Para entender qué tipo de video funciona. |
| **Duración promedio de video** | Tiempo que ven el video | Te dice si tu contenido retiene atención. |
| **Comentarios por publicación** | Total de comentarios | Te ayuda a detectar preguntas y objeciones. |

Para tus productos, yo mediría especialmente:

- **Aurora:** guardados, comentarios, mensajes por WhatsApp y conversión.
- **Sol:** vistas, compartidos, comentarios y clics a producto.
- **Luna:** clics, carritos iniciados, conversiones y recompra.

---

# 4. KPIs de WhatsApp y atención al cliente

Como WhatsApp será clave para convertir, debes medirlo.

| KPI | Fórmula | Por qué medirlo |
|---|---|---|
| **Mensajes recibidos** | Total de conversaciones iniciadas | Para entender interés. |
| **Tasa de respuesta** | Conversaciones respondidas / mensajes recibidos | Mide capacidad de atención. |
| **Tiempo promedio de respuesta** | Tiempo total de respuesta / conversaciones | Importante para no perder ventas. |
| **Conversaciones por producto** | Mensajes donde preguntan por Aurora, Sol o Luna | Te dice qué producto genera más interés. |
| **Conversión por WhatsApp** | Ventas cerradas por WhatsApp / conversaciones | Mide la efectividad del canal. |
| **Ticket promedio por WhatsApp** | Ingresos por WhatsApp / ventas por WhatsApp | Te dice si WhatsApp cierra ventas de mayor valor. |
| **Clientes que preguntan y no compran** | Conversaciones sin venta | Para identificar objeciones. |
| **Motivos de abandono** | Razón por la que no compran | Precio, duda, envío, confianza, etc. |

---

# 5. KPIs de email y CRM

Aunque apenas estés empezando, en el primer trimestre ya deberías empezar a construir base de datos.

| KPI | Fórmula | Por qué medirlo |
|---|---|---|
| **Suscriptores nuevos** | Nuevos emails o contactos | Para medir crecimiento de base. |
| **Tasa de apertura** | Aperturas / correos enviados | Mide interés por tu marca. |
| **CTR de email** | Clics / correos enviados | Mide intención de comprar. |
| **Ingresos por email** | Ventas atribuidas a email | Mide rentabilidad del canal. |
| **Recompra por email** | Ventas de recompra / clientes en base | Muy importante para skincare. |
| **Tasa de desuscripción** | Desuscripciones / correos enviados | Te alerta si estás enviando contenido poco relevante. |

---

# 6. KPIs de retención y fidelización

En skincare y cuidado corporal, la recompra es clave. Si solo mides ventas nuevas, puedes perder la visión de rentabilidad a mediano plazo.

| KPI | Fórmula | Por qué medirlo |
|---|---|---|
| **Clientes nuevos** | Primeras compras en el trimestre | Para entender crecimiento. |
| **Clientes recurrentes** | Clientes que compran 2 o más veces | Para medir fidelidad. |
| **Porcentaje de recompra** | Clientes recurrentes / total clientes | Te dice si tu base está volviendo. |
| **Frecuencia de compra** | Total pedidos / total clientes | Te dice con qué frecuencia compran. |
| **Valor de vida

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

El usuario pide un plan de campaña de 4 semanas enfocado exclusivamente en su producto más caro. Según el contexto:
- Producto más caro: "Aurora", set de cuidado facial, precio premium.
- Mercado: Bogotá.
- Competidores: Botica Verde y Skin Lab.
- Propuesta de valor: tienda online bogotana que combina cuidado facial, maquillaje natural y cuidado corporal; ayuda a elegir rutina ideal.
- Canales priorizados: Instagram/Meta, WhatsApp, TikTok, Google, email.
- Frecuencia orgánica: Instagram 4-5/semana, TikTok 3-4/semana, WhatsApp 1 promo/semana + estados, Google 1 contenido/semana, email 1/semana.
- KPIs primer trimestre: ventas, ticket promedio, conversión, CAC, ROAS, recompra, etc.
- Diferenciación: no guerra de precios, sino claridad, cercanía, asesoría, experiencia premium, educación, prueba social, postventa.

Debo ser específica con el nombre "Aurora" en todo el plan. El usuario pidió: objetivo, audiencia, canales, mensaje principal y métricas de éxito. Debo hacer un plan de 4 semanas. Debo usar datos del contexto sin preguntar. Debo responder en español.

Necesito estructurar bien:
- Nombre de campaña probablemente centrada en Aurora.
- Objetivo específico, medible.
- Audiencia: Bogotá, intereses skincare, premium, edad, dolor, segmentación.
- Canales: Instagram/Meta principal, WhatsApp, TikTok, Google, email.
- Mensaje principal: diferenciador, premium, rutina completa, confianza, Bogotá, no guerra de precios.
- Plan semana a semana: objetivo de la semana, acciones, contenido, pauta, WhatsApp, email, métricas.
- Métricas de éxito: ventas de Aurora, leads, CAC, ROAS, conversión, recompra, mensajes, etc.
- Puede incluir presupuesto? No lo pidió, pero puede ser útil. Debo no inventar cifras específicas de precio porque no las conoce. Puedo usar porcentajes o rangos relativos.
- Debo evitar mencionar a competidores directamente en mensajes públicos.
- Debo ser específica con nombre del producto: Aurora.
- Tal vez incluir embudo: descubrimiento, consideración, conversión, postventa.
- Debo mantener coherencia con canales y frecuencias.
- Debo usar formato claro, tablas quizá.
- Debo ser asistente que ayuda a planificar campañas.

Posible respuesta:
"Campaña: Aurora, tu rutina facial premium en Bogotá"
Objetivo: en 4 semanas, generar X ventas de Aurora, X leads, CAC, ROAS. Como no tengo presupuesto, puedo poner objetivo por ejemplo: "llegar a 30-50 ventas de Aurora" pero sería inventar. Mejor poner objetivos como placeholders? El usuario pidió específico. Podría proponer metas sugeridas: 40 ventas de Aurora, 150 leads, ROAS 3-4x, CAC máximo 30% del ticket. Pero si no conoce ticket, podría decir "ajustar según ticket". Pero pidió específico; puedo proponer metas de ejemplo basadas en un primer trimestre. Debo ser cuidadoso: "propongo estas metas iniciales, ajústalas según tu ticket y presupuesto". Pero el usuario dijo "Sé específica con el nombre del producto en todo el plan", no necesariamente con cifras. Puedo dar métricas de éxito con umbrales.

Audiencia:
- Principal: mujeres 25-45 en Bogotá, interesadas en skincare, cuidado facial, belleza, autocuidado, rutina nocturna, piel sensible/mixta/seca, compra online, ticket premium.
- Secundaria: 18-30 que quieren empezar rutina facial pero con asesoría; 35-50 que buscan experiencia premium.
- Exclusiones: solo busca descuentos? No necesariamente.
- Lookalikes si tiene base.
- Retargeting: visitantes, carrito, Instagram, WhatsApp.

Mensaje principal:
"Aurora es la rutina facial premium en Bogotá para quienes quieren cuidar su piel con pasos claros, constancia y una experiencia de uso más cuidada."
O: "Aurora: tu rutina facial completa, premium y cercana, pensada para Bogotá."
Debe diferenciar sin guerra de precios: "No es el set más barato, es el set que te ayuda a no equivocarte."
Puede tener ángulos:
1. Claridad: "No necesitas 10 productos, necesitas una rutina que funcione."
2. Premium: "Cuidado facial premium con experiencia cercana."
3. Bogotá: "Pensado para tu piel y tu rutina en Bogotá."
4. Confianza: "Te acompañamos antes, durante y después."

Canales:
- Instagram/Meta: 60% presupuesto.
- WhatsApp: 15%.
- TikTok: 15%.
- Google: 10%.
- Email: 5%? O no presupuesto, solo soporte.
Pero debe ser plan de campaña, no solo orgánico. Incluir pauta.

Plan 4 semanas:
Semana 1: Lanzamiento/educación "¿Por qué Aurora?"
- Objetivo: generar conciencia y leads.
- Contenido: 3 reels, 2 carruseles, 1 guía, WhatsApp estados, email.
- Pauta: prospecting + retargeting suave.
- Métricas: alcance, CTR, leads, CAC lead.

Semana 2: Prueba social y educación "Aurora en 30 días"
- Objetivo: consideración.
- Contenido: testimonios, antes/después, rutina paso a paso, FAQ.
- Pauta: retargeting.
- WhatsApp: asesoría.
- Métricas: guardados, comentarios, conversaciones, carritos.

Semana 3: Conversión "Aurora, tu rutina premium"
- Objetivo: ventas.
- Contenido: oferta, combo? Pero exclusivamente Aurora, no otros productos. Puede ofrecer guía de uso o asesoría gratuita, no descuento agresivo. "Compra Aurora y recibe guía de rutina + asesoría por WhatsApp".
- Pauta: retargeting fuerte, Google Shopping.
- WhatsApp: cierres.
- Email: secuencia.
- Métricas: ventas, ROAS, CAC, conversión.

Semana 4: Postventa y recompra/última oportunidad
- Objetivo: cerrar pendientes y fidelizar.
- Contenido: testimonios de compradoras, UGC, última oportunidad, postventa.
- Pauta: retargeting carrito y compradores? Para recompra quizá no en 4 semanas para Aurora, pero sí postventa.
- WhatsApp: seguimiento a 7 días.
- Email: gracias + guía + testimonio.
- Métricas: ventas, NPS, testimonios, recompra a 30 días (seguimiento).

Métricas de éxito:
- Ventas de Aurora: meta sugerida 30-50? Mejor: "Meta inicial: 40 ventas de Aurora en 4 semanas, ajustable según presupuesto". Pero si no hay presupuesto, podría decir "objetivo de prueba: 20-30 ventas". Debo ser específica pero no inventar? Como asistente, puedo proponer. Para que sea útil, propongo "meta de campaña: 30 ventas de Aurora" y "lead: 150". Pero si no tiene base, puede ser alto. Tal vez mejor: "Meta mínima: 15 ventas; meta ideal: 30; meta stretch: 50". Eso es específico y flexible.
- Leads: 100-200.
- CAC: no superar 30% del ticket promedio de Aurora.
- ROAS: 3x-5x.
- Conversión web: 1.5%-3% para retargeting, 0.5%-1% prospecting.
- WhatsApp: 40 conversaciones, 20% conversión.
- Email: 25% apertura, 3% CTR.
- Contenido: 100k alcance? Depende. Mejor: 50k-100k impresiones, 2% interacción.
- Postventa: 70% tasa de respuesta, 5 testimonios.

Debo incluir "métricas de éxito" claras, quizá tablas por semana y por KPI.

También debo incluir "mensaje principal" quizá una matriz de mensajes por semana.

Asegurar que en todo el plan se mencione Aurora. No usar "el producto más caro" después de definirlo. Usar Aurora siempre.

Posible estructura final:
1. Nombre de campaña
2. Producto
3. Objetivo de campaña
4. Audiencia
5. Posicionamiento/mensaje principal
6. Canales y distribución
7. Plan 4 semanas (tablas)
8. Métricas de éxito
9. Reglas para no caer en guerra de precios
10. Siguiente paso.

Debo no hacer demasiado largo? El desired oververbosity 9, así que detallado. Pero el usuario pidió plan, así que bien.

Necesito no mencionar que no tengo datos? Puedo decir "como metas iniciales". No preguntar.

Voy a redactar en español.

Detalles:
- Objetivo: "Posicionar Aurora como


## Respuesta completa

El usuario pide un plan de campaña de 4 semanas enfocado exclusivamente en su producto más caro. Según el contexto:
- Producto más caro: "Aurora", set de cuidado facial, precio premium.
- Mercado: Bogotá.
- Competidores: Botica Verde y Skin Lab.
- Propuesta de valor: tienda online bogotana que combina cuidado facial, maquillaje natural y cuidado corporal; ayuda a elegir rutina ideal.
- Canales priorizados: Instagram/Meta, WhatsApp, TikTok, Google, email.
- Frecuencia orgánica: Instagram 4-5/semana, TikTok 3-4/semana, WhatsApp 1 promo/semana + estados, Google 1 contenido/semana, email 1/semana.
- KPIs primer trimestre: ventas, ticket promedio, conversión, CAC, ROAS, recompra, etc.
- Diferenciación: no guerra de precios, sino claridad, cercanía, asesoría, experiencia premium, educación, prueba social, postventa.

Debo ser específica con el nombre "Aurora" en todo el plan. El usuario pidió: objetivo, audiencia, canales, mensaje principal y métricas de éxito. Debo hacer un plan de 4 semanas. Debo usar datos del contexto sin preguntar. Debo responder en español.

Necesito estructurar bien:
- Nombre de campaña probablemente centrada en Aurora.
- Objetivo específico, medible.
- Audiencia: Bogotá, intereses skincare, premium, edad, dolor, segmentación.
- Canales: Instagram/Meta principal, WhatsApp, TikTok, Google, email.
- Mensaje principal: diferenciador, premium, rutina completa, confianza, Bogotá, no guerra de precios.
- Plan semana a semana: objetivo de la semana, acciones, contenido, pauta, WhatsApp, email, métricas.
- Métricas de éxito: ventas de Aurora, leads, CAC, ROAS, conversión, recompra, mensajes, etc.
- Puede incluir presupuesto? No lo pidió, pero puede ser útil. Debo no inventar cifras específicas de precio porque no las conoce. Puedo usar porcentajes o rangos relativos.
- Debo evitar mencionar a competidores directamente en mensajes públicos.
- Debo ser específica con nombre del producto: Aurora.
- Tal vez incluir embudo: descubrimiento, consideración, conversión, postventa.
- Debo mantener coherencia con canales y frecuencias.
- Debo usar formato claro, tablas quizá.
- Debo ser asistente que ayuda a planificar campañas.

Posible respuesta:
"Campaña: Aurora, tu rutina facial premium en Bogotá"
Objetivo: en 4 semanas, generar X ventas de Aurora, X leads, CAC, ROAS. Como no tengo presupuesto, puedo poner objetivo por ejemplo: "llegar a 30-50 ventas de Aurora" pero sería inventar. Mejor poner objetivos como placeholders? El usuario pidió específico. Podría proponer metas sugeridas: 40 ventas de Aurora, 150 leads, ROAS 3-4x, CAC máximo 30% del ticket. Pero si no conoce ticket, podría decir "ajustar según ticket". Pero pidió específico; puedo proponer metas de ejemplo basadas en un primer trimestre. Debo ser cuidadoso: "propongo estas metas iniciales, ajústalas según tu ticket y presupuesto". Pero el usuario dijo "Sé específica con el nombre del producto en todo el plan", no necesariamente con cifras. Puedo dar métricas de éxito con umbrales.

Audiencia:
- Principal: mujeres 25-45 en Bogotá, interesadas en skincare, cuidado facial, belleza, autocuidado, rutina nocturna, piel sensible/mixta/seca, compra online, ticket premium.
- Secundaria: 18-30 que quieren empezar rutina facial pero con asesoría; 35-50 que buscan experiencia premium.
- Exclusiones: solo busca descuentos? No necesariamente.
- Lookalikes si tiene base.
- Retargeting: visitantes, carrito, Instagram, WhatsApp.

Mensaje principal:
"Aurora es la rutina facial premium en Bogotá para quienes quieren cuidar su piel con pasos claros, constancia y una experiencia de uso más cuidada."
O: "Aurora: tu rutina facial completa, premium y cercana, pensada para Bogotá."
Debe diferenciar sin guerra de precios: "No es el set más barato, es el set que te ayuda a no equivocarte."
Puede tener ángulos:
1. Claridad: "No necesitas 10 productos, necesitas una rutina que funcione."
2. Premium: "Cuidado facial premium con experiencia cercana."
3. Bogotá: "Pensado para tu piel y tu rutina en Bogotá."
4. Confianza: "Te acompañamos antes, durante y después."

Canales:
- Instagram/Meta: 60% presupuesto.
- WhatsApp: 15%.
- TikTok: 15%.
- Google: 10%.
- Email: 5%? O no presupuesto, solo soporte.
Pero debe ser plan de campaña, no solo orgánico. Incluir pauta.

Plan 4 semanas:
Semana 1: Lanzamiento/educación "¿Por qué Aurora?"
- Objetivo: generar conciencia y leads.
- Contenido: 3 reels, 2 carruseles, 1 guía, WhatsApp estados, email.
- Pauta: prospecting + retargeting suave.
- Métricas: alcance, CTR, leads, CAC lead.

Semana 2: Prueba social y educación "Aurora en 30 días"
- Objetivo: consideración.
- Contenido: testimonios, antes/después, rutina paso a paso, FAQ.
- Pauta: retargeting.
- WhatsApp: asesoría.
- Métricas: guardados, comentarios, conversaciones, carritos.

Semana 3: Conversión "Aurora, tu rutina premium"
- Objetivo: ventas.
- Contenido: oferta, combo? Pero exclusivamente Aurora, no otros productos. Puede ofrecer guía de uso o asesoría gratuita, no descuento agresivo. "Compra Aurora y recibe guía de rutina + asesoría por WhatsApp".
- Pauta: retargeting fuerte, Google Shopping.
- WhatsApp: cierres.
- Email: secuencia.
- Métricas: ventas, ROAS, CAC, conversión.

Semana 4: Postventa y recompra/última oportunidad
- Objetivo: cerrar pendientes y fidelizar.
- Contenido: testimonios de compradoras, UGC, última oportunidad, postventa.
- Pauta: retargeting carrito y compradores? Para recompra quizá no en 4 semanas para Aurora, pero sí postventa.
- WhatsApp: seguimiento a 7 días.
- Email: gracias + guía + testimonio.
- Métricas: ventas, NPS, testimonios, recompra a 30 días (seguimiento).

Métricas de éxito:
- Ventas de Aurora: meta sugerida 30-50? Mejor: "Meta inicial: 40 ventas de Aurora en 4 semanas, ajustable según presupuesto". Pero si no hay presupuesto, podría decir "objetivo de prueba: 20-30 ventas". Debo ser específica pero no inventar? Como asistente, puedo proponer. Para que sea útil, propongo "meta de campaña: 30 ventas de Aurora" y "lead: 150". Pero si no tiene base, puede ser alto. Tal vez mejor: "Meta mínima: 15 ventas; meta ideal: 30; meta stretch: 50". Eso es específico y flexible.
- Leads: 100-200.
- CAC: no superar 30% del ticket promedio de Aurora.
- ROAS: 3x-5x.
- Conversión web: 1.5%-3% para retargeting, 0.5%-1% prospecting.
- WhatsApp: 40 conversaciones, 20% conversión.
- Email: 25% apertura, 3% CTR.
- Contenido: 100k alcance? Depende. Mejor: 50k-100k impresiones, 2% interacción.
- Postventa: 70% tasa de respuesta, 5 testimonios.

Debo incluir "métricas de éxito" claras, quizá tablas por semana y por KPI.

También debo incluir "mensaje principal" quizá una matriz de mensajes por semana.

Asegurar que en todo el plan se mencione Aurora. No usar "el producto más caro" después de definirlo. Usar Aurora siempre.

Posible estructura final:
1. Nombre de campaña
2. Producto
3. Objetivo de campaña
4. Audiencia
5. Posicionamiento/mensaje principal
6. Canales y distribución
7. Plan 4 semanas (tablas)
8. Métricas de éxito
9. Reglas para no caer en guerra de precios
10. Siguiente paso.

Debo no hacer demasiado largo? El desired oververbosity 9, así que detallado. Pero el usuario pidió plan, así que bien.

Necesito no mencionar que no tengo datos? Puedo decir "como metas iniciales". No preguntar.

Voy a redactar en español.

Detalles:
- Objetivo: "Posicionar Aurora como