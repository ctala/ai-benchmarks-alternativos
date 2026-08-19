# Qwen 3.8 2.4T (A95B) — agent_long_horizon/clarification_quality

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 53.522s | tokens_per_second: 175.7
- input_tokens: 5214 | output_tokens: 6581

## Conversación completa (4 turnos)

### Turno 1 — usuario

Necesito que me hagas la propuesta.

### Turno 1 — modelo



Con gusto. Antes de redactarla necesito aclarar algo clave: **¿qué tipo de propuesta necesitas y para quién va dirigida?**

Por ejemplo:
- Propuesta comercial para un cliente
- Propuesta de servicios/proyecto
- Propuesta de inversión
- Propuesta interna para un socio o equipo

Si me dices el objetivo, el destinatario y un poco de contexto, te preparo la propuesta.

### Turno 2 — usuario

Es una propuesta comercial. Para un cliente nuevo. Yo vendo software.

### Turno 2 — modelo



Perfecto. La ambigüedad material aquí es que una propuesta de software puede variar mucho según el tipo de producto, el problema del cliente y el modelo de venta. No es lo mismo vender un SaaS estándar que un desarrollo a medida o una licencia con implementación.

Para no asumir algo que cambie el resultado, necesito que me confirmes al menos estos puntos:

1. **Nombre de tu empresa o software**  
2. **Qué tipo de software vendes**  
   - SaaS / suscripción  
   - Licencia  
   - Desarrollo a medida  
   - Implementación de software de terceros  
3. **Qué problema resuelve o qué beneficio principal aporta**  
4. **Perfil del cliente nuevo**  
   - Sector, tamaño, cargo del contacto  
5. **Qué incluye la propuesta**  
   - Licencias, implementación, capacitación, soporte, integración, horas, etc.  
6. **Precio o modelo comercial**  
   - Mensual, anual, pago único, por usuario, por módulo, por proyecto  
7. **Plazo estimado de implementación o entrega**  
8. **Diferenciadores clave frente a otras opciones**

Mientras tanto, te dejo una **propuesta comercial base profesional** que puedes usar con campos rellenables.

---

# Propuesta comercial de software

**Para:** [Nombre del cliente / Empresa]  
**De:** [Tu nombre / Tu empresa]  
**Fecha:** [Fecha]  
**Validez de la propuesta:** [Ej. 15 días]

---

## 1. Resumen ejecutivo

Estimado/a [nombre del contacto]:

A partir de lo conversado, entendemos que [empresa del cliente] busca [objetivo principal: mejorar control, automatizar procesos, aumentar ventas, reducir errores, digitalizar operación, etc.].

Desde [tu empresa/software], proponemos una solución de software orientada a [beneficio principal], permitiendo [resultado concreto: centralizar información, automatizar tareas, mejorar la trazabilidad, tomar decisiones con datos, reducir tiempos operativos, etc.].

Nuestra propuesta contempla [licenciamiento / implementación / configuración / capacitación / soporte], con el objetivo de que la solución pueda ser adoptada de forma rápida, segura y alineada a las necesidades del negocio.

---

## 2. Entendimiento de la necesidad

Según lo identificado, [empresa del cliente] presenta los siguientes desafíos:

- [Dolor 1: ejemplo, información dispersa en planillas o sistemas separados]  
- [Dolor 2: ejemplo, falta de visibilidad en tiempo real]  
- [Dolor 3: ejemplo, procesos manuales que generan retrabajo]  
- [Dolor 4: ejemplo, dificultad para controlar operaciones, ventas, inventario, clientes, etc.]

Esta situación puede generar [consecuencia: pérdida de tiempo, errores, costos innecesarios, demoras, falta de control, menor productividad, etc.].

La solución propuesta busca atacar directamente estos puntos mediante [nombre del software], una plataforma diseñada para [funcionalidad central].

---

## 3. Solución propuesta

Proponemos la implementación de **[nombre del software]**, una solución de software que permite:

- [Funcionalidad 1]  
- [Funcionalidad 2]  
- [Funcionalidad 3]  
- [Funcionalidad 4]  
- [Funcionalidad 5]

### Beneficios esperados

Con esta solución, [empresa del cliente] podrá:

- [Beneficio 1: ejemplo, centralizar la operación en una sola plataforma]  
- [Beneficio 2: ejemplo, reducir tareas manuales]  
- [Beneficio 3: ejemplo, mejorar la trazabilidad de la información]  
- [Beneficio 4: ejemplo, acceder a reportes en tiempo real]  
- [Beneficio 5: ejemplo, mejorar la toma de decisiones]

---

## 4. Alcance del servicio

La propuesta incluye los siguientes componentes:

### 4.1 Licenciamiento / acceso a la plataforma

- Acceso a [nombre del software]
- Modalidad: [SaaS / licencia / cloud / on-premise]
- Usuarios incluidos: [cantidad]
- Módulos incluidos: [módulos]
- Periodo contratado: [mensual / anual / proyecto]

### 4.2 Implementación y configuración

- Relevamiento inicial de requerimientos
- Configuración de la plataforma según necesidades del cliente
- Carga inicial de datos / parametrización básica
- Configuración de usuarios, roles y permisos
- Ajustes de flujos principales

### 4.3 Integraciones, si aplica

- Integración con [sistema / ERP / CRM / facturación / e-commerce / API]
- Alcance de la integración: [detalle]
- Requisitos técnicos: [detalle]

### 4.4 Capacitación

- Capacitación inicial para usuarios clave
- Modalidad: [presencial / remota]
-

### Turno 3 — usuario

Es una agencia de viajes mediana, 30 empleados, en Lima. Mi software es un CRM con módulo de cotización rápida para vendedores de turismo. Quieren saber qué les ofrezco y precio.

### Turno 3 — modelo

We need answer in Spanish. User asks: "Es una agencia de viajes mediana, 30 empleados, en Lima. Mi software es un CRM con módulo de cotización rápida para vendedores de turismo. Quieren saber qué les ofrezco y precio."

We need produce proposal. Need maybe ask about price? The user hasn't given pricing. Ambiguity affects price materially. But perhaps we can draft proposal with pricing placeholders or propose a pricing structure and ask for confirmation. System says if ambiguity material ask before assuming. Price is material and unknown. But user asks to make proposal. Could provide draft with suggested pricing options and explicit assumption? Need maybe ask for price details. However likely they need a proposal they can send; we can create a proposal with pricing table using placeholders or recommended ranges. Since price is unknown, we should either ask or state assumptions. Better: give ready-to-use proposal with pricing as editable, and mention I need pricing to finalize. But user likely wants output. We can include a suggested pricing model, but not assume actual numbers unless explicit. Maybe we can say: "No tengo tu precio, así que te dejo una estructura con importes editables; si me das precios los reemplazo." But the instruction: if decide assume, declare. We could assume a SaaS monthly per user pricing? But material. Maybe avoid making up numbers, use placeholders. However the user says "Quieren saber qué les ofrezco y precio." Need provide proposal that includes price. Could include price ranges or packages with placeholder [S/ X]. Maybe propose 3 planes based on 30 employees. But if we invent numbers, risky. We can state: "Dejé los precios como variables editables porque no me indicaste tu tarifa; si quieres, pásame precio por usuario, implementación y soporte y lo dejo listo." But maybe less helpful. Could also include a recommended pricing framework for CRM tourism in Lima: maybe implementation one-time + monthly per user. But we shouldn't assert market rates? Could as assumption. Need maybe ask one targeted question: price. But user likely expects draft. Since they gave enough context except price. We can produce a proposal with pricing table placeholders and explicit assumption that prices need confirmation. Maybe also include a suggested commercial structure: 3 packages: Essential, Pro, Advanced. For 30 employees, maybe 15-30 users? Need clarify: 30 employees, not all users. Could assume 10 vendedor/usuario licenses? But material. Use placeholders.

Need final answer in Spanish. Should be comprehensive, ready to copy/edit. Include: cover, client, problem, solution, modules, benefits, scope, implementation plan, deliverables, pricing, payment terms, validity, next steps. Since price unknown, include editable pricing. Could also include "opción recomendada para 30 empleados" with 10-15 usuarios vendedores + admins. Need maybe mention currency: soles or USD? In Lima, likely S/ or USD. Ask? Could use S/ placeholder. But if assume currency, state. We can state: "Asumo que cotizas en soles; si es USD, cambiar." But price still unknown.

Need maybe include a short note at top: "Como no me diste precios, te dejo estructura con montos editables. Si me pasas precios, lo completo." But the final should be proposal. Could include two sections: 1) questions needed to finalize price; 2) draft proposal. But user asked make proposal. We can be helpful: provide a sendable proposal with [S/ monto]. Maybe include recommended pricing if they want? We can include a "tabla de precios sugerida" but label as editable.

Need consider system: when ambiguous and material, ask before assuming. If decide assume, declare. We can say: "No voy a inventar tu precio; te dejo campos editables. Para cerrarla necesito: precio por usuario, implementación, etc." But perhaps we can still provide proposal. The instruction says if question points to real ambiguity better. The real ambiguity is price and number of licensed users. Could ask before generating? But they've asked for proposal; maybe we can provide a template and ask for price. However final answer should satisfy. Could produce a proposal with placeholders and explicit assumptions. That seems safe.

Need maybe include specific features for travel agency CRM: gestión de leads, cotizaciones rápidas, itinerarios, proveedores, seguimiento, recordatorios, documentos, ventas, comisiones, reportes, integración con WhatsApp/email, etc. Module cotización rápida: plantillas, tarifas, margen, envío PDF, seguimiento, aprobación. For 30 employees: maybe roles: asesores, ejecutivos, operaciones, administración. Need propose phased implementation: diagnóstico, configuración, migración, capacitación, puesta en marcha, soporte. Timeline: 3-6 semanas. Pricing packages: Setup one-time + subscription per user. Maybe include optional add-ons: WhatsApp Business API, facturación, contabilidad, pasarela, data migration, advanced analytics. Payment terms: 50% inicio, 50% go-live; subscription monthly/annual. Validity 15/30 days. Include assumptions and exclusions.

Need maybe include "qué les ofrezco" clearly. Could produce formal proposal.

Need decide if include numbers placeholders or suggested amounts. The user says "precio". If I leave placeholders, maybe not enough. Could propose a pricing structure with example ranges but clearly as assumption. But if I invent numbers, could mislead. Maybe include "rangos referenciales" and ask to confirm. But system says if assume declare. Could say: "Como no me indicaste tu lista de precios, te dejo una estructura con montos editables. No estoy asumiendo precios finales." That is not assuming. But maybe need include numbers? Could include [S/ 0.00]. Better.

Could also ask a concise clarifying question: "¿Cuál es tu precio por usuario/mes, implementación y soporte?" But user likely expects final. We can combine: "Te dejo propuesta lista para completar con precios; si me das precios la finalizo." The instruction says pregunta antes de asumir if ambiguity material. Since price is material, ask. But we can still provide a draft. Need maybe final answer with proposal and explicit request for price details.

Need ensure Spanish. Tone professional. Maybe include "Asunción declarada: la propuesta está en soles y para 15 usuarios vendedores + 3 administradores; ajustar." But user didn't say number of users. 30 employees may not all use CRM. Could assume 15-20 users? Material. Better ask: "¿cuántos usuarios reales usarán el CRM?" Could include in proposal as variable.

Need maybe produce a proposal that uses "30 empleados" as company size, but licenses "a definir". Could propose "paquete recomendado hasta 20 usuarios". But if we assume, state. Maybe: "Para una agencia de 30 empleados, suelo recomendar un paquete de 15 a 20 usuarios (asesores + operaciones + administración), pero debemos confirmarlo." That is a recommendation not final.

Need maybe include pricing table with "Precio unitario" blank. Could include formulas: total = implementation + monthly * users. That helps.

Could final:

"Perfecto. Con ese contexto te preparo una propuesta comercial lista para enviar. Como no me indicaste precios ni cantidad exacta de usuarios, dejo montos editables y una estructura de cobro. Si me pasas: moneda, precio por usuario, implementación, soporte, usuarios estimados, te la dejo final."

Then proposal:

Logo, fecha, cliente, etc.

1. Antecedentes y objetivo.
2. Situación actual.
3. Solución: CRM Turístico + cotización rápida.
4. Funcionalidades: gestión de clientes, leads, cotizaciones, itinerarios, productos/servicios, proveedores, seguimiento, tareas, recordatorios, documentos, reportes, roles, seguridad.
5. Beneficios: reducir tiempo de cotización, aumentar conversión, trazabilidad, etc.
6. Alcance: licencias, implementación, configuración, capacitación, soporte.
7. Plan de implementación: fases with weeks.
8. Entregables.
9. Inversión: table with concepts: Implementación y configuración, Licenciamiento mensual/anual, Capacitación, Soporte, Opcionales. Use placeholders. Maybe packages: Básico, Profesional, Premium. For 30 employees, recommended Profesional. Include "usuarios incluidos" placeholders.
10. Condiciones comerciales: moneda, impuestos, pago, validez, renovación.
11. Supuestos y exclusiones.
12. Próximos pasos.
13. Cierre.

Need maybe include "precio" in clear terms. Could include example: "Ejemplo de estructura (reemplazar): Implementación: S/ 3,500; Suscripción: S/ 120/usuario/mes; Paquete 20 usuarios: S/ 2,400/mes." But if we put example, could be taken as assumption. Maybe label "ejemplo editable". The user likely wants a proposal, maybe with price. If no price, maybe we can propose a price based on market? But that's risky. However as assistant for entrepreneurs, maybe can suggest pricing. Need maybe ask before assuming. But if we decide to assume, declare. Could assume a price range for a CRM SaaS in Peru? Hmm.

Let's think: The user sells software. They need proposal for client. They likely know their price? They didn't provide. They ask "Quieren saber qué les ofrezco y precio." Maybe they

### Turno 4 — usuario

Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% de descuento. Incluye onboarding gratis 2 semanas. Tienen un competidor actual que cobra $120/usuario sin onboarding.

### Turno 4 — modelo

We need answer in Spanish. User provided pricing details. Need produce final proposal. Need maybe calculate pricing. Let's analyze.

User: agency mediana 30 empleados Lima. CRM with quick quote module. They want know what offers and price. Now provided: Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% descuento. Incluye onboarding gratis 2 semanas. Tienen competidor actual que cobra $120/usuario sin onboarding.

Need create propuesta commercial probably ready to send. Need maybe calculate for 10 users minimum and maybe for 30? But not all employees users. Need recommend number of users. Could include scenarios: 10, 15, 20, 30? Since 30 employees, likely users are salespeople + ops + managers. Need maybe ask? But now enough to draft with pricing. Could assume proposal based on minimum 10 users, but maybe client needs more. We can include scalable table: 10 usuarios minimum, recommended 12-15? Need not over-assume. We can state: "He preparado la propuesta con base en 10 usuarios (mínimo), y escenarios de 15/20 para cubrir vendedores, operaciones y supervisión." But if we assume 10, okay because pricing minimum. Maybe include "si todos los 30 empleados usan, precio 30 usuarios". But likely not all.

Need calculate:
Monthly list per user $89. Annual contract 15% discount. Discounted monthly per user = 89 * 0.85 = $75.65. Annual per user = 75.65*12 = $907.80. List annual = 89*12 = $1068; discount = $160.20; final $907.80.
For 10 users: monthly discounted = $756.50; annual = $9,078.00. Without discount: $890 monthly, $10,680 annual. Savings $1,602.
For 15: monthly discounted = 15*75.65 = $1,134.75; annual = $13,617.00. Without discount: $1,335 monthly, $16,020 annual. Savings $2,403.
For 20: monthly = $1,513.00; annual = $18,156.00. Without discount: $1,780 monthly, $21,360 annual. Savings $3,204.
For 30: monthly = $2,269.50; annual = $27,234.00. Without discount: $2,670 monthly, $32,040 annual. Savings $4,806.
Competitor: $120/user/month. For 10 users: $1200/mo, $14,400/year. Our discounted annual: $9,078/year. Savings vs competitor: $5,322/year (36.96% less? 5322/14400=36.96%). Plus free onboarding 2 weeks. If competitor charges $120 and no onboarding, maybe onboarding cost separate. For 15: competitor $1800/mo, $21,600/year; ours $13,617, savings $7,983 (36.96%). For 20: competitor $2400/mo, $28,800/year; ours $18,156, savings $10,644. For 30: competitor $3600/mo, $43,200/year; ours $27,234, savings $15,966.

Need maybe mention currency USD. In Lima maybe USD? User used $. Could state "Los precios están en USD". Need maybe include taxes? Usually not included. Need mention if IGV/IVA not included? In Peru, prices may include IGV? For B2B software maybe no? Need avoid assumption? Could state "Precios no incluyen impuestos locales salvo indicación". But maybe we need assume. We can include "Los precios están expresados en USD y no incluyen impuestos". That's a commercial assumption; we can state. Or ask? It's not material? Could be. But to make proposal, include standard clause: "Precios en USD, no incluyen IGV/impuestos; de ser requerido, se agregarán." That is safe.

Need maybe include comparison table vs competitor. Need emphasize onboarding gratis 2 semanas. Need maybe ROI: time saved, faster quotes, conversion. Could include value proposition.

Need produce final proposal: formal but concise enough. Could be lengthy. Desired oververbosity 9. Need include all.

Need maybe include "Supuestos" about number of users. Since 30 employees but users unknown. We can present recommended: 10, 15, 20, 30. Maybe propose initial 10 users with option to scale. For a travel agency with 30 employees, likely 10-15 vendedores, plus operations/admin. Could say: "Recomendado iniciar con 12-15 usuarios si el equipo comercial y de operaciones usará el CRM; el mínimo contractual es 10." But we don't know. Include scenarios.

Need maybe include "Qué ofrezco" details:
- CRM turístico: leads, prospectos, clientes, pipeline, actividades, historial, segmentación.
- Cotización rápida: plantillas por destino/paquete, productos/servicios, tarifas, márgenes, conversión a reserva/venta, PDF/WhatsApp/email, seguimiento de cotización, aprobaciones.
- Gestión de vendedores: asignación, seguimiento, recordatorios, tareas, oportunidades, comisiones maybe optional.
- Reportes: ventas, conversión, cotizaciones, desempeño, destinos más vendidos.
- Onboarding: 2 semanas gratis: configuración inicial, carga de productos/plantillas, usuarios, capacitación, acompañamiento.
- Soporte: include? Need specify maybe standard support. User didn't mention support. Could include "soporte estándar incluido" but maybe assume. Need be careful. Since plan professional likely includes support? Could say "soporte incluido según plan" without specifics. Or include "soporte por correo/chat en horario hábil". But if not given, maybe mark as to confirm. However proposal needs offer. Could include "onboarding gratis 2 semanas" and subscription. Could mention "soporte estándar incluido" as assumption? Better to state "incluye soporte estándar de la plataforma; alcance exacto a definir en contrato." But maybe too vague. Could include "Soporte y actualizaciones incluidas" as typical SaaS. Need maybe not invent. Could say: "Incluye acceso a la plataforma, actualizaciones y soporte estándar (canales y SLA a confirmar)." That's safe.

Need include implementation timeline:
Semana 1: kickoff, relevamiento, configuración de usuarios, carga de catálogo básico, plantillas de cotización.
Semana 2: capacitación, pruebas, ajustes, salida en vivo.
Post onboarding: adopción y soporte.

Need include pricing table:
Plan Profesional:
- Precio lista: $89/user/month.
- Annual with 15% discount: $75.65/user/month equivalent.
- Minimum 10 users.
- Onboarding 2 weeks: $0 (incluido).
- Contrato anual.
Maybe show annual billing or monthly? "contrato anual con 15% descuento". Could present payment options: annual upfront? or monthly? Need maybe clarify: discount applies to annual contract. Could say "Facturación anual: $907.80 por usuario/año" or "mensual con contrato anual: $75.65 por usuario/mes". Need maybe if paid annually upfront, total. Could include both.

Scenarios:
Usuarios | Precio mensual con descuento | Precio anual con descuento | Ahorro vs lista anual | Costo competidor anual | Ahorro vs competidor
10: $756.50, $9,078, $1,602, $14,400, $5,322
15: $1,134.75, $13,617, $2,403, $21,600, $7,983
20: $1,513, $18,156, $3,204, $28,800, $10,644
30: $2,269.50, $27,234, $4,806, $43,200, $15,966
Need maybe calculations: list annual per user 1068; discounted annual 907.80; competitor annual per user 1440. Savings per user vs competitor = 532.20 (36.96%). Could mention.


## Respuesta completa

We need answer in Spanish. User provided pricing details. Need produce final proposal. Need maybe calculate pricing. Let's analyze.

User: agency mediana 30 empleados Lima. CRM with quick quote module. They want know what offers and price. Now provided: Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% descuento. Incluye onboarding gratis 2 semanas. Tienen competidor actual que cobra $120/usuario sin onboarding.

Need create propuesta commercial probably ready to send. Need maybe calculate for 10 users minimum and maybe for 30? But not all employees users. Need recommend number of users. Could include scenarios: 10, 15, 20, 30? Since 30 employees, likely users are salespeople + ops + managers. Need maybe ask? But now enough to draft with pricing. Could assume proposal based on minimum 10 users, but maybe client needs more. We can include scalable table: 10 usuarios minimum, recommended 12-15? Need not over-assume. We can state: "He preparado la propuesta con base en 10 usuarios (mínimo), y escenarios de 15/20 para cubrir vendedores, operaciones y supervisión." But if we assume 10, okay because pricing minimum. Maybe include "si todos los 30 empleados usan, precio 30 usuarios". But likely not all.

Need calculate:
Monthly list per user $89. Annual contract 15% discount. Discounted monthly per user = 89 * 0.85 = $75.65. Annual per user = 75.65*12 = $907.80. List annual = 89*12 = $1068; discount = $160.20; final $907.80.
For 10 users: monthly discounted = $756.50; annual = $9,078.00. Without discount: $890 monthly, $10,680 annual. Savings $1,602.
For 15: monthly discounted = 15*75.65 = $1,134.75; annual = $13,617.00. Without discount: $1,335 monthly, $16,020 annual. Savings $2,403.
For 20: monthly = $1,513.00; annual = $18,156.00. Without discount: $1,780 monthly, $21,360 annual. Savings $3,204.
For 30: monthly = $2,269.50; annual = $27,234.00. Without discount: $2,670 monthly, $32,040 annual. Savings $4,806.
Competitor: $120/user/month. For 10 users: $1200/mo, $14,400/year. Our discounted annual: $9,078/year. Savings vs competitor: $5,322/year (36.96% less? 5322/14400=36.96%). Plus free onboarding 2 weeks. If competitor charges $120 and no onboarding, maybe onboarding cost separate. For 15: competitor $1800/mo, $21,600/year; ours $13,617, savings $7,983 (36.96%). For 20: competitor $2400/mo, $28,800/year; ours $18,156, savings $10,644. For 30: competitor $3600/mo, $43,200/year; ours $27,234, savings $15,966.

Need maybe mention currency USD. In Lima maybe USD? User used $. Could state "Los precios están en USD". Need maybe include taxes? Usually not included. Need mention if IGV/IVA not included? In Peru, prices may include IGV? For B2B software maybe no? Need avoid assumption? Could state "Precios no incluyen impuestos locales salvo indicación". But maybe we need assume. We can include "Los precios están expresados en USD y no incluyen impuestos". That's a commercial assumption; we can state. Or ask? It's not material? Could be. But to make proposal, include standard clause: "Precios en USD, no incluyen IGV/impuestos; de ser requerido, se agregarán." That is safe.

Need maybe include comparison table vs competitor. Need emphasize onboarding gratis 2 semanas. Need maybe ROI: time saved, faster quotes, conversion. Could include value proposition.

Need produce final proposal: formal but concise enough. Could be lengthy. Desired oververbosity 9. Need include all.

Need maybe include "Supuestos" about number of users. Since 30 employees but users unknown. We can present recommended: 10, 15, 20, 30. Maybe propose initial 10 users with option to scale. For a travel agency with 30 employees, likely 10-15 vendedores, plus operations/admin. Could say: "Recomendado iniciar con 12-15 usuarios si el equipo comercial y de operaciones usará el CRM; el mínimo contractual es 10." But we don't know. Include scenarios.

Need maybe include "Qué ofrezco" details:
- CRM turístico: leads, prospectos, clientes, pipeline, actividades, historial, segmentación.
- Cotización rápida: plantillas por destino/paquete, productos/servicios, tarifas, márgenes, conversión a reserva/venta, PDF/WhatsApp/email, seguimiento de cotización, aprobaciones.
- Gestión de vendedores: asignación, seguimiento, recordatorios, tareas, oportunidades, comisiones maybe optional.
- Reportes: ventas, conversión, cotizaciones, desempeño, destinos más vendidos.
- Onboarding: 2 semanas gratis: configuración inicial, carga de productos/plantillas, usuarios, capacitación, acompañamiento.
- Soporte: include? Need specify maybe standard support. User didn't mention support. Could include "soporte estándar incluido" but maybe assume. Need be careful. Since plan professional likely includes support? Could say "soporte incluido según plan" without specifics. Or include "soporte por correo/chat en horario hábil". But if not given, maybe mark as to confirm. However proposal needs offer. Could include "onboarding gratis 2 semanas" and subscription. Could mention "soporte estándar incluido" as assumption? Better to state "incluye soporte estándar de la plataforma; alcance exacto a definir en contrato." But maybe too vague. Could include "Soporte y actualizaciones incluidas" as typical SaaS. Need maybe not invent. Could say: "Incluye acceso a la plataforma, actualizaciones y soporte estándar (canales y SLA a confirmar)." That's safe.

Need include implementation timeline:
Semana 1: kickoff, relevamiento, configuración de usuarios, carga de catálogo básico, plantillas de cotización.
Semana 2: capacitación, pruebas, ajustes, salida en vivo.
Post onboarding: adopción y soporte.

Need include pricing table:
Plan Profesional:
- Precio lista: $89/user/month.
- Annual with 15% discount: $75.65/user/month equivalent.
- Minimum 10 users.
- Onboarding 2 weeks: $0 (incluido).
- Contrato anual.
Maybe show annual billing or monthly? "contrato anual con 15% descuento". Could present payment options: annual upfront? or monthly? Need maybe clarify: discount applies to annual contract. Could say "Facturación anual: $907.80 por usuario/año" or "mensual con contrato anual: $75.65 por usuario/mes". Need maybe if paid annually upfront, total. Could include both.

Scenarios:
Usuarios | Precio mensual con descuento | Precio anual con descuento | Ahorro vs lista anual | Costo competidor anual | Ahorro vs competidor
10: $756.50, $9,078, $1,602, $14,400, $5,322
15: $1,134.75, $13,617, $2,403, $21,600, $7,983
20: $1,513, $18,156, $3,204, $28,800, $10,644
30: $2,269.50, $27,234, $4,806, $43,200, $15,966
Need maybe calculations: list annual per user 1068; discounted annual 907.80; competitor annual per user 1440. Savings per user vs competitor = 532.20 (36.96%). Could mention.