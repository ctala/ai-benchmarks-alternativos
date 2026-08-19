# Qwen 3.7 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 6.24 | quality: 6.0
- latency_total: 33.233s | tokens_per_second: 95.5
- input_tokens: 255 | output_tokens: 3174

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

Con tu capacidad real (**4h/día × 8 semanas ≈ 160h totales**), el orden tiene que ser implacable. Lo ideal no escala cuando el equipo eres tú solo. Aquí va la priorización basada en impacto/hora, dependencias y riesgo de bloqueo:

### 📊 Orden recomendado: **B → D → C (reescopada) → A (pospuesta)**

| Iniciativa | Por qué va ahí | Horas estimadas | Riesgo si se mueve |
|------------|----------------|-----------------|-------------------|
| **B** Arreglar alta | Alto impacto, bajo esfuerzo, cero dependencia. Cierra una fuga crítica y libera conversión para todo lo demás. | ~20h | Si no se hace, C y D pierden contexto (más usuarios llegando a un funnel roto). |
| **D** 10 videos | Medio impacto, no bloquea nada, genera pipeline externo. Se puede ejecutar en bloques sin romper el flujo de desarrollo. | ~40h | Retrasarlo no afecta producto, pero sí mantiene o reduce la visibilidad. |
| **C** Panel métricas | Depende de A, pero A no cabe. Si no lo desacoplas, C muere este trimestre. | ~60h (si se lightea) | Si se espera a A, no habrá entrega visible ni feedback de clientes. |
| **A** Reescribir framework | 3 meses a tiempo completo. Con 4h/día tardarías 12+ semanas solo en esto, dejando 0h para el resto. Además, reescribir mientras se arreglan fugas y se crean features es la receta clásica para contexto roto y deuda nueva. | ~120h+ | Empezarlo ahora bloquea todo el trimestre y consume tu única ventaja: velocidad de decisión. |

---

### 🗓️ Plan de 8 semanas (~160h disponibles)
*(Asume 5 días/productivos. Ajusta según tu ritmo real).*

| Semanas | Enfoque | Entregable claro | Hrs |
|---------|---------|------------------|-----|
| **1-2** | **B** Fix onboarding | Flujo estable, métrica de conversión en paso 2 mejorada ≥15%, deployed | 20h |
| **3-5** | **C** Panel métricas ligero | 3-4 KPIs clave visibles para cliente, sin tocar arquitectura base | 60h |
| **6-7** | **D** Grabación + publicación | 10 videos grabados, editados, publicados, con calendario de distribución | 40h |
| **8** | Buffer + cierre | Revisión de métricas post-B/C, limpieza técnica, planificación Q+1 | 40h |

---

### ⚠️ Reglas no negociables para que funcione
1. **No empieces A** hasta que B tenga datos reales de mejora y C esté en producción. Un rewrite sin validar el funnel actual es gasto puro.
2. **Desacopla C de A.** Si técnicamente dice que depende, reemplázalo por un workaround viable: query directa a BD, export CSV automatizado, o integración con Metabase/Grafana en modo lectura. Tu objetivo este trimestre es **entregar valor**, no cumplir arquitectura ideal.
3. **Define “terminado” antes de abrir el IDE.** Ej: `“C está listo cuando el cliente ve 3 métricas en <2 clicks sin pedir soporte”`. Sin eso, el scope creep te comerá las 160h.
4. **Protege las 4h.** El soporte/op debe estar contenido en esas 2h fijas. Si se desborda, crea plantillas de respuesta, FAQs o limita horarios de atención. No robes tiempo de build para apagar fuegos.

---

¿Quieres que te ayude a **desacoplar C** o a definir el **MVP exacto del panel** sin tocar A? Dime qué stack tienes (DB, frontend, hosting) y te devuelvo un plan técnico de 3 pasos para lanzarlo en 10 días reales.