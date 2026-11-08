# Nemotron 3 Ultra 550B — business_audit/roadmap_restriccion_capacidad

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 91.535s | tokens_per_second: 13.4
- input_tokens: 266 | output_tokens: 1222

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

**Veredicto rápido: Solo caben B y D. A y C mueren este trimestre.**

---

### Tu capacidad real
- **4 h/día × 5 días × 8 semanas = 160 h** (≈ 4 semanas a tiempo completo).
- **A** necesita ~480 h → **3× tu capacidad total**. No cabe.
- **C** necesita ~120 h **y depende de A** → **imposible**.

---

### Orden de ejecución (8 semanas)

| Semana | Iniciativa | Horas | Qué entregas |
|--------|------------|-------|--------------|
| **1** | **B – Arreglar flujo de alta** | ~40 h | Paso 2 rediseñado, tests A/B listos, métrica de conversión ≥ 40 % (desde 40 % actual). |
| **2–3** | **D – Grabar 10 videos** | ~80 h | 10 videos editados, subidos, con CTAs a la alta nueva. |
| **4–8** | **Buffer / Iterar / Vender** | ~40 h | - Medir impacto real de B (¿sube activación? ¿baja churn?).<br>- Retocar onboarding según datos.<br>- Responder leads que entren por D.<br>- Deuda técnica **pequeña** (no reescritura). |

---

### Por qué este orden
1. **B primero**: Tapas la fuga *antes* de traer más gente con D. 60 % de drop en paso 2 es una hemorragia; cada semana sin arreglarlo pierdes clientes que ya pagaste (o esforzaste) conseguir.
2. **D segundo**: Contenido evergreen que alimenta el top-of-funnel *mientras* duermes. Con la alta arreglada, cada lead nuevo vale más.
3. **A y C al congelador**:  
   - A: Reescribir framework es **riesgo existencial** para un solo founder con 4 h/día. Si insistes, no entregas nada visible en 8 semanas.  
   - C: Sin A no existe. Cuando (y *si*) hagas la migración en otro trimestre, el panel vendrá solo.

---

### Qué decir a stakeholders / clientes
> «Este trimestre cerramos la fuga del onboarding (B) y lanzamos academia en vídeo (D). La reescritura técnica (A) y el panel de métricas (C) se evaluarán en Q+1 con datos de conversión reales.»

---

### Checklist de arranque (hoy, en tu primera hora de build)
1. **Instrumenta** el paso 2 actual (eventos, heatmap, sesión grabada).  
2. **Define** el experimento: variante A (actual) vs B (nuevo flujo) – métrica: % que completan paso 2 → paso 3.  
3. **Boceta** los 10 temas de vídeo (uno por cliente ideal / objeción frecuente).  
4. **Bloquea** en calendario: 4 h/día *sagradas* (mismo horario, modo avión).  

---

**Resultado a 8 semanas:**  
- Onboarding que convierte el doble.  
- 10 assets de vídeo trayendo leads cualificados.  
- Cero meses quemados en reescritura invisible.  
- Espacio mental para decidir en Q+1 si A merece la pena (probablemente no, o solo módulos).