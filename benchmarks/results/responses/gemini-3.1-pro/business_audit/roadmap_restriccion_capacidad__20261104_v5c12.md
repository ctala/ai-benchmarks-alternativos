# Gemini 3.1 Pro — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 6.85 | quality: 8.0
- latency_total: 24.684s | tokens_per_second: 80.3
- input_tokens: 242 | output_tokens: 1981

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

Como jefe de producto de tu empresa, mi trabajo es protegerte de ti mismo y de tu optimismo. 

Vamos a hacer los números reales, porque la matemática no perdona:
Tienes 4 horas al día. Eso son 20 horas a la semana. 
Faltan 8 semanas para cerrar el trimestre. 
**Tu capacidad total real para este trimestre es de 160 horas.** (Es decir, el equivalente a *solo 4 semanas* de trabajo a tiempo completo normal).

Sabiendo esto, vamos a destrozar tu backlog con pura realidad:

*   **A) Reescribir la plataforma:** Requiere 3 meses a tiempo completo (~480 horas). Tienes 160 horas. Si empiezas esto, vas a llegar al final del trimestre con un código a medias, la plataforma actual sin tocar, cero crecimiento y quemado. **Descartado para este trimestre.**
*   **C) Panel de métricas:** Depende de A. Como A está muerto este trimestre, C también. **Descartado.**
*   **B) Arreglar el alta:** Pierdes al 60% de la gente. Tienes un agujero en el barco. Esfuerzo de "1 semana" (40 horas) significa que a tu ritmo te tomará **2 semanas reales**. Alto impacto inmediato. **Prioridad absoluta.**
*   **D) 10 videos:** Esfuerzo de "2 semanas" (80 horas) significa que a tu ritmo te tomará **4 semanas reales**. Impacto medio, pero trae tráfico. **Aprobado.**

---

### Tu plan para las próximas 8 semanas

No vas a hacer 4 cosas, vas a hacer 2. Así queda tu calendario:

**Semanas 1 y 2: Iniciativa B (Arreglar el flujo de alta)**
*   *Por qué:* De nada sirve traer gente con videos si el 60% se te va a ir en el paso 2. Primero tapamos el agujero del barco. 
*   *Objetivo:* Bajar ese 60% de caída a un número manejable (ej. 20%). 

**Semanas 3, 4, 5 y 6: Iniciativa D (Grabar los 10 videos)**
*   *Por qué:* Ahora que el flujo de alta funciona y retiene, tiene sentido meterle gasolina al marketing. 
*   *Objetivo:* Grabar, editar y programar la publicación de los 10 videos.

**Semanas 7 y 8: El "Buffer" de la Realidad**
*   *Por qué:* Eres solo founder. El soporte va a explotar algún día. Te vas a resfriar. Un video te va a tomar más de la cuenta. Nunca planificamos al 100% de capacidad.
*   *Si te sobra tiempo en estas dos semanas:* No empieces a programar la iniciativa A. Úsalas para **investigar y diseñar** la arquitectura de A en papel o Notion, para que cuando tengas el tiempo el próximo trimestre, vayas a tiro hecho.

### Un consejo de PM a Founder:
El impulso de reescribir todo (Iniciativa A) es el asesino silencioso de los *solo founders*. Entiendo que el framework actual te frustra, pero no te está matando; lo que te está matando es perder al 60% de tus usuarios en el onboarding. 

Céntrate en el dinero y la retención hoy. El código bonito puede esperar al próximo trimestre. ¡A trabajar!