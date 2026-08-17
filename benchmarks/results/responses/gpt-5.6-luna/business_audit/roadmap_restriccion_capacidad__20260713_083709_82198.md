# GPT-5.6 Luna — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 5.91 | quality: 6.0
- latency_total: 9.307s | tokens_per_second: 130.4
- input_tokens: 241 | output_tokens: 1214

## Respuesta completa

Con tu capacidad real, no puedes completar A ni C este trimestre:

- Capacidad disponible: **4 h/día × 5 días × 8 semanas ≈ 160 h**
- A requiere aproximadamente **3 meses a tiempo completo**, es decir, probablemente **400–500 h**. A tu ritmo ocuparía unos **5–6 meses**.
- C depende de A, así que tampoco cabe.
- B + D suman aproximadamente **3 semanas de trabajo**, dejando margen para medir, corregir y operar.

## Orden recomendado

### Semanas 1–2: B — Arreglar el alta

No lo trates como “una semana y terminado”. Incluye:

- Instrumentar claramente cada paso del alta.
- Identificar por qué se pierde el 60% en el paso 2.
- Implementar la solución más pequeña posible.
- Medir la conversión durante varios días.
- Hacer una segunda iteración si los datos lo justifican.

**Objetivo:** reducir drásticamente la pérdida del paso 2 y aumentar activaciones. Es el mayor retorno inmediato.

### Semanas 3–4: D — Grabar y publicar los videos

Agrupa el trabajo para evitar cambiar de contexto:

- Preparar guiones y formato reutilizable.
- Grabar varios videos en una misma sesión.
- Editar con una plantilla.
- Programar/publicar los 10.
- Medir si generan tráfico, registros o activación.

No invertiría dos semanas en producción sofisticada. El objetivo es sacar contenido útil, no crear una infraestructura audiovisual.

### Semanas 5–8: Mejorar lo que ya funciona

No empezaría la reescritura completa. Usaría estas semanas para:

1. **Iterar sobre el alta** con datos reales.
2. Arreglar los siguientes puntos de fricción del onboarding.
3. Hablar con usuarios que abandonan o no activan.
4. Mejorar medición y alertas internas.
5. Preparar la decisión técnica sobre A:
   - qué partes causan realmente la lentitud;
   - qué módulo tiene más sentido migrar primero;
   - qué riesgos existen;
   - si una migración incremental puede evitar una reescritura total.

Como máximo, dedicaría **1 semana** a un spike técnico muy acotado de A, con un entregable concreto. Por ejemplo: migrar un módulo pequeño o demostrar que una parte crítica funciona en el nuevo framework. No empezaría una reescritura abierta.

## Resumen

| Prioridad | Iniciativa | Cuándo |
|---|---|---|
| 1 | B: arreglar alta | Semanas 1–2 |
| 2 | D: videos | Semanas 3–4 |
| 3 | Iterar onboarding, medir y preparar A | Semanas 5–8 |
| Fuera del trimestre | A: reescritura completa | No comprometerla ahora |
| Fuera del trimestre | C: panel de métricas | Después de resolver su dependencia |

La decisión importante es **no empezar A como proyecto principal**. Es demasiado grande para tu capacidad actual y no entrega valor suficiente dentro de las 8 semanas. Primero arreglaría el embudo que ya existe; después decidiría si la plataforma realmente necesita una reescritura completa o solo mejoras incrementales.