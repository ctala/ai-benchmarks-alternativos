# MiMo V2-Pro (Xiaomi direct) — startup_content/workshop_outline

- model_id: `mimo-v2-pro`
- success: True  | final: 7.73 | quality: 9.24
- latency_total: 41.014s | tokens_per_second: 49.9
- input_tokens: 209 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# 🚀 Workshop: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"

## 📋 INFORMACIÓN GENERAL

| Detalle | Especificación |
|---|---|
| **Duración total** | 3 horas (180 minutos) |
| **Audiencia** | 20-30 emprendedores early-stage, no-técnicos |
| **Formato** | Presencial, interactivo, hands-on |
| **Resultado esperado** | Cada participante sale con un asistente de IA funcional para su startup |
| **Tono** | Energético, práctico, sin jerga técnica innecesaria |
| **Requisito mínimo** | Laptop + cuenta de ChatGPT (free o plus) o Claude |

---

## 🧰 2. MATERIALES NECESARIOS (Preparar antes del workshop)

### Para el facilitador:
- [ ] Proyector/pantalla grande + HDMI/USB-C adaptador
- [ ] Micrófono (si el espacio lo requiere)
- [ ] Bocinas para audio de demos
- [ ] Pizarra blanca o rotafolio grande + marcadores
- [ ] Post-its de 3 colores (amarillo, rosa, verde)
- [ ] Timer visible (proyectado o físico)
- [ ] Presentación en PDF como backup (por si falla internet)
- [ ] Botella de agua + café/agua para participantes
- [ ] Playlist de fondo para ejercicios prácticos (música baja)

### Para cada participante:
- [ ] Laptop propia (comunicar antes del evento)
- [ ] Acceso a internet (WiFi del venue - verificar capacidad para 30 dispositivos)
- [ ] Cuenta creada en ChatGPT (enviar instrucciones 3 días antes)
- [ ] Workbook impreso (PDF que se entrega, ver sección 6)
- [ ] Tarjeta con prompt maestro (template laminado)

### Logística del espacio:
- [ ] Mesas de trabajo en grupos de 4-5 personas
- [ ] Espacio para que todos vean la pantalla
- [ ] Zona de "parking lot" (pizarra para preguntas postergadas)
- [ ] Registros de asistencia

---

## ⏰ 3. AGENDA DETALLADA CON BLOQUES

---

### 🟡 BLOQUE 1: "DESPIERTA EL MOTOR"
**⏰ 0:00 - 0:20 (20 minutos)**

**Objetivo:** Romper el hielo, activar la energía del grupo, establecer el marco mental correcto y hacer que todos entiendan POR QUÉ esto importa AHORA.

**Dinámica:** Ejercicio interactivo + charla corta

**Desglose:**

| Tiempo | Actividad | Detalle |
|---|---|---|
| 0:00-0:05 | Bienvenida & energía | Saludo energético, música de fondo, reglas de la casa (teléfonos OK para buscar, modo avión NO requerido, preguntas en cualquier momento) |
| 0:05-0:12 | Ejercicio "El Dolor" | Cada persona escribe en un post-it AMARILLO la tarea más repetitiva/frustrante de su startup. Se pegan en la pared. Facilitador lee 5-6 en voz alta. |
| 0:12-0:20 | Mini-charla "IA no es el futuro, es tu asistente de HOY" | 3 ejemplos reales de startups LATAM usando asistentes de IA (atención al cliente, prospección, contenido). Datos concretos de tiempo ahorrado. |

**Key Takeaway:**
> *"La IA no reemplaza tu visión de emprendedor. Libera tu tiempo para que hagas lo que solo TÚ puedes hacer: tomar decisiones estratégicas."*

**📊 Slides estimados:** 8-10 slides

---

### 🟠 BLOQUE 2: "ANATOMÍA DE UN ASISTENTE DE IA"
**⏰ 0:20 - 0:45 (25 minutos)**

**Objetivo:** Que cada participante entienda los 4 componentes de un asistente de IA y pueda IDENTIFICAR cuál necesita para su startup.

**Dinámica:** Charla interactiva con demo en vivo + ejercicio rápido

**Desglose:**

| Tiempo | Actividad | Detalle |
|---|---|---|
| 0:20-0:32 | Charla "Los 4 Pilares" | Presentar el framework **R.O.L.E.** (explicado abajo) con ejemplos concretos para startups |
| 0:32-0:38 | Demo en vivo | Facilitador muestra un asistente ya construido funcionando (ej: asistente de atención al cliente para una tienda online). Se ve el antes y después. |
| 0:38-0:45 | Ejercicio "Elige tu asistente" | En el workbook, cada participante llena una matriz para decidir QUÉ asistente construir hoy |

**Framework R.O.L.E.:**
```
R - Rol: ¿Quién es? (Ej: "Eres un experto en atención al cliente...")
O - Objetivo: ¿Qué debe lograr? (Ej: "Tu objetivo es resolver dudas en menos de 2 interacciones...")
L - Límites: ¿Qué NO debe hacer? (Ej: "Nunca prometas descuentos sin autorización...")
E - Estilo: ¿Cómo habla? (Ej: "Habla de forma cálida, usa 'tú', sé breve...")
```

**Matriz de decisión (ejercicio):**
| Pregunta | Mi respuesta |
|---|---|
| ¿Qué tarea me roba más de 3 horas semanales? | |
| ¿Quién la hace ahora? (yo / nadie / alguien a regañadientes) | |
| ¿Se puede describir con reglas claras? | |
| ¿Necesita datos de mi negocio o es general? | |

**Key Takeaway:**
> *"Un asistente de IA es como contratar a un empleado: necesitas definirle el puesto (rol), los KPIs (objetivo), las reglas (límites) y la cultura de la empresa (estilo)."*

**📊 Slides estimados:** 12-15 slides

---

### 🔴 BLOQUE 3: "EL ARTE DEL PROMPT - Tu Nueva Superpotencia"
**⏰ 0:45 - 1:15 (30 minutos)**

**Objetivo:** Dominar la técnica de escritura de prompts que convierte a ChatGPT/Claude de "chatbot genérico" en "tu empleado experto".

**Dinámica:** Charla corta + ejercicio práctico iterativo (el más técnico del workshop, pero accesible)

**Desglose:**

| Tiempo | Actividad | Detalle |
|---|---|---|
| 0:45-0:55 | Charla "Prompting para mortales" | La fórmula S.C.O.R.E. (explicada abajo). Errores comunes. Antes/después de un buen prompt. |
| 0:55-1:05 | Ejercicio "Prompt Battle" (ronda 1) | Cada mesa recibe el MISMO caso de uso. Escriben un prompt. Lo prueban. Comparan resultados entre mesas. El facilitador muestra la versión optimizada. |
| 1:05-1:15 | Ejercicio "Prompt Battle" (ronda 2) | Ahora cada participante escribe un prompt para SU asistente específico. Prueban. Ajustan. El facilitador circula y ayuda. |

**Fórmula S.C.O.R.E.:**
```
S - Situación:     "Eres [rol] de una startup de [industria]..."
C - Contexto:      "Nuestro cliente típico es... Nuestro producto es..."
O - Objetivo:      "Tu tarea es... Siempre busca..."
R - Restricciones: "Nunca hagas...