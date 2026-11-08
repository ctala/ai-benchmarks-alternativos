# Mistral Large 4.0 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 7.04 | quality: 8.0
- latency_total: 75.826s | tokens_per_second: 56.6
- input_tokens: 172 | output_tokens: 4294

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

No construyas nada. Tu experimento no es un estudio de mercado: **es una venta**. La única forma concluyente de saber si alguien paga $200/mes es pedirle $200 hoy, antes de que exista el producto.

Aquí el experimento completo:

---

## El experimento: "Pre-venta con depósito real" (5 días, <$150)

### Día 1 — Nicho + oferta + lista (3 horas, $0)

**Elige UN nicho hiperespecífico.** "Agencias pequeñas" es muy vago. Elige algo como: *"agencias de publicidad digital de 2–10 empleados en [tu ciudad/país]"* (ej: Meta Ads en Ciudad de México, SEO en Madrid). Mientras más específico, más fácil contactarlos y más real la señal.

**Consigue 60 prospectos gratis:**
- LinkedIn Sales Navigator (prueba gratis 1 mes) → filtra "Owner / Director" + "Marketing & Advertising" + tamaño 2–11 empleados.
- O Google Maps: busca "agencia de marketing" en 3 zonas de tu ciudad, entra a sus webs, saca nombre del dueño y su WhatsApp/LinkedIn.

**Escribe la oferta (copy exacto para landing y mensajes):**

> **"Deja de hacer reportes a mano."**
> Sacamos el reporte mensual a tus clientes automáticamente (metas, gasto, resultados) en 10 minutos.
> **$200/mes. Cancela cuando quieras.**
> Programa founding: solo 5 plazas. Para reservar la tuya pedimos un **depósito de $200 hoy**, que se descuenta 100% de tu primer mes. Si no te sirve, te devolvemos el depósito menos $50 de costo administrativo... *(no, mejor: depósito NO reembolsable. El filtro es el punto).*

**Landing mínima (30 min):** Carrd.co ($19/año) o incluso un Google Form + link de pago. Un solo botón: **"Reservar mi plaza — pagar $200"**. Conecta Stripe, PayPal o MercadoPago. No hace falta que exista el producto: el botón cobra de verdad.

**Costo día 1:** ~$30 (dominio + Carrd) o $0 si usas solo WhatsApp + link de MercadoPago.

---

### Días 2–4 — Outreach + ads (6 horas, ≤$100)

**Canal A (prioridad): 60 mensajes directos** por WhatsApp/LinkedIn/email. Script:

> "Hola [nombre], vi [Agencia X]. Estamos armando una herramienta que saca solo el reporte mensual a clientes y buscamos 5 agencias founding a $200/mes, cancela cuando quieras. Para reservar plaza pedimos depósito de $200 hoy (se descuenta del mes 1). ¿10 min de llamada hoy o mañana? Si no, sin problema."

Haz follow-up a los que no responden a las 24h: *"¿Te sirve un slot el [día] a las [hora]?"*

**Canal B (volumen): $100 en ads** (Facebook/Instagram o LinkedIn) dirigido a dueños de agencias de tu nicho, que lleven a la landing. $50/día × 2 días. No gastes más.

**Regla de oro:** en las llamadas NO hagas demo (no existe). Vende el resultado: *"recuperas tu viernes por la tarde"*. Al final de la llamada, si hay interés, diles: *"perfecto, te mando el link para el depósito de $200, así queda reservado tu slot"*. **Si no pagan en las siguientes 24h, no es un sí.**

---

### Día 5 — Decisión (30 min)

Cuenta: contactados, respuestas, llamadas, **pagos reales en tu cuenta**.

---

## Tabla de costos y tiempo

| Item | Costo | Tiempo |
|---|---|---|
| Lista de 60 prospectos (LinkedIn trial / Maps) | $0 | 1 h |
| Landing + dominio + Carrd | ~$30 | 1 h |
| Ads (2 días) | $100 | 30 min de setup |
| Outreach manual (60 msgs + follow-ups + 10 llamadas) | $0 | 6 h |
| Stripe/MercadoPago | $0 (comisión solo si vendes) | 30 min |
| **TOTAL** | **≤ $130** | **~10 h en 5 días** |

---

## El resultado que MATA la hipótesis (kill criteria)

Abandonas la idea si ocurre **cualquiera** de estos:

1. **Menos de 3 pagos/depósitos de $200 en 7 días**, habiendo contactado ≥60 agencias del nicho + gastado los $100 en ads. (Con 60 contactos fríos + ads, 3 pagos = 5%, que ya es una señal débil para un SaaS de $200/mes con churn; menos que eso = no hay demanda real a ese precio).
2. **Cero pagos** y la objeción dominante es *"ya lo hago gratis con Looker/Excel"* o *"mis clientes no lo valoran"* → el problema no duele lo suficiente.
3. Para cerrar una venta tuviste que bajar a **< $100/mes o "prueba gratis 3 meses"** → la hipótesis de **$200** está muerta (quizás exista a $49, pero esa es otra hipótesis).
4. El costo de adquirir un pago (ads + tu tiempo valorado) **supera los $200** → no hay margen.

**Cuenta como NO, aunque suene positivo:** "me interesa", "mándame info", "hablamos en 2 meses", "después de ver una demo". **Solo cuenta dinero en tu cuenta o una firma + pago inicial.**

---

## Si NO muere (3–5 pagos)

Entonces sí tiene sentido construir — pero **construye solo para quienes ya pagaron** (máximo 5 clientes founding). No inviertas los 2 meses hasta tener esos 3–5 pagos comprometidos. El producto se convierte en "cumplir lo vendido", no en una apuesta.

---

## Versión ultra-mínima (48 h, $0) si quieres matar la duda ya

Manda 20 mensajes con el script de arriba + link de pago de $200. Si **0 de 20 pagan**, la hipótesis está Practically muerta. Si 1–2 pagan, amplía a 60 y ads.

---

**La trampa que debes evitar:** no caigas en "necesito mostrarles el producto para que vean el valor". Eso es construir para validar. Aquí vendes la promesa con dinero real de por medio. Si nadie pone $200 sobre la mesa en 5 días, estabas equivocado, y te ahorraste 2 meses.

¿Qué nicho vas a atacar primero? Con eso te ayudo a armar la lista de 60 en 30 minutos.