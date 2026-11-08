# MiniMax M3.1 Flash — agent_long_horizon/implicit_state_construction

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 978.048s | tokens_per_second: 15.3
- input_tokens: 16927 | output_tokens: 26681

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Sí, Camila, queda claro el contexto:

- **Negoio:** tienda online en Colombia.
- **Mercado actual:** únicamente **Bogotá**.
- **Productos:**
  - **Aurora:** set de cuidado facial, precio **premium**.
  - **Sol:** kit de maquillaje natural, precio **medio**.
  - **Luna:** crema corporal, precio **entrada**.
- **Competidores principales:** **Botica Verde** y **Skin Lab**, ambos.TargetLng: es.
- **TargetLng: es.

Usaré estos datos para ayudarte a planificar campañas y resolver referencias posteriores sin que tengas que repetirlos.

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

En nuestra tienda online en Bogotá ofrecemos opciones de cuidado personal y belleza para distintas necesidades y presupuestos: **Luna** para entrar, **Sol** paraußwahl—mal makeup natural y **Aurora** para el cuidado facial premium. Así puedes comparar y elegir el producto ideal desde un solo canal, con una experiencia sencilla y precios acordes a cada categoría.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Para tu tienda, priorizaría un modelo de **descubrimiento + intención de compra + retención**, segmentado estrictamente a **Bogotá**.

### 1. Instagram como canal principal
Combinaría contenido orgánico y publicidad en Meta:

- **Aurora:** educación sobre rutinas, texturas y propuesta premium.
- **Sol:** tutoriales, demostraciones y contenido generado por usuarios.
- **Luna:** publicaciones simples, beneficios y ofertas de entrada.
- Historias, reels, carretes y colaboraciones con microcreadores de belleza de Bogotá.

Instagram permite mostrar bien los productos y crear confianza antes de la compra.

### 2. TikTok para probar y escalar contenido
Lo utilizaría como complemento de Instagram, publicando videos breves y authenticity-driven: rutinas, antes/después, recomendaciones y respuestas a dudas. Si el equipo es pequeño, conviene adaptar contenido de Instagram en lugar de mantener una estrategia totalmente independiente.

### 3. Anuncios en Meta
Serían la principal herramienta de adquisición pagada. Crearía campañas separadas por producto y objetivo:

- Reconocimiento y video para **Aurora**.
- Consideración yTraffic de demostraciones para **Sol**.
- Conversión y ofertas de primera compra para **Luna**.
- Campañas de re-marketing para visitas al sitio, carritos abandonados y compradores de productos relacionados.

La segmentación geográfica debe limitarse a Bogotá y se pueden crear públicos similares a partir de compradores actuales.

### 4. Google Search y Shopping
Es fundamental para captar personas que ya buscan productos de belleza, cuidado facial o maquillaje natural. Recomendaría:

- Campañas de búsqueda separadas por producto.
- Feed de Shopping o Performance Max con **Aurora, Sol y Luna**.
- Campañas de marca para proteger el nombre de la tienda.
- Contenido SEO en el sitio sobre rutinas, tipos de producto y comparativas.

### 5. WhatsApp Business
Lo usaría como canal de cierre y atención, no solo como atención al cliente:

- Catálogo con los tres productos.
- Botones de compra y seguimiento del pedido.
- Recuperación de carritos abandonment.
- Mensajes sobre disponibilidad, usos del producto y cuidados posteriores a la compra.

Los mensajes automáticos deben cumplir las reglas de privacidad y enviarse solo con consentimiento适当.

### 6. Email y collaborations locales
- **Email:** bienvenida, recomendaciones, carritos abandonados,aktur cross-sells y recordatorios de recompra, especialmente para **Luna**.
- **Microcreadores de Bogotá:** prioritariamente creoadores pequeños pero especializados, con códigos o afiliados para medir ventas.

### Distribución inicial sugerida del presupuesto promocional
- **40% Meta Ads**
- **30% Google Search y Shopping**
- **15% creación de contenido y microcreadores**
- **10% email y WhatsApp**
- **5% pruebas de nuevos formatos o canales**

La prioridad sería **Instagram + Meta Ads y Google**, usando TikTok, WhatsApp y email para complementar. Así aprovechas el contenido visual de la belleza, capturas demanda existente y reduces el costo de所长 adquisición mediante segmentación, remarketing ydbc retención.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

TeRecommendaría una cadencia sostenible para un equipo pequeño, con **Instagram como canal principal** y el resto como complemento. No todos los canales necesitan “publicar” con la misma frecuencia:

| Canal | Frecuencia recomendada | Contenido sugerido |
|---|---:|---|
| **Instagram** | **3 reels + 2 carruseles o posts por semana**; historias **3–5 días por semana** | Routines/tutorials, demostraciones de **Aurora** y **Sol**, beneficios de **Luna**, pruebas y contenido local de Bogotá |
| **TikTok** | **3–5 videos por semana** | Antes/después, Tips rápidas, respuestas a dudas y contenido de creadores. Los reels de Instagram pueden adaptarse, aunque conviene ajustar el ritmo y el texto |
| **Sitio web/SEO** | **2 artículos útiles al mes** | Guías de cuidado facial, rutinas de maquillaje natural, Cosmética naturalBogotáán y comparativas. Las páginas de producto y categoría deben actualizarse mensualmente |
| **Email** | **1–2 newsletters al mes** | Nuevos contenidos, recomendaciones, Ventashticas y educación. Los correos de carrito abandonado, bienvenida y poscompra deben activarse según la conducta del usuario |
| **WhatsApp Business** | **1 mensaje informativo o promocional por semana como máximo** | Nuevos productos, consejos de uso y ofertas. El catálogo, los recordatorios y la recuperación de carritos pueden gestionarse automáticamente |
| **YouTube** *(opcional)* | **1 video largo al mes** | Routines completas, reseñas y comparativas. No lo priorizaría hasta validar la demanda en Instagram y TikTok |

### Distribución sugerida del contenido
- **Aurora:** 40% — educación, ingredientes, texturas y rutinas.
- **Sol:** 35% — demostraciones, tutoriales y pruebas de resultado.
- **Luna:** 25% — beneficios, accesibilidad y recomendaciones de uso.

### Ejemplo de semana en Instagram
- **Lunes:** reel educativo sobre Aurora.
- **Martes:** historias con encuesta y preguntas.
- **Miércoles:** carrusel de rutina con Sol.
- **Jueves:** reel de uso o错误 before/después de Luna.
- **Viernes:** carrusel de preguntas frecuentes.
- **Fin de semana:** una demostración más不比/o aspecto близко al producto.

Si el equipo tiene muy poco tiempo, el mínimo viable sería **2 publicaciones y 2 reels semanales en Instagram, 3 videos en TikTok y 1 artículo mensual en el sitio**. Evaluaría el rendimiento durante **6–8 semanas**, priorizando guardados, compartidos, visitas, clics y compras, no solo seguidores.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para **skincare**, el contenido que mejor funciona combina **demostraciones reales, educación y pruebas de confianza**. En tu caso, el foco principal sería **Aurora**; para **Luna**, la estrategia sería más práctica y orientada al uso diario.

### Tipos de contenido prioritarios

1. **Demostración de textura y aplicación**
   - Videos cortos sin filtros ni demasiada producción.
   - Muestran cuánto producto se usa, cómo se extiende y qué textura deja.
   - Para **Aurora**: ventaja clave para justificar su posicionamiento premium.
   - Para **Luna**: aplicación, absorción y uso en distintas zonas.

2. **Rutinas paso a paso**
   - “Cómo integrar Aurora en una rutina de mañana o noche”.
   - “Orden correcto de los productos”.
   - “Errores frecuentes al aplicar cuidado facial”.
   
   Este contenido genera guardados y puede_atomizarake SEO con una intención clara de compra.

3. **Contenido educativo sobrePIO la piel**
   - Cómo limpiar, hidratar y proteger la piel.
   - Diferencias entre aceite, crema, sérum y gel, sin asegurar que un producto sirva para todos.
   - Respuestas a preguntas frecuentes: orden de uso, frecuencia, compatibilidad y conservación.

4. **Ficha transparente del producto**
   - Ingredientes y función de cada uno, según la información técnica verificada.
   - Presentación, empaque, modo de uso y vida útil.
   - En **Aurora**, muestra con detalle por qué es una opción premium: textura, experiencia de uso, concentración o tecnología **solo si están respaldadas por la ficha técnica**.

5. **Reseñas y contenido de clientes**
   - Testimonios en video, unboxing y contenido generado por usuarios.
   - Publica con autorización y sin edición engañosa.
   - Para una marca nueva son más。许氏 clave que las fotos producir demasiadochas y brutales.

6. **Comparativascepts honestas**
   - “Skincare de entrada vs. premium: qué esperas de cada categoría”.
   - “Cómo elegir una crema corporal según tu necesidad y presupuesto”.
   - Evita atribuir ventajas a Botica Verde o Skin Lab sin evidencia verificable.

### Formatos recomendados

| Formato | Uso principal | Ejemplo para tus productos |
|---|---|---|
| **Reels y TikTok** | Demostraciones y educate | “Así se aplica Aurora en 20 segundos” |
| **Carrusel** | Educación y objeciones | “5 errores al ordenar tu rutina de skincare” |
| **Historias** | Interacción y confianza | Encuestas, caja de preguntas y uso real |
| **UGC** | Prueba social | Reseñas de clientas con consentimiento |
| **Blog/SEO** | Búsquedas de alta intención | “Cómo construir una rutina facial sencilla” |
| **Email** | Recordatorio y conversión | Guía de uso de Aurora + recomendaciones relacionadas |

### Distribución sugerida del contenido

- **Aurora:** 60% educación, 25% demostraciones y pruebas, 15% oferta.
- **Luna:** 50% demostración y beneficios prácticos, 30% educación, 20% prueba social y oferta.
- **Sol:** Although it is makeup rather than skincare, use similar demonstration content: application, finish and natural-makeup looks.

### Ejemplos concretos

- **“La textura real de Aurora, sin filtros”**
- **“Aurora en una rutina nocturna: orden paso a paso”**
- **“Qué debes revisar antes de comprar skincare premium”**
- **“ absorbs.Luna se ve: White, como se absorbe en 10 segundos”**
- **“Reseñas sin retoque: qué dicen clientas de Bogotá”**
- **“Skincare para principiantes: tres pasos y nada más”**

En Colombia, evita promesas como “elimina wrinkles”, “cura el acné” o “revierte el envejecimiento”. Usa afirmaciones demostrables, identifica_Testimonios como experiencias personales y menciona el registro sanitario de Invima únicamente si está verificado; la notificación sanitaria no sustituye la evidencia de eficacia.

Como regla general, prioriza el contenido que **enseña a usar el producto y demuestra su experiencia real**: es el que genera guardados, visitas al sitio y compras, no solo interacción.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

La mejor estrategia es **no competir por “el precio más bajo”**, sino hacer que tu tienda sea perceived como **más fácil de elegir, más confiable y con una experiencia más personalizada**. Como ambos competidores también están en Bogotá, el mercado local por sí solo no te diferencia; necesitas una propuesta de marca propia.

## 1. Posicionamiento recomendado

Una propuesta quecould unify tus productos sería:

> **Belleza clara, bien elegida y explicada:** opciones para cada presupuesto y necesidad, con demostraciones reales, orientación honesta y una experiencia cercana en Bogotá.

Tu diferenciación puede construirse sobre cuatro pilares:

1. **Curaduría:**=no vendes un catálogo amplio; ayudas a elegir.
2. **Confianza:**explicas ingredientes, usos, resultados y limitaciones con transparencia.
3. **Experiencia:**la compra en línea se siente TAN personalizada como comprar en una tienda física.
4. **Cercanía:**te especializas en las necesidades y preferencias de tu público de Bogotá.

## 2. Dale un rol diferente a cada producto

| Producto | Rol en la estrategia | communicated diferenciador |
|---|---|---|
| **Aurora** | Producto bandera y máximo valor de marca | Ritual facial premium, education, textures and a complete experience |
| **Sol** | Opción intermedia y de alta demanda visual | Maquillaje natural, easy application and looks that can be explained clearly |
| **Luna** | Producto de entrada, prueba y recompra | Cuidado corporal práctico y accessible para el día a día |

Así construyes una escalera de valor —**entrada, media y premium**— sin depender de descuentos constantes. Aurora puede actuar como producto ancla; Luna facilita comprar por primera vez; Sol ocupa el espacio intermedio.

## 3. Convierte la educación y el servicio en parte del producto

- Crea una guía como **“¿Qué producto es para ti según tu necesidad y presupuesto?”**.
- Ofrece recomendaciones por WhatsApp con criterio humano, no solo respuestas automáticas.
- En cada ficha de producto explica:
  - Para quién es adecuado.
  - Cómo se utiliza.
  - Qué resultados puedes esperar.
  - Ingredientes y atributos verificados.
  - Con qué productos puede combinarse.
  - Preguntas frecuentes y contraindicaciones reales.
- Publica videos sin filtros que muestren **textura, aplicación, acabado y tiempo de absorción**.

Esta orientación puede ser más difícil de copiar que un precio promocional.

## 4. Usa demostraciones y pruebas reales

Para教学楼 de Aurora Sol y Luna, prioriza:

- **UGC:** reseñas y rutinas de clientas de Bogotá.
- Videos de textura y aplicación sin retoques.
- Contenido con distintos tonos de piel, sin prometer resultados universales.
- Unboxings que muestren empaque y experiencia.
- Comparaciones por necesidad: “¿buscas cuidado facial, maquillaje o hidratación corporal?”.
- Sesiones o lives de educación y aplicación.

No menciones directamente a Botica Verde o Skin Lab en tus anuncios. Compara **soluciones y necesidades**, no marcas.

## 5. Protege tu precio con valor añadido

En lugar de bajar precios:

- Agrupa productos en kits solo cuando sean complementarios y se haya verificado su compatibilidad.
- Añade una miniatura, guía de uso,落后的, reparación complementaria o una experiencia de recomendación en lugar de purely discount.
- Crea ediciones de regalo con escritura y empaques(--)دون't know.
- Ofrece Fertilizing Lune como producto de recompra y crea recordatorios de reposición.
- Usa demostraciones, garantía clara y atención humana para justificar el precio premium de Aurora.

No necesitas convertir cada publicación en una oferta. Una proporción razonable sería **70% educación, prueba y entretenimiento; 20% conversión; 10% promoción explícita**.

## 6. exploiting Bogotá sin make an exclusive claim

Como los competidores también operan allí, no puedes afirmar que eres “la única tienda local”. Sí puedes construir cercanía mediante:

- Creadores de belleza de Bogotá que midan resultados reales.
- Historias de clientas capitalinas.
- Pop-ups, workshops o demos en algún punto físico.
- Contenido adaptado a climas,_truthful incluidas las necesidades de piel de tu audiencia.
-ZTONG logistical convenience only if you can deliver it operationally: entregas locales, recogidas o envío rápido.

## 7. Campañas que pueden posicionar tu marca

- **“Elige tu ritual de belleza”**: quiz por necesidad, uso y presupuesto.
- **“La textura real de Aurora”**: demostración sin filtros.
- **“Maquillaje natural en paso a paso”**: tutorial centrado en Sol.
- **“Cuidado corporal que sí cabe en tu rutina”**: contenido funcional de Luna.
- **“Rutinas reales de clientas en Bogotá”**: UGC con consentimiento.
- **“Antes de comprar skincare premium”**: contenido educativo que construya autoridad.

## Plan breve de 90 días

1. **Semanas 1–2:** audita precios, Messages, contenido, promotions, delivery and service of Botica Verde and Skin Lab.
2. **Semanas 3–4:** define positioning, revisa landing pages and creates selector and verified product guides.
3. **Semanas 5–8:** prueba UGC, educational content and creators; measure saves, shares, clicks and sales by product.
4. **Semanas 9–12:** scale the formats and messages that generate qualified visits and purchases; optimize Luna for repeat purchases and Aurora for average order value.

La métrica central no debe ser solo el alcance: observa **conversión, costo de adquisición, valor promedio de pedido, recompra de Luna y porcentaje de ventaswicklung de Aurora**. Así construirás una marca premium por su elección y experiencia, no porque todos los competidores hayan subido sus precios.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para el primer trimestre te recomiendo medir **tres capas**: resultados del negocio, comportamiento de la funnel y señales de marca/cliente. Como estás establishendo una base de medición, el objetivo principal será **instrumentar correctamente, generar un baseline y mejorar sin comprar ventas no rentables**.

## 1. KPIs principales del negocio

| KPI | Qué indica | Cómo medirlo |
|---|---|---|
| **Ingresos netos** | Ventas menos descuentos, anulaciones y devoluciones | Segmentados por producto y canal |
| **Margen de contribución** | Capacidad real de generar utilidad después de costos variables y publicidad | Ingreso neto − productos, empaque, fulfilment, comisiones, envío subsidized y publicidad |
| **Número de pedidos** | Escala comercial | Total y por producto |
| **Clientes nuevos** | Crecimiento de la base | Clientes que nunca han comprado |
| **Tasa de conversión ecommerce** | Eficacia de la tienda | Pedidos ÷ sesiones |
| **Valor promedio de pedido (AOV)** | Capacidad de generar más ingreso por compra | Ingreso neto ÷ pedidos |
| **CAC de cliente nuevo** | Costo de adquisición | Inversión en marketing ÷ clientes nuevos |
| **MER** | Rentabilidad combinada de todo el marketing | Ingreso neto ÷ inversión total en marketing |
| **ROAS por canal** | Rentabilidad específica de Meta, Google, etc. | Ingreso atribuido ÷ inversión publicitaria |
| **Tasa de recompra** | Retención comercial | Clientes con segunda compra ÷ clientes elegibles |

Tu indicador principal podría ser el **margen de contribución**, acompañado de pedidos y clientes nuevos. Los ingresos por sí solos pueden crecer mientras la utilidad baja.

## 2. Embudo de compra

Estos KPIs te capricán dónde está el cuello de botella:

- **Sesiones de la tienda**
- **Tasa de visita a ficha de producto**
- **Tasa de adición al carrito**
- **Tasa de inicio de checkout**
- **Tasa de checkout completado**
- **Tasa de abandono de carrito**
- **Tasa de abandono de checkout**
- **Ingreso por visitante**

Calcula las tasas sobre la misma base. Por ejemplo:

> Tasa de carrito abandonment = 1 − (pedidos con carrito ÷ sesiones con carrito)

Al revisar el embudo, segmenta por **producto, dispositivo, fuente y ubicación**. Como tu mercado objetivo es Bogotá, mide especialmente el tráfico y las conversiones de esa ciudad.

## 3. KPIs por producto

Cada producto cumple un rol diferente, por lo que no conviene evaluarlos todos con la misma métrica.

### Aurora — skincare facial premium

Prioriza:

- Ingresos y margen generados.
- Porcentaje de ventas a precio completo.
- Conversión de su página de producto.
- Valor promedio de pedido.
- Attached rate de otros productos.
- CAC y Contribution margin de clientes que compran Aurora.

Aquí conviene medir más la **rentabilidad y el valor percibido** que el volumen aislado.

### Sol — maquillaje natural

Prioriza:

- CTR de tutorials y demostraciones.
- Conversión de su ficha de producto.
- Unidades vendidas por pedido.
- Attached rate con Aurora o Luna.
- Ventas de kits o combinaciones, si los ofreces.

Su contenido debe juzgarse por **visitas cualificadas y ventas**, no solamente por reproducciones o likes.

### Luna — crema corporal de entrada

Prioriza:

- Porcentaje de clientes nuevos que comienza con Luna.
- Conversión de su página de producto.
- Primera recompra.
- Recompra a 30, 60 y 90 días.
- Margen y costo de adquisición.
- Frecuencia de reposición.

Luna puede funcionar como **producto de entrada y de recompra**, aunque su ROAS inicial sea inferior al de Aurora.

## 4. KPIs de canales

### Meta Ads — Instagram y Facebook

- Inversión.
- Alcance e impresiones.
- CTR.
- CPC.
- Visitas a la tienda.
- Pedidos y clientes nuevos.
- CAC.
- ROAS.
- Frecuencia.
- Conversión por creativo, producto y público.

Las métricas más útiles son **CTR, visitas, CAC, ROAS y contribution margin**. Los seguidores y los likes son secundarios.

### TikTok

- CTR hacia el producto o tienda.
- Visitas calificadas.
- Conversión de la visita.
- CAC y ROAS.
- Ventas generadas por creatividades o códigos.
- Uso posterior del contenido en otras plataformas.

### Google Search y Shopping

- Impresiones y clics.
- CPC.
- Conversión de la búsqueda.
- ROAS.
- Conversión por consulta.
- Tráfico orgánico y conversiones orgánicas.
- Posición media en búsquedas de marca y no marca.

### Email y WhatsApp

- Tasa de clics.
- Conversiones atribuidas.
- Ingreso y margen generados.
- Recuperación de carritos.
- Bajas o bloqueos.
- Tiempo de respuesta.
- Conversión de WhatsApp a pedido.

El **open rate** de email debe ser una métrica secundaria porque los filtros pueden distorsionarlo; prioriza clics y compras.

## 5. Marca, confianza y experiencia del cliente

Estos KPIs son importantes para validar que estás construyendo diferenciación y no solo generando descuentos:

- Número y tasa de reseñas.
- Calificación promedio.
- Volumen de contenido generado por clientas.
- Menciones de marca o demanda de búsqueda de marca.
- Tráfico directo.
- CSAT después de la compra.
- Net Promoter Score o intención de recompra.
- Tasa de devolución o reembolso.
- Quejas relacionadas con producto, entrega o empaque.
- Tiempo de entrega y porcentaje de pedidos entregados a tiempo.

No presentes NPS con muestras muy pequeñas como una tendencia fuerte; úsalo como indicador cualitativo junto con las reseñas y entrevistas.

## 6. Reglas de atribución

Para que los datos sean comparables:

1. Define **ingreso neto** como ventas menos descuentos, anulaciones y devoluciones, manteniendo el IVA separado.
2. Usa UTMs para Meta, Google, TikTok, email, WhatsApp y creadores.
3. Registra correctamente el origen de las compras asistidas.
4. Mide el **MER** para evaluar el negocio en conjunto; no confíes exclusivamente en el ROAS reportado por cada plataforma.
5. Analiza las recompras por **cohortes según la fecha de primera compra**.
6. Asigna también un valor de margen, no solo de ingresos, a cada campaña y producto.

## Cómo organizar el trimestre

### Semanas 1–2: instrumentación
- Configura GA4, Meta Pixel, Google Ads, Search Console y UTMs.
- Verifica que las compras y los márgenes se registren correctamente.
- Define una fuente única para el dashboard.

### Semanas 3–4: baseline
- Calcula durante cuatro semanas los valores iniciales de CAC, conversión, AOV, ROAS y MER.
- Identifica el mayor punto de fuga del embudo.
- No saques conclusiones definitivas con pocos días de datos.

### Semanas 5–8: optimización
- Prioriza el canal, producto y contenido con mayor margen.
- Corrige obstructed la etapa con peor conversión.
- Prueba creatividades, ofertas, guías y combinaciones de producto.
- Comienza a medir las primeras cohortes de recompra.

### Semanas 9–12: escalamiento
- Escala lo que genere margen y no solo ROAS.
- Formaliza las combinaciones que eleven el AOV.
- Reduce inversión en formatos que attractan clicks pero no compran.
- Compara los resultados con el baseline y documenta aprendizajes.

## Los 10 KPIs que miraría en un dashboard único

Si solo puedes controlar un tablero reducido:

1. Ingresos netos.
2. Margen de contribución.
3. Pedidos.
4. Clientes nuevos.
5. Sesiones.
6. Tasa de conversión.
7. Valor promedio de pedido.
8. CAC.
9. MER.
10. Tasa de recompra.

El principal criterio para tomar decisiones debe ser: **¿esta campaña, producto o contenido genera margen después de toda la inversión?** Eso te ayudará a crecer sin entrar en una guerra de precios ni sacrificar la rentabilidad.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

## Campaña de 4 semanas: **“Aurora, cuidado facial premium con total transparencia”**

**Producto-exclusive:** Aurora.  
**Mercado:** Bogotá.  
**Objetivo comercial:** vender Aurora de forma rentable, generar confianza en su categoría premium y crear una primera audiencia propia de personas interesadas en skincare.

> Como todavía no conocemos el precio exacto, el margen ni la conversión actual de Aurora, los objetivos económicos se calculan con fórmulas. Fijar un ROAS o CPA en pesos sin esos datos sería arbitrario.

---

## 1. Objetivo de la campaña

### Objetivo principal
Conseguir durante cuatro semanas ventas rentables de **Aurora** en Bogotá, validando un modelo de adquisición que pueda repetirse y escalarse sin convertir a Aurora en un producto de descuento.

### Objetivo SMART
Establecer antes del lanzamiento:

- **CAC máximo de Aurora:**  
  `Ingreso neto por pedido de Aurora × margen de contribución antes de publicidad`
- **ROAS de equilibrio:**  
  `1 ÷ margen de contribución antes de publicidad`
- **Pedidos objetivo:**  
  `1,2 × presupuesto pagado ÷ CAC máximo`  
  El 20 % adicional funciona como colchón frente a devoluciones y cambios de costo.
- **Tráfico cualificado objetivo:**  
  `Pedidos objetivo ÷ tasa de conversión esperada de Aurora`  
  Mientras se establece el baseline, puedes usar provisionalmente una conversión del **2,5 %**.

### Objetivos secundarios
- Conseguir una lista de personas interesadas específicamente en **Aurora**.
- Aumentar la confianza mediante demostraciones, educación y reseñas reales.
- Identificar qué mensaje genera mejores resultados: **textura**, **ritual paso a paso**, **transparencia**, **asesoría** o **prueba social**.

---

## 2. Audiencia

### Audiencia principal

Personas adultas residentes en Bogotá que:

- Se interesan por el cuidado facial y el skincare premium.
- Valoran la calidad, la experiencia de uso, la claridad de la información y una asesoría confiable.
- Compran o investigan productos de belleza por Internet.
- Buscan actively un set o kit de cuidado facial, especialmente en categorías premium.

No limitaría la campaña por edad o género sin datos previos. La segmentación inicial debe ser **geográfica, conductual y por intención**.

| Segmento | Señales | Tratamiento |
|---|---|---|
| **Prospectos fríos** | Bogotá; interés en skincare premium, rutinas faciales, dermocosmética y belleza online | Meta Ads y Google |
| **Prospectos tibios** | Visitaron la página de Aurora, interactuaron con Instagram, vieron videos o hicieron clic en correos sobre Aurora | Meta Ads y remarketing |
| **Prospectos calientes** | Agregaron Aurora al carrito,soul began checkout,_BIT. preguntaron por Aurora o abandonaron el pago | Meta Ads, Google y WhatsApp |
| **Clientes existentes sin Aurora** | Compraron anteriormente, pero aún no han adquirido Aurora | Email y remarketing, siProfiles have consented |

### Exclusiones recomendadas

- Personas fuera de Bogotá.
- Compradores recientes de **Aurora** en campañas de adquisición; separarlos para recompra si applicable.
- Visitantes que ya compraron **Aurora** y no necesitan otra comunicación.
- Menores de edad.
- Tráfico de sitios irrelevantes o de baja calidad.

---

## 3. Mensaje principal

### Mensaje central

> **“Descubre Aurora: cuidado facial premium con total transparencia. Conoce su textura, su modo de uso y para quién es, y recibe orientación para elegirlo con confianza.”**

### Mensajes de apoyo

1. **Demostración real:** mostrar cuánto se usa, cómo se aplica y cuál es su textura, sin filtros ni retoques.
2. **Experiencia premium:** explicar qué hace que la experiencia de **Aurora** sea superior sin inventar atributos ni resultados.
3. **Educación clara:** mostrar el protocolo de uso, compatibilidad, conservación y preguntas frecuentes.
4. **Orientación humana:** recomendar **Aurora** según necesidades y rutina, no solo según presupuesto.
5. **Confianza verificable:** incluir atributos confirmados, reseñas autorizadas y contenido generado por clientas.

### Llamados a la acción

- **Descubrimiento:** “Conoce Aurora”.
- **Consideración:** “Descubre si Aurora es para ti”.
- **Asesoría:** “Habla con una asesora sobre Aurora”.
- **Conversión:** “Elige Aurora con orientación”.
- **Última etapa:** “Últimos días de la campaña Aurora”, únicamente si existe una fecha real de cierre.

### Qué no hacer

- No DIRECTAMENTE mencionar a Botica Verde o Skin Lab en los anuncios.
- No afirmar que Aurora “elimina皱纹”, “cura el acné” o “revierte el envejecimiento” sin evidencia regulatoria.
- No comprar con descuentos aggressive. Si hace falta un incentivo, usar **valor añadido**: asesoría de uso de Aurora, guía digital, entrega prioritaria en Bogotá o garantía clara, siempre que sea sostenible.

---

## 4. Canales y roles

| Canal | Rol en la campaña | Frecuencia o configuración |
|---|---|---|
| **Sitio web de Aurora** | Convertir visitas y responder objeciones | Página y landingIRD optimizadas para móvil |
| **Instagram** | Generar demanda y hacer tangible la experiencia premium | 3 reels, 2 carruseles y stories 4–5 días por semana |
| **Meta Ads** | Adquisición, prueba de mensajes y remarketing | Segmentos frío, tibio y caliente separados |
| **Google Search y Shopping** | Capturar demanda de alta intención | Siempre activo; frases exactas y términos de marca |
| **Creadores y UGC** | Generar prueba social creíble | 2–3 creadores de skincare de Bogotá durante la campaña |
| **Email** | Cultivar y convertir interés en Aurora | 3 envíos manuales y automatizaciones de carrito |
| **WhatsApp Business** | Asesorar y recuperar carritos | Automatizaciones y seguimiento con consentimiento |
| **TikTok** | Probar contenido de descubrimiento | 2–3 videos semanales, principalmenteISI reutilizando reels |

### Distribución orientativa del presupuesto pagado

- **50 % Meta Ads:** adquisición y remarketing.
- **35 % Google Search y Shopping:** demanda existente.
- **15 % creadores y producción de UGC:** contenido que luego se utiliza en Meta.

### Página de Aurora

La página de **Aurora** debe incluir:

- Qué incluye exactamente el set.
- Precio y condiciones de pago.
- Fotos y videos reales de textura y empaque.
- Ingredientes y atributos solo si están verificados.
- Paso a paso y frecuencia de uso.
- Indicaciones de compatibilidad y contraindicaciones.
- Reseñas verificables.
- Tiempo de entrega y política de cambios en Bogotá.
- Preguntas frecuentes.
- Botón visible: **“Hablar sobre Aurora”**.

---

## 5. Plan de cuatro semanas

### Semana 1: Fundación y prueba de mensajes

**Objetivo:** preparar la infraestructura y descubrir qué mensaje genera mayor interés en **Aurora**.

**Acciones:**
- Finalizar la página de **Aurora** y_optimizar la velocidad móvil.
- Configurar GA4, Meta Pixel, Google Ads, Shopping y UTMs.
- Publicar:
  - Reel: **“La textura real de Aurora, sin filtros”**.
  - Carrusel: **“Qué incluye y cómo se usa Aurora”**.
  - Reel: **“Cómo integrar Aurora en una rutina facial”**.
- Lanzar en Meta tres ángulos:
  1. Textura y experiencia.
  2. Educación y uso.
  3. Qué significa skincare premium para ti.
- Activar Google con búsquedas como:
  - “set de cuidado facial premium Bogotá”.
  - “kit skincare facial Bogotá”.
  - “kit facial premium”.
  - Búsquedas de marca relacionadas con **Aurora**.
- Enviar el primer correo a personas感兴趣的 en **Aurora**.

**Indicadores de la semana:**
- CTR de salida.
- Visitas cualificadas a la página de Aurora.
- Tasa de adición al carrito.
- Conversión de la página.
- Coste por lead de WhatsApp o correo.

**Decisión al finalizar:** mantener los mensajes con mayor intención, no necesariamente los de mayor alcance.

---

### Semana 2: Demostración y prueba social

**Objetivo:** reducir dudas y demostrar que la promesa de **Aurora** es tangible.

**Acciones:**
- Publicar un reel completo de aplicación de **Aurora**.
- Publicar un carrusel: **“Aurora paso a paso: cantidad, orden y errores comunes”**.
- Incorporar una experiencia UGC o reseña real, con autorización.
- Publicar en Instagram una historia de preguntas frecuentes sobre **Aurora**.
- Activar remarketing para:
  - Visitantes de la página de Aurora.
  - Visores de videos de Aurora.
  - Personas que interactuaron con Instagram.
- Enviar el segundo correo: **“Conoce Aurora antes de elegir tu ritual facial”**.
- Llevar los ganadores de Meta a campañas de optimización hacia compra.

**Indicadores:**
- CTR y tasa de adición al carrito por creativo.
- Compras asistidas de Aurora.
- Uso de códigos o enlaces de creadores.
- Consultas sobre Aurora por WhatsApp.
- Conversión de visits que interactuaron con el contenido de UGC.

**Decisión al finalizar:**Wp concentration budget on creatives with actual add-to-cart or purchase signals; reduce impressions-only content.

---

### Semana 3: Conversión y asesoría

**Objetivo:** convertir el interés en **Aurora** en pedidos, especialmente entre quienes yaSEA warmly know Aurora.

**Acciones:**
- Realizar un live de 20–30 minutos: **“Cómo elegir y usar un set de cuidado facial premium como Aurora”**.
- Publicar una malla de preguntas frecuentes sobre:
  - Uso.
  - Compatibilidad.
  - Textura.
  - Envíos en Bogotá.
  - Cambios y devoluciones.
- Abrir una campaña de WhatsApp: **“¿Aurora es para tu rutina?”**.
- Enviar el tercer correo con demostraciones, reseñas y enlace directo a **Aurora**.
- Activar recuperación de carrito de Aurora:
  - Recordatorio a las 2–4 horas.
  - Ayuda a las 24 horas.
  - Último recordatorio a las 48–72 horas.
- En Google, dar mayor peso a términos de alta intención y a Shopping.
- Sustituir descuentos, si fueran necesarios, por una asesoría o una guía de uso de **Aurora**.

**Indicadores:**
- Conversión de carrito y checkout de Aurora.
- CAC de Aurora.
- Conversión de consulta a pedido.
- Recuperación de carritos.
- ROAS por campaña y creator.
- Motivos de abandono más frecuentes.

**Decisión al finalizar:** invertir más en los públicos y anuncios que generan pedidos rentables, no solo visitas.

---

### Semana 4: Escalamiento y cierre

**Objetivo:** consolidar lo aprendido, escalar lo que funciona y realizar un cierre transparente.

**Acciones:**
- Escalar entre **20 % y 30 %** los anuncios de Meta queesterday:
  - CAC dentro del límite.
  - ROAS superior al punto de equilibrio.
  - Conversión suficiente para no depender de una compra aislada.
- Reducir o pausar:
  - Anuncios con muchas impresiones y pocos clics.
  - Audiencias con alto costo de carrito.
  - Creatividades que generan interacción, pero no advances.
- Publicar el mejor contenido de **Aurora** nuevamente en Instagram y TikTok.
- Enviar el último correo de campaña con:
  - Demostración favorita.
  - Reseñas.
  - Preguntas frecuentes.
  - CTA directo.
- Usar “últimos días” solamente si la fecha de cierre es real.
- Comparar:
  - Prospectos fríos frente a remarketing.
  - Nuevos clientes frente a clientes existentes.
  - Meta frente a Google.
  - Ventas netas y margen de contribución.

**Resultado esperado al finalizar:**
- Baseline real de CAC, ROAS, conversión y pedidos de **Aurora**.
- Identificación de los dos o tres mensajes más eficientes.
- Una audiencia propia interested en **Aurora**.
- Criterios claros para decidir si la campaña se repite, se optimiza o se detiene.

---

## 6. Métricas de éxito

### Métricas financieras prioritarias

1. **Ingreso neto de Aurora:** ventas menos anulaciones, devoluciones y descuentos.
2. **Margen de contribución de Aurora después de publicidad:** debe ser positivo.
3. **ROAS de Aurora:** debe superar el punto de equilibrio.
4. **CAC de Aurora:** no debe superar el CAC máximo calculado.
5. **Clientes nuevos que compran Aurora.**
6. **Pedidos de Aurora**, comparados con el objetivo de `1,2 × presupuesto ÷ CAC máximo`.

### Embudo de Aurora

| Métrica | Referencia inicial de trabajo |
|---|---:|
| CTR de salida en Meta | ≥ 1 % |
| Visita a la página de Aurora desde campañas | Registrar por campaña y creador |
| Tasa de adición al carrito de Aurora | ≥ 8 % |
| Conversión de la página de Aurora | ≥ 2,5 % provisional o +25 % frente al baseline |
| Finalización del checkout | ≥ 40 % |
| Conversión de consulta a pedido de Aurora | ≥ 10 % provisional |
| Recuperación de carritos de Aurora | Medir por recovered revenue y margen |

Estas cifras son **guardarrails iniciales**, no verdades universales. Después de la primera semana deben ajustarse al tráfico real, al precio de Aurora, al tipo de campaña y a la calidad de la página.

### Métricas de confianza y contenido

- Guardados y compartidos del contenido de Aurora.
- Porcentaje de reproducción de los videos de Aurora.
- Número de reseñas verificadas de Aurora.
- Volumen de UGC autorizado de Aurora.
- Consultas resueltas sin很强的 fricción por WhatsApp.
- Tasa de devolución o reembolso de Aurora.
- Quejas relacionadas con el empaque, la entrega o el uso de Aurora.
- Entregas de Aurora completadas a tiempo en Bogotá.

---

## 7. Reglas de medición y optimización

- Usar el **backend de la tienda** como fuente principal de ingresos; contrastar Meta y Google con GA4.
- Añadir UTMs específicas por campaña, anuncio, creator y correo.
- Separar ventas de **prospectos fríos** y ventas asistidas por **remarketing**.
- No utilizar el open rate del correo como indicador principal.
- No cambiar precio, página y anuncio al mismo tiempo.
- Revisar el rendimiento de **Aurora** diariamente y tomar decisiones司 weekly.
- Escalar solo cuando el CAC de **Aurora** esté dentro del límite y haya suficientes compras para evitar decisiones basadas en una sola venta.
- Revisar todas las afirmaciones sobre ingredientes y resultados de **Aurora** antes de publicarlas.

### Criterio final

La campaña será exitosa si:

1. Alcanza al menos el **80 % de los pedidos objetivo de Aurora**.
2. Mantiene el **ROAS de Aurora por encima del punto de equilibrio**.
3. Mantiene el **CAC de Aurora dentro del máximo permitido**.
4. Alcanza una conversión de página de **2,5 % o superior**, o una mejora mínima del **25 %** frente al baseline.
5. Genera margen después de publicidad, no únicamente ventas.


## Respuesta completa

## Campaña de 4 semanas: **“Aurora, cuidado facial premium con total transparencia”**

**Producto-exclusive:** Aurora.  
**Mercado:** Bogotá.  
**Objetivo comercial:** vender Aurora de forma rentable, generar confianza en su categoría premium y crear una primera audiencia propia de personas interesadas en skincare.

> Como todavía no conocemos el precio exacto, el margen ni la conversión actual de Aurora, los objetivos económicos se calculan con fórmulas. Fijar un ROAS o CPA en pesos sin esos datos sería arbitrario.

---

## 1. Objetivo de la campaña

### Objetivo principal
Conseguir durante cuatro semanas ventas rentables de **Aurora** en Bogotá, validando un modelo de adquisición que pueda repetirse y escalarse sin convertir a Aurora en un producto de descuento.

### Objetivo SMART
Establecer antes del lanzamiento:

- **CAC máximo de Aurora:**  
  `Ingreso neto por pedido de Aurora × margen de contribución antes de publicidad`
- **ROAS de equilibrio:**  
  `1 ÷ margen de contribución antes de publicidad`
- **Pedidos objetivo:**  
  `1,2 × presupuesto pagado ÷ CAC máximo`  
  El 20 % adicional funciona como colchón frente a devoluciones y cambios de costo.
- **Tráfico cualificado objetivo:**  
  `Pedidos objetivo ÷ tasa de conversión esperada de Aurora`  
  Mientras se establece el baseline, puedes usar provisionalmente una conversión del **2,5 %**.

### Objetivos secundarios
- Conseguir una lista de personas interesadas específicamente en **Aurora**.
- Aumentar la confianza mediante demostraciones, educación y reseñas reales.
- Identificar qué mensaje genera mejores resultados: **textura**, **ritual paso a paso**, **transparencia**, **asesoría** o **prueba social**.

---

## 2. Audiencia

### Audiencia principal

Personas adultas residentes en Bogotá que:

- Se interesan por el cuidado facial y el skincare premium.
- Valoran la calidad, la experiencia de uso, la claridad de la información y una asesoría confiable.
- Compran o investigan productos de belleza por Internet.
- Buscan actively un set o kit de cuidado facial, especialmente en categorías premium.

No limitaría la campaña por edad o género sin datos previos. La segmentación inicial debe ser **geográfica, conductual y por intención**.

| Segmento | Señales | Tratamiento |
|---|---|---|
| **Prospectos fríos** | Bogotá; interés en skincare premium, rutinas faciales, dermocosmética y belleza online | Meta Ads y Google |
| **Prospectos tibios** | Visitaron la página de Aurora, interactuaron con Instagram, vieron videos o hicieron clic en correos sobre Aurora | Meta Ads y remarketing |
| **Prospectos calientes** | Agregaron Aurora al carrito,soul began checkout,_BIT. preguntaron por Aurora o abandonaron el pago | Meta Ads, Google y WhatsApp |
| **Clientes existentes sin Aurora** | Compraron anteriormente, pero aún no han adquirido Aurora | Email y remarketing, siProfiles have consented |

### Exclusiones recomendadas

- Personas fuera de Bogotá.
- Compradores recientes de **Aurora** en campañas de adquisición; separarlos para recompra si applicable.
- Visitantes que ya compraron **Aurora** y no necesitan otra comunicación.
- Menores de edad.
- Tráfico de sitios irrelevantes o de baja calidad.

---

## 3. Mensaje principal

### Mensaje central

> **“Descubre Aurora: cuidado facial premium con total transparencia. Conoce su textura, su modo de uso y para quién es, y recibe orientación para elegirlo con confianza.”**

### Mensajes de apoyo

1. **Demostración real:** mostrar cuánto se usa, cómo se aplica y cuál es su textura, sin filtros ni retoques.
2. **Experiencia premium:** explicar qué hace que la experiencia de **Aurora** sea superior sin inventar atributos ni resultados.
3. **Educación clara:** mostrar el protocolo de uso, compatibilidad, conservación y preguntas frecuentes.
4. **Orientación humana:** recomendar **Aurora** según necesidades y rutina, no solo según presupuesto.
5. **Confianza verificable:** incluir atributos confirmados, reseñas autorizadas y contenido generado por clientas.

### Llamados a la acción

- **Descubrimiento:** “Conoce Aurora”.
- **Consideración:** “Descubre si Aurora es para ti”.
- **Asesoría:** “Habla con una asesora sobre Aurora”.
- **Conversión:** “Elige Aurora con orientación”.
- **Última etapa:** “Últimos días de la campaña Aurora”, únicamente si existe una fecha real de cierre.

### Qué no hacer

- No DIRECTAMENTE mencionar a Botica Verde o Skin Lab en los anuncios.
- No afirmar que Aurora “elimina皱纹”, “cura el acné” o “revierte el envejecimiento” sin evidencia regulatoria.
- No comprar con descuentos aggressive. Si hace falta un incentivo, usar **valor añadido**: asesoría de uso de Aurora, guía digital, entrega prioritaria en Bogotá o garantía clara, siempre que sea sostenible.

---

## 4. Canales y roles

| Canal | Rol en la campaña | Frecuencia o configuración |
|---|---|---|
| **Sitio web de Aurora** | Convertir visitas y responder objeciones | Página y landingIRD optimizadas para móvil |
| **Instagram** | Generar demanda y hacer tangible la experiencia premium | 3 reels, 2 carruseles y stories 4–5 días por semana |
| **Meta Ads** | Adquisición, prueba de mensajes y remarketing | Segmentos frío, tibio y caliente separados |
| **Google Search y Shopping** | Capturar demanda de alta intención | Siempre activo; frases exactas y términos de marca |
| **Creadores y UGC** | Generar prueba social creíble | 2–3 creadores de skincare de Bogotá durante la campaña |
| **Email** | Cultivar y convertir interés en Aurora | 3 envíos manuales y automatizaciones de carrito |
| **WhatsApp Business** | Asesorar y recuperar carritos | Automatizaciones y seguimiento con consentimiento |
| **TikTok** | Probar contenido de descubrimiento | 2–3 videos semanales, principalmenteISI reutilizando reels |

### Distribución orientativa del presupuesto pagado

- **50 % Meta Ads:** adquisición y remarketing.
- **35 % Google Search y Shopping:** demanda existente.
- **15 % creadores y producción de UGC:** contenido que luego se utiliza en Meta.

### Página de Aurora

La página de **Aurora** debe incluir:

- Qué incluye exactamente el set.
- Precio y condiciones de pago.
- Fotos y videos reales de textura y empaque.
- Ingredientes y atributos solo si están verificados.
- Paso a paso y frecuencia de uso.
- Indicaciones de compatibilidad y contraindicaciones.
- Reseñas verificables.
- Tiempo de entrega y política de cambios en Bogotá.
- Preguntas frecuentes.
- Botón visible: **“Hablar sobre Aurora”**.

---

## 5. Plan de cuatro semanas

### Semana 1: Fundación y prueba de mensajes

**Objetivo:** preparar la infraestructura y descubrir qué mensaje genera mayor interés en **Aurora**.

**Acciones:**
- Finalizar la página de **Aurora** y_optimizar la velocidad móvil.
- Configurar GA4, Meta Pixel, Google Ads, Shopping y UTMs.
- Publicar:
  - Reel: **“La textura real de Aurora, sin filtros”**.
  - Carrusel: **“Qué incluye y cómo se usa Aurora”**.
  - Reel: **“Cómo integrar Aurora en una rutina facial”**.
- Lanzar en Meta tres ángulos:
  1. Textura y experiencia.
  2. Educación y uso.
  3. Qué significa skincare premium para ti.
- Activar Google con búsquedas como:
  - “set de cuidado facial premium Bogotá”.
  - “kit skincare facial Bogotá”.
  - “kit facial premium”.
  - Búsquedas de marca relacionadas con **Aurora**.
- Enviar el primer correo a personas感兴趣的 en **Aurora**.

**Indicadores de la semana:**
- CTR de salida.
- Visitas cualificadas a la página de Aurora.
- Tasa de adición al carrito.
- Conversión de la página.
- Coste por lead de WhatsApp o correo.

**Decisión al finalizar:** mantener los mensajes con mayor intención, no necesariamente los de mayor alcance.

---

### Semana 2: Demostración y prueba social

**Objetivo:** reducir dudas y demostrar que la promesa de **Aurora** es tangible.

**Acciones:**
- Publicar un reel completo de aplicación de **Aurora**.
- Publicar un carrusel: **“Aurora paso a paso: cantidad, orden y errores comunes”**.
- Incorporar una experiencia UGC o reseña real, con autorización.
- Publicar en Instagram una historia de preguntas frecuentes sobre **Aurora**.
- Activar remarketing para:
  - Visitantes de la página de Aurora.
  - Visores de videos de Aurora.
  - Personas que interactuaron con Instagram.
- Enviar el segundo correo: **“Conoce Aurora antes de elegir tu ritual facial”**.
- Llevar los ganadores de Meta a campañas de optimización hacia compra.

**Indicadores:**
- CTR y tasa de adición al carrito por creativo.
- Compras asistidas de Aurora.
- Uso de códigos o enlaces de creadores.
- Consultas sobre Aurora por WhatsApp.
- Conversión de visits que interactuaron con el contenido de UGC.

**Decisión al finalizar:**Wp concentration budget on creatives with actual add-to-cart or purchase signals; reduce impressions-only content.

---

### Semana 3: Conversión y asesoría

**Objetivo:** convertir el interés en **Aurora** en pedidos, especialmente entre quienes yaSEA warmly know Aurora.

**Acciones:**
- Realizar un live de 20–30 minutos: **“Cómo elegir y usar un set de cuidado facial premium como Aurora”**.
- Publicar una malla de preguntas frecuentes sobre:
  - Uso.
  - Compatibilidad.
  - Textura.
  - Envíos en Bogotá.
  - Cambios y devoluciones.
- Abrir una campaña de WhatsApp: **“¿Aurora es para tu rutina?”**.
- Enviar el tercer correo con demostraciones, reseñas y enlace directo a **Aurora**.
- Activar recuperación de carrito de Aurora:
  - Recordatorio a las 2–4 horas.
  - Ayuda a las 24 horas.
  - Último recordatorio a las 48–72 horas.
- En Google, dar mayor peso a términos de alta intención y a Shopping.
- Sustituir descuentos, si fueran necesarios, por una asesoría o una guía de uso de **Aurora**.

**Indicadores:**
- Conversión de carrito y checkout de Aurora.
- CAC de Aurora.
- Conversión de consulta a pedido.
- Recuperación de carritos.
- ROAS por campaña y creator.
- Motivos de abandono más frecuentes.

**Decisión al finalizar:** invertir más en los públicos y anuncios que generan pedidos rentables, no solo visitas.

---

### Semana 4: Escalamiento y cierre

**Objetivo:** consolidar lo aprendido, escalar lo que funciona y realizar un cierre transparente.

**Acciones:**
- Escalar entre **20 % y 30 %** los anuncios de Meta queesterday:
  - CAC dentro del límite.
  - ROAS superior al punto de equilibrio.
  - Conversión suficiente para no depender de una compra aislada.
- Reducir o pausar:
  - Anuncios con muchas impresiones y pocos clics.
  - Audiencias con alto costo de carrito.
  - Creatividades que generan interacción, pero no advances.
- Publicar el mejor contenido de **Aurora** nuevamente en Instagram y TikTok.
- Enviar el último correo de campaña con:
  - Demostración favorita.
  - Reseñas.
  - Preguntas frecuentes.
  - CTA directo.
- Usar “últimos días” solamente si la fecha de cierre es real.
- Comparar:
  - Prospectos fríos frente a remarketing.
  - Nuevos clientes frente a clientes existentes.
  - Meta frente a Google.
  - Ventas netas y margen de contribución.

**Resultado esperado al finalizar:**
- Baseline real de CAC, ROAS, conversión y pedidos de **Aurora**.
- Identificación de los dos o tres mensajes más eficientes.
- Una audiencia propia interested en **Aurora**.
- Criterios claros para decidir si la campaña se repite, se optimiza o se detiene.

---

## 6. Métricas de éxito

### Métricas financieras prioritarias

1. **Ingreso neto de Aurora:** ventas menos anulaciones, devoluciones y descuentos.
2. **Margen de contribución de Aurora después de publicidad:** debe ser positivo.
3. **ROAS de Aurora:** debe superar el punto de equilibrio.
4. **CAC de Aurora:** no debe superar el CAC máximo calculado.
5. **Clientes nuevos que compran Aurora.**
6. **Pedidos de Aurora**, comparados con el objetivo de `1,2 × presupuesto ÷ CAC máximo`.

### Embudo de Aurora

| Métrica | Referencia inicial de trabajo |
|---|---:|
| CTR de salida en Meta | ≥ 1 % |
| Visita a la página de Aurora desde campañas | Registrar por campaña y creador |
| Tasa de adición al carrito de Aurora | ≥ 8 % |
| Conversión de la página de Aurora | ≥ 2,5 % provisional o +25 % frente al baseline |
| Finalización del checkout | ≥ 40 % |
| Conversión de consulta a pedido de Aurora | ≥ 10 % provisional |
| Recuperación de carritos de Aurora | Medir por recovered revenue y margen |

Estas cifras son **guardarrails iniciales**, no verdades universales. Después de la primera semana deben ajustarse al tráfico real, al precio de Aurora, al tipo de campaña y a la calidad de la página.

### Métricas de confianza y contenido

- Guardados y compartidos del contenido de Aurora.
- Porcentaje de reproducción de los videos de Aurora.
- Número de reseñas verificadas de Aurora.
- Volumen de UGC autorizado de Aurora.
- Consultas resueltas sin很强的 fricción por WhatsApp.
- Tasa de devolución o reembolso de Aurora.
- Quejas relacionadas con el empaque, la entrega o el uso de Aurora.
- Entregas de Aurora completadas a tiempo en Bogotá.

---

## 7. Reglas de medición y optimización

- Usar el **backend de la tienda** como fuente principal de ingresos; contrastar Meta y Google con GA4.
- Añadir UTMs específicas por campaña, anuncio, creator y correo.
- Separar ventas de **prospectos fríos** y ventas asistidas por **remarketing**.
- No utilizar el open rate del correo como indicador principal.
- No cambiar precio, página y anuncio al mismo tiempo.
- Revisar el rendimiento de **Aurora** diariamente y tomar decisiones司 weekly.
- Escalar solo cuando el CAC de **Aurora** esté dentro del límite y haya suficientes compras para evitar decisiones basadas en una sola venta.
- Revisar todas las afirmaciones sobre ingredientes y resultados de **Aurora** antes de publicarlas.

### Criterio final

La campaña será exitosa si:

1. Alcanza al menos el **80 % de los pedidos objetivo de Aurora**.
2. Mantiene el **ROAS de Aurora por encima del punto de equilibrio**.
3. Mantiene el **CAC de Aurora dentro del máximo permitido**.
4. Alcanza una conversión de página de **2,5 % o superior**, o una mejora mínima del **25 %** frente al baseline.
5. Genera margen después de publicidad, no únicamente ventas.