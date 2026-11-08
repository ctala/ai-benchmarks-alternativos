# Mercury 3 — business_audit/roadmap_restriccion_capacidad

- model_id: `inception/mercury-3`
- success: True  | final: 8.91 | quality: 10.0
- latency_total: 10.597s | tokens_per_second: 475.3
- input_tokens: 277 | output_tokens: 5037

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

Con tu capacidad real (4h/día de construcción ≈ 20h/semana, 160h en 8 semanas), el orden es claro:

## Orden del trimestre

### 1. B — Arreglar el flujo de alta  
**Semana 1**

Es la única iniciativa de impacto alto y esfuerzo bajo. Además, si pierdes al 60% en el paso 2, cualquier tráfico que generes con los videos se desperdicia. Primero arregla el embudo, luego abre más la llave.

Métrica: % de gente que pasa del paso 2 al paso 3. Mide antes/después.

---

### 2. D — Grabar 10 videos  
**Semanas 2-3**

Hazlo justo después de B, no antes. Los videos pueden atraer gente, pero si el alta sigue roto, estarás quemando presupuesto de atención.

Grálalos en lote, publícalos a lo largo de las semanas siguientes y no edites de más.

---

### 3. A y C quedan fuera del trimestre

- **A**: 3 meses a tiempo completo ≈ 480h. Con 4h/día necesitarías ~24 semanas, no 8. Empezar una reescritura que no vas a terminar no entrega valor y deja la plataforma en un estado peor.
- **C**: depende de que A esté terminado. Como A no va a estar terminado, C no es factible este trimestre.

---

### 4. Semanas 4-8: no metas A ni C

Te quedan unas 100h. Úsalas para:

- Reducir las 2h diarias de soporte/operación: automatiza, crea FAQ, plantillas, self-service. Eso te libera capacidad futura.
- Si tus clientes necesitan métricas, haz una versión provisional: informe semanal manual o un dashboard externo (Looker Studio, Metabase) sobre la base de datos actual. No es C, pero cubre la necesidad sin esperar a A.
- Si A es inevitable, haz solo un pilotaje técnico pequeño (migrar un módulo, probar el framework) para reducir riesgo, pero no lo comprometas como entrega del trimestre.

---

## Resumen

| Semana | Qué hacer |
|---|---|
| 1 | B: arreglar flujo de alta |
| 2-3 | D: grabar 10 videos |
| 4-8 | Reducir operación, solución provisional de métricas, preparar A sin comprometerla |

**Decisión clave:** B primero, D después, A pospuesta, C fuera por dependencia.