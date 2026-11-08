# Claude Haiku 5.5 — presentation/slide_outline

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.55 | quality: 9.52
- latency_total: 18.899s | tokens_per_second: 217.5
- input_tokens: 217 | output_tokens: 4110
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

Aquí tienes un outline completo para la presentación. Como no tengo datos reales del proyecto, he usado marcadores entre corchetes (por ejemplo [X%], [$XXX K]) que puedes reemplazar con las cifras correctas. Si me compartes métricas, fechas y riesgos concretos, puedo afinar el contenido.

# Presentación: Estado del Proyecto "Plataforma Digital 2.0"
**Audiencia:** Board de Directores
**Duración sugerida:** 20-25 minutos + 10 de preguntas

---

## Slide 1. Portada
- Proyecto: Plataforma Digital 2.0
- Subtítulo: Estado de avance y decisiones requeridas
- Fecha de corte del reporte: [DD/MM/AAAA]
- Presentado por: [Nombre, rol]

**Tipo de visual:** Imagen de marca o logotipo del proyecto con fondo limpio.
**Notas del presentador:** Anuncia que la sesión tiene dos objetivos: informar el avance y obtener tres decisiones específicas al final. Esto fija expectativas desde el inicio.

---

## Slide 2. Resumen ejecutivo
- Avance global: [XX]% completado, [en/por encima/por debajo] del plan original
- Estado general: [Verde / Amarillo / Rojo] con [N] riesgos críticos abiertos
- Presupuesto: [XX]% ejecutado con [XX]% de avance físico
- Hito reciente: [Lanzamiento de módulo X / Cierre de fase Y]
- Solicitudes: 3 decisiones que requieren aprobación hoy

**Tipo de visual:** Tarjetas de KPI (4 tarjetas con semáforo de color).
**Notas del presentador:** Da la respuesta completa en esta slide: si el proyecto va bien, mal o con reservas. Los directores valoran la claridad desde el primer minuto.

---

## Slide 3. Objetivos del proyecto y alcance
- Objetivo estratégico: [Ej. Aumentar ingresos digitales en X%]
- Alcance incluido: [módulos o funcionalidades principales]
- Fuera de alcance: [elementos excluidos explícitamente]
- Beneficiarios: [clientes, áreas internas, socios]
- Criterios de éxito: [2-3 métricas medibles]

**Tipo de visual:** Diagrama de alcance (dentro/fuera) o tabla de objetivos vs. metas.
**Notas del presentador:** Recuerda el propósito original para que el board evalúe el avance contra la intención, no solo contra las tareas. Aclara lo que no está incluido para evitar expectativas erróneas.

---

## Slide 4. Estado actual por fase
- Fase 1 (Diseño y arquitectura): [Completada / % avance]
- Fase 2 (Desarrollo core): [Completada / % avance]
- Fase 3 (Integraciones): [En curso / % avance]
- Fase 4 (Pruebas y lanzamiento): [Pendiente]
- Próximo hito crítico: [fecha y descripción]

**Tipo de visual:** Diagrama de Gantt simplificado o barra de progreso por fase.
**Notas del presentador:** Señala en qué fase estamos hoy y cuál es el siguiente hito que puede cambiar el rumbo. Menciona si alguna fase está en la ruta crítica.

---

## Slide 5. Métricas de progreso: avance físico
- Entregables completados: [N] de [N] planeados
- Historias de usuario o features cerrados: [N] ([XX]%)
- Módulos en producción, staging y desarrollo
- Velocidad del equipo: [tendencia de los últimos sprints]
- Desviación frente a la línea base: [+/- X semanas]

**Tipo de visual:** Gráfico de burndown o curva S (planeado vs. real).
**Notas del presentador:** Explica la diferencia entre lo planeado y lo real con números concretos. Si hay desviación, indica si es recuperable y en cuánto tiempo.

---

## Slide 6. Métricas de progreso: calidad y adopción
- Defectos críticos abiertos: [N] (meta: 0 antes de lanzamiento)
- Cobertura de pruebas: [XX]%
- Disponibilidad en entornos de prueba: [XX]%
- Usuarios piloto activos: [N] / [meta]
- Feedback de piloto: [score de satisfacción o NPS preliminar]

**Tipo de visual:** Tablero de indicadores con semáforos o tendencia mensual.
**Notas del presentador:** Conecta la calidad con el riesgo de lanzamiento. Un board quiere saber si el producto está listo, no solo si el código avanza.

---

## Slide 7. Hitos completados últimos 90 días
- [Hito 1]: completado el [fecha], impacto: [descripción]
- [Hito 2]: completado el [fecha], impacto: [descripción]
- [Hito 3]: completado el [fecha], impacto: [descripción]
- [Hito 4]: completado el [fecha], impacto: [descripción]

**Tipo de visual:** Línea de tiempo horizontal con hitos marcados.
**Notas del presentador:** Reconoce al equipo en los logros más relevantes. Elige los hitos que demuestran valor de negocio, no solo actividad técnica.

---

## Slide 8. Presupuesto: ejecutado vs. planeado
- Presupuesto aprobado total: [$XXX M]
- Ejecutado a la fecha: [$XXX M] ([XX]%)
- Avance físico: [XX]% (relación costo-avance: [índice])
- Proyección al cierre: [$XXX M] ([+/- X%] vs. aprobado)
- Principales variaciones: [rubro y causa]

**Tipo de visual:** Gráfico de barras agrupadas (planeado vs. ejecutado) por rubro, más un indicador de proyección.
**Notas del presentador:** Relaciona el gasto con el avance real para que el board vea si el dinero rinde lo esperado. Si hay sobrecosto, explica la causa y la acción correctiva.

---

## Slide 9. Presupuesto: detalle por categoría y forecast
- Personal: planeado [$], ejecutado [$], variación [%]
- Tecnología y licencias: planeado [$], ejecutado [$], variación [%]
- Proveedores externos: planeado [$], ejecutado [$], variación [%]
- Contingencia: disponible [$] ([XX]% del total)
- Escenarios de cierre: optimista / base / pesimista

**Tipo de visual:** Tabla detallada con columna de variación resaltada en color.
**Notas del presentador:** Muestra cuánta reserva de contingencia queda y bajo qué escenario se usaría. Esto da confianza de que el presupuesto tiene margen.

---

## Slide 10. Mapa de riesgos
- Riesgo 1: [descripción] | Probabilidad: [A/M/B] | Impacto: [A/M/B] | Estado: [mitigado/abierto]
- Riesgo 2: [descripción] | Probabilidad: [A/M/B] | Impacto: [A/M/B] | Estado: [mitigado/abierto]
- Riesgo 3: [descripción] | Probabilidad: [A/M/B] | Impacto: [A/M/B] | Estado: [mitigado/abierto]
- Riesgos críticos totales: [N]; mitigados en el último mes: [N]

**Tipo de visual:** Matriz de riesgos 3x3 (probabilidad vs. impacto) con burbujas numeradas.
**Notas del presentador:** Prioriza los tres riesgos más altos y explica qué se hace para cada uno. Evita listar todos los riesgos menores; el board necesita foco.

---

## Slide 11. Riesgos críticos: plan de mitigación
- Riesgo principal: [descripción y causa raíz]
- Acción de mitigación: [qué se hace, quién lo hace]
- Fecha compromiso: [DD/MM/AAAA]
- Indicador de seguimiento: [métrica que confirma que el riesgo baja]
- Impacto si no se mitiga: [consecuencia en plazo, costo o alcance]

**Tipo de visual:** Ficha o tabla de 3 columnas (riesgo, acción, responsable y fecha).
**Notas del presentador:** Sé específico con responsables y fechas. Un riesgo sin dueño y sin fecha se percibe como no gestionado.

---

## Slide 12. Roadmap Q2-Q3: hitos principales
- Abril-mayo: [entregable o hito clave]
- Junio: [hito de cierre de fase / revisión]
- Julio-agosto: [integraciones, piloto ampliado]
- Septiembre: [lanzamiento o go-live, según plan]
- Dependencias externas: [proveedores, aprobaciones, otros proyectos]

**Tipo de visual:** Roadmap visual por trimestre (Gantt o timeline con hitos).
**Notas del presentador:** Señala las dependencias externas, porque son las que el board puede ayudar a destrabar. Indica qué hitos son fijos y cuáles tienen margen.

---

## Slide 13. Roadmap Q2-Q3: detalle por iniciativa
- Iniciativa A: [alcance, responsable, fecha objetivo, dependencias]
- Iniciativa B: [alcance, responsable, fecha objetivo, dependencias]
- Iniciativa C: [alcance, responsable, fecha objetivo, dependencias]
- Recursos requeridos: [personas, presupuesto adicional si aplica]
- Criterio de salida por iniciativa: [condición de cierre]

**Tipo de visual:** Tabla de iniciativas con semáforo de confianza en la fecha.
**Notas del presentador:** Indica el nivel de confianza en cada fecha. Un roadmap con confianza explícita genera más credibilidad que uno que promete todo como seguro.

---

## Slide 14. Decisiones y asks al board
- Decisión 1: [ej. Aprobar ampliación presupuestal de $XXX K para X]
- Decisión 2: [ej. Autorizar contratación de X perfiles / proveedor]
- Decisión 3: [ej. Priorizar integración con sistema Y frente al Z]
- Consecuencia de no aprobar: [impacto concreto en plazo o resultado]
- Plazo de decisión requerido: [fecha]

**Tipo de visual:** Tabla de decisiones con columnas (solicitud, justificación, impacto, fecha límite).
**Notas del presentador:** Haz cada ask de forma explícita y en formato de decisión sí/no. Presenta la consecuencia de no aprobar para que el board entienda la urgencia sin presión indebida.

---

## Slide 15. Cierre y próximos pasos
- Resumen: avance, riesgos principales y decisiones solicitadas
- Próximos 30 días: [3 acciones clave con responsable]
- Próxima actualización al board: [fecha]
- Contacto para seguimiento: [nombre, correo]

**Tipo de visual:** Imagen de cierre simple con los tres mensajes clave en texto grande.
**Notas del presentador:** Cierra repitiendo las tres decisiones solicitadas para que queden registradas. Termina abriendo espacio para preguntas.

---

Si me compartes los datos reales (porcentajes de avance, cifras de presupuesto, riesgos actuales y el roadmap), puedo completar los marcadores y ajustar el tono y la profundidad para el perfil de tu board.