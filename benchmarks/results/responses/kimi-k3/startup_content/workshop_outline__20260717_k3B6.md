# Kimi K3 — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.82 | quality: 10.0
- latency_total: 194.472s | tokens_per_second: 35.1
- input_tokens: 302 | output_tokens: 6817
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando un plan detallado y práctico para el taller.

## Respuesta completa

# 🚀 Construye tu Asistente de IA para tu Startup
### Outline completo — Workshop presencial, 3 horas, 20-30 emprendedores no-técnicos

**La promesa del taller:** *"Entras con una idea, sales con un asistente funcionando."* Todo el diseño gira alrededor de esa promesa. Poca teoría, mucha construcción.

---

## 1. Agenda General (vista rápida)

| Hora | Bloque | Duración | Dinámica |
|------|--------|----------|----------|
| 0:00 – 0:15 | Bienvenida + Conexión | 15 min | Icebreaker |
| 0:15 – 0:35 | La IA ya llegó: qué puede hacer por tu startup | 20 min | Charla + mini-demos |
| 0:35 – 1:00 | ¿Dónde duele? Mapa de Oportunidades | 25 min | Ejercicio individual + parejas |
| 1:00 – 1:20 | Anatomía de un Asistente + Demo en vivo | 20 min | Demo en vivo |
| 1:20 – 1:35 | ☕ Break | 15 min | — |
| 1:35 – 2:25 | ⚡ Sprint de Construcción: tu Asistente v1.0 | 50 min | Ejercicio principal |
| 2:25 – 2:45 | Testea al vecino | 20 min | Pruebas cruzadas |
| 2:45 – 2:55 | Los 5 errores que matan a un asistente | 10 min | Charla relámpago |
| 2:55 – 3:00 | Cierre: tu compromiso de 7 días | 5 min | Acción pública |

---

## 2. Materiales (preparar ANTES)

### Del facilitador
- **Slides** (~32 total, ver desglose abajo)
- **Demo pre-grabada en video** de respaldo (la regla de oro: nunca confíes 100% en el wifi del venue)
- **Plantilla impresa "Prompt Maestro"** — 1 por persona + 10 extras (ver sección 4)
- **Hoja "Mapa de Oportunidades"** impresa — 1 por persona
- Post-its de 2 colores + marcadores gruesos
- Flip chart para el "Parking Lot" (preguntas avanzadas que no frenan al grupo)
- Timer visible para todos (proyectado o físico)
- QR impreso grande con los recursos para llevar
- Hotspot móvil cargado como Plan B de internet
- Extensiones y regletas de corriente

### De los participantes (enviar email 3-4 días antes)
- ✅ **Laptop obligatoria** (no tablet, no celular)
- ✅ **Cuenta creada en ChatGPT o Claude ANTES del taller** (30 personas creando cuentas a la vez = 20 minutos perdidos y wifi muerto)
- ✅ Traer en digital: descripción de su negocio, precios, FAQs, políticas de envío/devolución — lo que tengan, aunque sea desordenado
- ✅ Saber su usuario/contraseña (sí, hay que decirlo 😄)

### Del venue
- Wifi que aguante 30+ dispositivos simultáneos (probarlo el día anterior)
- Mesas de trabajo en grupos de 4-6 (NO formato auditorio)
- Proyector + enchufes accesibles por mesa

**Equipo humano ideal:** 1 facilitador principal + 1-2 asistentes flotantes para el sprint de construcción. Con 30 personas, el ratio 1:15 es el mínimo viable.

---

## 3. Bloque por Bloque

### 🔥 Bloque 1 — Bienvenida + Conexión (15 min)
- **Objetivo:** Subir la energía, romper el hielo y calibrar el nivel del grupo.
- **Dinámica:** Bienvenida rápida (3 min). Luego cada persona: nombre + startup + "la tarea que más odio de mi negocio" en 30 segundos. El facilitador anota patrones en el flip chart — eso alimenta el Bloque 3.
- **Key takeaway:** *"Hoy nadie se va sin un asistente funcionando."* (Decirlo en voz alta, es la promesa.)
- **Slides: 3** (portada, reglas del juego, promesa del taller)

### 🌎 Bloque 2 — La IA ya llegó (20 min)
- **Objetivo:** Nivelar el piso: qué es un asistente de IA hoy y por qué ya no necesitas programadores.
- **Dinámica:** Charla de 12 min con 3 ejemplos reales tipo LatAm (una tienda online que responde por WhatsApp, un consultor que agenda citas, un restaurante que toma pedidos). Luego 2 mini-demos en vivo de 3 min: hacer una pregunta de cliente a un asistente ya armado.
- **Key takeaway:** *"La IA no es magia: es un empleado rapidísimo que necesita instrucciones muy claras."*
- **Slides: 7** (momento actual, 3 ejemplos, qué es/qué no es, 2 de demo)

### 🎯 Bloque 3 — ¿Dónde duele? Mapa de Oportunidades (25 min)
- **Objetivo:** Que cada uno identifique EL caso de uso de su asistente (el error #1 es querer que haga todo).
- **Dinámica:** Ejercicio individual (10 min) con la hoja "Mapa de Oportunidades": listar 5 tareas repetitivas → marcar cuál consume más horas → definir en una frase qué haría el asistente. Luego 10 min en parejas: cada uno presenta su caso y el compañero pregunta "¿y esto te ahorra tiempo o dinero de verdad?". Cierre: 3 voluntarios comparten al grupo (5 min).
- **Key takeaway:** *"El mejor asistente resuelve un dolor real, no uno cool."*
- **Slides: 4** (instrucciones del ejercicio, ejemplos de casos de uso, timer)

### 🔬 Bloque 4 — Anatomía de un Asistente + Demo en vivo (20 min)
- **Objetivo:** Desmitificar la construcción: mostrar que un asistente son 4 ingredientes, no código.
- **Dinámica:** Charla de 8 min: la fórmula **Rol + Conocimiento + Reglas + Límites**. Luego demo en vivo de 12 min: construir desde cero un asistente para un negocio ficticio (ej: "Pupusas Don Chepe" 🫓) usando la plantilla Prompt Maestro en pantalla. Que el público sugiera la personalidad del asistente — participación = atención.
- **Key takeaway:** *"Asistente = rol + conocimiento + reglas + límites. Si falta uno, se rompe."*
- **Slides: 5** (la fórmula, la plantilla, 3 del paso a paso)

### ⚡ Bloque 5 — Sprint de Construcción (50 min) — *EL CORAZÓN DEL TALLER*
- Detalle completo en la sección 4. ⬇️
- **Slides: 6** (una por cada paso del sprint — quedan proyectadas como referencia)

### 🧪 Bloque 6 — Testea al vecino (20 min)
- **Objetivo:** Descubrir los huecos del asistente antes de que los descubra un cliente real.
- **Dinámica:** Pruebas cruzadas en parejas: cada uno le hace a su compañero "las 5 preguntas incómodas" (un cliente confundido, uno enojado, algo fuera de tema, algo que el asistente no sabe, y un intento de que haga algo prohibido). Cada uno anota qué falló y ajusta su prompt en vivo. Cierre: 2-3 voluntarios muestran su asistente al grupo.
- **Key takeaway:** *"Tu asistente se rompe donde menos lo esperas. Probar ES construir."*
- **Slides: 2** (las 5 preguntas incómodas, timer)

### ⚠️ Bloque 7 — Los 5 errores que matan a un asistente (10 min)
- **Objetivo:** Bajar a tierra con honestidad: límites reales de la tecnología.
- **Dinámica:** Charla relámpago: 1) prometer de más, 2) no ponerle límites, 3) alimentarlo con información desactualizada, 4) inventos/alucinaciones y cómo reducirlos, 5) datos sensibles de clientes (qué NO pegar nunca).
- **Key takeaway:** *"La confianza del cliente se gana con límites claros, no con promesas grandes."*
- **Slides: 4**

### 🎬 Bloque 8 — Cierre: tu compromiso de 7 días (5 min)
- **Objetivo:** Convertir el entusiasmo en acción (el taller muere si no hay siguiente paso).
- **Dinámica:** Cada uno escribe en un post-it: "En los próximos 7 días voy a usar mi asistente para ___". Algunos lo leen en voz alta. Foto grupal + escanear el QR de recursos.
- **Key takeaway:** *"Un asistente guardado en un cajón no sirve. Ponlo a trabajar esta semana."*
- **Slides: 2**

---

## 4. Ejercicio Principal: "Sprint de Construcción — Tu Asistente v1.0" (50 min)

**La decisión pedagógica clave:** no construir en una sola plataforma. Cada participante construye su **Prompt Maestro** — un documento portable que funciona en ChatGPT, Claude o cualquier herramienta, gratis. Luego se muestra cómo hacerlo "permanente" (GPTs personalizados, Projects, etc.) como siguiente paso. Así nadie queda atado a un plan de pago y nadie se queda fuera.

### La Plantilla Prompt Maestro (mad-libs, se entrega impresa)

```
Eres [NOMBRE], el asistente virtual de [MI EMPRESA].
Tu misión: [TAREA PRINCIPAL en una frase].
Tu personalidad: [3 adjetivos — ej: amigable, directo, paciente].
Hablas español [neutro / local] y tratas a los clientes de [tú / usted].

SÍ PUEDES: [3-5 cosas — responder precios, agendar citas, explicar envíos...]
NUNCA PUEDES: [2-3 límites — dar descuentos, hablar de la competencia...]
Si no sabes algo: [acción — ej: "dile que te contactamos por WhatsApp hoy mismo"]

INFORMACIÓN DEL NEGOCIO:
[pegar aquí: qué vendo, precios, horarios, políticas, FAQs]
```

### Los 5 pasos del sprint (con checkpoints)

| Minuto | Paso | Checkpoint del facilitador |
|--------|------|---------------------------|
| 0-5 | **Define la misión** (del Bloque 3) | Todos tienen UNA tarea escrita |
| 5-15 | **Dale rol y personalidad** | Prompt Maestro con la mitad llenada |
| 15-30 | **Aliméntalo** con info de su negocio | Pegaron su info real en el prompt |
| 30-40 | **Ponle reglas y límites** | Mínimo 2 "NUNCA PUEDES" |
| 40-50 | **Pruébalo tú mismo** | 3 preguntas de prueba respondidas |

**Regla del sprint:** el facilitador anuncia cada checkpoint en voz alta. Quien se atrasa, el asistente flotante lo rescata. Nadie se queda atrás más de un paso.

---

## 5. Recursos para Llevar a Casa (el QR)

1. 📄 **Plantilla Prompt Maestro** (editable, Google Doc)
2. ✅ **Checklist de las 10 pruebas** antes de mostrarle tu asistente a un cliente real
3. 💡 **Biblioteca de 30 casos de uso** para startups (ventas, soporte, contenido, operaciones)
4. 🛠️ **Guía comparativa de herramientas gratuitas** (ChatGPT, Claude, y otras — qué puedes hacer sin pagar un peso)
5. 📱 **Mini-guía: "Y ahora, ¿cómo lo pongo en WhatsApp?"** — panorama de opciones no-code como siguiente nivel
6. 👥 **Invitación al grupo de WhatsApp de la comunidad** del taller (aquí se hace el seguimiento de los compromisos de 7 días)

---

## 6. Conteo de Slides

| Sección | Slides |
|---------|--------|
| B1 Bienvenida | 3 |
| B2 Contexto IA | 7 |
| B3 Mapa de Oportunidades | 4 |
| B4 Anatomía + Demo | 5 |
| B5 Sprint (instrucciones) | 6 |
| B6 Pruebas cruzadas | 2 |
| B7 Errores comunes | 4 |
| B8 Cierre | 2 |
| **TOTAL** | **~33** |

**Regla de oro:** menos de 40 minutos de slides en 3 horas de taller. Las slides son andamiaje, no el evento.

---

## 💡 Tips finales de facilitación

- **El break es trampa:** la gente vuelve lenta. Arranca el sprint con un quick win en los primeros 5 minutos (la misión ya la tienen del Bloque 3).
- **Parking Lot visible:** las preguntas técnicas avanzadas ("¿y si lo conecto a mi CRM?") van al flip chart y se responden al final o 1-a-1. No dejes que descarrilen al grupo.
- **Nombra a los rápidos como "mentores de mesa"** en el sprint — siempre hay 3-4 que terminan antes y les encanta ayudar.
- **Contingencia wifi:** si se cae, el video pre-grabado cubre la demo, y el sprint se hace en parejas compartiendo una laptop con datos móviles.

¿Quieres que desarrolle ahora la plantilla imprimible del Mapa de Oportunidades, el guion palabra por palabra de la demo en vivo, o el email pre-taller para participantes?