# Jubilación de Modelos AI - Octubre 2026

**Fecha**: 2026-10-10

Este documento presenta **dos opciones** para establecer un roster activo de modelos. La decisión final la tomará Cristian.

## Comparación de Opciones

| Aspecto | Opción A (Regla Estricta) | Opción B (Regla Flexible) |
|---------|---------------------------|---------------------------|
| **Activos** | 59 | 90 |
| **Cupos** | 41 | 10 |
| **Roster Total** | 100 | 100 |
| **Jubilados** | 158 (16+54+26+**62**) | 127 (16+54+26+**31**) |
| **Dominados jubilados** | **TODOS** (62) | Solo los 31 más claros |
| **Dominados activos** | 0 | 31 (menos dominados, conservados como referencia) |
| **Costo mensual** | **$98.53/mes** | **$150.30/mes** |
| **Examen completo** | $505.04 | $770.40 |

### Base de Cálculo de Costos

- **Costo por modelo/mes**: $1.67 (medido abril-septiembre 2026: $119/mes ÷ 71 modelos/mes)
- **Costo examen completo**: $8.56 (22 suites)

### Opción A - Regla Estricta

**Filosofía**: Jubilar TODOS los dominados (62). Solo quedan modelos no dominados.

**Pros**:
- Roster más limpio: solo modelos Pareto-óptimos dentro de sus familias
- Menor costo mensual ($98.53/mes)
- 41 cupos libres para lanzamientos nuevos

**Contras**:
- Familias grandes (Qwen, GPT, Claude) pierden diversidad
- Se pierden referencias históricas útiles (ej: Claude Opus 4.7, DeepSeek V3)
- Solo 59 modelos en el roster base (podría ser poco para comparaciones)

### Opción B - Regla Flexible (Actual)

**Filosofía**: Jubilar solo los 31 dominados más claros. Los 31 menos dominados se conservan como referencia.

**Pros**:
- Preserva diversidad dentro de familias grandes
- Mantiene referencias históricas (Claude Opus 4.7, Gemini 3.8 Flash, DeepSeek V3)
- 90 modelos = muestra más robusta para comparaciones
- Los 31 conservados están documentados como dominados (transparente)

**Contras**:
- Mayor costo mensual ($150.30/mes vs $98.53)
- Solo 10 cupos para lanzamientos (más ajustado)
- Roster incluye modelos técnicamente dominados

## Desglose por Criterio

Ambas opciones aplican los criterios 1-3 igual:

1. **Retired**: 16 (deprecados por proveedor)
2. **Provider Variant**: 54 (miden serving, no calidad)
3. **Sin Runs**: 26 (nunca medidos, 0 runs)

**Diferencia** está en el criterio 4 (dominados):
- **Opción A**: Jubila los 62 dominados detectados
- **Opción B**: Jubila solo los 31 más dominados; conserva 31 como referencia

## Definición de "Familia" y Dominancia

**Familia** = mismo proveedor + misma línea base del modelo, sin importar la generación.

Ejemplos:
- Qwen 3.5, 3.6, 3.7, 3.8 → familia "Qwen"
- GPT-5.5, GPT-5.6 Luna → familia "GPT"
- Claude Opus 4.7, 4.8 → familia "ClaudeOpus"

Un modelo está **dominado** si otro de su familia tiene:
- Calidad ≥ (Q_dominador >= Q_dominado)
- Costo ≤ (costo_dominador <= costo_dominado por examen)

Costo por examen = 300 tokens input + 1500 tokens output.

## Los 31 Dominados que Difieren entre Opciones

En **Opción A**: TODOS jubilados.
En **Opción B**: Estos 31 quedan **activos** como referencia:

| # | Modelo | Dominado por | Δ Quality | Δ Costo |
|---|--------|--------------|-----------|---------|
| 32 | Qwen 3.8 27B | Qwen 3.8 Flash | +0.03 | -$0.0031 |
| 33 | GPT-5.6 Luna Pro | GPT-5.6 Luna | +0.02 | $0.00 |
| 34 | Gemma 4 31B | Gemma 4 12B (Spark) | +0.01 | -$0.0002 |
| 35 | DeepSeek V4 Pro | DeepSeek R1 | 0.00 | +$0.0007 |
| ... | *(ver docs completos para los 31)* | | | |

(Lista completa en `docs/jubilacion-2026-10-opcion-A.md` y `docs/jubilacion-2026-10-opcion-B.md`)

## Comando para Regenerar

### Opción A (Regla Estricta)
```bash
python3 benchmarks/analizar_dominancia.py
python3 benchmarks/analizar_jubilacion_final.py --opcion A
python3 benchmarks/generar_doc_jubilacion.py --opcion A
```

### Opción B (Regla Flexible)
```bash
python3 benchmarks/analizar_dominancia.py
python3 benchmarks/analizar_jubilacion_final.py --opcion B
python3 benchmarks/generar_doc_jubilacion.py --opcion B
```

## Documentos Generados

- `docs/jubilacion-2026-10-opcion-A.md` / `.json` - Regla estricta (59 activos)
- `docs/jubilacion-2026-10-opcion-B.md` / `.json` - Regla flexible (90 activos)
- `docs/jubilacion-2026-10-final.json` - Symlink a la opción B (backward compat)

## Recomendación para la Decisión

Ambas opciones son válidas. La decisión depende de:

1. **Presupuesto**: ¿$50/mes de diferencia es significativo?
2. **Diversidad**: ¿Vale la pena conservar modelos dominados como referencias?
3. **Cupos**: ¿Se esperan >10 lanzamientos/mes que requieran más cupos libres?

Ver análisis completo y listados de todos los 217 modelos en los documentos específicos de cada opción.
