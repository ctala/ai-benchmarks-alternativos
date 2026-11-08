# Kimi K2 — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.14 | quality: 9.72
- latency_total: 68.596s | tokens_per_second: 46.2
- input_tokens: 219 | output_tokens: 3166
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

# 🚀 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
## Workshop Práctico | 3 Horas | Emprendedores Early-Stage

---

## 📋 1. AGENDA DETALLADA (3 HORAS)

| Bloque | Tiempo | Actividad |
|--------|--------|-----------|
| **Bloque 1** | 0:00-0:45 | Fundamentos y Mapeo de Tu Proceso |
| *Break* | 0:45-0:50 | ☕ (5 min) |
| **Bloque 2** | 0:50-1:35 | Construcción en Vivo: Tu Primer Asistente |
| *Break* | 1:35-1:45 | 🍪 (10 min) |
| **Bloque 3** | 1:45-2:35 | Conexiones, Automatizaciones y Escalamiento |
| **Cierre** | 2:35-3:00 | Presentaciones Rápidas y Próximos Pasos |

---

## 🎒 2. MATERIALES NECESARIOS

### Para el facilitador (preparar antes):
| Item | Cantidad | Detalle |
|------|----------|---------|
| Cuentas demo | 3-4 | ChatGPT Plus, Claude Pro, Make/Zapier, Notion |
| Hotspot de respaldo | 1 | Por si falla el WiFi del lugar |
| Adaptadores HDMI/USB-C | 2 | Para conectar laptops de participantes |
| Stickers/post-its de colores | 3 paquetes | Para votaciones y organización |
| Extensiones eléctricas | 4 | Para cargar laptops |
| Agua y snacks | Suficiente | Para 30 personas |

### Para cada participante (enviar checklist 48h antes):
```
✅ Laptop con cargador (obligatorio)
✅ Cuenta de Gmail/Outlook activa
✅ Tarjeta de crédito (para free trials, sin cargo real)
✅ Lista de 3 tareas repetitivas que hacen semanalmente
✅ Acceso a su email de trabajo (para probar integraciones)
```

### Infraestructura del salón:
- WiFi estable (testear antes con 30 dispositivos simultáneos)
- Pantalla grande + 2 monitores laterales (visibilidad)
- Mesas en formato "cabaret" (4-5 personas por mesa, no auditorio)
- Sonido con micrófono inalámbrico

---

## 🔥 3. BLOQUES DETALLADOS

### **BLOQUE 1: "Antes de Clickear: Mapea Tu Caos"**
*45 minutos | Slides: 12-15*

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Que cada emprendedor identifique UNA tarea específica y de alto impacto para automatizar, no diez vagas |
| **Dinámica** | Charla rápida (15 min) + Ejercicio grupal (25 min) + Compartir (5 min) |

**Flujo:**
1. **Charla energética** (15 min): "El mito del emprendedor héroe que todo lo hace solo" → casos reales de founders latinoamericanos que escalaron con IA antes de contratar
2. **Ejercicio "La Fábrica de Tareas"** (25 min):
   - Individual: Listar 10 tareas que hicieron la semana pasada
   - En mesas: Clasificar en matriz 2x2 (Tiempo consumido vs. Valor estratégico)
   - Votar con post-its: ¿Cuál liberaría más energía si la automatizan?
3. **Compartir rápido**: 3 voluntarios, 30 segundos cada uno

**Key Takeaway:**  
> *"No automatices lo que puedes eliminar. No elimines lo que puedes estandarizar. Tu primera automatización debe liberarte 5+ horas semanales."*

---

### **BLOQUE 2: "Manos en el Código... Sin Código"**
*45 minutos | Slides: 8-10 (más pantalla compartida)*

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Cada participante construye un asistente funcional que responda emails o genere contenido para su startup |
| **Dinámica** | Demo en vivo + Ejercicio guiado + Mesa de ayuda itinerante |

**Flujo:**
1. **Demo "El Antes y Después"** (10 min): Mostrar 3 asistentes reales funcionando (responder consultas, generar propuestas, calificar leads)
2. **Construcción guiada** (30 min):

   **OPCIÓN A (Recomendada - más fácil):**
   - Herramienta: ChatGPT + Google Sheets + Zapier (gratis)
   - Resultado: Asistente que lee formulario de contacto → genera respuesta personalizada → guarda en spreadsheet
   
   **OPCIÓN B (Más potente):**
   - Herramienta: Claude + Make + Notion
   - Resultado: Asistente que procesa audio de reuniones → extrae action items → crea tareas

3. **Ronda de ayuda** (5 min): Facilitador + 2 ayudantes recorren mesas

**Key Takeaway:**  
> *"Tu asistente no necesita ser perfecto. Necesita ser 70% bueno y 100% tuyo. La iteración la haces con el uso real."*

---

### **BLOQUE 3: "Conecta, Automatiza, Escala"**
*50 minutos | Slides: 10-12*

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Expandir el asistente básico a un flujo de trabajo conectado y preparar roadmap de los próximos 90 días |
| **Dinámica** | Demo + Ejercicio de diseño + Discusión en mesas + Compromiso individual |

**Flujo:**
1. **Demo "El Ecosistema"** (15 min): Mostrar stack completo de un founder real (entrada → procesamiento → salida → seguimiento)
2. **Ejercicio "Dibuja Tu Cadena"** (20 min):
   - En papel: Dibujar 3-5 pasos de su flujo ideal
   - Identificar qué ya funciona, qué falta, qué puede esperar
3. **Discusión en mesas** (10 min): Compartir diseños, dar feedback rápido
4. **Compromiso 90 días** (5 min): Cada uno escribe en post-it: "Para [fecha] mi asistente hará: ___"

**Key Takeaway:**  
> *"Un asistente desconectado es un lujo. Un asistente integrado en tu operación es un multiplicador de tu equipo."*

---

### **CIERRE: "Demo Day Express"**
*25 minutos | Slides: 3-5*

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Celebrar avances, crear accountability entre pares, y asegurar siguiente paso concreto |
| **Dinámica** | Presentaciones relámpago + Votación + Cierre energético |

**Flujo:**
1. **Presentaciones relámpago** (15 min): 6 voluntarios, 90 segundos cada uno mostrando su asistente
2. **Votación** (5 min): Todos votan con stickers por "Más útil", "Más creativo", "Más probable que lo use"
3. **Cierre** (5 min): Compromiso grupal + foto + reparto de recursos

---

## 🛠️ 4. EJERCICIO PRINCIPAL: "TU PRIMER ASISTENTE FUNCIONAL"

### **Nombre:** Asistente de Respuesta a Clientes Potenciales

### **Descripción:**
Cada participante construirá un sistema que reciba una consulta de un cliente potencial y genere una respuesta personalizada, lista para enviar (o enviada automáticamente en versión avanzada).

### **Niveles de dificultad:**

| Nivel | Herramientas | Resultado | Tiempo estimado |
|-------|-------------|-----------|-----------------|
| **🟢 Básico** | ChatGPT + copiar/pegar | Prompt optimizado que genera respuestas | 15 min |
| **🟡 Intermedio** | ChatGPT + Google Sheets + Zapier | Formulario → spreadsheet → respuesta generada → guardada para revisión | 30 min |
| **🔴 Avanzado** | Claude + Make + Gmail + Notion | Email recibido → analizado → respuesta generada → enviada automáticamente (con copia humana) → tarea creada | 45 min |

### **Plantilla de prompt que entregamos:**

```
ROL: Eres [nombre del asistente], el especialista en atención de [startup] 
que ofrece [servicio/producto].

CONTEXTO: Recibiste este mensaje de un posible cliente:
---
[MENSAJE DEL CLIENTE]
---

TU TAREA: Responde de manera profesional, cálida y concisa que:
1. Agradece su interés
2. Responde específicamente a [punto clave de su mensaje]
3. Propone UN siguiente paso claro (llamada, demo, envío de info)
4. Menciona brevemente [diferenciador clave de tu startup]

TONO: [ej: cercano pero profesional / técnico pero accesible / lujo discreto]

RESTRICCIONES: Máximo 150 palabras. No uses jerga de [industria]. 
Incluye una pregunta que invite a responder.
```

### **Checklist de éxito del ejercicio:**
- [ ] El asistente recibe información de entrada (email/formulario/manual)
- [ ] Procesa con alguna herramienta de IA
- [ ] Genera salida útil y personalizada
- [ ] La salida se guarda o entrega de forma accesible

---

## 📦 5. RECURSOS PARA LLEVAR A CASA

### **Kit digital (enviar por email 24h después):**

| Recurso | Formato | Descripción |
|---------|---------|-------------|
| **Playbook del workshop** | PDF | Todo el contenido + screenshots paso a paso |
| **Biblioteca de prompts** | Notion/Google Docs | 20+ prompts probados para emprendedores (ventas, marketing, operaciones, atención al cliente) |
| **Plantilla de evaluación de herramientas** | Excel/Sheets | Matriz para comparar costo, tiempo de setup, y ROI de diferentes herramientas |
| **Roadmap 90 días** | PDF editable | Plan semana a semana para expandir su asistente |
| **Comunidad WhatsApp/Discord** | Link | Grupo de seguimiento con los participantes |

### **Cheat sheets impresas (entregar al final):**
- **"Los 5 errores que matan tu primer asistente de IA"** (tamaño media carta, laminado)
- **"Emergencia: ¿Qué hacer cuando tu asistente falla?"** (flujo de decisión rápido)

### **Descuentos/accesos:**
- Códigos de free trial extendido para herramientas usadas
- Acceso a webinar gratuito de seguimiento (30 días después)

---

## 📊 6. SLIDE COUNT ESTIMADO

| Sección | Slides | Notas |
|---------|--------|-------|
| Apertura y contexto | 3 | Título, foto de grupo esperada, reglas del juego |
| Bloque 1 - Fundamentos | 12 | Incluye matrices, ejemplos de founders reales |
| Bloque 2 - Construcción | 8 | Más demo en vivo que slides |
| Bloque 3 - Escalamiento | 10 | Diagramas de flujo, arquitecturas de ejemplo |
| Cierre y recursos | 4 | QR codes, contactos, foto grupal |
| **TOTAL** | **~37 slides** | + pantallas de herramientas durante demos |

---

## 💡 NOTAS PARA EL FACILITADOR

### **Energía y ritmo:**
- Cada 20 minutos, cambiar de posición (sentado/parado), tono, o actividad
- Usar música de fondo baja durante ejercicios (playlist "lo-fi beats" o similar)
- Celebrar rápido: "¡Eso!" cuando alguien logra algo

### **Manejo de 20-30 personas:**
- 2 ayudantes técnicos que recorren durante ejercicios
- Sistema de "tarjetas de ayuda": roja (estoy atascado), amarilla (duda), verde (avanzando)
- Mesas de 4-5, mix de industrias si es posible

### **Contingencias:**
- Si el WiFi falla: versión offline con prompts pre-cargados y ejercicio de diseño en papel
- Si alguien no tiene laptop: emparejar con alguien que sí tenga (pair programming)
- Si van muy rápido: desafío bonus de integración con herramienta adicional

---

*¿Listo para liberar horas de tu semana? Empecemos.* 🚀