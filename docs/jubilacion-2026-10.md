# Jubilación de Modelos — Octubre 2026

> **Fecha**: 10 de octubre de 2026  
> **Objetivo**: Reducir el catálogo de 217 modelos a 100 activos que se vuelvan a medir
> **Razón**: Controlar el costo mensual de medición manteniendo la diversidad y calidad del benchmark

## Resumen Ejecutivo

| | Cantidad |
|---|---:|
| **Total modelos en catálogo** | 217 |
| **Jubilados** | 117 |
| **Activos (se vuelven a medir)** | 90 |
| **Cupos para modelos nuevos** | 10 |
| **Total roster activo** | 100 |

## Reglas de Jubilación

Un modelo **jubilado** queda en el histórico con todos sus datos y sigue siendo consultable, pero **NO se vuelve a medir** en lotes futuros. Los jubilados se documentan con fecha y motivo.

### Criterios (en orden de aplicación)

| # | Criterio | Razón | Cantidad |
|---|---|---|---:|
| **1** | Ya retired por el proveedor | El modelo ya no existe o no es accesible | 16 |
| **2** | Provider variant | Mide infraestructura/serving, no calidad del modelo | 56 |
| **3** | Sin runs (nunca medido) | 0 runs, nunca se midió | 44 |
| **4** | Baja prioridad | No ranked con baja calidad, o ranked pero de los 21 menos prioritarios | 1 |
| | **TOTAL** | | **117** |

### Criterio 1: Retired por el proveedor

Modelos que ya no tienen endpoint válido o fueron deprecados explícitamente.

**Ejemplos**:
- Devstral Small — llegó a estar #5, OpenRouter lo deprecó
- Grok 4.1 Fast — xAI migró a Grok 4.3
- MiMo-V2-Flash — Xiaomi deprecó el modelo

### Criterio 2: Provider variants

Estos modelos miden **cómo una infraestructura sirve un modelo**, no la calidad del modelo en sí. El modelo base ya está medido en el plano común (generalmente OpenRouter).

**Por qué existen**: Para casos donde el serving difiere materialmente:
- Qwen 3.5 397B: 8,42 en NIM vs 7,97 en Ollama Cloud (Δ 0,45)
- Suscripciones (Claude Code, MiniMax Agent Pro)
- Infraestructura local (DGX Spark, Ollama local)

**Ejemplos** (56 total):
- `claude-opus-5-sub` — Claude Opus 5 vía suscripción
- `nim-qwen3.5-397b` — Qwen 3.5 397B en NVIDIA NIM
- `local-gemma4-31b` — Gemma 4 31B en DGX Spark local

### Criterio 3: Sin runs (nunca medidos)

Modelos que están en el catálogo pero nunca se corrió un benchmark contra ellos (0 runs). Generalmente son:
- Modelos agregados recientemente que no se alcanzaron a medir
- Variantes de esfuerzo (`:thinking`, `-pro`) que requieren configuración especial
- Modelos de tier `:free` que el RUNBOOK desaconseja medir

**Ejemplos** (44 total):
- `deepseek-r1-free`
- `llama-3.3-70b-free`
- `qwen3-coder-free`
- `gemini-flash-thinking`
- `kimi-k2.6-thinking`

### Criterio 4: Baja prioridad / No dominados

⚠️ **Nota importante**: Estos modelos **NO están dominados** por otro de su familia (dominancia = otro modelo de la familia con igual o mejor calidad a menor o igual costo). Simplemente son los de **menor prioridad global** cuando se aplican los otros 3 criterios primero.

Para llegar a **90 activos** (dejando 10 cupos para modelos nuevos), se jubilan los **21 modelos de menor prioridad global** del catálogo restante.

**Orden de prioridad** (de mayor a menor):
1. ✅ Ranked con alta calidad (≥8.0) — **permanecen**
2. ✅ Ranked con calidad media-alta (7.75-8.0) — **permanecen**  
3. ⚠️ No-ranked con alta calidad (≥8.5) — **permanecen**
4. ❌ Ranked con baja calidad (<7.75) — **se jubilan 7 de estos**
5. ❌ No-ranked con calidad <8.5 — **se jubilan 14 de estos**

**Resultado**: Se jubilan 14 no-ranked + 7 ranked de menor calidad (Q 7.26-7.74). **Estos podrían reactivarse** si se agrega un modelo de su familia que claramente los domine, liberando su cupo.

**Ejemplos jubilados por este criterio (21 total)**:
- Kimi K2 Thinking (Q=5.00, 2 runs, no ranked)
- Mistral Nemo (Q=7.26, 522 runs, no ranked)
- Llama 3.1 8B Instant (Q=7.26, 155 runs, ranked)
- Gemini 3.1 Pro (Q=7.48, 143 runs, ranked)
- Qwen 3.6 27B base (Q=7.74, 182 runs, ranked)

## Cómo un Modelo Puede Volver

Un modelo jubilado puede reactivarse si:

1. **El proveedor lo relanza** (caso: un modelo retired vuelve con nueva versión)
2. **Hay caso de uso documentado** que lo requiere específicamente
3. **Se libera presupuesto** por jubilación de otros modelos
4. **Cambio de criterios** en una ventana de medición trimestral

**Prioridad para reactivar** (cuando hay cupo):
1. Modelos ranqueados (≥50 runs) jubilados por dominancia
2. Modelos tested (≥20 runs) con caso de uso documentado
3. Open source sobre propietarios a igual calidad
4. Más recientes (últimos 6 meses)

## Lista Completa de Modelos Jubilados

### Por Criterio 1: Retired (16)

| Modelo | Runs | Calidad | Razón del Proveedor |
|---|---:|---:|---|
| Devstral Small | 34 | 8.03 | OpenRouter: 'No endpoints found'. Llegó a estar #5 del ranking |
| Grok 4.1 Fast | 86 | 7.91 | xAI lo deprecó; recomienda migrar a Grok 4.3 |
| Nemotron Super 49B v1.5 | 128 | 8.00 | OpenRouter 404; NVIDIA movió su oferta a Nemotron 3 |
| MiMo-V2-Flash | 31 | 7.78 | Xiaomi deprecó el modelo |
| MiMo-V2-Pro | 79 | 7.99 | Xiaomi deprecó el modelo |
| ... y 11 más | | | Ver `docs/data/models.json` |

### Por Criterio 2: Provider Variants (56)

Estos modelos **siguen siendo medibles** en sus variantes de proveedor cuando hay necesidad de comparar infraestructuras. No se jubilan sus datos históricos.

| Modelo | Runs | Descripción |
|---|---:|---|
| claude-opus-5-sub | 113 | Claude Opus 5 vía suscripción ($20/mes) |
| nim-qwen3.5-397b | 94 | Qwen 3.5 397B en NVIDIA NIM |
| local-gemma4-31b | 84 | Gemma 4 31B en DGX Spark local |
| claude-fable-5-sub | 102 | Claude Fable 5 vía suscripción |
| ... y 52 más | | Ver lista completa en `docs/jubilacion-2026-10.json` |

### Por Criterio 3: Sin Runs (44)

| Modelo | Razón |
|---|---|
| deepseek-r1-free | Tier `:free`, no se mide según RUNBOOK |
| llama-3.3-70b-free | Tier `:free`, no se mide según RUNBOOK |
| qwen3-coder-free | Tier `:free`, no se mide según RUNBOOK |
| minimax-m2.7-highspeed | Requiere API directa MiniMax, pendiente |
| gemini-flash-thinking | Variante thinking no medida |
| kimi-k2.5-thinking | Variante thinking no medida |
| kimi-k2.6-thinking | Variante thinking no medida |
| ... y 37 más | Ver lista completa en `docs/jubilacion-2026-10.json` |

### Por Criterio 4: Baja Prioridad (21)

Para llegar exactamente a 100 activos, se jubilan los **21 modelos de menor prioridad**:

| Modelo | Runs | Calidad | Ranked | Motivo |
|---|---:|---:|:---:|---|
| Kimi K2 Thinking | 2 | 5.00 | ❌ | No ranked, calidad muy baja |
| Mistral Nemo | 522 | 7.26 | ❌ | No ranked, calidad baja |
| Qwen 3-Next 80B Thinking | 156 | 7.52 | ❌ | No ranked |
| Nemotron 3 Base 33B (Spark) | 86 | 7.82 | ❌ | No ranked, local |
| Nemotron 3 Nano Omni Reasoning | 147 | 7.99 | ❌ | No ranked |
| Nemotron Nano 9B v2 | 134 | 8.02 | ❌ | No ranked |
| DiffusionGemma 26B-A4B | 91 | 8.14 | ❌ | No ranked, local |
| Gemma 4 12B (Spark, reasoning) | 85 | 8.19 | ❌ | No ranked, local |
| Qwen 2.5 72B | 172 | 8.27 | ❌ | No ranked |
| GPT-5.6 Terra Pro | 275 | 8.40 | ❌ | No ranked |
| Gemma 4 12B (Spark Q4) | 86 | 8.49 | ❌ | No ranked, local |
| GPT-5.6 Luna Pro | 264 | 8.50 | ❌ | No ranked |
| LongCat 2.0 | 22 | 8.52 | ❌ | No ranked, pocos runs |
| Sakana Namazu | 1728 | 8.59 | ❌ | No ranked |
| Llama 3.1 8B Instant | 155 | 7.26 | ✅ | Ranked pero calidad más baja |
| Gemini 3.1 Pro | 143 | 7.48 | ✅ | Ranked pero calidad baja |
| Gemini 3.5 Flash | 166 | 7.51 | ✅ | Ranked pero calidad baja |
| Gemini 2.5 Pro | 179 | 7.68 | ✅ | Ranked pero calidad baja |
| Nemotron 3 Nano 30B | 152 | 7.69 | ✅ | Ranked pero calidad baja |
| Grok 4.20 | 146 | 7.70 | ✅ | Ranked pero calidad baja |
| Qwen 3.6 27B base (FP8) | 182 | 7.74 | ✅ | Ranked pero calidad baja |

**Nota**: El criterio preserva diversidad manteniendo los modelos de mayor prioridad: ranked con Q≥7.75 y no-ranked con Q≥8.5 que tienen muestra sólida (≥100 runs) o son únicos en su categoría.

## Los 100 Modelos Activos

Los 100 modelos que **se volverán a medir** en lotes futuros incluyen:

- **107 ranked** (≥50 runs) — menos el 1 jubilado por dominancia
- Cobertura de todas las familias principales
- Diversidad de tiers: free, cheap, medium, premium
- Balance open-source / propietarios
- Representación de todos los proveedores principales

**Ver lista completa**: `docs/jubilacion-2026-10.json` campo `lista_activos`

## Estimación de Costo

### Costos Reales Medidos (Septiembre 2026)

**Fuente**: Lotes de septiembre 2026 en `benchmarks/results/benchmark_202609*.json`, calculados con `benchmarks/calculate_costs.py`.

| Modelo | Runs | Costo por Examen Completo |
|---|---:|---:|
| Mercury 2.5 | 199 | $0.15 |
| DeepSeek V4.1 Flash | 213 | $1.76 |
| Gemini 3.8 Flash | 213 | $7.65 |
| Muse Spark 1.3 | 213 | $12.22 |
| Fugu Max | 213 | $21.03 |
| **Promedio** | | **$8.56** |

**Rango**: $0.15 (modelos ultra-económicos) a $21.03 (thinking models premium)

### Escenario Teórico (re-medición completa)

Si se re-midieran **todos** los modelos mensualmente (lo cual NO sucede en la práctica):

| | Costo Mensual |
|---|---:|
| **217 modelos** (catálogo actual) | $1,858 |
| **100 modelos** (roster activo) | $856 |
| **Ahorro potencial** | **$1,002 (54% reducción)** |

### Escenario REALISTA (medido)

**Basado en CHANGELOG**: El repo publica ~12 versiones al año, con ~10-15 modelos nuevos/actualizados por versión.

| Roster | Modelos re-medidos/mes | Costo Mensual Real |
|---|---|---:|
| **217 modelos** | ~20-30 | $171 - $257 |
| **100 modelos** | ~10-15 | **$86 - $128** |
| **Ahorro real** | | **$85 - $129/mes** |

**Por qué solo 10-15 modelos/mes:**
- Re-medición **NO es automática** — solo cuando:
  1. Sale versión nueva del modelo (distinto ID)
  2. Cambian suites/tests del benchmark (trimestral)
  3. Bug del runner/adapter invalida runs previos
  4. Modelo tiene cambios silenciosos del proveedor (raro)
- La mayoría de los modelos se miden **una vez** y sus resultados permanecen válidos hasta que algo cambie.

**Comando usado**:
```bash
python3 benchmarks/calculate_costs.py --estimar "gpt-5.5" --precio-in 3.0 --precio-out 15.0
```

### Dónde NO está el $29-43

El valor "$29-43 por modelo" citado en versiones previas **era incorrecto**. Ese valor:
- **Existe en DECISIONES.md** pero se refiere al costo de **agregar UNA SUITE NUEVA** (no un modelo completo)
- Viene de la entrada del 13-ago-2026: "Una suite nueva cuesta $29-43 y no invalida ningún run"
- Un examen completo son **22 suites**, no una sola

## Impacto en Diversidad

### Cobertura Preservada

| Aspecto | Antes | Después |
|---|---:|---:|
| Familias de modelos | 13 | 13 ✓ |
| Proveedores | 15+ | 15+ ✓ |
| Open source | 49 | ~45 ✓ |
| Propietarios | 168 | ~55 ✓ |
| Tiers representados | 6 | 6 ✓ |

## Próximos Pasos

1. ✅ Documentar reglas (este archivo)
2. ✅ Generar lista de jubilados (`docs/jubilacion-2026-10.json`)
3. ⏳ Actualizar `DECISIONES.md` con decisión fechada
4. ⏳ Actualizar `METODOLOGIA.md` con sección de jubilación
5. ⏳ Calcular ahorro de costo exacto con `calculate_costs.py`
6. ⏳ Correr `qa.py` para verificar integridad
7. ⏳ Crear PR en draft para revisión

---

**Generado**: 10 de octubre de 2026  
**Por**: Sistema de jubilación de modelos del benchmark  
**Datos fuente**: `docs/data/models.json` (217 modelos, 67.035 runs válidos)
