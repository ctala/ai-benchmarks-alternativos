# DeepSeek V4.1 Flash — agent_long_horizon/clarification_quality

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 91.258s | tokens_per_second: 91.7
- input_tokens: 5134 | output_tokens: 8799

## Conversación completa (4 turnos)

### Turno 1 — usuario

Necesito que me hagas la propuesta.

### Turno 1 — modelo

Claro, con gusto — pero antes necesito entender qué propuesta es, porque ahora mismo no tengo contexto y cualquier cosa que escriba sería inventada.

Dime lo esencial:

1. **¿Propuesta de qué?** (comercial a un cliente, proyecto, servicios profesionales, inversión, colaboración, presupuesto interno…)
2. **¿Para quién?** Tipo de cliente/empresa y, si aplica, quién la va a leer y decidir.
3. **¿Cuál es el objetivo?** ¿Que firmen, que pidan más información, que aprueben un presupuesto, que acepten una alianza?
4. **¿Qué ofreces exactamente?** Alcance, entregables, plazos y, si lo tienes, precio o rango.
5. **¿Formato y extensión?** Correo breve, documento de 2-3 páginas, presentación, one-pager.

Si lo que necesitas es arrancar rápido, mi **supuesto** sería: propuesta comercial de servicios, en formato documento de 1-2 páginas, dirigida a un cliente potencial, con estructura de problema → solución → alcance → precio → siguiente paso. Dime si te sirve esa base y la relleno con tus datos, o pásame los puntos de arriba y la hago a medida.

### Turno 2 — usuario

Es una propuesta comercial. Para un cliente nuevo. Yo vendo software.

### Turno 2 — modelo

Perfecto. Con eso ya sé la categoría, pero en software la propuesta cambia mucho según el modelo de venta, así que te dejo **4 preguntas** (las que de verdad cambian el documento) y, debajo, un **esqueleto listo** para que solo rellenemos huecos.

**Lo que necesito saber:**

1. **Qué tipo de software y cómo se cobra:** ¿SaaS/suscripción, licencia, desarrollo a medida, implantación + cuota, servicio gestionado? Esto define la sección de inversión.
2. **Cliente y problema:** sector, tamaño aproximado, y quién decide (área técnica, dirección, finanzas). ¿Qué dolor le resuelves y qué pasa si no lo resuelve?
3. **Precio y plazo:** ¿me das cifras y fechas, o los pongo como `[PLACEHOLDER]` para que los completes tú?
4. **Formato y acción deseada:** ¿one-pager, documento de 3-5 páginas, PPT, o correo? ¿Y qué quieres que haga al leerlo (agendar demo, firmar, pedir PO)?

**Supuestos que estoy usando mientras no me digas lo contrario** (dímelo si alguno falla):
- Formato: documento de 3-4 páginas + versión correo de envío.
- Modelo: suscripción anual con implantación inicial.
- Objetivo: agendar una demo/reunión técnica, no cierre inmediato.
- Precios y fechas: placeholders.

**Esqueleto que usaría:**

1. **Resumen ejecutivo** — 4 líneas: problema, solución, resultado esperado, inversión. Escrito para que se entienda sin leer el resto.
2. **Contexto y problema** — en las palabras del cliente, no en las tuyas.
3. **Solución propuesta** — qué hace el software, cómo encaja en su operación, qué cambia el día 1.
4. **Alcance** — entregables, módulos incluidos y **explícitamente lo que no incluye** (esto evita el 80% de los conflictos).
5. **Implementación** — fases, hitos, qué necesitas de ellos y cuándo.
6. **Inversión** — desglose, condiciones de pago, vigencia de la oferta, qué pasa al renovar.
7. **Supuestos y responsabilidades del cliente** — dependencias, accesos, personas.
8. **Por qué nosotros** — 2-3 pruebas concretas (caso, métrica, referencia), breve.
9. **Siguiente paso** — una sola acción, con fecha.

Pásame los puntos 1-4 (aunque sea en bruto y desordenado) y te escribo la propuesta completa. Si prefieres velocidad, dime "tira con los supuestos" y te entrego el documento con placeholders marcados para que solo cambies cifras.

### Turno 3 — usuario

Es una agencia de viajes mediana, 30 empleados, en Lima. Mi software es un CRM con módulo de cotización rápida para vendedores de turismo. Quieren saber qué les ofrezco y precio.

### Turno 3 — modelo

Perfecto, con eso ya puedo escribirla. Voy con los supuestos que declaré antes (suscripción anual + implantación, objetivo = agendar demo, formato documento + correo).

**Único hueco material: el precio.** No lo invento. Abajo te dejo la propuesta completa con la estructura de precios armada y las cifras como `[PLACEHOLDER]`. Al final te digo exactamente qué 3 datos necesito para cerrarla. Los rangos que verás son **referencia de mercado LATAM para CRM mid-market, no tu precio** — ajústalos o dímelos.

---

# Propuesta comercial
## CRM con cotización rápida para [Nombre de la Agencia]

**Preparado para:** [Nombre], [Cargo] — [Agencia de Viajes]
**Preparado por:** [Tu nombre], [Tu empresa]
**Fecha:** [fecha] · **Válida hasta:** [fecha + 30 días]

---

### 1. Resumen ejecutivo

Una agencia de 30 personas en Lima cotiza hoy en Excel, WhatsApp y correo: cada cotización toma [X] minutos, vive en el chat de un vendedor y se pierde cuando ese vendedor está ocupado. En temporada alta eso se traduce directamente en ventas no cerradas.

Proponemos un CRM con **módulo de cotización rápida** diseñado para venta turística: el vendedor arma una cotización con tarifas y márgenes en minutos, la envía con la marca de la agencia y el sistema le recuerda hacer seguimiento hasta el cierre. La gerencia ve por primera vez cuántas cotizaciones se emiten, cuántas se convierten y con qué margen.

**Inversión:** [S/ X] de implantación + [S/ Y] mensuales por [N] usuarios.
**Siguiente paso:** demo de 45 min con el equipo comercial ([fecha propuesta]).

---

### 2. Situación actual

Lo que suele pasar en agencias de este tamaño (valídalo con ellos, es la parte que más resuena):

- Las cotizaciones se hacen una y otra vez desde cero, porque no hay tarifas ni plantillas centralizadas.
- El seguimiento depende de la memoria del vendedor. La venta turística se gana en el tercer o cuarto contacto, no en el primero.
- No hay visibilidad: gerencia no sabe cuántas cotizaciones hay abiertas ni cuánto valen.
- La información del cliente (viajes previos, preferencias, pasaporte, condiciones) está dispersa.
- Cuando un vendedor se va, se va con su cartera.

**El costo real no es el software que no tienen. Es la cotización que no se siguió.**

---

### 3. Qué ofrecemos

**a) Módulo de cotización rápida**
- Plantillas de paquetes y servicios (vuelos, hoteles, traslados, tours, seguros).
- Tarifas y temporadas configurables, con cálculo de margen automático por cotización.
- Cotización en PDF con la marca de la agencia, lista para enviar.
- Duplicar y ajustar una cotización anterior en lugar de empezar de cero.

**b) CRM comercial**
- Pipeline con etapas propias de venta turística: consulta → cotizado → en seguimiento → reservado / perdido.
- Recordatorios automáticos de seguimiento por oportunidad.
- Historial del cliente: viajes anteriores, preferencias, documentación, notas.
- Registro de motivos de pérdida (para saber por qué se cae la venta: precio, fechas, competencia).

**c) Visibilidad para gerencia**
- Cotizaciones emitidas vs. cerradas, por vendedor y por período.
- Ticket promedio y margen por cotización.
- Tiempo de respuesta a la consulta inicial.
- Embudo por etapa y proyección del mes.

**d) Integraciones**
- Correo y WhatsApp para enviar y registrar la conversación en la ficha del cliente. `[Confirmar: WhatsApp Business API / integración simple]`

---

### 4. Alcance

**Incluido:**
- Configuración de [N] usuarios y perfiles (vendedor / supervisor / gerencia).
- Carga inicial de clientes y catálogo de servicios/tarifas desde su data actual.
- Plantillas de cotización con identidad de la agencia.
- Capacitación: [2] sesiones en vivo + manual y videos cortos.
- Soporte durante la implantación y [30] días de acompañamiento post-lanzamiento.

**No incluido** (evita el 80% de los malentendidos):
- Migración de historial no estructurado (chats, correos sueltos, papeles).
- Desarrollo de funcionalidades a medida fuera del alcance descrito.
- Licencias de terceros (WhatsApp API, pasarela de pagos, proveedores de contenido turístico).
- Integración con su sistema de reservas/back-office: `[cotizar aparte si lo necesitan]`.
- Hardware, conectividad o soporte de equipos del cliente.

---

### 5. Implementación

| Fase | Qué pasa | Duración |
|---|---|---|
| 1. Descubrimiento | Definimos etapas, tarifas, perfiles y plantillas con [2] personas clave | Semana 1 |
| 2. Configuración | CRM, cotizador, catálogo, permisos, plantillas | Semanas 1-2 |
| 3. Carga y prueba | Migración de clientes/tarifas + prueba con [3] vendedores | Semana 3 |
| 4. Capacitación | Sesiones por rol + manual | Semana 4 |
| 5. Salida en vivo | Arranque con acompañamiento cercano | Semana 5 |

**Plazo total estimado: [4-6] semanas** desde la firma y la entrega de accesos.

---

### 6. Inversión

| Concepto | Importe |
|---|---|
| Implantación (una vez) | `[S/ X]` |
| Suscripción mensual — `[N]` usuarios | `[S/ Y]` / mes |
| Usuario adicional | `[S/ Z]` / mes |
| Contrato | `[12]` meses, renovación automática |

**Condiciones:**
- Facturación mensual/trimestral: `[definir]`.
- Pago de implantación: `[50%]` al inicio, `[50%]` al go-live.
- Precio vigente por `[12]` meses desde la firma.
- No incluye IGV.
- Incluye actualizaciones de la plataforma y soporte en horario `[L-V 9-18]`.

**Alternativa a evaluar:** plan anual prepagado con `[X%]` de descuento — mejora su flujo de caja y reduce la rotación de suscripción.

---

### 7. Supuestos y responsabilidades del cliente

- `[N]` usuarios activos. Si el número sube, aplica tarifa de usuario adicional.
- El cliente designa un responsable interno del proyecto con disponibilidad para las sesiones.
- El cliente entrega accesos, catálogo de tarifas y base de clientes en formato utilizable.
- Las tarifas y márgenes son responsabilidad de la agencia; el sistema los calcula, no los valida.
- Plazos asumen disponibilidad del cliente según el cronograma.

---

### 8. Por qué nosotros

`[2-3 líneas con prueba concreta: cliente del sector, métrica de resultado, tiempo de implantación, referencia contactable. Si no tienes caso en turismo, usa el más cercano en venta consultiva y dilo con honestidad.]`

---

### 9. Siguiente paso

Demo de **45 minutos** con el equipo comercial y gerencia, usando su propio catálogo de tarifas para cotizar un paquete real en vivo.

**Fechas disponibles:** `[opción 1]` / `[opción 2]`

---

### Correo de envío (versión corta)

> **Asunto:** Cotización rápida y seguimiento comercial para [Agencia]
>
> [Nombre]:
>
> Te adjunto la propuesta. En resumen: un CRM donde tus vendedores arman una cotización con tarifas y márgenes en minutos, la envían con la marca de la agencia, y el sistema les obliga a hacer seguimiento hasta el cierre. Gerencia ve cotizaciones emitidas, convertidas y margen por vendedor.
>
> Inversión: [S/ X] de implantación + [S/ Y] mensuales por [N] usuarios. Plazo de puesta en marcha: [4-6] semanas.
>
> Te propongo 45 minutos para cotizar un paquete real de los tuyos en vivo. ¿[fecha] o [fecha]?
>
> [Tu nombre]

---

## Para cerrar la propuesta necesito 3 datos

1. **Número de usuarios y precio:** ¿cuántos vendedores usarían el CRM y cuánto cobras por usuario/mes + implantación? Si aún no lo tienes fijado, dime tu objetivo de ingreso por cliente y te propongo una estructura de 2-3 planes.
2. **WhatsApp:** ¿está en el alcance o lo dejas fuera? Cambia el precio y el plazo.
3. **Caso o referencia:** ¿tienes algún cliente o resultado que pueda poner en la sección 8? Es lo que más mueve la decisión.

Pásame eso y te devuelvo la versión final sin placeholders, lista para enviar.

### Turno 4 — usuario

Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% de descuento. Incluye onboarding gratis 2 semanas. Tienen un competidor actual que cobra $120/usuario sin onboarding.

### Turno 4 — modelo

Con eso cierro los números. Antes de la propuesta, **dos supuestos que debes validar** porque mueven la cifra:

1. **El 15% se aplica al total anual** → precio efectivo **$75,65/usuario/mes** ($89 × 0,85). Si el descuento es otra cosa (ej. 15% solo sobre el primer año, o sobre implantación), dímelo.
2. **El plan Profesional no incluye WhatsApp Business API** (solo registro de conversación manual). Si lo incluyes, sube el precio y hay costo de terceros.

También asumo que los $120 del competidor son precio de lista mensual sin descuento anual comparable. Si ellos también descuentan, la brecha se reduce y conviene no apoyarse tanto en el precio.

---

# Propuesta comercial
## CRM con cotización rápida para [Nombre de la Agencia]

**Preparado para:** [Nombre], [Cargo] — [Agencia de Viajes], Lima
**Preparado por:** [Tu nombre], [Tu empresa]
**Fecha:** [fecha] · **Válida hasta:** [fecha + 30 días]

---

### 1. Resumen ejecutivo

Una agencia de 30 personas en Lima cotiza hoy en Excel, WhatsApp y correo: cada cotización se arma desde cero, vive en el chat de un vendedor y se pierde cuando ese vendedor está ocupado. En temporada alta eso son ventas que no se cierran.

Proponemos un CRM con **módulo de cotización rápida** para venta turística: el vendedor cotiza con tarifas y márgenes en minutos, envía con la marca de la agencia, y el sistema le marca el seguimiento hasta el cierre. Gerencia ve por primera vez cuántas cotizaciones se emiten, cuántas se convierten y con qué margen.

**Inversión:** **USD 75,65 por usuario/mes** (plan anual, 10 usuarios = **USD 756,50/mes**), con **onboarding de 2 semanas incluido sin costo**.
**Siguiente paso:** demo de 45 min cotizando un paquete real de los suyos ([fecha propuesta]).

---

### 2. Situación actual

Lo que suele pasar en agencias de este tamaño (valídalo en la reunión, es la parte que más resuena):

- Cotizaciones repetidas desde cero: no hay tarifas ni plantillas centralizadas.
- El seguimiento depende de la memoria del vendedor. La venta turística se gana en el tercer o cuarto contacto.
- Gerencia no sabe cuántas cotizaciones hay abiertas ni cuánto valen.
- La información del cliente (viajes previos, preferencias, documentación) está dispersa.
- Si se va un vendedor, se va su cartera y su historial.

**El costo real no es el software que no tienen. Es la cotización que no se siguió.**

---

### 3. Qué ofrecemos

**a) Módulo de cotización rápida**
- Plantillas de paquetes y servicios (vuelos, hoteles, traslados, tours, seguros).
- Tarifas y temporadas configurables, con cálculo de margen automático por cotización.
- Cotización en PDF con la marca de la agencia, lista para enviar.
- Duplicar y ajustar una cotización anterior en lugar de empezar de cero.

**b) CRM comercial**
- Pipeline con etapas de venta turística: consulta → cotizado → en seguimiento → reservado / perdido.
- Recordatorios automáticos de seguimiento por oportunidad.
- Ficha de cliente con historial: viajes previos, preferencias, documentación, notas.
- Registro de motivos de pérdida (precio, fechas, competencia).

**c) Visibilidad para gerencia**
- Cotizaciones emitidas vs. cerradas, por vendedor y período.
- Ticket promedio y margen por cotización.
- Tiempo de respuesta a la consulta inicial.
- Embudo por etapa y proyección del mes.

**d) Integraciones**
- Correo y registro de conversaciones de WhatsApp en la ficha del cliente.
- `[Confirmar: alcance exacto de la integración de WhatsApp]`

---

### 4. El plan Profesional en números

| Concepto | Detalle |
|---|---|
| Precio de lista | **USD 89** / usuario / mes |
| Mínimo | **10 usuarios** |
| Contrato anual | **15% de descuento** sobre el total anual |
| **Precio efectivo** | **USD 75,65** / usuario / mes |
| Onboarding | **2 semanas incluidas, sin costo** |
| Implantación / setup | **USD 0** |

**Escenarios según tamaño del equipo comercial:**

| Usuarios | Lista/mes | Anual con 15% dcto. | Equivalente mensual |
|---|---|---|---|
| 10 (mínimo) | USD 890 | **USD 9.078 / año** | USD 756,50 |
| 15 | USD 1.335 | **USD 13.617 / año** | USD 1.134,75 |
| 20 | USD 1.780 | **USD 18.156 / año** | USD 1.513,00 |

**Comparación con la alternativa de mercado que están evaluando:**

| | Este plan | Alternativa actual |
|---|---|---|
| Precio por usuario/mes | **USD 75,65** | USD 120,00 |
| 10 usuarios / año | **USD 9.078** | USD 14.400 |
| Onboarding | **Incluido (2 semanas)** | Se cobra aparte |
| **Ahorro anual** | — | **USD 5.322 (37% menos)** |

El ahorro crece con el equipo: a 15 usuarios son **USD 7.983/año** y a 20 usuarios **USD 10.644/año**.

> **Cómo leerlo:** a 10 usuarios, el CRM se paga con **`[1]` cotización cerrada al mes** (ticket promedio `[S/ X]`). Todo lo demás es margen.

**Condiciones comerciales:**
- Contrato anual, facturación `[mensual/trimestral/anual]`.
- Precio garantizado por 12 meses desde la firma.
- Incluye actualizaciones de plataforma y soporte `[L-V 9-18]`.
- No incluye IGV ni licencias de terceros (WhatsApp API, pasarelas, contenido turístico).

---

### 5. Alcance

**Incluido:**
- Configuración de usuarios y perfiles (vendedor / supervisor / gerencia).
- Carga inicial de clientes y catálogo de servicios y tarifas desde su data actual.
- Plantillas de cotización con identidad de la agencia.
- Onboarding de 2 semanas: sesiones por rol, manual y videos cortos.
- Acompañamiento durante el arranque.

**No incluido** (evita el 80% de los malentendidos):
- Migración de historial no estructurado (chats, correos sueltos, papel).
- Desarrollos a medida fuera de lo descrito.
- Licencias de terceros.
- Integración con su back-office o sistema de reservas: `[cotizar aparte si lo necesitan]`.
- Equipos, conectividad o soporte de hardware del cliente.

---

### 6. Onboarding: 2 semanas, sin costo

| Fase | Qué pasa | Cuándo |
|---|---|---|
| 1. Descubrimiento | Definimos etapas, tarifas, perfiles y plantillas con [2] personas clave | Días 1-2 |
| 2. Configuración | CRM, cotizador, catálogo, permisos, plantillas de marca | Días 3-6 |
| 3. Carga y prueba | Clientes y tarifas cargados + prueba con [3] vendedores | Días 7-9 |
| 4. Capacitación | Sesiones por rol + manual y videos | Días 10-12 |
| 5. Salida en vivo | Arranque acompañado | Días 13-14 |

**Dependencias del cliente:** un responsable interno designado, accesos, catálogo de tarifas y base de clientes en formato utilizable. Si la data llega desordenada o incompleta, el calendario se corre — y conviene decirlo desde ahora, no en la semana 2.

---

### 7. Por qué nosotros

`[2-3 líneas con prueba concreta: cliente del sector, métrica de resultado, tiempo de implantación, referencia contactable. Si no tienes caso en turismo, usa el más cercano en venta consultiva y dilo con honestidad.]`

---

### 8. Siguiente paso

Demo de **45 minutos** con el equipo comercial y gerencia, cotizando un paquete real de los suyos en vivo.

**Fechas disponibles:** `[opción 1]` / `[opción 2]`

---

### Correo de envío

> **Asunto:** Cotización rápida y seguimiento comercial para [Agencia]
>
> [Nombre]:
>
> Te adjunto la propuesta. En resumen: un CRM donde tus vendedores arman una cotización con tarifas y márgenes en minutos, la envían con la marca de la agencia, y el sistema les marca el seguimiento hasta el cierre. Gerencia ve cotizaciones emitidas, convertidas y margen por vendedor.
>
> Plan Profesional: **USD 89/usuario/mes**, mínimo 10 usuarios, con **15% de descuento por contrato anual** (equivale a USD 75,65/usuario/mes) y **onboarding de 2 semanas incluido**. A 10 usuarios son USD 9.078 al año frente a los USD 14.400 de la alternativa que están evaluando.
>
> Te propongo 45 minutos para cotizar un paquete real de los tuyos en vivo. ¿[fecha] o [fecha]?
>
> [Tu nombre]

---

## Lo que queda abierto (3 cosas)

1. **¿Cuántos usuarios van a tomar?** La propuesta está armada con el mínimo de 10 (USD 9.078/año). Si en la reunión detectas que serán 15 o 20, cambia la tabla y conviene que lo lleves pre-calculado.
2. **WhatsApp:** si el plan no lo incluye, la propuesta ya lo dice; si lo incluyes, hay que mover precio y añadir el costo de terceros.
3. **Sección 7:** un caso o referencia. Es lo que más mueve la decisión y es lo único que no puedo rellenar por ti.

Pásame esos tres puntos y te entrego la versión final lista para enviar.


## Respuesta completa

Con eso cierro los números. Antes de la propuesta, **dos supuestos que debes validar** porque mueven la cifra:

1. **El 15% se aplica al total anual** → precio efectivo **$75,65/usuario/mes** ($89 × 0,85). Si el descuento es otra cosa (ej. 15% solo sobre el primer año, o sobre implantación), dímelo.
2. **El plan Profesional no incluye WhatsApp Business API** (solo registro de conversación manual). Si lo incluyes, sube el precio y hay costo de terceros.

También asumo que los $120 del competidor son precio de lista mensual sin descuento anual comparable. Si ellos también descuentan, la brecha se reduce y conviene no apoyarse tanto en el precio.

---

# Propuesta comercial
## CRM con cotización rápida para [Nombre de la Agencia]

**Preparado para:** [Nombre], [Cargo] — [Agencia de Viajes], Lima
**Preparado por:** [Tu nombre], [Tu empresa]
**Fecha:** [fecha] · **Válida hasta:** [fecha + 30 días]

---

### 1. Resumen ejecutivo

Una agencia de 30 personas en Lima cotiza hoy en Excel, WhatsApp y correo: cada cotización se arma desde cero, vive en el chat de un vendedor y se pierde cuando ese vendedor está ocupado. En temporada alta eso son ventas que no se cierran.

Proponemos un CRM con **módulo de cotización rápida** para venta turística: el vendedor cotiza con tarifas y márgenes en minutos, envía con la marca de la agencia, y el sistema le marca el seguimiento hasta el cierre. Gerencia ve por primera vez cuántas cotizaciones se emiten, cuántas se convierten y con qué margen.

**Inversión:** **USD 75,65 por usuario/mes** (plan anual, 10 usuarios = **USD 756,50/mes**), con **onboarding de 2 semanas incluido sin costo**.
**Siguiente paso:** demo de 45 min cotizando un paquete real de los suyos ([fecha propuesta]).

---

### 2. Situación actual

Lo que suele pasar en agencias de este tamaño (valídalo en la reunión, es la parte que más resuena):

- Cotizaciones repetidas desde cero: no hay tarifas ni plantillas centralizadas.
- El seguimiento depende de la memoria del vendedor. La venta turística se gana en el tercer o cuarto contacto.
- Gerencia no sabe cuántas cotizaciones hay abiertas ni cuánto valen.
- La información del cliente (viajes previos, preferencias, documentación) está dispersa.
- Si se va un vendedor, se va su cartera y su historial.

**El costo real no es el software que no tienen. Es la cotización que no se siguió.**

---

### 3. Qué ofrecemos

**a) Módulo de cotización rápida**
- Plantillas de paquetes y servicios (vuelos, hoteles, traslados, tours, seguros).
- Tarifas y temporadas configurables, con cálculo de margen automático por cotización.
- Cotización en PDF con la marca de la agencia, lista para enviar.
- Duplicar y ajustar una cotización anterior en lugar de empezar de cero.

**b) CRM comercial**
- Pipeline con etapas de venta turística: consulta → cotizado → en seguimiento → reservado / perdido.
- Recordatorios automáticos de seguimiento por oportunidad.
- Ficha de cliente con historial: viajes previos, preferencias, documentación, notas.
- Registro de motivos de pérdida (precio, fechas, competencia).

**c) Visibilidad para gerencia**
- Cotizaciones emitidas vs. cerradas, por vendedor y período.
- Ticket promedio y margen por cotización.
- Tiempo de respuesta a la consulta inicial.
- Embudo por etapa y proyección del mes.

**d) Integraciones**
- Correo y registro de conversaciones de WhatsApp en la ficha del cliente.
- `[Confirmar: alcance exacto de la integración de WhatsApp]`

---

### 4. El plan Profesional en números

| Concepto | Detalle |
|---|---|
| Precio de lista | **USD 89** / usuario / mes |
| Mínimo | **10 usuarios** |
| Contrato anual | **15% de descuento** sobre el total anual |
| **Precio efectivo** | **USD 75,65** / usuario / mes |
| Onboarding | **2 semanas incluidas, sin costo** |
| Implantación / setup | **USD 0** |

**Escenarios según tamaño del equipo comercial:**

| Usuarios | Lista/mes | Anual con 15% dcto. | Equivalente mensual |
|---|---|---|---|
| 10 (mínimo) | USD 890 | **USD 9.078 / año** | USD 756,50 |
| 15 | USD 1.335 | **USD 13.617 / año** | USD 1.134,75 |
| 20 | USD 1.780 | **USD 18.156 / año** | USD 1.513,00 |

**Comparación con la alternativa de mercado que están evaluando:**

| | Este plan | Alternativa actual |
|---|---|---|
| Precio por usuario/mes | **USD 75,65** | USD 120,00 |
| 10 usuarios / año | **USD 9.078** | USD 14.400 |
| Onboarding | **Incluido (2 semanas)** | Se cobra aparte |
| **Ahorro anual** | — | **USD 5.322 (37% menos)** |

El ahorro crece con el equipo: a 15 usuarios son **USD 7.983/año** y a 20 usuarios **USD 10.644/año**.

> **Cómo leerlo:** a 10 usuarios, el CRM se paga con **`[1]` cotización cerrada al mes** (ticket promedio `[S/ X]`). Todo lo demás es margen.

**Condiciones comerciales:**
- Contrato anual, facturación `[mensual/trimestral/anual]`.
- Precio garantizado por 12 meses desde la firma.
- Incluye actualizaciones de plataforma y soporte `[L-V 9-18]`.
- No incluye IGV ni licencias de terceros (WhatsApp API, pasarelas, contenido turístico).

---

### 5. Alcance

**Incluido:**
- Configuración de usuarios y perfiles (vendedor / supervisor / gerencia).
- Carga inicial de clientes y catálogo de servicios y tarifas desde su data actual.
- Plantillas de cotización con identidad de la agencia.
- Onboarding de 2 semanas: sesiones por rol, manual y videos cortos.
- Acompañamiento durante el arranque.

**No incluido** (evita el 80% de los malentendidos):
- Migración de historial no estructurado (chats, correos sueltos, papel).
- Desarrollos a medida fuera de lo descrito.
- Licencias de terceros.
- Integración con su back-office o sistema de reservas: `[cotizar aparte si lo necesitan]`.
- Equipos, conectividad o soporte de hardware del cliente.

---

### 6. Onboarding: 2 semanas, sin costo

| Fase | Qué pasa | Cuándo |
|---|---|---|
| 1. Descubrimiento | Definimos etapas, tarifas, perfiles y plantillas con [2] personas clave | Días 1-2 |
| 2. Configuración | CRM, cotizador, catálogo, permisos, plantillas de marca | Días 3-6 |
| 3. Carga y prueba | Clientes y tarifas cargados + prueba con [3] vendedores | Días 7-9 |
| 4. Capacitación | Sesiones por rol + manual y videos | Días 10-12 |
| 5. Salida en vivo | Arranque acompañado | Días 13-14 |

**Dependencias del cliente:** un responsable interno designado, accesos, catálogo de tarifas y base de clientes en formato utilizable. Si la data llega desordenada o incompleta, el calendario se corre — y conviene decirlo desde ahora, no en la semana 2.

---

### 7. Por qué nosotros

`[2-3 líneas con prueba concreta: cliente del sector, métrica de resultado, tiempo de implantación, referencia contactable. Si no tienes caso en turismo, usa el más cercano en venta consultiva y dilo con honestidad.]`

---

### 8. Siguiente paso

Demo de **45 minutos** con el equipo comercial y gerencia, cotizando un paquete real de los suyos en vivo.

**Fechas disponibles:** `[opción 1]` / `[opción 2]`

---

### Correo de envío

> **Asunto:** Cotización rápida y seguimiento comercial para [Agencia]
>
> [Nombre]:
>
> Te adjunto la propuesta. En resumen: un CRM donde tus vendedores arman una cotización con tarifas y márgenes en minutos, la envían con la marca de la agencia, y el sistema les marca el seguimiento hasta el cierre. Gerencia ve cotizaciones emitidas, convertidas y margen por vendedor.
>
> Plan Profesional: **USD 89/usuario/mes**, mínimo 10 usuarios, con **15% de descuento por contrato anual** (equivale a USD 75,65/usuario/mes) y **onboarding de 2 semanas incluido**. A 10 usuarios son USD 9.078 al año frente a los USD 14.400 de la alternativa que están evaluando.
>
> Te propongo 45 minutos para cotizar un paquete real de los tuyos en vivo. ¿[fecha] o [fecha]?
>
> [Tu nombre]

---

## Lo que queda abierto (3 cosas)

1. **¿Cuántos usuarios van a tomar?** La propuesta está armada con el mínimo de 10 (USD 9.078/año). Si en la reunión detectas que serán 15 o 20, cambia la tabla y conviene que lo lleves pre-calculado.
2. **WhatsApp:** si el plan no lo incluye, la propuesta ya lo dice; si lo incluyes, hay que mover precio y añadir el costo de terceros.
3. **Sección 7:** un caso o referencia. Es lo que más mueve la decisión y es lo único que no puedo rellenar por ti.

Pásame esos tres puntos y te entrego la versión final lista para enviar.