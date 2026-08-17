# Claude Opus 5 Fast — presentation/slide_outline

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.34 | quality: 9.22
- latency_total: 31.359s | tokens_per_second: 212.6
- input_tokens: 217 | output_tokens: 6668
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

# Outline: "Plataforma Digital 2.0" — Reporte de Estado al Board

**Duración sugerida:** 30 min de presentación + 15 min de Q&A
**Tono:** Ejecutivo, orientado a decisión. Cada slide debe poder leerse en 20 segundos.

> ⚠️ **Nota:** Las cifras incluidas son *placeholders ilustrativos*. Reemplázalas con los datos reales del proyecto antes de presentar.

---

## SLIDE 1 — Portada: Plataforma Digital 2.0 | Reporte de Estado al Board

**Contenido:**
- Nombre del programa y versión del reporte (ej. "Q1 2025 — Corte al 31 de marzo")
- Sponsor ejecutivo y líder de programa
- Fecha de la sesión y periodo cubierto
- Clasificación de confidencialidad

**Visual sugerido:** Imagen — portada limpia con branding corporativo, screenshot desenfocado del producto de fondo y un badge de estado global (🟢/🟡/🔴).

**Notas del presentador:** Abrir con una frase de encuadre: "Hoy venimos a reportar avance, transparentar dos riesgos materiales y pedir tres decisiones concretas." Anclar expectativas de tiempo desde el inicio.

---

## SLIDE 2 — Resumen Ejecutivo: Lo que el Board Necesita Saber

**Contenido:**
- **Estado global: 🟡 Amarillo** — avance 62% vs. 68% planeado (-6 pts)
- Fase 1 (core transaccional) **liberada en producción**, con 34% de usuarios migrados
- Presupuesto ejecutado: $4.2M de $6.8M (62%) — alineado al avance físico
- 2 riesgos en zona roja: integración con core legacy y disponibilidad de talento técnico
- **3 asks al board:** aprobación de $850K adicionales, decisión sobre alcance del módulo X, y sponsor para la gobernanza de datos

**Visual sugerido:** Diagrama — tarjetas tipo *scorecard* (4-5 KPIs con semáforo y flecha de tendencia) en una sola fila.

**Notas del presentador:** Este es el slide más importante: si el board solo ve uno, debe ser este. Decir explícitamente los tres asks aquí para que la audiencia escuche el resto con ese lente.

---

## SLIDE 3 — Recordatorio: El Caso de Negocio y los Compromisos

**Contenido:**
- Objetivo del programa: consolidar 4 plataformas legacy en una arquitectura única cloud-native
- Beneficios comprometidos: $12M de NPV a 5 años, -35% en costo de operación de TI
- Compromisos originales: 18 meses, $6.8M CAPEX, go-live completo en octubre 2025
- Métricas de éxito definidas: adopción, NPS, time-to-market, costo por transacción
- Qué **no** cambió: el business case sigue vigente y validado

**Visual sugerido:** Diagrama — línea de tiempo horizontal con los 3 hitos comprometidos + caja lateral con los 4 beneficios cuantificados.

**Notas del presentador:** Reanclar al board en lo que se aprobó originalmente; muchos directores no recuerdan los números exactos. Enfatizar que el business case no se ha deteriorado, solo la ruta de ejecución.

---

## SLIDE 4 — Estado Actual: Dónde Estamos Hoy

**Contenido:**
- Fase 1 — Core transaccional: ✅ **Completada** (liberada en febrero)
- Fase 2 — Módulos de cliente y self-service: 🟡 **En curso, 58%** (2 semanas de retraso)
- Fase 3 — Analítica y automatización: ⚪ **No iniciada** (arranque planeado en mayo)
- Migración de usuarios: 34% completada (12,400 de 36,500 usuarios)
- Decomisionamiento de legacy: 1 de 4 plataformas apagada

**Visual sugerido:** Diagrama — barra de progreso por fase (tipo Gantt simplificado) con marcador de "hoy" y semáforo por fase.

**Notas del presentador:** Enfatizar que el logro más relevante del trimestre es tener el core en producción sin incidentes críticos. El retraso está concentrado en una sola fase y es acotado.

---

## SLIDE 5 — Avance por Workstream

**Contenido:**
- Producto & UX: 71% — 🟢 en tiempo
- Ingeniería & Arquitectura: 64% — 🟡 riesgo por dependencia de integración
- Datos & Migración: 48% — 🔴 principal cuello de botella
- Gestión del cambio & Capacitación: 55% — 🟡 depende del ritmo de migración
- Seguridad & Cumplimiento: 82% — 🟢 auditoría interna aprobada sin hallazgos críticos

**Visual sugerido:** Tabla — 5 filas × 5 columnas (workstream, % avance, % plan, desviación, semáforo) con celdas coloreadas.

**Notas del presentador:** Dirigir la atención a Datos & Migración: es la causa raíz del 80% de la desviación total. Los demás workstreams no requieren decisión del board.

---

## SLIDE 6 — Métricas de Progreso: Entrega

**Contenido:**
- Velocidad del equipo: 42 story points/sprint promedio (vs. 50 planeado, -16%)
- Funcionalidades liberadas: 87 de 140 comprometidas (62%)
- Calidad: 0 defectos críticos en producción; 14 defectos mayores abiertos (SLA en verde)
- Disponibilidad de la plataforma: 99.94% (SLA: 99.9%)
- Deuda técnica: 8% del backlog (umbral de alerta: 15%)

**Visual sugerido:** Gráfico — combinado: líneas de *burn-up* (plan vs. real acumulado) con eje secundario de defectos abiertos por mes.

**Notas del presentador:** El mensaje es "vamos más lento, pero no estamos sacrificando calidad", lo cual es deliberado y correcto. Si preguntan por la velocidad, la causa es rotación de 3 ingenieros senior, no problemas de diseño.

---

## SLIDE 7 — Métricas de Adopción y Valor Temprano

**Contenido:**
- Usuarios activos mensuales en la nueva plataforma: 12,400 (+180% vs. trimestre anterior)
- NPS de usuarios migrados: 42 (baseline legacy: 18)
- Tiempo promedio de procesamiento: -41% vs. plataforma legacy
- Tickets de soporte por 1,000 usuarios: -28%
- Beneficio capturado a la fecha: $1.1M anualizado (9% del objetivo total)

**Visual sugerido:** Gráfico — barras comparativas "antes vs. después" en 4 métricas, más un termómetro de beneficio capturado vs. comprometido.

**Notas del presentador:** Este slide es la prueba de que la inversión está funcionando donde ya se implementó. Usarlo para sostener la confianza del board antes de entrar a riesgos y presupuesto.

---

## SLIDE 8 — Presupuesto: Ejecutado vs. Planeado

**Contenido:**
- Presupuesto aprobado: $6.8M | Ejecutado: $4.2M (62%) | Comprometido no ejecutado: $1.1M
- Avance físico 62% vs. avance financiero 62% → **CPI = 1.00** (eficiencia en costo en línea)
- **SPI = 0.91** (retraso en cronograma, no sobrecosto)
- Desglose: Personal 54%, Licencias & Cloud 23%, Consultoría externa 18%, Contingencia 5%
- Contingencia consumida: 62% del total ($340K de $550K)

**Visual sugerido:** Gráfico — barras apiladas de ejecutado vs. planeado por categoría + tabla resumen de CPI/SPI al pie.

**Notas del presentador:** El punto clave: no hay sobrecosto en el trabajo realizado; el problema es que el retraso extenderá el periodo de gasto corriente. La contingencia consumida es la señal de alerta real.

---

## SLIDE 9 — Proyección al Cierre y Análisis de Desviaciones

**Contenido:**
- Proyección a cierre (EAC): **$7.65M vs. $6.8M aprobado** → desviación de **+$850K (12.5%)**
- Causas de la desviación: extensión de 8 semanas del equipo core ($480K), consultoría adicional en migración de datos ($270K), licencias extendidas de legacy en paralelo ($100K)
- Escenario optimizado (reducción de alcance en módulo X): $7.1M, ahorro de $550K
- Impacto en el business case: NPV se reduce de $12M a $11.3M — **el proyecto sigue siendo positivo**
- Fecha de go-live completo proyectada: diciembre 2025 (vs. octubre original)

**Visual sugerido:** Gráfico — waterfall (cascada) desde presupuesto aprobado hasta EAC, mostrando cada driver de desviación.

**Notas del presentador:** Este es el slide que sustenta el ask #1; ir despacio y dejar espacio para preguntas. Tener listos los supuestos detrás de cada driver por si el CFO los cuestiona.

---

## SLIDE 10 — Mapa de Riesgos

**Contenido:**
- **R1 — 🔴 Integración con core bancario/ERP legacy:** probabilidad alta, impacto alto (retraso adicional de 4-6 semanas)
- **R2 — 🔴 Rotación y escasez de talento técnico:** 3 salidas en el trimestre, 2 posiciones críticas abiertas
- **R3 — 🟡 Calidad de datos en migración:** 12% de registros con inconsistencias
- **R4 — 🟡 Resistencia al cambio en operaciones:** adopción por debajo de meta en 2 unidades de negocio
- **R5 — 🟢 Cumplimiento regulatorio:** mitigado, auditoría aprobada

**Visual sugerido:** Diagrama — matriz de riesgo 3×3 (probabilidad × impacto) con burbujas numeradas y codificadas por color.

**Notas del presentador:** No suavizar los riesgos rojos: la credibilidad ante el board se construye con transparencia. Aclarar que R1 y R2 son la razón del retraso, y que ambos tienen planes de mitigación en el siguiente slide.

---

## SLIDE 11 — Plan de Mitigación y Dependencias Externas

**Contenido:**
- **R1:** contratación de partner especializado en integración + arquitectura de *strangler pattern* para desacoplar (decisión requerida: presupuesto)
- **R2:** retención con esquema de bono de permanencia + 2 contrataciones vía staffing (en curso, cierre en 4 semanas)
- **R3:** *data quality sprint* dedicado en abril, con ownership del área de negocio
- **Dependencias fuera de control del programa:** disponibilidad del equipo de core legacy (área de TI Operaciones) y aprobación de proveedor por Compras
- Fecha de próxima revisión de riesgos: reunión mensual del Comité Ejecutivo

**Visual sugerido:** Tabla — riesgo | acción de mitigación | responsable | fecha compromiso | estado.

**Notas del presentador:** Señalar que dos mitigaciones dependen de decisiones que solo el board o el comité ejecutivo pueden desbloquear. Nombrar responsables con nombre y apellido genera accountability visible.

---

## SLIDE 12 — Roadmap Q2 2025

**Contenido:**
- **Abril:** cierre de brechas de integración + data quality sprint + migración de 8,000 usuarios adicionales
- **Mayo:** liberación de módulos de self-service (Fase 2 completa) + arranque de Fase 3
- **Junio:** apagado de 2 plataformas legacy adicionales + 60% de usuarios migrados
- Hito de decisión (gate) al cierre de mayo: validar viabilidad del go-live de diciembre
- Métrica objetivo del trimestre: 22,000 usuarios activos y beneficio anualizado de $3.5M

**Visual sugerido:** Diagrama — timeline de 3 meses con carriles (swimlanes) por workstream e íconos de hitos y *gates*.

**Notas del presentador:** Destacar el *gate* de mayo como mecanismo de control: si no se cumple, se activa el escenario de alcance reducido. Esto le da al board una sensación de opcionalidad y control.

---

## SLIDE 13 — Roadmap Q3 2025 y Ruta a Cierre

**Contenido:**
- **Julio-agosto:** Fase 3 (analítica y automatización) + migración del 90% de usuarios
- **Septiembre:** estabilización, hardening y pruebas de carga a escala completa
- **Q4 (fuera de alcance del trimestre):** apagado final de legacy y transición a operación (diciembre)
- Preparación de la operación: modelo de soporte, SLAs y transferencia al equipo run
- Beneficio proyectado al cierre de Q3: $7.8M anualizado (65% del objetivo)

**Visual sugerido:** Diagrama — roadmap horizontal Q2→Q4 con la curva de captura de beneficios superpuesta.

**Notas del presentador:** Enfatizar que el programa termina cuando se apaga el legacy, no cuando se libera el software; ahí está el ahorro comprometido. Aprovechar para introducir el tema de transición a operación, que suele preocupar al board.

---

## SLIDE 14 — Asks al Board: Decisiones Requeridas Hoy

**Contenido:**
- **Ask 1 — Aprobación presupuestal:** $850K adicionales (12.5%) para cubrir extensión y partner de integración. *Alternativa: reducir alcance del módulo X, con impacto de -$700K en NPV.*
- **Ask 2 — Decisión de alcance:** ¿mantener el módulo X en la Fase 3 o diferirlo a 2026?
- **Ask 3 — Sponsor ejecutivo para gobernanza de datos:** se requiere un miembro del board o C-level que destrabe el ownership de datos en las unidades de negocio
- Consecuencia de no decidir hoy: cada semana de demora suma ~$45K y desplaza el go-live
- Fecha límite para las tres decisiones: **30 de abril**

**Visual sugerido:** Tabla — 3 filas: Ask | Monto/Impacto | Alternativa | Decisor | Fecha límite. Encabezados en color de acento.

**Notas del presentador:** Pausar después de este slide y pedir explícitamente la decisión, no solo comentarios. Si el board quiere posponer, dejar registrado el costo de la demora en la minuta.

---

## SLIDE 15 — Cierre: Compromisos y Próximos Pasos

**Contenido:**
- Compromiso del equipo: cumplir el *gate* de mayo o activar el plan de alcance reducido
- Próximos hitos de reporte: comité ejecutivo mensual + siguiente reporte al board el 15 de julio
- Acciones acordadas en esta sesión (a completar en vivo con los acuerdos)
- Contacto y disponibilidad del líder de programa para sesiones de profundización 1:1
- Apéndice disponible: detalle financiero, arquitectura técnica, registro completo de riesgos

**Visual sugerido:** Diagrama — 3 tarjetas de "próximos pasos" con fecha y responsable, más un pie con la agenda de reportes.

**Notas del presentador:** Cerrar repitiendo los tres asks y confirmando verbalmente qué se decidió. Ofrecer sesiones individuales para directores que quieran profundizar sin extender la reunión.

---

## Recomendaciones adicionales

| Aspecto | Recomendación |
|---|---|
| **Regla de tiempo** | Slides 2, 9 y 14 son los críticos: asigna ~4 min a cada uno y ≤1.5 min al resto. |
| **Slides de respaldo** | Prepara 6-8 apéndices: detalle presupuestal por línea, registro completo de riesgos, arquitectura, plan de migración por unidad de negocio, CVs del partner propuesto. |
| **Pre-work** | Envía el mazo 48-72h antes y agenda pre-briefings con el CFO y el sponsor para que los asks no sean sorpresa en la sesión. |
| **Consistencia visual** | Usa el mismo código de semáforo en todo el mazo y no mezcles escalas (% avance vs. % presupuesto) en un mismo gráfico. |
| **Densidad** | Máximo 5 bullets y ~30 palabras por slide; todo lo demás va al apéndice o a las notas. |

¿Quieres que desarrolle el contenido completo de algún slide en particular, o que ajuste las cifras placeholder con los datos reales de tu proyecto?