# Inkling Small — agent_long_horizon/clarification_quality

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 103.796s | tokens_per_second: 107.9
- input_tokens: 4650 | output_tokens: 10374

## Conversación completa (4 turnos)

### Turno 1 — usuario

Necesito que me hagas la propuesta.

### Turno 1 — modelo

Antes de redactarla, necesito aclarar porque “la propuesta” puede ser muy distinta según el contexto y cambiaría por completo el resultado:

1. **¿Qué tipo de propuesta necesitas?** (ej. propuesta de negocio/inversión, propuesta comercial a un cliente, propuesta de proyecto/servicio, plan de negocio, etc.)
2. **¿Para qué contexto o industria?** (ej. startup de tecnología, consultoría, producto físico, evento, etc.)
3. **¿A quién va dirigida?** (inversor, cliente potencial, socio, entidad pública, etc.)
4. **¿Qué debe incluir obligatoriamente?** (resumen ejecutivo, análisis de mercado, modelo de ingresos, cronograma, presupuesto, propuesta de valor, etc.)
5. **¿Hay algún dato o restricción clave que deba incorporar?** (monto solicitado, fechas límite, tono formal/informal, extensión aproximada)

Si prefieres que asuma, dímelo explícitamente y te declaro mi suposición (por ejemplo: “asumo que es una propuesta comercial de servicios para un cliente B2B con estructura estándar”). ¿Cuál es tu caso?

### Turno 2 — usuario

Es una propuesta comercial. Para un cliente nuevo. Yo vendo software.

### Turno 2 — modelo

Hay ambigüedades que cambian por completo el documento, así que te pregunto antes de tirar un borrador definitivo:

1. **¿Qué software es exactamente?** (SaaS, licencia, desarrollo a medida, consultoría + tool, etc.) y **¿para qué industria/cliente?**  
2. **¿El cliente ya expresó un problema concreto o es un acercamiento frío?** (Esto define si incluyo diagnóstico o solo presentación).  
3. **¿Qué debe incluir obligatoriamente?** (Precio/estimación, cronograma de implementación, términos, demo, contrato modelo, etc.).

**Si prefieres que avance ya**, declaro mi suposición explícita:  
*Asumo que buscas una **propuesta comercial B2B para un cliente nuevo**, de tipo **SaaS / software de gestión o automatización**, con objetivo de **presentar la solución y agendar cierre/demo** (no un contrato final). Asumo que no tienes precio definitivo ni cronograma técnico cerrado, así que uso **[placeholders]** para que los rellenes.*

Aquí va el borrador estructurado con esa suposición:

---

**ASUNTO:** Propuesta comercial — [Nombre del Software] para [Nombre Cliente / Sector]

**Estimado/a [Nombre del contacto / Equipo de [Cliente]]:**

Tras nuestra [reunión / llamada / intercambio inicial], entendemos que su operación enfrenta **[problema clave: ej. dispersión de datos, procesos manuales, falta de visibilidad, escalabilidad limitada]**. Esto impacta directamente en **[métrica: tiempo, costos, errores, experiencia del cliente]**.

Por eso, proponemos la implementación de **[Nombre del Software / Plataforma]**, una solución diseñada para **[función principal: ej. centralizar la gestión de proyectos / automatizar flujos / integrar sistemas]**.

### 1. Propuesta de valor / Qué resolvemos
- **Diagnóstico inicial:** Mapeo de su proceso actual y puntos de fricción.
- **Configuración / Integración:** Adaptación a su flujo de trabajo (APIs, importación de datos, roles).
- **Capacitación:** Sesiones para su equipo clave.
- **Soporte / Evolución:** [Período de acompañamiento / SLAs].

### 2. Alcance sugerido (ejemplo de entregables)
| Fase | Entregable / Actividad | Plazo estimado |
|---|---|---|
| 1 | Diagnóstico y diseño de solución | [X semanas] |
| 2 | Implementación / Configuración | [X semanas] |
| 3 | Capacitación y puesta en marcha | [X semanas] |
| 4 | Acompañamiento inicial | [X meses] |

### 3. Inversión / Modelo (completar según tu caso)
- **Opción A — Licencia / Suscripción:** Desde **[Monto] / mes o usuario** (escala según volumen).
- **Opción B — Proyecto de implementación:** **[Monto]** (incluye configuración, integración y capacitación).
- **Opción C — Mixta:** Cuota inicial de puesta en marcha + suscripción mensual.

> *Nota: El monto final se ajustará tras el diagnóstico inicial y según el alcance definitivo.*

### 4. Beneficios esperados para [Cliente]
- Reducción de **[X %]** en tiempo de [proceso].
- Elimación de errores manuales / duplicidad de información.
- Escalabilidad sin aumentar proporcionalmente la plantilla operativa.
- Visibilidad en tiempo real de **[métrica clave]**.

### 5. Próximos pasos
Para avanzar, sugiero:
1. **Reunión de alineación técnica** (30 min) para validar el diagnóstico.
2. **Demo / Prueba piloto** con datos reales (si aplica).
3. **Firma de propuesta / Contrato** y inicio de fase 1.

Quedo atento a sus comentarios o a una fecha para la reunión. Estoy disponible para ajustar alcances, plazos o el modelo de inversión según sus prioridades.

Un cordial saludo,  
**[Tu nombre]**  
**[Cargo]** | **[Empresa / Software]**  
**[Contacto / Web]**

---

**¿Cómo lo adaptamos?** Si me dices:
- El **nombre del software / el problema específico**,
- Si hay **precio o fechas reales**,
- Si es **B2B enterprise, PYME o un nicho específico**,

retrabajo este borrador para que suene como una propuesta real, no una plantilla. ¿Cuál es tu caso?

### Turno 3 — usuario

Es una agencia de viajes mediana, 30 empleados, en Lima. Mi software es un CRM con módulo de cotización rápida para vendedores de turismo. Quieren saber qué les ofrezco y precio.

### Turno 3 — modelo

Antes de entregarte el documento definitivo, declaro mis suposiciones explícitas porque afectan el precio y el alcance:

- **Asumo** que es una propuesta comercial formal (no contrato) para una agencia de viajes de Lima con ~30 empleados, dirigida al gerente o jefe de ventas.
- **Asumo** que tu CRM es **SaaS** (suscripción mensual por usuario) con una fase de implementación inicial; no es una licencia única ni un desarrollo a medida.
- **Asumo** que el equipo que usará el CRM es el de ventas (ej. 8–12 personas de un total de 30); si es toda la agencia, el precio cambia.
- **Asumo** que el precio debe ser concreto para que decidan; presento un modelo con cifras de referencia del mercado LATAM (B2B para pymes de servicios), pero marcadas como ejemplo para que las ajustes.

Si tu modelo es distinto (precio fijo por agencia, incluye integración con GDS/Amadeus, o es solo un documento de acercamiento sin implementación), dime y corrijo la sección 3.

---

**PROPUESTA COMERCIAL**
**Para:** [Nombre de la Agencia / Gerente General / Jefe de Ventas]  
**De:** [Tu nombre / Tu Agencia de Software]  
**Fecha:** [Fecha]  
**Asunto:** Propuesta — CRM + Módulo de Cotización Rápida para tu equipo de ventas

---

### 1. Entendemos su operación
Agencia de viajes mediana en Lima, ~30 colaboradores, con un equipo comercial que hoy probablemente gestiona cotizaciones de paquetes turísticos, vuelos y hoteles entre Excel, WhatsApp y correos. Eso genera:
- Tiempos de respuesta lentos (horas para armar una cotización).
- Errores de precios, fechas y condiciones entre vendedores.
- Pérdida de seguimientos (no se sabe quién contactó a qué cliente).
- Falta de visibilidad para el gerente: ¿cuántas cotizaciones se envían? ¿cuál es la tasa de cierre?

---

### 2. Qué les ofrecemos (el alcance)
No solo un CRM: una **plataforma de ventas de turismo** con módulo de cotización rápida.

| Componente | Qué incluye para una agencia de viajes |
|---|---|
| **CRM de ventas** | Pipeline visual: Consulta → Cotización → Negociación → Reserva → Post-venta. Historial completo por cliente (viajes pasados, preferencias, documentos). |
| **Módulo Cotización Rápida** | Plantillas por tipo de producto (paquete, vuelo+hotel, grupo). Cálculo automático de precios, descuentos y condiciones. Generación de PDF o WhatsApp en minutos. |
| **Base de proveedores / tarifas** | Registro de proveedores, tarifas vigentes y vigencias. Evita que el vendedor use una tarifa vieja. |
| **Integraciones básicas** | WhatsApp Business / Email / Calendario (para que el vendedor no salga del CRM). Si usas Excel hoy, importamos tu base de clientes y proveedores. |
| **App móvil** | El vendedor puede cotizar y actualizar el pipeline desde el celular o en reuniones con clientes. |
| **Dashboard para gerencia** | Conversión de cotizaciones, ingreso proyectado, mejor vendedor, destinos más cotizados, tiempo promedio de cierre. |
| **Implementación** | Configuración inicial, migración de datos (clientes, proveedores, tarifas base), capacitación para el equipo de ventas y 3 meses de acompañamiento intensivo. |

---

### 3. Inversión / Precio (modelo sugerido)
**Nota:** Este es un modelo de referencia para una agencia de este tamaño. Si tu software tiene otro esquema, reemplázalo.

| Concepto | Detalle | Monto estimado |
|---|---|---|
| **Implementación y Configuración** | Setup, migración de datos, integración básica, capacitación inicial (equipo de ventas) | **$1,500 – $2,500 USD** (one-time) |
| **Suscripción mensual** | Por usuario activo (vendedor / asistente de ventas) | **$30 – $45 USD / usuario / mes** |
| **Ejemplo práctico** | 10 usuarios (equipo de ventas) + implementación | **$300 – $450 USD / mes + $1,500 – $2,500 USD inicial** |

**Opciones de pago:**
- **Anual:** 15–20 % de descuento sobre la suscripción mensual (ej. $3,600 – $5,400 USD/año por 10 usuarios, sin contar setup).
- **Pago inicial:** Setup al inicio; suscripción mensual o trimestral.

> **Ajuste:** Si necesitas que el CRM se conecte con un GDS (Amadeus, Galileo, etc.) o con un sistema contable específico, el setup puede variar. Si prefieres un precio fijo por agencia sin importar usuarios, indícamelo y lo reestructuro.

---

### 4. Beneficios específicos para su agencia
1. **Velocidad:** De horas a minutos para entregar una propuesta de viaje.
2. **Precisión:** El precio y las fechas salen del sistema, no de un cálculo manual.
3. **Seguimiento:** El gerente sabe en qué etapa está cada cliente y qué vendedor lo atiende.
4. **Repetición:** Al tener el historial, pueden ofrecer paquetes personalizados a clientes de viajes anteriores.
5. **Escalabilidad:** Si crecen a 15 o 20 vendedores, solo se agregan usuarios; no se redepliega el sistema.

---

### 5. Próximos pasos propuestos
1. **Reunión de validación (30 min):** Confirmamos cuántos vendedores usarán el CRM, qué datos hoy manejan (Excel, WhatsApp, etc.) y si hay integración con algún proveedor o sistema contable.
2. **Demo personalizada:** Mostramos la cotización rápida con un ejemplo real de su catálogo (destino, fechas, pasajeros).
3. **Propuesta técnica y contrato:** Ajustamos alcance, precio final según número de usuarios y fechas de inicio.
4. **Inicio:** Configuración + capacitación en 2–3 semanas.

---

Quedo atento a confirmar:
- ¿Cuántos vendedores / usuarios usarán el CRM? (Esto define la sección 3 exactamente).
- ¿Hay algún sistema actual que deba integrarse (Excel, software contable, proveedor de vuelos)?
- ¿Prefieres que sea propuesta por correo, documento PDF o presentación en vivo?

Si me confirmas esos puntos, te entrego la versión final con precios exactos y sin placeholders. ¿Ajustamos?

### Turno 4 — usuario

Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% de descuento. Incluye onboarding gratis 2 semanas. Tienen un competidor actual que cobra $120/usuario sin onboarding.

### Turno 4 — modelo

**Declaración de suposición:** Asumo que deseas la propuesta final dirigida al gerente/jefe de ventas de la agencia de viajes de Lima (~30 empleados), integrando exactamente lo que acabas de definir: **Plan Profesional a $89 USD/usuario/mes**, **mínimo 10 usuarios**, **contrato anual con 15 % de descuento**, **onboarding gratuito de 2 semanas**, y una **sección comparativa frente al competidor ($120/usuario, sin onboarding)**. Asumo que los precios son en USD y que el onboarding cubre configuración inicial, migración básica y capacitación del equipo de ventas.

---

# PROPUESTA COMERCIAL
**Plan Profesional — CRM + Módulo de Cotización Rápida para Ventas de Turismo**

**Para:** [Nombre del Gerente / Jefe de Ventas / Agencia de Viajes — Lima]  
**De:** [Tu nombre / Tu empresa de software]  
**Fecha:** [Fecha]  
**Asunto:** Propuesta de implementación — Plan Profesional (10 usuarios mínimo)

---

## 1. Entendemos su operación
Agencia de viajes mediana en Lima, ~30 colaboradores, con un equipo comercial que hoy arma cotizaciones de paquetes turísticos, vuelos y hoteles entre Excel, WhatsApp y correos. Eso genera:
- Respuesta lenta al cliente (horas para armar una propuesta).
- Errores de precios, fechas y condiciones entre vendedores.
- Seguimientos perdidos (no se sabe quién atendió a qué cliente).
- Falta de visibilidad gerencial: ¿cuántas cotizaciones se envían? ¿cuál es la tasa de cierre?

---

## 2. Lo que les ofrecemos: Plan Profesional
No es solo un CRM. Es una **plataforma de ventas de turismo** para que sus vendedores coticen, negocien y cierren más rápido.

| Componente | Qué incluye para su agencia |
|---|---|
| **CRM de ventas** | Pipeline visual por cliente (consulta → cotización → negociación → reserva → post-venta). Historial completo: viajes pasados, preferencias, documentos. |
| **Módulo Cotización Rápida** | Plantillas por producto (paquete, vuelo+hotel, grupo). Cálculo automático de precios, descuentos y condiciones. PDF / WhatsApp en minutos. |
| **Tarifas y proveedores** | Registro de proveedores, tarifas vigentes y fechas de vigencia. Evita usar una tarifa vieja. |
| **Integraciones básicas** | WhatsApp Business, correo electrónico, calendario. Importación de su base actual (clientes, proveedores, tarifas base). |
| **App móvil** | Cotizar y actualizar el pipeline desde el celular, incluso en reuniones con clientes o en la agencia. |
| **Dashboard gerencial** | Conversión de cotizaciones, ingreso proyectado, mejor vendedor, destinos más cotizados, tiempo promedio de cierre. |
| **Onboarding (incluido)** | **2 semanas de configuración inicial, migración de datos y capacitación del equipo de ventas.** Sin costo adicional. |

---

## 3. Inversión — Plan Profesional
**Tarifa de lista:** **$89 USD por usuario / mes**  
**Compromiso:** **10 usuarios mínimos** (equipo de ventas)  
**Contrato:** **Anual con 15 % de descuento** sobre el total anual.

| Concepto | Cálculo | Monto |
|---|---|---|
| **Mensual (sin descuento)** | 10 usuarios × $89 | **$890 USD / mes** |
| **Anual (sin descuento)** | $890 × 12 meses | $10,680 USD / año |
| **Anual con 15 % de descuento** | $10,680 × 0.85 | **$9,078 USD / año** |
| **Equivalente mensual (anual)** | $9,078 ÷ 12 | **$756.50 USD / mes** |
| **Equivalente por usuario/mes** | $756.50 ÷ 10 | **$75.65 USD / usuario / mes** |

> **Nota:** El onboarding de 2 semanas está incluido en la inversión inicial. No hay cargo extra por implementación básica ni capacitación inicial.

**Condiciones del contrato anual:**
- Duración: 12 meses.
- Mínimo: 10 usuarios activos.
- Facturación: mensual o anual (si elige anual, aplica el 15 % de descuento).
- Renovación: automática con 30 días de aviso; se mantiene la tarifa anual si se renovó sin interrupciones.

---

## 4. Comparativa directa vs. su competidor actual
| Característica | **Su competidor actual** | **Nuestro Plan Profesional** |
|---|---|---|
| **Tarifa por usuario / mes** | $120 USD | **$89 USD** (lista) / **$75.65 USD** (equivalente anual) |
| **Onboarding / Implementación** | **No incluido** (costo extra o auto-servicio) | **2 semanas gratis** (configuración + capacitación) |
| **Compromiso mínimo** | No especificado / variable | **10 usuarios** (escala con su equipo de ventas) |
| **Descuento por anualidad** | No indicado | **15 % de descuento** |
| **Módulo de cotización rápida** | No especificado | **Incluido** (diseñado para turismo) |
| **Dashboard gerencial** | No especificado | **Incluido** |

**Resultado:** Por 10 usuarios, en un año usted paga **$9,078 USD** con onboarding incluido, versus **$14,400 USD** (10 usuarios × $120 × 12 meses) sin onboarding ni descuento. Eso representa un **ahorro de $5,322 USD anuales** y una puesta en marcha acompañada.

---

## 5. Onboarding incluido (2 semanas)
Para que no pierda tiempo ni dinero en aprender el sistema:
- **Semana 1:** Configuración de la cuenta, migración de su base de clientes/proveedores, creación de plantillas de cotización para sus productos turísticos.
- **Semana 2:** Capacitación práctica con su equipo de ventas (2 sesiones de 90 min + material de apoyo), prueba de cotización real con un cliente de ejemplo, ajuste de permisos y roles.

Después de las 2 semanas: **acompañamiento prioritario** durante los primeros 30 días de uso real.

---

## 6. Términos clave del contrato
- **Plan:** Profesional (CRM + Cotización Rápida).
- **Usuarios:** 10 mínimos; puede agregar usuarios adicionales a $89 USD/mes (o a la tarifa anual proporcional si mantiene el contrato anual).
- **Duración:** 12 meses.
- **Pago:** Mensual o anual (15 % descuento si es anual).
- **Cancelación:** No aplica durante el año; renovación anual con 30 días de aviso.
- **Datos:** Usted conserva la propiedad de sus datos; pueden exportarse al finalizar.

---

## 7. Próximos pasos propuestos
1. **Confirmación de alcance:** ¿Cuántos vendedores usarán el CRM? ¿Hay algún sistema contable o proveedor de vuelos que deba conectarse?
2. **Demo personalizada (30 min):** Mostramos la cotización rápida con un ejemplo real de su catálogo (destino, fechas, pasajeros, precios).
3. **Firma de propuesta / contrato:** Ajustamos el número final de usuarios y fecha de inicio.
4. **Inicio del onboarding:** Configuración inmediata; capacitación en 2 semanas.

---

**¿Confirmamos el número exacto de usuarios y la fecha de inicio?** Con eso, paso esta propuesta a contrato con precios y fechas definitivas.

Quedo atento.  
**[Tu nombre]**  
**[Cargo / Empresa]**  
**[Contacto / Email / WhatsApp]**  
**Lima, [Fecha]**

---

**¿Necesitas que adapte esto a un formato PDF/visual, que agregue una página de "Preguntas frecuentes" o que calcule el precio si son 12 usuarios en lugar de 10?** Dime y lo ajusto inmediatamente.


## Respuesta completa

**Declaración de suposición:** Asumo que deseas la propuesta final dirigida al gerente/jefe de ventas de la agencia de viajes de Lima (~30 empleados), integrando exactamente lo que acabas de definir: **Plan Profesional a $89 USD/usuario/mes**, **mínimo 10 usuarios**, **contrato anual con 15 % de descuento**, **onboarding gratuito de 2 semanas**, y una **sección comparativa frente al competidor ($120/usuario, sin onboarding)**. Asumo que los precios son en USD y que el onboarding cubre configuración inicial, migración básica y capacitación del equipo de ventas.

---

# PROPUESTA COMERCIAL
**Plan Profesional — CRM + Módulo de Cotización Rápida para Ventas de Turismo**

**Para:** [Nombre del Gerente / Jefe de Ventas / Agencia de Viajes — Lima]  
**De:** [Tu nombre / Tu empresa de software]  
**Fecha:** [Fecha]  
**Asunto:** Propuesta de implementación — Plan Profesional (10 usuarios mínimo)

---

## 1. Entendemos su operación
Agencia de viajes mediana en Lima, ~30 colaboradores, con un equipo comercial que hoy arma cotizaciones de paquetes turísticos, vuelos y hoteles entre Excel, WhatsApp y correos. Eso genera:
- Respuesta lenta al cliente (horas para armar una propuesta).
- Errores de precios, fechas y condiciones entre vendedores.
- Seguimientos perdidos (no se sabe quién atendió a qué cliente).
- Falta de visibilidad gerencial: ¿cuántas cotizaciones se envían? ¿cuál es la tasa de cierre?

---

## 2. Lo que les ofrecemos: Plan Profesional
No es solo un CRM. Es una **plataforma de ventas de turismo** para que sus vendedores coticen, negocien y cierren más rápido.

| Componente | Qué incluye para su agencia |
|---|---|
| **CRM de ventas** | Pipeline visual por cliente (consulta → cotización → negociación → reserva → post-venta). Historial completo: viajes pasados, preferencias, documentos. |
| **Módulo Cotización Rápida** | Plantillas por producto (paquete, vuelo+hotel, grupo). Cálculo automático de precios, descuentos y condiciones. PDF / WhatsApp en minutos. |
| **Tarifas y proveedores** | Registro de proveedores, tarifas vigentes y fechas de vigencia. Evita usar una tarifa vieja. |
| **Integraciones básicas** | WhatsApp Business, correo electrónico, calendario. Importación de su base actual (clientes, proveedores, tarifas base). |
| **App móvil** | Cotizar y actualizar el pipeline desde el celular, incluso en reuniones con clientes o en la agencia. |
| **Dashboard gerencial** | Conversión de cotizaciones, ingreso proyectado, mejor vendedor, destinos más cotizados, tiempo promedio de cierre. |
| **Onboarding (incluido)** | **2 semanas de configuración inicial, migración de datos y capacitación del equipo de ventas.** Sin costo adicional. |

---

## 3. Inversión — Plan Profesional
**Tarifa de lista:** **$89 USD por usuario / mes**  
**Compromiso:** **10 usuarios mínimos** (equipo de ventas)  
**Contrato:** **Anual con 15 % de descuento** sobre el total anual.

| Concepto | Cálculo | Monto |
|---|---|---|
| **Mensual (sin descuento)** | 10 usuarios × $89 | **$890 USD / mes** |
| **Anual (sin descuento)** | $890 × 12 meses | $10,680 USD / año |
| **Anual con 15 % de descuento** | $10,680 × 0.85 | **$9,078 USD / año** |
| **Equivalente mensual (anual)** | $9,078 ÷ 12 | **$756.50 USD / mes** |
| **Equivalente por usuario/mes** | $756.50 ÷ 10 | **$75.65 USD / usuario / mes** |

> **Nota:** El onboarding de 2 semanas está incluido en la inversión inicial. No hay cargo extra por implementación básica ni capacitación inicial.

**Condiciones del contrato anual:**
- Duración: 12 meses.
- Mínimo: 10 usuarios activos.
- Facturación: mensual o anual (si elige anual, aplica el 15 % de descuento).
- Renovación: automática con 30 días de aviso; se mantiene la tarifa anual si se renovó sin interrupciones.

---

## 4. Comparativa directa vs. su competidor actual
| Característica | **Su competidor actual** | **Nuestro Plan Profesional** |
|---|---|---|
| **Tarifa por usuario / mes** | $120 USD | **$89 USD** (lista) / **$75.65 USD** (equivalente anual) |
| **Onboarding / Implementación** | **No incluido** (costo extra o auto-servicio) | **2 semanas gratis** (configuración + capacitación) |
| **Compromiso mínimo** | No especificado / variable | **10 usuarios** (escala con su equipo de ventas) |
| **Descuento por anualidad** | No indicado | **15 % de descuento** |
| **Módulo de cotización rápida** | No especificado | **Incluido** (diseñado para turismo) |
| **Dashboard gerencial** | No especificado | **Incluido** |

**Resultado:** Por 10 usuarios, en un año usted paga **$9,078 USD** con onboarding incluido, versus **$14,400 USD** (10 usuarios × $120 × 12 meses) sin onboarding ni descuento. Eso representa un **ahorro de $5,322 USD anuales** y una puesta en marcha acompañada.

---

## 5. Onboarding incluido (2 semanas)
Para que no pierda tiempo ni dinero en aprender el sistema:
- **Semana 1:** Configuración de la cuenta, migración de su base de clientes/proveedores, creación de plantillas de cotización para sus productos turísticos.
- **Semana 2:** Capacitación práctica con su equipo de ventas (2 sesiones de 90 min + material de apoyo), prueba de cotización real con un cliente de ejemplo, ajuste de permisos y roles.

Después de las 2 semanas: **acompañamiento prioritario** durante los primeros 30 días de uso real.

---

## 6. Términos clave del contrato
- **Plan:** Profesional (CRM + Cotización Rápida).
- **Usuarios:** 10 mínimos; puede agregar usuarios adicionales a $89 USD/mes (o a la tarifa anual proporcional si mantiene el contrato anual).
- **Duración:** 12 meses.
- **Pago:** Mensual o anual (15 % descuento si es anual).
- **Cancelación:** No aplica durante el año; renovación anual con 30 días de aviso.
- **Datos:** Usted conserva la propiedad de sus datos; pueden exportarse al finalizar.

---

## 7. Próximos pasos propuestos
1. **Confirmación de alcance:** ¿Cuántos vendedores usarán el CRM? ¿Hay algún sistema contable o proveedor de vuelos que deba conectarse?
2. **Demo personalizada (30 min):** Mostramos la cotización rápida con un ejemplo real de su catálogo (destino, fechas, pasajeros, precios).
3. **Firma de propuesta / contrato:** Ajustamos el número final de usuarios y fecha de inicio.
4. **Inicio del onboarding:** Configuración inmediata; capacitación en 2 semanas.

---

**¿Confirmamos el número exacto de usuarios y la fecha de inicio?** Con eso, paso esta propuesta a contrato con precios y fechas definitivas.

Quedo atento.  
**[Tu nombre]**  
**[Cargo / Empresa]**  
**[Contacto / Email / WhatsApp]**  
**Lima, [Fecha]**

---

**¿Necesitas que adapte esto a un formato PDF/visual, que agregue una página de "Preguntas frecuentes" o que calcule el precio si son 12 usuarios en lugar de 10?** Dime y lo ajusto inmediatamente.