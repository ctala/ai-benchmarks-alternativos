# GPT-5.6 Terra — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 6.67 | quality: 8.0
- latency_total: 45.854s | tokens_per_second: 88.6
- input_tokens: 167 | output_tokens: 4061
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y práctico para validar la hipótesis de manera efectiva.

## Respuesta completa

## Experimento: venderlo antes de construirlo

No hagas una encuesta. No recojas “interés”. No pidas cartas de intención.

La única señal que importa para esta hipótesis es:

> Una agencia paga **$200 hoy** por empezar, aunque el producto esté en beta y el primer mes tenga intervención manual.

### Hipótesis exacta a matar

No puedes probar “las agencias pequeñas” en general. Hazla falsable:

> Agencias de performance de 2–15 personas, con 5–20 clientes activos y que hoy invierten al menos 3 horas/mes en reportes de Meta Ads, Google Ads y GA4, pagarán $200/mes por reportes automatizados y con su marca.

---

# La oferta que vas a vender

No construyas software. Vende un **beta concierge**, siendo totalmente transparente.

### Oferta

> “Reportes de cliente listos para enviar, con tu marca, conectando Meta Ads, Google Ads y GA4.  
> $200/mes por agencia, hasta 10 clientes.  
> Primer reporte entregado en 7 días.  
> Estamos en beta: el onboarding y algunos pasos pueden tener intervención manual al principio, pero el resultado para tus clientes será el reporte final.”

No digas que está automatizado si todavía no lo está. Di que estás vendiendo el resultado y que la operación inicial es parcialmente manual.

### Condiciones

- Cobro: **$200 por adelantado** vía Stripe.
- Sin descuento de “founder”.
- Sin prueba gratis.
- Puedes ofrecer garantía ética: “Si no entregamos el primer reporte en 7 días, devolvemos el dinero.”
- El pago solo cuenta si:
  1. Pagan los $200.
  2. Agendan onboarding.
  3. Mantienen el pago al menos 7 días.

Un “sí, me interesa”, “mándame información” o “cuando esté listo lo veo” cuenta como **no**.

---

# Qué haces exactamente

## Día 1: prepara el mínimo material — 3 horas

### 1. Haz una landing de una página

En Notion, Carrd o Google Doc. No diseñes una web completa.

Incluye:

- Titular:  
  **“Reportes de marketing para clientes, listos para enviar sin perder horas cada mes.”**
- Para quién: agencias de performance de 2–15 personas.
- Qué cubre: Meta Ads, Google Ads, GA4.
- Resultado: reporte mensual/semanal con branding de la agencia.
- Precio visible: **$200/mes, hasta 10 clientes.**
- Estado: “Beta limitada a 5 agencias.”
- Botón: **“Empezar beta — $200/mes”**, conectado a Stripe Payment Link.
- Un mockup de reporte hecho en Canva/Figma/Google Slides con datos ficticios y marcado como ejemplo.

No necesitas login, integraciones ni dashboard.

### 2. Crea el link de pago

Stripe Payment Link:

- Producto: “Beta — reportes automatizados para agencias”
- Precio: $200/mes
- Renovación mensual
- Garantía: primer reporte en 7 días o devolución

### 3. Define tu lista de prospectos

Busca **60 agencias**, no 60 marketers individuales.

Criterios:

- 2–15 empleados.
- Hacen paid media / PPC / performance.
- Tienen servicios de Meta Ads, Google Ads o analítica.
- Fundador, director de operaciones o head de client services accesible.
- Preferentemente con 5+ clientes.

Fuentes gratuitas:

- LinkedIn.
- Google Maps: “agencia Google Ads”, “agencia performance”.
- Clutch.
- Tu red, exclientes, freelancers de paid media.
- Pide 10 introducciones directas a gente que conozca dueños de agencia.

---

## Días 2–5: consigue 15 conversaciones calificadas — 5 a 7 horas

Envía mensajes personalizados a los 60 prospectos. Tu objetivo no es “hacer volumen”; es conseguir conversaciones con personas que pueden pagar.

### Mensaje de outreach

> Hola, [Nombre]. Vi que [Agencia] gestiona campañas de [Meta/Google] para clientes.  
>   
> Estoy probando una beta para agencias que quieren dejar de montar reportes manuales: entregamos reportes con branding de la agencia a partir de Meta Ads, Google Ads y GA4 por $200/mes.  
>   
> No busco feedback genérico: estoy buscando 5 agencias dispuestas a pagar y usarlo este mes.  
>   
> ¿Hoy cuánto tiempo os lleva preparar reportes de clientes? Si es más de 2–3 horas al mes, ¿te va una llamada de 15 minutos esta semana?

Haz follow-up 48 horas después:

> Te escribo una vez más porque cierro las plazas beta esta semana. Si los reportes no son un dolor relevante ahora, no insisto.

No uses publicidad. Un anuncio mide curiosidad y clics; no voluntad de pago. Además cuesta más y tarda más.

---

## En cada llamada: 15 minutos, sin entrevista complaciente

Primero califica. Pregunta:

1. “¿Cuántos clientes activos reportáis cada mes?”
2. “¿Qué fuentes incluís?”
3. “¿Quién prepara los reportes hoy?”
4. “¿Cuántas horas os lleva al mes?”
5. “¿Qué pasa cuando se retrasa o sale mal un reporte?”
6. “¿Usáis alguna herramienta? ¿Cuánto pagáis?”
7. “¿Tú puedes decidir una compra de $200/mes?”

Solo sigue con el pitch si:

- Tienen al menos 5 clientes.
- Hacen reportes recurrentes.
- El decisor está presente.
- El problema les consume tiempo real.

### Cierre literal

> Por lo que me cuentas, esto os ahorraría aproximadamente [X] horas al mes y evitaría [dolor citado].  
>   
> La beta cuesta $200/mes, hasta 10 clientes. El primer reporte llega en siete días. Al principio habrá onboarding manual, pero no os vendo una demo: os entregamos el resultado.  
>   
> Si quieres entrar, te paso ahora el link de pago y reservamos el onboarding. ¿Lo activamos?

Después, cállate.

No preguntes:

- “¿Lo usarías?”
- “¿Te parece útil?”
- “¿Qué precio pagarías?”
- “¿Quieres que te avise cuando esté?”

Eso solo produce falsos positivos.

---

# Criterio de abandono: defínelo antes de empezar

Haz **20 conversaciones calificadas** con decisores reales.

Tu umbral es:

| Resultado tras 20 conversaciones calificadas | Decisión |
|---|---|
| **0–2 pagos reales de $200** | **Abandona la hipótesis.** No construyas 2 meses de producto. |
| **3 pagos reales** | No construyas aún. Haz el servicio manual durante un mes y mide uso, retención y coste de entrega. |
| **4+ pagos reales** | Hay una señal fuerte. Sigue con concierge manual y empieza a identificar qué automatizar primero. |

## El resultado que mata la idea

> Si menos de 3 de 20 decisores calificados pagan $200 por adelantado, abandonas la idea de “herramienta de reportes para pequeñas agencias a $200/mes” para este segmento.

No cambies el precio a mitad del test.  
No amplíes “solo cinco conversaciones más”.  
No conviertas un “quizá” en una venta.

Si obtienes 0–2 pagos, puedes guardar las objeciones para una idea futura, pero no le regales dos meses de construcción a una hipótesis que no logró venderse manualmente.

---

# Coste y tiempo

## Dinero

| Concepto | Coste |
|---|---:|
| Notion / Google Docs / Calendly | $0 |
| Canva / Figma | $0 |
| Stripe | $0 hasta cobrar; luego comisión por pago |
| Dominio opcional | $10–15 |
| LinkedIn, email y llamadas manuales | $0 |
| **Total** | **$0–15** |

## Tiempo

| Actividad | Tiempo |
|---|---:|
| Landing, mockup y Stripe | 3 horas |
| Lista de 60 agencias | 2–3 horas |
| Outreach y follow-ups | 2 horas |
| 20 llamadas de 15 min | 5 horas |
| Seguimiento y cobro | 1–2 horas |
| **Total fundador** | **13–15 horas** |
| **Duración calendario** | **5–7 días** |

---

# Qué no valida este experimento

Incluso si logras 3 pagos, todavía no has validado que debas construir software.

Solo has validado algo más importante:

> Algunas agencias pagan $200 por el resultado de eliminar trabajo de reporting.

Luego debes entregar manualmente o con herramientas existentes a esos clientes durante 30 días y medir:

- ¿Usan los reportes?
- ¿Renuevan el segundo mes?
- ¿Cuánto tiempo te toma entregar cada cuenta?
- ¿Qué parte del flujo se repite?
- ¿Qué integración o paso manual genera más trabajo?

Construye únicamente lo que ya estés repitiendo manualmente para clientes que pagan.

Pero primero: intenta que te digan que no con su tarjeta.