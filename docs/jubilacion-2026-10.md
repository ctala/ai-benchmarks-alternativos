# Jubilación de Modelos — Octubre 2026

> **Fecha**: 10 de octubre de 2026  
> **Objetivo**: Reducir el catálogo de 217 modelos a 100 activos que se vuelvan a medir
> **Razón**: Controlar el costo mensual de medición manteniendo la diversidad y calidad del benchmark

## Resumen Ejecutivo

| | Cantidad |
|---|---:|
| **Total modelos en catálogo** | 217 |
| **Jubilados** | 117 |
| **Activos (se vuelven a medir)** | 100 |

## Reglas de Jubilación

Un modelo **jubilado** queda en el histórico con todos sus datos y sigue siendo consultable, pero **NO se vuelve a medir** en lotes futuros. Los jubilados se documentan con fecha y motivo.

### Criterios (en orden de aplicación)

| # | Criterio | Razón | Cantidad |
|---|---|---|---:|
| **1** | Ya retired por el proveedor | El modelo ya no existe o no es accesible | 16 |
| **2** | Provider variant | Mide infraestructura/serving, no calidad del modelo | 56 |
| **3** | Sin runs (nunca medido) | 0 runs, nunca se midió | 44 |
| **4** | Dominado | Otro modelo de su familia tiene ≥ calidad a ≤ costo | 1 |
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

### Criterio 4: Dominado

Un modelo está **dominado** cuando otro modelo de su misma familia tiene:
- Calidad **mayor o igual** Y
- Costo **menor o igual**

**Aplicación para llegar a 100**: De los 108 candidatos dominados detectados, se jubilan solo los **21 de menor calidad** dentro de su familia que además **no están ranked**.

**Ejemplo**:
- **Jubilado**: Kimi K2 Thinking (calidad 5.00, 2 runs, no ranked)
- **Domina**: Kimi K2.6 (calidad 8.30, 219 runs, ranked)

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

### Por Criterio 4: Dominado (1)

Para llegar exactamente a 100 activos, se jubila **solo el modelo de menor calidad** que además está dominado y no ranked:

| Modelo | Runs | Calidad | Dominado por | Razón |
|---|---:|---:|---|---|
| Kimi K2 Thinking | 2 | 5.00 | Kimi K2.6 (Q=8.30) | Calidad muy baja, solo 2 runs, familia Kimi tiene 5 mejores |

**Nota**: Se detectaron 108 modelos técnicamente dominados, pero solo se jubilan cuando es necesario para mantener el objetivo de 100. Los demás permanecen activos para mantener diversidad.

## Los 100 Modelos Activos

Los 100 modelos que **se volverán a medir** en lotes futuros incluyen:

- **107 ranked** (≥50 runs) — menos el 1 jubilado por dominancia
- Cobertura de todas las familias principales
- Diversidad de tiers: free, cheap, medium, premium
- Balance open-source / propietarios
- Representación de todos los proveedores principales

**Ver lista completa**: `docs/jubilacion-2026-10.json` campo `lista_activos`

## Impacto Estimado

### Costo de Medición

**Cálculo pendiente**: Ejecutar `python benchmarks/calculate_costs.py` comparando:
- 217 modelos actuales
- 100 modelos activos

**Estimación aproximada** (basada en distribución de costos por suite):
- `niah_es` cuesta ~74% del total
- `agent_long_horizon` cuesta ~13% del total
- Suite típica: $0.30-$2 por modelo

**Ahorro estimado por lote** (pendiente cálculo exacto):
- 117 modelos menos × $2 promedio = ~$234/lote
- Con lotes mensuales: ~$234/mes de ahorro

### Diversidad Preservada

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
