# MiniMax M3 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.54 | quality: 8.4
- latency_total: 31.158s | tokens_per_second: 75.8
- input_tokens: 321 | output_tokens: 2363

## Respuesta completa

# El Experimento: "Vende Antes de Construir"

Tu hipótesis tiene **dos partes** que pueden morir por separado:
1. ¿El problema existe y duele? (fácil de testar)
2. ¿Pagan $200/mes por resolverlo? (donde muere el 80% de las hipótesis)

La trampa clásica es validar solo (1) con preguntas tipo "¿usarías esto?" → todos dicen sí. Eso no vale nada. Necesitas que **saquen la tarjeta**.

---

## El protocolo exacto (5 días)

### Día 1-2: Caza y criba (4 horas/día)

- Entra a LinkedIn, busca: *"fundador"* + *"agencia de marketing"* + filtros de empleados (1-10)
- Envía 50 mensajes directos con este guion (copia y pega, adapta):

> *"Hola [nombre], estoy validando una herramienta. ¿Tienes 10 min esta semana para una videollamada? Te regalo una Starbucks card de $10 aunque no participes."*

- Meta: agendar 15 llamadas con dueños/socios (no empleados junior, no project managers)
- Si no consigues 15 calls, **la hipótesis ya está herida**: no hay densidad de mercado suficiente

**Costo:** $150 en Starbucks cards (solo si cumples el compromiso)
**Tiempo:** 2 días

---

### Día 3-4: Las 15 llamadas (45 min cada una)

Estructura de cada llamada, en este orden estricto:

**Parte A — Problema (10 min, NO menciones tu herramienta todavía)**
- "¿Cómo le reportas resultados a tus clientes hoy?"
- "¿Cuántas horas al mes dedicas a esto?"
- "¿Qué herramienta usas?" *(anota qué usan hoy)*
- "¿Alguna vez perdiste un cliente por reportes malos o lentos?"

**Si el problema no es vívido y recurrente → KILL.**

**Parte B — Solución (10 min, describe el producto)**
- "Te enseño algo en lo que estoy trabajando: automatiza los reportes a clientes, conecta tus fuentes (Meta Ads, Google Ads, GA4), genera un PDF blanco con tu marca, lo manda solo cada lunes."
- "¿Eso te serviría?"

**Si dicen "suena bien, pero ahora no tengo tiempo / no es prioridad" → KILL.**

**Parte C — El precio real (15 min, AQUÍ ES DONDE MUERE LA HIPÓTESIS)**
- "Sería $200/mes. Si te dijera que está listo hoy, ¿lo comprarías?"
- **Silencio. Espera.** No llenes el silencio.
- Si dicen "depende" → "¿Depende de qué? Dame el peor caso."
- Si dicen "sí" → "Puedo reservarte un precio de fundador de $150/mes de por vida si me das tu tarjeta ahora y empiezas en cuanto lo lance en 6 semanas. ¿Arrancamos?"

---

### Día 5: El veredicto

Mira los números y aplica los criterios de abajo.

---

## Los criterios de muerte

| Resultado | Veredicto |
|---|---|
| **0-1 de 15 calls dicen "sí, te doy la tarjeta"** | **KILL.** $200 es demasiado, o el problema no es agudo. |
| **2-3 dicen sí, pero solo a $50-80/mes** | **KILL.** Tu economics no funcionan a ese precio. |
| **3-5 dicen sí a $200, pero solo "cuando esté listo"** | **Casi KILL.** Estás en territorio de "pala, no pico". Construye cuando 3 firmen. |
| **5+ firman con tarjeta o LOI firmado** | **Sigue adelante.** La hipótesis vive. |
| **La mayoría ya usa AgencyAnalytics, Whatagraph, Dashthis o similar** | **KILL.** Mercado saturado a precios más bajos. |
| **Dicen "mi VA lo hace en Google Sheets"** | **KILL.** No van a pagar por algo que resuelven con $5/hora. |

---

## Costo total

| Concepto | Monto |
|---|---|
| Starbucks cards | $150 |
| Tu tiempo (~50 horas) | $0 (pero es tu costo de oportunidad) |
| Zoom / calendario | $0 |
| **Total** | **$150 + 1 semana** |

---

## Las trampas que te van a tentar a autoengañarte

1. **"Me dijeron que sería útil"** → No es señal. Útil ≠ Pagar.
2. **"Sí lo usaría, suena interesante"** → Calor de llamada, no dinero.
3. **"Vuelve cuando esté listo"** → No van a volver. Es un "no" educado.
4. **"El precio está bien para lo que hace"** → Dijo "está bien", no "lo compro".

La única señal válida es: **tarjeta de crédito, transferencia, o LOI firmado.**

---

## Si la hipótesis muere, no perdiste nada

Perdiste 1 semana y $150. Lo que te ahorraste: 2 meses de construcción que descubren que el mercado no quería tu producto. Eso es un retorno de 1000x en tiempo y plata.

**Ve a vender hoy, no a construir.**