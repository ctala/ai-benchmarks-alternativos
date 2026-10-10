<!-- doc: snapshot -->
---
title: "Datasheet octubre 2026 — v4.16: GPT-6 Luna y el patrón que se repite: la versión Pro cuesta 3× por la misma nota"
mes: "2026-10"
fecha_snapshot: "2026-10-01"
version_benchmark: "v4.16.0"
audiencia: "Quien tiene que decidir hoy qué modelo pone en producción, con un presupuesto real"
---

# 📊 Datasheet octubre 2026

> 📍 **Qué es y qué no.** Esto no reemplaza a HumanEval, MMLU ni SWE-bench. Los
> complementa con lo que esos no miden y a un emprendedor sí le importa: **español que no
> suene traducido, precio del proveedor real, y tareas de negocio ejecutadas de verdad
> dentro de un agente.** Snapshot anterior: [DATASHEET_2026-09.md](DATASHEET_2026-09.md).

## TL;DR

**El lote de octubre trae GPT-6 Luna, MiMo V2.6 Flash, Ling 3.0 Flash VL y el primer modelo con compresión ternaria medido contra su original.**

- **GPT-6 Luna y Luna Pro sacan 8.75** — pero Luna Pro cuesta **$2.83** contra **$0.93** de Luna regular. Tres veces el gasto por cero diferencia medible.
- **MiMo V2.6 Flash** (Xiaomi, open source, MIT): **8.66 de calidad por $1.52** — el mejor open source del lote y el mejor en calidad/costo ($1.52 examen vs $2.83-$0.93 de los Luna).
- **Ling 3.0 Flash VL**: el más barato del lote con vídeo nativo, **$0.08 el examen**, pero **7.63 de calidad** — cuatro posiciones orquestando y cinco en tool calling lo ponen entre los peores del catálogo en agentes.
- **Bonsai 2 27B** y **Qwen 3.8 Omni Flash** quedaron a medias (103 y 114 de 213 runs): son modelos thinking lentos y sus proveedores tardaron 157-165 s/run. **No se publican medias de exámenes incompletos** — es el error que el repo ya pagó.

## El hallazgo del mes: cuando "Pro" solo significa "caro"

**GPT-6 Luna y GPT-6 Luna Pro** son el mismo modelo base, servido con `reasoning.mode: pro`. OpenAI los declara así: Luna Pro razona más profundo. La medición dice otra cosa:

| | Calidad | Costo examen | Costo/run | Diferencia |
|---|---:|---:|---:|---|
| **GPT-6 Luna** | 8.75 | $0.93 | $0.0044 | — |
| **GPT-6 Luna Pro** | 8.75 | **$2.83** | **$0.0133** | +$1.90 (+204%) por +0.00 en nota |

**Tres veces el gasto, nota indistinguible.** Y no es un caso aislado: el mes pasado GLM 5.3 y GLM 5.3 Flash tenían **0.01 de diferencia por 18× el precio**. El patrón se repite.

No decimos que Luna Pro sea inútil — decimos que **en este examen no justifica su precio**. Si pagas 3× más, deberías poder medirlo.

## Comparación con la generación anterior

GPT-6 Luna **NO supera** a su predecesor GPT-5.6 Luna:

| | Calidad | Costo examen |
|---|---:|---:|
| GPT-5.6 Luna (generación anterior) | 8.93 | $1.86 |
| **GPT-6 Luna** | **8.75** | **$0.93** |
| Diferencia | **−0.18** | −50% |

Cuesta la mitad pero mide peor. Puede ser una decisión de producto (velocidad, capacidades multimodales, algo que este examen no captura), pero **no es un upgrade en calidad de texto**.

## Modelos nuevos medidos

| Modelo | Precio $/M in-out | Runs | Estado |
|---|---|---|---|
| **GPT-6 Luna** | $1.00 / $5.00 | 213 | ✅ Completo, 8.75 |
| **GPT-6 Luna Pro** | $1.00 / $5.00 | 213 | ✅ Completo, 8.75 (3× el gasto real) |
| **MiMo V2.6 Flash** | $0.14 / $0.28 | 213 | ✅ Completo, 8.66 (mejor open source) |
| **Ling 3.0 Flash VL** | $0.021 / $0.062 | 199 | ✅ Completo¹, 7.63 |
| Qwen 3.8 Omni Flash | $0.15 / $0.47 | 114/213 | ⏳ Parcial, no publicable |
| Bonsai 2 27B | $0.075 / $0.50 | 103/213 | ⏳ Parcial, no publicable |

## Lo que falta para cerrar el lote

**No se publican promedios de exámenes a medias** — es el error que costó un sesgo de supervivencia de 8 centésimas en Qwen 3.8 Flash (los runs que sobrevivieron le inflaron la nota). Por eso:

### Mediciones pendientes
- **Qwen 3.8 Omni Flash**: 99 runs de 213 (~$0.62)
- **Bonsai 2 27B**: 110 runs de 213 (~$0.37)
- **Tareas agénticas Harbor**: 6 modelos (~$3-8)
- **Total estimado: $4-9 USD**

### Por qué quedaron a medias
Los dos razonan mucho y sus proveedores son lentos: **157-165 segundos por run**, ~10 horas de reloj cada uno. El lote se pausó para no generar costos sin autorización explícita.

### El caso Bonsai 2: comprimir a ternario ¿cuánto cuesta?
**Bonsai 2 27B** es Qwen 3.8 27B con **compresión ternaria** (1.58 bits/peso). El benchmark ya tiene medido el original (#5, calidad 8.50). Completar Bonsai 2 responde algo que nadie publica: **cuánta calidad pierde un modelo al comprimirlo**.

## Notas

¹ **Ling 3.0 Flash VL con 199/213 runs (93%)** cuenta como completo según `RUNBOOK-MEDICION.md:133-140`: le faltan 14 tests de `niah_es` (contexto largo), que es una suite **omitible sin perder el ranking** — se reporta aparte y no contamina el score. Tiene las 35 suites completas excepto `niah_es` parcial (15/29).

## Caveats honestos

- **Este datasheet cubre 4 modelos completos + 2 parciales.** Los parciales NO entran al ranking hasta completar el examen.
- **El juez es Phi-4** (`phi4-or` vía OpenRouter, el juez canónico desde sep-2026), un modelo de Microsoft de 14B con licencia MIT.
- **Precio de lista, no negociado.** Quien tenga acuerdo con un proveedor verá otros números.
- **La calidad está apretada en la población global: 1,27 puntos separan al primero del último de los 100 rankeados.** Dos modelos con cuatro puestos de diferencia suelen ser indistinguibles estadísticamente.

## Qué sigue

### Inmediato (para cerrar v4.16.0)
1. Completar Qwen 3.8 Omni y Bonsai 2 con `--resume` (~$1)
2. Harbor tasks de los 6 modelos (~$3-8)
3. Regenerar artefactos + merge

### Próximo lote (v4.17.0, noviembre 2026)
- ⏳ **Claude 5.5 family** (Opus, Sonnet): lanzados pero pendientes de agregar
- Suite multimodal nativa (imagen + vídeo)
- Backfill de modelos con examen parcial

## Recursos

- **Calculadora interactiva**: [benchmarks.cristiantala.com](https://benchmarks.cristiantala.com/)
- **Código fuente**: [github.com/ctala/ai-benchmarks-alternativos](https://github.com/ctala/ai-benchmarks-alternativos)
- **Resultados completos**: `benchmarks/results/` (versionado en git)
- **Respuestas auditables**: `benchmarks/results/responses/<modelo>/<suite>/`

---

**Snapshot generado**: 2026-10-10  
**Versión del benchmark**: v4.16.0  
**Lote**: `lote/2026-09-26-gpt6-y-video`  
**Commit**: pendiente de merge
