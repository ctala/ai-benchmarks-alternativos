# Claude Fable 5 (suscripción) — deep_reasoning/fermi_estimation

- model_id: `claude-fable-5`
- success: True  | final: 6.21 | quality: 8.0
- latency_total: 19.216s | tokens_per_second: 68.0
- input_tokens: 2 | output_tokens: 1307

## Respuesta completa

# Estimación Fermi: litros de café diarios en oficinas de Santiago

## Razonamiento paso a paso

**Supuesto 1 — Población del Gran Santiago:** ~7 millones de habitantes.

**Supuesto 2 — Fuerza laboral ocupada:** ~50% de la población → **3.5 millones de trabajadores**.

**Supuesto 3 — Proporción que trabaja en oficinas:** No todos trabajan en oficina (retail, construcción, salud, transporte, educación, terreno). Estimo 30-35% en trabajos de oficina → **~1.1 millones de personas**.

**Supuesto 4 — Presencialidad:** Post-pandemia hay trabajo híbrido. Un día promedio, asisten físicamente ~70% → **~770,000 personas en oficinas un día cualquiera**.

**Supuesto 5 — Proporción que toma café en la oficina:** Chile es históricamente más tomador de té que de café, aunque el café ha crecido fuerte. Estimo que **65%** consume al menos un café en la oficina → **~500,000 consumidores diarios**.

**Supuesto 6 — Tazas por persona por día:** Entre 1 y 3 tazas en horario laboral. Promedio: **2 tazas**.

**Supuesto 7 — Volumen por taza:** Taza estándar de oficina (máquina, instantáneo o de cafetería): **~200 ml**.

## Cálculo central

```
500,000 personas × 2 tazas × 0.2 L = 200,000 litros/día
```

**Mejor estimación: ~200,000 litros de café al día** (200 m³ — aproximadamente el volumen de una piscina semiolímpica grande).

## Rango mínimo-máximo

| Escenario | Trabajadores oficina presentes | % cafeteros | Tazas | ml/taza | Resultado |
|---|---|---|---|---|---|
| **Mínimo** | 600,000 | 50% | 1.5 | 150 ml | **~70,000 L/día** |
| **Central** | 770,000 | 65% | 2 | 200 ml | **~200,000 L/día** |
| **Máximo** | 900,000 | 80% | 3 | 250 ml | **~540,000 L/día** |

**Rango: 70,000 — 540,000 litros/día**, con mejor estimación en **~200,000 litros**.

## Supuesto con mayor impacto

El de mayor sensibilidad es la combinación **tazas por persona × % de cafeteros** (Supuestos 5 y 6), porque:

1. **Es multiplicativo y tiene el rango relativo más amplio:** el % de cafeteros varía de 50% a 80% (factor 1.6x) y las tazas de 1.5 a 3 (factor 2x). Combinados explican un factor ~3.2x del rango total.
2. **Es el más incierto culturalmente:** Chile tiene tradición de té e instantáneo (Nescafé domina), pero el consumo de café de especialidad creció mucho en la última década. No hay un dato intuitivo y confiable, a diferencia de la población (bien conocida) o el tamaño de la taza (acotado físicamente entre 150-250 ml).
3. Los demás supuestos (población, % oficinistas, presencialidad) tienen anclas más sólidas en datos censales y laborales.

Si tuviera que mejorar la estimación con un solo dato real, buscaría **el consumo per cápita de café en Chile** (está en torno a 1.2-2 kg/persona/año, bajo vs. promedio mundial) para calibrar los supuestos 5 y 6 hacia abajo — lo que sugiere que la realidad probablemente está más cerca de **150,000 litros/día** que del escenario máximo.