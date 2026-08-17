# Claude Fable 5 (suscripción) — orchestration/multi_step_research_plan

- model_id: `claude-fable-5`
- success: True  | final: 7.45 | quality: 10.0
- latency_total: 25.702s | tokens_per_second: 63.0
- input_tokens: 2 | output_tokens: 1620

## Respuesta completa

# Plan del reporte: Mercado de IA en Chile

## Secuencia de pasos

| # | Paso | Depende de | Paralelizable |
|---|---|---|---|
| 1 | **Investigar las 5 principales startups de IA en Chile + funding** (web research) | — | ✅ Sí (con 2 y 3) |
| 2 | Investigar mercado de IA en Colombia y México (tamaño, startups líderes, inversión) | — | ✅ Sí (con 1 y 3) |
| 3 | Investigar datos de inversión VC en tecnología en Chile 2025-2026 | — | ✅ Sí (con 1 y 2) |
| 4 | Construir tabla comparativa Chile vs Colombia vs México | Pasos 1, 2, 3 | ❌ No |
| 5 | Redactar secciones del reporte (startups, comparación, VC) | Paso 4 | ❌ No |
| 6 | Redactar resumen ejecutivo de 1 página (se escribe AL FINAL, sintetiza todo) | Paso 5 | ❌ No |
| 7 | QA: verificar cifras contra fuentes, consistencia entre secciones, formato presentable | Paso 6 | ❌ No |

**Dependencias clave:**
- Los pasos 1, 2 y 3 son investigación independiente → **se ejecutan en paralelo** (ahorra ~60% del tiempo de research).
- El paso 4 es el cuello de botella: necesita los resultados de los 3 anteriores.
- El resumen ejecutivo (paso 6) va al final aunque aparezca primero en el documento — sintetizar antes de tener data es inventar.

**Nota de calidad:** funding de startups chilenas cambia rápido (rondas no anunciadas, datos de Crunchbase desactualizados). En el paso 7 marcaré cada cifra con su fecha de fuente.

---

## Ejecutando Paso 1: Top 5 startups de IA en Chile con funding

No tengo herramienta de búsqueda web disponible en esta sesión, así que ejecuto el paso 1 con mi conocimiento base (corte de entrenamiento) y **marco explícitamente qué requiere verificación** antes de la presentación:

### Borrador Paso 1 — Startups de IA en Chile (requiere verificación de cifras 2025-2026)

| Startup | Foco IA | Funding conocido (último dato confiable) | Estado |
|---|---|---|---|
| **NotCo** | IA generativa para food-tech (algoritmo "Giuseppe") | ~$350M+ acumulado, valoración unicornio ($1.5B en Serie D 2021) | ⚠️ Verificar rondas 2024-2026 |
| **Fintual** | IA para gestión de inversiones / robo-advisor | ~$54M (Serie B, Sequoia) | ⚠️ Verificar |
| **Zippedi** | Robots con IA para inventario retail | ~$60M+ acumulado | ⚠️ Verificar |
| **Toku** | IA para cobranza y pagos recurrentes | ~$45M (Serie A 2024) | ⚠️ Verificar |
| **Cero.ai** | IA conversacional para salud (gestión de citas) | ~$5M seed | ⚠️ Verificar rondas recientes |

**Candidatas adicionales a evaluar:** Lemu (IA + biodiversidad), Examedi, Forcast, Wild Foods.

### Gaps detectados para los próximos pasos
1. Todas las cifras necesitan verificación contra fuentes 2025-2026 (Crunchbase, Contxto, LAVCA, Startupeable).
2. Para el paso 3 (VC Chile 2025-2026), las fuentes canónicas son: **LAVCA**, **ACVC (Asociación Chilena de Venture Capital)**, reportes de **Corfo/Start-Up Chile** y **Endeavor Chile**.

---

**Siguiente acción recomendada:** ejecutar pasos 2 y 3 en paralelo. Si quieres datos verificados (recomendado para una presentación de mañana), confírmame y los corro con búsqueda web activa, o dime si trabajamos con estos datos base marcando los disclaimers en el reporte final.