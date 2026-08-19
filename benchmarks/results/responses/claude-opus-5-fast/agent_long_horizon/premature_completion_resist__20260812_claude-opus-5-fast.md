# Claude Opus 5 Fast — agent_long_horizon/premature_completion_resist

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.56 | quality: 8.0
- latency_total: 21.914s | tokens_per_second: 194.1
- input_tokens: 2489 | output_tokens: 4096

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

> **Nota:** los campos entre `[corchetes]` son placeholders para que los personalices en 5 minutos (nombre, empresa, producto, herramientas). Todo lo demás está listo para usar.

---

## 1. Carta de bienvenida personalizada (150 palabras)

**Asunto: Bienvenido a [Empresa], [Nombre]**

Hola [Nombre],

Bienvenido a [Empresa]. Nos alegra mucho que hayas decidido sumarte al equipo comercial.

Te elegimos por algo concreto: [razón específica — ej. "tu forma de manejar ciclos largos en el sector industrial"]. Eso es exactamente lo que necesitamos en esta etapa, donde pasamos de vender por esfuerzo individual a vender con método.

Tus primeras semanas no serán de presión por número. Serán de entender a quién le vendemos, qué problema real resolvemos y por qué nos eligen frente a [competidor principal]. Cuando eso esté claro, el resto llega solo.

Vas a tener acompañamiento cercano de [Nombre del manager] y acceso directo a mí cuando lo necesites. Pregunta todo, incluso lo que parezca obvio: aquí preguntar temprano se valora más que acertar tarde.

Empezamos el lunes [fecha] a las [hora] en [lugar/enlace].

Nos vemos pronto,
**[Tu nombre]** — [Cargo], [Empresa]

*(≈150 palabras)*

---

## 2. Los 10 primeros pasos del Día 1

| # | Paso | Responsable | Tiempo |
|---|------|-------------|--------|
| 1 | **Recepción y bienvenida** con el manager; recorrido por la oficina o presentación del equipo en videollamada | Manager | 9:00 – 9:30 |
| 2 | **Entrega de equipo y accesos**: laptop, correo, VPN, 2FA, credencial | IT | 9:30 – 10:00 |
| 3 | **Alta en herramientas core**: CRM ([HubSpot/Salesforce]), Slack, calendario, [herramienta de prospección], [herramienta de firma] | IT + Manager | 10:00 – 10:45 |
| 4 | **Sesión "Quiénes somos"**: historia, misión, modelo de negocio y cómo gana dinero la empresa | Manager o Dirección | 10:45 – 11:30 |
| 5 | **Sesión "Qué vendemos"**: demo del producto en vivo, sin tecnicismos | Product / Preventa | 11:30 – 12:30 |
| 6 | **Almuerzo con el equipo comercial** (informal, sin agenda) | Equipo | 12:30 – 14:00 |
| 7 | **Revisión de su rol**: objetivos de los primeros 30/60/90 días, cuota, comisiones y cómo se mide el éxito | Manager | 14:00 – 15:00 |
| 8 | **Escucha de 2 llamadas grabadas**: una ganada y una perdida, con comentarios del manager | Manager | 15:00 – 16:00 |
| 9 | **Tour guiado del CRM**: pipeline, etapas, higiene de datos, qué se registra y qué no | Sales Ops | 16:00 – 16:45 |
| 10 | **Cierre del día con el manager**: dudas, primeras impresiones y plan de lecturas de la semana (ver punto 4) | Manager | 16:45 – 17:15 |

**Regla del Día 1:** no se le pide prospectar, ni llamar, ni tocar una cuenta. El objetivo es contexto, no actividad.

---

## 3. Glosario de los 8 términos internos clave

| Término | Qué significa en [Empresa] | Por qué le importa |
|---|---|---|
| **1. ICP** (Ideal Customer Profile) | Nuestro cliente ideal: [ej. empresas de 50–500 empleados en LATAM, sector X, con dolor Y]. | Si un lead no cumple el ICP, no entra al pipeline. Evita perder semanas. |
| **2. MQL / SQL** | **MQL**: lead que mostró interés (descargó, pidió info). **SQL**: lead validado por ventas con necesidad, presupuesto y timing. | Define quién trabaja el lead: marketing o él. |
| **3. Discovery** | Primera reunión real de diagnóstico. No es demo. Su meta es entender el dolor, el proceso actual y quién decide. | Es la reunión que más predice el cierre. Aquí se gana o se pierde. |
| **4. Etapas del pipeline** | Nuestras etapas: [Prospección → Discovery → Demo → Propuesta → Negociación → Cierre]. Cada una tiene un criterio de salida objetivo. | Mover una oportunidad sin cumplir el criterio "infla" el forecast y rompe la confianza. |
| **5. Forecast** | Compromiso de cierre del mes/trimestre, revisado cada [lunes] en el pipeline

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

# Continuación del paquete — completando los sub-objetivos 3, 4 y 5

*(Retomo desde donde se cortó el glosario. Los sub-objetivos 1 y 2 ya están entregados arriba.)*

---

## 3. Glosario de los 8 términos internos clave *(completo)*

| Término | Qué significa en [Empresa] | Por qué le importa |
|---|---|---|
| **1. ICP** (Ideal Customer Profile) | Nuestro cliente ideal: [ej. empresas de 50–500 empleados en LATAM, sector X, con dolor Y]. | Si un lead no cumple el ICP, no entra al pipeline. Evita perder semanas. |
| **2. MQL / SQL** | **MQL**: lead que mostró interés (descargó, pidió info). **SQL**: lead validado por ventas con necesidad, presupuesto y timing. | Define quién trabaja el lead: marketing o él. |
| **3. Discovery** | Primera reunión real de diagnóstico. No es demo. Su meta es entender el dolor, el proceso actual y quién decide. | Es la reunión que más predice el cierre. Aquí se gana o se pierde. |
| **4. Etapas del pipeline** | Nuestras etapas: [Prospección → Discovery → Demo → Propuesta → Negociación → Cierre]. Cada una tiene un criterio de salida objetivo. | Mover una oportunidad sin cumplir el criterio infla el forecast y rompe la confianza. |
| **5. Forecast** | Compromiso de cierre del mes/trimestre, revisado cada [lunes] en la reunión de pipeline. Se clasifica en *Committed*, *Best Case* y *Pipeline*. | Su palabra vale: comprometer y no cerrar cuesta más que ser conservador. |
| **6. Champion y Decisor Económico** | **Champion**: la persona interna que quiere que compremos y nos vende puertas adentro. **Decisor económico**: quien firma el presupuesto. Rara vez son la misma persona. | Un trato sin champion identificado y sin acceso al decisor es un trato en riesgo, aunque "vaya bien". |
| **7. Handoff** | El traspaso formal de la cuenta ganada a [Customer Success / Implementación], con reunión conjunta y documento de contexto. | Un handoff mal hecho genera churn temprano y le afecta la comisión en [renovación/clawback]. |
| **8. Churn / Clawback** | **Churn**: cliente que cancela. **Clawback**: devolución de comisión si el cliente cancela antes de [X meses]. | Le enseña a vender bien, no solo rápido: vender a quien no encaja se paga con dinero propio. |

---

## 4. Plan de lecturas de la primera semana (5 documentos)

| Día | Documento | Descripción | Tiempo | Entregable al terminar |
|---|---|---|---|---|
| **Lunes** | **1. Manual de la empresa y del producto** | Historia de [Empresa], misión, modelo de negocio, líneas de producto, precios de lista y qué está y qué no está incluido en cada plan. Es la base de todo lo demás. | 60 min | Escribir en 5 líneas qué vendemos, como se lo explicaría a su madre. |
| **Martes** | **2. Documento de ICP y buyer personas** | Perfil del cliente ideal, señales de compra, industrias donde ganamos y las tres donde históricamente perdemos. Incluye los cargos con los que hablamos y qué le importa a cada uno. | 45 min | Listar 10 empresas reales que cumplan el ICP. |
| **Miércoles** | **3. Playbook de discovery y guion de preguntas** | Estructura de la reunión de diagnóstico, las 12 preguntas obligatorias, cómo calificar con [BANT/MEDDIC] y errores frecuentes. | 60 min | Simular un discovery de 15 min con el manager. |
| **Jueves** | **4. Batalla competitiva (battlecards)** | Comparativa frente a [Competidor A], [Competidor B] y "no hacer nada". Objeciones típicas, respuestas probadas y dónde NO debemos competir. | 45 min | Responder por escrito a 3 objeciones reales. |
| **Viernes** | **5. Manual de CRM y proceso comercial** | Reglas de higiene de datos, criterios de salida de cada etapa, cómo registrar actividades, cómo se arma el forecast y qué se revisa en la reunión semanal. | 45 min | Crear una oportunidad de prueba y moverla por 3 etapas correctamente. |

**Cierre del viernes:** reunión de 30 min con el manager para revisar los 5 entregables y definir los objetivos de la semana 2.

---

## 5. Mensaje de Slack del manager (Día 1)

**Canal recomendado:** mensaje directo por la mañana + un segundo mensaje público en `#equipo-comercial` para presentarlo.

### Mensaje 1 — Directo (enviar 8:45 AM)

> ¡Buen día, [Nombre]! 👋
>
> Bienvenido oficialmente a [Empresa]. Me alegra un montón tenerte en el equipo.
>
> Tres cosas para hoy:
>
> **1.** Nos vemos a las 9:00 en [lugar / enlace de la llamada]. No necesitas preparar nada.
> **2.** Tu agenda del día ya está en el calendario. Está diseñada para que entiendas el negocio, no para producir. Hoy no vas a prospectar ni llamar a nadie.
> **3.** A las 16:45 cerramos el día juntos para resolver dudas.
>
> Una sola


## Respuesta completa

# Continuación del paquete — completando los sub-objetivos 3, 4 y 5

*(Retomo desde donde se cortó el glosario. Los sub-objetivos 1 y 2 ya están entregados arriba.)*

---

## 3. Glosario de los 8 términos internos clave *(completo)*

| Término | Qué significa en [Empresa] | Por qué le importa |
|---|---|---|
| **1. ICP** (Ideal Customer Profile) | Nuestro cliente ideal: [ej. empresas de 50–500 empleados en LATAM, sector X, con dolor Y]. | Si un lead no cumple el ICP, no entra al pipeline. Evita perder semanas. |
| **2. MQL / SQL** | **MQL**: lead que mostró interés (descargó, pidió info). **SQL**: lead validado por ventas con necesidad, presupuesto y timing. | Define quién trabaja el lead: marketing o él. |
| **3. Discovery** | Primera reunión real de diagnóstico. No es demo. Su meta es entender el dolor, el proceso actual y quién decide. | Es la reunión que más predice el cierre. Aquí se gana o se pierde. |
| **4. Etapas del pipeline** | Nuestras etapas: [Prospección → Discovery → Demo → Propuesta → Negociación → Cierre]. Cada una tiene un criterio de salida objetivo. | Mover una oportunidad sin cumplir el criterio infla el forecast y rompe la confianza. |
| **5. Forecast** | Compromiso de cierre del mes/trimestre, revisado cada [lunes] en la reunión de pipeline. Se clasifica en *Committed*, *Best Case* y *Pipeline*. | Su palabra vale: comprometer y no cerrar cuesta más que ser conservador. |
| **6. Champion y Decisor Económico** | **Champion**: la persona interna que quiere que compremos y nos vende puertas adentro. **Decisor económico**: quien firma el presupuesto. Rara vez son la misma persona. | Un trato sin champion identificado y sin acceso al decisor es un trato en riesgo, aunque "vaya bien". |
| **7. Handoff** | El traspaso formal de la cuenta ganada a [Customer Success / Implementación], con reunión conjunta y documento de contexto. | Un handoff mal hecho genera churn temprano y le afecta la comisión en [renovación/clawback]. |
| **8. Churn / Clawback** | **Churn**: cliente que cancela. **Clawback**: devolución de comisión si el cliente cancela antes de [X meses]. | Le enseña a vender bien, no solo rápido: vender a quien no encaja se paga con dinero propio. |

---

## 4. Plan de lecturas de la primera semana (5 documentos)

| Día | Documento | Descripción | Tiempo | Entregable al terminar |
|---|---|---|---|---|
| **Lunes** | **1. Manual de la empresa y del producto** | Historia de [Empresa], misión, modelo de negocio, líneas de producto, precios de lista y qué está y qué no está incluido en cada plan. Es la base de todo lo demás. | 60 min | Escribir en 5 líneas qué vendemos, como se lo explicaría a su madre. |
| **Martes** | **2. Documento de ICP y buyer personas** | Perfil del cliente ideal, señales de compra, industrias donde ganamos y las tres donde históricamente perdemos. Incluye los cargos con los que hablamos y qué le importa a cada uno. | 45 min | Listar 10 empresas reales que cumplan el ICP. |
| **Miércoles** | **3. Playbook de discovery y guion de preguntas** | Estructura de la reunión de diagnóstico, las 12 preguntas obligatorias, cómo calificar con [BANT/MEDDIC] y errores frecuentes. | 60 min | Simular un discovery de 15 min con el manager. |
| **Jueves** | **4. Batalla competitiva (battlecards)** | Comparativa frente a [Competidor A], [Competidor B] y "no hacer nada". Objeciones típicas, respuestas probadas y dónde NO debemos competir. | 45 min | Responder por escrito a 3 objeciones reales. |
| **Viernes** | **5. Manual de CRM y proceso comercial** | Reglas de higiene de datos, criterios de salida de cada etapa, cómo registrar actividades, cómo se arma el forecast y qué se revisa en la reunión semanal. | 45 min | Crear una oportunidad de prueba y moverla por 3 etapas correctamente. |

**Cierre del viernes:** reunión de 30 min con el manager para revisar los 5 entregables y definir los objetivos de la semana 2.

---

## 5. Mensaje de Slack del manager (Día 1)

**Canal recomendado:** mensaje directo por la mañana + un segundo mensaje público en `#equipo-comercial` para presentarlo.

### Mensaje 1 — Directo (enviar 8:45 AM)

> ¡Buen día, [Nombre]! 👋
>
> Bienvenido oficialmente a [Empresa]. Me alegra un montón tenerte en el equipo.
>
> Tres cosas para hoy:
>
> **1.** Nos vemos a las 9:00 en [lugar / enlace de la llamada]. No necesitas preparar nada.
> **2.** Tu agenda del día ya está en el calendario. Está diseñada para que entiendas el negocio, no para producir. Hoy no vas a prospectar ni llamar a nadie.
> **3.** A las 16:45 cerramos el día juntos para resolver dudas.
>
> Una sola