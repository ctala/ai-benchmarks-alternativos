# Nemotron 3 Ultra 550B — presentation/slide_outline

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.46 | quality: 8.68
- latency_total: 73.517s | tokens_per_second: 70.1
- input_tokens: 146 | output_tokens: 5153
- judge_score: 4.2 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

Aquí tienes el outline completo, estructurado para una narrativa ejecutiva de alto impacto (formato "Situación → Implicación → Decisión").

---

### **Metadatos de la Presentación**
*   **Proyecto:** Plataforma Digital 2.0
*   **Audiencia:** Board de Directores
*   **Duración estimada:** 20 min presentación + 10 min Q&A
*   **Tono:** Estratégico, transparente, orientado a decisiones (no operacional).

---

### **Slide 1: Portada**
*   **Título:** Plataforma Digital 2.0 — Estado del Programa & Próximos Hitos Críticos
*   **Subtítulo:** Revisión Ejecutiva Q1 202X | Decisiones Requeridas para Q2-Q3
*   **Visual:** Imagen de fondo corporativa (clean), Logo de la compañía, Fecha, Clasificación: *Confidencial - Board Only*.
*   **Notas:** "Bienvenidos. En 20 minutos cubriremos dónde estamos realmente, los 3 riesgos que definen el éxito del año y las 2 decisiones que necesitamos de ustedes hoy para desbloquear el roadmap."

---

### **Slide 2: Resumen Ejecutivo (Executive Summary / "TL;DR")**
*   **Título:** Veredicto: **Ambar** — Entrega MVP en riesgo sin decisiones de alcance/recursos esta semana.
*   **Bullets:**
    *   **Progreso Real:** 62% completado vs 70% planificado (retraso concentrado en migración de datos legacy).
    *   **Presupuesto:** 85% ejecutado vs 75% planificado (overrun 13% por licencias Cloud no previstas).
    *   **Riesgo Crítico #1:** Falta de definición de "Done" para MVP con Negocio retrasa UAT 3 semanas.
    *   **Ask Principal:** Aprobación de *Change Request* ($1.2M / 4 semanas) **O** recorte de alcance "Módulo Analytics" para salvar fecha Go-Live Septiembre.
*   **Visual:** **Dashboard Semáforo (RAG Status)** con 4 KPIs: Alcance, Tiempo, Coste, Riesgo (3 Amber, 1 Red).
*   **Notas:** "No lean el detalle; lean el veredicto. Estamos en Ambar por dos factores controlables: alcance difuso y coste cloud. Hoy pedimos autorización para corregir rumbo."

---

### **Slide 3: Estado Actual del Programa (Current State)**
*   **Título:** ¿Dónde estamos hoy? — Arquitectura Técnica & Entregables Completados
*   **Bullets:**
    *   **Core Platform (100%):** Kubernetes cluster prod, CI/CD, Observabilidad, Security Hardening — **Certificado ISO 27001**.
    *   **Módulo Clientes (85%):** Onboarding digital, KYC automatizado, Portal Self-Service — *En UAT*.
    *   **Módulo Operaciones (45%):** Motor de reglas, Integración Core Bancario (Legacy) — **Cuello de botella actual**.
    *   **Deuda Técnica:** 12 hallazgos críticos de PenTest resueltos; 3 medios pendientes (no bloqueantes).
*   **Visual:** **Diagrama de Arquitectura Simplificado** (C4 Level 1/2) con checkmarks verdes/ámbar por componente.
*   **Notas:** "La plataforma base es sólida y segura. El problema no es 'construir tech', es integrar con el legacy y alinear expectativas de negocio."

---

### **Slide 4: Métricas de Progreso vs Plan (Earned Value / Velocity)**
*   **Título:** Métricas Objetivas: Valor Ganado (EV) vs Planificado (PV) — Tendencia Q1
*   **Bullets:**
    *   **SPI (Schedule Performance Index): 0.88** — Retraso acumulado 3 sprints (principalmente Data Migration).
    *   **CPI (Cost Performance Index): 0.88** — Sobrecoste por escalado automático Cloud (variable) + contractors especialistas Legacy.
    *   **Velocity Equipo Core:** Estable en 85 pts/sprint (predecible).
    *   **Defect Escape Rate:** 2% en Prod (Objetivo <5%) — Calidad alta.
    *   **Adopción Beta (Usuarios Piloto):** 320 usuarios activos, NPS 42/100 (Objetivo >40).
*   **Visual:** **Gráfico de Líneas (Burn-up Chart)** comparando Scope Completado vs Planificado vs Línea Base Presupuesto (EV/PV/AC).
*   **Notas:** "La velocidad del equipo es sana; la varianza viene de dependencias externas (Legacy) y costes variables Cloud. No es un problema de productividad, es de estimación de incertidumbre."

---

### **Slide 5: Análisis de Presupuesto — Ejecutado vs. Planeado (CAPEX/OPEX)**
*   **Título:** Situación Financiera: Overrun 13% ($1.8M) — Drivers y Proyección Fin de Año
*   **Bullets:**
    *   **Budget Approved:** $14.2M (CAPEX $9.5M / OPEX $4.7M).
    *   **Actuals YTD:** $12.1M gastados (85% del total anual en Q1).
    *   **Drivers Principales:** (1) Licencias Cloud +$0.9M (uso real vs estimado), (2) Contractors Legacy +$0.6M, (3) PenTest/Compliance +$0.3M.
    *   **Forecast EAC (Estimate at Completion):** $16.5M **sin cambios** vs $15.4M **con CR aprobado** (optimización Cloud + scope cut).
    *   **Runway:** Fondos actuales cubren hasta **Junio 15** sin inyección adicional.
*   **Visual:** **Tabla Comparativa (Presupuestado vs Real vs Forecast)** + **Gráfico de Cascada (Waterfall)** explicando la varianza $1.8M.
*   **Notas:** "Gastamos rápido porque avanzamos en la parte cara (infra/licencias) primero. El overrun es explicable y recuperable *si* decidimos hoy. Sin decisión, nos quedamos sin caja en 6 semanas."

---

### **Slide 6: Top 5 Riesgos Críticos & Mitigación (Risk Heatmap)**
*   **Título:** Mapa de Riesgos: 2 Críticos, 2 Altos, 1 Medio — Foco en "Go-Live Septiembre"
*   **Bullets:**
    1.  🔴 **CRÍTICO: Definición de MVP Scope (Negocio).** *Prob: Alta | Impacto: Alto.* Owner: CPO. *Mitigación:* Workshop "Scope Freeze" esta semana + CR formal.
    2.  🔴 **CRÍTICO: Migración Datos Legacy (Calidad/Volumen).** *Prob: Media | Impacto: Muy Alto.* Owner: CTO. *Mitigación:* Paralelismo 2 semanas + Data Stewards dedicados (requiere budget).
    3.  🟠 **ALTO: Retención Talento Clave (3 Architects).** *Prob: Media | Impacto: Alto.* Mitigación: Retention bonus aprobado RRHH.
    4.  🟠 **ALTO: Dependencia Proveedor Core Bancario (APIs inestables).** *Prob: Alta | Impacto: Medio.* Mitigación: SLA contractual + Mocks internos.
    5.  🟡 **MEDIO: Cambio Regulatorio (Normativa Datos Q3).** *Prob: Baja | Impacto: Alto.* Mitigación: Arquitectura "Privacy by Design" ya implementada.
*   **Visual:** **Matriz de Calor (Heatmap 5x5)** con flechas de tendencia (↑ ↓ →) vs mes anterior.
*   **Notas:** "Los dos rojos son decisiones de *gobernanza*, no técnicos. El #1 lo resuelve este Board hoy. El #2 lo resuelve budget para Data Stewards."

---

### **Slide 7: Deep Dive — Cuello de Botella: Migración de Datos Legacy**
*   **Título:** El "Elefante en la Sala": Calidad y Volumen de Datos Históricos (12 TB / 14 Sistemas)
*   **Bullets:**
    *   **Realidad:** 40% de los campos críticos sin dueño de negocio definido (Data Ownership gap).
    *   **Impacto:** Re-work en scripts ETL = 3 sprints perdidos en Q1.
    *   **Plan A (Actual):** Limpieza "on-the-fly" durante migración → **Riesgo alto de corte productivo fallido.**
    *   **Plan B (Recomendado):** Sprint 0 de "Data Prep" (4 sem, 2 FTEs Data Stewards + 1 Arch) → **Asegura corte limpio, cuesta $180k.**
*   **Visual:** **Diagrama de Flujo (Sankey o Swimlane)** mostrando estado actual: Fuente Legacy → Staging → Limpieza → Target vs Ideal.
*   **Notas:** "Este es el riesgo técnico #1. No podemos 'codear' nuestra salida de mala data de origen. Necesitamos dueños de negocio asignados *ya* o aceptamos retraso en Go-Live."

---

### **Slide 8: Roadmap Q2-Q3 — Hitos Comprometidos (Baseline)**
*   **Título:** Roadmap Comprometido (Baseline) — *Sujeto a Decisiones de Hoy (Slide 11)*
*   **Bullets:**
    *   **Q2 (Abr-Jun):**
        *   Sprint 10-14: Completar Módulo Operaciones (Integración Core).
        *   **Hito M1 (May 15): Code Freeze MVP Funcional.**
        *   **Hito M2 (Jun 30): UAT Finalizado & Performance Test Pass.**
    *   **Q3 (Jul-Sep):**
        *   **Hito M3 (Jul 15): Go/No-Go Decision Gate.**
        *   **Hito M4 (Sep 02): Go-Live Producción (Big Bang / Canary 10%).**
        *   Sprint 15-18: Hypercare + Módulo Analytics (Fase 2).
*   **Visual:** **Timeline / Gantt de Alto Nivel** con "Gates" de decisión (Diamantes) y hitos (Rombo). Marcar zona de "Buffer" (2 semanas).
*   **Notas:** "Este es el plan 'feliz'. Tiene 2 semanas de buffer total. Cualquier variación en Scope o Data Migration come buffer y pone en riesgo Septiembre."

---

### **Slide 9: Roadmap Q2-Q3 — Escenarios Alternativos (Scenario Planning)**
*   **Título:** Tres Escenarios para Q2-Q3 — Impacto en Fecha, Coste y Valor
*   **Bullets:**
    *   **Escenario A: "Full Scope" (CR Aprobado +$1.2M / +4 sem).**
        *   Go-Live: **Nov 15**. Entrega todo lo prometido (incl. Analytics). Riesgo: Fatiga organización, mercado.
    *   **Escenario B: "MVP Seguro" (Recorte Analytics + Data Prep Sprint) — *Recomendación PMO*.**
        *   Go-Live: **Sep 15** (On target). Coste: +$180k (Data Stewards). Valor: Core business operativo 2 meses antes.
    *   **Escenario C: "Force Fit" (Sin cambios, presión equipo).**
        *   Go-Live: **Oct 15** (Probabilidad éxito <30%). Coste oculto: Burnout, deuda técnica, bugs en Prod.
*   **Visual:** **Tabla Comparativa de Escenarios** (Fecha, Coste Total, Scope Entregado, Riesgo Ejecución, Valor Negocio).
*   **Notas:** "No les pido opiniones, les pido que elijan A o B. C no es una opción responsable. Mi recomendación es B: protege la fecha, minimiza coste, entrega valor core."

---

### **Slide 10: Organización, Gobernanza & Talento**
*   **Título:** Estructura de Gobernanza & Salud del Equipo
*   **Bullets:**
    *   **Steering Committee:** Quincenal (Este Board). **Ask:** Cambio a **Semanal** durante Q2 (Critical Path).
    *   **Product Owners:** 3 asignados (Clientes, Ops, Plataforma). *Gap:* Falta PO Data/Analytics (contratando).
    *   **Equipo Técnico:** 42 FTEs (28 internos, 14 contractors). **Attrition YTD: 4.5%** (Bajo media sector).
    *   **Riesgo Personas:** 3 Architects "Single Point of Failure". Plan sucesión iniciado.
    *   **Cultura:** eNPS Equipo +12 (Subió 5 pts vs Q4). Psychological Safety: Alta.
*   **Visual:** **Organigrama Ligero (RACI simplificado)** + **KPIs Personas** (Attrition, eNPS, Bus Factor).
*   **Notas:** "El equipo está sano y motivado, pero frágil por concentracion de conocimiento. La gobernanza semanal en Q2 es no negociable para velocidad de decisión."

---

### **Slide 11: Decisiones Requeridas — "The Asks" (Core Slide)**
*   **Título:** **Acciones Requeridas del Board — Para Decidir HOY**
*   **Bullets:**
    1.  **APROBAR Change Request MVP (Escenario B):** Recortar "Módulo Analytics v1" del scope Go-Live Sept. → **Ahorra 6 sprints / $400k**. *Mover a Fase 2 (Q4).*
    2.  **AUTORIZAR Budget Extra $1.2M (CAPEX):**
        *   $180k Data Stewards (4 sem) — *Crítico para migración.*
        *   $600k Optimización Cloud (Reserved Instances / FinOps) — *Reduce run-rate 25%.*
        *   $420k Buffer contingencia (Legacy APIs / Regulatorio).
    3.  **DESIGNAR "Data Owners" de Negocio (3 nombres):** Responsables de firma de calidad datos para Migración. Plazo: **Viernes EOD**.
    4.  **VALIDAR Gobernanza Semanal (Steering Comm):** 30 min / Lunes 9:00 AM — Solo decisiones, no reporting.
*   **Visual:** **Lista numerada grande (Big Rocks)** con Owner y Deadline. Formato "Decision Log".
*   **Notas:** "Estas 4 decisiones desbloquean el 90% de la incertidumbre. Si salimos sin dueños de datos y sin CR firmado, el proyecto entra en 'modo supervivencia' y perdemos Septiembre."

---

### **Slide 12: Análisis de Valor de Negocio (Business Case Refresh)**
*   **Título:** ¿Sigue valiendo la pena? — NPV / ROI Actualizado vs Business Case Original
*   **Bullets:**
    *   **Business Case Original:** NPV $45M (5 años) | ROI 2.8x | Payback 18 meses post Go-Live.
    *   **Actualización (Escenario B - Recomendado):**
        *   Coste Total Proyectado: $15.4M (+8% vs original $14.2M).
        *   Beneficios Anticipados (Go-Live Sep vs Nov): +$3.2M NPV (captura campaña Q4).
        *   **NPV Ajustado: $48.2M | ROI 3.1x | Payback 16 meses.**
    *   **Sensibilidad:** Si Go-Live > Oct 15, NPV cae a $38M (ROI < 2.5x).
*   **Visual:** **Gráfico de Barras Apiladas** (Coste vs Beneficios Acumulados Año 1-5) comparando Original vs Escenario B vs Escenario A.
*   **Notas:** "Paradójicamente, *recortar scope (Analytics) y gastar $1.2M extra ahora* **mejora** el NPV y el Payback porque adelanta el Go-Live del Core. El coste de oportunidad de 2 meses es mayor que el overrun."

---

### **Slide 13: Preparación Operativa & Go-Live Strategy (Readiness)**
*   **Título:** Estrategia de Despliegue: Canary Release + Rollback Plan — Readiness Checklist
*   **Bullets:**
    *   **Estrategia:** Canary 10% (Usuarios Beta + Internos) → 50% (Semana 2) → 100% (Semana 4). **Rollback < 30 min** (Blue/Green validado).
    *   **Runbooks:** 12/15 completados (Faltan 3 Legacy Fallback).
    *   **Soporte Post-Go-Live (Hypercare):** 4 semanas / 24x7 (Equipo mixto Interno + Vendor).
    *   **Comunicación:** Plan Change Management lanzado (Townhalls, Guías, Champions Network 50 users).
    *   **Dependencia Crítica:** Aprobación Seguridad Info (CISO) para Go/No-Go Gate (Jul 15).
*   **Visual:** **Checklist Visual (Matriz Madurez)** con % completado por pilar: Tech, Ops, Security, Business, People.
*   **Notas:** "Técnicamente sabemos hacer el despliegue seguro. El riesgo operativo es la adopción de negocio y la estabilidad de las APIs Legacy en las primeras 72h."

---

### **Slide 14: Próximos Pasos Inmediatos (Next 30 Days)**
*   **Título:** Plan de Acción Inmediato (Post-Board) — "First 30 Days"
*   **Bullets:**
    *   **Semana 1:** Firmar CR / Scope Freeze / Nombrar Data Owners / Kickoff Data Prep Sprint.
    *   **Semana 2:** Iniciar FinOps Cloud Optimization (Quick wins: Apagar envs dev nocturnos, RIs).
    *   **Semana 3:** Completar Runbooks Legacy Fallback / Mocks API Core listos.
    *   **Semana 4:** **Gate Interno:** Code Freeze MVP Funcional (Target May 15) → Entrada UAT.
    *   **KPIs Semanales a Reportar:** SPI, % Data Quality, Cloud Spend/Día, Defectos Bloqueantes.
*   **Visual:** **Kanban / Tablero 4 Semanas** (To Do / Doing / Done) con Dueños y Fechas.
*   **Notas:** "Esto no es una wishlist; es el plan de trabajo del lunes. Les enviaré el 'Decision Log' firmado hoy y el status semanal todos los lunes a las 8 AM."

---

### **Slide 15: Cierre / Q&A / Appendix**
*   **Título:** Plataforma Digital 2.0 — Listos para Ejecutar. Necesitamos su Mandato.
*   **Bullets:**
    *   **Mensaje Final:** La plataforma es sólida, el equipo es capaz, el plan es realista **SI** decidimos hoy.
    *   **Contacto:** [Nombre PMO/Director Programa] | [Email] | [Tel] — Disponible para deep-dives 1:1 esta semana.
    *   **Apéndice Disponible:** Detalle Financiero, Technical Debt Register, Risk Register Completo, Plan de Pruebas, Contratos Proveedores.
*   **Visual:** Imagen corporativa inspiradora / Foto equipo (opcional) / QR Code a Repo Documentación Board.
*   **Notas:** "Gracias por el tiempo. La pelota está en su tejado. Estoy a disposición para cualquier detalle técnico o financiero en los próximos días. Vamos a por Septiembre."

---

### **Guía Rápida para el Presentador (Cheat Sheet)**

| Minuto | Slide | Foco Clave | "Watch out" |
| :--- | :--- | :--- | :--- |
| 0-2 | 1-2 | **Hook & Veredicto** | No pidas permiso para presentar, *informa* el estado. |
| 2-6 | 3-5 | **Evidencia (Hechos/Datos)** | Velocidad: "Equipo bien" vs "Estimación mal". No culpes al equipo. |
| 6-10 | 6-7 | **Riesgos Reales (No teatro)** | Dato: "40% datos sin dueño". Eso duele, pero es verdad. |
| 10-15 | 8-9 | **Escenarios & Recomendación** | **No preguntes "qué hacemos?". Di: "Recomiendo B porque..."** |
| 15-18 | 10-12 | **Gobernanza & Business Case** | Conecta dinero con valor. $1.2M extra = +$3.2M NPV. |
| 18-20 | 13-15 | **Cierre & Ask Explícito** | Lee las 4 decisiones del Slide 11 una a una. Pide "Sí/No" por cada una. |

---

### **Apéndice Sugerido (Slides Ocultas / Backup para Q&A)**
*   **A1:** Detalle Financiero Mensual (Cashflow Proyección).
*   **A2:** Registro Completo de Riesgos (RAID Log).
*   **A3:** Deuda Técnica Detallada & Plan Pago.
*   **A4:** Matriz de Trazabilidad Requisitos -> Test Cases.
*   **A5:** Benchmark Costes Cloud vs Peers / Industria.
*   **A6:** Plan de Comunicación Externa / Clientes (Go-Live).