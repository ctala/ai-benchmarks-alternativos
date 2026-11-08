# Grok 4.3 — startup_content/workshop_outline

- model_id: `x-ai/grok-4.3`
- success: True  | final: 8.34 | quality: 9.72
- latency_total: 35.087s | tokens_per_second: 59.5
- input_tokens: 364 | output_tokens: 2086
- judge_score: 4.8 | justificación: 

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

# Outline Workshop: "Construye tu Asistente de IA para tu Startup"

## 📋 Información General
- **Duración:** 3 horas (180 minutos)
- **Formato:** Presencial, 20-30 participantes
- **Perfil:** Emprendedores early-stage no-técnicos
- **Espacio:** Sala con mesas grupales (4-5 personas por mesa)

---

## 🕐 AGENDA DETALLADA

### **BLOQUE 1: El "Wow" - 15 min**
### **BLOQUE 2: Anatomía de un Asistente IA - 25 min**
### **BLOQUE 3: Tu Primer Asistente (Demo en Vivo) - 20 min**
### **☕ BREAK - 10 min**
### **BLOQUE 4: El Ejercicio Principal - 70 min**
### **BLOQUE 5: Demo & Feedback - 25 min**
### **BLOQUE 6: Roadmap & Recursos - 15 min**

---

## 📦 MATERIALES A PREPARAR

### Antes del Workshop:
- [ ] **Cuentas de prueba** en ChatGPT Plus o Claude Pro (5-6 licencias)
- [ ] **WiFi robusto** (mínimo 50 Mbps para 30 personas)
- [ ] **Proyector + pantalla** + altavoces
- [ ] **Post-its** (3 colores) + marcadores por mesa
- [ ] **Template impreso** "Mi Asistente IA" (1 por persona)
- [ ] **QR codes** a recursos (ver sección Recursos)
- [ ] **Backup offline** de slides en PDF
- [ ] **Cronómetro visible** para ejercicios

---

## 🎯 BLOQUES DETALLADOS

---

### **BLOQUE 1: El "Wow" - 15 min**
**Objetivo:** Romper el hielo y mostrar que "sí se puede" en 5 minutos

**Dinámica:** Demo relámpago
- Muestra cómo un asistente IA puede:
  - Escribir un pitch de 30 segundos para un startup ficticia
  - Generar 10 nombres de marca en 30 segundos
  - Crear un email de outreach a inversores

**Key Takeaway:** "Tu asistente IA puede hacer en 5 minutos lo que antes tomaba 2 horas"

**Slides:** 4 slides
- Portada + agenda
- "Antes vs Ahora" (comparativa visual)
- Demo en vivo (sin slides)
- "¿Qué harías si tuvieras esto desde día 1?"

---

### **BLOQUE 2: Anatomía de un Asistente IA - 25 min**
**Objetivo:** Entender los 3 componentes sin tecnicismos

**Dinámica:** Charla + analogía con "contratación de empleados"

| Componente | Analogía | Ejemplo Simple |
|------------|----------|----------------|
| **Prompt Base** | "Tu empleado nuevo" | "Eres un experto en ventas B2B..." |
| **Contexto** | "Tu manual de empresa" | "Nuestra startup vende X a Y..." |
| **Tareas** | "Tu lista de pendientes" | "Escribe emails de seguimiento..." |

**Ejercicio rápido (5 min):** Cada mesa define su "empleado ideal" en 3 frases

**Key Takeaway:** "No necesitas saber programar, necesitas saber qué quieres que haga"

**Slides:** 6 slides
- Analogía del empleado
- Los 3 componentes (visual)
- Ejemplos reales de startups LATAM
- Errores comunes (y cómo evitarlos)
- Tu "empleado ideal" (plantilla)
- Transición al demo

---

### **BLOQUE 3: Tu Primer Asistente (Demo en Vivo) - 20 min**
**Objetivo:** Ver el proceso completo de creación

**Dinámica:** Live coding/demo
- Creo un asistente "Sales Coach" desde cero
- Explico cada decisión en voz alta
- Muestro iteración: "No funciona → ajusto → funciona"

**Key Takeaway:** "El primer intento nunca es perfecto, pero ya tienes algo funcional en 10 minutos"

**Slides:** 3 slides
- Antes de empezar (checklist)
- El proceso paso a paso (diagrama)
- "Tu turno" (transición al ejercicio)

---

### ☕ **BREAK - 10 min**
- QR code para que prueben ChatGPT/Claude
- Networking rápido entre mesas

---

### **BLOQUE 4: Ejercicio Principal - 70 min**
**Objetivo:** Cada persona sale con su asistente funcionando

**Dinámica:** "Design Sprint" de 4 fases

#### **Fase 1: Define tu Dolor (10 min)**
- Plantilla: "Odio cuando tengo que [actividad repetitiva]"
- Cada persona escribe 3 dolores
- Comparte con su mesa, elige el #1

#### **Fase 2: Diseña tu Empleado (15 min)**
- Plantilla "Mi Asistente IA" con 4 secciones:
  1. **Nombre** del asistente
  2. **Rol** (qué hace)
  3. **Contexto** (información de tu startup)
  4. **Tareas específicas** (3 máximo)

#### **Fase 3: Construye (25 min)**
- Cada persona crea su asistente en ChatGPT/Claude
- Facilitador circula respondiendo dudas
- "Buddy system": cada mesa tiene un "buddy técnico" (pre-seleccionado)

#### **Fase 4: Prueba y Ajusta (20 min)**
- Prueba con 2 casos reales de su startup
- Itera mínimo 2 veces
- Documenta qué funcionó/no funcionó

**Key Takeaway:** "Tienes un prototipo funcional de tu asistente en 70 minutos"

**Slides:** 8 slides
- Instrucciones Fase 1
- Plantilla "Mi Asistente IA"
- Instrucciones Fase 2
- Tips para prompts efectivos
- Instrucciones Fase 3
- Troubleshooting común
- Instrucciones Fase 4
- "Comparte tu prototipo" (transición)

---

### **BLOQUE 5: Demo & Feedback - 25 min**
**Objetivo:** Aprender de otros y validar ideas

**Dinámica:** "Demo rápida" (3 min por persona)
- 8-10 personas presentan su asistente (seleccionados al azar)
- Formato: "Mi asistente se llama X y hace Y"
- Feedback de 2 personas de otras mesas

**Key Takeaway:** "Las mejores ideas vienen de ver cómo otros resuelven problemas similares"

**Slides:** 2 slides
- Reglas de la demo
- "Felicidades, ya tienes un asistente"

---

### **BLOQUE 6: Roadmap & Recursos - 15 min**
**Objetivo:** Dar el siguiente paso después del workshop

**Dinámica:** Charla + Q&A

#### **Roadmap de 30 días:**
- **Semana 1:** Refinar tu asistente con 5 casos reales
- **Semana 2:** Crear tu segundo asistente (otro dolor)
- **Semana 3:** Integrar 2 asistentes (ej: Sales + Customer Success)
- **Semana 4:** Documentar tu "sistema" de asistentes

#### **Recursos para llevar:**
- [Lista de 10 prompts probados](QR)
- [Comunidad de WhatsApp](QR)
- [Template Notion "Mis Asistentes IA"](QR)
- [Calendario: "1 hora/semana para IA"](QR)

**Key Takeaway:** "Esto no termina aquí, es el primer paso de tu sistema de IA"

**Slides:** 5 slides
- Roadmap 30 días (visual)
- Recursos (QR codes)
- Comunidad
- Q&A
- Cierre inspirador

---

## 🛠️ EJERCICIO PRINCIPAL DETALLADO

### **"Crea tu Asistente de IA en 70 Minutos"**

**Entregable:** Cada participante sale con:
1. ✅ Su asistente funcionando en ChatGPT/Claude
2. ✅ 2 casos de uso probados
3. ✅ Documentación de iteraciones

**Template "Mi Asistente IA":**

```
NOMBRE: _________________
ROL: _________________
CONTEXTO DE MI STARTUP: _________________
3 TAREAS ESPECÍFICAS:
1. _________________
2. _________________
3. _________________
```

---

## 📱 RECURSOS PARA LLEVAR A CASA

### **QR Codes a incluir:**
1. **Prompt Library** - 10 prompts listos para usar
2. **Comunidad WhatsApp** - Grupo post-workshop
3. **Template Notion** - Organizador de asistentes
4. **Calendario 30 días** - Recordatorios automáticos
5. **Video de 5 min** - "Cómo iterar tu asistente"

---

## 📊 SLIDE COUNT TOTAL: 28 slides

**Distribución:**
- Bloque 1: 4 slides
- Bloque 2: 6 slides
- Bloque 3: 3 slides
- Bloque 4: 8 slides
- Bloque 5: 2 slides
- Bloque 6: 5 slides

---

## ⚡ TIPS DE FACILITACIÓN

- **Tiempo es oro:** Usa cronómetro visible en cada ejercicio
- **Buddy system:** Pre-identifica 4-5 personas con algo de experiencia técnica
- **Backup offline:** Ten prompts impresos por si falla el internet
- **Energía:** Cada 20 min, haz que se levanten o cambien de mesa
- **Celebración:** Cada demo termina con aplausos del grupo