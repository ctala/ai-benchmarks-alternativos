# Jubilación de Modelos AI - Octubre 2026

**Fecha**: 2026-10-11 (actualizado con Claude 5.5 family)  
**Decisión**: Roster de 100 modelos (62 activos + 38 cupos) — **Regla Estricta**

## Resumen Ejecutivo

- **Total modelos en catálogo**: 227 (217 originales + 10 nuevos)
- **Activos**: 62
- **Jubilados**: 165
- **Cupos reservados**: 38

### Cambios con Claude 5.5 Family

Se agregaron 4 modelos Claude nuevos (Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1):
- ✅ **Claude Haiku 5.5**: ACTIVO (no dominado)
- ❌ **Claude Sonnet 5.5**: JUBILADO (dominado por Claude Sonnet 5)
- ✅ **Claude Opus 5.5**: ACTIVO (no dominado)
- ❌ **Claude Fable 5.1**: JUBILADO (dominado por Claude Fable 5)

### Desglose de Jubilados

**Orden de precedencia** (un solo motivo por modelo):

1. **Retired**: 16 (deprecados por proveedor)
2. **Provider Variant**: 54 (miden serving, no calidad)
3. **Sin Runs**: 26 (nunca medidos, 0 runs)
4. **Dominados**: 69 (**TODOS** — regla estricta, incluye 2 de los 4 Claude nuevos)

**Verificación**: 16 + 54 + 26 + 69 = **165 jubilados** ✓  
**Total**: 62 activos + 165 jubilados = **227** ✓

### Dominados

- **Total detectados**: 69 (antes 62)
- **Jubilados**: 69 (TODOS)
- **Quedan activos**: 0

**Regla estricta vigente**: Todos los dominados se jubilan sin excepciones.

## Definición de Familia

**Familia** = mismo proveedor + misma línea base del modelo, sin importar la generación.

Ejemplos:
- Qwen 3.5, 3.6, 3.7, 3.8 → "Qwen"
- GPT-5.5, GPT-5.6 Luna → "GPT"  
- Claude Opus 4.7, 4.8, 5.5 → "ClaudeOpus"
- Claude Sonnet 4.6, 5, 5.5 → "ClaudeSonnet"
- Claude Fable 5, 5.1 → "ClaudeFable"

## Proyección de Costos

### Criterio de Medición Mensual

**Solo se miden**:
1. **Modelos nuevos** (ocupan los 38 cupos) → examen completo
2. **Activos que cambien** → re-medición parcial

**NO se vuelven a medir** los activos que no cambien.

### Costo Mensual Estimado

**~$100/mes** (estimado, actualizado con 62 activos)

**Supuestos marcados**:
- ~10 lanzamientos nuevos/mes (de 38 cupos disponibles)
- ~6 activos cambian/mes

**Costos base** (medidos abr-sep 2026):
- Examen completo: $8.56 promedio (rango $0.08-$28)
- Re-medición parcial: $1.67/modelo

**Cálculo**:
- Modelos nuevos: 10 × $8.56 = $85.60
- Activos que cambian: 6 × $1.67 = $10.02
- **Total**: ~$96/mes (similar a estimación previa)

### Examen Completo de Todos los Activos

**$530.72** (si se re-midieran todos los 62)

- Cálculo: 62 × $8.56 = $530.72

---

Ver `docs/jubilacion-2026-10.json` para datos estructurados completos.

**Refs**: Decisión tomada 10-oct-2026, actualizada 11-oct-2026 con Claude 5.5 family
