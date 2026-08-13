# Claude Opus 5 — agent_long_horizon/implicit_state_construction

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 5.57 | quality: 7.0
- latency_total: 227.979s | tokens_per_second: 62.6
- input_tokens: 31302 | output_tokens: 13633

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Hola Camila, sí, me queda claro. Te lo resumo para confirmar que lo tengo bien registrado:

**Tu negocio**
- Tienda online en Colombia
- Mercado actual: Bogotá (único, por ahora)

**Tu portafolio (3 productos)**
| Producto | Categoría | Posicionamiento de precio |
|---|---|---|
| **Aurora** | Set de cuidado facial | Premium |
| **Sol** | Kit de maquillaje natural | Medio |
| **Luna** | Crema corporal | Entrada |

**Competencia principal**
- **Botica Verde** (Bogotá)
- **Skin Lab** (Bogotá)

Tienes una estructura de portafolio bastante limpia: un producto por cada nivel de precio, lo cual es útil para campañas escalonadas (captar con Luna, monetizar con Aurora).

Para avanzar con la planificación, me ayudaría saber algunas cosas que aún no me has contado:

1. **Objetivo de la campaña**: ¿adquirir clientes nuevos, aumentar recompra, sacar inventario, o lanzar algo?
2. **Presupuesto y horizonte** de tiempo con el que trabajas.
3. **Canales** que ya usas (Instagram, TikTok, Meta Ads, WhatsApp, email, marketplaces como Mercado Libre o Falabella).
4. **Qué tan diferenciada** te sientes frente a Botica Verde y Skin Lab: ¿compiten por precio, por ingredientes, por marca?
5. **Ticket promedio y márgenes** aproximados, aunque sea en rangos.

Con eso puedo proponerte algo concreto en lugar de genérico. ¿Por dónde quieres empezar?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Aquí va una versión base, construida solo con lo que sé de tu negocio:

> **"Cuidado personal natural para mujeres en Bogotá que quieren una rutina completa sin tener que comprarla en tres marcas distintas: desde una crema corporal accesible como Luna hasta un ritual facial premium como Aurora. Todo se pide online, llega a tu casa y está pensado para que empieces por donde quieras y subas de nivel cuando estés lista."**

**Por qué la armé así**

La primera oración planta tu ventaja estructural real: tienes un portafolio escalonado (entrada, medio, premium) que cubre rostro, maquillaje y cuerpo. Ni Botica Verde ni Skin Lab necesariamente cubren los tres niveles con esa limpieza, y eso te permite ser "la marca a la que le compras siempre" en vez de "la marca a la que le compras una cosa".

La segunda oración convierte eso en una promesa al cliente: no hay barrera de entrada (Luna) y hay a dónde crecer (Aurora). Es la lógica de "captar con Luna, monetizar con Aurora" que mencioné antes, pero dicha en lenguaje de cliente.

**Dos cosas que debes saber antes de usarla**

1. Asumí que **"natural"** es un atributo transversal de tu marca, no solo de Sol. Sé con certeza que Sol es maquillaje natural, pero no me has dicho si Aurora y Luna comparten esa promesa. Si no la comparten, hay que cambiar el arranque.

2. Esta propuesta se apoya en la **arquitectura de tu portafolio**, no en un beneficio único de producto (un ingrediente propio, un resultado comprobable, una historia de origen). Es defendible, pero un competidor con más capital puede copiar un portafolio escalonado. Si tienes algo más difícil de imitar, la propuesta debería colgar de ahí.

**Para afilarla necesito una sola cosa:** ¿qué te dicen tus clientas actuales cuando te compran por segunda vez? Ese motivo de recompra suele ser la propuesta de valor real, y es mejor dato que cualquier cosa que yo pueda deducir. También me sirve saber si compites contra Botica Verde y Skin Lab por precio, por ingredientes o por marca.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Te propongo una priorización en tres niveles. Está construida sobre la lógica de tu portafolio escalonado —Luna capta, Aurora monetiza— porque es la ventaja que ya identificamos.

## Nivel 1: los que sostendrían la campaña

**1. Instagram (orgánico + Meta Ads)**

Sigue siendo el canal central para belleza en Colombia y donde tu público en Bogotá ya está evaluando alternativas. Lo importante es cómo repartes los productos:

| Producto | Rol en Instagram |
|---|---|
| **Luna** | Anuncios de adquisición en frío. Precio de entrada = umbral bajo de decisión |
| **Sol** | Contenido orgánico y colaboraciones. El maquillaje natural es lo más "demostrable" en video |
| **Aurora** | Retargeting exclusivamente. No la pongas en frío, quema presupuesto |

**2. WhatsApp Business**

En Colombia esto no es un canal secundario, es donde se cierra la venta. Te sirve para tres cosas: resolver dudas antes de comprar (crítico en Aurora, donde el precio premium genera fricción), recuperar carritos abandonados, y armar la recompra escalonada —quien compró Luna hace seis semanas es tu mejor prospecto para Sol.

Configura catálogo, respuestas rápidas y etiquetas por producto comprado. Es el canal con mejor retorno relativo a lo que cuesta.

**3. TikTok orgánico**

Costo de entrada bajísimo y el alcance orgánico en Colombia todavía es generoso comparado con Instagram. Sol es tu producto natural aquí: aplicación, antes/después, rutinas rápidas. Si un video funciona, lo reciclas como anuncio en Meta.

## Nivel 2: cuando ya tengas el nivel 1 andando

**Google Search, solo dos tipos de búsqueda:** tu propia marca (defensiva, evita que Botica Verde o Skin Lab te intercepten) y búsquedas de intención alta tipo "set cuidado facial Bogotá". No compres términos genéricos de categoría, ahí pierdes contra presupuestos grandes.

**Micro-influencers bogotanas (5k–30k seguidores).** Mejor cinco perfiles pequeños con audiencia local real que uno grande y nacional. Tu mercado es una sola ciudad: no pagues alcance en Medellín o Cali que no puedes convertir. Paga con producto + comisión antes que con tarifa fija.

**Email/base propia.** No es de adquisición, pero es el único canal que no te cobra por volver a hablarle a alguien que ya te compró. Con un portafolio de tres productos, la secuencia post-compra prácticamente se escribe sola.

## Nivel 3: lo que yo dejaría para después

**Marketplaces** (Mercado Libre, Falabella, Linio). Te dan volumen, pero cobran comisión, te obligan a competir por precio y no te dejan quedarte con el dato del cliente. Con un producto premium como Aurora, además, el contexto de marketplace juega en contra: es un entorno donde la gente compara precios, no donde construyes percepción de marca.

**Pinterest, LinkedIn, radio o medios locales.** No para esta etapa.

## Dos cosas prácticas

Antes de invertir en tráfico, revisa que tu checkout acepte **Nequi, Daviplata, PSE y contraentrega**. En Colombia la caída por métodos de pago limitados es alta, y es plata que pierdes después de haberla gastado en traer al visitante.

Y si tienes logística propia en Bogotá, **la entrega en 24–48 horas es argumento de venta**, no un detalle operativo. Úsalo en los anuncios.

## Lo que cambiaría esta recomendación

Te di una estructura que funciona razonablemente en varios escenarios, pero el orden se movería si me dices tu **presupuesto mensual**. Por debajo de unos 2 millones de pesos al mes, yo concentraría todo en Instagram + WhatsApp y dejaría TikTok solo en orgánico; con más margen, Meta Ads y Search entran en paralelo desde el inicio.

También sigue pendiente algo que te pregunté antes y que sí cambia el planteamiento: **cómo compites contra Botica Verde y Skin Lab**. Si tu diferencia está en ingredientes, el contenido educativo pesa más y TikTok sube de prioridad. Si es marca y estética, Inst

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Antes de darte números, una advertencia que importa: la frecuencia sostenible le gana a la frecuencia ideal. Un calendario que abandonas en tres semanas te deja peor que uno modesto que cumples seis meses, porque los algoritmos castigan la inconsistencia. Así que te doy dos versiones: la recomendada y el piso mínimo.

## Cadencia recomendada

| Canal | Frecuencia | Formato dominante |
|---|---|---|
| **Instagram feed/Reels** | 4 por semana (3 Reels + 1 carrusel) | Video vertical |
| **Instagram Stories** | Diario, 3–5 piezas | Cotidiano, sin producción |
| **TikTok** | 4–5 por semana | Nativo, cero pulido |
| **Estados de WhatsApp** | 2–3 por semana | Producto, pedidos saliendo |
| **Difusión de WhatsApp** | 2 al mes, máximo | Solo con motivo real |
| **Email** | 2 al mes + secuencias automáticas | — |

Dos notas sobre esa tabla. En **TikTok** publicas más que en Instagram porque el costo por pieza es más bajo: no requiere edición cuidada y el alcance orgánico todavía premia volumen. Y en **difusión de WhatsApp** el número es bajo a propósito: es el canal más invasivo que tienes, y si lo saturas la gente te bloquea. Ahí no hay vuelta atrás.

## Piso mínimo, si el tiempo aprieta

- Instagram: 2 Reels por semana + Stories 4 días
- TikTok: 3 por semana, reciclando lo de Instagram
- WhatsApp: estados 2 por semana
- Email: 1 al mes

Con esto mantienes presencia. Por debajo, empiezas a desaparecer.

## Cómo reparto tus tres productos

Esta es la parte que no es genérica, porque depende de tu portafolio:

**Sol, 40% del contenido.** El maquillaje natural es lo único que puedes mostrar en acción con resultado visible en 15 segundos. Es tu motor de alcance, aunque no sea tu producto más rentable.

**Luna, 30%.** Contenido de entrada y hooks de precio accesible. Sirve para atraer a quien todavía no confía en la marca.

**Aurora, 20%.** Aquí cambia el registro: contenido educativo, rutinas, explicación de por qué cuesta lo que cuesta. Un producto premium no se vende con volumen de publicaciones, se vende con autoridad acumulada. No la sobreexpongas.

**Marca y detrás de cámaras, 10%.** Empaques, pedidos saliendo hacia barrios de Bogotá, tu proceso. Es lo que Botica Verde y Skin Lab no pueden copiar.

## La única forma de que esto sea sostenible

Graba en bloque: **una sesión de 2–3 horas por semana** para producir todo el contenido de los siguientes 7 días. Publicar diario es viable; producir diario, no, y ahí es donde la mayoría abandona.

Dos atajos que reducen la carga a la mitad:

Un mismo video te sirve para Reels y TikTok, con edición mínima. No dupliques trabajo. Y todo lo que funcione orgánico, guárdalo: es tu materia prima para los anuncios de Meta que mencionamos, y contenido probado convierte mejor que creatividad hecha desde cero.

## Lo que no sé

No me has dicho **si trabajas sola o tienes alguien apoyando**, y eso define cuál de las dos versiones aplica. Si estás sola y además manejas empaque, envíos y atención por WhatsApp, arranca con el piso mínimo y sube en un mes, cuando ya tengas ritmo. Si tienes ayuda, la cadencia recomendada es alcanzable desde la primera semana.

Y sigue abierto lo de **Botica Verde y Skin Lab**: si compites por ingredientes, el contenido educativo de Aurora debería pesar más que el 20% que te propuse.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Tu pregunta cae justo en tu producto más difícil: **Aurora**. El maquillaje se vende mostrando resultado inmediato, pero el skincare vende un resultado que tarda semanas y casi no se ve en cámara. Eso cambia el tipo de contenido que funciona.

## Los formatos que mejor rinden

**1. Textura y aplicación en primer plano**

Lo más rentable en relación esfuerzo/resultado. Producto extendiéndose en la piel, cómo absorbe, cómo queda el acabado. Grabado muy cerca, con sonido real. Retiene atención en los primeros segundos, que es donde se gana o se pierde el alcance, y lo produces en 20 minutos sin guion.

Funciona para Aurora y para Luna por igual. Empieza por aquí si tienes poco tiempo.

**2. Rutina paso a paso**

Aurora es un **set**, y eso te da una ventaja de formato: puedes mostrar orden de aplicación, cuánto producto usar, cuánto tarda la rutina completa. "Mi rutina de noche en 4 pasos" vende el conjunto, no una pieza. Es el contenido que más sube el ticket promedio.

**3. Documentación en el tiempo**

Día 1, día 14, día 28, misma luz, mismo ángulo, sin filtro. Es el contenido más persuasivo que existe en skincare y el que menos gente hace, porque exige empezar hoy para publicar en un mes.

Mi recomendación concreta: **elige dos o tres clientas de Aurora esta semana** y pídeles que registren el proceso a cambio de producto. En cuatro semanas tienes material que ninguna competencia improvisa.

**4. Educativo con criterio local**

Aquí tienes un ángulo que casi nadie está usando bien: **Bogotá tiene un clima que castiga la piel de forma particular**. Frío, aire seco, y a 2.600 metros la radiación UV es notablemente más intensa que a nivel del mar. Eso significa deshidratación y necesidad real de protección solar, incluso en días nublados.

Contenido tipo "por qué tu piel se descama en Bogotá y no te pasaba en tierra caliente" es específico, útil y te posiciona como quien entiende a tu clienta. Botica Verde y Skin Lab están en la misma ciudad, pero este ángulo está casi siempre desaprovechado.

**5. Manejo de objeciones**

Para un premium como Aurora, el freno no es el interés, es el precio. Contenido que responda directo: cuántas semanas dura el set, costo por día de uso, qué pasa si no te funciona, por qué la formulación cuesta lo que cuesta. Esto va sobre todo en **retargeting y WhatsApp**, no en frío.

**

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

La regla de fondo es simple: una guerra de precios la gana quien tiene más caja para aguantar pérdidas. No sabes si Botica Verde o Skin Lab tienen inversión detrás, así que no es un terreno donde te convenga apostar. Lo que sigue está ordenado de lo **fácil de copiar** a lo **difícil de copiar**, porque una diferenciación que tu competencia replica en dos semanas no es diferenciación, es un anuncio gratis para ellos.

## Ejes ordenados por defensibilidad

**Fácil de copiar (úsalos, pero no cuelgues la marca de ahí)**

Empaque bonito, envío rápido, contenido de mejor calidad, un ingrediente de moda. Todo esto lo replica cualquiera con presupuesto. Sirven para ganar la venta de hoy, no para construir una posición.

**Medianamente defendible**

*Tu portafolio escalonado.* Tienes rostro, maquillaje y cuerpo en tres niveles de precio limpios. Que alguien copie la estructura le toma meses de desarrollo de producto. No es eterno, pero te da ventaja ahora.

*Servicio consultivo por WhatsApp.* No vender productos, vender **una rutina armada para esa persona**: pregúntale tipo de piel, en qué zona de Bogotá vive, si trabaja en interior con aire seco, y devuélvele una recomendación específica —a veces recomendando el producto más barato. Esto es costoso de escalar, y precisamente por eso una marca con inversión no lo hace: no le sale la cuenta. A ti sí, mientras seas pequeña. Es tu ventaja de tamaño.

**Difícil de copiar (aquí está tu foso real)**

*Autoridad hiperlocal en piel bogotana.* Ya lo mencioné como formato de contenido, pero funciona mejor como **posicionamiento de marca**: "formulado para lo que el clima de Bogotá le hace a tu piel". Frío, aire seco, altitud y radiación UV alta. Tus competidoras están en la misma ciudad, pero apropiarse de un territorio conceptual es una carrera que gana quien llega primero y es consistente tres años. Si tú lo ocupas, ellas quedan copiando.

*Tu cara y tu criterio.* Una marca con fundadora visible que responde, explica y se equivoca en público no se replica con presupuesto. Es lo único

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Antes de la lista, un criterio: en el primer trimestre tu objetivo no es *optimizar*, es **establecer líneas base**. No tienes historia propia contra la que comparar, así que cualquier meta que te pongas hoy es inventada. Mide pocas cosas, mídelas siempre igual, y al final del mes 3 ya tendrás tus propios números de referencia —que valen más que cualquier promedio de industria.

Y el otro criterio: si estás sola manejando contenido, WhatsApp, empaque y envíos, **no vas a sostener 15 indicadores**. Te propongo 5.

## Nivel 0: la cifra que manda

**Contribución bruta mensual** = ventas netas − costo de producto − costo de envío − comisiones de pasarela.

No uses ventas totales como cifra principal. Con tu portafolio escalonado, vender $3 millones en Luna y vender $3 millones en Aurora son negocios distintos: mismo ingreso, márgenes muy diferentes. Si mides solo ingreso, vas a creer que un mes bueno de Luna equivale a un mes bueno de Aurora, y tomarás decisiones mal.

*Si aún no tienes tus costos unitarios claros, ese es el primer trabajo del mes 1.* Sin eso, ningún otro KPI se interpreta bien.

## Nivel 1: los cinco KPIs del trimestre

| # | KPI | Por qué este | Frecuencia |
|---|---|---|---|
| 1 | **Contribución bruta** | Tu cifra rectora | Mensual |
| 2 | **Mix de ventas por producto** (% Aurora / Sol / Luna) | Verifica si la tesis del portafolio escalonado funciona | Mensual |
| 3 | **CAC por canal** vs. margen del primer pedido | Decide dónde poner el presupuesto en el mes 4 | Mensual |
|

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

# Campaña Aurora — Plan de 4 semanas

**Producto:** Aurora (set de cuidado facial, precio premium)
**Mercado:** Bogotá
**Duración:** 28 días

---

## Antes de empezar: cómo resolví una tensión del plan

Te dije antes que **no pusieras Aurora en anuncios en frío** porque quema presupuesto, y me sostengo en eso. Pero me pediste una campaña exclusivamente de Aurora, así que la resolví distinto: el tráfico frío no ve un anuncio de venta de Aurora, ve **contenido educativo sobre piel en Bogotá**. Aurora aparece después, cuando la persona ya demostró interés.

O sea: la campaña es 100% de Aurora, pero Aurora no es el primer mensaje. Es el segundo.

---

## 1. Objetivo

**Principal:** validar que Aurora se puede vender de forma repetible en Bogotá, e identificar cuál mensaje y cuál canal lo logran a un costo que tu margen aguante.

**Por qué está formulado así:** en 4 semanas, con un producto premium y sin historia de campañas previas, el resultado valioso no es un número de ventas, es **saber qué funciona**. Un premium tiene ciclo de decisión largo: la gente lo piensa, compara, vuelve. Mucha de la demanda que generes en la semana 4 se cierra en la semana 6 o 7.

**Secundario:** construir una audiencia de retargeting caliente de Aurora que puedas reactivar en campañas futuras. Esto es un activo que te queda incluso si el mes cierra flojo.

---

## 2. Audiencia

**Núcleo (frío):** mujeres en Bogotá, 28–45 años, que ya compran cuidado facial y no están descubriendo la categoría. Perfil que se identifica con piel deshidratada, tirante o que se descama. Interés en skincare, ingredientes, rutinas.

Segmenta por **localidades de Bogotá donde tu logística responda bien**. Si entregas mejor en Chapinero, Usaquén y Suba, concentra ahí y no pagues alcance en zonas donde el envío te complica.

**Segmentos calientes — aquí está el verdadero valor:**

| Segmento | Por qué es prioritario para Aurora |
|---|---|
| **Compradoras previas de Luna** | Ya te compraron, ya confían, ya recibieron un paquete tuyo. Es tu audiencia más barata de convertir a Aurora |
| **Compradoras previas de Sol** | Igual de valiosa, y con hábito de rutina ya instalado |
| **Visitantes de la página de Aurora que no compraron** | Interés declarado + freno de precio. Objeción específica y atacable |
| **Vistas de video de contenido educativo** al 50%+ | Interés real, no clic accidental |

**Lo que excluiría:** tráfico frío que nunca te ha visto, para anuncios de venta directa de Aurora. Ahí es donde se pierde el presupuesto.

---

## 3. Canales y rol de cada uno

| Canal | Rol en la campaña de Aurora |
|---|---|
| **Instagram/TikTok orgánico** | Generar el contenido educativo y de rutina que alimenta todo lo demás. Costo cero |
| **Meta Ads — frío** | Amplificar **solo** el contenido educativo (clima de Bogotá, piel deshidratada). No vende Aurora, captura audiencia |
| **Meta Ads — retargeting** | Aquí sí Aurora explícito: rutina completa, testimonios, manejo de objeción de precio |
| **WhatsApp consultivo** | Donde se cierra Aurora. Un premium rara vez se compra sin resolver dudas |
| **Email/base propia** | Secuencia dedicada a compradoras de Luna y Sol. Canal gratuito, audiencia caliente |
| **Google Search de marca** | Defensivo. Que quien busque "Aurora + tu marca" te encuentre a ti, no a Botica Verde o Skin Lab |

**Fuera de esta campaña:** marketplaces (contexto de comparación de precios, pésimo para premium) y micro-influencers. Las influencers valen, pero


## Respuesta completa

# Campaña Aurora — Plan de 4 semanas

**Producto:** Aurora (set de cuidado facial, precio premium)
**Mercado:** Bogotá
**Duración:** 28 días

---

## Antes de empezar: cómo resolví una tensión del plan

Te dije antes que **no pusieras Aurora en anuncios en frío** porque quema presupuesto, y me sostengo en eso. Pero me pediste una campaña exclusivamente de Aurora, así que la resolví distinto: el tráfico frío no ve un anuncio de venta de Aurora, ve **contenido educativo sobre piel en Bogotá**. Aurora aparece después, cuando la persona ya demostró interés.

O sea: la campaña es 100% de Aurora, pero Aurora no es el primer mensaje. Es el segundo.

---

## 1. Objetivo

**Principal:** validar que Aurora se puede vender de forma repetible en Bogotá, e identificar cuál mensaje y cuál canal lo logran a un costo que tu margen aguante.

**Por qué está formulado así:** en 4 semanas, con un producto premium y sin historia de campañas previas, el resultado valioso no es un número de ventas, es **saber qué funciona**. Un premium tiene ciclo de decisión largo: la gente lo piensa, compara, vuelve. Mucha de la demanda que generes en la semana 4 se cierra en la semana 6 o 7.

**Secundario:** construir una audiencia de retargeting caliente de Aurora que puedas reactivar en campañas futuras. Esto es un activo que te queda incluso si el mes cierra flojo.

---

## 2. Audiencia

**Núcleo (frío):** mujeres en Bogotá, 28–45 años, que ya compran cuidado facial y no están descubriendo la categoría. Perfil que se identifica con piel deshidratada, tirante o que se descama. Interés en skincare, ingredientes, rutinas.

Segmenta por **localidades de Bogotá donde tu logística responda bien**. Si entregas mejor en Chapinero, Usaquén y Suba, concentra ahí y no pagues alcance en zonas donde el envío te complica.

**Segmentos calientes — aquí está el verdadero valor:**

| Segmento | Por qué es prioritario para Aurora |
|---|---|
| **Compradoras previas de Luna** | Ya te compraron, ya confían, ya recibieron un paquete tuyo. Es tu audiencia más barata de convertir a Aurora |
| **Compradoras previas de Sol** | Igual de valiosa, y con hábito de rutina ya instalado |
| **Visitantes de la página de Aurora que no compraron** | Interés declarado + freno de precio. Objeción específica y atacable |
| **Vistas de video de contenido educativo** al 50%+ | Interés real, no clic accidental |

**Lo que excluiría:** tráfico frío que nunca te ha visto, para anuncios de venta directa de Aurora. Ahí es donde se pierde el presupuesto.

---

## 3. Canales y rol de cada uno

| Canal | Rol en la campaña de Aurora |
|---|---|
| **Instagram/TikTok orgánico** | Generar el contenido educativo y de rutina que alimenta todo lo demás. Costo cero |
| **Meta Ads — frío** | Amplificar **solo** el contenido educativo (clima de Bogotá, piel deshidratada). No vende Aurora, captura audiencia |
| **Meta Ads — retargeting** | Aquí sí Aurora explícito: rutina completa, testimonios, manejo de objeción de precio |
| **WhatsApp consultivo** | Donde se cierra Aurora. Un premium rara vez se compra sin resolver dudas |
| **Email/base propia** | Secuencia dedicada a compradoras de Luna y Sol. Canal gratuito, audiencia caliente |
| **Google Search de marca** | Defensivo. Que quien busque "Aurora + tu marca" te encuentre a ti, no a Botica Verde o Skin Lab |

**Fuera de esta campaña:** marketplaces (contexto de comparación de precios, pésimo para premium) y micro-influencers. Las influencers valen, pero