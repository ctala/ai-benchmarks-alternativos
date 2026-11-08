# DeepSeek V4 Pro — agent_long_horizon/premature_completion_resist

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 76.519s | tokens_per_second: 64.7
- input_tokens: 2054 | output_tokens: 7522

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

## (1) Carta de bienvenida personalizada

**Para:** [Nombre del Vendedor]  
**Asunto:** ¡Bienvenido/a al equipo de Ventas de [Empresa]!

Hola [Nombre],

¡Bienvenido/a al equipo de Ventas en [Empresa]! Estamos encantados de que te unas a nosotros. Tu experiencia en ventas consultivas y tu pasión por ayudar a los clientes serán grandes activos. Confiamos en que tu energía y habilidades acelerarán nuestro éxito en el mercado.  

Nos tomamos muy en serio tu integración: el primer día te reunirás con el equipo, configurarás tus herramientas y conocerás nuestra cultura. Durante las próximas semanas dominarás nuestra metodología de ventas y nuestro portafolio de productos. Valoramos la curiosidad y la colaboración; no dudes en hacer preguntas y compartir ideas. Recuerda que cada pregunta es una oportunidad para crecer; estamos aquí para aprender juntos. Queremos que te sientas parte del equipo desde el minuto uno.  

Tu manager, [Nombre del Manager], y todo el equipo estamos aquí para apoyarte. Estamos seguros de que harás una contribución increíble. Prepárate para un viaje emocionante.  

Un fuerte abrazo,  
El equipo de Ventas de [Empresa]

---

## (2) Lista de los 10 primeros pasos del día 1

1. **Llegada y recepción** – Preséntate en recepción a las 9:00 para recoger tus credenciales, tarjeta de acceso y mapa de la oficina.
2. **Bienvenida del manager** – [Nombre del Manager] te recibirá, te mostrará tu puesto de trabajo y te dará una visión general del día.
3. **Configuración del equipo** – Enciende tu portátil, configura el correo corporativo, Slack, el CRM y las herramientas de calendario (Outlook/Google).
4. **Instalación de plataformas de ventas** – Accede y verifica tu cuenta en Salesforce, Outreach/Gong y la intranet de producto.
5. **Reunión de recursos humanos** – Sesión rápida para firmar documentos, revisar beneficios, políticas de la empresa y recibir tu kit de bienvenida.
6. **Presentación al equipo de ventas** – Reunión breve (virtual o presencial) donde conocerás a los compañeros, sus roles y algún proyecto actual.
7. **Almuerzo de bienvenida** – Comida con tu manager y tu “buddy” asignado para romper el hielo y resolver primeras dudas.
8. **Recorrido por áreas clave** – Paseo por los espacios de producto, marketing, soporte y finanzas para entender quién hace qué.
9. **Primera demo guiada del producto** – Un compañero te mostrará la plataforma, sus módulos principales y responderá preguntas técnicas.
10. **Cierre y plan de semana** – Revisarás con tu manager los objetivos de la semana, accederás al plan de lecturas y confirmarás las sesiones de formación de los próximos días.

---

## (3) Glosario de los 8 términos internos clave

1. **ARR (Ingresos Anuales Recurrentes)** – Valor total de los contratos de suscripción normalizados a un año. Es la métrica estrella de nuestro crecimiento.
2. **ACV (Valor Anual del Contrato)** – Importe promedio que un cliente paga anualmente por un contrato, excluyendo servicios puntuales.
3. **MQL (Marketing Qualified Lead)** – Lead que ha mostrado suficiente interés (descargas, webinars, etc.) para ser transferido al equipo de ventas.
4. **SQL (Sales Qualified Lead)** – Lead que el equipo de ventas ha calificado como oportunidad real tras el primer contacto.
5. **CAC (Coste de Adquisición de Cliente)** – Coste total de marketing y ventas dividido por el número de nuevos clientes conseguidos en un período.
6. **LTV (Valor de Vida del Cliente)** – Ingresos netos que se espera obtener de un cliente a lo largo de toda su relación con nosotros.
7. **ICP (Perfil de Cliente Ideal)** – Conjunto de atributos (sector, tamaño, cargo del decisor, etc.) que definen al cliente que mejor encaja con nuestra solución.
8. **BANT** – Acrónimo que usamos para cualificar oportunidades: Budget (presupuesto), Authority (autoridad), Need (necesidad) y Timeline (calendario de decisión).

---

## (4) Plan de lecturas de la primera semana

**Documento 1: Manual de bienvenida y cultura Empresa**  
Descripción: Presenta nuestra misión, visión, valores y la historia de la compañía. Incluye consejos sobre cómo vivimos el trabajo en equipo y la orientación al cliente. Se recomienda leerlo el primer día.

**Documento 2: Playbook de ventas**  
Descripción: Guía paso a paso de nuestro proceso comercial: fases del pipeline, guiones de descubrimiento, manejo de objeciones y técnicas de cierre. La referencia para toda acción de ventas.

**Documento 3: Guía rápida del producto**  
Descripción: Resumen de los módulos principales, funcionalidades clave y casos de uso más habituales. Incluye enlaces a demos grabadas y fichas de preguntas frecuentes.

**Documento 4: Panorama competitivo**  
Descripción: Análisis de nuestros principales competidores, tabla comparativa de prestaciones, argumentario de ventas (battlecards) y cómo posicionarnos en cada escenario.

**Documento 5: Plan de éxito de los primeros 90 días**  
Descripción: Define las expectativas, métricas (reuniones, pipeline generado, cierres) y los hitos de formación durante el primer trimestre. Incluye calendario de reuniones con el manager.

---

## (5) Mensaje de Slack que el manager le enviará el primer día

**De:** [Nombre del Manager]  
**Para:** [Nombre del Vendedor]  
**Canal:** #onboarding-ventas o DM directo

---

¡Buenos días, [Nombre]! 👋  

Hoy empieza una etapa increíble y todo el equipo está deseando conocerte. Te espero en la recepción a las 9:00; yo mismo te acompañaré a tu mesa y te ayudaré con la primera configuración.  

A las 10:30 tendremos una reunión virtual con el resto del equipo de ventas para que te presenten y nos cuenten en qué están trabajando. Después, comeremos juntos y por la tarde tendrás una primera demo del producto con [Nombre del Compañero].  

Cualquier duda que te surja antes de llegar, o durante el día, escríbeme por aquí sin problema. Mi puerta (y mi Slack) están siempre abiertos.  

¡Nos vemos en un rato! 🚀

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Los 5 sub-objetivos están completos en mi respuesta anterior. Aquí tienes un resumen de verificación rápida:

| # | Sub-objetivo | Estado |
|---|-------------|--------|
| (1) | Carta de bienvenida personalizada (~150 palabras) | ✅ Hecho |
| (2) | Lista de 10 primeros pasos del día 1 | ✅ Hecho |
| (3) | Glosario de 8 términos internos clave | ✅ Hecho |
| (4) | Plan de lecturas de la 1ª semana (5 docs + descripción) | ✅ Hecho |
| (5) | Mensaje de Slack del manager para el día 1 | ✅ Hecho |

El paquete de onboarding está listo y cubre todo lo solicitado. Si necesitas ajustar algún detalle (nombres, empresa, tono, etc.), solo indícamelo.


## Respuesta completa

Los 5 sub-objetivos están completos en mi respuesta anterior. Aquí tienes un resumen de verificación rápida:

| # | Sub-objetivo | Estado |
|---|-------------|--------|
| (1) | Carta de bienvenida personalizada (~150 palabras) | ✅ Hecho |
| (2) | Lista de 10 primeros pasos del día 1 | ✅ Hecho |
| (3) | Glosario de 8 términos internos clave | ✅ Hecho |
| (4) | Plan de lecturas de la 1ª semana (5 docs + descripción) | ✅ Hecho |
| (5) | Mensaje de Slack del manager para el día 1 | ✅ Hecho |

El paquete de onboarding está listo y cubre todo lo solicitado. Si necesitas ajustar algún detalle (nombres, empresa, tono, etc.), solo indícamelo.