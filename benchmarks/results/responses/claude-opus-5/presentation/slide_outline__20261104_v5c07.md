# Claude Opus 5 — presentation/slide_outline

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.75 | quality: 9.8
- latency_total: 83.673s | tokens_per_second: 75.5
- input_tokens: 217 | output_tokens: 6319
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, cubriendo todos los aspectos solicitados con detalles útiles y estructura organizada, lo que la hace altamente útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

# Plataforma Digital 2.0 — Estado del Proyecto
## Outline de Presentación para el Board de Directores
**Duración estimada:** 35–40 min (25 min presentación + 10–15 min Q&A)

---

## SLIDE 1 — Portada: Plataforma Digital 2.0 — Revisión Trimestral al Board

**Contenido:**
- Título del programa y versión del reporte (ej. Q1 2025 — Cierre)
- Fecha de la sesión y periodo cubierto
- Patrocinador ejecutivo, Program Director y PMO
- Nivel de confidencialidad (Uso interno — Board)
- Semáforo global del proyecto en una sola palabra: **ÁMBAR**

**Visual sugerido:** Imagen — portada limpia con el logo corporativo, la marca del programa y un chip de color (ámbar) que ancle visualmente el estado general.

**Notas del presentador:** Abrir anclando la conclusión: "El programa avanza, llegaremos a producción, pero necesitamos tres decisiones de este board hoy." Mencionar que la agenda está diseñada para dejar 15 minutos de discusión.

---

## SLIDE 2 — Resumen Ejecutivo: Lo que Necesitan Saber en 60 Segundos

**Contenido:**
- **Progreso:** 62% de avance global, 4 de 7 módulos en producción
- **Cronograma:** Go-live completo se mueve de junio a **agosto 2025** (+6 semanas)
- **Presupuesto:** $8.4M ejecutados de $13.2M aprobados (64%) — proyección de cierre en $14.1M (+6.8%)
- **Valor ya capturado:** $1.9M en ahorro operativo anualizado de los módulos en vivo
- **Asks al board:** aprobación de $900K de contingencia, decisión sobre alcance del módulo de analítica, y nombramiento de un sponsor de negocio para Operaciones

**Visual sugerido:** Tabla/dashboard — cuadrícula de 5 tarjetas KPI con valor, meta y flecha de tendencia (verde/ámbar/rojo).

**Notas del presentador:** Esta es la única slide que el board recordará: decirla completa y despacio. Aclarar que la desviación de cronograma es consecuencia de una decisión deliberada de calidad, no de una falla de ejecución.

---

## SLIDE 3 — Dónde Estamos vs. Dónde Dijimos que Estaríamos

**Contenido:**
- Línea base aprobada (nov 2024) vs. ejecución real a la fecha
- Hitos cumplidos en tiempo: 11 de 14
- Hitos reprogramados: 3 (migración de datos, integración ERP, UAT de pagos)
- Causa raíz dominante: calidad de datos legados (58% de la desviación)
- Confirmación de que el **alcance aprobado no se ha reducido**

**Visual sugerido:** Diagrama — Gantt simplificado de dos carriles (plan vs. real) con marcadores de hito y zona sombreada de desviación.

**Notas del presentador:** Enfatizar que el alcance se mantiene intacto: no estamos entregando menos, estamos entregando más tarde. Si preguntan por la causa raíz, la respuesta corta es calidad de datos del sistema legado.

---

## SLIDE 4 — Estado por Módulo: Mapa de Calor del Programa

**Contenido:**
- 7 módulos: Identidad/SSO, Portal Cliente, Pagos, Catálogo, CRM, Analítica, App Móvil
- **Verde (3):** Identidad/SSO, Portal Cliente, Catálogo — en producción y estables
- **Ámbar (3):** Pagos (certificación PCI en curso), CRM (integración ERP), App Móvil (dependencia de Pagos)
- **Rojo (1):** Analítica — alcance no congelado, sin owner de negocio
- Dependencia crítica: App Móvil no puede liberarse antes de Pagos

**Visual sugerido:** Diagrama — mapa de calor (heatmap) de 7 filas × 4 columnas (Alcance, Cronograma, Presupuesto, Calidad) con celdas semaforizadas.

**Notas del presentador:** Dirigir la atención al único rojo y adelantar que será uno de los asks del slide 14. Evitar entrar en detalle técnico aquí; hay backup en el anexo.

---

## SLIDE 5 — Métricas de Progreso Técnico y de Entrega

**Contenido:**
- Historias de usuario completadas: 1,142 de 1,840 (62%)
- Velocidad del equipo: 148 puntos/sprint promedio (meta: 160) — estable últimos 4 sprints
- Cobertura de pruebas automatizadas: 74% (meta: 80%)
- Defectos abiertos: 212 totales, **0 críticos**, 18 severidad alta
- Despliegues a producción: 46 en el trimestre, tasa de rollback 4.3%

**Visual sugerido:** Gráfico — combinación de líneas: burn-up de alcance (acumulado completado vs. total) y barras de velocidad por sprint.

**Notas del presentador:** El mensaje clave es predictibilidad: la velocidad lleva cuatro sprints estable, lo que hace creíble la nueva fecha de agosto. Cero defectos críticos en producción es el indicador de calidad a resaltar.

---

## SLIDE 6 — Métricas de Adopción y Negocio: El Valor Ya Está Llegando

**Contenido:**
- Usuarios activos en la nueva plataforma: 38,400 (meta trimestral: 30,000) — **128% de cumplimiento**
- Migración de usuarios desde legado: 41% del total
- Reducción de tiempo de onboarding de cliente: de 12 días a 4.5 días (-62%)
- NPS de la nueva experiencia: 46 (vs. 21 en plataforma legada)
- Tickets de soporte por 1,000 usuarios: -34%

**Visual sugerido:** Gráfico — barras comparativas "antes vs. después" para 4 métricas de negocio, más un indicador grande de usuarios activos.

**Notas del presentador:** Esta es la slide que justifica continuar la inversión: el valor no es una promesa futura, ya es medible. Conectar los $1.9M de ahorro anualizado con estas métricas operativas.

---

## SLIDE 7 — Presupuesto: Ejecutado vs. Planeado

**Contenido:**
- Presupuesto aprobado total: **$13.2M** | Ejecutado a la fecha: **$8.4M (64%)**
- Planeado a la fecha: $7.9M → **sobre-ejecución de $500K (+6.3%)**
- Desglose: Personal interno $3.1M | Vendors/integrador $3.4M | Licencias/cloud $1.3M | Contingencia usada $600K de $800K
- Comprometido no facturado: $1.2M
- Proyección a cierre (EAC): **$14.1M** → desviación de +$900K (+6.8%)

**Visual sugerido:** Gráfico — curva S de costo acumulado (planeado vs. real vs. proyectado) acompañada de una tabla de desglose por categoría.

**Notas del presentador:** Ser explícito: la contingencia está casi agotada (75% usada) y de ahí viene el ask de $900K. Aclarar que el sobrecosto es principalmente horas adicionales de remediación de datos, no expansión de alcance.

---

## SLIDE 8 — Análisis de Desviación: ¿En Qué se Fue el Dinero Extra?

**Contenido:**
- Remediación de calidad de datos legados: **+$520K** (no previsto en línea base)
- Extensión de contrato con integrador por 6 semanas: +$310K
- Licenciamiento de herramienta de observabilidad: +$95K (decisión de arquitectura)
- Ahorros compensatorios: -$125K por renegociación de cloud y retiro anticipado de 2 servidores legados
- Índice de desempeño de costo (CPI): 0.94 | Índice de cronograma (SPI): 0.91

**Visual sugerido:** Gráfico — waterfall (cascada) desde el presupuesto planeado hasta la proyección final, mostrando cada contribución positiva y negativa.

**Notas del presentador:** Un waterfall evita la sensación de "se nos fue el dinero" porque cada dólar tiene nombre y apellido. Mencionar que el ahorro de cloud fue iniciativa del equipo, no un requerimiento.

---

## SLIDE 9 — Riesgos Principales: Top 5 del Programa

**Contenido:**
- **R1 — Calidad de datos legados (Alto/Alto):** bloquea migración de CRM. Mitigación: squad dedicado de 4 personas + herramienta de profiling
- **R2 — Certificación PCI de Pagos (Medio/Alto):** auditoría externa en mayo. Mitigación: pre-auditoría ya agendada en abril
- **R3 — Dependencia del integrador (Medio/Alto):** 3 arquitectos clave sin respaldo. Mitigación: plan de transferencia de conocimiento y 2 contrataciones internas
- **R4 — Capacidad de adopción del negocio (Alto/Medio):** Operaciones sin sponsor dedicado. Mitigación: **requiere decisión del board**
- **R5 — Alcance de Analítica no congelado (Alto/Medio):** crecimiento de requerimientos. Mitigación: **requiere decisión del board**

**Visual sugerido:** Diagrama — matriz de riesgo 5×5 (probabilidad × impacto) con los 5 riesgos ubicados como burbujas numeradas y flechas de tendencia.

**Notas del presentador:** Señalar que dos de los cinco riesgos solo se pueden cerrar con decisiones del board, no con acción del equipo. Mencionar que R1 ya bajó de probabilidad respecto al trimestre anterior.

---

## SLIDE 10 — Riesgos Materializados y Lecciones Aprendidas

**Contenido:**
- Riesgo materializado: subestimación de la deuda de datos del sistema legado → impacto real de 6 semanas y $520K
- Riesgo evitado: falla de performance detectada en pruebas de carga antes de go-live (habría afectado a 38K usuarios)
- Lección 1: incluir un assessment de calidad de datos **antes** de fijar la línea base, no durante
- Lección 2: los módulos con sponsor de negocio activo avanzaron 2.3× más rápido
- Acción institucional: ambas lecciones ya incorporadas al estándar de la PMO para nuevos programas

**Visual sugerido:** Tabla — tres columnas: Qué pasó / Impacto cuantificado / Qué cambiamos permanentemente.

**Notas del presentador:** Mostrar transparencia sobre el error gana credibilidad para el ask de presupuesto. El dato de 2.3× es la evidencia que sostiene el pedido de sponsor de negocio en el slide 14.

---

## SLIDE 11 — Roadmap Q2 2025: Estabilizar y Certificar

**Contenido:**
- **Abril:** cierre de remediación de datos (hito M12) + pre-auditoría PCI
- **Mayo:** certificación PCI de Pagos + inicio de UAT de CRM
- **Junio:** go-live de Pagos y CRM + migración del 70% de usuarios
- Entregables de habilitación: capacitación a 240 usuarios de Operaciones, runbooks de soporte
- Métricas de salida de Q2: 75% de avance global, 6 de 7 módulos en producción, 70% de usuarios migrados

**Visual sugerido:** Diagrama — timeline horizontal de 3 meses con swimlanes por módulo, hitos en forma de diamante y compuertas de decisión marcadas.

**Notas del presentador:** El mensaje es que Q2 es trimestre de ejecución, no de nuevas definiciones: todo está ya planificado y con recursos asignados. La compuerta crítica es la certificación PCI de mayo.

---

## SLIDE 12 — Roadmap Q3 2025: Completar y Apagar el Legado

**Contenido:**
- **Julio:** go-live de App Móvil + decommissioning de los primeros 3 sistemas legados
- **Agosto:** go-live del módulo de Analítica (sujeto a decisión del board) + **cierre funcional del programa**
- **Septiembre:** hypercare, migración del 100% de usuarios y transición formal a operación/BAU
- Beneficios proyectados al cierre: $4.6M de ahorro anualizado, -$780K/año en costo de mantenimiento legado
- Cierre del programa: reporte final de beneficios al board en octubre 2025

**Visual sugerido:** Diagrama — timeline de 3 meses con una banda inferior de "curva de valor" que muestre el ahorro acumulado creciendo mes a mes.

**Notas del presentador:** Resaltar que apagar el legado es donde está el ahorro real y que no ocurre hasta que el 100% de usuarios estén migrados. Aclarar que el go-live de agosto depende de la decisión del ask #2.

---

## SLIDE 13 — Escenarios de Decisión: Tres Caminos Posibles

**Contenido:**
- **Escenario A — Alcance completo (recomendado):** +$900K, go-live agosto 2025, $4.6M de beneficio anual
- **Escenario B — Analítica diferida a 2026:** +$450K, go-live julio 2025, $3.8M de beneficio anual, legado parcialmente activo
- **Escenario C — Congelar en el alcance actual:** +$120K de cierre, $1.9M de beneficio anual, se pierde el caso de negocio original
- Criterio de comparación: ROI a 3 años → A: 3.1× | B: 2.4× | C: 0.8×
- Recomendación del comité directivo: **Escenario A**, por unanimidad

**Visual sugerido:** Tabla — comparativa de 3 columnas (A/B/C) × 5 filas (inversión, fecha, beneficio anual, ROI 3 años, riesgo residual), con la columna recomendada resaltada.

**Notas del presentador:** Dar al board opciones reales, no un ultimátum: eso cambia la conversación de "aprobar o no" a "elegir". Ser claro en que el Escenario C destruye el caso de negocio que este board aprobó en noviembre.

---

## SLIDE 14 — Asks al Board: Tres Decisiones Requeridas Hoy

**Contenido:**
- **Ask 1 — Financiero:** aprobar $900K de contingencia adicional (presupuesto total a $14.1M). *Decisión requerida hoy; sin ella se detiene la remediación de datos el 30 de abril.*
- **Ask 2 — Alcance:** confirmar el Escenario A (Analítica dentro del programa) y congelar su alcance. *Decisión requerida antes del 15 de mayo.*
- **Ask 3 — Gobierno:** nombrar un sponsor de negocio dedicado para Operaciones, con 50% de su tiempo asignado al programa. *Decisión requerida hoy.*
- Soporte solicitado (sin votación): comunicación del CEO sobre la obligatoriedad de la migración
- Próxima revisión al board: **julio 2025** (cierre de Q2)

**Visual sugerido:** Tabla — cuatro columnas: Ask / Qué pedimos / Fecha límite / Consecuencia de no decidir.

**Notas del presentador:** Leer los tres asks textualmente y pedir decisión explícita sobre cada uno antes de cerrar la sesión. La columna de "consecuencia de no decidir" es la que genera la acción: no omitirla.

---

## SLIDE 15 — Cierre: Compromisos y Próximos Pasos

**Contenido:**
- Lo que el equipo se compromete a entregar: go-live completo en agosto, dentro de $14.1M, con 100% de usuarios migrados en septiembre
- Lo que el board decide hoy: contingencia, alcance de Analítica, sponsor de Operaciones
- Cadencia de reporte: dashboard mensual a la mesa + alerta inmediata ante cualquier desviación mayor a 5%
- Hito de confianza: cierre de remediación de datos el 30 de abril — primer indicador de que el plan se sostiene
- Agradecimiento y apertura a preguntas

**Visual sugerido:** Diagrama — dos columnas enfrentadas: "Nuestros compromisos" vs. "Sus decisiones", con el hito del 30 de abril destacado como punto de verificación.

**Notas del presentador:** Cerrar reforzando la reciprocidad: el equipo asume compromisos medibles y a cambio pide tres decisiones concretas. Dejar la slide en pantalla durante todo el Q&A.

---

## ANEXO SUGERIDO (no presentar, tener a mano)
- A1: Registro completo de riesgos (23 riesgos activos)
- A2: Detalle presupuestal por partida y por vendor
- A3: Arquitectura técnica y plan de decommissioning del legado
- A4: Plan de gestión del cambio y currícula de capacitación
- A5: Caso de negocio original (nov 2024) vs. actualizado

---

**Nota sobre las cifras:** todos los números de este outline son ilustrativos y deben reemplazarse con los datos reales del programa antes de presentar. Están construidos para ser internamente consistentes (porcentajes, totales y proyecciones cuadran entre slides), de modo que puedas usarlos como plantilla y sustituirlos manteniendo la lógica narrativa.