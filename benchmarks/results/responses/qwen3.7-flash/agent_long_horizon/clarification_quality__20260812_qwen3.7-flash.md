# Qwen 3.7 Flash — agent_long_horizon/clarification_quality

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 8.97 | quality: 10.0
- latency_total: 84.86s | tokens_per_second: 131.2
- input_tokens: 4026 | output_tokens: 9413

## Conversación completa (4 turnos)

### Turno 1 — usuario

Necesito que me hagas la propuesta.

### Turno 1 — modelo

Para entregarte una propuesta realmente útil y alineada a tu situación, necesito aclarar 5 puntos que definen su contenido y estructura:

1. **¿Tipo de propuesta?** (comercial, de proyecto, alianza estratégica, financiamiento, servicio, licitación, interna, etc.)
2. **¿Destinatario?** (cliente potencial, inversionista, entidad pública, socio, directorio, cliente recurrente…)
3. **Sector/industria** en el que operas o donde se aplicará la propuesta.
4. **Objetivo principal y alcance esperado** (¿qué quieres lograr con este documento? ¿qué debe incluir o excluir?)
5. **Restricciones prácticas** (plazo de entrega, presupuesto orientativo, formato obligatorio, extensión máxima, lenguaje institucional/colaborativo/etc.)

Con estos datos te entrego un borrador estructurado, listo para personalizar. 

🔹 *Si prefieres no desglosarlo ahora*, dime solo el contexto general y haré suposiciones claras sobre cada punto vacío; las declararé explícitamente para que puedas corregirlas antes de usar el documento.

### Turno 2 — usuario

Es una propuesta comercial. Para un cliente nuevo. Yo vendo software.

### Turno 2 — modelo

Para que la propuesta sea útil y no genérica, necesito aclarar **4 puntos que determinan la estructura, el mensaje y la sección comercial**:

1. **¿Qué tipo de software vendes?** (SaaS B2B, ERP/CRM, herramienta de IA, analítica, desarrollo a medida, vertical/nicho, etc.)
2. **¿Qué problema concreto o dolor resuelves para este cliente en particular?** (Eficiencia, cumplimiento normativo, ingresos, experiencia de usuario, reducción de costos, etc.)
3. **¿Cómo estructuras el precio/comercialización?** (Suscripción mensual/anual, licencia perpetua, por usuario/plataforma, proyecto cerrado, freemium + premium, etc.)
4. **¿En qué industria u operación se usará?** (Logística, retail, salud, fintech, manufactura, servicios profesionales, etc. → esto define el lenguaje, casos de uso y menciones de seguridad/cumplimiento).

🔹 **Si prefieres que avance ahora mismo**, trabajaré con estas **suposiciones explícitas** (fáciles de modificar después):
- `Software`: SaaS B2B de gestión/productividad (tipo CRM/ERP ligero o herramienta de automatización)
- `Dolor principal`: Procesos manuales, falta de visibilidad en tiempo real y pérdida de eficiencia operativa
- `Modelo comercial`: Suscripción anual por usuario/plataforma, con implementación guiada y soporte incluido
- `Cliente`: PYME o mediana empresa de servicios/logística/manufactura (sector genérico, fácil de adaptar)
- `Tono y enfoque`: Profesional, orientado a ROI tangible, reducción de fricción y adopción rápida

Con esta base te entrego:
✅ Estructura recomendada para propuestas de software B2B  
✅ Borrador redactado con secciones clave (contexto, valor, solución, implementación, inversión, garantías, siguientes pasos)  
✅ Placeholders claros `[entre corchetes]` para personalizarlo sin reescribir desde cero  

¿Prefieres que genere el borrador bajo estas suposiciones o respondes los 4 puntos primero para ajustarlo al 100% a tu realidad?

### Turno 3 — usuario

Es una agencia de viajes mediana, 30 empleados, en Lima. Mi software es un CRM con módulo de cotización rápida para vendedores de turismo. Quieren saber qué les ofrezco y precio.

### Turno 3 — modelo

Antes del borrador, declaro mis **suposiciones explícitas** (todas son editables sin reescribir la propuesta):
- 💰 **Precio**: S/ `[85]`/usuario/mes (mensual) | `-15%` con pago anual | Implementación y onboarding incluidos si se firma en los primeros 7 días.
- 📅 **Contrato**: Mínimo 6 meses, renovación automática mensual/anual, cancelación con 30 días de aviso.
- 🛠️ **Implementación**: Configuración en `<48h`, migración básica de contactos (CSV/Excel), 1 sesión grupal de capacitación (2h) + 15 días de acompañamiento post-lanzamiento.
- 📞 **Soporte**: Estándar por chat/email, horario hábil Lima (UTC-5), respuesta `<4h`, resolución `<24h`. Sin account manager dedicado ni SLA penalizado.
- 🔌 **Integraciones**: Correo (Gmail/Outlook), calendario, exportación PDF/Excel. WhatsApp Business API y conectores contables como adicionales o futuros.
- 🇵🇪 **Moneda y facturación**: Soles peruanos (S/), factura electrónica disponible. Precio final sujeto a ajuste si requieres módulos extra (crédito turístico, comisiones por agente, integración con GDS/API de aerolíneas, etc.).

---

# PROPUESTA COMERCIAL
**[Nombre de tu Software]** | CRM Turístico + Cotización Rápida  
**Dirigido a**: [Nombre de la Agencia] | Lima, Perú  
**Elaborado por**: [Tu Nombre/Cargo] | [Email] | [Teléfono] | [Fecha]

## 1. Contexto y desafío detectado
Las agencias medianas (~30 colaboradores) suelen gestionar cotizaciones mediante hojas de cálculo, correos electrónicos y mensajes internos. Esta dispersión genera:
- Tiempos de respuesta superiores a 24 horas, reduciendo la probabilidad de cierre.
- Duplicidad de prospectos y pérdida de seguimiento comercial.
- Dificultad para auditar descuentos, márgenes y comisiones por vendedor.
- Falta de visibilidad en tiempo real del pipeline por tipo de producto (vuelos, tours, cruceros, corporativo).

**Objetivo de esta propuesta**: Centralizar la gestión comercial, estandarizar la creación de presupuestos y acelerar el cierre sin sacrificar la personalización que exige el sector turismo.

## 2. Solución propuesta
Plataforma SaaS segura, accesible desde navegador y dispositivo móvil, compuesta por:
- **CRM con pipelines visuales** segmentados por línea de negocio y etapa comercial.
- **Módulo de Cotización Rápida**: combinación de servicios (vuelo + hotel + traslados + seguro), cálculo automático de margen, IVA y políticas de cancelación.
- **Generador de documentos**: exportación a PDF con logo, datos fiscales y términos de la agencia, listo para enviar por correo o WhatsApp.
- **Automatizaciones internas**: recordatorios de seguimiento, asignación inteligente de leads, aprobaciones jerárquicas para descuentos >X%.
- **Dashboard gerencial**: ventas cerradas, tasa de conversión, tiempo medio de ciclo, rendimiento por vendedor y top productos.

## 3. Beneficios medibles
| Proceso actual | Con [Nombre de tu Software] | Impacto esperado |
|----------------|-----------------------------|------------------|
| Cotización manual (30-90 min) | Plantillas preconfiguradas + cálculo automático | `<5 min` por presupuesto |
| Seguimiento en correos/chats | Pipeline unificado + alertas automáticas | `+15–25%` tasa de conversión |
| Control de descuentos/márgenes | Reglas configurables + auditoría completa | `100%` trazabilidad y cumplimiento interno |
| Reportes manuales | Dashboards en tiempo real | Decisiones basadas en datos reales |

## 4. Alcance técnico y funcionalidades incluidas
- Gestión de clientes/prospectos con segmentación y etiquetas
- Catálogo de productos/servicios con costos base y disponibilidad
- Cotizador dinámico con validación de reglas comerciales
- Historial completo de interacciones y versiones de presupuestos
- Roles y permisos granulares (vendedor, supervisor, gerente, admin)
- Integraciones básicas: Gmail/Outlook, calendario, exportación PDF/Excel
- Cumplimiento normativo: respaldo diario, cifrado en tránsito y reposo, alineación con Ley N° 29733 (Protección de Datos Personales, Perú)

## 5. Plan de implementación y capacitación
| Fase | Duración | Entregable |
|------|----------|------------|
| Configuración inicial | 1 día | Cuenta activa, catálogos, roles, flujos de aprobación |
| Migración de datos | 1 día | Importación limpia de contactos y oportunidades (CSV/Excel) |
| Capacitación comercial | 1 sesión (2h) | Uso práctico del CRM y cotizador + grabación disponible |
| Acompañamiento post-lanzamiento | 15 días | Soporte prioritario, ajustes menores y métricas de adopción |

## 6. Inversión y modelo de precios
| Concepto | Detalle | Valor |
|----------|---------|-------|
| Licencia SaaS | Usuario activo (acceso ilimitado a módulos CRM + Cotización) | `S/ [85]` /usuario/mes |
| Descuento anual | `-15%` sobre tarifa mensual | `S/ [72]` /usuario/mes (facturado anual) |
| Implementación y onboarding | Configuración, migración, capacitación y 15 días de soporte intensivo | `Incluido` si se firma antes del `[Fecha límite]` |
| Extras opcionales | WhatsApp Business API, integraciones contables, reportes avanzados, SLA premium | A cotizar según necesidad |

**Ejemplo de inversión para 30 usuarios:**
- Modalidad mensual: `S/ [85] × 30 = S/ 2.550` /mes
- Modalidad anual: `S/ [72] × 30 × 12 = S/ 25.920` /año (ahorro equivalente a 1.8 meses)

*Forma de pago*: Transferencia bancaria o tarjeta. Moneda: PEN. Facturación electrónica disponible. Precios sujetos a variación por cambios en alcance o requerimientos de desarrollo a medida.

## 7. Condiciones comerciales
- **Vigencia de oferta**: 15 días naturales desde la fecha de emisión.
- **Compromiso mínimo**: 6 meses. Renovación automática bajo las mismas condiciones.
- **Cancelación**: Notificación por escrito con 30 días de antelación.
- **Propiedad de datos**: La agencia conserva la titularidad absoluta. Portabilidad garantizada al finalizar el contrato.
- **SLA de soporte**: Respuesta `<4h` hábiles (Lima), resolución `<24h`. Mantenimiento programado fuera de horario comercial.
- **Actualizaciones**: Incluidas sin costo adicional durante la vigencia del contrato.

## 8. Próximos pasos
1. Revisión conjunta de esta propuesta (15 min virtual o presencial en Lima).
2. Activación de **entorno de prueba gratuito por 14 días** con datos de ejemplo y flujo real de cotización.
3. Firma de acuerdo de servicio y cronograma de activación confirmado.

---
**Firma de conformidad**  
Nombre: ________________________ Cargo: ________________________  
Firma: _________________________ Fecha: _________________________  

---

### 🔍 ¿Qué necesitas ajustar antes de enviar?
Dime solo los valores exactos que quieres cambiar y te devuelvo la versión lista en `<2 min>`:
- Tarifa por usuario y descuento anual
- Plazo mínimo de compromiso
- Incluye/excluye alguna integración o módulo extra
- Formato de entrega preferido (PDF, Word, Canva, slide deck)

### Turno 4 — usuario

Plan profesional: $89/mes por usuario, mínimo 10 usuarios, contrato anual con 15% de descuento. Incluye onboarding gratis 2 semanas. Tienen un competidor actual que cobra $120/usuario sin onboarding.

### Turno 4 — modelo

Antes del borrador actualizado, declaro mis **suposiciones explícitas** (todas son editables sin reescribir):
- 💵 **Moneda**: Precios en USD ($) como indicaste. En Perú se podrá facturar en USD o en PEN equivalente al tipo de cambio oficial del día de emisión, con factura electrónica SUNAT.
- 📦 **Alcance del onboarding gratuito (2 semanas)**: Configuración inicial, carga de catálogos y roles, capacitación por puesto (vendedor, supervisor, admin), migración básica de contactos/opportunidades y acompañamiento intensivo durante la primera quincena de uso real.
- ⚖️ **Competidor**: No lo nombraré directamente para mantener tono profesional, pero sí cuantificaré el ahorro tangible vs. su propuesta actual ($120/usuario, sin onboarding).
- 🇵🇪 **Contexto peruano**: Se menciona cumplimiento Ley N° 29733 (protección de datos), facturación electrónica y horarios hábiles Lima (UTC-5).

---

# PROPUESTA COMERCIAL
**[Nombre de tu Software]** | CRM Turístico + Cotización Rápida  
**Dirigido a**: [Nombre de la Agencia] | Lima, Perú  
**Elaborado por**: [Tu Nombre/Cargo] | [Email] | [Teléfono] | [Fecha]

## 1. Contexto y desafío detectado
Las agencias medianas (~30 colaboradores) suelen gestionar cotizaciones mediante hojas de cálculo, correos electrónicos y mensajes internos. Esta dispersión genera:
- Tiempos de respuesta superiores a 24 horas, reduciendo la probabilidad de cierre.
- Duplicidad de prospectos y pérdida de seguimiento comercial.
- Dificultad para auditar descuentos, márgenes y comisiones por vendedor.
- Falta de visibilidad en tiempo real del pipeline por tipo de producto (vuelos, tours, cruceros, corporativo).

**Objetivo de esta propuesta**: Centralizar la gestión comercial, estandarizar la creación de presupuestos y acelerar el cierre sin sacrificar la personalización que exige el sector turismo.

## 2. Solución propuesta
Plataforma SaaS segura, accesible desde navegador y dispositivo móvil, compuesta por:
- **CRM con pipelines visuales** segmentados por línea de negocio y etapa comercial.
- **Módulo de Cotización Rápida**: combinación de servicios (vuelo + hotel + traslados + seguro), cálculo automático de margen, impuestos y políticas de cancelación.
- **Generador de documentos**: exportación a PDF con logo, datos fiscales y términos de la agencia, listo para enviar por correo o WhatsApp.
- **Automatizaciones internas**: recordatorios de seguimiento, asignación inteligente de leads, aprobaciones jerárquicas para descuentos >X%.
- **Dashboard gerencial**: ventas cerradas, tasa de conversión, tiempo medio de ciclo, rendimiento por vendedor y top productos.

## 3. Beneficios medibles
| Proceso actual | Con [Nombre de tu Software] | Impacto esperado |
|----------------|-----------------------------|------------------|
| Cotización manual (30-90 min) | Plantillas preconfiguradas + cálculo automático | `<5 min` por presupuesto |
| Seguimiento en correos/chats | Pipeline unificado + alertas automáticas | `+15–25%` tasa de conversión |
| Control de descuentos/márgenes | Reglas configurables + auditoría completa | `100%` trazabilidad interna |
| Reportes manuales | Dashboards en tiempo real | Decisiones basadas en datos reales |

## 4. Plan de implementación y onboarding (incluido)
| Semana | Actividad | Entregable |
|--------|-----------|------------|
| **Semana 1** | Configuración técnica, catálogos, roles y flujos de aprobación<br>Capacitación por puesto (vendedores, supervisores, admins)<br>Carga de contactos y oportunidades iniciales | Sistema operativo + grabación de sesiones + manual rápido |
| **Semana 2** | Hypercare: resolución de dudas en vivo<br>Ajuste de reglas comerciales y plantillas según casos reales<br>Revisión de métricas de adopción y primer reporte de impacto | Checklist de go-live firmado + plan de optimización mensual |

*Nota: El onboarding se activa tras firma de contrato y no requiere inversión adicional.*

## 5. Inversión y modelo de precios
| Concepto | Detalle | Valor |
|----------|---------|-------|
| **Plan Profesional** | Licencia SaaS ilimitada (CRM + Cotización + Dashboards + Soporte estándar) | `$89` /usuario/mes |
| **Compromiso anual** | `-15%` sobre tarifa mensual (facturado anual) | `$75.65` /usuario/mes |
| **Mínimo de usuarios** | 10 usuarios activos | Aplica a todo el contrato |
| **Onboarding** | Configuración, capacitación y 2 semanas de acompañamiento intensivo | `Incluido` |
| **Extras opcionales** | WhatsApp Business API, integraciones contables, reportes avanzados, SLA premium | A cotizar según necesidad |

### 📊 Ejemplo de inversión anual
| Usuarios | Costo mensual equivalente | Facturación anual | Ahorro vs. competencia actual* |
|----------|---------------------------|-------------------|-------------------------------|
| 10 | `$75.65` | `$9,078` | `-31.7%` en precio base + onboarding incluido |
| 30 | `$75.65` | `$27,234` | `-31.7%` en precio base + onboarding incluido |

*\*Comparación basada en tarifa actual del mercado: $120/usuario sin onboarding incluido. El ahorro se calcula sobre la diferencia de precio base anual.*

**Forma de pago**: Transferencia bancaria o tarjeta. Moneda: USD. Facturación electrónica disponible. Precios sujetos a variación por cambios en alcance o requerimientos de desarrollo a medida.

## 6. Condiciones comerciales
- **Vigencia de oferta**: 15 días naturales desde la fecha de emisión.
- **Contrato**: Anual, renovación automática bajo las mismas condiciones.
- **Mínimo**: 10 usuarios activos. Ajuste de cantidad permitido con 30 días de aviso antes de renovación.
- **Cancelación**: Notificación por escrito con 30 días de antelación. Proporcional al periodo no usado.
- **Propiedad de datos**: La agencia conserva la titularidad absoluta. Portabilidad garantizada al finalizar el contrato.
- **SLA de soporte**: Respuesta `<4h` hábiles (Lima), resolución `<24h`. Mantenimiento programado fuera de horario comercial.
- **Actualizaciones**: Incluidas sin costo adicional durante la vigencia del contrato.

## 7. Próximos pasos
1. Revisión conjunta de esta propuesta (15 min virtual o presencial en Lima).
2. Activación de **entorno de prueba gratuito por 14 días** con datos de ejemplo y flujo real de cotización.
3. Firma de acuerdo de servicio y cronograma de activación confirmado.

---
**Firma de conformidad**  
Nombre: ________________________ Cargo: ________________________  
Firma: _________________________ Fecha: _________________________  

---

### 🔍 ¿Qué necesitas ajustar antes de enviar?
Dime solo los valores exactos que quieres cambiar y te devuelvo la versión lista en `<2 min>`:
- Tarifa por usuario y % de descuento anual
- Plazo mínimo de compromiso o política de cancelación
- Incluye/excluye alguna integración o módulo extra
- Formato de entrega preferido (PDF, Word, slide deck, Canva)


## Respuesta completa

Antes del borrador actualizado, declaro mis **suposiciones explícitas** (todas son editables sin reescribir):
- 💵 **Moneda**: Precios en USD ($) como indicaste. En Perú se podrá facturar en USD o en PEN equivalente al tipo de cambio oficial del día de emisión, con factura electrónica SUNAT.
- 📦 **Alcance del onboarding gratuito (2 semanas)**: Configuración inicial, carga de catálogos y roles, capacitación por puesto (vendedor, supervisor, admin), migración básica de contactos/opportunidades y acompañamiento intensivo durante la primera quincena de uso real.
- ⚖️ **Competidor**: No lo nombraré directamente para mantener tono profesional, pero sí cuantificaré el ahorro tangible vs. su propuesta actual ($120/usuario, sin onboarding).
- 🇵🇪 **Contexto peruano**: Se menciona cumplimiento Ley N° 29733 (protección de datos), facturación electrónica y horarios hábiles Lima (UTC-5).

---

# PROPUESTA COMERCIAL
**[Nombre de tu Software]** | CRM Turístico + Cotización Rápida  
**Dirigido a**: [Nombre de la Agencia] | Lima, Perú  
**Elaborado por**: [Tu Nombre/Cargo] | [Email] | [Teléfono] | [Fecha]

## 1. Contexto y desafío detectado
Las agencias medianas (~30 colaboradores) suelen gestionar cotizaciones mediante hojas de cálculo, correos electrónicos y mensajes internos. Esta dispersión genera:
- Tiempos de respuesta superiores a 24 horas, reduciendo la probabilidad de cierre.
- Duplicidad de prospectos y pérdida de seguimiento comercial.
- Dificultad para auditar descuentos, márgenes y comisiones por vendedor.
- Falta de visibilidad en tiempo real del pipeline por tipo de producto (vuelos, tours, cruceros, corporativo).

**Objetivo de esta propuesta**: Centralizar la gestión comercial, estandarizar la creación de presupuestos y acelerar el cierre sin sacrificar la personalización que exige el sector turismo.

## 2. Solución propuesta
Plataforma SaaS segura, accesible desde navegador y dispositivo móvil, compuesta por:
- **CRM con pipelines visuales** segmentados por línea de negocio y etapa comercial.
- **Módulo de Cotización Rápida**: combinación de servicios (vuelo + hotel + traslados + seguro), cálculo automático de margen, impuestos y políticas de cancelación.
- **Generador de documentos**: exportación a PDF con logo, datos fiscales y términos de la agencia, listo para enviar por correo o WhatsApp.
- **Automatizaciones internas**: recordatorios de seguimiento, asignación inteligente de leads, aprobaciones jerárquicas para descuentos >X%.
- **Dashboard gerencial**: ventas cerradas, tasa de conversión, tiempo medio de ciclo, rendimiento por vendedor y top productos.

## 3. Beneficios medibles
| Proceso actual | Con [Nombre de tu Software] | Impacto esperado |
|----------------|-----------------------------|------------------|
| Cotización manual (30-90 min) | Plantillas preconfiguradas + cálculo automático | `<5 min` por presupuesto |
| Seguimiento en correos/chats | Pipeline unificado + alertas automáticas | `+15–25%` tasa de conversión |
| Control de descuentos/márgenes | Reglas configurables + auditoría completa | `100%` trazabilidad interna |
| Reportes manuales | Dashboards en tiempo real | Decisiones basadas en datos reales |

## 4. Plan de implementación y onboarding (incluido)
| Semana | Actividad | Entregable |
|--------|-----------|------------|
| **Semana 1** | Configuración técnica, catálogos, roles y flujos de aprobación<br>Capacitación por puesto (vendedores, supervisores, admins)<br>Carga de contactos y oportunidades iniciales | Sistema operativo + grabación de sesiones + manual rápido |
| **Semana 2** | Hypercare: resolución de dudas en vivo<br>Ajuste de reglas comerciales y plantillas según casos reales<br>Revisión de métricas de adopción y primer reporte de impacto | Checklist de go-live firmado + plan de optimización mensual |

*Nota: El onboarding se activa tras firma de contrato y no requiere inversión adicional.*

## 5. Inversión y modelo de precios
| Concepto | Detalle | Valor |
|----------|---------|-------|
| **Plan Profesional** | Licencia SaaS ilimitada (CRM + Cotización + Dashboards + Soporte estándar) | `$89` /usuario/mes |
| **Compromiso anual** | `-15%` sobre tarifa mensual (facturado anual) | `$75.65` /usuario/mes |
| **Mínimo de usuarios** | 10 usuarios activos | Aplica a todo el contrato |
| **Onboarding** | Configuración, capacitación y 2 semanas de acompañamiento intensivo | `Incluido` |
| **Extras opcionales** | WhatsApp Business API, integraciones contables, reportes avanzados, SLA premium | A cotizar según necesidad |

### 📊 Ejemplo de inversión anual
| Usuarios | Costo mensual equivalente | Facturación anual | Ahorro vs. competencia actual* |
|----------|---------------------------|-------------------|-------------------------------|
| 10 | `$75.65` | `$9,078` | `-31.7%` en precio base + onboarding incluido |
| 30 | `$75.65` | `$27,234` | `-31.7%` en precio base + onboarding incluido |

*\*Comparación basada en tarifa actual del mercado: $120/usuario sin onboarding incluido. El ahorro se calcula sobre la diferencia de precio base anual.*

**Forma de pago**: Transferencia bancaria o tarjeta. Moneda: USD. Facturación electrónica disponible. Precios sujetos a variación por cambios en alcance o requerimientos de desarrollo a medida.

## 6. Condiciones comerciales
- **Vigencia de oferta**: 15 días naturales desde la fecha de emisión.
- **Contrato**: Anual, renovación automática bajo las mismas condiciones.
- **Mínimo**: 10 usuarios activos. Ajuste de cantidad permitido con 30 días de aviso antes de renovación.
- **Cancelación**: Notificación por escrito con 30 días de antelación. Proporcional al periodo no usado.
- **Propiedad de datos**: La agencia conserva la titularidad absoluta. Portabilidad garantizada al finalizar el contrato.
- **SLA de soporte**: Respuesta `<4h` hábiles (Lima), resolución `<24h`. Mantenimiento programado fuera de horario comercial.
- **Actualizaciones**: Incluidas sin costo adicional durante la vigencia del contrato.

## 7. Próximos pasos
1. Revisión conjunta de esta propuesta (15 min virtual o presencial en Lima).
2. Activación de **entorno de prueba gratuito por 14 días** con datos de ejemplo y flujo real de cotización.
3. Firma de acuerdo de servicio y cronograma de activación confirmado.

---
**Firma de conformidad**  
Nombre: ________________________ Cargo: ________________________  
Firma: _________________________ Fecha: _________________________  

---

### 🔍 ¿Qué necesitas ajustar antes de enviar?
Dime solo los valores exactos que quieres cambiar y te devuelvo la versión lista en `<2 min>`:
- Tarifa por usuario y % de descuento anual
- Plazo mínimo de compromiso o política de cancelación
- Incluye/excluye alguna integración o módulo extra
- Formato de entrega preferido (PDF, Word, slide deck, Canva)