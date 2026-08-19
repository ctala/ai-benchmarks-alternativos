# Inkling Small — business_audit/roadmap_restriccion_capacidad

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 68.217s | tokens_per_second: 44.5
- input_tokens: 249 | output_tokens: 3037
- judge_score: 5 | justificación: La respuesta es precisa, altamente relevante, ofrece una profundidad significativa con insights prácticos, está claramente organizada y es extremadamente útil para un emprendedor.

## Respuesta completa

Tu capacidad real es **4h/día × 8 semanas ≈ 160 horas de construcción**. No 480. No 320. 160.

Con eso, el orden no es una preferencia: es matemática.

### Lo que no entra (y por qué)

| Iniciativa | Esfuerzo real (4h/día) | ¿Cabe en 8 semanas? |
|---|---|---|
| **A** Reescribir framework | ~24 semanas (480h) | **No. Ni de lejos.** Es un proyecto de 6 meses. Además, te bloquea C y te deja sin clientes porque el flujo sigue roto. |
| **C** Panel de métricas | ~6 semanas (120h) | **No, porque depende de A.** Si haces C sin A, te duplicas el trabajo luego. |
| **B** Flujo de alta | ~2 semanas (30-40h) | **Sí.** |
| **D** 10 videos | ~4 semanas (60-80h) | **Sí, si va después de B.** |

**Regla de oro para un solo fundador:** No hagas un "rewrite" mientras tu embudo pierde al 60%. Es el lujo de un equipo con ingresos estables y gente que cubra soporte. Tú no tienes ni una ni otra.

---

### El orden del trimestre (semana a semana)

**Semanas 1-2: Solo B. Nada más.**
- Objetivo: parar la hemorragia del paso 2.
- No paralelices con D ni con "un poco de A". Cada día que pasa sin arreglar el flujo, pierdes más clientes de los que ganarías con videos o con una plataforma más rápida.
- Si el paso 2 es técnico, haz el parche mínimo viable. No lo "arquitectures". Que funcione.

**Semanas 3-6: D (videos).**
- Una vez que el flujo de alta funciona, necesitas **tráfico calificado** para alimentarlo.
- Es trabajo de producción (escritura + grabación + edición), no de arquitectura. No depende de A.
- Si te quedan horas, usarlas para medir si B funcionó (¿bajó la pérdida del 60%? ¿Subió la conversión?).

**Semanas 7-8: Medición + reducción de soporte + planificación de A.**
- No intentes terminar A. Usa estas semanas para:
  1. Ver si B realmente movió la aguja.
  2. Automatizar una parte de esas 2h de soporte/operación que te comen (para liberar más horas para el próximo trimestre).
  3. **Planear A para el Q siguiente**, pero solo si los ingresos del flujo arreglado te permiten contratar o delegar algo.

---

### ¿Por qué no C?

Dijiste que depende de A. Si descartas A, descartas C. No hagas un panel de métricas sobre una plataforma que vas a reescribir en 3 meses. Es trabajo de basura.

Si en algún momento quieres un panel básico para clientes, hazlo con una query manual o un dashboard rápido (Notion/Metabase/lo que sea) en **1 día**, no 3 semanas.

---

### Resumen para tu calendario

- **B:** Semanas 1-2 (impacto alto, esfuerzo bajo).
- **D:** Semanas 3-6 (impacto medio, sin dependencias técnicas).
- **A:** **Cero horas este trimestre.** Es un proyecto de Q+1, si es que sobrevives con los ingresos de B.
- **C:** **Cero horas.** Bloqueado por A; si lo necesitas, haz un parche de 1 día, no 3 semanas.

**Tu riesgo real no es la velocidad del framework. Es que sigas perdiendo clientes en el paso 2 mientras intentas ser "técnicamente perfecto".**

Arregla el flujo, graba los videos para llenar el embudo que ahora funciona, y usa el resto del trimestre para no quemarte en soporte. Eso es ser jefe de producto con 4 horas al día.