# Tencent Hy4 preview — agent_long_horizon/clarification_quality

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.03 | quality: 10.0
- latency_total: 433.135s | tokens_per_second: 71.0
- input_tokens: 6150 | output_tokens: 28778

## Conversación completa (4 turnos)

### Turno 1 — usuario

Necesito que me hagas la propuesta.

### Turno 1 — modelo

¡Claro que sí! Me encantaría ayudarte a redactar esa propuesta. Sin embargo, para que sea realmente efectiva, persuasiva y esté hecha a tu medida, necesito un poco más de contexto, ya que el término "propuesta" es muy amplio.

Para poder crear el mejor borrador para ti, por favor respóndeme lo siguiente:

1. **¿Qué tipo de propuesta necesitas?** (¿Es una propuesta comercial o de ventas, la presentación de un proyecto, una propuesta de inversión para buscar fondos, o una alianza/colaboración?)
2. **¿Cuál es tu oferta?** (¿Qué producto o servicio estás proponiendo? Una breve descripción basta).
3. **¿Quién es el receptor?** (¿A qué empresa, inversor o persona va dirigida? ¿Conoces sus necesidades actuales o el problema que intentan resolver?)
4. **¿Cuál es el objetivo principal?** (¿Qué quieres que pase exactamente después de que lean la propuesta? Ej: agendar una reunión, firmar un contrato, recibir una cantidad específica de dinero).

En cuanto me des estos detalles, ¡me pongo manos a la obra con la estructura y el contenido!

### Turno 2 — usuario

Es una propuesta comercial. Para un cliente nuevo. Yo vendo software.

### Turno 2 — modelo

Perfecto. Ya tenemos el marco: **propuesta comercial para un cliente nuevo y tú vendes software**.

Antes de redactarla, necesito hacerte unas preguntas, porque la palabra “software” es demasiado amplia y esa ambigüedad cambia por completo el documento. No se vende igual un **SaaS por suscripción** que un **desarrollo a medida**, una **licencia on-premise**, una **implementación de ERP/CRM** o un **servicio de integración**.

Responde lo que puedas; con eso armo la propuesta. Si falta información, la marco como `[COMPLETAR]` o la infiero y te lo señalo explícitamente.

### Preguntas clave

1. **¿Qué software vendes exactamente y en qué modalidad?**
   - Ejemplos: SaaS por suscripción, licencia perpetua, desarrollo a medida, app, integración/API, etc.
   - Principales funcionalidades que quieres destacar.

2. **¿Qué problema o necesidad le resuelves a este cliente?**
   - El “dolor” concreto (ej.: procesos manuales lentos, errores administrativos, falta de control, necesidad de facturar electrónicamente, escalar ventas, cumplir una normativa).
   - Si ya tuviste una reunión con el cliente, ¿qué fue lo que más le importó?

3. **¿Quién es el cliente?**
   - Nombre (opcional), sector/industria y tamaño (PyME, empresa grande, startup, gobierno).
   - Esto define el tono y el nivel de detalle técnico.

4. **¿Qué incluye la oferta y cuánto cuesta?**
   - Módulos, usuarios, licencias, horas de desarrollo, implementación, capacitación, soporte, SLA.
   - Precio, moneda, forma de pago, validez de la oferta y si hay descuento o condiciones especiales.

5. **¿Cuál es el siguiente paso que quieres que dé el cliente?**
   - Firmar, agendar una demo, aprobar un piloto, pagar la primera cuota, etc. Esto será el cierre/llamado a la acción.

6. **¿Tienes elementos de prueba o diferenciales?**
   - Casos de éxito, métricas, garantías, certificaciones, testimonios o algo que te haga mejor que la competencia.

---

### Estructura que voy a usar

Cuando tenga las respuestas, la propuesta tendrá esta estructura:

1. **Resumen ejecutivo / contexto**
2. **Problema o desafío del cliente**
3. **Solución propuesta** (qué hace tu software)
4. **Alcance y entregables**
5. **Beneficios y valor / ROI**
6. **Inversión y condiciones**
7. **Por qué elegirte** (diferenciales y prueba social)
8. **Próximos pasos / llamado a la acción**

---

### Si prefieres que avance ya sin más preguntas

Responde **“avanza con supuestos”** y te entrego un borrador estructurado. En ese caso, para que no haya sorpresas, estas serían mis **suposiciones explícitas**:

- Vendes una **solución de software B2B** (no consultoría ni hardware).
- La modalidad es **SaaS o licenciamiento con pago recurrente/único**; si es desarrollo a medida, dímelo porque cambia el alcance.
- El cliente es una **PyME o empresa mediana** y ya hubo al menos una conversación previa donde detectaste la necesidad.
- El objetivo de la propuesta es que el cliente **acepte y avance al siguiente paso** (reunión de cierre, firma o piloto).
- Incluiré una sección de **inversión con valores de ejemplo** y espacios `[COMPLETAR]` para precios reales, módulos específicos y casos de éxito.

¿Me pasas las respuestas o prefieres que avance con la base y estos supuestos?

### Turno 3 — usuario

Es una agencia de viajes mediana, 30 empleados, en Lima. Mi software es un CRM con módulo de cotización rápida para vendedores de turismo. Quieren saber qué les ofrezco y precio.

### Turno 3 — modelo

Con esta información ya tengo el contexto para una propuesta comercial sólida: **agencia de viajes mediana (30 empleados) en Lima**, y tu producto es un **CRM con módulo de cotización rápida para vendedores de turismo**.

Antes de darte el documento final, hay un punto que es el corazón de la propuesta y que **no puedo inventar**: el **precio y las condiciones comerciales**. Como eso afecta materialmente tu margen y tu posicionamiento, te pido confirmar lo siguiente (son preguntas reales, no triviales):

### Preguntas clave para cerrar la propuesta
1. **¿Cuál es tu precio y modelo de cobro?**  
   ¿Cobras por usuario/mes, una tarifa plana, o anualidad? Indica moneda (**PEN** o **USD**) y si los montos son **con o sin IGV**.
2. **¿Cuántos usuarios pagarán licencia?**  
   ¿Serán los 30 empleados o solo el equipo comercial/administrativo (por ejemplo, 15–20 vendedores)? Esto cambia el precio total.
3. **¿Necesitan integraciones?**  
   ¿El CRM debe conectarse con GDS (Amadeus/Sabre), WhatsApp Business, correo, pasarelas de pago o contabilidad/SUNAT? De ser así, el alcance y el precio cambian.
4. **Implementación, capacitación y soporte:**  
   ¿Cobras un fee de setup/onboarding? ¿Incluye capacitación? ¿El soporte va incluido y por cuánto tiempo?
5. **Condiciones:**  
   ¿Validez de la oferta (ej. 15 días)? ¿Forma de pago (mensual/anticipado o anual)? ¿Hay plazo mínimo de contrato?

> Si aún **no tienes definido el precio**, dime **“sugiere precio”** y te paso una estrategia de pricing con rangos de mercado para Latinoamérica/Perú.

---

Mientras me confirmas, te dejo el **borrador de la propuesta** estructurado y listo para enviar. He dejado como `[COMPLETAR]` los datos comerciales y, al final, te detallo **mis supuestos explícitos**.

---

# Propuesta Comercial

**[Tu Logotipo]**  
**[Nombre de tu empresa]**  
Lima, **[Fecha]**

**Cliente:** **[Nombre de la Agencia de Viajes]**  
**Atención:** **[Nombre del contacto]**, **[Cargo]**  
**Asunto:** Propuesta de implementación de **[Nombre del CRM]** – CRM con módulo de cotización rápida para ventas de turismo.

---

## 1. Resumen ejecutivo
En **[Tu empresa]** ayudamos a agencias de viajes como **[Nombre cliente]** a vender más en menos tiempo. Nuestra solución es un **CRM especializado en turismo** que incluye un **módulo de cotización rápida**, diseñado para que tu equipo comercial arme y envíe propuestas de viaje profesionales en minutos, sin depender de plantillas manuales en Word o Excel.

El objetivo de esta propuesta es que **[Nombre cliente]** pueda:
- Responder a los clientes más rápido que su competencia.
- Dar seguimiento sistemático a cada cotización y oportunidad.
- Centralizar clientes, paquetes, tarifas y márgenes en un solo lugar.
- Aumentar la conversión de cotizaciones a ventas cerradas.

---

## 2. Desafío actual
En una agencia mediana, los vendedores suelen perder tiempo valioso armando cotizaciones manualmente, lo que genera:
- Demoras en responder al cliente (y pérdida de ventas frente a agencias más ágiles).
- Falta de seguimiento: no se sabe qué pasó con cada propuesta enviada.
- Errores en tarifas, disponibilidad o márgenes.
- Poca visibilidad del *pipeline* comercial para la gerencia.

---

## 3. Solución propuesta: [Nombre del CRM]
Un CRM en la nube, enfocado en turismo, con dos grandes componentes:

### A. Módulo CRM (Gestión comercial)
- Base centralizada de clientes y contactos.
- Historial de interacciones (llamadas, correos, WhatsApp, reuniones).
- *Pipeline* de ventas por etapas (prospecto → cotizado → negociación → cerrado).
- Tareas y recordatorios automáticos de seguimiento.
- Reportes de productividad por vendedor y de ventas cerradas.

### B. Módulo de cotización rápida (el diferencial)
- Catálogo de paquetes y servicios turísticos (vuelos, hoteles, tours, traslados) reutilizable.
- Generación de cotizaciones en minutos seleccionando servicios precargados.
- Cálculo automático de márgenes, impuestos y totales.
- Envío de la cotización por correo o enlace web/WhatsApp en un clic.
- Seguimiento de apertura de la cotización por parte del cliente.
- Conversión de cotización a reserva/venta sin reingresar datos.

### C. Otros beneficios
- Acceso desde web y móvil.
- Control de usuarios y permisos (vendedores, supervisores, gerencia).
- Información respaldada en la nube con altos estándares de seguridad.

---

## 4. Alcance y entregables

| Ítem | Detalle |
|---|---|
| **Licencias de uso** | Acceso para **[NÚMERO DE USUARIOS: ej. 20]** usuarios. |
| **Modalidad** | SaaS en la nube (sin instalación de servidores locales). |
| **Configuración inicial** | Creación de cuenta, alta de usuarios, carga inicial del catálogo de servicios/paquetes y plantillas de cotización. |
| **Capacitación** | **[NÚMERO]** sesiones de capacitación (remotas o presenciales en Lima) para vendedores y administradores. |
| **Soporte** | Soporte técnico por **[correo/WhatsApp/teléfono]** en horario **[COMPLETAR]**, incluido por **[COMPLETAR: ej. 12 meses]**. |
| **Integraciones** | **[COMPLETAR: “No incluidas en esta etapa” o “Integración con correo y WhatsApp incluida; GDS/Amadeus cotizado aparte”]**. |

---

## 5. Beneficios y retorno de inversión
- **Ahorro de tiempo:** Un vendedor que hoy tarda 45–60 minutos en cotizar podría hacerlo en menos de 10 minutos. Con 4 cotizaciones diarias, recuperas más de 3 horas diarias por vendedor.
- **Más cierres:** Al responder rápido y hacer seguimiento automático, reduces la fuga de clientes interesados.
- **Imagen profesional:** Cotizaciones uniformes, con tu marca y márgenes calculados correctamente.
- **Control gerencial:** Visibilidad en tiempo real de cuánto se cotiza y cuánto se vende.

---

## 6. Inversión
> **Importante:** Esta sección es la que debes completar. No inventé tus precios; están como estructura y campos por llenar. Si te sirve, más abajo te doy una **sugerencia de mercado** claramente marcada.

| Concepto | Detalle | Monto |
|---|---|---|
| **Licencias de uso (SaaS)** | [NÚMERO] usuarios × [PRECIO POR USUARIO/MES] | [MONTO MENSUAL] |
| **Implementación / Setup (único)** | Configuración, carga de catálogo y capacitación inicial | [MONTO ÚNICO] |
| **Soporte y mantenimiento** | [Incluido / Monto adicional] | [MONTO] |
| **Total mensual recurrente** | | **[MONTO MENSUAL TOTAL]** |
| **Inversión inicial (primer mes)** | Implementación + primer mes de licencias | **[MONTO TOTAL INICIAL]** |

- **Moneda:** [PEN / USD]  
- **Impuestos:** [Precios + IGV / Precios incluyen IGV]  
- **Forma de pago:** [Mensual anticipado / Anual con X% de descuento]  
- **Vigencia de la oferta:** [15] días calendario.  
- **Plazo mínimo de contrato:** [1 mes / 6 meses / 12 meses].

**Sugerencia de precio de referencia (NO es tu precio real, solo una guía de mercado):**  
Un CRM nicho para turismo en Perú/LatAm suele cobrarse entre **USD 20 y USD 40 por usuario/mes** (aprox. **S/ 75 – S/ 150 por usuario/mes**), más un fee de implementación único de entre **USD 300 y USD 1,000** (aprox. **S/ 1,200 – S/ 4,000**). Ajústalo según tus costos y el valor que entregas.

---

## 7. Condiciones comerciales
- Los pagos se realizan [mensual/anual] por adelantado.
- Licencias adicionales se cotizan al mismo valor unitario.
- La propiedad del software es de **[Tu empresa]**; el cliente adquiere una licencia de uso.
- La información cargada por el cliente es confidencial y de su propiedad.

---

## 8. ¿Por qué elegirnos?
- **Especialización en turismo:** No es un CRM genérico; el cotizador ya entiende de paquetes, tarifas y márgenes turísticos.
- **Implementación rápida:** En **[X]** días tu equipo puede estar operando.
- **Soporte local:** Atención en Lima y en tu huso horario.
- **Escalable:** Crece contigo si abres más sucursales o sumas vendedores.
- **[COMPLETAR: caso de éxito, testimonio o garantía, si lo tienes].**

---

## 9. Próximos pasos
Para avanzar necesitamos:
1. Que nos confirmes el número final de usuarios y el plan elegido.
2. Tu aprobación de esta propuesta (firma o correo de aceptación).
3. Agendar la reunión de *kickoff* para configurar el sistema y capacitar al equipo.

Quedamos atentos.  
**[Tu nombre]**  
**[Tu cargo] – [Tu empresa]**  
**[Teléfono] | [Email]**

---

## Mis supuestos explícitos (si usas el borrador tal cual)
Para no inventar datos críticos, esto es lo que **asumí** y que debes revisar:
1. Asumo que tu solución es **SaaS en la nube** (no instalación en servidores del cliente).
2. Asumo que los precios se manejarán en **soles (PEN)** y **no incluyen IGV**, salvo que me digas lo contrario.
3. Asumo que **no hay integraciones complejas** (GDS/Amadeus, contabilidad) salvo que me indiques que sí; de existir, el alcance y el precio cambian.
4. Asumo que el número de usuarios con licencia es **menor a 30** (solo equipo comercial/administrativo); si son los 30 empleados, el precio mensual sube proporcionalmente.
5. **No asumí tu precio real:** todos los montos están como `[COMPLETAR]` o como sugerencia de mercado claramente marcada.

---

Respóndeme con: **1) precio/modelo, 2) número de usuarios, 3) integraciones y 4) condiciones**, y te devuelvo la propuesta final lista para pasar a PDF y enviar. Si quieres que yo **defina el precio por ti**, dime **“sugiere precio”** y lo trabajamos.

### Turno 4 — usuario

Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% de descuento. Incluye onboarding gratis 2 semanas. Tienen un competidor actual que cobra $120/usuario sin onboarding.

### Turno 4 — modelo

Listo. Con el **Plan Profesional a USD 89/usuario/mes (mínimo 10 usuarios)**, el **contrato anual con 15% de descuento** y el **onboarding gratis de 2 semanas**, más el dato del competidor (**USD 120/usuario sin onboarding**), ya tengo todo para una propuesta persuasiva.

Como aún no me diste el **número exacto de usuarios** ni las **integraciones/condiciones fiscales**, la propuesta incluye una **tabla con los totales de 10 a 30 usuarios** y dejo esos campos marcados. Al final te detallo mis supuestos y lo único que falta para dejar el documento 100% listo para enviar.

---

# Propuesta Comercial

**[Tu Logotipo]**  
**[Nombre de tu empresa]**  
Lima, **[Fecha]**

**Cliente:** **[Nombre de la Agencia de Viajes]**  
**Atención:** **[Nombre del contacto]**, **[Cargo]**  
**Asunto:** Propuesta comercial – Plan Profesional **[Nombre del CRM]**: CRM con módulo de cotización rápida para ventas de turismo.

---

## 1. Resumen ejecutivo

En **[Tu empresa]** ayudamos a agencias de viajes medianas a vender más y más rápido. Nuestra solución es el **Plan Profesional de [Nombre del CRM]**, un CRM especializado en turismo con **módulo de cotización rápida**, diseñado para que tu equipo comercial arme y envíe propuestas profesionales en minutos.

**Condiciones destacadas de esta propuesta:**

- **Plan Profesional:** USD 89 / usuario / mes (precio de lista).  
- **Contrato anual con 15% de descuento:** se reduce a **USD 75.65 / usuario / mes** (equivalente a **USD 907.80 / usuario / año**).  
- **Mínimo 10 usuarios.**  
- **Onboarding gratuito de 2 semanas** (configuración, carga de catálogo y capacitación).  
- Frente al competidor actual, que cobra **USD 120 / usuario / mes sin onboarding**, el ahorro es directo y medible desde el primer mes.

---

## 2. Contexto y desafío

Una agencia con 30 empleados y operación comercial activa necesita velocidad. El proceso manual de cotización en Word o Excel genera demoras, errores en márgenes y pérdida de seguimiento de cada oportunidad. Nuestro objetivo es que tu equipo responda primero, cotice mejor y haga seguimiento sistemático para cerrar más ventas.

---

## 3. Solución propuesta: Plan Profesional

El **Plan Profesional** incluye:

### A. CRM para turismo
- Base centralizada de clientes y contactos.
- Historial de interacciones (llamadas, correos, WhatsApp, reuniones).
- Pipeline de ventas por etapas y tareas de seguimiento.
- Reportes de productividad por vendedor y ventas cerradas.

### B. Módulo de cotización rápida (diferencial clave)
- Catálogo reutilizable de paquetes y servicios turísticos.
- Generación de cotizaciones en minutos con servicios precargados.
- Cálculo automático de márgenes, impuestos y totales.
- Envío por correo o enlace/WhatsApp y seguimiento de apertura.
- Conversión de cotización a reserva sin reingresar datos.

### C. Onboarding incluido (2 semanas, valor USD 0)
- Configuración de cuenta y alta de usuarios.
- Carga inicial de catálogo de servicios/paquetes y plantillas de cotización.
- Capacitación práctica para vendedores y administradores.
- Acompañamiento en los primeros días de uso.

---

## 4. Alcance y entregables

| Ítem | Detalle |
|---|---|
| **Licencias** | Acceso para **[NÚMERO DE USUARIOS]** usuarios (mínimo 10). |
| **Modalidad** | SaaS en la nube (sin instalación de servidores locales). |
| **Onboarding** | 2 semanas, sin costo. |
| **Capacitación** | Incluida dentro del onboarding. |
| **Soporte** | **[COMPLETAR: canal, horario y vigencia. Ej.: correo/WhatsApp, lunes a viernes 9am–6pm, incluido durante los 12 meses]**. |
| **Integraciones** | **[COMPLETAR / Asumo que no incluye GDS, contabilidad o SUNAT; si se requieren, se cotizan aparte]**. |

---

## 5. Inversión

**Precios en dólares americanos (USD).**

| Concepto | Valor |
|---|---|
| Precio de lista mensual | USD 89.00 / usuario / mes |
| Precio con contrato anual (15% dto.) | USD 75.65 / usuario / mes |
| Equivalente anual por usuario | USD 907.80 / usuario / año |
| Onboarding (2 semanas) | USD 0.00 (gratuito) |
| Mínimo de facturación | 10 usuarios |

### Totales según número de usuarios (con contrato anual y 15% de descuento)

| Usuarios | Inversión mensual | Inversión anual | Costo anual competidor (USD 120) | Ahorro anual vs competidor |
|---|---:|---:|---:|---:|
| 10 | USD 756.50 | USD 9,078.00 | USD 14,400.00 | USD 5,322.00 |
| 15 | USD 1,134.75 | USD 13,617.00 | USD 21,600.00 | USD 7,983.00 |
| 20 | USD 1,513.00 | USD 18,156.00 | USD 28,800.00 | USD 10,644.00 |
| 25 | USD 1,891.25 | USD 22,695.00 | USD 36,000.00 | USD 13,305.00 |
| 30 | USD 2,269.50 | USD 27,234.00 | USD 43,200.00 | USD 15,966.00 |

> **Nota:** la agencia tiene 30 empleados. Lo habitual es licenciar al **equipo comercial + administración** (entre 15 y 25 usuarios) o a **toda la planilla (30)**. Selecciona el número final; el mínimo facturable es 10 usuarios.

### Condiciones comerciales
- **Moneda:** USD.  
- **Impuestos:** **[COMPLETAR / Asumo que los precios NO incluyen IGV; se emite factura electrónica con IGV (18%) adicional, salvo otro régimen]**.  
- **Contrato:** anual (12 meses) con 15% de descuento sobre la tarifa mensual.  
- **Facturación:** **[COMPLETAR / Asumo emisión y pago mensual a la tarifa descontada de USD 75.65/usuario; si exiges pago anual anticipado, indícalo]**.  
- **Vigencia de la oferta:** **[COMPLETAR: ej. 15 días]** calendario.  
- **Onboarding:** 100% gratuito por 2 semanas (el competidor no lo incluye).

---

## 6. Comparativo frente a su proveedor actual

| Concepto | **[Tu CRM] – Plan Profesional** | Competidor actual |
|---|---|---|
| Precio por usuario / mes | USD 89 (lista) / **USD 75.65** con contrato anual | USD 120 |
| Onboarding / implementación | **Gratis (2 semanas)** | No incluido |
| Especialización en turismo | CRM + cotizador diseñado para paquetes y márgenes turísticos | **[COMPLETAR si conoces al competidor]** |
| Ahorro mensual por usuario (con dto.) | **USD 44.35 menos** | - |
| Ahorro anual (ej. 20 usuarios) | **USD 10,644.00** | - |

**Lectura directa:** por cada usuario, el competidor les cuesta **USD 120/mes sin onboarding**. Nosotros, con contrato anual, les sale **USD 75.65/mes con onboarding incluido**. En 20 usuarios, el ahorro anual supera los **USD 10,000**, sin contar el valor de la implementación que el competidor no entrega.

---

## 7. Beneficios y retorno de inversión
- **Ahorro de tiempo:** cotizaciones en menos de 10 minutos vs. 45–60 minutos de proceso manual.  
- **Más cierres:** seguimiento automático y respuesta rápida al cliente.  
- **Imagen profesional:** cotizaciones uniformes y con márgenes calculados correctamente.  
- **Control gerencial:** visibilidad del pipeline y productividad por vendedor.  
- **Implementación sin fricción:** onboarding de 2 semanas sin costo.

---

## 8. Próximos pasos
1. Confirmar el **número de usuarios** a licenciar (mínimo 10).  
2. Aprobación de la propuesta y firma del **contrato anual** (aplica el 15% de descuento).  
3. Agendar el **kickoff** para iniciar el onboarding gratuito de 2 semanas.

Quedamos atentos.

**[Tu nombre]**  
**[Tu cargo] – [Tu empresa]**  
**[Teléfono] | [Email]**

---

# Mis supuestos explícitos

Para no inventar datos críticos, esto es lo que **asumí** al armar la propuesta:

1. **Moneda e impuestos:** los precios están en **USD** y asumo que **NO incluyen IGV**; se emitirá factura electrónica con el IGV peruano (18%) adicional, salvo que me indiques otro tratamiento.  
2. **Descuento anual:** asumo que el **15% se aplica sobre la tarifa mensual** al firmar contrato anual, por lo que el precio efectivo es **USD 75.65/usuario/mes** (anual: USD 907.80/usuario). Si el descuento aplica solo a pago anual anticipado, el total anual es el mismo.  
3. **Usuarios:** no me confirmaste cuántos licenciarán. Incluí la tabla de **10 a 30 usuarios** y dejé `[NÚMERO DE USUARIOS]` en el cuerpo. El ejemplo de ahorro de 20 usuarios es solo referencial.  
4. **Integraciones:** asumo que **NO se incluyen** integraciones con GDS (Amadeus/Sabre), contabilidad o SUNAT; si las requieren, van como alcance adicional cotizado aparte.  
5. **Soporte:** dejé `[COMPLETAR]` porque no indicaste canal, horario ni vigencia. Asumo que el Plan Profesional incluye soporte estándar durante el contrato, pero debes confirmarlo.  
6. **Onboarding:** asumo que las 2 semanas incluyen configuración, carga de catálogo/plantillas y capacitación, según habíamos conversado.

---

# Preguntas pendientes (materiales)

Para eliminar los corchetes y darte el PDF final, confírmame:

1. **¿Cuántos usuarios?** (10, 15, 20, 25 o 30).  
2. **¿Requieren integraciones?** (WhatsApp, GDS/Amadeus, contabilidad, SUNAT, etc.).  
3. **¿Los USD 89 son +IGV o inc. IGV?**  
4. **¿La facturación del contrato anual es mensual a tarifa descontada o exigen pago anual anticipado?** ¿Qué vigencia tendrá la oferta?

Con esas cuatro respuestas te devuelvo la propuesta final sin corchetes y lista para enviar.


## Respuesta completa

Listo. Con el **Plan Profesional a USD 89/usuario/mes (mínimo 10 usuarios)**, el **contrato anual con 15% de descuento** y el **onboarding gratis de 2 semanas**, más el dato del competidor (**USD 120/usuario sin onboarding**), ya tengo todo para una propuesta persuasiva.

Como aún no me diste el **número exacto de usuarios** ni las **integraciones/condiciones fiscales**, la propuesta incluye una **tabla con los totales de 10 a 30 usuarios** y dejo esos campos marcados. Al final te detallo mis supuestos y lo único que falta para dejar el documento 100% listo para enviar.

---

# Propuesta Comercial

**[Tu Logotipo]**  
**[Nombre de tu empresa]**  
Lima, **[Fecha]**

**Cliente:** **[Nombre de la Agencia de Viajes]**  
**Atención:** **[Nombre del contacto]**, **[Cargo]**  
**Asunto:** Propuesta comercial – Plan Profesional **[Nombre del CRM]**: CRM con módulo de cotización rápida para ventas de turismo.

---

## 1. Resumen ejecutivo

En **[Tu empresa]** ayudamos a agencias de viajes medianas a vender más y más rápido. Nuestra solución es el **Plan Profesional de [Nombre del CRM]**, un CRM especializado en turismo con **módulo de cotización rápida**, diseñado para que tu equipo comercial arme y envíe propuestas profesionales en minutos.

**Condiciones destacadas de esta propuesta:**

- **Plan Profesional:** USD 89 / usuario / mes (precio de lista).  
- **Contrato anual con 15% de descuento:** se reduce a **USD 75.65 / usuario / mes** (equivalente a **USD 907.80 / usuario / año**).  
- **Mínimo 10 usuarios.**  
- **Onboarding gratuito de 2 semanas** (configuración, carga de catálogo y capacitación).  
- Frente al competidor actual, que cobra **USD 120 / usuario / mes sin onboarding**, el ahorro es directo y medible desde el primer mes.

---

## 2. Contexto y desafío

Una agencia con 30 empleados y operación comercial activa necesita velocidad. El proceso manual de cotización en Word o Excel genera demoras, errores en márgenes y pérdida de seguimiento de cada oportunidad. Nuestro objetivo es que tu equipo responda primero, cotice mejor y haga seguimiento sistemático para cerrar más ventas.

---

## 3. Solución propuesta: Plan Profesional

El **Plan Profesional** incluye:

### A. CRM para turismo
- Base centralizada de clientes y contactos.
- Historial de interacciones (llamadas, correos, WhatsApp, reuniones).
- Pipeline de ventas por etapas y tareas de seguimiento.
- Reportes de productividad por vendedor y ventas cerradas.

### B. Módulo de cotización rápida (diferencial clave)
- Catálogo reutilizable de paquetes y servicios turísticos.
- Generación de cotizaciones en minutos con servicios precargados.
- Cálculo automático de márgenes, impuestos y totales.
- Envío por correo o enlace/WhatsApp y seguimiento de apertura.
- Conversión de cotización a reserva sin reingresar datos.

### C. Onboarding incluido (2 semanas, valor USD 0)
- Configuración de cuenta y alta de usuarios.
- Carga inicial de catálogo de servicios/paquetes y plantillas de cotización.
- Capacitación práctica para vendedores y administradores.
- Acompañamiento en los primeros días de uso.

---

## 4. Alcance y entregables

| Ítem | Detalle |
|---|---|
| **Licencias** | Acceso para **[NÚMERO DE USUARIOS]** usuarios (mínimo 10). |
| **Modalidad** | SaaS en la nube (sin instalación de servidores locales). |
| **Onboarding** | 2 semanas, sin costo. |
| **Capacitación** | Incluida dentro del onboarding. |
| **Soporte** | **[COMPLETAR: canal, horario y vigencia. Ej.: correo/WhatsApp, lunes a viernes 9am–6pm, incluido durante los 12 meses]**. |
| **Integraciones** | **[COMPLETAR / Asumo que no incluye GDS, contabilidad o SUNAT; si se requieren, se cotizan aparte]**. |

---

## 5. Inversión

**Precios en dólares americanos (USD).**

| Concepto | Valor |
|---|---|
| Precio de lista mensual | USD 89.00 / usuario / mes |
| Precio con contrato anual (15% dto.) | USD 75.65 / usuario / mes |
| Equivalente anual por usuario | USD 907.80 / usuario / año |
| Onboarding (2 semanas) | USD 0.00 (gratuito) |
| Mínimo de facturación | 10 usuarios |

### Totales según número de usuarios (con contrato anual y 15% de descuento)

| Usuarios | Inversión mensual | Inversión anual | Costo anual competidor (USD 120) | Ahorro anual vs competidor |
|---|---:|---:|---:|---:|
| 10 | USD 756.50 | USD 9,078.00 | USD 14,400.00 | USD 5,322.00 |
| 15 | USD 1,134.75 | USD 13,617.00 | USD 21,600.00 | USD 7,983.00 |
| 20 | USD 1,513.00 | USD 18,156.00 | USD 28,800.00 | USD 10,644.00 |
| 25 | USD 1,891.25 | USD 22,695.00 | USD 36,000.00 | USD 13,305.00 |
| 30 | USD 2,269.50 | USD 27,234.00 | USD 43,200.00 | USD 15,966.00 |

> **Nota:** la agencia tiene 30 empleados. Lo habitual es licenciar al **equipo comercial + administración** (entre 15 y 25 usuarios) o a **toda la planilla (30)**. Selecciona el número final; el mínimo facturable es 10 usuarios.

### Condiciones comerciales
- **Moneda:** USD.  
- **Impuestos:** **[COMPLETAR / Asumo que los precios NO incluyen IGV; se emite factura electrónica con IGV (18%) adicional, salvo otro régimen]**.  
- **Contrato:** anual (12 meses) con 15% de descuento sobre la tarifa mensual.  
- **Facturación:** **[COMPLETAR / Asumo emisión y pago mensual a la tarifa descontada de USD 75.65/usuario; si exiges pago anual anticipado, indícalo]**.  
- **Vigencia de la oferta:** **[COMPLETAR: ej. 15 días]** calendario.  
- **Onboarding:** 100% gratuito por 2 semanas (el competidor no lo incluye).

---

## 6. Comparativo frente a su proveedor actual

| Concepto | **[Tu CRM] – Plan Profesional** | Competidor actual |
|---|---|---|
| Precio por usuario / mes | USD 89 (lista) / **USD 75.65** con contrato anual | USD 120 |
| Onboarding / implementación | **Gratis (2 semanas)** | No incluido |
| Especialización en turismo | CRM + cotizador diseñado para paquetes y márgenes turísticos | **[COMPLETAR si conoces al competidor]** |
| Ahorro mensual por usuario (con dto.) | **USD 44.35 menos** | - |
| Ahorro anual (ej. 20 usuarios) | **USD 10,644.00** | - |

**Lectura directa:** por cada usuario, el competidor les cuesta **USD 120/mes sin onboarding**. Nosotros, con contrato anual, les sale **USD 75.65/mes con onboarding incluido**. En 20 usuarios, el ahorro anual supera los **USD 10,000**, sin contar el valor de la implementación que el competidor no entrega.

---

## 7. Beneficios y retorno de inversión
- **Ahorro de tiempo:** cotizaciones en menos de 10 minutos vs. 45–60 minutos de proceso manual.  
- **Más cierres:** seguimiento automático y respuesta rápida al cliente.  
- **Imagen profesional:** cotizaciones uniformes y con márgenes calculados correctamente.  
- **Control gerencial:** visibilidad del pipeline y productividad por vendedor.  
- **Implementación sin fricción:** onboarding de 2 semanas sin costo.

---

## 8. Próximos pasos
1. Confirmar el **número de usuarios** a licenciar (mínimo 10).  
2. Aprobación de la propuesta y firma del **contrato anual** (aplica el 15% de descuento).  
3. Agendar el **kickoff** para iniciar el onboarding gratuito de 2 semanas.

Quedamos atentos.

**[Tu nombre]**  
**[Tu cargo] – [Tu empresa]**  
**[Teléfono] | [Email]**

---

# Mis supuestos explícitos

Para no inventar datos críticos, esto es lo que **asumí** al armar la propuesta:

1. **Moneda e impuestos:** los precios están en **USD** y asumo que **NO incluyen IGV**; se emitirá factura electrónica con el IGV peruano (18%) adicional, salvo que me indiques otro tratamiento.  
2. **Descuento anual:** asumo que el **15% se aplica sobre la tarifa mensual** al firmar contrato anual, por lo que el precio efectivo es **USD 75.65/usuario/mes** (anual: USD 907.80/usuario). Si el descuento aplica solo a pago anual anticipado, el total anual es el mismo.  
3. **Usuarios:** no me confirmaste cuántos licenciarán. Incluí la tabla de **10 a 30 usuarios** y dejé `[NÚMERO DE USUARIOS]` en el cuerpo. El ejemplo de ahorro de 20 usuarios es solo referencial.  
4. **Integraciones:** asumo que **NO se incluyen** integraciones con GDS (Amadeus/Sabre), contabilidad o SUNAT; si las requieren, van como alcance adicional cotizado aparte.  
5. **Soporte:** dejé `[COMPLETAR]` porque no indicaste canal, horario ni vigencia. Asumo que el Plan Profesional incluye soporte estándar durante el contrato, pero debes confirmarlo.  
6. **Onboarding:** asumo que las 2 semanas incluyen configuración, carga de catálogo/plantillas y capacitación, según habíamos conversado.

---

# Preguntas pendientes (materiales)

Para eliminar los corchetes y darte el PDF final, confírmame:

1. **¿Cuántos usuarios?** (10, 15, 20, 25 o 30).  
2. **¿Requieren integraciones?** (WhatsApp, GDS/Amadeus, contabilidad, SUNAT, etc.).  
3. **¿Los USD 89 son +IGV o inc. IGV?**  
4. **¿La facturación del contrato anual es mensual a tarifa descontada o exigen pago anual anticipado?** ¿Qué vigencia tendrá la oferta?

Con esas cuatro respuestas te devuelvo la propuesta final sin corchetes y lista para enviar.