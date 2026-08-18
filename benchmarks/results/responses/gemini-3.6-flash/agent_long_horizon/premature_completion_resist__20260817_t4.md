# Gemini 3.6 Flash — agent_long_horizon/premature_completion_resist

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 7.33 | quality: 8.0
- latency_total: 18.191s | tokens_per_second: 152.9
- input_tokens: 1725 | output_tokens: 3553

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

Aquí tienes el paquete completo de onboarding organizado en los 5 sub-objetivos requeridos:

---

### (1) Carta de bienvenida personalizada

**¡Bienvenido al equipo de Ventas!**

Estamos absolutamente encantados de tenerte con nosotros a partir de este lunes. Tu llegada marca el comienzo de una etapa llena de oportunidades y crecimiento, tanto para ti como para la empresa. Seleccionamos tu perfil porque vimos en ti la pasión, la destreza comercial y la visión estratégica necesarias para llevar nuestras relaciones con los clientes al siguiente nivel.

Sabemos que los primeros días pueden ser abrumadores con tanta nueva información, pero no estás solo. Tienes a todo un equipo respaldándote y listo para ayudarte a adaptarte rápidamente. Nuestro objetivo es darte todas las herramientas y la confianza necesarias para que alcances tus metas e incluso las superes.

Prepárate para aprender, conectar con personas increíbles y cerrar tratos extraordinarios. ¡Tu talento marcará la diferencia aquí!

¡Mucho éxito en este primer día!

Atentamente,  
**El equipo directivo y tu nuevo equipo de trabajo.**

---

### (2) Lista de los 10 primeros pasos del día 1

1. **Recepción y equipo:** Llegada a la oficina / conexión inicial para recibir las credenciales y el equipo de trabajo (laptop y periféricos).
2. **Configuración técnica:** Configurar el correo corporativo, contraseñas y la autenticación de doble factor (2FA).
3. **Plataformas de comunicación:** Unirse a los canales clave de Slack y Teams (canales de la empresa, ventas y anuncios).
4. **Reunión 1 a 1 inicial:** Sesión de bienvenida de 30 minutos con tu Manager directo para alinear expectativas del día.
5. **Configuración del CRM:** Sesión con el equipo de TI/Operaciones para activar y verificar acceso al CRM y herramientas de prospección.
6. **Almuerzo de bienvenida:** Almuerzo (presencial o virtual) con el equipo comercial para conocer a tus compañeros.
7. **Recorrido / Tour:** Tour por las instalaciones físicas de la empresa o recorrido guiado por las plataformas digitales.
8. **Documentación de RR.HH.:** Revisar, completar y firmar la documentación administrativa y de Recursos Humanos.
9. **Conocer a tu Buddy:** Presentación con tu "Onboarding Buddy" (compañero mentor) asignado para guiarte en el día a día.
10. **Check-out del Día 1:** Breve reunión al final de la jornada con tu Manager para resolver dudas y revisar la agenda del Día 2.

---

### (3) Glosario de los 8 términos internos clave que debe conocer

1. **CRM (Customer Relationship Management):** Nuestra plataforma central donde registramos cada interacción, llamada, correo y oportunidad comercial con los clientes.
2. **ARR / MRR (Annual / Monthly Recurring Revenue):** Ingreso Recurrente Anual o Mensual. La métrica principal para medir el valor de nuestros contratos.
3. **MQL (Marketing Qualified Lead):** Prospecto que ha interactuado con nuestro contenido de marketing y cumple con los criterios para ser abordado.
4. **SQL (Sales Qualified Lead):** Prospecto verificado por ventas que cuenta con presupuesto, autoridad, necesidad y tiempo de compra claro (BANT).
5. **Pipeline de Ventas:** Representación visual de todas las oportunidades de negocio activas y las etapas en las que se encuentran dentro del ciclo de venta.
6. **ICP (Ideal Customer Profile):** Descripción del cliente ideal que obtiene el máximo valor de nuestra solución y genera la mayor rentabilidad.
7. **SLA de Ventas (Service Level Agreement):** Compromiso interno sobre el tiempo máximo de respuesta para contactar a un lead asignado (máximo 2 horas).
8. **AE / SDR:** *SDR (Sales Development Rep)* califica la oportunidad; *AE (Account Executive)* realiza las demostraciones, negociaciones y cierra la venta.

---

### (4) Plan de lecturas de la primera semana

1. **Manual de Cultura y Valores de la Empresa**  
   *Descripción:* Documento fundamental que explica la historia, misión, visión y los principios éticos y operativos que rigen nuestras decisiones diarias.
2. **Playbook de Ventas (Sales Playbook)**  
   *Descripción:* Guía maestra del proceso comercial que abarca la metodología de venta, etapas de la oportunidad, scripts de llamadas y manejo de objeciones comunes.
3. **Matriz de Productos y Argumentario de Competencia**  
   *Descripción:* Resumen detallado de las soluciones que vendemos, la estructura de precios, casos de uso y comparativas clave contra competidores del mercado.
4. **Guía de Procesos e Integración del CRM**  
   *Descripción:* Manual paso a paso sobre las mejores prácticas para registrar clientes, mover negocios en el pipeline y mantener la higiene de datos en el sistema.
5. **Historias de Éxito y Casos de Estudio de Clientes**  
   *Descripción:* Compilación de ejemplos reales sobre cómo ayudamos a nuestros clientes a resolver sus problemas y el ROI (retorno de inversión) que generamos para ellos.

---

### (5) Mensaje de Slack que el manager le enviará el primer día

> ¡Hola **[Nombre del Empleado]**! 👋 ¡Súper bienvenido/a oficialmente al equipo de Ventas! 🎉  
> 
> Estamos muy entusiasmados de que empieces hoy con nosotros. En tu correo ya tienes la agenda detallada para esta semana, pero para empezar con calma, a las 10:00 AM nos conectaremos a nuestra primera reunión 1 a 1 para saludarnos y revisar los pasos del día.  
> 
> Tu "buddy" asignado/a es **[Nombre del Buddy]**, quien te acompañará para resolver cualquier duda rápida que tengas sobre la marcha.  
> 
> Tómate estas primeras horas para configurar tu equipo, tus accesos y tu perfil. ¡Nos vemos en un rato! 🚀

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

El paquete de onboarding está **100% completo** y contiene los 5 sub-objetivos solicitados en la respuesta anterior:

1. **Carta de bienvenida personalizada** (~150 palabras) ✅
2. **Lista de los 10 primeros pasos del día 1** ✅
3. **Glosario de los 8 términos internos clave** ✅
4. **Plan de lecturas de la primera semana** (5 documentos con descripción) ✅
5. **Mensaje de Slack del manager** ✅

Puedes revisar el texto completo en el mensaje anterior. Si necesitas que haga algún ajuste, cambie algún nombre de variable o personalice algún detalle adicional, dime y con gusto lo adapto.


## Respuesta completa

El paquete de onboarding está **100% completo** y contiene los 5 sub-objetivos solicitados en la respuesta anterior:

1. **Carta de bienvenida personalizada** (~150 palabras) ✅
2. **Lista de los 10 primeros pasos del día 1** ✅
3. **Glosario de los 8 términos internos clave** ✅
4. **Plan de lecturas de la primera semana** (5 documentos con descripción) ✅
5. **Mensaje de Slack del manager** ✅

Puedes revisar el texto completo en el mensaje anterior. Si necesitas que haga algún ajuste, cambie algún nombre de variable o personalice algún detalle adicional, dime y con gusto lo adapto.