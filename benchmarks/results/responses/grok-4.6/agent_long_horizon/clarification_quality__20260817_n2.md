# Grok 4.6 — agent_long_horizon/clarification_quality

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.09 | quality: 10.0
- latency_total: 181.841s | tokens_per_second: 54.2
- input_tokens: 4840 | output_tokens: 7834

## Conversación completa (4 turnos)

### Turno 1 — usuario

Necesito que me hagas la propuesta.

### Turno 1 — modelo

Para hacerte **la propuesta** de forma útil necesito contexto, porque “propuesta” puede ser muchas cosas distintas y el resultado cambia por completo.

Responde, por favor, a esto (lo más concreto posible):

1. **¿Qué tipo de propuesta es?**  
   (inversión/pitch, comercial a un cliente, alianza/partnership, proyecto, subvención, interna al equipo, otra)

2. **¿De qué negocio, producto o proyecto se trata?**  
   (en 4-8 líneas: qué vendéis, a quién, en qué fase estáis)

3. **¿Para quién es exactamente?**  
   (nombre o perfil: inversor, cliente concreto, socio, organismo…)

4. **¿Qué objetivo tiene?**  
   (cerrar una reunión, pedir X €, vender un servicio, firmar un acuerdo…)

5. **¿Qué material ya tienes?**  
   (números, competencia, diferenciación, equipo, plazos, presupuesto, condiciones que quieres incluir)

6. **Formato y tono**  
   (documento Word/PDF, presentación, email, 1 página o más extensa; formal, directo, storytelling…)

Con eso te la redacto yo. Si falta algún dato crítico te lo pediré; si asumo algo lo diré explícitamente.

### Turno 2 — usuario

Es una propuesta comercial. Para un cliente nuevo. Yo vendo software.

### Turno 2 — modelo

Para redactar una **propuesta comercial** que no sea genérica (y que realmente pueda cerrar), me falta información que cambia el documento por completo.

Responde a esto, aunque sea en bullets:

**Sobre tu software**
- ¿Qué vendes exactamente? (nombre, tipo: SaaS, a medida, ERP, CRM, app, etc.)
- ¿Qué problema resuelve y para qué tipo de empresa?
- ¿Qué incluye la oferta? (licencias, implantación, formación, soporte, integraciones…)
- Precio o modelo (mensual, anual, por usuario, proyecto cerrado, rangos si aún no hay cifra fija)

**Sobre el cliente**
- Nombre o perfil (sector, tamaño, país)
- ¿Qué sabes de su necesidad o del contacto que has tenido? (reunión, email, dolor concreto)
- ¿Hay un decisor o un proceso de compra que debamos tener en cuenta?

**Sobre la propuesta**
- Objetivo: ¿primera oferta, presupuesto formal, o “vamos a una reunión”?
- ¿Quieres 1 página, 3-5 páginas o presentación?
- Condiciones que deban ir: plazos, forma de pago, vigencia de la oferta, garantía, SLA
- ¿Tienes casos de éxito, logos o cifras que podamos usar?

Con eso te la escribo lista para enviar. Si hay algo que no sepas aún, dímelo y lo dejo como variable o te propongo un texto flexible.

### Turno 3 — usuario

Es una agencia de viajes mediana, 30 empleados, en Lima. Mi software es un CRM con módulo de cotización rápida para vendedores de turismo. Quieren saber qué les ofrezco y precio.

### Turno 3 — modelo

**Suposiciones (cámbialas antes de enviar):** no me diste nombre comercial, alcance real ni tarifas. Redacto una propuesta lista para una agencia de viajes mediana en Lima, con CRM + cotización rápida. Empaqueté precio de referencia para ~12 usuarios comerciales (no los 30 empleados). **Sustituye importes, plazos y nombre del producto.** Si tus números son otros, dímelos y rearmo la tabla en un mensaje.

---

# PROPUESTA COMERCIAL  
**CRM de turismo + módulo de cotización rápida**

**Para:** Dirección / Jefatura Comercial  
Agencia de viajes — Lima, Perú (~30 colaboradores)  
**De:** [Tu empresa] · [Tu nombre] · [cargo] · [teléfono] · [email] · [web]  
**Fecha:** [dd/mm/aaaa]  
**Vigencia de esta oferta:** 30 días calendario  
**Ref.:** PROP-LIM-2026-001

---

## 1. Entendemos su operación

En una agencia mediana el cuello de botella casi nunca es “conseguir más leads”. Es **pasar de consulta a cotización firme** mientras el vendedor salta entre WhatsApp, Excel, correos del operador, tarifas que vencen y un seguimiento que se pierde cuando hay feriado, grupo o temporada alta.

Sin un sistema común suele pasar esto:

- Cada vendedor cotiza distinto (formato, margen, vigencia, condiciones).
- El cliente compara 2–3 agencias; gana quien responde **completo y rápido**.
- La jefatura no ve el pipeline real: cotizado vs. ganado vs. perdido, ni por producto (nacionales, internacionales, grupos, corporativo).
- Al rotar o faltar un vendedor, se lleva el historial en el celular.

Esta propuesta cubre exactamente eso: **un CRM pensado para vendedores de turismo**, con un módulo para armar y enviar cotizaciones en minutos, con control comercial para la agencia.

---

## 2. Qué les ofrecemos

**[NOMBRE DEL SOFTWARE]** — plataforma en la nube para el equipo comercial y de operaciones de la agencia.

### 2.1 CRM comercial
- Ficha única del cliente y del viajero (contacto, empresa, preferencias, historial).
- Embudo de ventas: lead → consulta → cotizado → seguimiento → ganado / perdido.
- Tareas, recordatorios y asignación por vendedor o por sucursal/equipo.
- Origen del lead (web, walk-in, referido, corporativo, redes, operadores).
- Agenda de seguimientos para que ninguna cotización “se enfríe”.
- Visibilidad para jefatura: actividad por vendedor, tasas de cierre, montos.

### 2.2 Módulo de cotización rápida (el diferenciador para el mostrador y el teléfono)
- Armado de cotización con bloques típicos de turismo: **aéreo, hotel, transfer, tours, seguros, otros**.
- Plantillas por tipo de viaje (nacional, internacional, luna de miel, grupo, corporativo, full day).
- Cálculo de **costo, markup/comisión y precio de venta** (el vendedor no “adivina” el margen).
- Varias opciones en un mismo documento (Ej. Hotel A / Hotel B, o vuelo directo vs. escala).
- Vigencia de tarifa y condiciones visibles para el cliente.
- Envío por **PDF, correo y enlace** (listo para reenviar por WhatsApp).
- Versionado: se ve qué se envió, cuándo y quién, y se clona para ajustar sin empezar de cero.
- Paso a “ganado” y registro del servicio vendido para no perder el hilo operativo.

### 2.3 Control de agencia
- Roles: vendedor, supervisor, administración, solo lectura.
- Catálogo de servicios / proveedores frecuentes (para no reescribir lo mismo cada vez).
- Reportes: cotizaciones emitidas, ticket promedio, conversión, ranking de vendedores.
- Exportación para cruce con facturación / tesorería (no reemplaza su contabilidad).

### 2.4 Lo que **no** está en esta fase (para no vender humo)
A menos que lo contraten como ampliación: motor de reservas GDS, pasarela de pagos, app del viajero, facturación electrónica SUNAT, o integración profunda con un DMC/operador concreto. Si lo necesitan, se cotiza aparte tras un relevamiento.

---

## 3. Cómo se implanta (para que se use de verdad)

Pensado para una agencia de ~30 personas, **sin parar la venta**.

| Fase | Qué ocurre | Duración orientativa |
|---|---|---|
| 1. Arranque | Kickoff, usuarios, roles, embudo y plantillas de cotización de *su* agencia | Semana 1 |
| 2. Configuración | Catálogo inicial, márgenes por política comercial, textos legales/condiciones | Semanas 1–2 |
| 3. Carga | Importación de clientes/contactos desde Excel (limpieza básica incluida) | Semana 2 |
| 4. Capacitación | Taller vendedores + sesión jefatura (reportes). Guía corta en PDF | Semana 3 |
| 5. Acompañamiento | Soporte de arranque y ajustes de plantillas con casos reales | Semanas 3–6 |

**Puesta en marcha objetivo: 3 a 4 semanas** hasta operación diaria.  
Ustedes designan un interlocutor interno (comercial u operaciones). Nosotros no pedimos un proyecto de 6 meses.

---

## 4. Qué incluye el servicio

**Incluso en el plan recomendado:**

- Licencia SaaS del CRM + módulo de cotización.
- Hosting, actualizaciones de producto y copias de seguridad.
- Implantación según el plan de la sección 3.
- Capacitación inicial (hasta 2 sesiones grupales + 1 de jefatura).
- Soporte en horario laboral [indicar, ej. Lun–Vie 9:00–18:00 Perú] por [correo / WhatsApp Business / mesa].
- Hasta **12 usuarios** nombrados (ampliable).

**No incluye:** desarrollos a medida, integraciones con terceros no listadas, migración desde otro CRM complejo, ni hardware.

---

## 5. Inversión

**Suposición de empaquetado** (ajústala a tu lista de precios real). Cifras en **USD + IGV (18%)**. Facturación en soles al tipo de cambio que acuerden, si lo prefieren.

Pensado para **agencia mediana, 12 usuarios comerciales** (el resto del staff no necesita licencia).

| Concepto | Plan Agencia (recomendado) |
|---|---|
| Puesta en marcha (único) — configuración, importación Excel, plantillas, capacitación | **USD 1.200** (pago único) |
| Suscripción mensual — CRM + cotización rápida, 12 usuarios, soporte estándar | **USD 348 / mes** (USD 29 / usuario) |
| Usuario adicional | USD 29 / mes |
| Compromiso | 12 meses (luego mes a mes) |
| Alternativa anual | **USD 3.480 / año** (2 meses de descuento vs. mes a mes) |

### Otras opciones (si quieren empezar más chico o escalar)

| | Esencial | **Agencia (recomendado)** | Red |
|---|---|---|---|
| Usuarios | 5 | **12** | 20 |
| Cotización rápida + CRM | Sí | **Sí** | Sí |
| Plantillas + reportes jefatura | Básico | **Completo** | Completo + más roles |
| Puesta en marcha | USD 800 | **USD 1.200** | USD 1.800 |
| Mensual | USD 175 | **USD 348** | USD 520 |

**Forma de pago sugerida:** 50% de la puesta en marcha al aceptar / 50% al go-live. Suscripción por adelantado mensual o anual, factura electrónica.

**Lo que esto reemplaza en la práctica:** horas de armado en Word/Excel, cotizaciones inconsistentes, seguimiento a ciegas y dependencia del “Excel de cada vendedor”. Si el equipo emite, por ejemplo, 80 cotizaciones/mes y acortan respuesta + mejoran cierre en unos pocos puntos, el sistema se paga solo; el número exacto lo validamos con *sus* cifras en la primera reunión de ajuste.

---

## 6. Condiciones comerciales

- Vigencia de precios: **30 días** desde la fecha de esta propuesta.
- Inicio: a los **5 días hábiles** de la orden de compra / aceptación por escrito y del primer pago.
- Los usuarios son nominativos; se pueden reasignar al rotar personal, sin costo.
- Datos de la agencia: son de ustedes. Al término del contrato, exportación en formato estándar (Excel/CSV) a solicitud.
- Confidencialidad mutua sobre tarifas, clientes y esta oferta.
- SLA de soporte estándar: respuesta en un día hábil; incidentes bloqueantes con prioridad.
- Impuestos: importes netos + IGV. Si aplica detracción u otra figura, se indica en la factura según norma vigente.

---

## 7. Próximo paso (simple)

1. Confirman el **plan** (Esencial / Agencia / Red) y el número de

### Turno 4 — usuario

Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% de descuento. Incluye onboarding gratis 2 semanas. Tienen un competidor actual que cobra $120/usuario sin onboarding.

### Turno 4 — modelo

**Suposición:** el plan único que cotizo es **Profesional** a **USD 89/usuario/mes**, **mínimo 10 usuarios**, **contrato a 12 meses** con **15 % de descuento** si cierran anual. Onboarding de **2 semanas incluido**. No asumo que los 30 empleados necesitan licencia: en agencia mediana suelen cotizar vendedores + jefatura; dejo 10 / 12 / 15 usuarios. Sustituye `[NOMBRE DEL SOFTWARE]`, tus datos y el nombre de la agencia.

---

# Propuesta comercial  
**CRM de turismo + cotización rápida — Plan Profesional**

**Para:** Dirección / Jefatura Comercial  
Agencia de viajes — Lima (~30 colaboradores)  
**De:** [Tu empresa] · [Tu nombre] · [cargo] · [teléfono] · [email] · [web]  
**Fecha:** [dd/mm/aaaa]  
**Vigencia:** 30 días calendario  
**Ref.:** PROP-LIM-2026-001

---

## 1. Para qué sirve esto en su agencia

El problema no es “tener más contactos”. Es **pasar de la consulta a una cotización clara, con margen y vigencia**, antes de que el viajero pida la misma ruta a otra agencia.

`[NOMBRE DEL SOFTWARE]` es un CRM pensado para vendedores de turismo, con un módulo de **cotización rápida** (aéreo, hotel, transfer, tours, seguros y extras). Un solo lugar para el cliente, el seguimiento y lo que se envió.

---

## 2. Qué incluye el Plan Profesional

### CRM comercial
- Ficha única de cliente / viajero e historial.
- Embudo: lead → consulta → cotizado → seguimiento → ganado / perdido.
- Tareas, recordatorios y asignación por vendedor.
- Origen del lead (web, mostrador, referido, corporativo, redes, operador).
- Visibilidad para jefatura: actividad, conversión y montos.

### Cotización rápida
- Bloques típicos de turismo y **varias opciones en un mismo documento**.
- Costo, markup/comisión y precio de venta (política de margen de la agencia).
- Plantillas: nacional, internacional, grupos, corporativo, luna de miel, full day.
- Vigencia y condiciones visibles para el cliente.
- Envío en **PDF, correo y enlace** (listo para WhatsApp).
- Versionado y clonado: se ve qué se mandó, cuándo y quién.

### Control de agencia
- Roles: vendedor, supervisor, administración, solo lectura.
- Catálogo de servicios y proveedores frecuentes.
- Reportes: cotizaciones, ticket promedio, ranking, tasa de cierre.
- Exportación para cruce con tesorería / facturación (no reemplaza contabilidad).

### Fuera de esta oferta (se cotiza aparte si lo piden)
GDS, pasarela de pagos, facturación electrónica SUNAT, app del viajero o integraciones profundas con un operador concreto.

---

## 3. Onboarding incluido (2 semanas, sin costo)

El competidor que están viendo cobra más y **no incluye implantación**. Aquí el arranque va en el plan:

| Semana | Qué hacemos |
|---|---|
| 1 | Kickoff, usuarios y roles, embudo, plantillas de *su* agencia, política de márgenes, importación de contactos desde Excel (limpieza básica). |
| 2 | Capacitación a vendedores + sesión de jefatura (reportes). Ajustes con cotizaciones reales. Salida a uso diario. |

Ustedes nombran un interlocutor interno. No paramos la venta.

**Después del go-live:** soporte en horario laboral [ej. Lun–Vie 9:00–18:00 Perú] por [correo / WhatsApp / mesa]. Actualizaciones y copias de seguridad incluidas.

---

## 4. Inversión — Plan Profesional

| Condición | Detalle |
|---|---|
| Tarifa de lista | **USD 89 / usuario / mes** |
| Mínimo | **10 usuarios** |
| Contrato | **12 meses** |
| Descuento anual | **15 %** |
| Onboarding (2 semanas) | **USD 0** |
| Usuario extra | USD 89 / mes (mismo 15 % si va en el anual) |
| Impuestos | Netos + **IGV 18 %** |

**Precio efectivo con contrato anual (−15 %):**  
USD 89 × 0,85 = **USD 75,65 / usuario / mes**  
o **USD 907,80 / usuario / año** (facturación anual adelantada).

### Ejemplos (eliges el número de licencias)

No hace falta licenciar a los 30 empleados. Licencias para quien cotiza, hace seguimiento o mira el pipeline.

| Usuarios | Lista (mensual) | **Anual con 15 %** (equivalente mensual) | **Total año** |
|---|---:|---:|---:|
| 10 (mínimo) | USD 890 | **USD 756,50** | **USD 9.078** |
| 12 (recomendado*) | USD 1.068 | **USD 907,80** | **USD 10.893,60** |
| 15 | USD 1.335 | **USD 1.134,75** | **USD 13.617** |

\*Recomendado si hay ~10 vendedores + 1–2 jefaturas. Si el equipo comercial es más chico, empiezan en 10 y suman usuarios al rotar o crecer.

**Forma de pago propuesta:** 100 % del anual al aceptar (activa el 15 %). Factura electrónica. Si prefieren soles, al tipo de cambio que acuerden en la OC.

---

## 5. Comparación directa (misma base: 10 usuarios, 12 meses)

Ustedes mencionaron un sistema actual / alternativa a **USD 120 / usuario**, **sin onboarding**.

| | Alternativa a USD 120 | **Plan Profesional** |
|---|---:|---:|
| Precio / usuario / mes | USD 120 | **USD 75,65** (anual −15 %) |
| 10 usuarios / mes | USD 1.200 | **USD 756,50** |
| Costo año (10 usuarios) | USD 14.400 | **USD 9.078** |
| Onboarding | No incluido | **2 semanas incluidas** |
| **Ahorro año 1** | — | **USD 5.322** + implantación |

A 12 usuarios el ahorro anual vs. USD 120 es **USD 6.386,40**, además de no pagar un proyecto de arranque aparte.

---

## 6. Condiciones

- Vigencia de esta oferta: **30 días**.
- Inicio: dentro de **5 días hábiles** de la aceptación por escrito y el pago del anual.
- Usuarios nominativos; se reasignan si rota personal, sin costo.
- Los datos son de la agencia. Al término: exportación Excel/CSV a solicitud.
- Confidencialidad mutua (tarifas, clientes, esta oferta).
- SLA estándar: respuesta en un día hábil; incidentes bloqueantes con prioridad.
- Renovación: se avisa con 30 días; si no hay aviso de no renovación, se propone renovar en las mismas condiciones vigentes.

---

## 7. Cómo seguir

1. Confirman **número de usuarios** (10 / 12 / 15 u otro ≥ 10).  
2. Les envío la OC / contrato de 12 meses con el total en USD + IGV.  
3. Kickoff en la fecha que elijan; **go-live objetivo: 10 días hábiles**.

Si quieres, el siguiente mensaje te lo dejo como **email de envío** (8–12 líneas) o como **versión de 1 página** para imprimir. Dime el **nombre del software**, el **nombre de la agencia** y si cotizan **10, 12 o 15** y lo dejo cerrado, sin corchetes.


## Respuesta completa

**Suposición:** el plan único que cotizo es **Profesional** a **USD 89/usuario/mes**, **mínimo 10 usuarios**, **contrato a 12 meses** con **15 % de descuento** si cierran anual. Onboarding de **2 semanas incluido**. No asumo que los 30 empleados necesitan licencia: en agencia mediana suelen cotizar vendedores + jefatura; dejo 10 / 12 / 15 usuarios. Sustituye `[NOMBRE DEL SOFTWARE]`, tus datos y el nombre de la agencia.

---

# Propuesta comercial  
**CRM de turismo + cotización rápida — Plan Profesional**

**Para:** Dirección / Jefatura Comercial  
Agencia de viajes — Lima (~30 colaboradores)  
**De:** [Tu empresa] · [Tu nombre] · [cargo] · [teléfono] · [email] · [web]  
**Fecha:** [dd/mm/aaaa]  
**Vigencia:** 30 días calendario  
**Ref.:** PROP-LIM-2026-001

---

## 1. Para qué sirve esto en su agencia

El problema no es “tener más contactos”. Es **pasar de la consulta a una cotización clara, con margen y vigencia**, antes de que el viajero pida la misma ruta a otra agencia.

`[NOMBRE DEL SOFTWARE]` es un CRM pensado para vendedores de turismo, con un módulo de **cotización rápida** (aéreo, hotel, transfer, tours, seguros y extras). Un solo lugar para el cliente, el seguimiento y lo que se envió.

---

## 2. Qué incluye el Plan Profesional

### CRM comercial
- Ficha única de cliente / viajero e historial.
- Embudo: lead → consulta → cotizado → seguimiento → ganado / perdido.
- Tareas, recordatorios y asignación por vendedor.
- Origen del lead (web, mostrador, referido, corporativo, redes, operador).
- Visibilidad para jefatura: actividad, conversión y montos.

### Cotización rápida
- Bloques típicos de turismo y **varias opciones en un mismo documento**.
- Costo, markup/comisión y precio de venta (política de margen de la agencia).
- Plantillas: nacional, internacional, grupos, corporativo, luna de miel, full day.
- Vigencia y condiciones visibles para el cliente.
- Envío en **PDF, correo y enlace** (listo para WhatsApp).
- Versionado y clonado: se ve qué se mandó, cuándo y quién.

### Control de agencia
- Roles: vendedor, supervisor, administración, solo lectura.
- Catálogo de servicios y proveedores frecuentes.
- Reportes: cotizaciones, ticket promedio, ranking, tasa de cierre.
- Exportación para cruce con tesorería / facturación (no reemplaza contabilidad).

### Fuera de esta oferta (se cotiza aparte si lo piden)
GDS, pasarela de pagos, facturación electrónica SUNAT, app del viajero o integraciones profundas con un operador concreto.

---

## 3. Onboarding incluido (2 semanas, sin costo)

El competidor que están viendo cobra más y **no incluye implantación**. Aquí el arranque va en el plan:

| Semana | Qué hacemos |
|---|---|
| 1 | Kickoff, usuarios y roles, embudo, plantillas de *su* agencia, política de márgenes, importación de contactos desde Excel (limpieza básica). |
| 2 | Capacitación a vendedores + sesión de jefatura (reportes). Ajustes con cotizaciones reales. Salida a uso diario. |

Ustedes nombran un interlocutor interno. No paramos la venta.

**Después del go-live:** soporte en horario laboral [ej. Lun–Vie 9:00–18:00 Perú] por [correo / WhatsApp / mesa]. Actualizaciones y copias de seguridad incluidas.

---

## 4. Inversión — Plan Profesional

| Condición | Detalle |
|---|---|
| Tarifa de lista | **USD 89 / usuario / mes** |
| Mínimo | **10 usuarios** |
| Contrato | **12 meses** |
| Descuento anual | **15 %** |
| Onboarding (2 semanas) | **USD 0** |
| Usuario extra | USD 89 / mes (mismo 15 % si va en el anual) |
| Impuestos | Netos + **IGV 18 %** |

**Precio efectivo con contrato anual (−15 %):**  
USD 89 × 0,85 = **USD 75,65 / usuario / mes**  
o **USD 907,80 / usuario / año** (facturación anual adelantada).

### Ejemplos (eliges el número de licencias)

No hace falta licenciar a los 30 empleados. Licencias para quien cotiza, hace seguimiento o mira el pipeline.

| Usuarios | Lista (mensual) | **Anual con 15 %** (equivalente mensual) | **Total año** |
|---|---:|---:|---:|
| 10 (mínimo) | USD 890 | **USD 756,50** | **USD 9.078** |
| 12 (recomendado*) | USD 1.068 | **USD 907,80** | **USD 10.893,60** |
| 15 | USD 1.335 | **USD 1.134,75** | **USD 13.617** |

\*Recomendado si hay ~10 vendedores + 1–2 jefaturas. Si el equipo comercial es más chico, empiezan en 10 y suman usuarios al rotar o crecer.

**Forma de pago propuesta:** 100 % del anual al aceptar (activa el 15 %). Factura electrónica. Si prefieren soles, al tipo de cambio que acuerden en la OC.

---

## 5. Comparación directa (misma base: 10 usuarios, 12 meses)

Ustedes mencionaron un sistema actual / alternativa a **USD 120 / usuario**, **sin onboarding**.

| | Alternativa a USD 120 | **Plan Profesional** |
|---|---:|---:|
| Precio / usuario / mes | USD 120 | **USD 75,65** (anual −15 %) |
| 10 usuarios / mes | USD 1.200 | **USD 756,50** |
| Costo año (10 usuarios) | USD 14.400 | **USD 9.078** |
| Onboarding | No incluido | **2 semanas incluidas** |
| **Ahorro año 1** | — | **USD 5.322** + implantación |

A 12 usuarios el ahorro anual vs. USD 120 es **USD 6.386,40**, además de no pagar un proyecto de arranque aparte.

---

## 6. Condiciones

- Vigencia de esta oferta: **30 días**.
- Inicio: dentro de **5 días hábiles** de la aceptación por escrito y el pago del anual.
- Usuarios nominativos; se reasignan si rota personal, sin costo.
- Los datos son de la agencia. Al término: exportación Excel/CSV a solicitud.
- Confidencialidad mutua (tarifas, clientes, esta oferta).
- SLA estándar: respuesta en un día hábil; incidentes bloqueantes con prioridad.
- Renovación: se avisa con 30 días; si no hay aviso de no renovación, se propone renovar en las mismas condiciones vigentes.

---

## 7. Cómo seguir

1. Confirman **número de usuarios** (10 / 12 / 15 u otro ≥ 10).  
2. Les envío la OC / contrato de 12 meses con el total en USD + IGV.  
3. Kickoff en la fecha que elijan; **go-live objetivo: 10 días hábiles**.

Si quieres, el siguiente mensaje te lo dejo como **email de envío** (8–12 líneas) o como **versión de 1 página** para imprimir. Dime el **nombre del software**, el **nombre de la agencia** y si cotizan **10, 12 o 15** y lo dejo cerrado, sin corchetes.