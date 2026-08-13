# Claude Opus 5 (suscripción) — agent_long_horizon/implicit_state_construction

- model_id: `claude-opus-5`
- success: True  | final: 6.62 | quality: 8.5
- latency_total: 564.218s | tokens_per_second: 62.2
- input_tokens: 16 | output_tokens: 30183

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Sí, claro. Te lo repito para que confirmes que no me quedé con nada torcido:

**Tu negocio:** tienda online en Colombia, mercado único Bogotá.

**Portafolio (3 productos):**
| Producto | Qué es | Posición de precio |
|---|---|---|
| Aurora | Set de cuidado facial | Premium |
| Sol | Kit de maquillaje natural | Medio |
| Luna | Crema corporal | Entrada |

**Competencia directa:** Botica Verde y Skin Lab, ambos también en Bogotá.

Lo tengo. De aquí en adelante, si me dices "el premium" o "el de entrada" ya sé de cuál hablamos, y si dices "los competidores" no te voy a preguntar quiénes son.

Tres cosas que **no** me diste y que van a condicionar cualquier campaña que armemos (no las necesito ahora mismo, pero apenas entremos en números me van a hacer falta):

1. **Precios reales y margen** de cada uno — "premium" y "entrada" son relativos, y sin margen no se puede decidir cuál producto aguanta pauta.
2. **Volumen actual**: cuál de los tres vende más hoy y cuál es tu ticket promedio.
3. **Por dónde llegan hoy** los clientes: Instagram, WhatsApp, marketplace, tienda propia, referidos.

¿Qué quieres planificar? ¿Campaña para lanzar, para mover uno de los tres en específico, o para pelear terreno contra alguno de los competidores?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Te la escribo, pero con una advertencia honesta: una propuesta de valor sale del diferenciador real, y ese dato todavía no me lo diste. Lo único sólido que tengo es lo que sí me contaste: portafolio escalonado (Luna → Sol → Aurora) y foco 100% en Bogotá. Sobre eso construyo tres versiones, cada una en dos oraciones.

**A. Ángulo escalera (mi favorita con la info que tengo)**
> Cuidado personal natural para mujeres de Bogotá que quieren empezar sin gastar de más y subir de nivel cuando su piel lo pida. Entras por Luna, sigues con Sol y llegas a Aurora: una sola marca que te acompaña en todo el camino, no tres marcas distintas.

**B. Ángulo local**
> Somos la marca de cuidado natural hecha para Bogotá: clima, agua y contaminación de esta ciudad, no fórmulas genéricas importadas. Tres productos que cubren rostro, maquillaje y cuerpo, con entrega rápida y una persona real del otro lado del WhatsApp.

**C. Ángulo curaduría**
> No vendemos catálogos de 40 referencias: vendemos tres productos que sí funcionan, uno para cada necesidad. Menos decisiones, menos plata desperdiciada en frascos que terminan en el cajón.

Las tres son defendibles, pero solo una es *tuya*. La pregunta que lo decide:

**¿Por qué una clienta te compra a ti y no a Botica Verde o Skin Lab?** Fórmula, precio, cercanía, ingredientes locales, asesoría, empaque, historia. Si la respuesta es "no sé" o "porque me conocen", eso también es un dato — significa que hoy compites por relación, y la propuesta de valor tiene que apoyarse en eso mientras construyes algo más difícil de copiar.

Dame ese diferenciador y te devuelvo una sola versión afilada, no tres genéricas.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Voy a asumir algo para no dar vueltas: que hoy vendes poco y de forma orgánica, sin pauta corriendo. Si ya tienes cientos de pedidos al mes por un canal específico, esto cambia y me lo dices.

## La regla que ordena todo

**Aurora no se vende a tráfico frío.** Un set facial premium de una marca que la persona no conoce no se compra en 30 segundos viendo un Reel. Luna sí: es crema corporal, precio de entrada, riesgo bajo, decisión rápida.

Entonces los canales no se priorizan "en general", se priorizan por rol:

| Canal | Rol | Producto que empuja |
|---|---|---|
| Instagram (orgánico + Reels) | Descubrimiento | Luna y Sol |
| WhatsApp Business | Cierre y recompra | Los tres |
| Base de correos propia | Ascenso a premium | Sol → Aurora |
| TikTok orgánico | Alcance frío barato | Sol |
| Meta Ads pago | Amplificar lo que ya funciona | Luna |

## Los dos que arrancan (no cinco)

**1. Instagram + WhatsApp como una sola pieza.** En Colombia la venta de belleza se cierra en WhatsApp, no en el checkout. Instagram genera la conversación, WhatsApp la convierte. Catálogo de WhatsApp Business con los tres productos, respuesta rápida, y un formato repetible de contenido: demostración de uso, antes/después realista, y la textura del producto en cámara. Nada de frases de marca sobre fondo beige.

**2. Tu base de correos.** Es lo único que no te pueden quitar y lo único que hace rentable a Aurora. Quien compró Luna hace 45 días es tu mejor candidata para Sol; quien compró Sol dos veces es tu candidata para Aurora. Ese es tu embudo real y no necesita presupuesto de pauta.

## Lo que viene después, en ese orden

**TikTok orgánico** cuando el formato de Instagram ya esté aceitado. Es el mismo video con otro corte, costo marginal casi cero, y el maquillaje natural (Sol) funciona bien ahí. No lo empieces al mismo tiempo que Instagram: dos canales nuevos a la vez terminan mal ejecutados los dos.

**Meta Ads pago** solo cuando tengas volumen de conversaciones y sepas qué mensaje las genera. Si arrancas pauta sin eso, estás pagando por descubrir algo que el orgánico te dice gratis. Y cuando arranques: campaña de clics a WhatsApp, producto Luna, un solo mensaje. Meta necesita alrededor de 50 conversiones semanales por conjunto de anuncios para salir de la fase de aprendizaje — si tu presupuesto no da para eso, el algoritmo nunca aprende y estás quemando plata en fase de prueba permanente.

## Lo que yo no priorizaría ahora

**Marketplaces** (Mercado Libre y similares): te comen margen y no construyen marca. Con Aurora en premium, ahí compites en una grilla donde el único criterio visible es el precio.

**Google Ads de búsqueda**: nadie busca tu marca todavía, y las búsquedas de categoría están copadas por cadenas grandes. Caro para lo que devuelve en esta etapa.

**Pinterest y YouTube**: no por malos, por orden. Requieren volumen de producción que hoy compite con lo que sí convierte.

## Un paso concreto antes de decidir presupuesto

La biblioteca de anuncios de Meta es pública. Busca **Botica Verde** y **Skin Lab** ahí: ves qué anuncios tienen activos, desde cuándo y con cuántas variantes. Un anuncio que lleva tres meses corriendo es un anuncio que les funciona. Eso te ahorra semanas de prueba y no cuesta nada.

Revisa también su Instagram: frecuencia de publicación, formato dominante, y sobre todo si responden comentarios. Si ninguno de los dos atiende bien la conversación, ahí tienes un hueco real — y encaja con el ángulo de "una persona real del otro lado" que te propuse antes.

---

**Lo único que necesito para afinar esto:** ¿por dónde llegan hoy tus clientas? Si ya hay un canal que trae ventas, no se empieza de cero, se dobla la apuesta ahí.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Antes de la tabla, la regla que decide todo esto: **la frecuencia correcta es la que sostienes 12 semanas seguidas.** Publicar 5 veces por semana durante tres semanas y desaparecer un mes es peor que 3 por semana constante — el algoritmo penaliza la intermitencia y tu audiencia deja de esperarte. Empieza por debajo de lo que crees que puedes.

## Frecuencia por canal

| Canal | Frecuencia | Qué publicas |
|---|---|---|
| Instagram feed | 3 por semana | 2 Reels + 1 carrusel |
| Instagram stories | 5 por semana (días hábiles) | Sin producción: cámara y listo |
| TikTok (fase 2) | 4-5 por semana | Recorte del mismo material de Reels |
| Estados de WhatsApp | 2-3 por semana | Producto en uso, pedidos saliendo |
| Difusión WhatsApp | Máximo 2 al mes | Solo con motivo real |
| Correo | 2 al mes (cada 15 días) | Más los automáticos, que no cuentan |

**El piso, para la semana que se te complica:** 2 Reels y las stories. Si solo logras eso, cumpliste. No es lo ideal, pero mantiene la constancia, que es lo que importa en los primeros meses.

## Tres advertencias sobre esa tabla

**Stories no es "más contenido".** Es el canal donde se genera la conversación que después cierras en WhatsApp: encuestas, cajas de preguntas, responder dudas de piel. Cinco stories improvisadas valen más que un Reel perfecto al mes. Y no se planifican, se hacen mientras trabajas.

**La difusión de WhatsApp es el canal más fácil de arruinar.** Dos mensajes al mes a toda tu lista es el techo, y cada uno tiene que tener una razón que la clienta reconozca: lanzamiento, reposición de algo agotado, cierre de promoción. Si mandas "hola, ¿cómo estás? mira esto" cada semana, te bloquean y pierdes el único canal con 90% de apertura que vas a tener.

**TikTok no arranca todavía.** Lo pongo en la tabla para que sepas el número cuando llegues, pero sumar ese canal antes de tener el ritmo de Instagram estable te va a dejar los dos a medias.

## Cómo se reparte entre tus tres productos

No es un tercio para cada uno.

- **Luna y Sol se llevan el 70% del contenido orgánico.** Son los de decisión rápida, los que generan la primera compra y los que funcionan en video corto: textura, aplicación, resultado visible.
- **Aurora se lleva el 30%, y en formato distinto.** Nada de "compra Aurora" en un Reel de 15 segundos. Aurora vive en contenido de profundidad — rutina completa, explicación de ingredientes, testimonio de alguien que lleva dos meses usándolo — y sobre todo en el correo, donde le escribes a gente que ya te compró y ya confía.

Por tema, un reparto que funciona: **6 de cada 10 piezas educativas o de uso, 2 de marca y detrás de cámara, 2 de venta directa.** Si el 100% es venta, la gente deja de mirar. Si el 0% lo es, nadie compra.

## Lo que hace que esto sea sostenible

Una sesión de producción **cada dos semanas**, de tres horas, donde grabas 6 a 8 piezas de una sola vez. Un solo montaje de luz, un solo cambio de ropa, todos los productos sobre la mesa. Si intentas grabar el mismo día que publicas, en tres semanas abandonas — eso es lo que mata el 90% de los calendarios de contenido.

Y una cosa más: **repite lo que funciona.** Un Reel que te trajo 12 conversaciones no se publica una vez. A los 45 días vuelve a subirse con otro gancho de entrada. Tu audiencia no lo tiene memorizado y el alcance orgánico solo llega a una fracción de tus seguidores cada vez.

## Cuándo subir la frecuencia

Cuando cumplas cuatro semanas seguidas sin fallar un solo día del calendario. Ahí, y solo ahí, sumas una pieza semanal. Antes de eso estás construyendo sobre entusiasmo, no sobre un sistema.

Y la métrica que decide si el contenido sirve no son los "me gusta": es **cuántas conversaciones de WhatsApp se abren por semana.** Anótalo cada viernes en una hoja. Si publicas más y ese número no se mueve, el problema es el mensaje, no la frecuencia — y ahí subir a 5 publicaciones por semana solo te va a cansar más rápido.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Aquí hay una precisión que importa: de tus tres productos, **skincare son dos, Aurora y Luna. Sol es maquillaje** y juega otro papel. Te separo el contenido así, porque mezclarlos es el error más común en marcas de belleza con portafolio corto.

## Los formatos, ordenados por lo que hacen

| Formato | Para qué sirve | Producto |
|---|---|---|
| Textura en macro | Detener el scroll | Luna |
| Rutina en tiempo real | Mostrar uso, generar preguntas | Luna, Aurora |
| Respuesta a pregunta real | Abrir conversación | Los tres |
| Ingrediente explicado | Construir autoridad | Aurora |
| Antes/después honesto | Cerrar venta | Aurora |
| Testimonio de clienta | Prueba social | Aurora |
| Detrás de cámara | Diferenciación difícil de copiar | Marca |

## Lo que funciona de verdad en skincare

**La textura es el rey del video corto.** Crema que se extiende, se absorbe, deja la piel con brillo. Macro, luz lateral, sin música épica. Es el único formato donde el producto se vende solo, sin argumento, y es exactamente lo que Luna necesita: producto de entrada, decisión rápida, riesgo bajo. No lo pienses como "contenido de marca", piénsalo como mostrar el producto de cerca durante 8 segundos.

**Las preguntas de tus clientas son tu mejor calendario editorial.** Abre la caja de preguntas en stories, recoge lo que llega, y cada pregunta real se convierte en una pieza. "¿Sirve para piel mixta?", "¿lo uso de día o de noche?", "¿por qué se me reseca tanto la cara acá?". Ese contenido no se te agota nunca y viene con la garantía de que a alguien le interesa, porque alguien lo preguntó.

**El ángulo Bogotá es tu ventaja y casi nadie lo usa bien.** 2.600 metros, clima frío y seco, radiación alta. La piel se comporta distinto que en Medellín o en la costa. Contenido tipo "por qué tu piel se descama en Bogotá y qué hacer" te posiciona como la marca que entiende el contexto local — y es el terreno donde Botica Verde y Skin Lab, si venden fórmulas genéricas, no te pueden seguir sin sonar impostados.

**Antes/después: sirve, pero con reglas.** Misma luz, misma hora del día, sin filtro, y con el plazo declarado ("cuatro semanas usando Aurora en la noche"). El antes/después demasiado pulido genera desconfianza, no deseo. Dos advertencias prácticas: en Colombia los cosméticos tienen registro sanitario y **el lenguaje terapéutico te mete en otra categoría regulatoria** — "hidrata", "suaviza", "mejora la apariencia" sí; "cura el acné", "elimina las manchas", "trata la rosácea" no. Verifica los claims exactos con quien te lleva el tema sanitario. Y segundo: **Meta restringe imágenes de antes/después en pauta**, así que ese material te sirve en orgánico pero necesitas versión alterna cuando pases a pagado.

## El reparto por producto

**Luna** vive de lo sensorial y lo cotidiano. Textura, aplicación después de la ducha, el frasco en el bolso. Formato corto, alta frecuencia, cero explicación técnica. Su trabajo es traer gente nueva.

**Aurora** necesita lo contrario: profundidad y tiempo. Rutina completa explicada, un ingrediente por pieza, testimonio de alguien que lleva dos meses. Nadie compra un set facial premium por un video de 15 segundos — lo compra después de verte tres veces y decidir que sabes de lo que hablas. Aurora se cocina en contenido largo y en correo, no en alcance frío.

**Sol es tu puente y lo estás desaprovechando si lo tratas como producto suelto.** El contenido que mejor funciona ahí es "maquillaje sobre piel preparada": muestras Luna o Aurora primero, y después Sol encima. Un mismo video vende dos productos y hace explícita la escalera de tu portafolio. Es el formato que más naturalmente lleva de un producto al siguiente.

## La serie que yo armaría primero

**Un diario de 4 semanas con Aurora.** Una pieza por semana, misma persona, misma luz, avance real y sin exagerar. Al terminar tienes: cuatro piezas de contenido, un antes/después con credibilidad, material para un correo largo, y un activo que puedes reciclar seis meses. Si además la protagonista es una clienta real y no tú, vale el doble.

Es lo más rentable que puedes producir con Aurora, porque ataca el problema exacto de un producto premium: la persona no duda del producto, duda de si le va a funcionar **a ella**.

## Lo que no funciona, aunque se vea bonito

Frases de marca sobre fondo beige. Fotos de producto en mármol sin mano ni piel. Listas de ingredientes en carrusel sin explicar qué hacen. Publicaciones de "feliz lunes". Todo eso se ve profesional y no abre una sola conversación de WhatsApp — que sigue siendo la métrica con la que decides, no los "me gusta".

Prueba concreta antes de producir nada nuevo: revisa tus últimas 15 publicaciones y marca cuáles trajeron un mensaje. Si tienes menos de tres, el problema no es el formato, es que ninguna pide una respuesta.

---

Sigue pendiente lo mismo de antes: **por qué te compran a ti y no a los otros dos**. Con ese dato el contenido deja de ser una lista de formatos y se convierte en un argumento repetido de diez maneras distintas, que es lo que construye marca.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Te lo pregunté tres veces y no llegó respuesta. Así que cambio el enfoque: voy a asumir que hoy **no tienes un diferenciador definido**, y eso no es una falla — la mayoría de las marcas de belleza pequeñas no lo tienen. La diferenciación casi nunca se descubre mirando hacia adentro; se construye eligiendo un terreno donde puedes pelear y ellos no.

## La regla de fondo

Nadie entra en guerra de precios por decisión propia. Se entra cuando **el único eje visible de comparación es el precio**. Si tu clienta ve tres frascos de crema corporal en tres tiendas de Instagram y no puede distinguir nada más, el precio decide sola. Tu trabajo no es defender tu precio: es hacer que la comparación ocurra en otro eje.

## Los ejes, ordenados por lo que cuesta copiarlos

| Eje | Se copia en | ¿Te sirve? |
|---|---|---|
| Precio | 1 día | No |
| Empaque y estética | 3-4 semanas | No |
| Fórmula | 3-6 meses (más si tienes laboratorio propio) | Solo si es tuya de verdad |
| Servicio y asesoría | Meses, y exige disciplina diaria | Sí |
| Contexto local Bogotá | Se copia el mensaje, no la credibilidad de quien llegó primero | Sí |
| Relación y comunidad | Casi imposible | Sí, es el techo |
| Tu base de datos de clientas | Nunca | Sí, y es lo único 100% tuyo |

Todo lo que está arriba de la línea de "servicio" es carrera perdida. Botica Verde puede bajar el precio mañana y copiarte el empaque el mes que viene. No puede copiarte tener 400 conversaciones abiertas de WhatsApp con mujeres cuya piel conoces por nombre.

## Los tres terrenos que yo pelearía con lo que tienes

**1. Asesoría, no venta de frascos.**

Este es el más fuerte y el más barato de montar. Un diagnóstico corto por WhatsApp antes de la primera compra: cinco o seis preguntas (tipo de piel, qué usa hoy, qué le pasa cuando cambia el clima, si tiene sensibilidad, presupuesto). Tú respondes con una recomendación concreta, y a veces esa recomendación es "todavía no compres Aurora, empieza con Luna".

Eso último es lo que lo vuelve un diferenciador y no un truco de venta. Cuando le dices a una clienta que **no** compre el producto caro todavía, dejas de ser una tienda y te conviertes en alguien en quien confía. Y la clienta que entró por Luna con esa conversación es la que compra Aurora en seis meses, sin descuento.

Además resuelve el problema estructural de Aurora: un set facial premium no se compra por precio, se compra por certeza de que le va a funcionar **a ella**. El diagnóstico es exactamente esa certeza.

**2. Curaduría radical: tres productos, no cuarenta.**

Revisa cuántas referencias tienen Botica Verde y Skin Lab. Si tienen catálogos grandes —que es lo habitual—, tu portafolio corto deja de ser una limitación y pasa a ser el argumento: *"no vendemos 40 productos para que elijas mal. Vendemos tres, uno para cada momento, y te decimos cuál te toca."*

Ojo con esto: solo funciona si de verdad sostienes que son tres. En el momento en que sumas ocho referencias más, perdiste el argumento y quedaste igual que ellos pero con menos catálogo.

**3. Bogotá como especialidad, no como dirección de envío.**

Ya lo mencioné con contenido, pero aquí funciona como posicionamiento. 2.600 metros, aire seco, radiación alta, agua dura. Si construyes autoridad sobre "qué le pasa a la piel en esta ciudad y qué hacer", el precio deja de compararse contra cualquier crema y empieza a compararse contra "la que entiende mi problema específico". Es un terreno que se ocupa por consistencia: quien lo dice durante un año seguido se lo queda, y el que llega después suena a que copió.

## Cuatro palancas concretas que quitan el precio de la mesa

**Garantía real.** "Si en 30 días no ves diferencia, te devuelvo la plata." Con Aurora es donde más rinde, porque el freno de un producto premium no es el precio, es el miedo a botar la plata. Antes de lanzarla, ponle número: si tienes margen sano en Aurora, una devolución del 5-8% se paga sola con el aumento de conversión. Si el margen es apretado, no la lances, la promesa se te vuelve en contra.

**Ritual en vez de producto.** Aurora + Sol vendidos juntos como "rostro preparado y maquillaje encima" ya no es comparable con el set facial de Skin Lab: es otro producto. Un combinado no se compara frasco contra frasco, y ese es todo el punto.

**Seguimiento a los 21 días.** Un mensaje a mano: "¿cómo te fue con Luna?". Cuesta cero, y casi nadie lo hace. Es donde nacen los testimonios, se detectan los problemas antes de la mala reseña y se abre la venta del siguiente escalón sin sonar a venta.

**Contenido con nombre y cara.** Tu marca tiene una persona detrás; las de ellos probablemente no, o no la muestran. Eso no se copia porque copiarlo sería fingirlo.

## El trabajo de campo que te falta

Antes de decidir el eje, dedícale una tarde a esto. No es opcional: la diferenciación se elige contra alguien concreto, y hoy no sabes cómo operan.

Escríbeles a los dos como clienta anónima —una amiga, otro número— y mide cinco cosas: cuánto tardan en responder por WhatsApp, si preguntan algo sobre tu piel o te tiran el catálogo, cuánto demora la entrega en Bogotá, si te escriben después de la compra, y qué llega en la caja. Suma cómo responden los comentarios en Instagram y si tienen anuncios activos en la biblioteca de Meta.

De ahí sale tu hueco. Y en marcas de este tamaño el hueco casi siempre está en lo mismo: responden lento, no preguntan nada antes de vender, y desaparecen después de que les pagas. Si confirmas eso, tu diferenciador ya no es una frase de marca, es una promesa operativa que puedes defender todos los días.

## La señal que te dice si funcionó

**Si necesitas descontar para vender, no tienes diferenciación.** Es la única prueba que sirve.

Concretamente, dos números a mirar en los próximos tres meses: cuántas ventas cierras **sin** mencionar promoción, y cuántas clientas de Luna pasan a Sol o Aurora. Si el primero sube y el segundo se mueve, el eje que elegiste está funcionando. Si vendes solo cuando hay descuento, ya estás en la guerra de precios aunque no la hayas declarado.

Y una cosa que sí necesito para el siguiente paso: **el margen de Aurora**. Sin eso no puedo decirte si la garantía de 30 días es una palanca o una forma elegante de perder plata.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Te voy a dar pocos. El error más común en el trimestre 1 es armar un tablero de 25 métricas que nadie mira en la semana 3. **Máximo 8 números, medidos cada viernes, en una hoja.**

Y una distinción que ordena todo: en los primeros 90 días **no mides resultado, mides si el motor gira**. La facturación de un negocio pequeño en trimestre 1 tiene demasiado ruido — un pedido grande, una amiga que compró, una semana mala. Lo que sí te dice la verdad son los números de proceso.

## Los tres que mandan

**1. Conversaciones nuevas de WhatsApp por semana.** Es tu métrica de cabecera, ya te la había marcado. Todo tu embudo pasa por ahí: si este número no se mueve, nada más importa. Es el único que revisarías si solo pudieras mirar uno.

**2. Tasa de cierre conversación → pedido.** De cada 10 personas que escriben, cuántas compran. Te separa dos problemas que se confunden todo el tiempo: si el primer número es bajo, el problema es el contenido; si el primero está bien y este es bajo, el problema es cómo vendes por WhatsApp o el precio no cuadra con lo que la clienta esperaba.

**3. Porcentaje de ventas sin descuento.** Es la prueba directa de si tu diferenciación existe. Te lo dije en el punto anterior y aquí se convierte en número: si vendes solo cuando hay promoción, ya estás en la guerra de precios.

## El tablero completo

| Capa | KPI | Cada | Qué decisión desbloquea |
|---|---|---|---|
| Ejecución | Piezas publicadas ÷ planificadas | Semana | Si el problema es el mensaje o que no publicaste |
| Descubrimiento | Cuentas alcanzadas **no seguidoras** | Semana | Si el contenido sale de tu burbuja |
| Descubrimiento | Guardados + compartidos por pieza | Semana | Qué formato repetir |
| Conversación | Conversaciones nuevas de WhatsApp | Semana | La métrica madre |
| Conversación | Tiempo hasta la primera respuesta | Semana | Tu diferenciador operativo, si eliges asesoría |
| Venta | Tasa de cierre | Semana | Contenido vs. cierre |
| Venta | Ticket promedio | Mes | Si el combinado Aurora + Sol funciona |
| Venta | Mezcla por producto (% Luna / Sol / Aurora) | Mes | Si Aurora está muerta o solo es lenta |
| Retención | Recompra a 90 días | Mes 3 | Si tienes negocio o solo transacciones |
| Retención | Clientas de Luna que suben a Sol o Aurora | Mes 3 | Si la escalera existe de verdad |
| Activo propio | Tamaño de la lista de correo | Mes | Lo único que no te pueden quitar |

Once en total, pero solo seis se miran semanalmente. Los de retención no tienen sentido antes del mes 3: no hay ciclo de recompra suficiente.

## Cumplimiento de calendario: el que nadie mide y explica todo

Piezas publicadas dividido piezas planificadas. Suena a métrica de escritorio y es la más útil del trimestre 1.

Motivo: cuando en la semana 6 mires las conversaciones y estén planas, la primera pregunta no es "¿el mensaje está mal?" sino **"¿publiqué lo que dije que iba a publicar?"**. Si tu cumplimiento va en 55%, no tienes un problema de estrategia, tienes uno de ejecución, y cambiar el mensaje sería arreglar lo que no está roto. He visto marcas rehacer toda su comunicación cuando lo único que pasaba era que publicaban la mitad.

## Cómo se ve mes a mes

**Mes 1 — línea base.** No hay metas. Solo mides y anotas. Las semanas 1 y 2 son tu punto cero, y cualquier número que te dé alguien de internet para compararte con "el promedio del sector" es ruido: no conoce tu ciudad, tu ticket ni tu punto de partida. La única meta del mes 1 es cumplimiento de calendario por encima del 80%.

**Mes 2 — cierre y mezcla.** Ya tienes tres o cuatro semanas de datos. Aquí se mira la tasa de cierre y la mezcla por producto. Y una pregunta específica: **¿Aurora vendió algo?** Si vendió cero en dos meses, no significa que el producto esté mal — significa que todavía no hay suficiente gente que confíe, que es exactamente lo esperado para un premium en una marca nueva. Aurora se juzga a los 6 meses, no a los 60 días. Lo que sí es señal de alarma es que Luna tampoco se mueva.

**Mes 3 — retención y la decisión de pauta.** Recompra, escalera y si ya tienes volumen para que Meta Ads tenga sentido.

## Los que no vas a medir

**Seguidores.** No pagan. Puedes crecer 800 seguidores y no abrir una conversación.

**Me gusta e impresiones.** Guardados y compartidos sí, porque señalan intención. Los "me gusta" no significan nada en belleza.

**ROAS o CAC**, mientras no tengas pauta corriendo con volumen. Un CAC calculado con 9 ventas es un número inventado con decimales.

**Facturación total como termómetro semanal.** Mirarla cada semana te va a llevar a decisiones nerviosas. Mes a mes está bien; semana a semana es ansiedad disfrazada de análisis.

## La hoja del viernes

Una sola pestaña, una fila por semana, y estas columnas:

`semana | piezas publicadas | piezas planificadas | alcance no seguidoras | conversaciones nuevas | pedidos | pedidos con descuento | ticket promedio`

Diez minutos cada viernes. Con eso construyes en 12 semanas algo que ninguna herramienta te da: **tu propio histórico.** Después de tres meses puedes ver qué semana explotó y qué publicaste esa semana. Eso vale más que cualquier tablero automático.

Ah, y un dato manual que sí conviene guardar: **de dónde llegó cada pedido** (comentario, story, referida, difusión, correo). Se pregunta una sola vez en la conversación y en 90 días te dice dónde poner la plata cuando arranques con pauta.

## El único número absoluto que te doy

**Tiempo de primera respuesta en WhatsApp: bajo 15 minutos en horario hábil.**

Es el único que no depende de tu punto de partida, porque no se compara contra ti misma sino contra Botica Verde y Skin Lab. Y ahí tienes el trabajo de campo que te propuse: escríbeles como clienta y cronométralos. Si ellos responden en tres horas y tú en diez minutos, eso ya no es una frase de marca, es un hecho medible que la clienta siente en la primera interacción.

## El gate del día 90

Tres preguntas. Se responden con la hoja, no con sensación:

1. **¿Las conversaciones semanales están por encima de la semana 3?** Si no, el mensaje está mal, y sumar canales o presupuesto no lo arregla.
2. **¿Más de la mitad de las ventas se cerraron sin descuento?** Si no, el eje de diferenciación que elegiste no está llegando.
3. **¿Alguna clienta de Luna subió a Sol o Aurora?** Aunque sea una. Si son cero en 90 días con seguimiento hecho, la escalera es una idea tuya, no un comportamiento real, y hay que replantear el portafolio o la forma de presentarlo.

Con dos síes de tres, escalas y ahí sí tiene sentido hablar de pauta. Con uno o cero, arreglas el motor antes de meterle plata.

---

Sigue faltando lo mismo: **el margen de Aurora** y **qué vendes hoy al mes**. Con eso puedo convertir estos KPIs en metas con número en vez de "mejora contra tu propia base", y decirte si la garantía de 30 días la puedes pagar.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Vamos con Aurora. Antes del plan, tres cosas que condicionan todo y que prefiero dejar arriba en vez de esconderlas en una nota al pie.

**1. Aurora no se vende a tráfico frío.** Ya lo trabajamos: un set facial premium de una marca que la persona no conoce no se compra en un Reel. Entonces esta no es una campaña de alcance, es una campaña **de dentro hacia afuera**: tu base de clientas de Luna y Sol, tu lista de correo, tus conversaciones abiertas de WhatsApp. Si la piensas como "campaña para conseguir gente nueva que compre Aurora", fracasa en 4 semanas y vas a concluir que Aurora está mal cuando el problema fue el orden.

**2. El plan cambia según una respuesta que no tengo:** ¿cuántas clientas han comprado Aurora hasta hoy?

- **Si son 3 o más** → tienes prueba. La campaña es de venta.
- **Si son cero o una** → no tienes prueba, y ninguna campaña de 4 semanas fabrica confianza de la nada. Entonces el objetivo primario cambia: conseguir las **primeras 5 clientas de Aurora con seguimiento documentado**, que es el activo que hace posible la campaña de los siguientes tres meses. Sigue siendo venta, pero la meta se mide distinto.

Escribo el plan para el escenario 2, que es el más probable, y marco qué cambia si ya tienes prueba.

**3. Aurora sube a 65% del contenido, no a 100%.** Si apagas Luna cuatro semanas, en el mes 2 no tienes gente nueva a quién venderle Aurora después. Luna se queda con una pieza semanal haciendo su trabajo de siempre: traer gente.

---

# Campaña Aurora — 4 semanas

## Objetivo

**Primario:** ventas de Aurora cerradas **sin descuento**.

No te invento el número, pero sí la regla para ponerlo:

| Tu situación | Meta de Aurora a 28 días |
|---|---|
| Nunca has vendido Aurora | 5 unidades, con las 5 clientas en seguimiento documentado |
| Vendes 1-2 al mes hoy | Duplicar: 3-4 |
| Vendes 5+ al mes | Meta = mes anterior + 50%, y el foco pasa a ticket, no a unidades |

**Secundario, y probablemente más valioso que el primario:** terminar la campaña con **3 clientas de Aurora que aceptaron documentar su proceso a 30 días** (foto misma luz, misma hora, semana 0 y semana 4). Ese material es el que te va a vender Aurora durante los siguientes seis meses. Sin eso, en enero estás igual que hoy pero con cuatro semanas menos.

**Indicador adelantado, el que miras cada viernes:** **diagnósticos de piel completados**. Es lo único que controlas del todo, y es la puerta por la que pasa toda venta de Aurora.

## Audiencia

Tres anillos, en orden estricto de prioridad. Empiezas por el centro y solo sales hacia afuera cuando el centro está agotado.

| Anillo | Quiénes | Cómo les llegas | Prioridad |
|---|---|---|---|
| **A1** | Compraron Luna o Sol hace más de 45 días. Doble compra = tope de lista | WhatsApp 1 a 1, mensaje escrito a mano | Máxima |
| **A2** | Lista de correo + conversaciones de WhatsApp que preguntaron y no compraron | Secuencia de correo + difusión | Alta |
| **A3** | Seguidoras que guardan, comentan o responden stories | Contenido orgánico + caja de preguntas | Media |
| **Fuera** | Tráfico frío, pauta a desconocidos, marketplaces | No entran en esta campaña | — |

**Quién es ella, en concreto:** mujer en Bogotá que ya gasta en cuidado de piel, que probó tres o cuatro cosas y ninguna le duró, y a la que el clima seco y la altura le pasan factura. **Su freno no es el precio de Aurora. Su freno es "ya boté plata antes en algo que no me sirvió".** Toda la campaña se escribe contra ese freno, no contra el precio.

Ojo con A1: es tu anillo más valioso y el más fácil de arruinar. No se le manda difusión. Se le escribe uno por uno, con el nombre, mencionando qué compró y cuándo. Si son 40 personas, son 40 mensajes en dos tardes. Es el trabajo menos glamoroso de la campaña y el que va a traer la mayoría de las ventas.

## Mensaje principal

**El mensaje núcleo, que se repite de diez formas distintas durante 4 semanas:**

> **Antes de venderte Aurora, quiero saber cómo está tu piel.** Aurora es una rutina completa pensada para lo que la altura y el aire seco de Bogotá le hacen a la piel — y si no es lo que necesitas hoy, te lo digo y te recomiendo empezar por otro lado.

Eso hace tres cosas al mismo tiempo: pone el diagnóstico como puerta de entrada, ancla el ángulo Bogotá que tus competidores no pueden reclamar sin sonar impostados, y **te da permiso para decir que no**, que es exactamente lo que vuelve creíble el sí.

**La estructura del argumento, en orden:**

| Capa | Qué dice |
|---|---|
| Promesa | Una rutina completa para tu piel en esta ciudad, no un frasco suelto |
| Razón para creer | El diagnóstico previo: no te vendo Aurora sin saber tu tipo de piel |
| Prueba | Clientas reales con seguimiento a 30 días, misma luz, sin filtro |
| Reversión de riesgo | Garantía de 30 días — **condicionada a tu margen, ver abajo** |
| Cierre | Cupos de diagnóstico limitados por semana, porque los haces tú |

**Las cuatro objeciones y su respuesta.** Escríbelas y ténlas a mano en WhatsApp, porque van a aparecer todas:

1. *"Está caro"* → No compares Aurora contra una crema. Compárala contra los tres productos que compraste este año y no terminaste. Y el precio nunca abre el mensaje: va después de la razón, en la conversación, no en el pie de foto.
2. *"¿Me va a funcionar a mí?"* → Para eso es el diagnóstico. Y para eso es la garantía.
3. *"Ya tengo una rutina"* → Perfecto, cuéntame cuál. Es la mejor puerta que existe: te da la información del diagnóstico gratis y la conversación se abre sola.
4. *"Prefiero probar algo más barato primero"* → Válido, y te digo cuál: Luna. **No la peleas.** Esa clienta entra por Luna y compra Aurora en seis meses; discutirle la pierdes hoy y mañana.

**Lo que no puedes decir:** nada terapéutico. "Hidrata", "suaviza", "mejora la apariencia" sí. "Cura", "elimina manchas", "trata" no. Verifica los claims exactos de Aurora con quien te lleve el registro sanitario antes de la semana 1, no en la semana 3 cuando ya publicaste.

## Canales y su rol

| Canal | Rol en la campaña Aurora | Volumen en 4 semanas |
|---|---|---|
| **WhatsApp 1 a 1** | Donde se vende Aurora. Todo lo demás alimenta esto | Todo A1, uno por uno |
| **Correo** | El motor de la campaña. Es donde Aurora se explica con espacio | 4 correos a segmento |
| **Instagram feed** | Prueba pública y autoridad | 8 piezas de Aurora + 4 de Luna |
| **Stories** | Conversación diaria y captación de diagnósticos | 5 por semana |
| **Difusión WhatsApp** | Dos disparos, con motivo real | 2 en todo el mes |
| **Pauta Meta** | Solo retargeting a quien ya te vio, y solo si tu píxel tiene datos | Opcional, sin presupuesto nuevo |
| TikTok / marketplaces / Google | No entran | 0 |

**Sobre los 4 correos:** te había dicho 2 al mes. Una campaña con secuencia justifica subir a 4, con dos condiciones: van **al segmento**, no a toda la lista, y cada uno tiene un motivo que la lectora reconoce. Terminada la campaña, vuelves a 2.

**Sobre pauta:** en 4 semanas y con este volumen, Meta no sale de fase de aprendizaje. Meterle presupuesto a Aurora en frío ahora es pagar por descubrir lo que la conversación te dice gratis. Si igual quieres usarla, que sea retargeting a quien visitó la página de Aurora, con presupuesto mínimo, y sabiendo que es un experimento, no un canal. Y recuerda que las imágenes de antes/después están restringidas en pauta: ese material es de orgánico.

---

## Las 4 semanas

### Semana 1 — Diagnóstico. Cero venta.

El objetivo de esta semana es que la palabra "Aurora" empiece a aparecer asociada a *entender la piel*, no a *comprar un set*.

| Qué | Detalle |
|---|---|
| Contenido | 2 piezas sobre qué le hace Bogotá a la piel (altura, aire seco, radiación, agua dura) + 1 pieza de Luna |
| Stories | Caja de preguntas: "cuéntame qué le pasa a tu piel en esta ciudad". Todas las respuestas son tu calendario editorial del mes |
| Lanzamiento | Abres el **Diagnóstico Aurora**: 6 preguntas por WhatsApp, gratis, con recomendación honesta al final |
| Correo 1 | El problema, no el producto. Cierre: "responde este correo con tu tipo de piel y te digo por dónde empezar" |
| A1 | Empiezas los mensajes uno a uno. No vendes: preguntas cómo le fue con Luna o Sol |
| Interno | Reclutas 3 clientas para documentar Aurora a 30 días. Si tienes que regalar las 3 unidades, hazlo: es costo de producción de tu activo más importante |
| Número a mirar | Diagnósticos completados |

En al menos 1 de cada 4 diagnósticos, la recomendación honesta va a ser "empieza por Luna". Dilo. Esa es la campaña.

### Semana 2 — Prueba. Por qué Aurora y no cualquier otra cosa.

| Qué | Detalle |
|---|---|
| Contenido | 1 ingrediente de Aurora explicado (qué hace, por qué está ahí) + 1 rutina completa en tiempo real + 1 de Luna |
| Stories | Diagnósticos en curso, respuestas reales, la semana 1 de las 3 clientas que están documentando |
| Correo 2 | Historia: una clienta que llegó con un problema concreto y qué pasó. Si no tienes ninguna, la tuya propia con Aurora |
| A1 | Sigues uno por uno. A quien respondió bien, le ofreces el diagnóstico. Aún no mencionas precio |
| Número a mirar | Diagnósticos → conversaciones donde surge Aurora |

### Semana 3 — Oferta. Aquí aparece el precio.

| Qué | Detalle |
|---|---|
| Contenido | 1 pieza del ritual **Aurora + Sol** (rostro preparado, maquillaje encima) + 1 testimonio + 1 de Luna |
| Stories | La garantía explicada por ti, hablando a cámara. No en texto sobre fondo |
| Correo 3 | La oferta completa: qué trae Aurora, para quién es, para quién no, garantía, y el ritual como opción |
| Difusión WhatsApp 1 | Anuncio de los cupos de diagnóstico de la semana. Motivo real, no "hola mira esto" |
| A1 | A quien ya hizo diagnóstico, propuesta concreta con precio |
| Número a mirar | Tasa diagnóstico → venta |

El ritual Aurora + Sol es tu mejor jugada contra Botica Verde y Skin Lab: un combinado no se compara frasco contra frasco. Ese es todo el punto.

### Semana 4 — Cierre.

| Qué | Detalle |
|---|---|
| Contenido | 1 pieza de objeciones respondidas + 1 de las 3 clientas en su semana 3-4 + 1 de Luna |
| Stories | Q&A en vivo o caja de preguntas solo sobre Aurora. Respondes todo, incluido el precio |
| Correo 4 | Cierre con fecha. La urgencia tiene que ser verdad: cupos de diagnóstico, no un descuento falso |
| Difusión WhatsApp 2 | Último llamado, mismo motivo real |
| A1 | Segundo toque a quien no respondió. Uno solo. Si no responde, se cierra y queda para el próximo ciclo |
| Cierre interno | Las 3 clientas documentadas te entregan foto de semana 4 y una frase escrita |

**La urgencia no puede ser un descuento.** Si cierras Aurora con 20% off, destruiste en una semana el trabajo de cuatro y le enseñaste a tu base a esperar la promoción. La escasez legítima aquí es tu tiempo: los diagnósticos los haces tú y no te alcanza para más de X por semana. Eso es cierto y se sostiene.

---

## Métricas de éxito

**Semanales, en la misma hoja del viernes:**

`semana | diagnósticos completados | conversaciones donde surge Aurora | ventas Aurora | ventas Aurora con descuento | ventas Luna+Sol`

**Al día 28, los cinco números que juzgan la campaña:**

| KPI | Por qué importa |
|---|---|
| Ventas de Aurora **sin descuento** | El número que define si hay negocio premium |
| Diagnósticos completados | Tu motor. Si es bajo, nada más se explica |
| Tasa diagnóstico → venta de Aurora | Separa problema de mensaje vs. problema de cierre |
| % de compradoras de Aurora que ya eran clientas de Luna o Sol | Confirma que la escalera existe de verdad |
| Ticket promedio del mes | Si el ritual Aurora + Sol funcionó, sube aunque las unidades sean pocas |

**Y uno que no es de venta pero es el que más vale:** 3 clientas de Aurora con documentación de 30 días completa. Si terminas con eso y con 2 ventas, la campaña fue mejor que si terminas con 6 ventas y cero material.

**Lo que no mides:** alcance, seguidores, "me gusta", ROAS. Nada de eso decide algo aquí.

### El gate del día 28

1. **¿Hubo al menos una venta de Aurora sin descuento?** Si sí, tienes producto vendible y solo falta volumen. Si no, el problema es la prueba: te falta material de clientas reales, no más publicaciones.
2. **¿La tasa diagnóstico → venta pasa el 15%?** Si los diagnósticos fluyen y ninguno convierte, el problema está en el precio contra el valor percibido, o en que Aurora se está ofreciendo a gente que todavía no está lista. Ahí revisas la oferta, no el contenido.
3. **¿Alguna compradora de Aurora venía de Luna o Sol?** Si sí, la escalera es real y el próximo trimestre se construye ahí. Si todas fueron clientas nuevas, tu portafolio no funciona como escalera y hay que replantear cómo lo presentas.

Con dos síes de tres, repites el ciclo el mes siguiente con la prueba que acabas de fabricar, y ahí sí tiene sentido hablar de pauta. Con uno o cero, no relanzas: arreglas.

---

## Cuatro riesgos concretos

**La garantía de 30 días sigue sin luz verde.** Es la palanca más fuerte de toda la campaña y no puedo aprobarla sin el margen de Aurora. Regla simple: si el margen bruto de Aurora aguanta una devolución del 8% sin quedar en rojo, lánzala. Si no, cámbiala por algo que no cuesta plata: acompañamiento a 30 días con seguimiento tuyo, y cambio por otro producto en vez de devolución de dinero.

**Quemar la lista.** Cuatro correos y dos difusiones en un mes es el techo. Si al día 20 vas mal y la tentación es mandar dos correos más, no lo hagas: el costo de esa decisión se paga durante seis meses en tasa de apertura.

**Canibalizar Luna.** Si en la semana 3 ves que Luna se frenó en seco, no es problema, es la mecánica de la campaña. Pero por eso mantienes 1 pieza semanal de Luna: la campaña de Aurora del mes que viene se alimenta de las clientas de Luna de este mes.

**Los claims.** Revisa el lenguaje de Aurora antes de la semana 1. Un correo con una promesa terapéutica no se puede desmandar.

---

## Lo que necesito para convertir esto en un plan con números

Sigue siendo lo mismo que vengo pidiendo, y ahora es lo único que separa este plan de uno accionable con metas reales:

1. **Precio y margen bruto de Aurora** → define si la garantía va, y cuánto puedes gastar en conseguir cada venta.
2. **Cuántas Aurora has vendido en total hasta hoy** → define escenario 1 o 2.
3. **Tamaño de tu lista de correo y cuántas clientas han comprado alguna vez** → convierte "5 ventas" en una meta calculada en vez de un piso razonable.

Dame esos tres y te devuelvo el mismo plan con metas numéricas por semana, y te digo si la garantía de 30 días es tu mejor palanca o una forma elegante de perder plata.


## Respuesta completa

Vamos con Aurora. Antes del plan, tres cosas que condicionan todo y que prefiero dejar arriba en vez de esconderlas en una nota al pie.

**1. Aurora no se vende a tráfico frío.** Ya lo trabajamos: un set facial premium de una marca que la persona no conoce no se compra en un Reel. Entonces esta no es una campaña de alcance, es una campaña **de dentro hacia afuera**: tu base de clientas de Luna y Sol, tu lista de correo, tus conversaciones abiertas de WhatsApp. Si la piensas como "campaña para conseguir gente nueva que compre Aurora", fracasa en 4 semanas y vas a concluir que Aurora está mal cuando el problema fue el orden.

**2. El plan cambia según una respuesta que no tengo:** ¿cuántas clientas han comprado Aurora hasta hoy?

- **Si son 3 o más** → tienes prueba. La campaña es de venta.
- **Si son cero o una** → no tienes prueba, y ninguna campaña de 4 semanas fabrica confianza de la nada. Entonces el objetivo primario cambia: conseguir las **primeras 5 clientas de Aurora con seguimiento documentado**, que es el activo que hace posible la campaña de los siguientes tres meses. Sigue siendo venta, pero la meta se mide distinto.

Escribo el plan para el escenario 2, que es el más probable, y marco qué cambia si ya tienes prueba.

**3. Aurora sube a 65% del contenido, no a 100%.** Si apagas Luna cuatro semanas, en el mes 2 no tienes gente nueva a quién venderle Aurora después. Luna se queda con una pieza semanal haciendo su trabajo de siempre: traer gente.

---

# Campaña Aurora — 4 semanas

## Objetivo

**Primario:** ventas de Aurora cerradas **sin descuento**.

No te invento el número, pero sí la regla para ponerlo:

| Tu situación | Meta de Aurora a 28 días |
|---|---|
| Nunca has vendido Aurora | 5 unidades, con las 5 clientas en seguimiento documentado |
| Vendes 1-2 al mes hoy | Duplicar: 3-4 |
| Vendes 5+ al mes | Meta = mes anterior + 50%, y el foco pasa a ticket, no a unidades |

**Secundario, y probablemente más valioso que el primario:** terminar la campaña con **3 clientas de Aurora que aceptaron documentar su proceso a 30 días** (foto misma luz, misma hora, semana 0 y semana 4). Ese material es el que te va a vender Aurora durante los siguientes seis meses. Sin eso, en enero estás igual que hoy pero con cuatro semanas menos.

**Indicador adelantado, el que miras cada viernes:** **diagnósticos de piel completados**. Es lo único que controlas del todo, y es la puerta por la que pasa toda venta de Aurora.

## Audiencia

Tres anillos, en orden estricto de prioridad. Empiezas por el centro y solo sales hacia afuera cuando el centro está agotado.

| Anillo | Quiénes | Cómo les llegas | Prioridad |
|---|---|---|---|
| **A1** | Compraron Luna o Sol hace más de 45 días. Doble compra = tope de lista | WhatsApp 1 a 1, mensaje escrito a mano | Máxima |
| **A2** | Lista de correo + conversaciones de WhatsApp que preguntaron y no compraron | Secuencia de correo + difusión | Alta |
| **A3** | Seguidoras que guardan, comentan o responden stories | Contenido orgánico + caja de preguntas | Media |
| **Fuera** | Tráfico frío, pauta a desconocidos, marketplaces | No entran en esta campaña | — |

**Quién es ella, en concreto:** mujer en Bogotá que ya gasta en cuidado de piel, que probó tres o cuatro cosas y ninguna le duró, y a la que el clima seco y la altura le pasan factura. **Su freno no es el precio de Aurora. Su freno es "ya boté plata antes en algo que no me sirvió".** Toda la campaña se escribe contra ese freno, no contra el precio.

Ojo con A1: es tu anillo más valioso y el más fácil de arruinar. No se le manda difusión. Se le escribe uno por uno, con el nombre, mencionando qué compró y cuándo. Si son 40 personas, son 40 mensajes en dos tardes. Es el trabajo menos glamoroso de la campaña y el que va a traer la mayoría de las ventas.

## Mensaje principal

**El mensaje núcleo, que se repite de diez formas distintas durante 4 semanas:**

> **Antes de venderte Aurora, quiero saber cómo está tu piel.** Aurora es una rutina completa pensada para lo que la altura y el aire seco de Bogotá le hacen a la piel — y si no es lo que necesitas hoy, te lo digo y te recomiendo empezar por otro lado.

Eso hace tres cosas al mismo tiempo: pone el diagnóstico como puerta de entrada, ancla el ángulo Bogotá que tus competidores no pueden reclamar sin sonar impostados, y **te da permiso para decir que no**, que es exactamente lo que vuelve creíble el sí.

**La estructura del argumento, en orden:**

| Capa | Qué dice |
|---|---|
| Promesa | Una rutina completa para tu piel en esta ciudad, no un frasco suelto |
| Razón para creer | El diagnóstico previo: no te vendo Aurora sin saber tu tipo de piel |
| Prueba | Clientas reales con seguimiento a 30 días, misma luz, sin filtro |
| Reversión de riesgo | Garantía de 30 días — **condicionada a tu margen, ver abajo** |
| Cierre | Cupos de diagnóstico limitados por semana, porque los haces tú |

**Las cuatro objeciones y su respuesta.** Escríbelas y ténlas a mano en WhatsApp, porque van a aparecer todas:

1. *"Está caro"* → No compares Aurora contra una crema. Compárala contra los tres productos que compraste este año y no terminaste. Y el precio nunca abre el mensaje: va después de la razón, en la conversación, no en el pie de foto.
2. *"¿Me va a funcionar a mí?"* → Para eso es el diagnóstico. Y para eso es la garantía.
3. *"Ya tengo una rutina"* → Perfecto, cuéntame cuál. Es la mejor puerta que existe: te da la información del diagnóstico gratis y la conversación se abre sola.
4. *"Prefiero probar algo más barato primero"* → Válido, y te digo cuál: Luna. **No la peleas.** Esa clienta entra por Luna y compra Aurora en seis meses; discutirle la pierdes hoy y mañana.

**Lo que no puedes decir:** nada terapéutico. "Hidrata", "suaviza", "mejora la apariencia" sí. "Cura", "elimina manchas", "trata" no. Verifica los claims exactos de Aurora con quien te lleve el registro sanitario antes de la semana 1, no en la semana 3 cuando ya publicaste.

## Canales y su rol

| Canal | Rol en la campaña Aurora | Volumen en 4 semanas |
|---|---|---|
| **WhatsApp 1 a 1** | Donde se vende Aurora. Todo lo demás alimenta esto | Todo A1, uno por uno |
| **Correo** | El motor de la campaña. Es donde Aurora se explica con espacio | 4 correos a segmento |
| **Instagram feed** | Prueba pública y autoridad | 8 piezas de Aurora + 4 de Luna |
| **Stories** | Conversación diaria y captación de diagnósticos | 5 por semana |
| **Difusión WhatsApp** | Dos disparos, con motivo real | 2 en todo el mes |
| **Pauta Meta** | Solo retargeting a quien ya te vio, y solo si tu píxel tiene datos | Opcional, sin presupuesto nuevo |
| TikTok / marketplaces / Google | No entran | 0 |

**Sobre los 4 correos:** te había dicho 2 al mes. Una campaña con secuencia justifica subir a 4, con dos condiciones: van **al segmento**, no a toda la lista, y cada uno tiene un motivo que la lectora reconoce. Terminada la campaña, vuelves a 2.

**Sobre pauta:** en 4 semanas y con este volumen, Meta no sale de fase de aprendizaje. Meterle presupuesto a Aurora en frío ahora es pagar por descubrir lo que la conversación te dice gratis. Si igual quieres usarla, que sea retargeting a quien visitó la página de Aurora, con presupuesto mínimo, y sabiendo que es un experimento, no un canal. Y recuerda que las imágenes de antes/después están restringidas en pauta: ese material es de orgánico.

---

## Las 4 semanas

### Semana 1 — Diagnóstico. Cero venta.

El objetivo de esta semana es que la palabra "Aurora" empiece a aparecer asociada a *entender la piel*, no a *comprar un set*.

| Qué | Detalle |
|---|---|
| Contenido | 2 piezas sobre qué le hace Bogotá a la piel (altura, aire seco, radiación, agua dura) + 1 pieza de Luna |
| Stories | Caja de preguntas: "cuéntame qué le pasa a tu piel en esta ciudad". Todas las respuestas son tu calendario editorial del mes |
| Lanzamiento | Abres el **Diagnóstico Aurora**: 6 preguntas por WhatsApp, gratis, con recomendación honesta al final |
| Correo 1 | El problema, no el producto. Cierre: "responde este correo con tu tipo de piel y te digo por dónde empezar" |
| A1 | Empiezas los mensajes uno a uno. No vendes: preguntas cómo le fue con Luna o Sol |
| Interno | Reclutas 3 clientas para documentar Aurora a 30 días. Si tienes que regalar las 3 unidades, hazlo: es costo de producción de tu activo más importante |
| Número a mirar | Diagnósticos completados |

En al menos 1 de cada 4 diagnósticos, la recomendación honesta va a ser "empieza por Luna". Dilo. Esa es la campaña.

### Semana 2 — Prueba. Por qué Aurora y no cualquier otra cosa.

| Qué | Detalle |
|---|---|
| Contenido | 1 ingrediente de Aurora explicado (qué hace, por qué está ahí) + 1 rutina completa en tiempo real + 1 de Luna |
| Stories | Diagnósticos en curso, respuestas reales, la semana 1 de las 3 clientas que están documentando |
| Correo 2 | Historia: una clienta que llegó con un problema concreto y qué pasó. Si no tienes ninguna, la tuya propia con Aurora |
| A1 | Sigues uno por uno. A quien respondió bien, le ofreces el diagnóstico. Aún no mencionas precio |
| Número a mirar | Diagnósticos → conversaciones donde surge Aurora |

### Semana 3 — Oferta. Aquí aparece el precio.

| Qué | Detalle |
|---|---|
| Contenido | 1 pieza del ritual **Aurora + Sol** (rostro preparado, maquillaje encima) + 1 testimonio + 1 de Luna |
| Stories | La garantía explicada por ti, hablando a cámara. No en texto sobre fondo |
| Correo 3 | La oferta completa: qué trae Aurora, para quién es, para quién no, garantía, y el ritual como opción |
| Difusión WhatsApp 1 | Anuncio de los cupos de diagnóstico de la semana. Motivo real, no "hola mira esto" |
| A1 | A quien ya hizo diagnóstico, propuesta concreta con precio |
| Número a mirar | Tasa diagnóstico → venta |

El ritual Aurora + Sol es tu mejor jugada contra Botica Verde y Skin Lab: un combinado no se compara frasco contra frasco. Ese es todo el punto.

### Semana 4 — Cierre.

| Qué | Detalle |
|---|---|
| Contenido | 1 pieza de objeciones respondidas + 1 de las 3 clientas en su semana 3-4 + 1 de Luna |
| Stories | Q&A en vivo o caja de preguntas solo sobre Aurora. Respondes todo, incluido el precio |
| Correo 4 | Cierre con fecha. La urgencia tiene que ser verdad: cupos de diagnóstico, no un descuento falso |
| Difusión WhatsApp 2 | Último llamado, mismo motivo real |
| A1 | Segundo toque a quien no respondió. Uno solo. Si no responde, se cierra y queda para el próximo ciclo |
| Cierre interno | Las 3 clientas documentadas te entregan foto de semana 4 y una frase escrita |

**La urgencia no puede ser un descuento.** Si cierras Aurora con 20% off, destruiste en una semana el trabajo de cuatro y le enseñaste a tu base a esperar la promoción. La escasez legítima aquí es tu tiempo: los diagnósticos los haces tú y no te alcanza para más de X por semana. Eso es cierto y se sostiene.

---

## Métricas de éxito

**Semanales, en la misma hoja del viernes:**

`semana | diagnósticos completados | conversaciones donde surge Aurora | ventas Aurora | ventas Aurora con descuento | ventas Luna+Sol`

**Al día 28, los cinco números que juzgan la campaña:**

| KPI | Por qué importa |
|---|---|
| Ventas de Aurora **sin descuento** | El número que define si hay negocio premium |
| Diagnósticos completados | Tu motor. Si es bajo, nada más se explica |
| Tasa diagnóstico → venta de Aurora | Separa problema de mensaje vs. problema de cierre |
| % de compradoras de Aurora que ya eran clientas de Luna o Sol | Confirma que la escalera existe de verdad |
| Ticket promedio del mes | Si el ritual Aurora + Sol funcionó, sube aunque las unidades sean pocas |

**Y uno que no es de venta pero es el que más vale:** 3 clientas de Aurora con documentación de 30 días completa. Si terminas con eso y con 2 ventas, la campaña fue mejor que si terminas con 6 ventas y cero material.

**Lo que no mides:** alcance, seguidores, "me gusta", ROAS. Nada de eso decide algo aquí.

### El gate del día 28

1. **¿Hubo al menos una venta de Aurora sin descuento?** Si sí, tienes producto vendible y solo falta volumen. Si no, el problema es la prueba: te falta material de clientas reales, no más publicaciones.
2. **¿La tasa diagnóstico → venta pasa el 15%?** Si los diagnósticos fluyen y ninguno convierte, el problema está en el precio contra el valor percibido, o en que Aurora se está ofreciendo a gente que todavía no está lista. Ahí revisas la oferta, no el contenido.
3. **¿Alguna compradora de Aurora venía de Luna o Sol?** Si sí, la escalera es real y el próximo trimestre se construye ahí. Si todas fueron clientas nuevas, tu portafolio no funciona como escalera y hay que replantear cómo lo presentas.

Con dos síes de tres, repites el ciclo el mes siguiente con la prueba que acabas de fabricar, y ahí sí tiene sentido hablar de pauta. Con uno o cero, no relanzas: arreglas.

---

## Cuatro riesgos concretos

**La garantía de 30 días sigue sin luz verde.** Es la palanca más fuerte de toda la campaña y no puedo aprobarla sin el margen de Aurora. Regla simple: si el margen bruto de Aurora aguanta una devolución del 8% sin quedar en rojo, lánzala. Si no, cámbiala por algo que no cuesta plata: acompañamiento a 30 días con seguimiento tuyo, y cambio por otro producto en vez de devolución de dinero.

**Quemar la lista.** Cuatro correos y dos difusiones en un mes es el techo. Si al día 20 vas mal y la tentación es mandar dos correos más, no lo hagas: el costo de esa decisión se paga durante seis meses en tasa de apertura.

**Canibalizar Luna.** Si en la semana 3 ves que Luna se frenó en seco, no es problema, es la mecánica de la campaña. Pero por eso mantienes 1 pieza semanal de Luna: la campaña de Aurora del mes que viene se alimenta de las clientas de Luna de este mes.

**Los claims.** Revisa el lenguaje de Aurora antes de la semana 1. Un correo con una promesa terapéutica no se puede desmandar.

---

## Lo que necesito para convertir esto en un plan con números

Sigue siendo lo mismo que vengo pidiendo, y ahora es lo único que separa este plan de uno accionable con metas reales:

1. **Precio y margen bruto de Aurora** → define si la garantía va, y cuánto puedes gastar en conseguir cada venta.
2. **Cuántas Aurora has vendido en total hasta hoy** → define escenario 1 o 2.
3. **Tamaño de tu lista de correo y cuántas clientas han comprado alguna vez** → convierte "5 ventas" en una meta calculada en vez de un piso razonable.

Dame esos tres y te devuelvo el mismo plan con metas numéricas por semana, y te digo si la garantía de 30 días es tu mejor palanca o una forma elegante de perder plata.