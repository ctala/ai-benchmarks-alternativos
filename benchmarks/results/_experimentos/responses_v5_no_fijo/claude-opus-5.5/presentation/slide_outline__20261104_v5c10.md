# Claude Opus 5.5 — presentation/slide_outline

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.77 | quality: 9.52
- latency_total: 51.861s | tokens_per_second: 105.4
- input_tokens: 219 | output_tokens: 5468
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
**Audiencia:** Board de Directores | **Duración sugerida:** 25-30 min + Q&A

> **Nota:** Las cifras entre [corchetes] son ilustrativas. Reemplázalas con los datos reales del proyecto.

---

## SECCIÓN 1: APERTURA

### Slide 1: Plataforma Digital 2.0: Estado del Proyecto y Próximos Pasos
- Título del proyecto y subtítulo: "Informe al Board de Directores"
- Fecha de la sesión y periodo reportado (ej. cierre Q1)
- Nombre y cargo del presentador (Sponsor ejecutivo / PMO)
- Clasificación: Confidencial

**Visual:** Imagen de portada con mockup de la plataforma y logo corporativo
**Notas del presentador:** Agradecer el tiempo del board y anticipar que al final habrá decisiones concretas que solicitar. Indicar que la presentación dura unos 25 minutos.

---

### Slide 2: Resumen Ejecutivo
- Estado general del proyecto: **Amarillo**, avance [62%] vs [68%] planeado
- Presupuesto ejecutado: [$4.2M] de [$7.5M] (56%), dentro del rango tolerado
- Hitos clave logrados: lanzamiento del MVP y migración del [40%] de usuarios
- Riesgo principal: retraso en la integración con el sistema de pagos
- Solicitamos 3 decisiones al board (detalle en slide 14)

**Visual:** Dashboard de una página con 4 tarjetas KPI (Avance, Presupuesto, Riesgos, Fecha de go-live) con código de semáforo
**Notas del presentador:** Si el board solo recordara una slide, debería ser esta. Hay que comunicar el mensaje central: el proyecto avanza con una desviación manejable y requiere decisiones puntuales para mantener la fecha de lanzamiento.

---

### Slide 3: Recordatorio: Objetivos y Alcance del Proyecto
- Objetivo estratégico: modernizar la experiencia digital del cliente y reducir costos operativos
- Metas comprometidas: [+25%] en conversión digital, [-30%] en costos de soporte y [99.9%] de disponibilidad
- Alcance: app móvil, portal web, nueva arquitectura cloud e integraciones core
- Periodo total: [Q3 año anterior] a [Q4 año actual]; inversión aprobada de [$7.5M]

**Visual:** Diagrama de los 4 pilares del proyecto con sus objetivos medibles debajo de cada uno
**Notas del presentador:** Recordar brevemente por qué el board aprobó esta inversión, para que el resto de la presentación se evalúe contra esos compromisos originales. Dedicar menos de un minuto.

---

## SECCIÓN 2: ESTADO ACTUAL

### Slide 4: Estado Actual por Frente de Trabajo
- Frontend y UX: **Verde**, diseño completado y desarrollo al [80%]
- Arquitectura cloud: **Verde**, infraestructura productiva operativa
- Integraciones (pagos, ERP, CRM): **Rojo**, [6 semanas] de retraso en pagos
- Migración de datos: **Amarillo**, [40%] migrado y calidad de datos por debajo de lo esperado
- Gestión del cambio y capacitación: **Amarillo**, plan definido y ejecución iniciando

**Visual:** Tabla de semáforo con columnas: Frente | Estado | Avance % | Responsable | Comentario
**Notas del presentador:** Enfocar la atención en el frente rojo y explicar que es el único con impacto potencial en la fecha final. No hay que detenerse en los frentes verdes.

---

### Slide 5: Hitos Completados en el Periodo
- Lanzamiento del MVP a [5,000] usuarios piloto
- Migración de infraestructura a la nube completada sin incidentes críticos
- Auditoría de seguridad aprobada sin hallazgos de severidad alta
- Equipo completo contratado: [45] personas entre internos y proveedor
- Firma del contrato con el nuevo proveedor de pagos

**Visual:** Línea de tiempo horizontal con hitos marcados como completados (check verde) y su fecha real vs planeada
**Notas del presentador:** Reconocer los logros del equipo genera confianza antes de hablar de riesgos. Destacar que la auditoría de seguridad era un requisito regulatorio crítico.

---

## SECCIÓN 3: MÉTRICAS DE PROGRESO

### Slide 6: Avance del Proyecto: Real vs Planeado
- Avance físico acumulado: [62%] real vs [68%] planeado (desviación de -6 pts)
- SPI (Schedule Performance Index): [0.91], por debajo de 0.95, lo que requiere atención
- Velocidad del equipo: [+15%] en el último trimestre tras ajustes de proceso
- Proyección: recuperar la brecha en Q2 si se aprueban los recursos solicitados

**Visual:** Gráfico de líneas con la Curva S (avance planeado vs real acumulado por mes) y proyección punteada
**Notas del presentador:** La desviación es real pero está acotada, y la tendencia de los últimos dos meses muestra recuperación. Conviene explicar el SPI en términos simples: por cada semana planeada estamos logrando el equivalente a 0.91 semanas.

---

### Slide 7: Primeros Resultados de Negocio (Piloto)
- Conversión digital en el piloto: [+18%] vs plataforma actual (meta: +25%)
- Satisfacción de usuarios (NPS): [52] vs [31] en la plataforma legacy
- Tiempo de carga: reducción de [4.2s] a [1.1s]
- Tickets de soporte por usuario: [-22%]
- Tasa de adopción del piloto: [74%] de usuarios activos semanales

**Visual:** Gráfico de barras comparativo (Legacy vs Plataforma 2.0) para cada KPI, con línea de meta
**Notas del presentador:** Estos son resultados tempranos con una muestra limitada, pero validan la tesis de inversión. El NPS es la señal más fuerte de que vamos en la dirección correcta.

---

## SECCIÓN 4: PRESUPUESTO

### Slide 8: Presupuesto Ejecutado vs Planeado
- Presupuesto total aprobado: [$7.5M]
- Ejecutado a la fecha: [$4.2M] vs [$4.5M] planeado (un 7% por debajo)
- CPI (Cost Performance Index): [0.96]; considerando el avance real, el costo por unidad de trabajo es ligeramente superior al plan
- Desglose: personal [55%], licencias y cloud [25%], proveedores externos [15%], contingencia [5%]

**Visual:** Gráfico de barras agrupadas por trimestre (Planeado vs Ejecutado) más un gráfico de dona con la distribución por categoría
**Notas del presentador:** Hay que aclarar que gastar menos no significa ahorrar: refleja en parte el retraso en integraciones. El indicador relevante es el CPI, que está en rango aceptable.

---

### Slide 9: Análisis de Desviaciones y Proyección al Cierre
- Sobrecosto en proveedor de integraciones: [+$320K] por cambios de alcance técnico
- Ahorro en infraestructura cloud: [-$180K] por optimización de arquitectura
- Contingencia utilizada: [40%] del fondo asignado
- Estimación al cierre (EAC): [$7.9M], es decir [+5%] sobre lo aprobado
- Opciones para cerrar la brecha: repriorizar alcance o aprobar una ampliación

**Visual:** Gráfico de cascada (waterfall) desde el presupuesto aprobado hasta la proyección final, mostrando cada desviación
**Notas del presentador:** Ser transparente: con la trayectoria actual cerraremos un 5% por encima. Esta slide prepara uno de los asks de la slide 14.

---

## SECCIÓN 5: RIESGOS

### Slide 10: Principales Riesgos del Proyecto
- **R1, Integración de pagos (Alto/Alto):** el retraso del proveedor puede mover el go-live
- **R2, Calidad de datos (Alto/Medio):** los datos legacy inconsistentes ralentizan la migración
- **R3, Retención de talento clave (Medio/Alto):** hay alta demanda de perfiles cloud en el mercado
- **R4, Adopción interna (Medio/Medio):** existe resistencia al cambio en áreas operativas
- **R5, Regulatorio (Bajo/Alto):** posibles cambios normativos en protección de datos

**Visual:** Matriz de riesgos 3x3 (Probabilidad vs Impacto) con los 5 riesgos posicionados como burbujas numeradas
**Notas del presentador:** Hay dos riesgos en la zona roja que requieren atención del board. Los demás están siendo gestionados por el comité del proyecto.

---

### Slide 11: Planes de Mitigación
- R1: equipo dedicado con el proveedor, penalidades contractuales activadas y plan B con un proveedor alterno evaluado
- R2: herramienta de limpieza de datos y equipo de data stewards por área de negocio
- R3: bonos de retención para [8] roles críticos y documentación de conocimiento
- R4: red de "champions" por área y programa de capacitación escalonado
- Revisión quincenal de riesgos en el Comité Directivo del proyecto

**Visual:** Tabla con columnas: Riesgo | Acción de mitigación | Responsable | Fecha | Estado
**Notas del presentador:** Cada riesgo tiene un dueño con nombre y apellido y una fecha de resolución. Para R1 y R3 necesitamos apoyo del board, que se detalla en los asks.

---

## SECCIÓN 6: ROADMAP

### Slide 12: Roadmap Q2-Q3
- **Q2:** cierre de integración de pagos, migración al [80%] y lanzamiento de la app móvil (beta)
- **Q2:** capacitación de [1,200] empleados y despliegue de la red de champions
- **Q3:** lanzamiento general (go-live) para el 100% de clientes en [agosto]
- **Q3:** apagado progresivo de la plataforma legacy e hipercuidado post-lanzamiento
- Hito de decisión: Go/No-Go del lanzamiento general a fines de [julio]

**Visual:** Diagrama de Gantt simplificado por trimestre y frente de trabajo, con hitos marcados como diamantes y el punto de Go/No-Go destacado
**Notas del presentador:** La fecha de go-live de agosto se mantiene, pero tiene menos holgura que antes. El punto Go/No-Go de julio es donde el board recibirá la siguiente actualización formal.

---

### Slide 13: Dependencias Críticas y Supuestos
- Entrega del proveedor de pagos antes del [30 de mayo]
- Disponibilidad de usuarios de negocio para pruebas UAT ([20] personas, 4 semanas)
- Congelamiento de cambios en sistemas core durante julio-agosto
- Aprobación regulatoria del nuevo flujo de onboarding digital

**Visual:** Diagrama de dependencias (flujo) que conecta cada dependencia con el hito del roadmap que habilita
**Notas del presentador:** Si alguna de estas dependencias falla, el go-live de agosto está en riesgo. Varias requieren coordinación entre áreas que está fuera del control directo del proyecto.

---

## SECCIÓN 7: DECISIONES Y CIERRE

### Slide 14: Solicitudes al Board
- **Ask 1, Presupuesto:** aprobar una ampliación de [$400K] (+5%) para cubrir la brecha proyectada y reponer la contingencia
- **Ask 2, Talento:** autorizar un paquete de retención de [$150K] para 8 roles críticos (incluido en el Ask 1)
- **Ask 3, Priorización:** respaldar el congelamiento de cambios en sistemas core durante julio-agosto, con comunicación desde la dirección
- Alternativa si no se aprueba el Ask 1: reducir el alcance diferiendo [módulo X] a Q4

**Visual:** Tabla de decisiones con columnas: Solicitud | Monto/Impacto | Justificación | Consecuencia de no aprobar
**Notas del presentador:** Esta es la slide más importante de la sesión, así que conviene presentar cada ask con claridad y pedir una decisión explícita. Mostrar la alternativa demuestra que hemos evaluado opciones y no solo pedimos más dinero.

---

### Slide 15: Próximos Pasos y Preguntas
- Próxima actualización al board: sesión Go/No-Go a fines de [julio]
- Reporte ejecutivo mensual por escrito a los miembros del board
- Acciones inmediatas tras esta sesión: formalizar decisiones y comunicarlas al equipo
- Contacto: [Sponsor ejecutivo] y [Director de PMO]
- Espacio para preguntas y discusión

**Visual:** Imagen limpia con resumen de 3 próximos pasos en íconos y el texto "Preguntas" destacado
**Notas del presentador:** Resumir las decisiones tomadas durante la sesión antes de abrir preguntas, para que queden registradas en el acta. Agradecer el apoyo continuo del board.

---

## Recomendaciones adicionales
- **Anexos de respaldo:** prepara slides extra (detalle financiero por partida, plan B de pagos, organigrama del equipo) para responder preguntas sin saturar la presentación principal.
- **Pre-lectura:** envía la slide 2 y la slide 14 al board 48 horas antes de la sesión, para que lleguen preparados a decidir.
- **Consistencia visual:** usa el mismo código de colores (verde/amarillo/rojo) en todas las slides de estado y riesgos.