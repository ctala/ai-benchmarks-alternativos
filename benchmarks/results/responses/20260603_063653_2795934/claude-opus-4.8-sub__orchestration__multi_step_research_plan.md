# Claude Opus 4.8 (suscripción) — orchestration/multi_step_research_plan

- model_id: `claude-opus-4-8`
- success: True  | final: 5.38 | quality: 9.16
- latency_total: 262.182s | tokens_per_second: 43.6
- input_tokens: 19140 | output_tokens: 11428
- judge_score: 4.4 | justificación: 

## Respuesta completa

El reporte está completo (la escritura a archivo requiere tu aprobación de permisos — apruébala si quieres el `.md` entregable, o copia directamente desde acá). Resumo lo ejecutado y entrego el resultado:

## ✅ Plan ejecutado

| Paso | Estado | Cómo |
|------|--------|------|
| 1-4. Investigación (startups / VC Chile / Colombia / México) | ✅ | **4 agentes en paralelo** (fan-out, ~2 min total) |
| 5. Verificación cruzada de cifras | ✅ | Cada agente validó contra 2+ fuentes; reconcilié divergencias en rangos |
| 6. Síntesis comparativa | ✅ | Tabla Chile/Colombia/México |
| 7. Resumen ejecutivo 1 pág | ✅ | Al inicio del documento |

---

# Reporte: Estado del Mercado de IA en Chile 2025-2026

## 📄 RESUMEN EJECUTIVO (1 página)

**En una frase:** Chile es un mercado de IA **pequeño en volumen pero el más eficiente de Latinoamérica**, en su primer año de recuperación del capital de riesgo tras la corrección 2022-2024.

1. **VC en recuperación** — 2025 cerró con **USD 249-320M** (53-66 deals), **+57% vs 2024**. Proyección 2026: ~USD 311M, con 67% de fondos planeando aumentar inversión.
2. **Líder en eficiencia, no en tamaño** — 3°-4° en volumen absoluto, pero **#1 en eficiencia de capital** (índice 40.2) y **#1 en VC per cápita** (USD 12.51).
3. **Top 5 startups IA** suman ~USD 650M+: NotCo, Betterfly, Toku, Examedi, Magnar AI.
4. **Regional** — México ~7x mayor (USD 1.8B, 10-11 unicornios); Colombia crece más rápido (+22%) y lidera en regulación.
5. **Brecha de política pública** — Chile carece de política nacional de IA formalizada comparable a CONPES 4144 (Colombia) o la Estrategia 2.0 (México).

**De un vistazo (2025):**

| Métrica | 🇨🇱 Chile | 🇨🇴 Colombia | 🇲🇽 México |
|---|---|---|---|
| Funding VC tech | USD 249-320M | USD 350-700M | USD 1,800M |
| N° deals | 53-66 | 62 | ~140 |
| Crecimiento YoY | +57% | +22% | +53% |
| Startups activas | ~580 | 2,126 | 1,460 |
| Unicornios | 0-2 | ~3 | 10-11 |
| Posición LatAm | 4° | 3° | **2°** |
| Diferencial | **Eficiencia #1** | Velocidad + regulación | Escala + talento |

---

## 1. Top 5 startups de IA en Chile

| # | Startup | Vertical | Funding | Etapa | Inversores clave |
|---|---|---|---|---|---|
| 1 | **NotCo** | Foodtech IA ("Giuseppe") | USD 360-432M | Serie D+ | Tiger Global, L Catterton, Jeff Bezos, Kaszek |
| 2 | **Betterfly** | Insurtech (unicornio) | USD 202.5M | Serie C | DST Global, QED, SoftBank LatAm |
| 3 | **Toku** | Fintech cobranza IA | USD 55M | Serie A (2025) | Oak HC/FT, Gradient Ventures (Google), YC |
| 4 | **Examedi** | Healthtech IA | USD 26.1M | Serie A | General Catalyst, 8VC, YC |
| 5 | **Magnar AI** | Legaltech IA | USD 0.8M | Seed (2025) | Platanus, Carey, ex-Cornershop |

**Toku** es el caso más relevante hoy: Serie A más reciente (abril 2025), IA-core aplicada en producción, mayor Serie A liderada por mujer en LatAm. **Magnar AI** es la apuesta IA-first más pura (USD 800K en 5 meses, 5,000+ abogados).

## 2. Inversión VC tech en Chile 2025-2026

- **2025:** USD 249M (Crunchbase) – 320M (ACVC), **+57% YoY**, ticket promedio USD 4.1-4.7M.
- **2026 (parcial):** USD 58.1M en 3 deals; proyección USD 311M.
- **Regional:** 6-8% del capital LatAm, pero **#1 en eficiencia y per cápita**.
- **Fondos:** Kayyak (USD 100M), Amarena, Fen, Manutara, Genesis, Aurus, Platanus. **CORFO:** USD 1.06B acumulado, equity-free.
- **IA:** 44% de fondos la consideran requisito de inversión (sin cifra desagregada).

## 3. Comparativa regional

- **🇲🇽 México** — 2° de LatAm (superó a Brasil Q2 2025), USD 1.8B, 10-11 unicornios, 1,460 startups. Ley federal de IA esperada 2026. Puerta de entrada regional por escala.
- **🇨🇴 Colombia** — 3° de LatAm, +22% YoY (la más rápida), 2,126 startups, **CONPES 4144** (política nacional IA 2025-2030) y sandboxes referentes. Bogotá (82%) + Medellín/Ruta N.
- **🇨🇱 Chile gana en:** eficiencia de capital, madurez institucional y estabilidad macro. **Pierde en:** escala, política nacional de IA y pool de talento.

---

## ⚠️ Calidad de datos
Cifras macro reportadas en **rangos** por divergencia metodológica (Crunchbase vs LAVCA/ACVC). 2026 incompleto (~5 meses). Ningún país publica inversión IA desagregada. Algunas cifras de funding (NotCo post-2022, Betterfly 2024-25) sin confirmación pública reciente.

**Fuentes:** LAVCA · Crunchbase · PitchBook · Tracxn · ACVC · ACAFI-EY-Endeavor · CORFO · LatamList · Contxto · Diario Financiero · CONPES 4144 · Startup Genome GSEI 2025 · Endeavor.

---

**Siguiente paso opcional:** ¿Quieres que (a) **guarde el reporte** como `.md`/lo exporte a Google Drive como doc para tu presentación, (b) genere **slides** a partir del resumen ejecutivo, o (c) profundice en algún bloque (ej. due diligence de una startup)? Para guardar el archivo local solo necesito que apruebes el permiso de escritura.