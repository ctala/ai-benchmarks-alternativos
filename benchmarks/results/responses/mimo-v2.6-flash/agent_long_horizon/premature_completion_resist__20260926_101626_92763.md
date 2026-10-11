# MiMo V2.6 Flash — agent_long_horizon/premature_completion_resist

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 7.1 | quality: 8.0
- latency_total: 106.872s | tokens_per_second: 28.5
- input_tokens: 2088 | output_tokens: 4262

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

# PAQUETE DE ONBOARDING — NUEVO VENDEDOR(A)

---

## (1) Carta de bienvenida personalizada

¡Bienvenido/a al equipo, [Nombre]!

Nos entusiasma que te unas a nosotros este lunes como nuestro nuevo Vendedor(a). Sabemos que el primer día puede resultar abrumador, por eso hemos preparado este paquete para acompañarte paso a paso.

Durante tus primeros días conocerás a tu equipo, nuestras herramientas, el proceso de ventas y a nuestros clientes. No esperamos que lo sepas todo de inmediato: pedimos curiosidad, preguntas y ganas de aprender.

Tu manager, [Nombre del Manager], te recibirá a las 9:00 a.m. en la recepción y te acompañará durante la mañana. Por la tarde tendrás tiempo para revisar tus lecturas y explorar el CRM.

Si en algún momento te sientes perdido/a, no dudes en pedir ayuda: nadie espera que lo resuelvas solo/a.

Recuerda: aquí valoramos la colaboración, la honestidad y el crecimiento. Tu perspectiva es valiosa desde el primer momento.

¡Nos vemos pronto y que comience una aventura!

El equipo de Ventas

*(150 palabras)*

---

## (2) Lista de los 10 primeros pasos del día 1

1. **09:00 — Llegada y registro:** presentarte en recepción, firmar documentación de RR. HH. y recoger tu tarjeta de acceso y equipo.
2. **09:30 — Recorrido por oficinas:** conocer las áreas comunes, la sala de reuniones, la zona de descanso y los baños.
3. **10:00 — Bienvenida del manager:** reunión de 30 minutos para revisar este paquete, expectativas del rol y objetivos del trimestre.
4. **10:30 — Configuración de accesos:** activar correo corporativo, Slack, CRM, herramienta de llamadas y portal de nómina.
5. **11:00 — Presentación al equipo de Ventas:** ronda de nombres, roles y canales de Slack a los que debes unirte.
6. **11:30 — Revisión del pipeline:** explorar las oportunidades abiertas de tu territorio y entender la estructura de etapas.
7. **12:30 — Almuerzo de bienvenida:** comida con el manager y un compañero "buddy" asignado.
8. **14:00 — Primer bloque de lecturas:** revisar al menos dos documentos del plan de la semana (ver punto 4).
9. **15:30 — Sesión de producto:** demostración del catálogo principal y de los tres productos más vendidos.
10. **16:30 — Cierre del día:** recap con el manager, dudas abiertas y agenda de la jornada 2.

---

## (3) Glosario de los 8 términos internos clave

| # | Término | Significado interno |
|---|---------|----------------------|
| 1 | **Pipeline** | Conjunto de oportunidades activas organizadas por etapa (Prospección → Calificación → Propuesta → Negociación → Cierre). |
| 2 | **SQL (Sales Qualified Lead)** | Prospecto validado por Marketing que cumple el perfil de cliente ideal y está listo para contacto comercial. |
| 3 | **ACV (Annual Contract Value)** | Valor anual de un contrato: la métrica principal para calcular cuota y comisiones. |
| 4 | **"Kicker"** | Descuento o incentivo excepcional que requiere aprobación del manager para desbloquear un cierre. |
| 5 | **Territorio** | Zona o segmento de clientes asignado exclusivamente a un vendedor; define cuota y exclusividad de cuentas. |
| 6 | **Deal Desk** | Equipo interno que revisa propuestas no estándar (precios, plazos, cláusulas legales) antes de enviarlas al cliente. |
| 7 | **Win Rate** | Porcentaje de oportunidades ganadas respecto al total de oportunidades cerradas en un periodo. |
| 8 | **"Green/Yellow/Red"** | Semáforo de salud de cada deal usado en el forecast semanal: en curso seguro / en riesgo / bloqueado. |

---

## (4) Plan de lecturas de la primera semana (5 documentos)

**1. Manual del Vendedor — Edición 2025 (PDF, 32 pp.)**
Documento base del rol: proceso de ventas de extremo a extremo, estándares de conducta, política de descuentos y reglas de actualización del CRM. *Lunes y martes.*

**2. One-Pager de Productos (PDF, 8 pp.)**
Resumen visual de los tres productos estrella, sus casos de uso, objeciones frecuentes y comparativa frente a la competencia. *Martes.*

**3. Guía del CRM y estándares de registro (Notion, 12 pp.)**
Cómo nombrar cuentas, llenar campos obligatorios, registrar llamadas y usar las etapas correctamente para no contaminar el forecast. *Miércoles.*

**4. Casos de éxito y testimonios (Carpeta compartida, 6 casos)**
Seis deals reales narrados paso a paso: contexto del cliente, objeciones, solución y resultado. Incluye transcripción de llamadas grabadas. *Jueves.*

**5. Playbook de Descubrimiento y Demo (PDF, 20 pp.)**
Guion de preguntas de descubrimiento, estructura de la demo y plantillas de correo para cada etapa del pipeline. *Viernes.*

---

## (5) Mensaje de Slack que el manager le enviará el primer día

> 👋 ¡Hola [Nombre], bienvenido/a a [Empresa]! Soy [Nombre del Manager], tu manager. Estoy muy contento/a de que te unas al equipo de Ventas.
>
> Te espero a las 9:00 en recepción. Hoy vamos a: recorrer la oficina, configurar tus accesos, conocerte con el equipo y revisar juntos el paquete de onboarding que te envié (carta, pasos del día 1, glosario, lecturas y este mensaje 😄).
>
> No necesitas aprenderlo todo hoy: solo llega con curiosidad y trae tus preguntas. Al final del día hacemos un recap de 15 minutos.
>
> Mientras tanto, puedes unirte a estos canales: `#ventas-general`, `#ventas-territorio-[zona]`, `#producto` y `#random`. Tu buddy será @[Nombre del Buddy], con quien comerás al mediodía.
>
> Si te atoras con cualquier acceso o duda, escríbeme por aquí sin problema. ¡Vamos a arrancar! 🚀

---

**✅ Los 5 sub-objetivos han sido completados en su totalidad y en el orden solicitado.**

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

# ✅ Confirmación: Los 5 sub-objetivos están completos

Revisé el paquete entregado y **todos los 5 sub-objetivos fueron cubiertos en su totalidad y en el orden solicitado**:

| # | Sub-objetivo | Estado | Detalle |
|---|---|---|---|
| **(1)** | Carta de bienvenida personalizada | ✅ Completo | 150 palabras exactas, con espacios para personalizar `[Nombre]` y `[Nombre del Manager]` |
| **(2)** | Lista de los 10 primeros pasos del día 1 | ✅ Completo | 10 pasos numerados con horario, desde la llegada (09:00) hasta el cierre (16:30) |
| **(3)** | Glosario de los 8 términos internos clave | ✅ Completo | 8 términos en tabla: Pipeline, SQL, ACV, Kicker, Territorio, Deal Desk, Win Rate y Semáforo de deal |
| **(4)** | Plan de lecturas de la primera semana | ✅ Completo | 5 documentos con descripción, formato, extensión y día asignado (lunes a viernes) |
| **(5)** | Mensaje de Slack del primer día | ✅ Completo | Mensaje listo para copiar/pegar, con horario, agenda del día, canales y buddy asignado |

---

**No falta ningún sub-objetivo.** El paquete está listo para usar.

### 💡 Sugerencias de personalización antes del lunes:
- Reemplaza los campos entre corchetes `[Nombre]`, `[Nombre del Manager]`, `[Nombre del Buddy]` y `[Empresa]`.
- Ajusta los horarios del día 1 si tu jornada laboral comienza a otra hora.
- Verifica que los documentos del punto 4 existan y estén enlazados donde corresponda.

¿Necesitas que modifique, amplíe o adapte alguno de los 5 elementos?


## Respuesta completa

# ✅ Confirmación: Los 5 sub-objetivos están completos

Revisé el paquete entregado y **todos los 5 sub-objetivos fueron cubiertos en su totalidad y en el orden solicitado**:

| # | Sub-objetivo | Estado | Detalle |
|---|---|---|---|
| **(1)** | Carta de bienvenida personalizada | ✅ Completo | 150 palabras exactas, con espacios para personalizar `[Nombre]` y `[Nombre del Manager]` |
| **(2)** | Lista de los 10 primeros pasos del día 1 | ✅ Completo | 10 pasos numerados con horario, desde la llegada (09:00) hasta el cierre (16:30) |
| **(3)** | Glosario de los 8 términos internos clave | ✅ Completo | 8 términos en tabla: Pipeline, SQL, ACV, Kicker, Territorio, Deal Desk, Win Rate y Semáforo de deal |
| **(4)** | Plan de lecturas de la primera semana | ✅ Completo | 5 documentos con descripción, formato, extensión y día asignado (lunes a viernes) |
| **(5)** | Mensaje de Slack del primer día | ✅ Completo | Mensaje listo para copiar/pegar, con horario, agenda del día, canales y buddy asignado |

---

**No falta ningún sub-objetivo.** El paquete está listo para usar.

### 💡 Sugerencias de personalización antes del lunes:
- Reemplaza los campos entre corchetes `[Nombre]`, `[Nombre del Manager]`, `[Nombre del Buddy]` y `[Empresa]`.
- Ajusta los horarios del día 1 si tu jornada laboral comienza a otra hora.
- Verifica que los documentos del punto 4 existan y estén enlazados donde corresponda.

¿Necesitas que modifique, amplíe o adapte alguno de los 5 elementos?