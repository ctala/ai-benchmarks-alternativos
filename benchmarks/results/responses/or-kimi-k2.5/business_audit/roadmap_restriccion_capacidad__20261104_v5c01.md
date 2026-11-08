# Kimi K2.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.08 | quality: 10.0
- latency_total: 201.68s | tokens_per_second: 27.2
- input_tokens: 304 | output_tokens: 5476

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

**Tu capacidad real este trimestre: ~160 horas de construcción**  
(8 semanas × 5 días × 4 h/día. Si trabajas 6 días, son ~192 h; el razonamiento no cambia).

Con esa restricción, **A es imposible** y **C es inexistente** este trimestre. No es opinión, es aritmética.

---

### El orden (y lo que no se toca)

#### 1. B — Arreglar el flujo de alta (Semana 1)
**Hazlo el lunes que viene.**  
Pierdes al 60 % en el paso 2. Eso no es un problema de framework; es un balde roto. Cada hora que inviertas en marketing, contenido o reescritura mientras ese agujero exista es dinero quemado.  
- **Esfuerzo:** ~20 h (una semana a tu ritmo).  
- **Impacto:** Inmediato y multiplicador. Si pasas de 40 % a 70 % de supervivencia en ese paso, duplicas tus usuarios activos sin gastar un euro más en adquisición.

#### 2. D — Los 10 videos (Semanas 2-3)
**Solo después de confirmar que B funciona.**  
Si el contenido es para atraer gente nueva, asegúrate de que el funnel ya no esté roto (espera 3-4 días de métricas post-B). Si es para usuarios ya activos (educación, retención), adelante.  
- **Esfuerzo:** ~40 h (dos semanas).  
- **Por qué va aquí:** Es la única iniciativa viable de tu lista que cabe en el tiempo restante y genera valor tangible este cuatrimestre.

#### 3. C — Panel de métricas
**No este trimestre.** Dijiste que depende de A. A no existe en tu calendario de 8 semanas, por tanto C no existe tampoco.  
- Si la dependencia es negociable, haz una **v1 mínima y fea** en las semanas 4-6, sobre tu stack actual. Pero si es estricta, congélalo.

#### 4. A — Reescribir la plataforma
**No lo toques. Ni siquiera lo planifiques.**  
- Esfuerzo estimado: ~3 meses a tiempo completo = ~480 h. Tú tienes 160 h. No cabe.  
- Un rewrite a 4 h/día con 2 h diarias de soporte es una receta para 9 meses de calvario, context-switching constante y cero entregas.  
- La "velocidad futura" es una trampa mental: si no sobrevives al presente (60 % de abandono), no hay futuro.

---

### Tu calendario realista (8 semanas)

| Semana | Focus | Horas (~20h/semana) |
|--------|-------|---------------------|
| 1 | **B**: Fix del paso 2. Medir antes y después. | 20 h |
| 2-3 | **D**: Grabar, editar y programar los 10 videos. | 40 h |
| 4-8 | **Espacio libre** (~100 h). Usarlo para: <br>• Iterar el onboarding (paso 3, 4, etc.) <br>• Deuda técnica quirúrgica (no rewrite) <br>• Ventas directas / demos si B2B <br>• Reducir soporte para ganar horas | 100 h |

---

### La regla de un solo founder

Con 4 h de construcción diarias, tu límite de WIP (trabajo en curso) es **1**. No puedes paralelizar. No puedes "avanzar un poco" en A mientras haces B.  
**Estrategia:** Quick wins que detengan sangrado → Activos que generen retorno → Todo lo demás se pospone.

Si a finales de las 8 semanas B está arreglado y los videos están publicados, habrás tenido un trimestre exitoso. A y C esperan al Q en el que puedas delegar soporte y liberar 6 h/día reales de construcción, o contratar a alguien. Hoy, **construir para sobrevivir > reescribir para soñar**.