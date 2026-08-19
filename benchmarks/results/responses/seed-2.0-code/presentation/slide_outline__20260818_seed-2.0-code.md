# Seed 2.0 Code — presentation/slide_outline

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.24 | quality: 9.6
- latency_total: 38.681s | tokens_per_second: 52.9
- input_tokens: 169 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un esquema detallado y bien estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa


El usuario pide un outline de 15 slides para el board sobre Plataforma Digital 2.0, con requisitos específicos por slide: número, título, bullets, visual, notas de presentador. También debe cubrir estado actual, métricas, riesgos, presupuesto, roadmap Q2-Q3 y asks al board.

Primero, calculo la distribución de 15 slides para cubrir todo lo pedido:

1. Slide 1: Portada (obligatorio, número 1)
2. Slide 2: Agenda (para orientar al board, número 2)
3. Slide 3: Objetivos Estratégicos de la Plataforma (conectar con el board's priorities, no se olvida que es board, les importa el impacto estratégico, no solo técnico)
4. Slide 4: Estado Actual General (lo primero que pide: estado actual)
5. Slide 5: Métricas de Progreso Técnico (métricas, parte técnica)
6. Slide 6: Métricas de Impacto Usuario (métricas, impacto, lo que le importa al board por ROI)
7. Slide 7: Presupuesto Ejecutado vs Planeado (lo pedido)
8. Slide 8: Desviaciones Presupuestarias Detalladas (profundizar, ya que es board, quieren saber por qué desviaciones)
9. Slide 9: Riesgos Identificados (lo pedido)
10. Slide 10: Planes de Mitigación de Riesgos (no solo decir riesgos, sino cómo lo solucionamos, board le gusta eso)
11. Slide 11: Roadmap Q2 (lo pedido, separar Q2 y Q3 para detalle, no juntar en una slide)
12. Slide 12: Roadmap Q3 + Hitos Clave Futuros
13. Slide 13: Asks al Board (lo pedido, específico, no ambigüo)
14. Slide 14: Resumen Ejecutivo (board suele leer resúmenes primero, pero ponerlo antes del cierre para recap)
15. Slide 15: Preguntas y Contacto (cierre)

Ahora, por cada slide, cumplir con todos los requisitos:

- Número y Título: Claro, orientado al board (no títulos técnicos oscuros)
- Bullets: 3-5, específicos, medibles, ligados a prioridades del board
- Visual: Apropiado para el contenido (ej: para presupuesto, gráfico de barras apiladas; para roadmap, diagrama de Gantt simplificado)
- Notas del presentador: 1-2 oraciones, dirigidas al board (ej: "Destacar que el alineamiento con los objetivos de ingresos 2024 es del 98% para mantener el foco estratégico")

Ahora, ajustar cada sección para que cubra lo que pide el usuario:

Estado actual: Slide 4, con bullets de cumplimiento de hitos clave, equipos involucrados, estado de integraciones. Visual: Diagrama de semáforo (rojo/amarillo/verde) para hitos.

Métricas de progreso: Slide 5 (técnico: % de módulos completados, tiempo de entrega por sprint, defectos cerrados) y Slide 6 (usuario: adopción beta, satisfacción NPS, reducción de soporte por usuario). Visuales: Slide 5: Gráfico de líneas de progreso por sprint; Slide 6: Tabla con métricas vs objetivo, más gráfico de barras para NPS.

Riesgos: Slide 9 (riesgos con probabilidad e impacto), Slide 10 (mitigación). Visual Slide 9: Matriz de riesgo (probabilidad vs impacto).

Presupuesto: Slide 7 (ejecutado vs planeado total), Slide 8 (desviaciones por rubro: personal, proveedores, herramientas). Visual Slide7: Gráfico de barras apiladas (ejecutado vs planeado); Slide8: Tabla de desviaciones con causas.

Roadmap Q2-Q3: Slide11 (Q2: hitos específicos, fechas, responsables) y Slide12 (Q3: hitos más estratégicos, como lanzamiento completo, integraciones con ERP). Visual: Diagrama de Gantt simplificado por trimestre.

Asks al Board: Slide13, debe ser específico (no "más dinero" sino "aprobación de presupuesto adicional de 15k USD para integraciones con proveedor X, aprobación de cambio de fecha de lanzamiento 2 semanas, asignación de 1 director de producto dedicado 4hrs/semana"). Visual: Tabla de Asks con detalle de necesidad, costo, impacto.

Ahora, verificar que cada slide tenga 3-5 bullets, visual adecuado, notas de presentador 1-2 oraciones, y que sean 15 slides exactos.

También, para el board, hay que ligar todo a los objetivos estratégicos de la empresa (ej: "Plataforma 2.0 alinea con el objetivo 2024 de incrementar ingresos por canales digitales en 30%"), por lo que el Slide 3 (Objetivos Estratégicos) es crucial para contextualizar.

Otra cosa: el board no quiere detalles técnicos irrelevantes, por lo que las métricas técnicas deben ser útiles para el negocio (ej: "% de módulos de pago completados" no "% de código escrito").

Notas del presentador: deben ser indicaciones de lo que el presentador (probablemente el PM o Director de Digital) debe destacar, no repetir los bullets. Ej: en la slide de presupuesto, "Destacar que la desviación de 8% se debe a un cambio de proveedor de seguridad que reduce riesgos de fuga de datos en un 70%, por lo que es una desviación estratégica".

Ahora, armar cada slide paso a paso:

Slide 1: Portada
- Título: Estado del Proyecto Plataforma Digital 2.0 | Trimestre 1 2024
- Bullets: 1) Proyecto Estratégico para Ingresos Digitales 2024, 2) Presentación para Board de Directores, 3) Fecha: 15 de Abril 2024
- Visual: Logotipo de la empresa + imagen de mockup de la plataforma (sin detalles técnicos, solo diseño limpio)
- Notas: Iniciar con un saludo breve y destacar que esta presentación se alinea con la agenda de prioridades del board para 2024.

Slide 2: Agenda
- Título: Agenda de la Presentación
- Bullets: 1) Objetivos Estratégicos de la Plataforma, 2) Estado Actual y Métricas de Progreso, 3) Presupuesto Ejecutado vs Planeado, 4) Riesgos y Mitigaciones, 5) Roadmap Q2-Q3 y Asks al Board
- Visual: Diagrama de flujo circular con los puntos de la agenda (ligado a logo)
- Notas: Recordar al board que cualquier pregunta puede hacerse en el momento, pero se reservará un bloque al final para consultas profundas.

Slide 3: Objetivos Estratégicos (conectar con board)
- Título: Objetivos Estratégicos de Plataforma Digital 2.0
- Bullets: 1) Incrementar ingresos por canales digitales en 30% (2024 vs 2023), 2) Reducir costos de soporte al cliente en 20%, 3) Mejorar la experiencia de usuario (NPS > 70), 4) Integrar todos los canales de venta en una sola plataforma
- Visual: Tabla de alineamiento: Objetivo Plataforma ↔ Objetivo Empresarial 2024 (ej: Incrementar ingresos digitales ↔ Meta de ingresos 2024 de $50M)
- Notas: Destacar que el 98% de los hitos de la plataforma están alineados con los objetivos del Plan Estratégico 2024, para validar la relevancia del proyecto.

Slide 4: Estado Actual General (lo pedido por usuario)
- Título: Estado Actual del Proyecto (T1 2024)
- Bullets: 1) 65% de hitos de T1 cumplidos (vs meta de 60%), 2) Equipo de 12 personas (8 técnicos, 4 de negocio) al 100% dedicado, 3) Módulos de registro y catálogo completados y en beta cerrada, 4) Integración con pasarela de pago Stripe en etapa de pruebas
- Visual: Diagrama de semáforo (verde: cumplido, amarillo: en plazo pero con ajustes, rojo: atrasado) para