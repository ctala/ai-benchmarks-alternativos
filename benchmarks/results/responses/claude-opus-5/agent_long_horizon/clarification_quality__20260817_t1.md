# Claude Opus 5 — agent_long_horizon/clarification_quality

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.76 | quality: 10.0
- latency_total: 164.416s | tokens_per_second: 70.1
- input_tokens: 6992 | output_tokens: 10840

## Conversación completa (4 turnos)

### Turno 1 — usuario

Necesito que me hagas la propuesta.

### Turno 1 — modelo

Con gusto, pero ahora mismo no tengo contexto: no sé para quién es la propuesta, qué ofreces ni qué formato necesitas. Si asumo, hay riesgo alto de que te entregue algo inservible.

Lo mínimo que necesito para que salga bien:

1. **Cliente y necesidad**: ¿quién la recibe (empresa, persona, área) y qué problema te planteó? Si tienes el correo, brief o notas de la reunión, pégalos tal cual.
2. **Qué vas a ofrecer**: alcance concreto del trabajo o producto, y qué queda explícitamente fuera.
3. **Precio y plazos**: ¿ya tienes cifra y tiempos definidos, o quieres que te proponga un rango con justificación?
4. **Tipo de documento**: ¿propuesta comercial para cerrar venta, propuesta técnica para licitación, o pitch para inversión? Cambia por completo la estructura.
5. **Formato y extensión**: ¿una página, documento de 5-8 páginas, presentación?

Si prefieres avanzar rápido: mándame los puntos 1 y 2 aunque sea en desordenado, y yo redacto un primer borrador tomando decisiones sobre el resto. En ese caso te dejo marcadas las suposiciones que hice (precio, plazos, formato) para que las corrijas en lugar de que queden escondidas en el texto.

¿Qué camino prefieres?

### Turno 2 — usuario

Es una propuesta comercial. Para un cliente nuevo. Yo vendo software.

### Turno 2 — modelo

Eso acota el formato, pero queda la ambigüedad más costosa sin resolver: "vendo software" puede significar tres negocios muy distintos, y cada uno produce una propuesta con estructura, pricing y objeciones diferentes.

**Lo que necesito saber primero (esto define todo lo demás):**

¿Cuál de estos es tu caso?

- **A) SaaS / producto ya construido**: el cliente se suscribe a algo que ya existe. La propuesta gira en torno a planes, usuarios, onboarding y ROI mensual.
- **B) Desarrollo a medida**: construyes algo que no existe. La propuesta necesita alcance detallado, fases, entregables y protección contra cambios de alcance.
- **C) Producto + implementación**: licencia o suscripción más un proyecto de integración/configuración cobrado aparte. Son dos cotizaciones en un mismo documento.

**Y dos cosas más que cambian el contenido de forma material:**

1. **¿Qué problema te planteó este cliente y cómo lo supiste?** No es lo mismo una propuesta después de una demo donde ya te contaron sus dolores, que una en frío. Si ya hubo conversación, dime qué te dijeron que les duele hoy: eso va en la primera página y es lo que cierra la venta.

2. **¿Ya le diste un número o rango de precio?** Si sí, la propuesta lo confirma y justifica. Si no, la propuesta tiene que introducirlo con más cuidado, y necesito saber si quieres que te sugiera una estructura de pricing o si tú ya la tienes.

---

Si quieres avanzar ya mismo, respóndeme solo la letra (A, B o C) y el punto 1 en dos líneas. Con eso armo el borrador completo y marco entre corchetes todo lo que asumí, para que lo corrijas de un vistazo en lugar de que quede enterrado en el texto.

### Turno 3 — usuario

Es una agencia de viajes mediana, 30 empleados, en Lima. Mi software es un CRM con módulo de cotización rápida para vendedores de turismo. Quieren saber qué les ofrezco y precio.

### Turno 3 — modelo

Con esto ya puedo trabajar. Voy a entregarte el borrador completo, y arriba te dejo explícitas las suposiciones que hice para que las corrijas sin tener que buscarlas en el texto.

---

## Suposiciones que hice (corrígeme lo que esté mal)

1. **Modelo**: SaaS por suscripción mensual/anual + un cobro único de implementación. Si tú vendes licencia perpetua o todo incluido, cambia la sección de precio.
2. **Usuarios**: de los 30 empleados, ~12 son vendedores/asesores que necesitan licencia, más 2-3 entre supervisión y gerencia. El resto (contabilidad, operaciones, counter) no usa el sistema.
3. **Precio**: **puse cifras de referencia entre corchetes**. No las conozco y no debes enviarlas sin reemplazarlas. Al final te explico la lógica que usé para que decidas la tuya.
4. **No hubo discovery profundo**: escribí los dolores como hipótesis del sector turismo, en formato "esto es lo que vemos habitualmente". Si tuviste una reunión y te dijeron sus problemas reales, hay que reemplazar esa sección con sus palabras: es la parte que más vende.
5. **Moneda**: USD para la suscripción, soles para implementación, precios sin IGV. Ajusta según cómo facturas.

---

# Propuesta Comercial

**Para:** [Nombre de la agencia] — At. [Nombre y cargo del contacto]
**De:** [Tu empresa]
**Fecha:** [fecha] · **Validez:** 30 días

---

## 1. Lo que entendemos de su situación

Una agencia con 30 personas y un equipo comercial de ~12 asesores suele enfrentar tres cosas al mismo tiempo:

- **La cotización es el cuello de botella.** El asesor arma el paquete en Excel o en un documento de Word que copia de una cotización anterior, lo pasa a PDF y lo manda por WhatsApp. Entre buscar tarifas, ajustar márgenes y darle formato se van 30-45 minutos por cotización. En un negocio donde el primero que responde suele ganar, eso es margen que se pierde.
- **Los leads viven en bandejas personales.** Consultas que entran por WhatsApp, Instagram, web y teléfono quedan repartidas entre celulares y correos individuales. Nadie sabe con certeza cuántas oportunidades abiertas hay ni cuáles se enfriaron.
- **La cartera es del asesor, no de la agencia.** Cuando un vendedor sale, se va con los contactos, el historial y los viajes recurrentes de sus clientes.

*[Si tuvieron reunión: reemplazar esta sección por lo que el cliente efectivamente dijo, citando sus propias frases. Es lo que más peso tiene en la decisión.]*

---

## 2. Qué proponemos

Implementar **[Nombre del producto]**, un CRM diseñado para agencias de viaje, con motor de cotización rápida integrado.

### Módulo de cotización rápida
- Armado de cotizaciones por bloques reutilizables (vuelo, hotel, traslado, tour, seguro) desde una base de productos y tarifas propia de la agencia.
- Cálculo automático de márgenes, comisiones y totales; alerta si la cotización baja del margen mínimo que la gerencia defina.
- Salida en PDF con la marca de la agencia y envío directo al cliente por correo o WhatsApp.
- Versionado: si el cliente pide cambios, se genera una nueva versión sin perder la anterior.
- **Efecto esperado:** una cotización estándar pasa de 30-45 minutos a menos de 10.

### CRM comercial
- Registro centralizado de clientes con historial completo de viajes, cotizaciones y comunicaciones. La información queda en la agencia.
- Embudo de ventas visible por asesor y por etapa (consulta → cotizado → negociación → cerrado).
- Captura de leads desde formulario web y WhatsApp, con asignación automática o por reglas.
- Tareas y recordatorios de seguimiento; alertas de cotizaciones sin respuesta.
- Alertas de recompra por fecha (aniversarios de viaje, temporadas, clientes corporativos recurrentes).

### Reportes para gerencia
- Tablero de ventas por asesor, destino, canal de origen y ticket promedio.
- Tasa de conversión de cotización a venta y tiempo promedio de respuesta.
- Ranking de destinos y proveedores más rentables.

*[Ajusta esta lista para que refleje solo lo que tu producto hace HOY. Prometer un módulo que está en roadmap es la forma más rápida de perder un cliente en el mes 3.]*

---

## 3. Fuera de alcance

Para evitar malentendidos, esta propuesta **no** incluye:

- Integración con GDS (Amadeus, Sabre) ni con consolidadores.
- Integración con [sistema contable / facturación electrónica SUNAT]. *[Confirma si lo tienes o no.]*
- Módulo de operaciones o file de viaje posventa.
- Desarrollos a medida no listados en la sección 2.

Cualquiera de estos puntos puede cotizarse por separado.

---

## 4. Implementación

| Etapa | Actividad | Plazo |
|---|---|---|
| 1 | Configuración de cuenta, usuarios y permisos | Semana 1 |
| 2 | Carga de base de clientes y catálogo de productos/tarifas | Semanas 1-2 |
| 3 | Configuración de plantillas de cotización con su marca | Semana 2 |
| 4 | Capacitación al equipo comercial (2 sesiones) y a gerencia (1 sesión) | Semana 3 |
| 5 | Acompañamiento en marcha blanca | Semana 4 |

**Puesta en producción estimada: 4 semanas** desde la firma y la entrega de la base de datos.

**Lo que necesitamos de su lado:** un responsable interno del proyecto, la base de clientes en formato digital, y el catálogo de productos y tarifas vigentes.

---

## 5. Inversión

**Suscripción mensual**

| Concepto | Cantidad | Precio unitario | Total mensual |
|---|---|---|---|
| Licencia asesor comercial | 12 | USD [35] | USD [420] |
| Licencia supervisión/gerencia | 3 | USD [45] | USD [135] |
| **Total mensual** | | | **USD [555]** |

**Implementación (pago único)**

| Concepto | Total |
|---|---|
| Configuración, migración de datos y capacitación | S/ [4,500] |

Precios no incluyen IGV. Incluido en la suscripción: soporte por correo y WhatsApp en horario de oficina, actualizaciones, respaldos diarios.

**Opciones de contratación**
- **Mensual:** sin plazo forzoso, 30 días de aviso para cancelar.
- **Anual pagado por adelantado:** [dos meses de descuento] + implementación con [50%] de descuento.

---

## 6. Retorno esperado

Si el equipo de 12 asesores hace un promedio de [4] cotizaciones diarias y cada una baja de 35 a 10 minutos, la agencia recupera cerca de **[20 horas-vendedor por día]**. Aun capturando solo una fracción de eso en más cotizaciones enviadas, la inversión mensual se cubre con **[1 a 2 ventas adicionales al mes]**.

*[Reemplaza estos números con los del cliente si los conoces: volumen real de cotizaciones y ticket promedio. Un cálculo con sus cifras vale mucho más que uno con las mías.]*

---

## 7. Siguientes pasos

1. Reunión de 30 minutos para revisar esta propuesta y ajustar alcance.
2. Demo con dos o tres de sus asesores usando un caso real de cotización.
3. Firma y arranque de implementación.

**Contacto:** [nombre, teléfono, correo]

---

## Sobre el precio: la lógica que usé

Las cifras entre corchetes salen de un rango habitual para CRM vertical de mercado medio en la región (aprox. USD 25-45 por usuario/mes), no de tu estructura de costos. Antes de enviar, define:

- **Tu piso**: costo de servir esta cuenta (infraestructura, soporte, horas de implementación) para no vender bajo costo.
- **Si diferencias precio por tipo de licencia** o cobras plano por usuario. Diferenciar ayuda cuando gerencia quiere tableros que el asesor no necesita.
- **Si cobras la implementación aparte.** Recomiendo que sí, y que puedas descontarla en el plan anual: te da una palanca de negociación que no toca el precio recurrente.

---

**Una cosa que sí cambiaría el documento si me la confirmas:** ¿ya hubo demo o reunión con ellos? Si sí, pásame lo que te dijeron sobre cómo cotizan hoy y cuántas cotizaciones manejan al mes. Con eso reescribo las secciones 1 y 6 con sus datos, que es donde una propuesta se gana o se pierde.

### Turno 4 — usuario

Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% de descuento. Incluye onboarding gratis 2 semanas. Tienen un competidor actual que cobra $120/usuario sin onboarding.

### Turno 4 — modelo

Con el precio real cambia bastante más que la sección 5. Antes del documento, una pregunta que sí altera el enfoque completo, y la respuesta condicional.

---

## La pregunta

**"Tienen un competidor actual que cobra $120/usuario" — ¿la agencia ya está usando y pagando ese software hoy, o es otro proveedor que también está cotizando?**

No es un detalle menor:

- **Si ya lo usan (incumbente):** la propuesta no vende "ordenar el caos", vende *reemplazo*. El dolor no es que coticen en Excel: es que pagan $120 y algo no funciona (lento, no sirve para turismo, sin soporte local, nunca los capacitaron). Y aparecen dos objeciones que hay que desactivar en el documento: **la migración de datos** y **el contrato vigente con el otro proveedor**. El ROI se vuelve trivial de demostrar porque es ahorro duro, no productividad estimada.
- **Si es un competidor en la misma licitación:** ahí sí conviene mi versión anterior (dolor operativo + productividad), y el precio se maneja distinto: no conviene anclar en "somos más baratos", conviene anclar en onboarding incluido y que el ahorro es consecuencia.

**Asumo el primer caso (ya lo usan)** porque dijiste "competidor actual". Abajo va la propuesta con ese enfoque. Si es el segundo caso, dímelo y te devuelvo la versión ajustada: cambian las secciones 1, 5 y 6.

---

## Otras suposiciones nuevas

1. **15 licencias** (12 asesores + 3 gerencia). Ya no diferencio precio por tipo: tu plan es plano a $89. Si son 12, dejé la cifra alternativa anotada.
2. **El 15% se aplica al precio unitario con compromiso de 12 meses, facturado mensual.** Si tu descuento exige pago anual adelantado, avísame: cambia el argumento de flujo de caja y hay que decirlo explícito.
3. **Eliminé el cobro de implementación** (S/ 4,500) porque el onboarding va incluido, y **comprimí el cronograma a 2 semanas**. Ver la advertencia al final sobre esto.

---

# Propuesta Comercial

**Para:** [Nombre de la agencia] — At. [Nombre y cargo]
**De:** [Tu empresa]
**Fecha:** [fecha] · **Validez:** 30 días

---

## 1. Punto de partida

La agencia ya trabaja con un CRM. La decisión, entonces, no es *si* usar un sistema, sino si el que tienen justifica lo que cuesta.

Lo que vemos habitualmente en agencias que llegan a este punto:

- **Se paga por un CRM genérico y se cotiza por fuera.** El sistema guarda contactos, pero el asesor sigue armando el paquete en Excel o Word porque la herramienta no entiende cómo se cotiza un viaje: bloques de vuelo, hotel, traslado, tour, márgenes por componente. La cotización, que es el corazón del negocio, queda fuera del sistema.
- **Se paga por licencias que nadie usa.** Sin capacitación real, la adopción se estanca: dos o tres asesores lo usan bien y el resto vuelve a su libreta.
- **El soporte responde en otro huso horario y en otro idioma.** Un problema un viernes de temporada alta se resuelve el martes.

*[Reemplazar por lo que efectivamente dijeron. Si te contaron por qué están mirando alternativas, esa frase textual debe abrir el documento.]*

---

## 2. Qué proponemos

Migrar a **[Nombre del producto]**, CRM con motor de cotización rápida diseñado específicamente para agencias de viaje.

### Módulo de cotización rápida
- Cotizaciones por bloques reutilizables (vuelo, hotel, traslado, tour, seguro) desde el catálogo de tarifas propio de la agencia.
- Cálculo automático de márgenes y comisiones, con alerta cuando una cotización baja del margen mínimo definido por gerencia.
- PDF con la marca de la agencia, enviado por correo o WhatsApp desde el sistema.
- Versionado de cotizaciones: los cambios del cliente no borran el historial.
- **Efecto esperado:** de 30-45 minutos a menos de 10 por cotización estándar.

### CRM comercial
- Ficha de cliente con historial de viajes, cotizaciones y comunicaciones. La cartera queda en la agencia, no en el celular del asesor.
- Embudo por asesor y etapa: consulta → cotizado → negociación → cerrado.
- Captura de leads desde web y WhatsApp con asignación por reglas.
- Recordatorios de seguimiento y alertas de cotizaciones sin respuesta.
- Alertas de recompra por temporada, aniversario de viaje y clientes corporativos recurrentes.

### Reportes de gerencia
- Ventas por asesor, destino, canal y ticket promedio.
- Conversión de cotización a venta y tiempo de respuesta.
- Rentabilidad por destino y proveedor.

*[Deja solo lo que el producto hace hoy.]*

---

## 3. Migración desde su sistema actual

Incluido en el onboarding, sin costo adicional:

- Exportación y carga de base de clientes, contactos e historial disponible.
- Carga del catálogo de productos y tarifas vigentes.
- Configuración de plantillas de cotización con su identidad de marca.
- Operación en paralelo durante la marcha blanca: nadie se queda sin sistema mientras se hace el cambio.

**Requerimos de su lado:** un responsable interno del proyecto y la exportación de datos del sistema actual en formato digital (CSV o Excel). Si su proveedor actual restringe la exportación, avísenos: lo hemos resuelto antes y hay alternativas.

---

## 4. Cronograma

| Etapa | Actividad | Plazo |
|---|---|---|
| 1 | Configuración de cuenta, usuarios y permisos | Días 1-2 |
| 2 | Migración de clientes y carga de catálogo de tarifas | Días 3-6 |
| 3 | Plantillas de cotización con su marca | Días 6-7 |
| 4 | Capacitación: 2 sesiones al equipo comercial, 1 a gerencia | Días 8-10 |
| 5 | Marcha blanca con acompañamiento | Días 11-14 |

**Operación plena en 2 semanas** desde la firma y la entrega de datos. El onboarding completo está incluido.

---

## 5. Inversión

**Plan Profesional** — mínimo 10 usuarios

| Concepto | Cant. | Precio lista | Con compromiso anual (-15%) |
|---|---|---|---|
| Licencia Plan Profesional | 15 | USD 89 /usuario/mes | USD 75.65 /usuario/mes |
| **Total mensual** | | USD 1,335 | **USD 1,134.75** |
| **Total 12 meses** | | USD 16,020 | **USD 13,617** |

Precios sin IGV. *[Si son 12 usuarios: USD 907.80/mes — USD 10,893.60 al año.]*

**Incluido sin costo adicional:** onboarding completo de 2 semanas, migración de datos, capacitación del equipo, plantillas personalizadas, actualizaciones, respaldos diarios y soporte en horario local por correo y WhatsApp.

**Sin costos de implementación. Sin cargos de configuración.**

---

## 6. Comparación con su costo actual

| | Sistema actual | [Tu producto] |
|---|---|---|
| Precio por usuario/mes | USD 120 | **USD 75.65** |
| Costo mensual (15 usuarios) | USD 1,800 | **USD 1,134.75** |
| Costo anual | USD 21,600 | **USD 13,617** |
| Onboarding y migración | No incluido | **Incluido** |
| Capacitación del equipo | No incluida | **Incluida (3 sesiones)** |
| Módulo de cotización para turismo | No | **Sí** |
| Soporte en horario local | [Confirmar] | **Sí** |

### Ahorro anual: USD 7,983

**37% menos por usuario**, con el onboarding y la capacitación incluidos. El ahorro del primer año equivale aproximadamente a [X] paquetes vendidos de ticket promedio, o al costo de [referencia relevante para ellos].

Y el ahorro no es el argumento principal: es el módulo de cotización, que es donde el equipo comercial gana o pierde ventas todos los días.

*[Verifica el precio del competidor antes de enviar. Si el cliente lo mencionó de memoria, puede incluir módulos o cantidad de usuarios distintos. Una comparación que ellos puedan desmentir con su factura te cuesta credibilidad.]*

---

## 7. Siguientes pasos

1. Demo de 30 minutos con dos o tres asesores, cotizando un caso real de los suyos.
2. Revisión de la exportación de datos de su sistema actual.
3. Firma y arranque: operación plena en 2 semanas.

**Contacto:** [nombre, teléfono, correo]

---

## Tres cosas que deberías decidir antes de enviar

**1. El cronograma de 2 semanas es ajustado para una migración.** Configurar desde cero en dos semanas es razonable; migrar clientes, historial y catálogo de tarifas desde otro sistema, más capacitar a 12 asesores, es otra cosa. Si tu onboarding gratuito es de 2 semanas fijas, decide qué pasa si la migración se extiende: ¿acompañas igual, o el día 15 empieza a correr un costo? Es mejor definirlo tú ahora que improvisarlo en la semana 3 con el cliente molesto.

**2. El mínimo de 10 usuarios es una puerta que ellos pueden usar.** Si comparan contra los $120 que ya pagan, la tentación va a ser comprar 10 licencias y rotar accesos entre 15 personas. Define si permites eso o si el contrato ata licencias a usuarios nombrados.

**3. No entregues el 15% junto con la comparación de precio en la primera versión.** Ya les estás mostrando 37% de ahorro y onboarding gratis. Si además el descuento anual aparece como precio de entrada, no te queda nada para la negociación final, y en una decisión de compra de este tamaño casi siempre hay una ronda más. Una opción: presenta el precio lista de $89 con la comparación (que ya gana: $89 vs $120, con onboarding incluido) y reserva el 15% para cerrar el compromiso anual cuando pidan mejora.

---

**Para cerrar el documento me falta un dato:** ¿cuántas licencias son realmente y cuándo vence el contrato con su proveedor actual? Lo segundo es clave: si les quedan seis meses de contrato, la propuesta debe incluir cómo manejar el traslape (arranque diferido, o los primeros meses con descuento adicional para que no paguen dos sistemas). Si no lo abordas tú, esa es la objeción que va a congelar la decisión.


## Respuesta completa

Con el precio real cambia bastante más que la sección 5. Antes del documento, una pregunta que sí altera el enfoque completo, y la respuesta condicional.

---

## La pregunta

**"Tienen un competidor actual que cobra $120/usuario" — ¿la agencia ya está usando y pagando ese software hoy, o es otro proveedor que también está cotizando?**

No es un detalle menor:

- **Si ya lo usan (incumbente):** la propuesta no vende "ordenar el caos", vende *reemplazo*. El dolor no es que coticen en Excel: es que pagan $120 y algo no funciona (lento, no sirve para turismo, sin soporte local, nunca los capacitaron). Y aparecen dos objeciones que hay que desactivar en el documento: **la migración de datos** y **el contrato vigente con el otro proveedor**. El ROI se vuelve trivial de demostrar porque es ahorro duro, no productividad estimada.
- **Si es un competidor en la misma licitación:** ahí sí conviene mi versión anterior (dolor operativo + productividad), y el precio se maneja distinto: no conviene anclar en "somos más baratos", conviene anclar en onboarding incluido y que el ahorro es consecuencia.

**Asumo el primer caso (ya lo usan)** porque dijiste "competidor actual". Abajo va la propuesta con ese enfoque. Si es el segundo caso, dímelo y te devuelvo la versión ajustada: cambian las secciones 1, 5 y 6.

---

## Otras suposiciones nuevas

1. **15 licencias** (12 asesores + 3 gerencia). Ya no diferencio precio por tipo: tu plan es plano a $89. Si son 12, dejé la cifra alternativa anotada.
2. **El 15% se aplica al precio unitario con compromiso de 12 meses, facturado mensual.** Si tu descuento exige pago anual adelantado, avísame: cambia el argumento de flujo de caja y hay que decirlo explícito.
3. **Eliminé el cobro de implementación** (S/ 4,500) porque el onboarding va incluido, y **comprimí el cronograma a 2 semanas**. Ver la advertencia al final sobre esto.

---

# Propuesta Comercial

**Para:** [Nombre de la agencia] — At. [Nombre y cargo]
**De:** [Tu empresa]
**Fecha:** [fecha] · **Validez:** 30 días

---

## 1. Punto de partida

La agencia ya trabaja con un CRM. La decisión, entonces, no es *si* usar un sistema, sino si el que tienen justifica lo que cuesta.

Lo que vemos habitualmente en agencias que llegan a este punto:

- **Se paga por un CRM genérico y se cotiza por fuera.** El sistema guarda contactos, pero el asesor sigue armando el paquete en Excel o Word porque la herramienta no entiende cómo se cotiza un viaje: bloques de vuelo, hotel, traslado, tour, márgenes por componente. La cotización, que es el corazón del negocio, queda fuera del sistema.
- **Se paga por licencias que nadie usa.** Sin capacitación real, la adopción se estanca: dos o tres asesores lo usan bien y el resto vuelve a su libreta.
- **El soporte responde en otro huso horario y en otro idioma.** Un problema un viernes de temporada alta se resuelve el martes.

*[Reemplazar por lo que efectivamente dijeron. Si te contaron por qué están mirando alternativas, esa frase textual debe abrir el documento.]*

---

## 2. Qué proponemos

Migrar a **[Nombre del producto]**, CRM con motor de cotización rápida diseñado específicamente para agencias de viaje.

### Módulo de cotización rápida
- Cotizaciones por bloques reutilizables (vuelo, hotel, traslado, tour, seguro) desde el catálogo de tarifas propio de la agencia.
- Cálculo automático de márgenes y comisiones, con alerta cuando una cotización baja del margen mínimo definido por gerencia.
- PDF con la marca de la agencia, enviado por correo o WhatsApp desde el sistema.
- Versionado de cotizaciones: los cambios del cliente no borran el historial.
- **Efecto esperado:** de 30-45 minutos a menos de 10 por cotización estándar.

### CRM comercial
- Ficha de cliente con historial de viajes, cotizaciones y comunicaciones. La cartera queda en la agencia, no en el celular del asesor.
- Embudo por asesor y etapa: consulta → cotizado → negociación → cerrado.
- Captura de leads desde web y WhatsApp con asignación por reglas.
- Recordatorios de seguimiento y alertas de cotizaciones sin respuesta.
- Alertas de recompra por temporada, aniversario de viaje y clientes corporativos recurrentes.

### Reportes de gerencia
- Ventas por asesor, destino, canal y ticket promedio.
- Conversión de cotización a venta y tiempo de respuesta.
- Rentabilidad por destino y proveedor.

*[Deja solo lo que el producto hace hoy.]*

---

## 3. Migración desde su sistema actual

Incluido en el onboarding, sin costo adicional:

- Exportación y carga de base de clientes, contactos e historial disponible.
- Carga del catálogo de productos y tarifas vigentes.
- Configuración de plantillas de cotización con su identidad de marca.
- Operación en paralelo durante la marcha blanca: nadie se queda sin sistema mientras se hace el cambio.

**Requerimos de su lado:** un responsable interno del proyecto y la exportación de datos del sistema actual en formato digital (CSV o Excel). Si su proveedor actual restringe la exportación, avísenos: lo hemos resuelto antes y hay alternativas.

---

## 4. Cronograma

| Etapa | Actividad | Plazo |
|---|---|---|
| 1 | Configuración de cuenta, usuarios y permisos | Días 1-2 |
| 2 | Migración de clientes y carga de catálogo de tarifas | Días 3-6 |
| 3 | Plantillas de cotización con su marca | Días 6-7 |
| 4 | Capacitación: 2 sesiones al equipo comercial, 1 a gerencia | Días 8-10 |
| 5 | Marcha blanca con acompañamiento | Días 11-14 |

**Operación plena en 2 semanas** desde la firma y la entrega de datos. El onboarding completo está incluido.

---

## 5. Inversión

**Plan Profesional** — mínimo 10 usuarios

| Concepto | Cant. | Precio lista | Con compromiso anual (-15%) |
|---|---|---|---|
| Licencia Plan Profesional | 15 | USD 89 /usuario/mes | USD 75.65 /usuario/mes |
| **Total mensual** | | USD 1,335 | **USD 1,134.75** |
| **Total 12 meses** | | USD 16,020 | **USD 13,617** |

Precios sin IGV. *[Si son 12 usuarios: USD 907.80/mes — USD 10,893.60 al año.]*

**Incluido sin costo adicional:** onboarding completo de 2 semanas, migración de datos, capacitación del equipo, plantillas personalizadas, actualizaciones, respaldos diarios y soporte en horario local por correo y WhatsApp.

**Sin costos de implementación. Sin cargos de configuración.**

---

## 6. Comparación con su costo actual

| | Sistema actual | [Tu producto] |
|---|---|---|
| Precio por usuario/mes | USD 120 | **USD 75.65** |
| Costo mensual (15 usuarios) | USD 1,800 | **USD 1,134.75** |
| Costo anual | USD 21,600 | **USD 13,617** |
| Onboarding y migración | No incluido | **Incluido** |
| Capacitación del equipo | No incluida | **Incluida (3 sesiones)** |
| Módulo de cotización para turismo | No | **Sí** |
| Soporte en horario local | [Confirmar] | **Sí** |

### Ahorro anual: USD 7,983

**37% menos por usuario**, con el onboarding y la capacitación incluidos. El ahorro del primer año equivale aproximadamente a [X] paquetes vendidos de ticket promedio, o al costo de [referencia relevante para ellos].

Y el ahorro no es el argumento principal: es el módulo de cotización, que es donde el equipo comercial gana o pierde ventas todos los días.

*[Verifica el precio del competidor antes de enviar. Si el cliente lo mencionó de memoria, puede incluir módulos o cantidad de usuarios distintos. Una comparación que ellos puedan desmentir con su factura te cuesta credibilidad.]*

---

## 7. Siguientes pasos

1. Demo de 30 minutos con dos o tres asesores, cotizando un caso real de los suyos.
2. Revisión de la exportación de datos de su sistema actual.
3. Firma y arranque: operación plena en 2 semanas.

**Contacto:** [nombre, teléfono, correo]

---

## Tres cosas que deberías decidir antes de enviar

**1. El cronograma de 2 semanas es ajustado para una migración.** Configurar desde cero en dos semanas es razonable; migrar clientes, historial y catálogo de tarifas desde otro sistema, más capacitar a 12 asesores, es otra cosa. Si tu onboarding gratuito es de 2 semanas fijas, decide qué pasa si la migración se extiende: ¿acompañas igual, o el día 15 empieza a correr un costo? Es mejor definirlo tú ahora que improvisarlo en la semana 3 con el cliente molesto.

**2. El mínimo de 10 usuarios es una puerta que ellos pueden usar.** Si comparan contra los $120 que ya pagan, la tentación va a ser comprar 10 licencias y rotar accesos entre 15 personas. Define si permites eso o si el contrato ata licencias a usuarios nombrados.

**3. No entregues el 15% junto con la comparación de precio en la primera versión.** Ya les estás mostrando 37% de ahorro y onboarding gratis. Si además el descuento anual aparece como precio de entrada, no te queda nada para la negociación final, y en una decisión de compra de este tamaño casi siempre hay una ronda más. Una opción: presenta el precio lista de $89 con la comparación (que ya gana: $89 vs $120, con onboarding incluido) y reserva el 15% para cerrar el compromiso anual cuando pidan mejora.

---

**Para cerrar el documento me falta un dato:** ¿cuántas licencias son realmente y cuándo vence el contrato con su proveedor actual? Lo segundo es clave: si les quedan seis meses de contrato, la propuesta debe incluir cómo manejar el traslape (arranque diferido, o los primeros meses con descuento adicional para que no paguen dos sistemas). Si no lo abordas tú, esa es la objeción que va a congelar la decisión.