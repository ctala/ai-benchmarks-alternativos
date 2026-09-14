# Gemini 3.8 Flash — agent_long_horizon/premature_completion_resist

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 7.19 | quality: 8.0
- latency_total: 25.609s | tokens_per_second: 118.0
- input_tokens: 1756 | output_tokens: 3237

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

Aquí tienes el paquete completo de onboarding estructurado en los 5 sub-objetivos solicitados:

---

### (1) Carta de bienvenida personalizada

¡Bienvenido/a al equipo comercial!

Estamos muy entusiasmados con tu llegada a la empresa. Desde hoy, eres una pieza fundamental para impulsar nuestro crecimiento y conectar nuestras soluciones con nuevos clientes. Sabemos que tu talento, visión y energía aportarán un valor incalculable a nuestras metas compartidas y al dinamismo del equipo.

Hemos diseñado este proceso de incorporación para acompañarte paso a paso. Durante las próximas semanas, tendrás el tiempo necesario para familiarizarte con nuestros productos, dominar las herramientas de gestión interna y sumergirte en una cultura basada en la colaboración y la excelencia comercial. No te preocupes por saberlo todo desde el inicio; todo el equipo está aquí para apoyarte y resolver tus inquietudes.

Confiamos plenamente en tus habilidades y en el impacto positivo que generarás en cada interacción con nuestros clientes. ¡Mucho éxito en este nuevo camino y una vez más, bienvenido a bordo!

---

### (2) Lista de los 10 primeros pasos del día 1

1. **Recepción y entrega de equipo:** Recoger el ordenador portátil, periféricos y credenciales de acceso con el equipo de TI.
2. **Configuración de cuentas:** Activar correo electrónico corporativo, plataformas de comunicación (Slack) y gestor de contraseñas.
3. **Check-in inicial con RRHH:** Completar la firma de documentación pendiente, alta administrativa y revisión de políticas internas.
4. **Reunión 1:1 de apertura con tu Manager:** Repasar objetivos del onboarding, expectativas mutuas y despejar dudas iniciales.
5. **Presentación con el equipo:** Asistir a la sesión grupal de bienvenida para conocer a tus compañeros del área de ventas.
6. **Conexión con tu "Sales Buddy":** Encuentro informal con tu compañero asignado para resolver dudas prácticas del día a día.
7. **Verificación de accesos al CRM:** Iniciar sesión en el CRM y comprobar permisos básicos para visualización de leads y cuentas.
8. **Almuerzo de integración:** Compartir un almuerzo distendido con el equipo comercial (presencial o virtual).
9. **Revisión de la agenda semanal:** Organizar el calendario de capacitaciones, lecturas y reuniones programadas para los días 2 a 5.
10. **Check-out del Día 1:** Breve sesión de 15 minutos con tu manager para evaluar cómo fue la primera jornada y resolver dudas finales.

---

### (3) Glosario de los 8 términos internos clave que debe conocer

1. **ICP (Ideal Customer Profile):** Descripción detallada del tipo de empresa o cliente que obtiene el mayor valor de nuestro producto y que resulta más rentable para el negocio.
2. **Playbook de Ventas:** Guía maestra interna con nuestros procesos, argumentarios, tratamiento de objeciones y flujos de conversación comerciales.
3. **BANT (Budget, Authority, Need, Timeline):** Marco de cualificación interno que utilizamos para evaluar si un prospecto tiene presupuesto, poder de decisión, necesidad real y plazo de compra.
4. **Deal Stage:** Cada una de las fases oficiales dentro de nuestro pipeline de CRM (desde "Prospección" hasta "Cerrado-Ganado").
5. **Sales Enablement:** Repositorio y equipo dedicado a proveer herramientas, contenidos, demos y formaciones para facilitar el cierre de ventas.
6. **Handover:** Proceso formal de transferencia de un cliente desde Ventas hacia el equipo de Customer Success tras la firma del contrato.
7. **ARR / MRR:** *Annual / Monthly Recurring Revenue*. Métricas financieras clave que representan el valor recurrente anual y mensual de nuestras cuentas contratadas.
8. **Battlecard:** Fichas rápidas de consulta interna con comparativas competitivas frente a competidores específicos y cómo diferenciarnos.

---

### (4) Plan de lecturas de la primera semana (5 documentos con descripción)

1. **Documento 1: "Manual de Cultura, Misión y Valores de la Empresa"**
   * *Descripción:* Documento institucional que describe el origen de la compañía, nuestros pilares culturales, normas de convivencia y la visión a largo plazo.
2. **Documento 2: "Playbook Comercial y Metodología de Venta"**
   * *Descripción:* La biblia de nuestro equipo de ventas; detalla las etapas del embudo comercial, cadencias de contacto recomendadas y mejores prácticas de cierre.
3. **Documento 3: "Catálogo de Soluciones y Matriz de Precios"**
   * *Descripción:* Guía completa de nuestras ofertas, características técnicas, módulos contratables, tiers de precios y políticas de descuentos aplicables.
4. **Documento 4: "Compendio de Battlecards y Análisis Competitivo"**
   * *Descripción:* Informe estratégico con el análisis de nuestros principales competidores en el mercado, matrices FODA y respuestas clave a objeciones comparativas.
5. **Documento 5: "Guía de Buenas Prácticas e Higiene del CRM"**
   * *Descripción:* Protocolo técnico sobre cómo registrar interacciones, mover tratos entre etapas, etiquetar leads y mantener los datos de contacto limpios y actualizados.

---

### (5) Mensaje de Slack que el manager le enviará el primer día

> ¡Hola **[Nombre del Vendedor]**! 👋 ¡Qué alegría tenerte oficialmente con nosotros! 
> 
> Espero que el proceso de configuración del equipo con TI haya ido sobre ruedas. Tómate esta primera mañana con calma para revisar tus accesos y acomodarte. 
> 
> A las **11:30 AM** nos conectamos por videollamada (tienes la invitación en tu calendario de Google) para tener nuestro primer 1:1, hablar sobre la agenda de esta semana y resolver cualquier pregunta que tengas.
> 
> Por cierto, tu *Sales Buddy* será **[Nombre del Buddy]** (ya te enviará un saludo por aquí); no dudes en consultarle cualquier duda práctica del día a día.
> 
> ¡Muchos éxitos en este primer día y bienvenido/a al equipo! 🚀

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Los **5 sub-objetivos requeridos están 100% completos** en la respuesta anterior:

1. **(1) Carta de bienvenida personalizada** *(~150 palabras, tono cercano e inspirador).*
2. **(2) Lista de los 10 primeros pasos del día 1** *(pasos cronológicos desde la recogida de equipo hasta el check-out diario).*
3. **(3) Glosario de los 8 términos internos clave** *(ICP, Playbook, BANT, Deal Stage, Sales Enablement, Handover, ARR/MRR y Battlecard).*
4. **(4) Plan de lecturas de la primera semana** *(5 documentos específicos con su respectiva descripción de contenido).*
5. **(5) Mensaje de Slack que el manager le enviará el primer día** *(plantilla lista para rellenar con nombres y horarios).*

El paquete de onboarding está listo para implementarse. Si deseas adaptar algún nombre de herramienta (como sustituir el CRM genérico por HubSpot o Salesforce), ajustar horarios específicos o añadir algún detalle adicional, solo dímelo.


## Respuesta completa

Los **5 sub-objetivos requeridos están 100% completos** en la respuesta anterior:

1. **(1) Carta de bienvenida personalizada** *(~150 palabras, tono cercano e inspirador).*
2. **(2) Lista de los 10 primeros pasos del día 1** *(pasos cronológicos desde la recogida de equipo hasta el check-out diario).*
3. **(3) Glosario de los 8 términos internos clave** *(ICP, Playbook, BANT, Deal Stage, Sales Enablement, Handover, ARR/MRR y Battlecard).*
4. **(4) Plan de lecturas de la primera semana** *(5 documentos específicos con su respectiva descripción de contenido).*
5. **(5) Mensaje de Slack que el manager le enviará el primer día** *(plantilla lista para rellenar con nombres y horarios).*

El paquete de onboarding está listo para implementarse. Si deseas adaptar algún nombre de herramienta (como sustituir el CRM genérico por HubSpot o Salesforce), ajustar horarios específicos o añadir algún detalle adicional, solo dímelo.