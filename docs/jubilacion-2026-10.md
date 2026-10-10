# Jubilación de Modelos AI - Octubre 2026

**Fecha**: 2026-10-10  
**Decisión**: Roster de 100 modelos (59 activos + 41 cupos) — **Regla Estricta**

## Resumen Ejecutivo

- **Total modelos en catálogo**: 217
- **Activos**: 59
- **Jubilados**: 158
- **Cupos reservados**: 41

### Desglose de Jubilados

**Orden de precedencia** (un solo motivo por modelo):

1. **Retired**: 16 (deprecados por proveedor)
2. **Provider Variant**: 54 (miden serving, no calidad)
3. **Sin Runs**: 26 (nunca medidos, 0 runs)
4. **Dominados**: 62 (**TODOS** — regla estricta)

**Verificación**: 16 + 54 + 26 + 62 = **158 jubilados** ✓  
**Total**: 59 activos + 158 jubilados = **217** ✓

### Dominados

- **Total detectados**: 62
- **Jubilados**: 62 (TODOS)
- **Quedan activos**: 0

**Regla estricta vigente**: Todos los dominados se jubilan sin excepciones. Un modelo está dominado si otro de su familia tiene Q ≥ y costo ≤.

> **Nota**: Se evaluó conservar 31 dominados menos claros como referencia (opción flexible: 90 activos + 10 cupos), pero se descartó por simplicidad y menor costo.

## Definición de Familia

**Familia** = mismo proveedor + misma línea base del modelo, sin importar la generación.

**Ejemplos**:
- Qwen 3.5, 3.6, 3.7, 3.8 → familia "Qwen"
- GPT-5.5, GPT-5.6 Luna → familia "GPT"
- Claude Opus 4.7, 4.8 → familia "ClaudeOpus"

Ver `METODOLOGIA.md` para definición completa.

## Proyección de Costos

### Criterio de Medición Mensual

**Solo se miden**:
1. **Modelos nuevos** (ocupan los 41 cupos)
2. **Activos que cambien** (nueva versión, cambio silencioso, bug runner, suite nueva)

**NO se vuelven a medir** los activos que no cambien.

### Costo Mensual Estimado

**~$96/mes** (estimado)

**Supuestos marcados**:
- ~**10 lanzamientos nuevos**/mes (de 41 cupos disponibles)
- ~**6 activos cambian**/mes (nueva versión o cambio del proveedor)

**Costos base** (medidos abr-sep 2026):
- **Examen completo** (modelo nuevo): ~$8.56 promedio por modelo (rango: $0.08 a ~$28)
- **Re-medición parcial** (activo que cambia): $1.67/modelo ($119/mes ÷ 71 modelos)

**Cálculo**:
- Modelos nuevos: 10 × $8.56 = **$85.60**
- Activos que cambian: 6 × $1.67 = **$10.02**
- **Total**: $85.60 + $10.02 ≈ **$96/mes**

vs $505/mes si se midieran todos los 59 completos cada mes.

### Examen Completo de Todos los Activos

**$505.04** (si se re-midieran todos los 59 completos)

- Costo por examen completo: $8.56 (22 suites)
- Cálculo: 59 × $8.56 = $505.04

**Escenario de uso**: Re-medición completa tras cambio metodológico mayor (nueva suite global, cambio de juez, etc.)

## Criterios de Jubilación (Orden de Prioridad)

1. **Retired** — Proveedor deprecó el modelo
2. **Provider variant** — Mide serving, no calidad
3. **Sin runs** — Nunca medido (0 runs)
4. **Dominado** — Otro de su familia tiene Q ≥ y costo ≤ (regla estricta: TODOS jubilados)

## Comando para Regenerar

```bash
python3 benchmarks/analizar_dominancia.py
python3 benchmarks/analizar_jubilacion_final.py  # Default: opción A
python3 benchmarks/generar_doc_jubilacion.py
```

O explícitamente:
```bash
python3 benchmarks/analizar_jubilacion_final.py --opcion A
python3 benchmarks/generar_doc_jubilacion.py --opcion A
```

## Listado Completo de Modelos

Ver archivos JSON generados:
- `docs/jubilacion-2026-10.json` — Datos estructurados completos
- `benchmarks/dominancia_resultado.json` — Análisis de dominancia con scores

**Incluye**:
- 59 modelos activos (ordenados por quality)
- 158 modelos jubilados (por categoría)
- Para cada dominado jubilado: modelo que lo domina, quality y costo de ambos

---

**Refs**: Decisión tomada 10-oct-2026 · [DECISIONES.md](DECISIONES.md) · [METODOLOGIA.md](METODOLOGIA.md)
