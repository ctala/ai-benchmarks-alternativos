# Claude Opus 5 — presentation/slide_outline

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.55 | quality: 9.5
- latency_total: 82.071s | tokens_per_second: 71.5
- input_tokens: 217 | output_tokens: 5869
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, cubriendo todos los aspectos solicitados con detalles útiles y estructura adecuada para una presentación ejecutiva.

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

# Presentación: Plataforma Digital 2.0 — Revisión de Estado
**Audiencia:** Consejo de Administración | **Duración estimada:** 25 min presentación + 15 min Q&A

---

## SLIDE 1 — Portada: Plataforma Digital 2.0 — Revisión Trimestral

**Contenido:**
- Nombre del proyecto y versión del reporte (Q1 cierre)
- Fecha, sponsor ejecutivo y líder de proyecto
- Clasificación del documento (Confidencial — Uso interno del Consejo)
- Semáforo global del proyecto: **ÁMBAR**

**Visual sugerido:** Imagen — portada limpia con identidad corporativa, logo del proyecto y un semáforo de estado grande y visible en la esquina superior derecha.

**Notas del presentador:** Abrir declarando el estado ámbar desde el primer segundo para que nadie sienta que se le oculta información. Anunciar la agenda en una frase: "estado, métricas, riesgos, presupuesto, roadmap y tres decisiones que necesito de ustedes hoy".

---

## SLIDE 2 — Resumen Ejecutivo: lo que necesitan saber

**Contenido:**
- El proyecto avanza al **72% de completitud funcional**, con 4 semanas de retraso respecto al plan original
- Presupuesto ejecutado: **58% del total aprobado**, alineado con el avance ajustado
- 2 riesgos críticos activos: integración con el core legacy y disponibilidad del talento especializado
- Fecha de go-live revisada: **de junio a mediados de julio**
- 3 asks concretos al Consejo (detalle en slide 14)

**Visual sugerido:** Tabla — cuadro de mando de 5 filas (Alcance, Tiempo, Costo, Calidad, Riesgo) con semáforo por fila y una columna de tendencia (↑ ↓ →).

**Notas del presentador:** Este es el slide que el Consejo recordará; dedicarle 3 minutos completos. Si solo hubiera tiempo para una diapositiva, sería esta.

---

## SLIDE 3 — Recordatorio: el caso de negocio

**Contenido:**
- Objetivo estratégico: migrar de plataforma monolítica a arquitectura modular para reducir el time-to-market de nuevos productos
- Beneficios comprometidos: reducción de costo operativo de TI, mejora en conversión digital, habilitación de nuevos canales
- Inversión total aprobada y horizonte de retorno original
- Los supuestos del caso de negocio siguen vigentes: **sí, con una revisión menor en el calendario de beneficios**

**Visual sugerido:** Diagrama — línea de tiempo de beneficios con hitos de captura de valor, marcando el desplazamiento de un trimestre.

**Notas del presentador:** El propósito es reanclar al Consejo en el "por qué" antes de entrar en detalle operativo. Enfatizar que el valor del caso de negocio no se ha deteriorado, solo se desplazó en el tiempo.

---

## SLIDE 4 — Estado actual por flujo de trabajo

**Contenido:**
- **Arquitectura y plataforma base:** completado, en operación
- **Migración de datos:** 85%, en curso sin incidencias mayores
- **Módulo de clientes y experiencia:** 70%, en curso
- **Integraciones con sistemas legacy:** 45%, **flujo crítico en retraso**
- **Seguridad y cumplimiento:** 90%, pendiente auditoría externa final

**Visual sugerido:** Gráfico — barras horizontales de progreso por flujo, con línea vertical marcando el avance planeado a la fecha para exponer la brecha visualmente.

**Notas del presentador:** Señalar que 4 de 5 flujos están en verde y que toda la atención de gestión está concentrada en integraciones. Evitar entrar en detalle técnico salvo pregunta directa.

---

## SLIDE 5 — Métricas de progreso: entrega

**Contenido:**
- Historias de usuario completadas: 412 de 570 (72%)
- Velocidad promedio del equipo: estable en los últimos 4 sprints tras la caída del sprint 9
- Cumplimiento de hitos: 7 de 10 entregados en fecha
- Deuda técnica acumulada: dentro del umbral tolerado (<15% del backlog)

**Visual sugerido:** Gráfico — combinado: línea de avance acumulado real vs. planeado (curva S) con barras de velocidad por sprint en eje secundario.

**Notas del presentador:** La curva S es la mejor prueba de que el retraso se estabilizó y ya no está creciendo. Mencionar que la caída del sprint 9 se explicó por la rotación de dos ingenieros senior, ya reemplazados.

---

## SLIDE 6 — Métricas de progreso: calidad

**Contenido:**
- Defectos críticos abiertos: 3 (vs. 11 el trimestre anterior)
- Cobertura de pruebas automatizadas: 78%, objetivo 85%
- Resultados de pruebas de carga: soporta 2.5x el volumen pico actual
- Pruebas de penetración: 1 hallazgo alto remediado, 4 medios en plan
- Satisfacción de usuarios en piloto interno: 4.1 / 5

**Visual sugerido:** Tabla — cuadro de métricas con columnas: Métrica / Actual / Objetivo / Trimestre anterior / Estado.

**Notas del presentador:** El mensaje clave es que el retraso no se está pagando con recortes de calidad, que es la preocupación natural de un Consejo. La tendencia de defectos críticos a la baja es el dato más fuerte de este slide.

---

## SLIDE 7 — Métricas de adopción y valor temprano

**Contenido:**
- Piloto en producción con 2 segmentos de cliente y ~8% del volumen transaccional
- Tiempo de completar la operación clave: reducción de 40% vs. plataforma actual
- Tasa de abandono en el flujo de alta: mejora de 12 puntos porcentuales
- Sin incidencias de severidad 1 en las 6 semanas del piloto
- Aprendizaje principal: la necesidad de rediseñar el flujo de recuperación de contraseña

**Visual sugerido:** Gráfico — barras comparativas "antes vs. después" para 3 métricas de experiencia, más un indicador grande con el % de mejora principal.

**Notas del presentador:** Esta es la diapositiva que convierte el proyecto de gasto en inversión con evidencia. Usarla para construir el crédito que necesitaremos al pedir el presupuesto de contingencia.

---

## SLIDE 8 — Presupuesto: ejecutado vs. planeado

**Contenido:**
- Presupuesto total aprobado vs. comprometido vs. desembolsado a la fecha
- Ejecución: 58% del presupuesto con 72% de avance funcional → **eficiencia favorable**
- Principal desviación: sobrecosto en consultoría de integración (+14% de su partida)
- Compensaciones logradas: ahorro en licenciamiento cloud por renegociación de contrato
- Proyección al cierre: dentro del presupuesto aprobado con **contingencia consumida al 65%**

**Visual sugerido:** Gráfico — barras apiladas o cascada (waterfall) mostrando presupuesto aprobado → desviaciones → ahorros → proyección de cierre.

**Notas del presentador:** El waterfall evita la discusión partida por partida y lleva la atención al número final. Ser explícito en que la contingencia es el verdadero punto de tensión, no el presupuesto base.

---

## SLIDE 9 — Presupuesto: desglose y proyección de flujo

**Contenido:**
- Distribución por categoría: personal interno, consultoría externa, licencias e infraestructura, contingencia
- Curva de gasto trimestral real vs. proyectada hasta el cierre del proyecto
- Necesidad de caja concentrada en Q2 por el pico de esfuerzo de integración
- Compromisos contractuales ya firmados vs. flexibles

**Visual sugerido:** Gráfico — área o líneas de gasto acumulado por trimestre (real y proyectado) con anotación del pico de Q2, acompañado de una dona de distribución por categoría.

**Notas del presentador:** Anticipar la pregunta del CFO sobre cuánto del gasto restante es realmente comprometido e irreversible. Tener la cifra exacta de compromisos firmados a mano.

---

## SLIDE 10 — Riesgos críticos y mitigación

**Contenido:**
- **R1 — Integración con core legacy (Alto/Alto):** documentación deficiente del sistema origen. Mitigación: equipo dedicado + apoyo del proveedor original bajo contrato de soporte extendido
- **R2 — Talento especializado (Alto/Medio):** 3 perfiles clave sin redundancia. Mitigación: plan de retención y contratación de 2 refuerzos externos
- **R3 — Auditoría de cumplimiento (Medio/Alto):** ventana de auditoría externa se solapa con el go-live. Mitigación: adelantar la pre-auditoría a mayo
- **R4 — Adopción del negocio (Medio/Medio):** resistencia en operaciones. Mitigación: plan de gestión del cambio con champions por área
- Riesgos cerrados este trimestre: 2 (estabilidad de arquitectura, capacidad cloud)

**Visual sugerido:** Diagrama — matriz de riesgos 3x3 (probabilidad × impacto) con burbujas numeradas y flechas de movimiento respecto al trimestre anterior.

**Notas del presentador:** Presentar cada riesgo siempre acompañado de su dueño y su acción de mitigación; nunca un riesgo huérfano ante un Consejo. Destacar los 2 riesgos cerrados para demostrar que el proceso de gestión funciona.

---

## SLIDE 11 — Análisis de escenarios de go-live

**Contenido:**
- **Escenario A — Go-live completo en julio:** requiere refuerzo de equipo, mayor costo, menor riesgo operativo
- **Escenario B — Go-live por fases (julio y septiembre):** menor riesgo técnico, beneficios diferidos, costo de operar en paralelo
- **Escenario C — Mantener fecha de junio:** alto riesgo de defectos en producción, **no recomendado**
- Recomendación de la dirección del proyecto: **Escenario B**
- Criterios de decisión: riesgo operativo, captura de beneficios, costo total

**Visual sugerido:** Tabla — matriz comparativa de 3 escenarios × 5 criterios, con la fila de recomendación resaltada y valoración por color.

**Notas del presentador:** Presentar los tres escenarios pero llegar con una recomendación clara y defendible; un Consejo no quiere elegir sin guía. Estar preparado para justificar por qué se descarta mantener la fecha original.

---

## SLIDE 12 — Roadmap Q2: estabilizar y preparar

**Contenido:**
- **Abril:** cierre de integraciones prioritarias y pre-auditoría de seguridad
- **Mayo:** pruebas end-to-end, migración de datos en ensayo completo, capacitación de operaciones
- **Junio:** congelamiento funcional, pruebas de aceptación del negocio, ensayo de go-live
- **Julio:** despliegue de fase 1 (segmentos de cliente principales)
- Hitos de decisión (gates) con criterios de salida definidos en mayo y junio

**Visual sugerido:** Diagrama — cronograma tipo Gantt simplificado por mes, con hitos en forma de diamante y los gates de decisión claramente marcados.

**Notas del presentador:** Enfatizar que los gates son puntos donde el Consejo puede detener o ajustar el proyecto, lo que reduce su exposición. Comprometer la fecha del próximo reporte de avance.

---

## SLIDE 13 — Roadmap Q3: escalar y capturar valor

**Contenido:**
- **Agosto:** ampliación a segmentos restantes y monitoreo intensivo post-despliegue
- **Septiembre:** despliegue de fase 2 (módulos avanzados) y apagado gradual de la plataforma legacy
- Inicio de captura formal de beneficios y medición contra el caso de negocio
- Liberación progresiva del equipo de proyecto hacia el modelo operativo permanente
- Criterio de cierre del proyecto: 3 meses de operación estable + beneficios validados

**Visual sugerido:** Diagrama — roadmap en carriles (entrega, adopción, apagado de legacy, captura de beneficios) sobre eje temporal Q3-Q4.

**Notas del presentador:** El apagado de la plataforma legacy es donde se materializa el ahorro operativo, así que vincularlo explícitamente al caso de negocio. Aclarar que el proyecto tiene una condición de cierre definida y no un final abierto.

---

## SLIDE 14 — Asks al Consejo: tres decisiones

**Contenido:**
- **Ask 1 — Aprobar el Escenario B** (go-live por fases, julio y septiembre) y la nueva línea base de calendario
- **Ask 2 — Liberar el 20% restante de la contingencia** para reforzar el equipo de integración durante Q2
- **Ask 3 — Designar un patrocinador del negocio para gestión del cambio** en operaciones, con dedicación del 50%
- Impacto de no decidir hoy: cada semana de retraso en la decisión desplaza el go-live una semana
- Decisiones que **no** se solicitan: no hay cambio de alcance ni de presupuesto base

**Visual sugerido:** Tabla — tres filas de asks con columnas: Qué se pide / Por qué / Impacto si no se aprueba / Decisión (☐ Aprobado ☐ Rechazado ☐ Diferido).

**Notas del presentador:** Leer los tres asks literalmente y pedir decisión explícita sobre cada uno antes de pasar de página. Aclarar que no se pide dinero nuevo, solo liberar contingencia ya aprobada, para bajar la temperatura de la conversación.

---

## SLIDE 15 — Cierre y próximos pasos

**Contenido:**
- Recapitulación en una línea: proyecto viable, retraso contenido, presupuesto bajo control, se requieren 3 decisiones
- Compromisos de la dirección del proyecto para los próximos 90 días
- Cadencia de reporte: informe mensual al Comité Ejecutivo, reporte completo al Consejo en el próximo trimestre
- Alerta temprana: compromiso de escalar de inmediato cualquier cambio de semáforo a rojo
- Espacio para preguntas

**Visual sugerido:** Imagen — cierre visual sobrio con los 3 asks repetidos en pequeño y los datos de contacto del líder de proyecto y el sponsor.

**Notas del presentador:** Cerrar repitiendo los asks para que sean lo último que escuchen antes del Q&A. Confirmar en voz alta quién es el dueño de cada acción acordada y con qué fecha.

---

## Anexos recomendados (no presentar, tener a mano)

| Anexo | Contenido | Pregunta que responde |
|---|---|---|
| A1 | Registro de riesgos completo | "¿Qué otros riesgos hay?" |
| A2 | Detalle presupuestario por partida y proveedor | "¿En qué se gastó exactamente?" |
| A3 | Estructura del equipo y plan de dotación | "¿Quién está trabajando en esto?" |
| A4 | Arquitectura técnica de alto nivel | "¿Qué construimos exactamente?" |
| A5 | Registro de cambios de alcance aprobados | "¿Cambió el alcance en el camino?" |
| A6 | Comparativa con benchmarks de industria | "¿Este retraso es normal?" |

---

**Notas de diseño general:** Máximo 5 bullets por slide y una sola idea central por diapositiva. Cifras siempre con comparativo (plan, trimestre anterior u objetivo). Usar consistentemente el mismo código de color de semáforo en toda la presentación. Los slides 2, 8, 10 y 14 son los que realmente importan al Consejo: si el tiempo se acorta, presentar solo esos cuatro.