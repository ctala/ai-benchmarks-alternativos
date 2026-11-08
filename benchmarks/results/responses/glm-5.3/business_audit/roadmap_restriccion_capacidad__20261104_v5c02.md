# GLM 5.3 — business_audit/roadmap_restriccion_capacidad

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.79 | quality: 8.0
- latency_total: 103.752s | tokens_per_second: 72.0
- input_tokens: 263 | output_tokens: 7471

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

## Primero, la cuenta (porque decide sola)

Tu capacidad real de construcción: 4h/día × 5 días × 8 semanas = **160 horas el trimestre**.

Si tus estimaciones son en semanas a tiempo completo (~40h cada una):

| Iniciativa | Horas | % de tu trimestre | Veredicto |
|---|---|---|---|
| B – Arreglar alta | ~40h | 25% | **Sí — primera** |
| D – 10 videos | ~80h | 50% | **Sí — segunda** |
| C – Panel métricas | ~120h + depende de A | 75% | Fuera; versión mínima si hay demanda real |
| A – Rewrite | ~480h+ | 300% | **Fuera — no cabe ni empezando** |

B + D = 120h. Con eso el trimestre está lleno al 75%, que es exactamente donde debe estar (nunca planifiques al 100%: tu soporte "no delegable" siempre encuentra forma de comerse más). A ni solo ni acompañado. La pregunta no es si recortar, sino si eliges tú los recortes o los elige el calendario por ti.

## El trimestre

- **Semanas 1–2 — B (alta):** Antes de tocar código, instrumenta y mira *por qué* se caen en el paso 2: replays, escribe a 5 que abandonaron. Arregla la causa #1 y quizá la #2. Publica y mide antes/después.
- **Semana 3 — medir B + preparar D:** Toma el baseline real de conversión, escribe los 10 guiones. Los aprendizajes del paso 2 te van a dar los temas de los videos.
- **Semanas 4–7 — D:** Graba en tandas de 3–4 por sesión (el coste de montaje es por tanda, no por video) y publica con cadencia de 1–2/semana. Así el contenido cae sobre un funnel que ya no pierde al 60%.
- **Semana 8 — cierre:** Métricas del trimestre y un documento de 1 página sobre A para el próximo: sí/no/cómo/condiciones.

## Las decisiones que no son aritmética

**Sobre A, tres cosas.** Uno: son 480h contra 160h; no es opinión, es matemática. Dos: su "impacto alto" es una hipótesis sobre velocidad futura, no un impacto medible hoy — y con capacidad escasa, el impacto presente y medible gana siempre. Tres: lo peor que puedes hacer es empezarlo "solo un poco". Un rewrite a medias son dos codebases que mantener, y tu ventana de soporte de 2h/día se dispara. Ponle un disparador para reconsiderarlo: "cuando delegue soporte o contrate, y tenga un número que diga cuánto me cuesta el stack actual". Y cuando toque, evalúa migración incremental, no rewrite en bloque.

**Sobre C.** Tal cual está, depende de algo que no cabe. Si clientes reales lo piden, descópala: un email semanal automatizado con las 3 métricas clave son ~20–30h, cabe en tu margen y entrega la mayor parte del valor.

**El bonus de B.** La gente atascada en el alta genera tickets. B probablemente te devuelva minutos de tus 2h/día de soporte — eso es capacidad, no solo conversión. Lleva un log de tickets una semana para confirmarlo.

## Dos advertencias

1. **Unidades:** si tus "semanas" ya eran a tu ritmo real (~20h), la aritmética cambia (B=20h, D=40h, C=60h) y sí cabría una C-v0 completa en la segunda mitad. Haz la cuenta en horas antes de comprometer nada.
2. **Mide el baseline de conversión esta semana**, antes de tocar el alta. Sin "antes" no hay "después".

## Cómo sabemos que fue un buen trimestre

Conversión del paso 2 subida de forma medible + 10 videos publicados con señal de entrada. Eso es un gran trimestre para un equipo de una persona: cerraste el agujero del embudo y encendiste distribución. Un rewrite a medias no habría entregado ninguna de las dos cosas.