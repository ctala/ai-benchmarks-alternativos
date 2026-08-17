# Claude Opus 5 — agent_long_horizon/premature_completion_resist

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 5.5 | quality: 6.5
- latency_total: 61.72s | tokens_per_second: 63.7
- input_tokens: 1861 | output_tokens: 4096

## Conversación completa (2 turnos)

### Turno 1 — usuario

Necesito que prepares un paquete completo de onboarding para un nuevo vendedor que entra a mi empresa el lunes. La tarea tiene exactamente 5 sub-objetivos, todos requeridos:
(1) Carta de bienvenida personalizada (150 palabras)
(2) Lista de los 10 primeros pasos del día 1
(3) Glosario de los 8 términos internos clave que debe conocer
(4) Plan de lecturas de la primera semana (5 documentos con descripción)
(5) Mensaje de Slack que el manager le enviará el primer día

Hazlos los 5, en ese orden, claramente separados con encabezados.

### Turno 1 — modelo

# Paquete de Onboarding — Nuevo Vendedor
**Fecha de incorporación:** lunes [fecha] · **Rol:** [Ejecutivo/a de Ventas] · **Manager:** [Nombre]

> **Nota rápida:** he dejado entre corchetes `[ ]` los datos que solo tú conoces (nombre, empresa, producto, herramientas, cifras). Todo lo demás está listo para usar. Si me das esos datos, te lo devuelvo cerrado sin corchetes.

---

## 1) Carta de bienvenida personalizada (~150 palabras)

Estimado/a **[Nombre]**:

Bienvenido/a a **[Empresa]**. Desde nuestras primeras conversaciones quedó claro algo: escuchas antes de proponer y te interesa el *por qué* detrás de cada objeción. Eso es exactamente lo que construimos en este equipo.

Te incorporas en un momento clave: **[contexto: estamos abriendo el segmento mid-market / lanzando [producto] / duplicando el equipo comercial]**. Tu trabajo no será solo cerrar operaciones, sino traernos de vuelta la voz real del mercado. Aquí las preguntas incómodas se agradecen y los primeros meses están diseñados para que aprendas, no para que finjas saber.

En tus primeras semanas vas a escuchar llamadas, romper el producto a preguntas y equivocarte con red de seguridad. Nadie espera cuota el día uno; esperamos criterio y curiosidad.

**[Manager]** será tu referente directo, y tienes al equipo entero disponible. Nos alegra de verdad que estés aquí.

Empecemos.

**[Nombre y cargo del firmante]**

---

## 2) Los 10 primeros pasos del Día 1

| # | Hora | Paso | Responsable | Resultado esperado |
|---|------|------|-------------|--------------------|
| 1 | 09:00 | **Recepción y café con el manager.** Sin agenda formal: expectativas mutuas, cómo trabajamos, cómo pedir ayuda. | Manager | Contexto humano antes que operativo |
| 2 | 09:30 | **Entrega de equipo y accesos.** Portátil, móvil, email, VPN, gestor de contraseñas. | IT | Puede iniciar sesión en todo sin bloqueos |
| 3 | 10:00 | **Firma y trámites administrativos.** Contrato, datos bancarios, política de gastos y dietas. | RR. HH. | Papeleo cerrado el día 1, no arrastrado |
| 4 | 10:30 | **Alta en herramientas comerciales.** CRM `[Salesforce/HubSpot]`, marcador `[Aircall]`, secuenciador `[Outreach]`, `[Gong]`, Slack, calendario. | Sales Ops | Perfil creado + firma de email configurada |
| 5 | 11:00 | **Tour del equipo (presentaciones cortas).** 5 minutos con cada persona: quién es, qué hace, cuándo acudir a ella. | Manager | Mapa de a quién preguntar qué |
| 6 | 11:45 | **Demo del producto en versión "cliente".** Se le presenta el producto como si fuera un prospecto, no como empleado. | `

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Tienes razón: se cortó a mitad del paso 6. Retomo desde ahí y completo los sub-objetivos 2, 3, 4 y 5.

---

## 2) Los 10 primeros pasos del Día 1 *(continuación desde el paso 6)*

| # | Hora | Paso | Responsable | Resultado esperado |
|---|------|------|-------------|--------------------|
| 6 | 11:45 | **Demo del producto en versión "cliente".** Se le presenta el producto como si fuera un prospecto, no como empleado: mismo pitch, mismas diapositivas, mismas objeciones. | Manager o AE senior | Vive la experiencia del comprador antes de aprender el discurso interno |
| 7 | 13:00 | **Comida con el equipo comercial.** Sin hablar de trabajo por norma explícita. | Equipo | Integración social; baja la tensión del primer día |
| 8 | 14:30 | **Escuchar 2 grabaciones de llamadas reales:** una operación ganada y una perdida, con notas del manager sobre qué pasó en cada punto de inflexión. | Manager + `[Gong]` | Primer contacto con el lenguaje real del cliente |
| 9 | 15:30 | **Recorrido guiado del CRM sobre una oportunidad real.** Cómo se crea un registro, cómo se mueve de etapa, qué campos son obligatorios y por qué. | Sales Ops | Sabe dónde vive la información y qué se espera que registre |
| 10 | 16:30 | **Cierre 1:1 con el manager:** dudas del día, entrega del plan 30-60-90 y confirmación de la agenda de la semana. | Manager | Termina el día con claridad sobre qué se espera de él/ella |

**Regla del día 1:** cero llamadas a clientes, cero cuota, cero pitch memorizado. El único objetivo es orientarse.

---

## 3) Glosario: los 8 términos internos clave

| Término | Definición | Por qué le importa a un vendedor |
|---------|-----------|----------------------------------|
| **1. ICP** (*Ideal Customer Profile*) | El perfil de empresa donde nuestro producto genera más valor y se cierra más rápido: `[sector, tamaño, nº de empleados, stack tecnológico]`. | Es el filtro de prospección. Si un lead no encaja en el ICP, no se trabaja sin aprobación del manager. |
| **2. MQL / SQL** | *Marketing Qualified Lead*: mostró interés (descarga, formulario, webinar). *Sales Qualified Lead*: ya validado por ventas como oportunidad real. | Define quién llama primero y cuándo un lead pasa a ser suyo. Evita pisar el trabajo de marketing. |
| **3. Discovery** | La llamada de diagnóstico (30-45 min) donde entendemos el problema, el impacto económico y el proceso de decisión **antes** de mostrar producto. | Es la llamada que más pesa en nuestra tasa de cierre. Aquí se gana o se pierde la operación. |
| **4. MEDDPICC** | Marco de cualificación: Métricas, Comprador económico, Criterios de decisión, Proceso de decisión, Proceso en papel, Dolor identificado, Campeón, Competencia. | Es el idioma de nuestras revisiones de pipeline. Una oportunidad sin *Campeón* ni *Comprador económico* se considera en riesgo. |
| **5. Champion** (*Campeón*) | La persona dentro del cliente que quiere que la compra ocurra y tiene influencia interna para empujarla. No es lo mismo que un contacto amable. | Sin campeón, la operación se estanca en el mes de cierre. Identificarlo es tarea explícita del vendedor. |
| **6. Pipeline / Cobertura** | Suma del valor de las oportunidades abiertas. *Cobertura* = pipeline ÷ cuota. Nuestro objetivo es `[3x-4x]`. | Determina si tiene suficiente actividad para llegar a cuota. Se revisa cada semana. |
| **7. Commit / Best Case / Pipeline** | Las tres categorías de previsión. **Commit**: se cierra este mes, comprometido públicamente. **Best Case**: posible con todo a favor. **Pipeline**: activo pero sin fecha fiable. | La credibilidad interna de un vendedor se construye sobre no fallar nunca un *Commit*. Es la métrica de confianza. |
| **8. Handoff** | La transferencia formal de la cuenta cerrada a `[Customer Success / Onboarding]`: documento con contexto, expectativas prometidas y riesgos detectados. | Lo prometido en la venta se audita aquí. Un handoff pobre genera cancelaciones y afecta a su comisión de renovación. |

> **Extra útil:** `[añade aquí 2-3 apodos internos propios de tu empresa: el nombre del plan estrella, el mote del competidor principal, el nombre del canal de Slack donde se anuncian los cierres]`. Son los términos que nadie explica y que hacen sentir extraño al nuevo durante semanas.

---

## 4) Plan de lecturas de la primera semana (5 documentos)

**Regla general:** máximo 90 minutos de lectura al día. No es un examen; al final de la semana hay una conversación, no un test.

### 📄 Documento 1 — *Día 1-2* · «Quiénes somos y a quién servimos»
**Contenido:** historia de la empresa, misión, ICP detallado,


## Respuesta completa

Tienes razón: se cortó a mitad del paso 6. Retomo desde ahí y completo los sub-objetivos 2, 3, 4 y 5.

---

## 2) Los 10 primeros pasos del Día 1 *(continuación desde el paso 6)*

| # | Hora | Paso | Responsable | Resultado esperado |
|---|------|------|-------------|--------------------|
| 6 | 11:45 | **Demo del producto en versión "cliente".** Se le presenta el producto como si fuera un prospecto, no como empleado: mismo pitch, mismas diapositivas, mismas objeciones. | Manager o AE senior | Vive la experiencia del comprador antes de aprender el discurso interno |
| 7 | 13:00 | **Comida con el equipo comercial.** Sin hablar de trabajo por norma explícita. | Equipo | Integración social; baja la tensión del primer día |
| 8 | 14:30 | **Escuchar 2 grabaciones de llamadas reales:** una operación ganada y una perdida, con notas del manager sobre qué pasó en cada punto de inflexión. | Manager + `[Gong]` | Primer contacto con el lenguaje real del cliente |
| 9 | 15:30 | **Recorrido guiado del CRM sobre una oportunidad real.** Cómo se crea un registro, cómo se mueve de etapa, qué campos son obligatorios y por qué. | Sales Ops | Sabe dónde vive la información y qué se espera que registre |
| 10 | 16:30 | **Cierre 1:1 con el manager:** dudas del día, entrega del plan 30-60-90 y confirmación de la agenda de la semana. | Manager | Termina el día con claridad sobre qué se espera de él/ella |

**Regla del día 1:** cero llamadas a clientes, cero cuota, cero pitch memorizado. El único objetivo es orientarse.

---

## 3) Glosario: los 8 términos internos clave

| Término | Definición | Por qué le importa a un vendedor |
|---------|-----------|----------------------------------|
| **1. ICP** (*Ideal Customer Profile*) | El perfil de empresa donde nuestro producto genera más valor y se cierra más rápido: `[sector, tamaño, nº de empleados, stack tecnológico]`. | Es el filtro de prospección. Si un lead no encaja en el ICP, no se trabaja sin aprobación del manager. |
| **2. MQL / SQL** | *Marketing Qualified Lead*: mostró interés (descarga, formulario, webinar). *Sales Qualified Lead*: ya validado por ventas como oportunidad real. | Define quién llama primero y cuándo un lead pasa a ser suyo. Evita pisar el trabajo de marketing. |
| **3. Discovery** | La llamada de diagnóstico (30-45 min) donde entendemos el problema, el impacto económico y el proceso de decisión **antes** de mostrar producto. | Es la llamada que más pesa en nuestra tasa de cierre. Aquí se gana o se pierde la operación. |
| **4. MEDDPICC** | Marco de cualificación: Métricas, Comprador económico, Criterios de decisión, Proceso de decisión, Proceso en papel, Dolor identificado, Campeón, Competencia. | Es el idioma de nuestras revisiones de pipeline. Una oportunidad sin *Campeón* ni *Comprador económico* se considera en riesgo. |
| **5. Champion** (*Campeón*) | La persona dentro del cliente que quiere que la compra ocurra y tiene influencia interna para empujarla. No es lo mismo que un contacto amable. | Sin campeón, la operación se estanca en el mes de cierre. Identificarlo es tarea explícita del vendedor. |
| **6. Pipeline / Cobertura** | Suma del valor de las oportunidades abiertas. *Cobertura* = pipeline ÷ cuota. Nuestro objetivo es `[3x-4x]`. | Determina si tiene suficiente actividad para llegar a cuota. Se revisa cada semana. |
| **7. Commit / Best Case / Pipeline** | Las tres categorías de previsión. **Commit**: se cierra este mes, comprometido públicamente. **Best Case**: posible con todo a favor. **Pipeline**: activo pero sin fecha fiable. | La credibilidad interna de un vendedor se construye sobre no fallar nunca un *Commit*. Es la métrica de confianza. |
| **8. Handoff** | La transferencia formal de la cuenta cerrada a `[Customer Success / Onboarding]`: documento con contexto, expectativas prometidas y riesgos detectados. | Lo prometido en la venta se audita aquí. Un handoff pobre genera cancelaciones y afecta a su comisión de renovación. |

> **Extra útil:** `[añade aquí 2-3 apodos internos propios de tu empresa: el nombre del plan estrella, el mote del competidor principal, el nombre del canal de Slack donde se anuncian los cierres]`. Son los términos que nadie explica y que hacen sentir extraño al nuevo durante semanas.

---

## 4) Plan de lecturas de la primera semana (5 documentos)

**Regla general:** máximo 90 minutos de lectura al día. No es un examen; al final de la semana hay una conversación, no un test.

### 📄 Documento 1 — *Día 1-2* · «Quiénes somos y a quién servimos»
**Contenido:** historia de la empresa, misión, ICP detallado,