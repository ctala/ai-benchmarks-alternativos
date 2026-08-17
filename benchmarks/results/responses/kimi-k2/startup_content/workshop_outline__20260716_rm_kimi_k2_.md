# Kimi K2 — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 46.178s | tokens_per_second: 44.3
- input_tokens: 219 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y dinámicas de workshop bien estructuradas.

## Respuesta completa

# 🚀 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
## Workshop Práctico | 3 Horas | Emprendedores Early-Stage

---

## 📋 1. AGENDA DETALLADA (3 HORAS)

| Hora | Bloque | Duración |
|:---|:---|:---|
| 0:00 - 0:15 | **Check-in & Contexto** | 15 min |
| 0:15 - 0:45 | **Módulo 1: De la idea al flujo** | 30 min |
| 0:45 - 1:15 | **Módulo 2: Tu primer asistente funcional** | 30 min |
| 1:15 - 1:30 | ☕ **Coffee break + networking** | 15 min |
| 1:30 - 2:15 | **Módulo 3: Superpoderes para tu asistente** | 45 min |
| 2:15 - 2:45 | **Ejercicio principal: El reto de los 20 min** | 30 min |
| 2:45 - 3:00 | **Cierre, showcase y recursos** | 15 min |

---

## 🎒 2. MATERIALES NECESARIOS (PRE-WORKSHOP)

### Para el facilitador:
| Item | Cantidad | Detalle |
|:---|:---|:---|
| Proyector + HDMI/USB-C | 1 | Testeado antes |
| Micrófono (para 20+ personas) | 1 | Preferible lavalier |
| Timer visible | 1 | Para mantener ritmo |
| Stickers de colores | 3 paquetes | Rojo/amarillo/verde para votaciones |
| Post-its grandes (20x20cm) | 2 bloques | Para mapeo colectivo |
| Marcadores gruesos | 10 | Negros, para post-its |

### Para cada participante:
| Item | Cantidad | Preparación |
|:---|:---|:---|
| Laptop cargada | 1 | **CRÍTICO: Confirmar 3 días antes** |
| Cuenta de OpenAI/Claude | 1 | Instrucciones enviadas por email previo |
| Cuenta de Make/Zapier (free) | 1 | Instrucciones enviadas por email previo |
| Ficha de trabajo impresa | 1 | [Ver anexo] |
| Pluma | 1 | Buena calidad |
| Agua + snack ligero | 1 | En mesa |

### Para el ambiente:
- Mesas en formato **cabaret** (4-5 personas por mesa, no filas)
- WiFi de alta velocidad probado con 30+ dispositivos
- Pared o espacio para "museo de flujos" (post-its de ejercicios)
- Música de entrada (playlist "Lo-fi beats" bajo volumen)

---

## 🎯 3. BLOQUES DETALLADOS

---

### **BLOQUE 0: CHECK-IN & CONTEXTO**
⏱️ **15 min** | 📊 **Slides: 5**

| Aspecto | Detalle |
|:---|:---|
| **Objetivo** | Romper hielo, calibrar expectativas y crear energía de "esto sí lo puedo hacer" |
| **Dinámica** | Ritual rápido + mapeo de dolor |
| **Key takeaway** | *"No necesitas saber programar. Necesitas saber qué problema resuelves."* |

**Flujo:**
1. **Entrada musical** (2 min): Mientras llegan, música activa
2. **La pregunta del día** (5 min): *"¿Qué tarea de tu startup te roba más tiempo y te da más pereza?"* → Cada uno escribe en post-it, pega en "Muro de Dolores"
3. **Votación rápida** (5 min): Todos ponen sticker verde en el problema que más resuenan
4. **Promesa del workshop** (3 min): Facilitador presenta los 3 casos que construiremos hoy (atención al cliente, generación de contenido, calificación de leads)

**Slides:**
- 1: Título + foto de asistente IA "real" (no stock photo robótica)
- 2: Foto de facilitador + "Por qué estoy aquí" (30 seg)
- 3: Agenda visual con íconos
- 4: Muro de Dolores (foto de ejemplos)
- 5: Los 3 casos que construiremos (con logos de herramientas)

---

### **MÓDULO 1: DE LA IDEA AL FLUJO**
⏱️ **30 min** | 📊 **Slides: 8**

| Aspecto | Detalle |
|:---|:---|
| **Objetivo** | Entender qué hace un "buen" asistente de IA vs. uno malo |
| **Dinámica** | Demo en vivo + análisis de caso + ejercicio grupal rápido |
| **Key takeaway** | *"Un buen asistente = contexto claro + instrucciones específicas + límite de decisión"* |

**Flujo:**

| Tiempo | Actividad |
|:---|:---|
| 5 min | **Demo: El bueno, el malo y el feo** |
| | - Mismo prompt en ChatGPT: primero genérico (malo), luego con contexto (bueno) |
| | - Participante voluntario lee inputs, todos ven diferencia |
| 10 min | **Anatomía del flujo** |
| | - Slide: "Los 3 pilares del asistente que funciona" |
| | 1. **Contexto**: ¿Quién eres? ¿Qué sabes? |
| | 2. **Instrucción**: ¿Qué hacer exactamente? |
| | 3. **Guardrail**: ¿Qué NO hacer? ¿Cuándo pedir ayuda? |
| 12 min | **Ejercicio en mesas: "El prompt de tu vecino"** |
| | - Cada uno escribe su tarea robatiempo (del check-in) en ficha |
| | - Pasa a la derecha, el vecino escribe: contexto + instrucción + guardrail |
| | - Rotan de nuevo, el tercero evalúa: ¿Esto funcionaría? ¿Qué falta? |
| 3 min | **Share rápido**: 2 mesas comparten su mejor versión |

**Slides:**
- 6: "El bueno, el malo y el feo" (side-by-side de respuestas)
- 7-9: Los 3 pilares (una por pilar, con ejemplos concretos)
- 10: Ejercicio "El prompt de tu vecino" (instrucciones visuales)
- 11: Plantilla de ficha (para referencia)
- 12-13: Ejemplos de guardrails reales (screenshots)

---

### **MÓDULO 2: TU PRIMER ASISTENTE FUNCIONAL**
⏱️ **30 min** | 📊 **Slides: 6**

| Aspecto | Detalle |
|:---|:---|
| **Objetivo** | Cada persona tiene un asistente básico funcionando en su laptop |
| **Dinámica** | Demo paso a paso + trabajo individual asistido + "doctor de código" |
| **Key takeaway** | *"En 15 minutos puedes tener algo que antes te hubiera costado $5,000 y 2 semanas"* |

**Flujo:**

| Tiempo | Actividad |
|:---|:---|
| 5 min | **Demo: Construyendo en tiempo real** |
| | - Facilitador comparte pantalla, construye asistente de ejemplo |
| | - Narración pensando en voz alta: "¿Por qué pongo esto aquí?" |
| 20 min | **Laboratorio: "Mi primer GPT"** |
| | - Todos abren chat.openai.com → "Create a GPT" |
| | - Usan la plantilla de su ficha del ejercicio anterior |
| | - **Rol de "doctores"**: 2-3 personas con más fluidez tecnológica dan vueltas ayudando |
| | - Facilitador proyecta "pantalla de referencia" con pasos numerados |
| 5 min | **Test de fuego**: Cada uno prueba su asistente con un input real, comparte en mesa |

**Slides:**
- 14: "Antes vs. Después" (costo/tiempo de desarrollo tradicional vs. no-code)
- 15: Screenshot numerado de dónde hacer clic (1. Create GPT)
- 16: Screenshot del builder (Configure vs. Preview)
- 17: Checklist de "¿Ya funciona?" (para auto-evaluación)
-