# Qwen 3.7 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 7.64 | quality: 8.0
- latency_total: 35.822s | tokens_per_second: 91.7
- input_tokens: 179 | output_tokens: 3285

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Este es el experimento diseñado para **matar la hipótesis**, no para acariciarla. No requiere código, no depende de supuestos ni de encuestas. Mide comportamiento real con dinero en juego.

---

### 🔪 Nombre: `Test del Depósito Refundable de $20`
**Objetivo:** Medir disposición real a pagar $200/mes por automatización de reportes antes de escribir una sola línea de código.
**Principio:** Si no arriesgan $20 hoy, no pagarán $200 mañana. Las opiniones mienten; los depósitos no.

---

### 🛠️ Qué hacer (paso a paso)

| Día | Acción | Detalle |
|-----|--------|---------|
| 1-2 | **Define tu buyer persona exacto** | Agencias de marketing de 2-8 personas que gestionen ≥3 clientes activos. Busca en LinkedIn, Directorios de agencias, o comunidades como r/agencies. |
| 2-3 | **Monta una landing de 1 página** | Usa Carrd o Gumroad ($19/año). Incluye: titular claro, 3 bullets sobre tiempo ahorrado, 1 mockup estático (Figma/Canva), precio `$200/mo`, botón `"Reservar acceso beta"`. Al hacer clic: pide nombre, email y un pago de `$20 (refundable si no se entrega o cambias de idea)`. |
| 3-5 | **Escanea y personaliza outreach** | Recopila 50 contactos. Envía 3 mensajes (email + LinkedIn) con secuencia de 10 días. Ejemplo:<br>`"Hola [Nombre], veo que manejan reportes para varios clientes. Estoy construyendo una herramienta que reduce ese trabajo de horas a minutos. Cobrará $200/mo. ¿Te interesaría asegurar una plaza beta a cambio de un depósito refundable de $20? Sin compromiso."` |
| 6-10 | **Cierra llamadas o cobra** | Quienes respondan positivo → agenda llamada de 10 min. Durante la llamada: muestra el mockup, explica el flujo, pregunta qué herramienta usan ahora y cuánto les cuesta en tiempo. Luego envíales el link de pago. **Si no pagan en 24h, no cuentan.** |
| 11 | **Analiza y decide** | Cruza datos contra los criterios de muerte (abajo). Si fallas → abandona. Si superas → construye. |

---

### 💰 Costo real
- Dominio + Carrd Pro: ~$15-20
- Herramienta de búsqueda (manual o 50 créditos de Apollo): $0-15
- Stripe/PayPal fees: solo si pagan ($0.50+$0.29 por transacción)
- **Total máximo: <$40 USD**
- **Tiempo total: 7-10 días** (sin contar tiempo muerto de espera)

---

### ☠️ Criterios de muerte (CONCLUSIVOS)
Abandona inmediatamente si ocurre **cualquiera** de esto:

1. **< 3 de 50 contactados pagan el depósito de $20** (tasa de conversión < 6%).  
   *Razón:* En B2B frío, un 6% que pone dinero real indica dolor real + percepción de valor. Menos de eso = precio demasiado alto, problema no prioritario, o solución mal enfocada.
2. **> 70% de quienes hablan contigo dicen explícitamente:**  
   - `"Ya uso Excel/Looker Studio gratuito y me basta"`  
   - `"No pagaría más de $30-50/mo por esto"`  
   - `"Los clientes no pagan extra por reportes bonitos, solo quieren resultados"`  
   *Razón:* Confirman que la propuesta de valor no justifica $200/mo o que el mercado ya tiene alternativas gratuitas/low-cost aceptadas.
3. **Ninguno te pide funcionalidades específicas o integración con sus herramientas actuales.**  
   *Razón:* Si no hay urgencia operativa, es un "nice-to-have", no un "must-pay".

---

### 📉 Por qué este experimento mata hipótesis mejor que cualquier encuesta o MVP
- Elimina el sesgo de aceptación social (`"sí, suena genial"` ≠ `"aquí va mi tarjeta"`).
- Filtra curiosos, competidores y agentes de IA. Solo quedan usuarios con piel en el juego.
- Te obliga a vender antes de construir: si no puedes cerrar 3 pagos con un mockup y un email, no vas a cerrar pagos con un producto terminado.
- El umbral de 3 depósitos es estadísticamente significativo para validar señal temprana sin sobreajustar.

---

### ✅ Si sobrevive
Tienes 3-5 clientes potenciales comprometidos. Construye el mínimo viable (integración con Sheets/Drive + exportación PDF/Link) en 2 semanas. Entrega manualmente durante 1 mes. Si renuevan a $200/mo tras la experiencia real, entonces sí tienes negocio.

---

**Regla de oro:** Si en 10 días no has cobrado al menos $60 en depósitos, apaga las luces. No eres malo vendiendo; la hipótesis es falsa. Ganas 2 meses y evitas quemar plata y crédito.

¿Quieres el copy exacto del email de outreach y la estructura de la landing en 1 hora? Dímelo y te lo entrego listo para copiar-pegar.