# GLM-5.1 — business_audit/roadmap_restriccion_capacidad

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.99 | quality: 8.0
- latency_total: 40.203s | tokens_per_second: 43.6
- input_tokens: 263 | output_tokens: 1754

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

# Plan de trimestre — versión realidad

## La matemática primero

- 4 h/día × 5 días × 8 semanas = **160 horas reales de construcción**
- Una "semana" normal (40h) para ti = **2 semanas calendario**
- Iniciativa A tal como está planteada: 3 meses a tiempo completo = ~480h → en tu ritmo real son **~6 meses**, no 8 semanas

**A no entra este trimestre. Punto.** No es una decisión de priorización, es aritmética. Si intentas empezarla, tendrás un rewrite a medio hacer en septiembre, con la plataforma actual congelada y la nueva sin poder salir a producción. Eso mata empresas solo-fundador.

## Orden del trimestre

### Semanas 1–2 → B (flujo de alta)
Es la iniciativa con mejor ratio impacto/esfuerzo que tienes, y además es la única que ataca una fuga de revenue *hoy*. Perder al 60% en el paso 2 significa que cualquier cosa que construyas después —incluido el panel de métricas o los videos— se está multiplicando por 0.4 desde el inicio. Arreglar esto es subir el suelo de todo lo demás.

20–40h bien invertidas aquí. Mide antes/después y ya tienes una victoria narrable de cara a clientes e inversores.

### Semanas 3–4 → D (10 videos)
Una vez estabilizado el funnel, el contenido es el multiplicador de adquisición que no requiere que toques producto. Dos semanas, entregable finito, impacto medio pero acumulativo (los videos siguen trabajando después).

### Semanas 5–8 → Tres opciones, elige una

No vas a meter A ni C. En su lugar, elige según tu cuello real:

1. **Si tu cuello es la operación (los 2h/día)**: dedica estas 4 semanas a automatizar/eliminar las tareas repetitivas de soporte. Cada hora que recuperes son 5h/semana para siempre. Es el ROI más alto que tienes ahora mismo, aunque no lo veas como "producto".
2. **Si tu cuello es retención**: construye una versión *mínima* del panel de métricas (C) **sin depender de A**. El hecho de que C dependa de A es una decisión de diseño tuya, no una ley de la física. Un panel sobre la base actual, aunque sea feo, valida si a tus clientes les importa.
3. **Si tu cuello es deuda técnica que frena todo**: usa las 4 semanas para *planificar* A en serio —no empezarlo—. Breakdown, migración incremental por módulos, decisión de si realmente necesitas un rewrite o si un refactor estrangulado basta. Lleva un plan ejecutable al próximo trimestre.

Mi recomendación: **opción 1**. Es la que más te acerca a recuperar capacidad.

## Lo que NO vas a hacer este trimestre

- **A**: rewrite completo. Imposible en 8 semanas a tu capacidad real. Aplázalo formalmente.
- **C**: tal como está diseñado, porque depende de A. Rediseñado sin esa dependencia, podría entrar en semanas 5–8.

## El error que estás cometiendo al plantearlo

C depende de A. Eso significa que has diseñado tu roadmap de forma que **una iniciativa inviable (A) bloquea una iniciativa factible (C)**. Ese acoplamiento es el verdadero problema, no la priorización. Si C importa, desacóplala. Si A importa, replanéala en trozos que quepan en tu capacidad real, no en la ideal.

## Resumen ejecutivo

| Semana | Iniciativa | Horas estimadas |
|--------|-----------|----------------|
| 1–2 | B — Fix onboarding | ~40h |
| 3–4 | D — 10 videos | ~40h |
| 5–8 | Automatizar soporte (recomendado) o C rediseñado sin dependencia de A | ~80h |
| — | A | Aplazada al próximo trimestre, replanificada en formato incremental |

**Una sola frase para guiar el trimestre**: primero tapa el agujero del cubo, luego llena más agua, y mientras tanto reduce el tiempo que pasas limpiando el suelo. El rewrite es un proyecto de otro trimestre —y probablemente de otro formato—.