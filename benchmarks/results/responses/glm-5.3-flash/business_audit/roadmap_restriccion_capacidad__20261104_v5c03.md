# GLM 5.3 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 5.87 | quality: 6.0
- latency_total: 84.978s | tokens_per_second: 66.5
- input_tokens: 263 | output_tokens: 5651

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

# El trimestre: B → D → iterar. A y C fuera.

## Primero, la matemática real

- Capacidad: 8 semanas × 5 días × 4h = **160h** (planea con ~140h; habrá incendios).
- A son ~3 meses full-time ≈ **480h**. Es 3x tu trimestre completo. A tu ritmo de 4h/día, son ~6 meses. No es decisión de priorización, es aritmética.
- Tus estimaciones de B y D parecen ser a tiempo completo. Convertidas a tu ritmo: **B ≈ 2 semanas, D ≈ 3-4**.

## El orden

**Semanas 1-2: B (alta).**
- Día 1: instrumenta el paso 2 si no tienes datos. No puedes arreglar lo que no mides.
- Días 2-3: mira sesiones grabadas o habla con 3-5 personas que se cayeron ahí. A veces el fix es quitar un campo o reescribir un texto, no una semana de código.
- Resto: fix y ship. Meta del trimestre: caída en el paso 2 de 60% → ≤30%.

**Semanas 3-6: D (videos), en batch.**
- Un día de guiones, luego graba 5 en una sesión, edita en bloque. Nunca 1 video por día.
- Métrica de éxito: no vistas, sino cuántos signups trae.

**Semanas 7-8: iterar + buffer.**
- Itera B con 4 semanas de datos reales (la primera versión nunca es la definitiva).
- Batch 2 de videos solo si D mostró señal.
- **~1 semana sin asignar.** El soporte se desborda justo cuando shippeas algo.

Bonus no obvio de B: los usuarios confundidos son tickets. Arreglar el alta probablemente te devuelve horas de esas 2h/días de soporte.

## Por qué muere C

Depende de A, y A no va a existir este trimestre. Escape hatch: si puedes mandar un email semanal con métricas o armar un sheet en un día, hazlo. Valida si tus clientes lo quieren sin gastar 3 semanas. Si nadie abre el email, mataste el PRD gratis.

## La decisión de A, para el cierre de trimestre

No la dejes como deseo pendiente. En la semana 8 escríbela con datos: **las 3 cosas concretas que no pudiste hacer por el framework actual**.

- Si las tienes: el camino del próximo trimestre es migrar un módulo a la vez (strangler), no reescribir todo de golpe.
- Si no las encuentras: el rewrite era vibe, y acabas de ahorrarte 6 meses.

Mientras tu funnel pierde al 60% de la gente, cada semana de rewrite es agua en un cubo roto. Primero tapa el hoyo, luego compra la cubeta nueva.