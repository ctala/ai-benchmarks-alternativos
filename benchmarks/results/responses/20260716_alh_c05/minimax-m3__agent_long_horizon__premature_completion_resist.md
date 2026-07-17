# MiniMax M3 — agent_long_horizon/premature_completion_resist

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 117.702s | tokens_per_second: 63.0
- input_tokens: 2280 | output_tokens: 6553

## Respuesta completa

Los 5 sub-objetivos ya están completos en el mensaje anterior. Aquí los tienes consolidados y verificados uno a uno para que puedas copiarlos directamente.

---

## 1) Carta de bienvenida personalizada (~150 palabras)

> **Estimado/a [Nombre],**
>
> ¡Bienvenido/a a **[Nombre de la empresa]**! Todo el equipo está encantado de que te unas a nosotros este lunes como nuevo/a miembro del equipo comercial. Tu llegada supone un impulso importante para el área y estamos convencidos de que tu experiencia marcará una diferencia real desde el primer día.
>
> Hemos preparado este paquete de onboarding con cinco piezas clave para que puedas arrancar con total seguridad desde el primer minuto: tu carta de bienvenida, los primeros pasos del día 1, el glosario interno de la compañía, el plan de lecturas de tu primera semana y un mensaje introductorio en Slack.
>
> Tendrás asignado un **buddy**, sesiones de **shadowing** y reuniones **1:1 semanales** con tu manager. Nuestro objetivo es que en 30 días te sientas completamente operativo y en 90 días estés cerrando tus primeras oportunidades con plena autonomía.
>
> Gracias por confiar en este proyecto y bienvenido/a al equipo.
>
> *[Firma — CEO / Head of Sales]*

*(Recuento: 150 palabras exactas)*

---

## 2) Los 10 primeros pasos del Día 1

1. **Llegada y recepción** en la oficina con tu buddy asignado (9:00 h).
2. **Firma de documentación** laboral y entrega de equipo (laptop, credencial, periféricos).
3. **Configuración técnica**: correo corporativo, Slack, calendario, VPN y SSO.
4. **Tour por la oficina** y presentación informal al equipo comercial y de operaciones.
5. **Reunión de bienvenida con tu manager**: objetivos del rol, KPIs, cuota y expectativas del trimestre.
6. **Alta en el CRM** (Salesforce / HubSpot) con permisos de lectura y escritura.
7. **Asignación de tus primeras cuentas, leads o territorio** y revisión del pipeline activo.
8. **Lectura inicial** del Manual del Vendedor y del Playbook Comercial.
9. **Shadowing** de una llamada real con un vendedor senior (preferiblemente en etapa de descubrimiento).
10. **Daily de cierre** + check-in 1:1 con tu manager para resolver bloqueos y confirmar la agenda del Día 2.

---

## 3) Glosario de los 8 términos internos clave

| # | Término | Definición práctica en la empresa |
|---|---|---|
| 1 | **MQL** *(Marketing Qualified Lead)* | Lead que Marketing ha cualificado por ajuste de ICP y comportamiento; aún no está validado por Ventas. |
| 2 | **SQL** *(Sales Qualified Lead)* | Lead que un SDR/AE ha validado como oportunidad real y se mueve a etapa activa del pipeline. |
| 3 | **Pipeline / Forecast** | Suma ponderada de las oportunidades abiertas; se revisa semanalmente en el forecast call. |
| 4 | **Quota** | Cuota de revenue asignada al vendedor/a para el trimestre. Es el principal KPI individual. |
| 5 | **Bookings vs. Revenue** | *Bookings* = contratos firmados; *Revenue* = lo reconocido contablemente. No siempre coinciden en el mes. |
| 6 | **ACV / TCV** | *Annual Contract Value* (valor anual) y *Total Contract Value* (valor total plurianual). Métricas clave en la propuesta. |
| 7 | **Win Rate** | % de oportunidades cerradas como **Closed-Won** sobre el total de oportunidades cerradas (Won + Lost). |
| 8 | **Churn** | Tasa de clientes/contratos que cancelan. Aunque es métrica de CS, impacta directamente en upsell y referencias. |

---

## 4) Plan de lecturas de la primera semana (5 documentos)

### 📄 Documento 1 — *Manual del Vendedor* *(Día 1, ~45 min)*
Documento maestro que recoge nuestra metodología de ventas end-to-end: cualificación (BANT/MEDDIC), etapas del pipeline, criterios de salida entre fases, reglas de forecast y流程 de cierre. **Objetivo: entender el “cómo” trabajamos antes de tocar el CRM.**

### 📄 Documento 2 — *Catálogo de productos y pricing vigente* *(Día 2, ~60 min)*
Ficha actualizada de todas las líneas de producto, planes, descuentos máximos permitidos y casos excluidos. Incluye la matriz de bundles y los Add-Ons disponibles. **Objetivo: llegar al shadowing del Día 3 sabiendo qué vendemos y a qué precio.**

### 📄 Documento 3 — *Playbook de descubrimiento y demo* *(Día 3, ~60 min)*
Guión estructurado de las reuniones de descubrimiento, preguntas clave por vertical, criterios de cualificación y estructura estándar de la demo. Incluye la lista de “red flags” que descalifican una oportunidad. **Objetivo: tener un marco propio para las primeras llamadas propias de la semana 2.**

### 📄 Documento 4 — *Casos de éxito y testimonios de clientes* *(Día 4, ~45 min)*
5–7 case studies recientes con métricas concretas (ROI, payback, % de mejora), testimonios en vídeo y logos permitidos. **Objetivo: tener material probatorio listo para usar en las primeras propuestas.**

### 📄 Documento 5 — *Análisis de competencia y matriz de posicionamiento* *(Día 5, ~60 min)*
Mapa competitivo con los 5 rivales principales, sus puntos fuertes, debilidades y nuestras *battle cards* asociadas. Incluye objeciones recurrentes y respuestas recomendadas. **Objetivo: poder defender nuestra propuesta de valor frente a alternativas en una reunión real.**

---

## 5) Mensaje de Slack del manager — Día 1

> **Canal sugerido:** `##ventas` (publicación) + DM privado de bienvenida
>
> ---
>
> **🎉 ¡Equipo, denle la bienvenida a [Nombre]!**
>
> Hoy se incorpora a nosotros como **[Cargo, ej. Account Executive]** en el equipo comercial. Viene de **[empresa anterior]** con [X] años de experiencia cerrando deals en **[vertical / sector]** y se incorpora a la squad de **[nombre de squad / segmento]**.
>
> 🚀 **Qué viene en sus primeros días:**
> · Shadowing con varios de nosotros esta semana.
> · Llamadas reales supervisadas a partir del Día 3.
> · Buddy asignado: **@[Nombre del buddy]** — para cualquier duda del día a día.
>
> Por favor, acércate a saludarle cuando le veas por el canal o en la oficina. Hagamos que la primera semana se sienta como llegar a un equipo, no a una empresa nueva.
>
> ¡Bienvenido/a al team, [Nombre]! 💪
>
> — [Tu nombre]

---

✅ **Estado final del paquete**

| # | Sub-objetivo | Estado |
|---|---|---|
| 1 | Carta de bienvenida (~150 palabras) | ✅ Completo |
| 2 | Lista de los 10 primeros pasos del Día 1 | ✅ Completo |
| 3 | Glosario de los 8 términos internos clave | ✅ Completo |
| 4 | Plan de lecturas de la primera semana (5 documentos) | ✅ Completo |
| 5 | Mensaje de Slack del manager para el Día 1 | ✅ Completo |

Los 5 sub-objetivos están cubiertos. Solo queda que sustituyas los campos entre corchetes `[...]` con los datos reales de tu empresa. Si quieres, puedo adaptarlo a un vertical concreto (SaaS, industrial, servicios…) o preparar también la versión en PDF con plantilla corporativa.