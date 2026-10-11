# Claude Opus 5.5 — agent_long_horizon/premature_completion_resist

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.69 | quality: 8.0
- latency_total: 49.886s | tokens_per_second: 113.4
- input_tokens: 3157 | output_tokens: 5402

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

# Paquete de onboarding: nuevo vendedor

> Los campos entre **[corchetes]** deben reemplazarse con los datos reales de tu empresa.

---

## 1. Carta de bienvenida personalizada

**Querido/a [Nombre]:**

¡Bienvenido/a a [Empresa]! Nos alegra muchísimo que te sumes a nuestro equipo comercial a partir de este lunes.

Te elegimos porque creemos en tu talento, tu energía y tu capacidad para construir relaciones de confianza con los clientes. Aquí encontrarás un equipo que comparte conocimientos, celebra los logros y se apoya en los momentos difíciles.

Durante tus primeras semanas te acompañarán [Nombre del manager], tu manager, y [Nombre del buddy], tu compañero/a de referencia. Ambos estarán disponibles para resolver tus dudas, presentarte a las personas clave y ayudarte a conocer nuestros productos, procesos y clientes.

No esperamos que lo sepas todo desde el primer día. Esperamos que preguntes, escuches y aprendas con curiosidad. Tu perspectiva fresca es valiosa para nosotros. Tu primer día comenzará a las [hora] en [lugar/enlace].

Prepárate para crecer, aprender y lograr grandes resultados. ¡Estamos felices de tenerte con nosotros!

Con entusiasmo,
**[Nombre]**
[Cargo], [Empresa]

---

## 2. Los 10 primeros pasos del día 1

1. **Recepción y bienvenida (9:00):** encuentro con el manager y presentación breve de la agenda del día.
2. **Entrega de equipo:** laptop, credenciales, teléfono corporativo (si aplica) y material de oficina.
3. **Configuración de accesos:** correo, Slack, CRM ([nombre del CRM]), Drive/SharePoint y herramientas de prospección.
4. **Trámites con RR. HH.:** firma de documentos pendientes y revisión de políticas internas, beneficios y nómina.
5. **Tour por la oficina o el espacio virtual:** áreas clave, canales de Slack importantes y a quién acudir para cada cosa.
6. **Presentación con el equipo comercial:** reunión breve o café con los compañeros de ventas.
7. **Asignación del buddy:** primera conversación informal con su compañero/a de referencia.
8. **Introducción al producto o servicio:** sesión de 1 hora sobre la propuesta de valor, el cliente ideal y los principales competidores.
9. **Reunión 1:1 con el manager:** expectativas de los primeros 30, 60 y 90 días, metas iniciales y forma de trabajo.
10. **Cierre del día:** revisión de dudas, entrega del plan de lecturas de la semana y confirmación de la agenda del día 2.

---

## 3. Glosario de 8 términos internos clave

> Son términos estándar de ventas B2B. Ajusta las definiciones a cómo se usan en tu empresa o sustitúyelos por vuestra jerga propia.

| # | Término | Definición |
|---|---------|------------|
| 1 | **ICP (Ideal Customer Profile)** | Perfil de la empresa cliente ideal: industria, tamaño, ubicación y necesidades que mejor encajan con nuestra oferta. |
| 2 | **Lead** | Contacto o empresa que ha mostrado algún interés, pero que aún no ha sido calificado. |
| 3 | **SQL (Sales Qualified Lead)** | Lead que ya fue evaluado y cumple los criterios para que un vendedor lo trabaje activamente. |
| 4 | **Pipeline** | Conjunto de oportunidades abiertas organizadas por etapa del proceso de venta dentro del CRM. |
| 5 | **Forecast** | Proyección de las ventas que se espera cerrar en un periodo. Se revisa semanalmente con el manager. |
| 6 | **Cuota** | Meta de ventas asignada a cada vendedor para un periodo (mensual o trimestral). |
| 7 | **Demo** | Presentación o demostración del producto adaptada a las necesidades específicas del prospecto. |
| 8 | **Churn** | Tasa de clientes que cancelan o no renuevan. Es clave para entender la retención y la calidad de las ventas. |

---

## 4. Plan de lecturas de la primera semana

| Día | Documento | Descripción |
|-----|-----------|-------------|
| **Lunes** | **1. Manual de cultura y valores de [Empresa]** | Historia de la empresa, misión, visión, valores y forma de trabajar. Ayuda a entender el "por qué" detrás de lo que hacemos. |
| **Martes** | **2. Guía de producto / catálogo de servicios** | Descripción de cada producto, sus funcionalidades, beneficios, precios y casos de uso principales. |
| **Miércoles** | **3. Playbook de ventas** | Proceso comercial paso a paso: etapas del pipeline, criterios de calificación, guiones de llamada, plantillas de correo y manejo de objeciones. |
| **Jueves** | **4. Análisis de competencia (battlecards)** | Comparativa con los principales competidores: fortalezas, debilidades y argumentos para diferenciarnos. |
| **Viernes** | **5. Casos de éxito de clientes** | Historias reales de clientes con el problema, la solución y los resultados obtenidos. Son útiles como referencia en conversaciones con prospectos. |

**Sugerencia:** el viernes, revisar con el manager las dudas surgidas de las cinco lecturas.

---

## 5. Mensaje de Slack del manager (día 1)

> ¡Hola, [Nombre]! 👋
>
> Bienvenido/a oficialmente al equipo de ventas de [Empresa]. 🎉 Estamos muy contentos de tenerte aquí.
>
> Te dejo lo esencial para hoy:
> 📅 **10:00:** presentación con el equipo en [sala/enlace]
> 🤝 **12:00:** café con [Nombre del buddy], tu buddy
> 🗓️ **16:00:** nuestro 1:1 para hablar de tus primeros 90 días
>
> 📌 Canales que te recomiendo unirte: #ventas, #anuncios, #wins y #producto
> 📂 El plan de lecturas de la semana está en [enlace]
>
> No te preocupes por saberlo todo hoy. La idea es que conozcas al equipo y te sientas cómodo/a. Cualquier duda, por pequeña que sea, escríbeme por aquí.
>
> ¡Vamos con todo! 🚀
> [Nombre del manager]

---

✅ **Están los 5 sub-objetivos:** carta de bienvenida, 10 pasos del día 1, glosario de 8 términos, plan de 5 lecturas y mensaje de Slack.

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Los 5 sub-objetivos ya están completos en mi respuesta anterior:

| # | Sub-objetivo | Estado | Verificación |
|---|--------------|--------|--------------|
| 1 | Carta de bienvenida personalizada | ✅ Completo | Unas 145 palabras en el cuerpo, con campos personalizables |
| 2 | 10 primeros pasos del día 1 | ✅ Completo | 10 pasos numerados, de la recepción al cierre |
| 3 | Glosario de 8 términos internos | ✅ Completo | 8 términos: ICP, Lead, SQL, Pipeline, Forecast, Cuota, Demo y Churn |
| 4 | Plan de lecturas de la primera semana | ✅ Completo | 5 documentos con descripción, uno por día |
| 5 | Mensaje de Slack del manager | ✅ Completo | Agenda del día, canales, enlace a lecturas y tono cercano |

Solo dos puntos podrían requerir ajuste:

- **Glosario:** son términos estándar de ventas B2B, no jerga propia de tu empresa, porque no la conozco. Si me pasas vuestros términos internos (nombres de productos, siglas, etapas del CRM), lo rehago con ellos.
- **Carta:** si necesitas exactamente 150 palabras, la ajusto.

¿Quieres alguno de estos cambios o el paquete en otro formato, como un documento único para enviar?


## Respuesta completa

Los 5 sub-objetivos ya están completos en mi respuesta anterior:

| # | Sub-objetivo | Estado | Verificación |
|---|--------------|--------|--------------|
| 1 | Carta de bienvenida personalizada | ✅ Completo | Unas 145 palabras en el cuerpo, con campos personalizables |
| 2 | 10 primeros pasos del día 1 | ✅ Completo | 10 pasos numerados, de la recepción al cierre |
| 3 | Glosario de 8 términos internos | ✅ Completo | 8 términos: ICP, Lead, SQL, Pipeline, Forecast, Cuota, Demo y Churn |
| 4 | Plan de lecturas de la primera semana | ✅ Completo | 5 documentos con descripción, uno por día |
| 5 | Mensaje de Slack del manager | ✅ Completo | Agenda del día, canales, enlace a lecturas y tono cercano |

Solo dos puntos podrían requerir ajuste:

- **Glosario:** son términos estándar de ventas B2B, no jerga propia de tu empresa, porque no la conozco. Si me pasas vuestros términos internos (nombres de productos, siglas, etapas del CRM), lo rehago con ellos.
- **Carta:** si necesitas exactamente 150 palabras, la ajusto.

¿Quieres alguno de estos cambios o el paquete en otro formato, como un documento único para enviar?