# Claude Sonnet 5.5 — presentation/slide_outline

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.75 | quality: 9.22
- latency_total: 29.729s | tokens_per_second: 136.2
- input_tokens: 219 | output_tokens: 4050
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

# Outline: Estado del Proyecto "Plataforma Digital 2.0"
**Audiencia:** Board de directores | **Duración sugerida:** 30-35 min + 10 min de Q&A

> Los datos entre [corchetes] son placeholders que deben reemplazarse con cifras reales.

---

## SECCIÓN 1: APERTURA

### Slide 1: Portada
- Plataforma Digital 2.0: Informe de Estado al Board
- Fecha de la sesión y período cubierto [Q1 20XX]
- Presentador y sponsor ejecutivo del proyecto
- Clasificación: Confidencial

**Visual:** Imagen de marca con el logo del proyecto y un fondo limpio.
**Notas:** Abre indicando que la sesión tiene tres objetivos: informar el estado, transparentar riesgos y obtener decisiones puntuales del board.

### Slide 2: Resumen ejecutivo
- Estado general: [Verde/Amarillo/Rojo], con [X]% de avance vs. [Y]% planeado
- Presupuesto: [X]% ejecutado vs. [Y]% planeado
- Principal riesgo: [descripción breve]
- Se requieren [N] decisiones del board hoy

**Visual:** Una sola diapositiva con 4 tarjetas de indicadores (avance, presupuesto, riesgo, asks).
**Notas:** Si el board solo recuerda esta slide, debe bastar para entender la situación. Adelanta que los asks están al final, pero que ya están anticipados aquí.

### Slide 3: Contexto y objetivos del proyecto
- Problema de negocio que resuelve la Plataforma 2.0
- Objetivos estratégicos: [ej. reducir costos operativos, aumentar conversión, escalar a nuevos mercados]
- Alcance aprobado y fecha de lanzamiento objetivo
- Inversión total aprobada: [$X]

**Visual:** Diagrama simple de "de dónde venimos / a dónde vamos" (Plataforma 1.0 → 2.0).
**Notas:** Recuerda brevemente el porqué del proyecto, sin extenderte. Conecta con la estrategia corporativa vigente.

---

## SECCIÓN 2: ESTADO Y PROGRESO

### Slide 4: Estado general por flujo de trabajo
- Semáforo por frente: Producto, Tecnología, Datos/Integraciones, Seguridad, Change Management
- Tendencia vs. el período anterior (↑ ↔ ↓)
- Frente con mayor desviación: [nombre y causa]
- Frente destacado positivamente: [nombre]

**Visual:** Tabla tipo semáforo (RAG) con columnas de estado, tendencia y comentario.
**Notas:** Sé directo con los rojos y amarillos. Indica que cada uno se desarrolla en la sección de riesgos.

### Slide 5: Hitos completados y logros clave
- [Hito 1] completado el [fecha] (a tiempo / con [X] días de retraso)
- [Hito 2]: ej. migración de [N] módulos al nuevo core
- [Hito 3]: ej. piloto con [N] usuarios o clientes
- Aprendizajes relevantes que ajustaron el plan

**Visual:** Línea de tiempo horizontal con hitos marcados (completado, en curso, pendiente).
**Notas:** Resalta 2 o 3 logros que importen al negocio, no solo al equipo técnico.

### Slide 6: Métricas de progreso vs. plan
- Avance global: [X]% real vs. [Y]% planeado
- Entregables completados: [N] de [M]
- Velocidad del equipo y tendencia de los últimos [N] sprints
- Variación de cronograma: [+/- X semanas]

**Visual:** Gráfico de líneas con curva S (avance planeado vs. real) y un indicador de variación.
**Notas:** Explica la causa de cualquier brecha entre planeado y real. Evita tecnicismos como story points; traduce a entregables.

### Slide 7: Métricas de impacto en negocio
- Adopción: [X]% de usuarios migrados a la nueva plataforma
- KPI 1: [ej. tiempo de proceso reducido en X%]
- KPI 2: [ej. NPS/CSAT de [X] vs. línea base de [Y]]
- Beneficios proyectados vs. capturados a la fecha

**Visual:** Gráfico de barras comparando línea base, actual y meta, con 3 o 4 KPIs.
**Notas:** Es la slide que más conecta con el board. Si aún no hay impacto medible, preséntalo como indicadores adelantados y aclara cuándo se esperan resultados.

### Slide 8: Calidad y desempeño técnico
- Disponibilidad y desempeño: [uptime X%, latencia Y ms]
- Calidad: defectos críticos abiertos [N], tendencia a la baja
- Deuda técnica y cobertura de pruebas: [X]%
- Estado de seguridad: hallazgos de auditoría [abiertos/cerrados]

**Visual:** Dashboard con 4 indicadores tipo velocímetro o tarjetas y mini-tendencias.
**Notas:** Mantén el nivel ejecutivo: lo importante es si la plataforma es estable y segura para escalar.

---

## SECCIÓN 3: RIESGOS Y PRESUPUESTO

### Slide 9: Principales riesgos
- Riesgo 1: [ej. dependencia de proveedor clave] (probabilidad Alta, impacto Alto)
- Riesgo 2: [ej. disponibilidad de talento especializado]
- Riesgo 3: [ej. resistencia al cambio / adopción]
- Riesgo 4: [ej. cumplimiento regulatorio]
- Cambios desde el último reporte: [nuevos / cerrados]

**Visual:** Matriz de calor (probabilidad vs. impacto) con los riesgos ubicados.
**Notas:** Presenta máximo 4 o 5 riesgos. Señala cuáles requieren intervención del board.

### Slide 10: Plan de mitigación y problemas activos
- Por cada riesgo top: acción, responsable y fecha
- Issues materializados y su impacto en plazo o costo
- Planes de contingencia activados o en preparación
- Riesgos que escalan a decisión del board (vinculados a los asks)

**Visual:** Tabla con columnas Riesgo | Mitigación | Responsable | Fecha | Estado.
**Notas:** Demuestra control: cada riesgo tiene dueño y plan. Conecta explícitamente con los asks de la slide 14.

### Slide 11: Presupuesto ejecutado vs. planeado
- Presupuesto total aprobado: [$X] | Ejecutado a la fecha: [$Y] ([Z]%)
- Variación vs. plan: [+/- $ y %] y sus causas principales
- Desglose por categoría: personal, licencias, infraestructura, terceros
- Compromisos ya contratados pero aún no facturados: [$X]

**Visual:** Gráfico de barras agrupadas (planeado vs. real por categoría) y una línea acumulada.
**Notas:** Explica las variaciones con claridad: si es timing de gasto o sobrecosto real. Esa distinción es lo primero que preguntará el board.

### Slide 12: Proyección financiera (Estimate at Completion)
- Costo estimado a la finalización: [$X] vs. presupuesto de [$Y]
- Escenarios: base, optimista y pesimista
- Reserva de contingencia: [$X] disponible, [$Y] comprometida
- Retorno esperado: ROI y payback actualizados [X meses]

**Visual:** Gráfico de cascada (waterfall) del presupuesto original al EAC, más una mini-tabla de escenarios.
**Notas:** Deja claro si el proyecto cerrará dentro del presupuesto. Si se requiere fondeo adicional, esta slide prepara el terreno para el ask.

---

## SECCIÓN 4: FUTURO Y DECISIONES

### Slide 13: Roadmap Q2-Q3
- Q2: [entregables y hitos principales, ej. lanzamiento de módulo X, migración fase 2]
- Q3: [entregables y hitos principales, ej. go-live general, desactivación de plataforma legacy]
- Dependencias críticas y ruta crítica
- Puntos de decisión (gates) y criterios de éxito por fase

**Visual:** Diagrama Gantt simplificado por trimestre, con hitos (rombos) y dependencias.
**Notas:** Resalta los 3 hitos más importantes y los gates donde volverás al board. Aclara qué cambió respecto al plan original.

### Slide 14: Asks al board
- **Decisión 1:** [ej. aprobar fondos adicionales de $X para contingencia]
- **Decisión 2:** [ej. autorizar extensión de contrato con proveedor clave]
- **Decisión 3:** [ej. patrocinio ejecutivo para el plan de adopción/cambio]
- Para cada ask: qué se pide, por qué ahora y qué pasa si no se aprueba

**Visual:** Tabla de 3 filas (Ask | Justificación | Impacto si no se aprueba | Fecha límite).
**Notas:** Sé específico y pide una decisión concreta por ask. Deja esta slide en pantalla durante el Q&A.

### Slide 15: Próximos pasos y cierre
- Resumen: dónde estamos, qué viene y qué necesitamos
- Acciones inmediatas tras la sesión (próximos 30 días)
- Cadencia de reporte al board: [mensual/trimestral]
- Preguntas y discusión

**Visual:** Checklist o línea de 30-60-90 días y datos de contacto.
**Notas:** Cierra repitiendo los asks en una frase y confirma qué decisiones quedan registradas en acta. Abre el espacio de preguntas.

---

## Apéndice sugerido (fuera de las 15 slides)
- Detalle de presupuesto por categoría
- Registro completo de riesgos
- Métricas técnicas detalladas
- Glosario de términos

**Recomendación:** Si los datos son más favorables o más críticos de lo previsto, ajusta el énfasis. Con malas noticias, mueve los riesgos y asks antes (slide 4 o 5). Con buenas noticias, mantén el orden actual.