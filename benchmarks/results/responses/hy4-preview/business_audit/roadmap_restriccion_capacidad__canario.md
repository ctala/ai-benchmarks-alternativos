# Tencent Hy4 preview — business_audit/roadmap_restriccion_capacidad

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.81 | quality: 8.0
- latency_total: 221.104s | tokens_per_second: 54.7
- input_tokens: 291 | output_tokens: 12087

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

Asumo que construyes 5 días/semana (4h/día = **20h/semana**). Si construyes 6 o 7 días, tienes más horas, pero **el orden y las conclusiones no cambian**.

## 1. Tu capacidad real (no la ideal)

- 8 semanas reales × 20h = **160h totales**.
- 160h / 40h = **4 semanas FT (a tiempo completo) de capacidad real** en todo el trimestre.

Esa es tu única moneda. Traduzco tus iniciativas (asumiendo que B, C y D están en la misma moneda que A: **semanas FT de 40h**):

| Iniciativa | Esfuerzo (semanas FT) | Esfuerzo real (a 20h/sem) | ¿Cabe en el trimestre? |
|---|---:|---:|---|
| **A** Reescribir plataforma | 12 (3 meses) | **24 semanas reales** | ❌ No (es 3x tu trimestre entero) |
| **B** Arreglar alta (pierde 60%) | 1 | **2 semanas reales** | ✅ Sí |
| **C** Panel de métricas | 3 | 6 semanas reales | ❌ No (depende de A; A+C = 30 semanas reales) |
| **D** 10 videos | 2 | **4 semanas reales** | ✅ Sí |

**B + D = 3 semanas FT.** Te sobra **1 semana FT (2 semanas reales)** de colchón.

---

## 2. Orden del trimestre

### 🥇 1. B — Arreglar el flujo de alta (semanas 1-2)
Es lo único que puede mover la aguja **dentro** de este trimestre.

- Perder al 60% en el paso 2 significa que hoy solo pasa el 40%. Arreglar eso es equivalente a **multiplicar tu adquisición actual por ~2.5x** sin gastar un euro en marketing.
- Impacto alto, esfuerzo más bajo, sin dependencias.
- **Hazlo antes que D:** no tiene sentido grabar videos para atraer tráfico si el 60% se cae en el paso 2. Primero arreglas el cubo, luego echas agua.

### 🥈 2. D — Grabar los 10 videos (semanas 3-6)
Es la única otra iniciativa ejecutable.

- Impacto medio, pero el contenido **tarda en traccionar**: no esperes que los videos muevan métricas antes de cerrar el trimestre. Son inversión para el próximo.
- Ocupa 4 semanas reales (2 FT). Entra justo después de B, cuando el alta ya convierte.

### 🚫 3. A — Reescribir la plataforma: NO entra
Es el canto de sirena clásico del fundador solo.

- “3 meses a tiempo completo” a tu ritmo real son **~6 meses**. Tienes 2 meses.
- Si empiezas A, el día del cierre del trimestre tendrás: plataforma a medio reescribir, C bloqueado, el 60% de fuga sin arreglar y ningún video publicado.
- **No empieces una reescritura que no puedes terminar.** Posterga A. Si el siguiente trimestre quieres atacarla, que sea por módulos o cuando tengas 3 meses full-time/libres de soporte.

### 🚫 4. C — Panel de métricas: BLOQUEADO, fuera del trimestre
Depende de A. Como A no se hace, C no se planifica.

- Si intentas hacer C sin A, o haces un parche que tirarás a la basura cuando reescribas, o generas deuda técnica.
- No la pongas en el roadmap de estas 8 semanas.

---

## 3. Calendario real (8 semanas)

| Semanas | Qué haces | Horas |
|---|---|---|
| **1-2** | **B:** arreglar paso 2 del alta. Instrumenta el embudo para medir el drop-off. Ship a producción. | 40h |
| **3-6** | **D:** grabar y publicar los 10 videos (batea la grabación, no lo hagas en plan diario). | 80h |
| **7-8** | **Buffer / consolidar.** | 40h |

### Qué hacer con el buffer (semanas 7-8)
**No lo uses para empezar A.** Úsalo para:

1. **Medir el impacto real de B.** Si el drop-off no bajó lo suficiente, itera B. Eso vale más que cualquier video nuevo.
2. **Medir el tráfico de D** y preparar el siguiente lote de contenidos.
3. **Documentar tu soporte/operación** (esas 2h/día que no puedes delegar *todavía*). Si en estas 2 semanas dejas procesos escritos para delegar eso el próximo trimestre, liberarás 10h/semana reales. Eso aumenta tu capacidad futura mucho más que reescribir el framework.

---

## Resumen en una línea
**Semanas 1-2: arregla el alta (B). Semanas 3-6: graba los videos (D). Semanas 7-8: mide, itera y prepara delegación. A y C quedan fuera del trimestre.**