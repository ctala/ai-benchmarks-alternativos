# DeepSeek V4.1 Flash — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 42.768s | tokens_per_second: 204.4
- input_tokens: 224 | output_tokens: 8742
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando una agenda detallada y útil para el workshop, con ejercicios prácticos y materiales necesarios, adecuados para emprendedores no técnicos.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un facilitador de workshops de emprendimiento y tecnologia con experiencia en Latinoamerica.

**user:**

Crea el outline completo para un workshop presencial de 3 horas titulado:
"Construye tu Asistente de IA para tu Startup - Workshop Practico"

La audiencia son emprendedores early-stage no-tecnicos (20-30 personas).

Incluye:
1. Agenda detallada con tiempos (3 horas)
2. Materiales necesarios (que preparar antes)
3. Para cada bloque:
   - Titulo y duracion
   - Objetivo
   - Dinamica (charla, ejercicio, demo, discusion)
   - Key takeaway
4. Ejercicio principal del workshop (que todos puedan hacer)
5. Recursos para llevar a casa
6. Slide count estimado por seccion

El tono debe ser energico y practico, no academico.


## Respuesta completa

# Workshop: Construye tu Asistente de IA para tu Startup
## Workshop Práctico

**Duración:** 3 horas (180 min)  
**Audiencia:** 20-30 emprendedores early-stage no técnicos  
**Formato:** Presencial, mesas redondas, tríos, laptops/celulares  
**Promesa:** *“Sales con un asistente de IA diseñado, probado y listo para usar en tu startup. Sin código. Sin humo.”*  
**Tono:** Energético, práctico, cero académico. “Menos teoría, más construir.”

---

## 1. Agenda detallada con tiempos

| Hora | Bloque | Min | Formato |
|---|---|---|---|
| 0:00 - 0:15 | Bienvenida y encuadre: “Tu startup en 3 palabras” | 15 | Dinámica + charla |
| 0:15 - 0:35 | IA sin humo: qué puede y qué no hacer por tu startup | 20 | Charla + demo en vivo |
| 0:35 - 1:00 | Detecta el trabajo repetitivo que te roba tiempo | 25 | Ejercicio en parejas + discusión |
| 1:00 - 1:20 | Anatomía de un asistente que sí resuelve | 20 | Charla + demo |
| 1:20 - 1:35 | Break: café + networking | 15 | Descanso |
| 1:35 - 2:25 | EJERCICIO PRINCIPAL: Construye tu Asistente de IA | 50 | Manos a la obra en tríos |
| 2:25 - 2:45 | Testing cruzado + Demo relámpago | 20 | Test + feedback + demo |
| 2:45 - 3:00 | Cierre: Plan de 7 días y recursos | 15 | Compromiso + entrega |

**Total:** 180 minutos.

---

## 2. Materiales necesarios (checklist antes del workshop)

### Logística y espacio
- Salón con mesas redondas para 5 personas (6 mesas para 30).
- Proyector, HDMI, adaptadores, sonido, micrófono si el grupo es grande.
- WiFi robusto + hotspot de respaldo.
- Extensiones eléctricas y regletas por mesa.
- Timer visible (pantalla o cronómetro grande).
- Música suave para ejercicios y break.

### Papelería
- Hojas de trabajo impresas:
  - Mapa de Dolores
  - Ficha del Asistente
  - Plantilla Prompt Maestro
  - Plan de 7 días
- Post-its, sharpies, stickers, tarjetas, etiquetas de nombre.
- Rotafolios o papelógrafos por mesa.
- Cinta adhesiva, marcadores gruesos.

### Tecnología y herramientas
- Slides listas y backup en USB + nube.
- QR a carpeta digital con plantillas, prompts y recursos.
- Cuentas de prueba: ChatGPT, Gemini, Copilot, Claude, Poe.
- Guía previa enviada por email: “Trae laptop, crea tu cuenta gratis en ChatGPT o Gemini”.
- Laptops de respaldo (2-3) por si alguien falla.
- Formulario de registro previo con preguntas: tipo de startup, dolor principal, herramientas que usa.

### Facilitación
- 1 facilitador principal + 2-3 asistentes para mesas.
- Guion de demos con datos ficticios.
- Casos de ejemplo reales de LatAm.
- Premios simbólicos: stickers, menciones, certificados.

### Coffee break
- Café, agua, snacks, fruta.
- Servilletas, vasos, bolsas de basura.

---

## 3. Bloques detallados

### Bloque 0: Bienvenida y encuadre — “Tu startup en 3 palabras”
**Duración:** 15 min  
**Slides:** 4  
**Objetivo:** Crear clima de confianza, alinear expectativas y mostrar el resultado final.  
**Dinámica:**  
- Dinámica rompehielo: cada persona dice su nombre, startup en 3 palabras y el dolor que más le quita tiempo.  
- Reglas del juego: práctico, sin jerga, todos construyen, se respeta el tiempo.  
- Muestra rápida: un asistente de IA funcionando en vivo (30 segundos).  
**Key takeaway:** *“No venimos a aprender teoría. Venimos a construir un asistente que te devuelva horas.”*

---

### Bloque 1: IA sin humo — qué puede y qué no hacer por tu startup
**Duración:** 20 min  
**Slides:** 8  
**Objetivo:** Entender capacidades y límites de la IA sin tecnicismos.  
**Dinámica:**  
- Charla con ejemplos reales: atención al cliente, contenido, cotizaciones, investigación de mercado.  
- Demo en vivo: “Prompt malo vs. Prompt bueno”.  
- Mitos vs. realidades: “No, no va a manejar tu startup solo. Sí, puede ahorrarte 5 horas semanales.”  
**Key takeaway:** *“La IA no reemplaza tu criterio; amplifica tu criterio. Sirve para tareas repetitivas con contexto.”*

---

### Bloque 2: Detecta el trabajo repetitivo que te roba tiempo
**Duración:** 25 min  
**Slides:** 10  
**Objetivo:** Priorizar 1 caso de uso de alto impacto y baja complejidad.  
**Dinámica:**  
- Ejercicio “Mapa de Dolores” en parejas:  
  1. Lista 5 tareas repetitivas que te quitan tiempo.  
  2. Puntúa frecuencia (1-5) y dolor (1-5).  
  3. Elige la de mayor puntaje que se pueda resolver con texto.  
  4. Comparte en mesa y recibe 1 idea.  
- Facilitadores pasan por mesas ayudando a elegir.  
**Key takeaway:** *“El mejor primer asistente no es el más ambicioso, es el que resuelve una tarea repetitiva, concreta y medible.”*

---

### Bloque 3: Anatomía de un asistente que sí resuelve
**Duración:** 20 min  
**Slides:** 12  
**Objetivo:** Conocer el framework “ADN del Asistente” para diseñar uno útil.  
**Dinámica:**  
- Presentar el framework:  
  - **Rol:** ¿Quién es?  
  - **Objetivo:** ¿Qué logra?  
  - **Contexto:** ¿Qué sabe de tu startup?  
  - **Reglas:** ¿Qué sí y qué no?  
  - **Conocimiento:** ¿Qué documentos usa?  
  - **Formato:** ¿Cómo responde?  
- Demo en vivo: construir un asistente de atención al cliente para una startup ficticia en 7 minutos.  
**Key takeaway:** *“Un asistente útil = problema claro + contexto de tu negocio + reglas + ejemplos + formato de salida.”*

---

### Break: Café + networking
**Duración:** 15 min  
**Slides:** 1  
**Objetivo:** Recargar energía y conectar con otros emprendedores.  
**Dinámica:** Café libre. Música. Reto opcional: “Encuentra a alguien que tenga un dolor similar al tuyo e intercambien ideas.”  
**Key takeaway:** *“Las mejores ideas salen con café y conversación random.”*

---

### Bloque 4: EJERCICIO PRINCIPAL — Construye tu Asistente de IA
**Duración:** 50 min  
**Slides:** 15  
**Objetivo:** Que cada participante construya y pruebe un asistente de IA para su startup usando plantillas y herramientas no-code.  
**Dinámica:** Trabajo en tríos con roles rotativos:  
- **Piloto:** dueño del problema.  
- **Copiloto:** ayuda a redactar el prompt.  
- **Tester:** hace preguntas difíciles.  
**Herramientas:** ChatGPT, Gemini, Copilot, Claude, Poe. Si tienen plan, crean Custom GPT/Gem. Si no, usan el Prompt Maestro en cualquier LLM gratis.  
**Pasos:**  
1. Elegir dolor (5 min).  
2. Completar Ficha del Asistente (10 min).  
3. Escribir Prompt Maestro + pegar contexto (15 min).  
4. Probar y ajustar con 5 preguntas reales (15 min).  
5. Preparar demo de 30 seg (5 min).  
**Key takeaway:** *“Ya tienes un asistente funcional. No es perfecto, pero es tuyo y puedes mejorarlo iterando.”*

---

### Bloque 5: Testing cruzado + Demo relámpago
**Duración:** 20 min  
**Slides:** 6  
**Objetivo:** Validar el asistente con otros ojos y aprender de los demás.  
**Dinámica:**  
- 10 min: test cruzado en parejas. Cada uno prueba el asistente del otro con 3 preguntas.  
- 10 min: demo relámpago. 3 voluntarios muestran su asistente. Feedback rápido: “¿Qué te sirvió? ¿Qué mejorarías?”  
**Key takeaway:** *“El feedback en vivo es el mejor prompt de mejora.”*

---

### Bloque 6: Cierre — Plan de 7 días y recursos
**Duración:** 15 min  
**Slides:** 6  
**Objetivo:** Convertir el asistente en hábito y siguiente paso.  
**Dinámica:**  
- Cada participante escribe en una tarjeta: “En 7 días voy a…” y lo comparte con su mesa.  
- Entrega de recursos por QR.  
- Foto grupal.  
**Key takeaway:** *“El valor no está en el workshop, está en usarlo mañana. Plan: 1 mejora por día.”*

---

## 4. Ejercicio principal del workshop: “Tu Primer Empleado de IA”

**Nombre:** Tu Primer Empleado de IA  
**Duración:** 50 min construcción + 20 min testing/demo  
**Formato:** Tríos. Todos construyen.  
**Herramientas:** ChatGPT, Gemini, Copilot, Claude, Poe.  
**Entregable:** Enlace al bot o Prompt Maestro + Ficha del Asistente.

### Paso a paso
1. **Elige el dolor (5 min)**  
   Usa el Mapa de Dolores. Un solo caso: atención al cliente, ventas, contenido, investigación o onboarding.

2. **Completa la Ficha del Asistente (10 min)**  
   - Nombre del asistente  
   - Usuario principal  
   - Objetivo en 1 frase  
   - Tono de voz  
   - 3 reglas claras  
   - Formato de salida deseado

3. **Escribe el Prompt Maestro (15 min)**  
   Plantilla:
   ```
   Eres [ROL] de [STARTUP]. Tu objetivo es [OBJETIVO].
   Contexto: [PITCH, CLIENTE IDEAL, PRODUCTO, PRECIOS, TONO].
   Reglas:
   - [REGLA 1]
   - [REGLA 2]
   - [REGLA 3]
   Conocimiento: [PEGA FAQ, PRECIOS, INFO CLAVE].
   Responde siempre en [FORMATO].
   Si no sabes algo, di: "No tengo esa información, consulta con el equipo".
   ```

4. **Prueba y ajusta (15 min)**  
   Haz 5 preguntas reales. Anota qué falla. Ajusta el prompt. Vuelve a probar.

5. **Prepara demo de 30 seg (5 min)**  
   Muestra qué hace, para qué sirve y qué resultado da.

6. **Testing cruzado (10 min)**  
   En parejas, cada uno prueba el asistente del otro con 3 preguntas difíciles.

7. **Demo relámpago (10 min)**  
   3 voluntarios muestran su asistente. Feedback rápido del grupo.

**Key takeaway:** *“No necesitas programar. Necesitas saber qué problema resuelves y darle contexto a la IA.”*

---

## 5. Recursos para llevar a casa

- **Plantilla Prompt Maestro** editable (Google Docs / Notion).
- **Ficha del Asistente** para diseñar nuevos asistentes.
- **Mapa de Dolores + Matriz de priorización** para elegir casos de uso.
- **25 prompts listos** para startups: atención, ventas, contenido, research, fundraising.
- **Guía de herramientas no-code:** Custom GPT, Gemini Gems, Poe, Botpress, Voiceflow, Make/Zapier.
- **Checklist de implementación en 7 días.**
- **Grabación del workshop y slides.**
- **Comunidad WhatsApp/Discord** + sesión de seguimiento opcional.

---

## 6. Slide count estimado por sección

| Sección | Slides |
|---|---|
| Portada + Bienvenida y encuadre | 4 |
| Bloque 1: IA sin humo | 8 |
| Bloque 2: Detecta trabajo repetitivo | 10 |
| Bloque 3: Anatomía del asistente | 12 |
| Break | 1 |
| Ejercicio principal | 15 |
| Testing + Demo relámpago | 6 |
| Cierre + Plan 7 días | 6 |
| Anexos (prompts, recursos, QR) | 8 |
| **Total estimado** | **70 slides** |

> **Tip:** Usa muchas visuales, memes tecnológicos, ejemplos reales y pocas palabras por slide. La energía se mantiene con demos y acción, no con diapositivas.

---

## 7. Tips logísticos para 20-30 personas

- Mesas de 5. Tríos para el ejercicio. Los otros 2 roles: apoyo y tester.
- 2-3 facilitadores de apoyo para que nadie se quede atascado.
- Envía un email 3 días antes: “Trae laptop, crea cuenta en ChatGPT o Gemini, piensa en tu tarea más repetitiva”.
- Ten un plan B si falla el WiFi: usa hotspots o prompts en local.
- Usa un timer visible. La energía sube cuando hay tiempos claros.
- Cierra con foto grupal y QR a todos los recursos.

**Frase de cierre sugerida:**  
*“La IA no va a reemplazar a los emprendedores. Pero los emprendedores que usan IA van a reemplazar a los que no la usan. Hoy ya tienes tu primer asistente. Ahora úsalo.”*