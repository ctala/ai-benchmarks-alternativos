# Muse Spark 1.3 — presentation/slide_outline

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.33 | quality: 9.8
- latency_total: 33.061s | tokens_per_second: 123.1
- input_tokens: 130 | output_tokens: 4071
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y ofrece una estructura útil para una presentación ejecutiva, con insights valiosos sobre el estado del proyecto y métricas técnicas.

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

# Outline Presentación: Plataforma Digital 2.0 - Estado del Proyecto
**Audiencia:** Board de Directores | **Duración sugerida:** 30 min + 15 min Q&A

---

### Slide 1: Portada - Plataforma Digital 2.0
* **Contenido:**
  * Título: Estado del Proyecto Plataforma Digital 2.0 - Corte a Q1 2026
  * Presentado por: [Nombre, PMO / CIO] - Fecha: Noviembre 2026
  * Clasificación: Confidencial - Uso interno Board
  * Tagline: De la construcción a la adopción y el ROI
* **Visual sugerido:** Imagen hero corporativa de la plataforma + logos
* **Notas del presentador:** Dar la bienvenida y enmarcar la sesión como informativa y decisoria, no solo de seguimiento.

### Slide 2: Objetivo de la Sesión y Agenda
* **Contenido:**
  * Objetivo: Informar avance, transparentar riesgos financieros y obtener 3 aprobaciones clave
  * Agenda en 5 bloques: 1. Resumen 2. Progreso y Métricas 3. Finanzas 4. Riesgos y Roadmap 5. Asks
  * Reglas: 30 min presentación, 15 min decisión y Q&A
  * Contexto: Proyecto estratégico con inversión aprobada de $4.2M
* **Visual sugerido:** Diagrama horizontal de agenda tipo timeline con 5 iconos
* **Notas del presentador:** Alinear expectativas desde el inicio: al final necesitaremos decisiones concretas del Board.

### Slide 3: Resumen Ejecutivo en Una Página
* **Contenido:**
  * Estado general: AMARILLO - Avance 68% vs 75% planeado, retraso de 3 semanas recuperable
  * Finanzas: 92% de presupuesto ejecutado vs plan, variación de +4% por licencias cloud
  * Negocio: 42k usuarios migrados (60% meta), NPS +48, uptime 99.9%
  * Mensaje clave: Necesitamos 2 decisiones hoy para no comprometer Go-Live de Q3
* **Visual sugerido:** Tabla semáforo RAG + 4 tarjetas KPI grandes
* **Notas del presentador:** Si el Board solo recuerda una slide, es esta; enfóquese en que el proyecto es viable pero requiere acción.

### Slide 4: Estado Actual del Programa
* **Contenido:**
  * Avance por stream: Core 82% (Verde), App Móvil 71% (Verde), Migración Datos 58% (Amarillo), Integraciones 61% (Amarillo)
  * Hitos: 12 de 15 completados en Q1, 2 retrasados por proveedor API pagos
  * Salud general: Alcance Amarillo, Tiempo Amarillo, Calidad Verde
  * Causa raíz del desfase: Retraso proveedor + rotación de 2 devs senior
* **Visual sugerido:** Gráfico de barras de progreso por workstream + semáforos RAG
* **Notas del presentador:** Ser transparente sobre el retraso de 3 semanas, pero mostrar que está contenido y con plan de recuperación.

### Slide 5: Métricas de Progreso Técnico
* **Contenido:**
  * Velocity Scrum: 85 story points/sprint, +12% vs Q4, tendencia estable
  * Calidad: Cobertura de tests 84%, bugs críticos 3 abiertos (vs 12 en Q4), MTTR 4h
  * DevOps: 120 deploys en Q1, lead time 2.1 días, 0 rollbacks mayores
  * Deuda técnica: 18% del backlog, dentro del umbral permitido del 20%
* **Visual sugerido:** Gráfico burndown + gráfico de líneas de velocity y calidad
* **Notas del presentador:** Demostrar madurez de ingeniería para dar confianza al Board en la capacidad de entrega.

### Slide 6: Métricas de Negocio y Adopción Temprana
* **Contenido:**
  * Adopción: 42k usuarios activos mensuales, 60% de meta Q1, retención D30 de 68%
  * Experiencia: NPS +48 (vs +32 plataforma 1.0), CSAT 4.6/5.0, tiempo de onboarding -35%
  * Impacto operativo: Tiempo de proceso clave de 12 min a 4 min, -40% tickets soporte
  * Gap: Adopción en segmento Enterprise solo 35% por falta de feature SSO
* **Visual sugerido:** Dashboard con 4 mini-gráficos de línea / gauge para NPS y adopción
* **Notas del presentador:** Conectar tecnología con valor de negocio: ya vemos eficiencia y satisfacción, pero Enterprise necesita el SSO.

### Slide 7: Logros Clave y Wins del Trimestre
* **Contenido:**
  * Lanzamiento exitoso de 3 módulos: Onboarding Digital, Pagos y Dashboard Cliente
  * Migración del 40% de la base de datos legacy sin downtime
  * Integración certificada con pasarela de pagos y firma electrónica
  * Reconocimiento: Auditoría de seguridad externa aprobada sin hallazgos mayores
* **Visual sugerido:** Timeline visual con fotos/screenshots del producto + iconos de check
* **Notas del presentador:** Celebrar los wins para balancear los riesgos y mostrar momentum tangible al Board.

### Slide 8: Presupuesto: Ejecutado vs. Planeado
* **Contenido:**
  * Presupuesto total aprobado: $4.2M, Ejecutado YTD: $2.31M (55%) vs Planeado $2.22M (+4% / +$90k)
  * Desglose: Desarrollo 58%, Cloud/Licencias 22% (+12% sobrecosto), Talento externo 15%, Otros 5%
  * Causa variación: Mayor consumo cloud por pruebas de carga y alza en licencias
  * Acciones de control: Renegociación cloud y freeze de consultorías no críticas
* **Visual sugerido:** Gráfico de barras agrupadas Planeado vs. Real por categoría + tabla de varianza
* **Notas del presentador:** Explicar que la desviación es pequeña y explicada, pero marca una tendencia a vigilar.

### Slide 9: Proyección Financiera y Burn Rate
* **Contenido:**
  * Forecast EOY: $4.45M (+$250k / +6% vs presupuesto) si no se toman acciones
  * Burn rate mensual actual: $285k, runway hasta Agosto con presupuesto actual
  * Escenarios: A) Recorte alcance ahorra $180k, B) Optimización cloud ahorra $120k
  * ROI esperado se mantiene: Payback en 18 meses post Go-Live por ahorro operativo
* **Visual sugerido:** Gráfico de líneas de forecast + gráfico waterfall de drivers de costo
* **Notas del presentador:** Anticipar la pregunta del Board sobre sobrecosto mostrando que tenemos escenarios modelados para volver a presupuesto.

### Slide 10: Top 5 Riesgos y Plan de Mitigación
* **Contenido:**
  * R1 Alto: Dependencia proveedor API pagos (Prob. Alta/Imp. Alto) - Mitigación: proveedor backup
  * R2 Alto: Brecha ciberseguridad en migración datos - Mitigación: pentest Q2 + cifrado
  * R3 Medio: Rotación talento clave (15% attrition) - Mitigación: plan retención y bonos
  * R4 Medio: Cambio regulatorio datos personales - Mitigación: mesa con Legal/Compliance
  * R5 Medio: Scope creep de áreas comerciales - Mitigación: comité de cambios estricto
* **Visual sugerido:** Matriz de calor Probabilidad vs. Impacto 2x2 + tabla de mitigación
* **Notas del presentador:** Enfocarse solo en los 2 riesgos altos para no alarmar, mostrando que todos tienen dueño y plan.

### Slide 11: Issues Críticos y Dependencias
* **Contenido:**
  * Issue #1 Bloqueante: Retraso 4 semanas entrega conector ERP por proveedor, impacta facturación
  * Issue #2: Falta aprobación de Legal para tratamiento de datos biométricos
  * Dependencia Infra: Aprobación para escalar ambientes productivos en AWS
  * Dependencia Negocio: Definición de pricing del nuevo módulo por Marketing antes del 15 Dic
* **Visual sugerido:** Tabla RAG de issues con dueño, fecha límite y diagrama de dependencias
* **Notas del presentador:** Dejar claro qué está fuera de nuestro control y requiere escalamiento y apoyo del Board.

### Slide 12: Roadmap Q2 - Q3: Camino al Go-Live
* **Contenido:**
  * Q2 Foco Estabilizar: Completar migración (100%), lanzar SSO Enterprise, Beta cerrada 10k usuarios
  * Q3 Foco Escalar: Go-Live general Agosto, hipercare, sunset Plataforma 1.0 en Septiembre
  * Hitos inamovibles: Freeze de alcance 30 Mayo, Code Freeze 15 Julio, Corte regulatorio
  * Supuestos críticos: Aprobación de presupuesto y contratación esta semana
* **Visual sugerido:** Roadmap Gantt / timeline por trimestres con diamantes de hitos
* **Notas del presentador:** Mostrar un camino creíble y con fechas concretas, vinculando el cumplimiento al apoyo que pediremos.

### Slide 13: Equipo, Capacidad y Organización
* **Contenido:**
  * Equipo actual: 48 personas (32 internas, 16 externas), 92% staffed, eNPS interno 72
  * Gap crítico: Faltan 2 Arquitectos Cloud Senior y 1 Lead Ciberseguridad
  * Modelo: 6 squads ágiles + PMO, dependencia de 30% en consultora frena transferencia
  * Plan: Internalizar 5 roles clave en Q2 para reducir costo y riesgo de conocimiento
* **Visual sugerido:** Organigrama simplificado + gráfico dona internos vs. externos y capacidad
* **Notas del presentador:** Justificar la necesidad de contratar talento interno como inversión para reducir riesgo y costo a largo plazo.

### Slide 14: Asks al Board - Decisiones Requeridas Hoy
* **Contenido:**
  * ASK 1: Aprobar extensión presupuestal de $250k para cloud y seguridad ($120k recuperables)
  * ASK 2: Aprobar contratación de 3 roles críticos senior + plan de retención ($95k)
  * ASK 3: Aprobar congelar alcance y priorizar SSO Enterprise sobre 2 features nice-to-have
  * Costo de no decidir: Retraso de 6-8 semanas en Go-Live y sobrecosto adicional de $400k
* **Visual sugerido:** Tabla Decisión / Impacto / Riesgo de no aprobar con montos claros
* **Notas del presentador:** Ser directo y pedir aprobación explícita; sin estas 3 decisiones no podemos garantizar la fecha de Agosto.

### Slide 15: Conclusiones, Próximos Pasos y Q&A
* **Contenido:**
  * 3 mensajes finales: Proyecto avanza y genera valor, desviación controlada, necesitamos su aval hoy
  * Próximos 30-60-90 días: Cierre migración, Beta Enterprise, Go-Live piloto
  * Gobernanza: Próxima revisión Board en 8 semanas + reporte mensual ejecutivo
  * Apertura a preguntas y sesión de demo de 5 min si el tiempo lo permite
* **Visual sugerido:** Imagen de cierre inspiradora + timeline 30-60-90 días
* **Notas del presentador:** Cerrar con confianza y optimismo, agradecer el apoyo y pasar a asegurar los acuerdos y responsables.