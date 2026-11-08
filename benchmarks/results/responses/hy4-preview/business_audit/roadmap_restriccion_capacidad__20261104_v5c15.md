# Tencent Hy4 preview — business_audit/roadmap_restriccion_capacidad

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.17 | quality: 10.0
- latency_total: 254.085s | tokens_per_second: 58.0
- input_tokens: 291 | output_tokens: 14745

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

Vamos a hablar en la única moneda que importa: **tu capacidad real**, no la ideal.

## 1. Tu capacidad real del trimestre

- Trabajo enfocado total: 6 h/día.
- Soporte/operación no delegable: 2 h/día.
- **Capacidad real de construcción: 4 h/día.**
- Si trabajas 5 días/semana: **20 h/semana**.
- Quedan 8 semanas → **160 horas totales**.

Eso equivale a **4 semanas-persona** (semanas de 40 h). Esa es toda tu moneda del trimestre.

> Si trabajas 6 días, tienes 192 h (4,8 semanas-persona); si 7 días, 224 h (5,6). El orden que te doy abajo no cambia.

---

## 2. Traducción de tus iniciativas a capacidad real

Asumo que cuando dices “1 semana” de esfuerzo es **1 semana-persona de 40 h** (lo estándar). Como tú solo puedes construir 20 h/semana, **1 semana-persona = 2 semanas de tu calendario**.

| Iniciativa | Impacto | Esfuerzo | En tu calendario (20 h/sem) | ¿Cabe este trimestre? | Decisión |
|---|---:|---:|---:|---|---|
| **A** Reescribir plataforma | Alto | ~12 semanas-persona (3 meses FT) | **24 semanas (6 meses)** | No (300% del trimestre) | **No empezar** |
| **B** Arreglar alta (pierde 60%) | Alto | 1 semana-persona | 2 semanas | Sí (25%) | **Hacer 1º** |
| **C** Panel de métricas | Medio | 3 semanas-persona | 6 semanas | No (bloqueada por A) | **Fuera este trimestre** |
| **D** 10 videos de contenido | Medio | 2 semanas-persona | 4 semanas | Sí (50%) | **Hacer 2º** |

**Nota:** si tus “semanas” ya eran semanas tuyas de 20 h, divide los tiempos de B/C/D entre 2 (B=1 sem, D=2 sem, C=3 sem). A sigue siendo ~24 semanas. El orden no cambia.

---

## 3. Decisiones, sin romanticismo

### ✅ B — Arreglar el flujo de alta
Es lo primero. Pierdes al 60% de la gente en el paso 2. Eso no es un “bug”, es una fuga en el cubo.  
Impacto alto, esfuerzo pequeño. Es la cosa más obvia y rentable que puedes hacer.

### ✅ D — 10 videos de contenido
Va segundo, **no primero**.  
Grabar videos para atraer tráfico a un alta que pierde al 60% es echar agua en un cubo agujereado. Primero arreglas B, luego llenas el cubo con D.

### ❌ C — Panel de métricas
Está **bloqueada por A**. Y A no va a pasar este trimestre.  
Aunque no dependiera de A, cuesta 3 semanas-persona (6 semanas tuyas en el escenario estándar) y solo te quedarían 1–2 semanas libres. No entra.

Si descubres que **C no depende realmente de A** y puedes hacer un panel provisional sobre la plataforma actual, entonces en el escenario optimista (con 5 semanas libres) podría entrar después de D. Pero tal como está escrito: fuera.

### ❌ A — Reescribir la plataforma
Este es el espejismo clásico del fundador solo.

- A cuesta **12 semanas-persona**.
- Tu trimestre tiene **4**.
- Aunque trabajes 7 días/semana, sigues necesitando ~17 semanas.

Si empiezas A, terminas el trimestre con **un 25–30% de una reescritura**, cero features nuevas, la plataforma vieja viva y una nueva a medias. Eso es peor que no hacer nada.

Además: **A no es un problema de tiempo, es un problema de restricción.** Mientras sigas gastando 2 h/día en soporte, A no cabe ni en dos trimestres. La única forma de que A sea viable en el futuro es primero recuperar esas 2 h.

---

## 4. Orden del trimestre (calendario)

Asumiendo 5 días/semana y estimaciones estándar (40 h/semana-persona):

### Semanas 1–2: **B**
- Arregla el paso 2.
- Instrumenta el funnel si aún no lo tienes.
- Define criterio de éxito: ejemplo, “paso 2 pasa del 40% al 70% de conversión”.
- No empieces nada más en paralelo. Context switching te costaría más que las 2 semanas.

### Semanas 3–6: **D**
- Guioniza, graba y edita los 10 videos.
- Publícalos de forma escalonada.
- Ahora sí tiene sentido atraer tráfico: el alta ya convierte.

### Semanas 7–8: holgura (no la gastes en A)
Te quedan ~1 semana-persona (2 semanas calendario, o 5 semanas si tus estimaciones eran de 20 h). Úsalas en esto, en este orden de prioridad:

1. **Medir B.** ¿Funcionó? ¿Cuánto subió la conversión? Sin medir, no sabes si ganaste.
2. **Iterar el siguiente cuello de botella (B2).** Detrás del paso 2 casi siempre hay otra fuga. Arreglar eso suele tener más impacto que un panel de métricas.
3. **Reducir las 2 h de soporte.** Documentación, FAQs, plantillas, automatizaciones. Esto parece “no construir producto”, pero sube tu capacidad de 4 h a 5–6 h/día. Es lo que hará posible A en el futuro.
4. **Spike de A, máximo 3–5 días.** Si quieres tocar el tema: prueba de concepto, comparar frameworks, plan de migración por fases. **No empieces la reescritura.** Con 1–2 semanas solo ensuciarías el código.

---

## 5. Resumen en una frase

**Este trimestre tu trabajo es: arreglar el cubo (B), llenarlo de tráfico (D) y prepararte para poder reconstruir la fontanería el próximo trimestre. No empieces la obra (A) con el agua corriendo, y olvida el panel (C) hasta que A no sea una fantasía.**

Cierras el trimestre con dos victorias defendibles:

- “Arreglé el alta y la fuga bajó del 60% a X%.”
- “Produje y publiqué 10 videos para alimentar el funnel.”

Eso es un trimestre realista para un equipo de una sola persona con 4 h/día.