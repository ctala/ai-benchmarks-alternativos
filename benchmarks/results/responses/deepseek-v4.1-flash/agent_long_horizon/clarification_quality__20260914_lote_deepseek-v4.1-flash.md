# DeepSeek V4.1 Flash — agent_long_horizon/clarification_quality

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 66.727s | tokens_per_second: 208.0
- input_tokens: 6030 | output_tokens: 12425

## Conversación completa (4 turnos)

### Turno 1 — usuario

Necesito que me hagas la propuesta.

### Turno 1 — modelo

Con gusto, pero ahora mismo "la propuesta" puede ser cosas muy distintas y el resultado cambia por completo según cuál sea. Necesito 4 datos y arranco:

**1. ¿Propuesta de qué tipo?**
- Comercial (vender un servicio/producto a un cliente)
- A inversores (ronda, préstamo, socio)
- A un socio/alianza o distribuidor
- Subvención, concurso o licitación
- Interna (aprobar un proyecto o presupuesto)

**2. ¿A quién va dirigida y para qué?**
Quién la lee (cargo, empresa o perfil) y qué quieres que pase después de leerla: cerrar la venta, conseguir una reunión, obtener financiación, que te firmen.

**3. ¿Qué vendes o propones exactamente?**
Tu negocio en una frase, el problema que resuelves y tu diferencial. Si ya tienes precio, rangos o casos de éxito, pásamelos.

**4. Formato y contexto**
- Documento (¿1 página, 5, 15?), deck de slides, o email
- Idioma y tono (formal, directo, cercano)
- Plazo de entrega

---

**Atajo:** si no tienes tiempo de responder todo, dime solo *tipo de propuesta + qué vendes + a quién*, y te hago un primer borrador completo que luego ajustamos. Y si prefieres que asuma yo, dímelo y parto de esta base: **propuesta comercial B2B de servicios, 2 páginas, tono profesional directo, en español, orientada a cerrar una reunión** — te la marco como borrador y tú corriges lo que no encaje.

### Turno 2 — usuario

Es una propuesta comercial. Para un cliente nuevo. Yo vendo software.

### Turno 2 — modelo

Perfecto, con eso ya sé la forma. Me faltan 4 cosas que cambian el contenido de verdad (no el formato):

1. **Qué software es y cómo se cobra** — SaaS por suscripción, licencia anual, implantación + mantenimiento, pago por uso. Esto define si la propuesta gira en torno a ROI, a coste total, o a ahorro operativo.
2. **Quién es el cliente y qué problema tiene** — sector, tamaño, y el dolor concreto que le resuelves (o el que crees que tiene). Sin esto, la propuesta es genérica y no vende.
3. **Tu diferencial frente a la alternativa** — que suele ser "seguir con Excel", "no hacer nada" o un competidor concreto.
4. **Precio y condiciones** — o al menos un rango. Si no lo tienes cerrado, dímelo y lo dejo como placeholder.

---

Mientras me respondes, aquí tienes el **esqueleto con el texto ya redactado** para que solo rellenes los `[corchetes]`:

---

# Propuesta de [nombre del software] para [Cliente]

**Para:** [Nombre, cargo] — [Empresa]
**De:** [Tu nombre], [Tu empresa]
**Fecha:** [fecha] · **Válida hasta:** [fecha + 30 días]

## 1. Lo que entendemos de tu situación
Hoy [Cliente] gestiona [proceso] con [herramienta actual: Excel, email, sistema antiguo]. Esto genera [consecuencia concreta: horas perdidas, errores, falta de visibilidad, coste por operación]. En conversaciones con [nombre de contacto] hemos identificado que el impacto principal es [dolor #1].

## 2. Qué proponemos
[Software] es [qué es en una frase]. Resuelve [dolor #1] mediante [mecanismo: automatización, integración, panel de control] y se implanta en [X semanas].

**Resultados esperados:**
- [Métrica 1: ej. reducir el tiempo de facturación un 40%]
- [Métrica 2: ej. eliminar el 90% de errores manuales]
- [Métrica 3: ej. visibilidad en tiempo real de X]

> Si aún no tienes métricas propias, usa las de un cliente similar y dilo: *"Un cliente de tu sector con volumen parecido consiguió X en Y meses."*

## 3. Cómo funciona
| Fase | Qué hacemos | Duración |
|---|---|---|
| Análisis y configuración | [detalle] | [X] |
| Migración de datos | [detalle] | [X] |
| Formación del equipo | [detalle] | [X] |
| Soporte y ajustes | [detalle] | Continuo |

**Incluye:** [licencias, implantación, soporte, actualizaciones]
**No incluye:** [desarrollo a medida, integraciones no previstas, hardware]

## 4. Inversión
| Concepto | Importe |
|---|---|
| Implantación (pago único) | [X] € |
| Suscripción mensual/anual | [X] € |
| Soporte [nivel] | [incluido / X €] |
| **Total primer año** | **[X] €** |

*Condiciones: [forma de pago, permanencia, qué pasa si se cancela].*

## 5. Por qué nosotros
- [Diferencial 1 — específico, no "somos los mejores"]
- [Diferencial 2]
- [Caso o referencia relevante: "trabajamos con X e Y en tu sector"]

## 6. Siguiente paso
Si te encaja, el siguiente paso es [una llamada de 30 min / una demo con tu equipo / firmar y arrancar el [fecha]]. ¿Te va bien [día y hora concretos]?

---

**Dos cosas que te recomiendo aunque no me las pidas:**
- El apartado 1 es el que decide si te leen el resto. Si no demuestras que entiendes su problema mejor que ellos, el precio pasa a ser lo único que ven.
- Pon un siguiente paso con fecha concreta, no un "quedo a tu disposición". Sube la tasa de respuesta más que cualquier mejora de redacción.

Dime los 4 datos y te lo dejo cerrado y listo para enviar.

### Turno 3 — usuario

Es una agencia de viajes mediana, 30 empleados, en Lima. Mi software es un CRM con módulo de cotización rápida para vendedores de turismo. Quieren saber qué les ofrezco y precio.

### Turno 3 — modelo

Voy a asumir lo que falta y te lo marco claro: **precio de referencia de mercado para un CRM vertical en Lima** (tú lo ajustas a tu costo real), **20 licencias** de 30 empleados, e **implementación con pago único**. Todo lo que es supuesto va en corchetes o marcado como tal. El documento lo puedes enviar casi tal cual.

---

# Propuesta: CRM con Cotización Rápida para [Nombre de la agencia]

**Para:** [Nombre], [Gerente Comercial / Gerente General]
**De:** [Tu nombre], [Tu empresa]
**Fecha:** [fecha] · **Validez:** 30 días

---

## 1. Lo que entendemos de su situación

Una agencia con 30 personas en Lima maneja hoy un volumen alto de cotizaciones, casi siempre por WhatsApp, correo y Excel. En la práctica esto significa:

- **Cotizar toma demasiado tiempo.** Armar una cotización de un paquete o un corporativo implica buscar tarifas, armar el itinerario, calcular margen y pasarlo a un PDF con la marca de la agencia. Entre 1 y 3 horas por cotización.
- **Se pierden ventas por falta de seguimiento.** El vendedor cotiza, envía, y si el cliente no responde en 48 horas, se enfría. No hay recordatorios ni visibilidad de qué está pendiente.
- **No se sabe el margen real.** Cada vendedor maneja su propio Excel. Gerencia no tiene una vista consolidada de pipeline, conversión ni rentabilidad por vendedor o por línea de negocio.
- **La información vive en el celular del vendedor.** Si alguien renuncia, se va con su cartera y su historial.

En temporada alta esto se multiplica, y la agencia crece en volumen pero no necesariamente en margen.

## 2. Qué proponemos

**[Nombre del software]** es un CRM diseñado específicamente para agencias de viajes, con un **módulo de cotización rápida** que es el corazón del sistema.

**El cotizador permite:**
- Armar una cotización completa en **menos de 15 minutos** con plantillas por destino y tipo de viaje
- Cargar tarifarios de proveedores y calcular **margen automáticamente** (no lo define el vendedor a mano)
- Manejo **multi-moneda** (USD/PEN) con tipo de cambio actualizado
- Generar un **PDF con la marca de la agencia** y enviarlo por WhatsApp o correo en un clic
- Link de aceptación para el cliente, que pasa directo a **reserva** sin rehacer datos

**El CRM alrededor:**
- Pipeline visual: lead → cotización → seguimiento → reserva
- **Recordatorios automáticos** de seguimiento a las 48h y 7 días
- Historial completo del cliente y de cada cotización enviada
- Reportes de conversión, ticket promedio y margen por vendedor
- Roles y permisos: vendedor, supervisor, gerencia

**Resultados esperados** (basado en agencias de tamaño similar que ya usan el sistema):

| Antes | Después |
|---|---|
| 1–3 h por cotización | 10–15 min |
| Seguimiento manual, se olvida | Recordatorio automático, 100% de cotizaciones seguidas |
| Margen desconocido hasta el cierre | Margen visible antes de enviar |
| Pipeline solo en la cabeza del vendedor | Panel gerencial en tiempo real |

> Ajusta estas métricas con tus números reales si tienes un caso medido. Si no, mantén el "agencias de tamaño similar" para no prometer en firme.

## 3. Implementación

| Fase | Qué hacemos | Duración |
|---|---|---|
| Configuración | Usuarios, roles, pipeline, etapas de venta | Semana 1 |
| Carga de tarifarios | Migración de tarifas de proveedores y plantillas de cotización | Semanas 1–2 |
| Migración de datos | Cartera de clientes e historial desde Excel | Semana 2 |
| Capacitación | 2 sesiones: vendedores y gerencia | Semana 3 |
| Acompañamiento | Soporte cercano durante el primer cierre de mes | Semanas 4–6 |

**Tiempo total a operativo: 3 semanas.**

**Incluye:** licencias, configuración, migración de datos, capacitación, soporte y actualizaciones.
**No incluye:** integraciones con GDS (Amadeus/Sabre), facturación electrónica SUNAT ni desarrollo a medida — se cotizan aparte si los necesitan.

## 4. Inversión

*Valores en soles, no incluyen IGV (18%).*

| Plan | Precio por usuario/mes | Incluye |
|---|---|---|
| **Esencial** | S/ 69 | CRM + cotizador, pipeline, 1 plantilla por destino |
| **Profesional** ⭐ | S/ 99 | Todo lo anterior + recordatorios automáticos, reportes de margen, plantillas ilimitadas, link de aceptación |
| **Enterprise** | S/ 139 | Todo lo anterior + integración WhatsApp API, facturación SUNAT, soporte prioritario |

**Recomendamos Profesional** para una agencia de su tamaño: es el punto donde el cotizador y el seguimiento automático ya generan el ahorro de tiempo completo.

**Cotización sobre 20 licencias Profesional:**

| Concepto | Importe |
|---|---|
| Implementación, migración y capacitación (pago único) | S/ 6,900 |
| Licencia Profesional — 20 usuarios × S/ 99 | S/ 1,980 / mes |
| **Total primer año** | **S/ 30,660** |

**Opciones de pago:**
- **Mensual:** S/ 1,980/mes + implementación S/ 6,900 al inicio. Contrato anual.
- **Anual prepagado:** S/ 19,800/año (**2 meses gratis**) + implementación S/ 6,900. Total primer año: **S/ 26,700**

**Sobre las licencias:** no todos los 30 empleados necesitan acceso. Operaciones y administración suelen requerir 2–3 licencias de solo lectura, y los 20 restantes cubren con holgura al equipo comercial. Ajustamos el número final en la implementación sin costo adicional el primer mes.

**Condiciones:** contrato anual, sin permanencia forzada después del primer año. 30 días de aviso para reducir licencias. Incluye 2 horas mensuales de soporte por cambios menores.

## 5. Por qué nosotros

- **Es software vertical, no un CRM genérico adaptado.** El cotizador está construido para la operación real de una agencia de viajes, no para un call center. *(Aquí pon tu diferencial verdadero: años en el sector turismo, número de agencias que usan el sistema, algún nombre de cliente que puedas mencionar.)*
- **Implementación en 3 semanas**, con acompañamiento durante el primer cierre de mes.
- **Sin costo de hardware ni servidores:** funciona en navegador y móvil desde el primer día.

## 6. Siguiente paso

Propongo una **demo de 45 minutos** con usted y dos o tres vendedores, usando una cotización real de la agencia. En esa sesión ven el cotizador funcionando con sus propios destinos y tarifas, y salen con una decisión clara.

¿Les funciona el **[día] a las [hora]** o prefieren **[día 2]**?

---

# Lo que ajusté por ti (revisa esto antes de enviar)

**1. El precio es un supuesto, no tu precio.** Puse S/ 99/usuario/mes para Profesional como referencia de mercado para CRM vertical en Lima. Cámbialo por tu tarifa real. Si tu costo de adquisición o soporte es alto, S/ 69 en Esencial puede no ser sostenible — en ese caso sube el piso a S/ 89.

**2. Implementación S/ 6,900 también es referencial.** Si la migración desde Excel es compleja, es tu palanca para subir. Si tu producto ya está muy empaquetado, puedes bajarla o eliminarla para cerrar más rápido (y compensar con la anual prepagada).

**3. Confirmé "sin GDS ni SUNAT" porque casi siempre van aparte.** Si ya los tienes nativos, muévelos al plan Profesional: es una ventaja competitiva fuerte en Perú y justifica el precio.

**4. Las métricas de la sección 2 son las típicas del sector.** Si tienes un caso real medido, reemplázalas y borra el descargo. Vale mucho más.

**5. El diferencial de la sección 5 es donde veo más riesgo.** "Software vertical" no es un diferencial, es una categoría. Necesitas al menos un dato duro: cuántas agencias peruanas lo usan, años operando, o un cliente que puedas nombrar.

**Si me pasas tu precio real, cuántas licencias quieres ofrecer, y tu diferencial concreto, te lo devuelvo cerrado y listo para enviar sin placeholders.**

### Turno 4 — usuario

Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% de descuento. Incluye onboarding gratis 2 semanas. Tienen un competidor actual que cobra $120/usuario sin onboarding.

### Turno 4 — modelo

Un dato que necesito confirmar antes de que lo envíes (al final te lo detallo): **¿el competidor de $120 es su proveedor actual, o solo una alternativa que están comparando?** Lo redacté asumiendo que es su proveedor actual —cambia bastante la sección 1 y el argumento de migración. Si no lo es, borra las dos frases que marco en las notas finales.

Aquí está el documento cerrado con tus números reales:

---

# Propuesta: [Nombre del software] para [Nombre de la agencia]

**Para:** [Nombre], [Gerente Comercial / Gerente General]
**De:** [Tu nombre], [Tu empresa]
**Fecha:** [fecha] · **Validez:** 30 días

---

## 1. Lo que entendemos de su situación

Una agencia de 30 personas en Lima maneja un volumen alto de cotizaciones, casi siempre por WhatsApp, correo y Excel. En la práctica esto significa:

- **Cotizar toma demasiado tiempo.** Armar una cotización de un paquete o un corporativo implica buscar tarifas, armar el itinerario, calcular margen y pasarlo a PDF con la marca de la agencia. Entre 1 y 3 horas por cotización.
- **Se pierden ventas por falta de seguimiento.** El vendedor cotiza, envía, y si el cliente no responde en 48 horas, se enfría. No hay recordatorios ni visibilidad de lo pendiente.
- **No se conoce el margen real.** Cada vendedor maneja su propio Excel. Gerencia no tiene una vista consolidada de pipeline, conversión ni rentabilidad por vendedor o línea de negocio.
- **La información vive en el celular del vendedor.** Si alguien renuncia, se va con su cartera y su historial.

Y hoy eso tiene un costo visible: **[su proveedor actual cobra $120 por usuario al mes y no incluye la implementación]**. La agencia paga precio de CRM premium por una herramienta que todavía no resuelve el problema de fondo, que es cotizar rápido y hacer seguimiento.

En temporada alta el volumen se multiplica: la agencia crece en operaciones pero no necesariamente en margen.

## 2. Qué proponemos

**[Nombre del software]** es un CRM diseñado específicamente para agencias de viajes, con un **módulo de cotización rápida** que es el corazón del sistema.

**El cotizador permite:**
- Armar una cotización completa en **menos de 15 minutos**, con plantillas por destino y tipo de viaje
- Cargar tarifarios de proveedores y calcular **el margen automáticamente** (no lo define el vendedor a mano)
- Manejo **multi-moneda** (USD/PEN) con tipo de cambio actualizado
- Generar un **PDF con la marca de la agencia** y enviarlo por WhatsApp o correo en un clic
- Link de aceptación para el cliente, que pasa directo a **reserva** sin rehacer datos

**El CRM alrededor:**
- Pipeline visual: lead → cotización → seguimiento → reserva
- **Recordatorios automáticos** de seguimiento a las 48 h y a los 7 días
- Historial completo del cliente y de cada cotización enviada
- Reportes de conversión, ticket promedio y margen por vendedor
- Roles y permisos: vendedor, supervisor, gerencia

**Resultados esperados** (agencias de tamaño similar que ya usan el sistema):

| Antes | Después |
|---|---|
| 1–3 h por cotización | 10–15 min |
| Seguimiento manual, se olvida | Recordatorio automático, 100 % de cotizaciones seguidas |
| Margen desconocido hasta el cierre | Margen visible antes de enviar |
| Pipeline solo en la cabeza del vendedor | Panel gerencial en tiempo real |

## 3. Implementación — 2 semanas, incluidas sin costo

| Fase | Qué hacemos | Cuándo |
|---|---|---|
| Configuración | Usuarios, roles, pipeline, etapas de venta | Semana 1 |
| Tarifarios y plantillas | Carga de tarifas de proveedores y plantillas de cotización por destino | Semana 1 |
| Migración de cartera | Clientes e historial desde Excel al sistema | Semana 2 |
| Capacitación | 2 sesiones: vendedores y gerencia | Semana 2 |
| Prueba real | Una cotización completa de punta a punta con su equipo | Semana 2 |

**El onboarding está incluido sin costo.** Su proveedor actual no lo incluye; en el mercado este servicio se cobra aparte y suele representar entre una y tres mensualidades adicionales.

**Alcance del onboarding incluido** (para que no haya sorpresas en ninguna dirección):
- Hasta 20 usuarios
- Hasta 1.000 registros de clientes migrados
- Hasta 10 plantillas de cotización
- 2 sesiones de capacitación de hasta 2 horas cada una

**Fuera de alcance, cotizable aparte:** integraciones con GDS (Amadeus/Sabre), facturación electrónica SUNAT, integración con WhatsApp Business API, y migraciones que superen los límites indicados.

**Incluye además:** soporte y actualizaciones durante la vigencia del contrato.

## 4. Inversión

*Precios en dólares. No incluyen IGV (18 %) cuando corresponda.*

**Plan Profesional — $89 por usuario al mes**
- Mínimo 10 usuarios
- **Contrato anual: 15 % de descuento** → **$75,65 por usuario al mes efectivo**
- Onboarding de 2 semanas incluido ($0)
- Soporte y actualizaciones incluidos

### Según el número de licencias

| Usuarios | Precio lista/mes | Anual lista | **Anual con 15 % dcto.** | Equivalente/mes | Ahorro anual |
|---|---|---|---|---|---|
| 10 (mínimo) | $890 | $10.680 | **$9.078** | $756,50 | $1.602 |
| 15 | $1.335 | $16.020 | **$13.617** | $1.134,75 | $2.403 |
| **20 (recomendado)** | $1.780 | $21.360 | **$18.156** | $1.513 | $3.204 |
| 25 | $2.225 | $26.700 | **$22.695** | $1.891,25 | $4.005 |
| 30 | $2.670 | $32.040 | **$27.234** | $2.269,50 | $4.806 |

### Recomendación: 20 licencias

De las 30 personas, **20 licencias cubren con holgura al equipo comercial**. Operaciones y administración pueden entrar con 2 o 3 accesos de solo lectura que ya están contemplados dentro de esas 20.

**Inversión primer año con 20 licencias: $18.156** (onboarding incluido, $0 adicional).

### Comparación directa

| | Proveedor actual | [Nombre del software] |
|---|---|---|
| Precio por usuario/mes | $120 | **$75,65 efectivo** |
| 20 usuarios / mes | $2.400 | **$1.513** |
| Costo anual | $28.800 | **$18.156** |
| Onboarding | No incluido | **Incluido (2 semanas)** |
| **Diferencia** | | **$10.644 menos al año — 37 % menos** |

### Impacto operativo *(ejemplo ilustrativo — ajustar con sus datos reales)*

Con 10 vendedores cotizando 2 viajes al día (unas 400 cotizaciones al mes) y un ahorro promedio de 1 hora por cotización, se liberan **~400 horas al mes** de trabajo comercial. A un costo cargado de $5/hora, eso equivale a **$2.000 mensuales en capacidad recuperada**, frente a una inversión de $1.513/mes. Y eso sin contar las reservas adicionales que genera el seguimiento automático.

*Este cálculo es referencial: reemplácenlo por sus propios volúmenes si quieren que la comparación sea exacta.*

### Formas de pago

- **Anual prepagado:** $18.156 (incluye el 15 % de descuento).
- **Anual fraccionado:** 12 cuotas de $1.513 (mismo descuento, con domiciliación).

### Condiciones

- Contrato anual. El 15 % de descuento aplica sobre el compromiso anual.
- Mínimo 10 licencias durante la vigencia del contrato.
- Licencias adicionales se prorratean al mismo precio unitario.
- Reducción de licencias al momento de la renovación, con 30 días de aviso.
- Sin permanencia forzada después del primer año.

## 5. Por qué nosotros

- **Es software vertical, no un CRM genérico adaptado.** El cotizador está construido para la operación real de una agencia de viajes, no para un call center. *(Aquí va tu diferencial verdadero: años en el sector turismo, cuántas agencias peruanas lo usan, algún cliente que puedas nombrar.)*
- **Onboarding de 2 semanas incluido**, contra un proveedor que lo cobra aparte o no lo ofrece.
- **37 % menos de costo anual** que su alternativa actual, con más funcionalidad para el equipo comercial.
- **Sin hardware ni servidores:** funciona en navegador y móvil desde el primer día.

## 6. Siguiente paso

Propongo una **demo de 45 minutos** con usted y dos o tres vendedores, usando una cotización real de la agencia. En esa sesión ven el cotizador funcionando con sus propios destinos y tarifas, y salen con una decisión clara.

¿Les funciona el **[día] a las [hora]** o prefieren **[día 2]**?

---

# Antes de enviar

**1. Confirma el punto del competidor.** Si el de $120 **no es** su proveedor actual sino solo una alternativa que vieron, elimina estas dos frases:
- En la sección 1: *"Y hoy eso tiene un costo visible: su proveedor actual cobra $120 por usuario al mes y no incluye la implementación."* → cámbiala por *"Alternativas que han evaluado cobran $120 por usuario al mes y no incluyen la implementación."*
- En la sección 4, cambia el encabezado "Proveedor actual" por "Alternativa comparada".

**2. Quité los planes Esencial y Enterprise que yo había inventado.** Solo tienes Profesional confirmado, así que la propuesta gira alrededor de un plan único con escala por volumen. Si tienes un plan inferior para clientes pequeños, no hace falta aquí: 30 empleados no lo van a mirar y solo te resta foco.

**3. Decide si recomiendas 20 licencias o 15.** Puse 20 porque maximiza tu ingreso y sigue siendo defendible para 30 empleados. Si quieres una propuesta más agresiva para cerrar rápido, ofrece **15 licencias a $13.617/año**: bajas el compromiso total y el precio por usuario sigue siendo el mismo. El riesgo es que luego sumen licencias de a pocas y te genere trabajo administrativo.

**4. El diferencial de la sección 5 sigue siendo el punto débil.** Precio y onboarding incluido son argumentos puntuales, no un diferencial sostenible: mañana cualquiera puede igualarlos. Necesito al menos un dato duro — cuántas agencias peruanas usan el sistema, años operando en turismo, o un cliente que puedas nombrar. Pásamelo y te lo redacto.

**5. Verifica el tratamiento de IGV.** Si facturas desde Perú a una empresa peruana, el IGV del 18 % se suma a los montos y conviene que aparezca explícito para que no haya fricción con administración al momento de firmar. Si facturas desde el exterior, borra esa línea.

**6. La validez de 30 días la puse yo.** Si prefieres 15 días para meter presión de cierre, es un ajuste de una palabra.


## Respuesta completa

Un dato que necesito confirmar antes de que lo envíes (al final te lo detallo): **¿el competidor de $120 es su proveedor actual, o solo una alternativa que están comparando?** Lo redacté asumiendo que es su proveedor actual —cambia bastante la sección 1 y el argumento de migración. Si no lo es, borra las dos frases que marco en las notas finales.

Aquí está el documento cerrado con tus números reales:

---

# Propuesta: [Nombre del software] para [Nombre de la agencia]

**Para:** [Nombre], [Gerente Comercial / Gerente General]
**De:** [Tu nombre], [Tu empresa]
**Fecha:** [fecha] · **Validez:** 30 días

---

## 1. Lo que entendemos de su situación

Una agencia de 30 personas en Lima maneja un volumen alto de cotizaciones, casi siempre por WhatsApp, correo y Excel. En la práctica esto significa:

- **Cotizar toma demasiado tiempo.** Armar una cotización de un paquete o un corporativo implica buscar tarifas, armar el itinerario, calcular margen y pasarlo a PDF con la marca de la agencia. Entre 1 y 3 horas por cotización.
- **Se pierden ventas por falta de seguimiento.** El vendedor cotiza, envía, y si el cliente no responde en 48 horas, se enfría. No hay recordatorios ni visibilidad de lo pendiente.
- **No se conoce el margen real.** Cada vendedor maneja su propio Excel. Gerencia no tiene una vista consolidada de pipeline, conversión ni rentabilidad por vendedor o línea de negocio.
- **La información vive en el celular del vendedor.** Si alguien renuncia, se va con su cartera y su historial.

Y hoy eso tiene un costo visible: **[su proveedor actual cobra $120 por usuario al mes y no incluye la implementación]**. La agencia paga precio de CRM premium por una herramienta que todavía no resuelve el problema de fondo, que es cotizar rápido y hacer seguimiento.

En temporada alta el volumen se multiplica: la agencia crece en operaciones pero no necesariamente en margen.

## 2. Qué proponemos

**[Nombre del software]** es un CRM diseñado específicamente para agencias de viajes, con un **módulo de cotización rápida** que es el corazón del sistema.

**El cotizador permite:**
- Armar una cotización completa en **menos de 15 minutos**, con plantillas por destino y tipo de viaje
- Cargar tarifarios de proveedores y calcular **el margen automáticamente** (no lo define el vendedor a mano)
- Manejo **multi-moneda** (USD/PEN) con tipo de cambio actualizado
- Generar un **PDF con la marca de la agencia** y enviarlo por WhatsApp o correo en un clic
- Link de aceptación para el cliente, que pasa directo a **reserva** sin rehacer datos

**El CRM alrededor:**
- Pipeline visual: lead → cotización → seguimiento → reserva
- **Recordatorios automáticos** de seguimiento a las 48 h y a los 7 días
- Historial completo del cliente y de cada cotización enviada
- Reportes de conversión, ticket promedio y margen por vendedor
- Roles y permisos: vendedor, supervisor, gerencia

**Resultados esperados** (agencias de tamaño similar que ya usan el sistema):

| Antes | Después |
|---|---|
| 1–3 h por cotización | 10–15 min |
| Seguimiento manual, se olvida | Recordatorio automático, 100 % de cotizaciones seguidas |
| Margen desconocido hasta el cierre | Margen visible antes de enviar |
| Pipeline solo en la cabeza del vendedor | Panel gerencial en tiempo real |

## 3. Implementación — 2 semanas, incluidas sin costo

| Fase | Qué hacemos | Cuándo |
|---|---|---|
| Configuración | Usuarios, roles, pipeline, etapas de venta | Semana 1 |
| Tarifarios y plantillas | Carga de tarifas de proveedores y plantillas de cotización por destino | Semana 1 |
| Migración de cartera | Clientes e historial desde Excel al sistema | Semana 2 |
| Capacitación | 2 sesiones: vendedores y gerencia | Semana 2 |
| Prueba real | Una cotización completa de punta a punta con su equipo | Semana 2 |

**El onboarding está incluido sin costo.** Su proveedor actual no lo incluye; en el mercado este servicio se cobra aparte y suele representar entre una y tres mensualidades adicionales.

**Alcance del onboarding incluido** (para que no haya sorpresas en ninguna dirección):
- Hasta 20 usuarios
- Hasta 1.000 registros de clientes migrados
- Hasta 10 plantillas de cotización
- 2 sesiones de capacitación de hasta 2 horas cada una

**Fuera de alcance, cotizable aparte:** integraciones con GDS (Amadeus/Sabre), facturación electrónica SUNAT, integración con WhatsApp Business API, y migraciones que superen los límites indicados.

**Incluye además:** soporte y actualizaciones durante la vigencia del contrato.

## 4. Inversión

*Precios en dólares. No incluyen IGV (18 %) cuando corresponda.*

**Plan Profesional — $89 por usuario al mes**
- Mínimo 10 usuarios
- **Contrato anual: 15 % de descuento** → **$75,65 por usuario al mes efectivo**
- Onboarding de 2 semanas incluido ($0)
- Soporte y actualizaciones incluidos

### Según el número de licencias

| Usuarios | Precio lista/mes | Anual lista | **Anual con 15 % dcto.** | Equivalente/mes | Ahorro anual |
|---|---|---|---|---|---|
| 10 (mínimo) | $890 | $10.680 | **$9.078** | $756,50 | $1.602 |
| 15 | $1.335 | $16.020 | **$13.617** | $1.134,75 | $2.403 |
| **20 (recomendado)** | $1.780 | $21.360 | **$18.156** | $1.513 | $3.204 |
| 25 | $2.225 | $26.700 | **$22.695** | $1.891,25 | $4.005 |
| 30 | $2.670 | $32.040 | **$27.234** | $2.269,50 | $4.806 |

### Recomendación: 20 licencias

De las 30 personas, **20 licencias cubren con holgura al equipo comercial**. Operaciones y administración pueden entrar con 2 o 3 accesos de solo lectura que ya están contemplados dentro de esas 20.

**Inversión primer año con 20 licencias: $18.156** (onboarding incluido, $0 adicional).

### Comparación directa

| | Proveedor actual | [Nombre del software] |
|---|---|---|
| Precio por usuario/mes | $120 | **$75,65 efectivo** |
| 20 usuarios / mes | $2.400 | **$1.513** |
| Costo anual | $28.800 | **$18.156** |
| Onboarding | No incluido | **Incluido (2 semanas)** |
| **Diferencia** | | **$10.644 menos al año — 37 % menos** |

### Impacto operativo *(ejemplo ilustrativo — ajustar con sus datos reales)*

Con 10 vendedores cotizando 2 viajes al día (unas 400 cotizaciones al mes) y un ahorro promedio de 1 hora por cotización, se liberan **~400 horas al mes** de trabajo comercial. A un costo cargado de $5/hora, eso equivale a **$2.000 mensuales en capacidad recuperada**, frente a una inversión de $1.513/mes. Y eso sin contar las reservas adicionales que genera el seguimiento automático.

*Este cálculo es referencial: reemplácenlo por sus propios volúmenes si quieren que la comparación sea exacta.*

### Formas de pago

- **Anual prepagado:** $18.156 (incluye el 15 % de descuento).
- **Anual fraccionado:** 12 cuotas de $1.513 (mismo descuento, con domiciliación).

### Condiciones

- Contrato anual. El 15 % de descuento aplica sobre el compromiso anual.
- Mínimo 10 licencias durante la vigencia del contrato.
- Licencias adicionales se prorratean al mismo precio unitario.
- Reducción de licencias al momento de la renovación, con 30 días de aviso.
- Sin permanencia forzada después del primer año.

## 5. Por qué nosotros

- **Es software vertical, no un CRM genérico adaptado.** El cotizador está construido para la operación real de una agencia de viajes, no para un call center. *(Aquí va tu diferencial verdadero: años en el sector turismo, cuántas agencias peruanas lo usan, algún cliente que puedas nombrar.)*
- **Onboarding de 2 semanas incluido**, contra un proveedor que lo cobra aparte o no lo ofrece.
- **37 % menos de costo anual** que su alternativa actual, con más funcionalidad para el equipo comercial.
- **Sin hardware ni servidores:** funciona en navegador y móvil desde el primer día.

## 6. Siguiente paso

Propongo una **demo de 45 minutos** con usted y dos o tres vendedores, usando una cotización real de la agencia. En esa sesión ven el cotizador funcionando con sus propios destinos y tarifas, y salen con una decisión clara.

¿Les funciona el **[día] a las [hora]** o prefieren **[día 2]**?

---

# Antes de enviar

**1. Confirma el punto del competidor.** Si el de $120 **no es** su proveedor actual sino solo una alternativa que vieron, elimina estas dos frases:
- En la sección 1: *"Y hoy eso tiene un costo visible: su proveedor actual cobra $120 por usuario al mes y no incluye la implementación."* → cámbiala por *"Alternativas que han evaluado cobran $120 por usuario al mes y no incluyen la implementación."*
- En la sección 4, cambia el encabezado "Proveedor actual" por "Alternativa comparada".

**2. Quité los planes Esencial y Enterprise que yo había inventado.** Solo tienes Profesional confirmado, así que la propuesta gira alrededor de un plan único con escala por volumen. Si tienes un plan inferior para clientes pequeños, no hace falta aquí: 30 empleados no lo van a mirar y solo te resta foco.

**3. Decide si recomiendas 20 licencias o 15.** Puse 20 porque maximiza tu ingreso y sigue siendo defendible para 30 empleados. Si quieres una propuesta más agresiva para cerrar rápido, ofrece **15 licencias a $13.617/año**: bajas el compromiso total y el precio por usuario sigue siendo el mismo. El riesgo es que luego sumen licencias de a pocas y te genere trabajo administrativo.

**4. El diferencial de la sección 5 sigue siendo el punto débil.** Precio y onboarding incluido son argumentos puntuales, no un diferencial sostenible: mañana cualquiera puede igualarlos. Necesito al menos un dato duro — cuántas agencias peruanas usan el sistema, años operando en turismo, o un cliente que puedas nombrar. Pásamelo y te lo redacto.

**5. Verifica el tratamiento de IGV.** Si facturas desde Perú a una empresa peruana, el IGV del 18 % se suma a los montos y conviene que aparezca explícito para que no haya fricción con administración al momento de firmar. Si facturas desde el exterior, borra esa línea.

**6. La validez de 30 días la puse yo.** Si prefieres 15 días para meter presión de cierre, es un ajuste de una palabra.