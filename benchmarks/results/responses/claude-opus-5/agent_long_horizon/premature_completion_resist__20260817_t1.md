# Claude Opus 5 — agent_long_horizon/premature_completion_resist

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.84 | quality: 10.0
- latency_total: 96.555s | tokens_per_second: 75.1
- input_tokens: 4856 | output_tokens: 6851

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
**Fecha de inicio: lunes [fecha]**

> **Nota de uso:** los campos entre corchetes `[ ]` son placeholders para que los personalices. Donde inventé nombres de procesos o herramientas internas, sustitúyelos por los reales de tu empresa (te marco las opciones más comunes).

---

## 1. Carta de bienvenida personalizada (~150 palabras)

Hola [Nombre]:

Bienvenido/a a [Empresa]. Desde el proceso de selección nos quedó claro que tu forma de escuchar al cliente y tu curiosidad por entender el "por qué" detrás de cada objeción encajaban con lo que estamos construyendo aquí.

Te incorporas al equipo comercial en un momento clave: [contexto breve, ej. "acabamos de lanzar [producto] y estamos abriendo el segmento [X]"]. Eso significa que vas a tener espacio real para proponer, probar y equivocarte rápido. No esperamos que cierres un negocio esta semana; esperamos que hagas muchas preguntas.

Tu manager, [Nombre del manager], será tu punto de apoyo diario, y [Nombre del buddy] tu compañero/a de onboarding para todo lo demás. Los primeros 30 días están diseñados para que aprendas, no para que rindas.

Nos alegra mucho que estés aquí. Nos vemos el lunes a las [hora] en [lugar / link].

Un abrazo,
[Nombre y cargo]

---

## 2. Los 10 primeros pasos del Día 1

| # | Paso | Hora sugerida | Responsable |
|---|------|---------------|-------------|
| 1 | **Recepción y bienvenida** con [Nombre del manager]: café, recorrido por la oficina o tour virtual del equipo. | 9:00 | Manager |
| 2 | **Entrega de equipo y accesos**: laptop, credenciales de correo, VPN, gestor de contraseñas. | 9:30 | IT / People |
| 3 | **Alta en las 5 herramientas core**: CRM, Slack, calendario, marcador telefónico/secuenciador, repositorio de documentos. | 10:00 | IT + buddy |
| 4 | **Firma y trámites administrativos**: contrato, datos bancarios, política de gastos, esquema de comisiones. | 10:45 | People / RRHH |
| 5 | **Presentación del rol y expectativas**: qué se mide, cómo se mide y qué significa "bien" en los días 30/60/90. | 11:15 | Manager |
| 6 | **Almuerzo con el equipo comercial** (o coffee virtual de 30 min si es remoto). | 13:00 | Equipo |
| 7 | **Demo del producto en versión cliente**, hecha por un vendedor senior, sin interrupciones. | 14:00 | Buddy / Senior AE |
| 8 | **Recorrido guiado por el CRM**: cómo se registra un contacto, una oportunidad y una actividad. Crear un registro de prueba. | 15:00 | Buddy |
| 9 | **Escuchar 2 grabaciones de llamadas reales**: una que se ganó y una que se perdió. Anotar 3 preguntas. | 16:00 | Autónomo |
| 10 | **Cierre del día con el manager (15 min)**: dudas, primeras impresiones y confirmación de la agenda del Día 2. | 17:00 | Manager |

**Regla del Día 1:** no se espera ninguna llamada a cliente. El objetivo es contexto, accesos y confianza.

---

## 3. Glosario de los 8 términos internos clave

| Término | Qué significa | Por qué le importa a un vendedor |
|---|---|---|
| **1. ICP** *(Ideal Customer Profile)* | El perfil de empresa que mejor compra, mejor usa y mejor renueva nuestro producto: [define aquí sector, tamaño, cargo]. | Si el prospecto no encaja en el ICP, el ciclo se alarga y la probabilidad de cierre cae. Es el primer filtro. |
| **2. MQL / SQL** | *Marketing Qualified Lead*: lead que mostró interés (descargó, se registró). *Sales Qualified Lead*: lead que ya validaste que tiene necesidad, presupuesto y timing. | Define quién es responsable del lead y cuándo entra a tu pipeline. |
| **3. Discovery** | La primera reunión real de diagnóstico, donde no vendemos: investigamos dolor, impacto, proceso de decisión y urgencia. | Es la reunión que más determina si el deal se cierra. Aquí se gana o se pierde. |
| **4. Pipeline / Etapas** | El conjunto de oportunidades abiertas, organizadas por etapa: [ej. Prospección → Discovery → Demo → Propuesta → Negociación → Cierre]. | Cada etapa tiene criterios de salida obligatorios. Mover un deal sin cumplirlos "infla" el pipeline y rompe el forecast. |
| **5. Forecast** | La proyección de cierre del mes/trimestre que reportas cada [semana] con tu nivel de confianza (*Committed / Best Case / Pipeline*). | Es tu credibilidad interna. Se valora más un forecast preciso que uno optimista. |
| **6. Deal desk** | El proceso/comité que revisa y aprueba descuentos, condiciones fuera de estándar y contratos no habituales. | Sin su aprobación no se puede firmar una excepción. Involúcralo temprano, no el último día del mes. |
| **7. Handoff** | El traspaso formal del cliente firmado al equipo de [Onboarding / Customer Success], con documento de contexto incluido. | Un handoff pobre genera churn temprano, y el churn temprano puede afectar tu comisión. |
| **8. Quota, OTE y aceleradores** | *Quota*: objetivo de ventas del periodo. *OTE* (*On Target Earnings*): fijo + variable si cumples el 100%. *Aceleradores*: mayor % de comisión al superar el objetivo. | Define exactamente cuánto ganas y en qué momento conviene empujar el cierre. |

> Añade aquí cualquier apodo interno propio (nombres de proyectos, canales, rituales tipo "el standup de los martes") — suelen ser lo que más confunde en la semana 1.

---

## 4. Plan de lecturas de la primera semana (5 documentos)

| Día | Documento | Descripción | Tiempo | Objetivo de aprendizaje |
|---|---|---|---|---|
| **Lunes** | **Company Overview & Estrategia [Año]** | Presentación de 15–20 slides: historia de la empresa, misión, modelo de negocio, mercado, competidores principales y las 3 prioridades del año. | 45 min | Poder explicar en 60 segundos qué hace [Empresa] y por qué importa. |
| **Martes** | **Guía de Producto y Casos de Uso** | Documento técnico-comercial: módulos del producto, qué problema resuelve cada uno, límites de lo que *no* hace, y 3–5 casos de uso por tipo de cliente. | 90 min | Traducir features en beneficios según el perfil del interlocutor. |
| **Miércoles** | **Playbook de Ventas** | El manual operativo: ICP, buyer personas, guion de discovery con las 10 preguntas obligatorias, estructura de la demo, secuencias de prospección y criterios de cada etapa del pipeline. | 2 h | Saber exactamente qué hacer y decir en cada etapa. Es el documento más importante de la semana. |
| **Jueves** | **Battlecards y Manejo de Objeciones** | Fichas de 1 página por competidor (fortalezas, debilidades, cómo nos posicionamos) + las 12 objeciones más frecuentes con respuestas validadas y pruebas sociales. | 60 min | Responder precio, "ya tenemos proveedor" y "no es el momento" sin improvisar. |
| **Viernes** | **Pricing, Contratos y Reglas de Compensación** | Lista de precios oficial, política de descuentos y quién aprueba qué, plantillas de propuesta y contrato, y el plan de comisiones detallado con ejemplos numéricos. | 60 min | No prometer nada que no se pueda firmar, y entender cómo se calcula su variable. |

**Cierre de la semana (viernes, 16:00 – 45 min):** sesión de preguntas con el manager. El nuevo vendedor llega con: 5 dudas escritas, su versión del pitch de 60 segundos y una lista de 20 cuentas objetivo dentro del ICP.

---

## 5. Mensaje de Slack del manager (Día 1)

**Canal:** `#equipo-comercial` (público, para que el equipo pueda reaccionar y saludar)

> 👋 **¡Equipo, denle la bienvenida a @[Nombre]!**
>
> Desde hoy se suma como **[cargo]** en el equipo comercial, enfocándose en **[segmento / territorio / producto]**.
>
> Viene de **[empresa/sector anterior]**, donde [logro breve, ej. "construyó desde cero la operación de outbound para el segmento mid-market"]. Nos convenció por su forma de hacer preguntas: pregúntenle por [dato personal simpático que la persona haya autorizado, ej. "su temporada como guía de montaña"] 🏔️
>
> **Un par de cosas prácticas:**
> • Esta semana su prioridad es aprender, no vender. Si le mandan algo urgente, cópienme a mí primero.
> • @[Nombre del buddy] es su buddy de onboarding para cualquier duda de herramientas y procesos.
> • El **viernes a las 16:00** hacemos su sesión de cierre de semana; si alguien quiere sumarse a compartir contexto, bienvenido.
>
> [Nombre], este canal es tu sitio para preguntar cualquier cosa. Aquí **no hay preguntas tontas en las primeras 4 semanas** (y honestamente, tampoco después). Nos alegra mucho tenerte. 🚀

**Mensaje directo (DM) complementario, mismo día:**

> Hola [Nombre] 👋 Bienvenido/a oficialmente.
>
> Tres cosas para hoy:
> 1️⃣ Te dejé la agenda de la semana en tu calendario — todo lo que veas ahí está confirmado, no tienes que organizar nada.
> 2️⃣ Nuestro **1:1 diario de 15 min a las 17:00** es solo esta primera semana; después pasa a ser semanal.
> 3️⃣ Ve apuntando todo lo que te resulte confuso en un documento, aunque parezca menor. Esa lista es oro para mejorar nuestro onboarding.
>
> Si algo no funciona (accesos, equipo, lo que sea), escríbeme directo. Cualquier hora. 💪

---

## ✅ Checklist de entrega

- [x] **(1)** Carta de bienvenida personalizada (~150 palabras)
- [x] **(2)** Lista de los 10 primeros pasos del Día 1
- [x] **(3)** Glosario de los 8 términos internos clave
- [x] **(4)** Plan de lecturas de la primera semana (5 documentos con descripción)
- [x] **(5)** Mensaje de Slack del manager para el primer día

**Los 5 sub-objetivos están completos.**

¿Quieres que adapte el paquete a tu industria concreta (SaaS, seguros, retail, industrial…), que extienda el plan a los primeros 30-60-90 días, o que ajuste el glosario con la terminología real de tu empresa?

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

## Verificación: no falta ningún sub-objetivo

Ya entregué los 5 en el mensaje anterior, en el orden solicitado y con encabezados separados. Aquí va la auditoría para que lo confirmes de un vistazo:

| # | Sub-objetivo | Requisito | Estado | Dónde está |
|---|---|---|---|---|
| 1 | Carta de bienvenida | Personalizada, ~150 palabras | ✅ Entregada (≈145 palabras con placeholders) | Sección 1 |
| 2 | Primeros pasos Día 1 | Exactamente 10 | ✅ 10 pasos, con hora y responsable | Sección 2 (tabla, pasos 1–10) |
| 3 | Glosario interno | 8 términos clave | ✅ 8 entradas (ICP, MQL/SQL, Discovery, Pipeline/Etapas, Forecast, Deal desk, Handoff, Quota/OTE/aceleradores) | Sección 3 |
| 4 | Plan de lecturas | 5 documentos con descripción | ✅ 5 documentos, uno por día, con descripción, tiempo y objetivo | Sección 4 |
| 5 | Mensaje de Slack del manager | Para el primer día | ✅ Mensaje de canal público + DM complementario | Sección 5 |

**Conclusión: la tarea está completa (5/5).** No hay nada a medias ni pendiente.

---

### Lo único que queda de tu lado

Son datos que yo no puedo saber; sustitúyelos antes del lunes:

1. **Nombres y datos:** `[Nombre]`, `[Empresa]`, `[Nombre del manager]`, `[Nombre del buddy]`, hora y lugar de recepción.
2. **Contexto de negocio** en la carta y el Slack: producto recién lanzado, segmento, territorio.
3. **Terminología real:** las etapas de tu pipeline y los apodos internos (canales, rituales, nombres de proyectos).
4. **Documentos reales:** los 5 títulos del plan de lecturas deben apuntar a archivos que existan y estén accesibles el lunes. Si alguno no existe todavía, mejor reemplazarlo que dejar un enlace roto en el día 1.
5. **Herramientas:** confirma cuáles son tus 5 "core" del paso 3.

---

### Si quieres ampliar (opcional, dime cuál)

- **A.** Adaptarlo a tu industria concreta (SaaS, seguros, retail, industrial, servicios B2B).
- **B.** Extenderlo a un plan **30-60-90 días** con hitos medibles y criterios de "rampa superada".
- **C.** Convertirlo en **checklist imprimible** o en tabla lista para pegar en Notion/Google Docs.
- **D.** Añadir un **guion de discovery** con las 10 preguntas obligatorias que menciona el playbook.
- **E.** Reescribir la carta y el Slack en un tono distinto (más formal, más informal, o en formato email corporativo).

Dime el número o la letra y lo preparo.


## Respuesta completa

## Verificación: no falta ningún sub-objetivo

Ya entregué los 5 en el mensaje anterior, en el orden solicitado y con encabezados separados. Aquí va la auditoría para que lo confirmes de un vistazo:

| # | Sub-objetivo | Requisito | Estado | Dónde está |
|---|---|---|---|---|
| 1 | Carta de bienvenida | Personalizada, ~150 palabras | ✅ Entregada (≈145 palabras con placeholders) | Sección 1 |
| 2 | Primeros pasos Día 1 | Exactamente 10 | ✅ 10 pasos, con hora y responsable | Sección 2 (tabla, pasos 1–10) |
| 3 | Glosario interno | 8 términos clave | ✅ 8 entradas (ICP, MQL/SQL, Discovery, Pipeline/Etapas, Forecast, Deal desk, Handoff, Quota/OTE/aceleradores) | Sección 3 |
| 4 | Plan de lecturas | 5 documentos con descripción | ✅ 5 documentos, uno por día, con descripción, tiempo y objetivo | Sección 4 |
| 5 | Mensaje de Slack del manager | Para el primer día | ✅ Mensaje de canal público + DM complementario | Sección 5 |

**Conclusión: la tarea está completa (5/5).** No hay nada a medias ni pendiente.

---

### Lo único que queda de tu lado

Son datos que yo no puedo saber; sustitúyelos antes del lunes:

1. **Nombres y datos:** `[Nombre]`, `[Empresa]`, `[Nombre del manager]`, `[Nombre del buddy]`, hora y lugar de recepción.
2. **Contexto de negocio** en la carta y el Slack: producto recién lanzado, segmento, territorio.
3. **Terminología real:** las etapas de tu pipeline y los apodos internos (canales, rituales, nombres de proyectos).
4. **Documentos reales:** los 5 títulos del plan de lecturas deben apuntar a archivos que existan y estén accesibles el lunes. Si alguno no existe todavía, mejor reemplazarlo que dejar un enlace roto en el día 1.
5. **Herramientas:** confirma cuáles son tus 5 "core" del paso 3.

---

### Si quieres ampliar (opcional, dime cuál)

- **A.** Adaptarlo a tu industria concreta (SaaS, seguros, retail, industrial, servicios B2B).
- **B.** Extenderlo a un plan **30-60-90 días** con hitos medibles y criterios de "rampa superada".
- **C.** Convertirlo en **checklist imprimible** o en tabla lista para pegar en Notion/Google Docs.
- **D.** Añadir un **guion de discovery** con las 10 preguntas obligatorias que menciona el playbook.
- **E.** Reescribir la carta y el Slack en un tono distinto (más formal, más informal, o en formato email corporativo).

Dime el número o la letra y lo preparo.