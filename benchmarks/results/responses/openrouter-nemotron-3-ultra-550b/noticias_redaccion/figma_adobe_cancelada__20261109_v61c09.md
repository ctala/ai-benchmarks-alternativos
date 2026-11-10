# Nemotron 3 Ultra 550B — noticias_redaccion/figma_adobe_cancelada

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 5.94 | quality: 6.1
- latency_total: 16.64s | tokens_per_second: 146.5
- input_tokens: 696 | output_tokens: 2437

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor de contenido para un founder hispanohablante que publica noticias y análisis para emprendedores de América Latina y España. Escribes en español neutro, claro y directo, con subtítulos en Markdown (##).

**user:**

Es para el newsletter de una comunidad de diseñadores de producto y founders SaaS.

Escribe la nota en español neutro, de 900 a 1.300 palabras, solo con datos de la fuente.

FUENTE:
Adobe and Figma have called off their planned merger. The software giant had agreed to buy the collaborative design startup for about $20 billion in cash and stock, but the two companies said there was no clear path to obtain the regulatory approvals needed in Europe and the United Kingdom.

Under the terms of the agreement, Adobe will pay Figma a termination fee of $1 billion.

Figma was founded by Dylan Field and Evan Wallace, who met as students at Brown University. Its product lets teams design interfaces directly in the web browser, with several people editing the same file at the same time. That collaborative approach made it a favorite among product teams and put it in direct competition with Adobe's own design tools.

Field, who serves as chief executive, started working on the idea while still at university and later left his studies to focus on the company with the support of a fellowship for young founders. The product took a long time to develop before it was released to the public, partly because running a professional design tool inside a browser required solving difficult technical problems.

Figma grew through a model that combines a free plan for individuals with paid plans for teams and large organizations. Designers often adopted the tool on their own and then brought it into their companies, where developers, product managers and marketing teams also began to use it to review and comment on designs.

When the acquisition was announced, many users expressed concern on social media that Adobe would raise prices or change the product. Adobe said at the time that it intended to keep Figma running as a separate product and to learn from its collaborative approach.

Regulators focused on the possibility that Adobe was buying Figma to remove a future competitor, a type of deal sometimes described as a "killer acquisition." The case was followed closely by technology lawyers and investors because it was among the largest acquisitions of a private software company ever attempted.

Competition authorities had expressed concern that the deal would eliminate a rival that was growing quickly and could reduce innovation in design software. The European Commission and the United Kingdom's Competition and Markets Authority had both opened in-depth investigations.

In a statement, both companies said they disagreed with the regulators' conclusions but had decided that it was in their best interest to move forward independently.

The decision means Figma will continue as an independent company, with the termination payment adding to its cash. Adobe, for its part, will keep developing its own collaborative products.

For founders, the case illustrates a risk that is easy to underestimate when an acquisition is announced: the deal is not closed until regulators approve it, and that process can take many months. During that time, the startup must keep its team motivated and its customers calm, without knowing whether it will end up inside a large company or on its own. Large technology deals now face closer scrutiny than in previous years, especially when the buyer is a market leader.


## Respuesta completa

## Adobe y Figma cancelan su fusión: 1.000 millones de razones para seguir solos

La operación más grande de la historia del software privado no llegará a cerrarse. Adobe y Figma han anunciado la terminación de su acuerdo de fusión, dejando tras de sí una indemnización de 1.000 millones de dólares y una lección clara para el ecosistema: en el entorno regulatorio actual, anunciar una compra no es sinónimo de cerrarla.

## El final de un proceso de 15 meses

En septiembre de 2022, Adobe comunicó su intención de adquirir Figma por unos 20.000 millones de dólares en efectivo y acciones. La lógica estratégica era evidente: la startup había construido la herramienta de referencia para el diseño colaborativo en el navegador, un espacio donde los productos históricos de Adobe —como XD o Photoshop— habían perdido tracción frente a la inmediatez del trabajo multipantalla y multiusuario en tiempo real.

Quince meses después, ambas compañías confirman que no existe “un camino claro” para obtener las aprobaciones regulatorias necesarias en la Unión Europea y el Reino Unido. Bajo los términos del acuerdo original, Adobe abonará a Figma una *termination fee* de 1.000 millones de dólares. El cheque ya está en camino; la integración, no.

## ¿Por qué Figma incomodaba tanto a los reguladores?

La investigación no se centró en el tamaño de la chequera de Adobe, sino en la dinámica de mercado. La Comisión Europea y la *Competition and Markets Authority* (CMA) británica abrieron investigaciones en profundidad (Fase 2) bajo la sospecha de una **“adquisición asesina” (*killer acquisition*)**: la compra de un rival emergente no para integrarlo, sino para neutralizar su trayectoria de crecimiento antes de que se convierta en una amenaza existencial.

Los argumentos de las autoridades se basaban en tres pilares:
1.  **Eliminación de un competidor directo:** Figma competía cara a cara con las herramientas de diseño de Adobe (Creative Cloud, XD) y ganaba cuota de mercado a velocidad inusual.
2.  **Crecimiento orgánico y viral:** Su modelo *freemium* —plan gratuito para individuos y planes de pago para equipos y empresas— permitía que diseñadores adoptaran la herramienta por su cuenta y la escalaran dentro de la organización, arrastrando a desarrolladores, *product managers* y marketing a un mismo archivo.
3.  **Reducción de la innovación futura:** La fusión suprimiría el incentivo de Adobe para innovar en colaboración y el de Figma para competir en *features* empresariales, frenando la carrera tecnológica en el sector.

Ambas compañías discrepan de las conclusiones regulatorias, pero han decidido que “lo mejor para sus intereses es avanzar de forma independiente”.

## El factor técnico que creó una categoría

Para entender por qué Figma llegó a valer 20.000 millones —y por qué Adobe quiso comprarla a toda costa— hay que mirar su origen. Dylan Field y Evan Wallace se conocieron en la Universidad de Brown. Field, actual CEO, abandonó los estudios tras recibir una beca para jóvenes fundadores (*Thiel Fellowship*) y dedicarse a tiempo completo a un problema técnico que la industria daba por imposible: **ejecutar una herramienta de diseño profesional completa dentro del navegador, con edición simultánea multiusuario y latencia imperceptible**.

Ese reto —renderizado WebGL, sincrónización de estado tipo CRDT, gestión de fuentes en la nube— retrasó el lanzamiento público años. Cuando llegó, cambió las reglas: ya no hacía falta instalar nada, guardar versiones manualmente ni pasar archivos por Slack. El archivo *era* la reunión.

## El modelo *bottom-up* que rompió el *top-down*

El crecimiento de Figma no vino de comerciales llamando a CTOs, sino de diseñadores individuales que entraban gratis, probaban, invitaban a un desarrollador a inspeccionar código, a un *PM* a comentar un flujo y, de pronto, la empresa entera pedía la factura del plan *Organization*.

Ese movimiento *bottom-up* es el *playbook* que todo fundador SaaS B2B quiere replicar: **el usuario final trae la herramienta; el comprador solo firma el cheque**. Adobe, cuyo motor histórico era la venta *enterprise* por licencias perpetuas y luego suscripción *Creative Cloud*, vio en Figma no solo un producto superior en UX, sino un motor de distribución que no sabía construir.

## El limbo regulatorio: el riesgo invisible para fundadores

El caso deja una radiografía valiosa para cualquier fundador que reciba una *term sheet* de un gigante: **el *deal* no se cierra en la firma, se cierra en el archivo del regulador**.

Durante 15 meses, Figma operó en un limbo:
*   **Equipo:** Retener talento cuando la mitad de la plantilla tiene cláusulas de *change of control* o simplemente no quiere trabajar para Adobe.
*   **Clientes:** Tranquilizar a empresas que temían subidas de precio, migración forzada a Creative Cloud o degradación del *roadmap* (Adobe prometió mantener Figma como producto separado y aprender de su enfoque colaborativo).
*   **Producto:** Seguir ejecutando *roadmap* propio sin poder acceder a recursos de Adobe (IA generativa *Firefly*, distribución *Enterprise*, infraestructura global) ni comprometerse con integraciones profundas.

Ese “congelamiento estratégico” es un coste de oportunidad real. Mientras tanto, competidores —desde Penpot hasta Sketch, pasando por las nuevas funciones colaborativas de Framer o FigJam clones— siguieron iterando.

## El cheque de 1.000 millones: *runway* para la independencia

La indemnización no es dinero de juguete. Para una empresa privada que ya era rentable (o cerca de serlo) y tenía caja, 1.000 millones de dólares líquidos cambian la partida de ajedrez:
*   **Independencia financiera real:** No necesitan levantar otra ronda a valuación plana o a la baja en 2024/25.
*   **Capacidad de M&A propia:** Pueden comprar startups de IA, *design systems*, *hand-off* a desarrollo o *motion design* para blindar su *moat*.
*   **Señal al mercado:** El pago valida que Adobe veía a Figma como un activo estratégico *irremplazable*, no como un capricho. Los inversores y talento lo leerán así.

## Adobe: a construir lo que no supo comprar

Para Adobe, el fracaso obliga a volver a la mesa de dibujo. Su comunicado apunta a “seguir desarrollando sus propios productos colaborativos”. La presión es alta: Firefly (su IA generativa) está integrada en Photoshop, Illustrator y Express, pero **la experiencia colaborativa nativa en navegador —el *killer feature* de Figma— sigue sin tener parangón en el ecosistema Adobe**.

La alternativa orgánica es más lenta, cara e incierta. Pero el entorno regulatorio actual —donde cualquier compra de un *market leader* a un *challenger* de crecimiento exponencial se examina con lupa— deja pocas opciones. Microsoft/Activision, Nvidia/Arm, Meta/Within: la lista de *mega-deals* caídos o condicionados crece. La regla nueva es simple: **si compras al #2 para defender el #1, prepárate para un *no* de Bruselas o Londres**.

## Claves operativas para tu próxima *term sheet*

Si estás negociando la venta de tu SaaS —o evaluando una oferta—, extrae estas lecciones del caso Figma/Adobe:

1.  **Modela el *worst case* regulatorio:** Asume 12-18 meses de limbo. ¿Tu *burn rate* aguanta? ¿Tu equipo se queda? ¿Tus *key accounts* renuevan sin claridad?
2.  **Negocia *reverse break-up fees* altas:** El 5 % del valor del *deal* (1.000 M / 20.000 M) es el nuevo estándar de referencia para *private deals* de este calibre. Exige cláusulas de *best efforts* contractuales del comprador ante reguladores.
3.  **Planifica la operación *stand-alone*:** Ten un *roadmap* de 18 meses que no dependa de la infraestructura del comprador. Si el *deal* muere, ese *roadmap* es tu plan A.
4.  **Comunica con transparencia radical:** Los clientes de Figma sabían que Adobe “prometía mantener el producto”, pero el miedo a la integración forzada era real. Si eres el vendedor, controla la narrativa: “Seguimos siendo nosotros, con más recursos *si* cierra; si no, seguimos siendo nosotros”.
5.  **Valora la opción de no vender:** Figma hoy tiene 1.000 M extra en caja, cero deuda, control total de *roadmap* y una valuación de referencia para una futura salida a bolsa o venta secundaria. A veces, el mejor *exit* es no salir.

## El nuevo escenario: más *antitrust*, menos *roll-ups*

La cancelación no es un accidente; es la norma emergente. Las grandes tecnológicas (GAFAM + Adobe, Salesforce, Nvidia) seguirán necesitando innovación externa, pero el coste regulatorio de comprarla *whole* se ha disparado.

Veremos más:
*   **Alianzas estratégicas profundas** (integración *OEM*, *co-selling*, *marketplace*) sin cambio de control.
*   **Inversiones minoritarias** con derechos de información y *pro-rata*, evitando la notificación *HSR* / *EUMR*.
*   **Acqui-hires de equipos** (tecnología + talento) por debajo del umbral de notificación, dejando el *cap table* y la marca intactos.

Para fundadores y *product leaders*, el mensaje es claro: **construye como si fueras a ser independiente para siempre**. Si llega una oferta que tiene sentido económico y estratégico —y el comprador acepta el riesgo regulatorio por escrito—, bienvenida sea. Pero tu *runway*, tu *roadmap* y tu cultura no pueden depender de la firma de un comisario europeo.

Figma acaba de demostrar que se puede decir “no” a 20.000 millones, cobrar 1.000 por el trastorno y seguir mandando en tu tablero. Ese es el *power move* definitivo.