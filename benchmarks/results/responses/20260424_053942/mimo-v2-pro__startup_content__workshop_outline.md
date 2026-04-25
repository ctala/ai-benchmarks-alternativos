# MiMo-V2-Pro — startup_content/workshop_outline

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 7.23 | quality: 9.24
- latency_total: 33.86s | tokens_per_second: 60.5
- input_tokens: 209 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# 🚀 "Construye tu Asistente de IA para tu Startup - Workshop Práctico"

## Outline Completo del Workshop (3 horas)

---

## 📋 INFORMACIÓN GENERAL

| Detalle | Descripción |
|---|---|
| **Duración** | 3 horas (180 min) |
| **Audiencia** | 20-30 emprendedores early-stage, no-técnicos |
| **Formato** | Presencial, mesas de trabajo (5-6 personas por mesa) |
| **Nivel requerido** | Cero conocimiento técnico |
| **Resultado esperado** | Cada participante sale con un asistente de IA funcional para su startup |
| **Tono** | Enérgico, práctico, hands-on, cero jerga técnica |

---

## 🧰 MATERIALES NECESARIOS (Preparación Previa)

### Lo que debe preparar EL FACILITADOR

```
ANTES DEL EVENTO (semana previa):
─────────────────────────────────
□ Crear cuentas de ChatGPT Plus (o Claude Pro) de demo
□ Preparar 5-6 cuentas de prueba para mesas (o pedir que cada uno traiga su cuenta)
□ Slide deck completo (ver slide count por sección)
□ Imprimir "AI Startup Canvas" (1 por participante) - tamaño A3
□ Imprimir "Prompt Cheat Sheet" (1 por participante)
□ Imprimir "Playbook del Asistente" template (1 por participante)
□ Preparar 3 casos de éxito reales de startups LATAM con IA
□ Preparar demo en vivo (2 asistentes pre-construidos como ejemplo)
□ Kit de post-it's de 4 colores (1 kit por mesa)
□ Marcadores gruesos (2 por mesa)
□ Proyector + pantalla
□ Micrófono (si hay más de 20 personas)
□ Música de fondo (playlist energética para ejercicios)
□ Timer visible en pantalla
□ Botellas de agua + café/snacks para el break
□ Grupo de WhatsApp del workshop (crear QR para que se unan)
```

### Lo que deben traer LOS PARTICIPANTES

```
📧 Email previo al evento (enviar 3 días antes):
─────────────────────────────────────────────────
→ Laptop cargada (OBLIGATORIO)
→ Cuenta de ChatGPT Plus o Claude Pro creada 
  (con instrucciones paso a paso adjuntas)
→ Datos de su startup en la mente:
  - ¿Qué problema resuelven?
  - ¿Quién es su cliente ideal?
  - ¿Cuál es su dolor operativo más grande HOY?
→ Datos de tarjeta para suscripción si no la tienen ($20/mes)
```

### Distribución del Espacio

```
SALA RECOMENDADA:
┌─────────────────────────────────────────┐
│  [PROYECTOR / PANTALLA]                 │
│  [MESA FACILITADOR + DEMO]              │
│                                         │
│   🪑🪑🪑    🪑🪑🪑    🪑🪑🪑           │
│   MESA 1    MESA 2    MESA 3            │
│                                         │
│   🪑🪑🪑    🪑🪑🪑    🪑🪑🪑           │
│   MESA 4    MESA 5    MESA 6            │
│                                         │
│  [PARED: AI Startup Canvas en grande]   │
│  [ESQUINA: Café + Snacks]               │
└─────────────────────────────────────────┘

5-6 personas por mesa, mesas redondas o cuadradas
```

---

## ⏱️ AGENDA DETALLADA

```
VISUAL DE LAS 3 HORAS:

0:00  ████████████████████████████████████████  1:00
      BLOQUE 1: DESPIERTA (20min)
      BLOQUE 2: FUNDAMENTOS (25min)
      BLOQUE 3: DEMO EN VIVO (15min)

1:00  ████████████████████████████████████████  2:00
      ☕ BREAK (10min)
      BLOQUE 4: EJERCICIO PRINCIPAL pt1 (25min)
      BLOQUE 5: EJERCICIO PRINCIPAL pt2 (25min)

2:00  ████████████████████████████████████████  3:00
      BLOQUE 6: REFINAMIENTO (15min)
      BLOQUE 7: SHOW & TELL (20min)
      BLOQUE 8: CIERRE + RECURSOS (25min)
```

---

## BLOQUE 1: "DESPIERTA EL ÁNGEL DE IA DENTRO DE TI"

**⏰ Duración:** 20 minutos (0:00 - 0:20)
**🎯 Objetivo:** Romper el hielo, generar curiosidad y hacer que todos se den cuenta de que YA usan IA sin saberlo
**🎤 Dinámica:** Charla interactiva + encuesta en vivo + actividad relámpago

### Desarrollo del bloque:

```
MINUTO 0-5: APERTURA ENÉRGICA
──────────────────────────────
• Bienvenida + reglas de la casa:
  - "Aquí no hay preguntas tontas"
  - "Celulares permitidos, laptops abiertas"
  - "El que no pregunta, no emprende"
• Encuesta de mano alzada:
  - "¿Quién usa ChatGPT?" 
  - "¿Quién cree que NO usa IA en su día a día?"
  - "¿Quién tiene miedo de que la IA le quite el trabajo?"

MINUTO 5-12: "LA IA YA VIVE EN TU BOLSILLO"
────────────────────────────────────────────
• Revelación: mostrar 10 formas en que YA usan IA:
  1. Autocompletado del celular
  2. Recomendaciones de Netflix/Spotify
  3. Filtros de Instagram/TikTok
  4. Waze/Google Maps
  5. Filtros de spam en email
  6. Siri/Alexa/Google Assistant
  7. Reconocimiento facial del celular
  8. Traductor de Google
  9. Recomendaciones de MercadoLibre/Amazon
  10. Grammarly/autocorrector
• Frase gancho: "Si ya usas IA para decidir qué serie ver, 
  ¿por qué no la usas para decidir cómo crecer tu startup?"

MINUTO 12-20: ACTIVIDAD RELÁMPAGO - "MI DOLOR OPERATIVO"
────────────────────────────────────────────────────────
• Cada persona escribe en un post-it ROJO:
  "La tarea más repetitiva y dolorosa de mi startup es: ___"
• Se pegan en la pared bajo el título "NUESTROS DOLLORES"
• El facilitador lee 5-6 en voz alta
• Promesa: "Para el final de hoy, tendrás un asistente de IA 
  que te ayude con AL MENOS uno de estos dolores"
```

**📊 Slide count estimado:** 8-10 slides
**💡 Key Takeaway:** "La IA no es el futuro. Es tu presente. Y hoy vas a aprender a domarla para tu startup."

---

## BLOQUE 2: "FUNDAMENTOS - IA PARA EMPRENDEDORES, NO PARA INGENIEROS"

**⏰ Duración:** 25 minutos (0:20 - 0:45)
**🎯 Objetivo:** Dar el vocabulario mínimo necesario y entender qué es un "asistente de IA" en términos de negocio, no de tecnología
**🎤 Dinámica:** Charla ilustrada + analogías + mini-discusión en mesas

### Desarrollo del bloque:

```
MINUTO 20-28: "¿QUÉ ES REALMENTE UN ASISTENTE DE IA?"
──────────────────────────────────────────────────────
• Analogía central: 
  "Un asistente de IA es como un becario increíblemente 
  inteligente pero que necesita que le expliques TODO 
  con detalle. No sabe de tu negocio. No conoce tu 
  contexto. Pero una vez que le enseñas, ejecuta 
  más rápido que cualquier humano."

• Los 3 niveles de uso de IA para startups:
  
  NIVEL 1: USUARIO (todos estamos aquí)
  → Usas ChatGPT para preguntas random
  → "Escríbeme un email..."
  
  NIV