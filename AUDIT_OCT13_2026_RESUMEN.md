# Auditoría 13-oct-2026 — Resumen de hallazgos y correcciones

## Hallazgos principales

### 1. ✅ RESUELTO: Fallo de CI regenerate-auto-artifacts.yml

**Causa raíz**: Conflicto de versiones después de los PRs #26 y #27.

- CHANGELOG.md declaraba **v4.17.0** (correcto)
- Pero 6 superficies seguían en **v4.15.0**: README.md, scoring_reference.json, docs/index.html (3 lugares), docs/data/models.json

El check_version.py fallaba por este desfase, impidiendo que el Action completara.

**Corrección**:
- Actualizar las 7 superficies a v4.17.0
- Crear tag v4.17.0 con `check_version.py --tag`
- El Action ahora pasa el step "Verificar que el repo declara una sola version de si mismo"

### 2. ✅ RESUELTO: Contradicciones en DECISIONES.md sobre roster

**Problema**: DECISIONES.md tenía DOS entradas contradictorias sobre el roster de 100 modelos:

- Línea 28: "59 activos + 41 cupos (regla estricta)" — **INCORRECTO**
- Línea 54: "90 modelos + 10 cupos" — **OBSOLETO**

**Números correctos** (según docs/jubilacion-2026-10.json):
- **227 modelos total** (no 217 como decía la entrada vieja)
- **62 activos + 38 cupos = 100**
- **165 jubilados**: 69 dominados + 54 provider_variant + 26 sin_runs + 16 retired

**Corrección**:
- Actualizar línea 28 con números correctos
- Eliminar línea 54 duplicada y obsoleta
- Verificado contra jubilacion-2026-10.json

### 3. ✅ IMPLEMENTADO: Sistema de tracking de modelos jubilados

**Problema**: La jubilación de 62 modelos dominados existía solo en docs (DECISIONES.md, docs/jubilacion-2026-10.md) pero no en código. Los generadores no podían filtrarlos automáticamente.

**Solución**:
- Crear `benchmarks/jubilacion.py` con constante `JUBILADOS` (set de 165 keys)
- Crear `benchmarks/add_jubilado_status.py` para regenerar lista desde JSON
- Los generadores ahora pueden importar y filtrar: `key not in JUBILADOS`

**Categorías de jubilados**:
1. **Dominados (69)**: otro modelo de la misma familia es estrictamente mejor
2. **Provider variant (54)**: miden infraestructura/serving, no calidad del modelo
3. **Sin runs (26)**: nunca medidos (0 runs)
4. **Retired (16)**: deprecados por el proveedor

## Pendientes identificados (requieren presupuesto/aprobación)

### Mediciones no completadas

#### 1. Suites noticias_* (~US$25)
- **5 suites** removidas del branch: `noticias_relevancia`, `noticias_repetidas`, `noticias_pauta`, `noticias_verificacion`, `noticias_seo_discover`
- **Motivos**:
  - No coinciden con diseño aprobado en `benchmark-pack-noticias.md`
  - Licencia CC BY 4.0 de Ecosistema Startup pendiente de aprobación
  - Test counts y scoring methodology incorrectos
- **Estado**: Reimplementación pospuesta a sesión futura

#### 2. Investigación SSL hang (~US$1.07)
- **Modelos afectados**: Qwen 3.8 Omni Flash, Prism Bonsai 2 27B
- **Problema**: Hang SSL en ~50% de tests
- **Estado**: Investigación no iniciada por prioridad de detener gastos tras exceso presupuestario de Claude 5.5
- **Tiempo estimado**: 45 min

#### 3. Pequeños classifiers vs Haiku 5.5
- **Propósito**: Comparar modelos pequeños contra Claude Haiku 5.5 (nuevo baseline)
- **Estado**: Pendiente de definición de scope

#### 4. Harbor 6 modelos (~US$4)
- **Propósito**: Medición agéntica completa de 6 modelos candidatos
- **Estado**: Pendiente de selección de modelos

#### 5. Nuevos candidatos premium
- **Gemini 4 Argon**: google/gemini-4-argon, **US$2/10 per M tokens**
- **Meta Muse Wonder**: meta/muse-wonder, **US$4/20 per M tokens**

**Cálculo de cap propuesto**:
- Input tokens medido: ~45K por test (promedio en examen completo)
- Output tokens estimado: ~2K por test (conservador)
- Costo por test Argon: (45K × $2 + 2K × $10) / 1M = $0.11
- Costo por test Wonder: (45K × $4 + 2K × $20) / 1M = $0.22
- Examen completo (213 tests):
  - Argon: $23.43
  - Wonder: $46.86
  - **Total cap propuesto: US$70** (ambos modelos con margen)

### Artefactos a regenerar

Estos SE PUEDEN regenerar desde datos existentes (sin costo):

1. ✅ `docs/data/models.json` — versión actualizada
2. ⏳ `DATASHEET_2026-10.md` — incluir Claude 5.5 family + corregir fecha header
3. ⏳ `calculadora/qa_calculadora.mjs` — verificar alignment con models.json v4.17
4. ⏳ `INSIGHTS.md` — regenerar con data-scientist agent
5. ⏳ `TESTS_FALTANTES.md` — regenerar desde JSON con coverage actual

## weekly-content.yml

**Hallazgo**: No ha corrido desde antes del 19-sep.

**Análisis**: Es `workflow_dispatch` (manual trigger only), no cron automático. Esto es **por diseño** para controlar costos de API (~$0.30 USD por run). No es un problema.

**Script de generación**: `scripts/generate_blog_post.py` existe y es funcional.

## Estado del CI

**Antes de esta PR**:
- ❌ regenerate-auto-artifacts.yml fallaba en step "Verificar versión" (run 38169226745)
- ✅ Último OK: 19-sep

**Después de esta PR**:
- ✅ `check_version.py` pasa limpio
- ✅ Tag v4.17.0 creado y pusheado
- Pendiente: Verificar que el Action completa tras este merge

## Archivos modificados

```
modified:   DECISIONES.md                    # Corregir números roster
modified:   README.md                        # v4.17.0
modified:   scoring_reference.json           # v4.17.0
modified:   docs/index.html                  # v4.17.0 (3 lugares)
modified:   docs/data/models.json            # v4.17.0
new file:   benchmarks/jubilacion.py         # Set JUBILADOS (165 modelos)
new file:   benchmarks/add_jubilado_status.py # Generador de lista
```

## GitHub Pages

El sitio `benchmarks.cristiantala.com` servirá la versión actualizada tras merge a main. No requiere acción manual.

**Preview**: El JSON actualizado ya está en esta branch y se puede verificar en:
`https://raw.githubusercontent.com/ctala/ai-benchmarks-alternativos/cursor/audit-oct13-fixes-2eee/docs/data/models.json`

## Próximos pasos

1. **Inmediato**: Merge de esta PR para restaurar el CI
2. **Corto plazo** (no requiere API):
   - Regenerar DATASHEET_2026-10.md
   - Regenerar INSIGHTS.md
   - Regenerar TESTS_FALTANTES.md
3. **Mediano plazo** (requiere presupuesto):
   - Completar Qwen 3.8 Omni / Bonsai 2 (~$1)
   - Medir Argon + Wonder con cap de $70
   - Decidir y ejecutar tareas Harbor (6 modelos, $4)

---

**Elaborado**: 13-oct-2026  
**Agente**: Cloud Agent (Cursor)  
**Refs**: PRs #26, #27 · docs/jubilacion-2026-10.json · CHANGELOG v4.17.0
