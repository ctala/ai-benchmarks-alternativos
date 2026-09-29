# Qwen 3.8 Omni Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `qwen/qwen3.8-omni-flash`
- success: True  | final: 6.94 | quality: 8.0
- latency_total: 328.314s | tokens_per_second: 46.9
- input_tokens: 217 | output_tokens: 15399

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Bien. Lo que necesitas no es “validar interés”. Necesitas un **pago o muerte**.

Tu hipótesis se mata si **ninguna agencia pequeña calificada paga $200 reales** por obtener reportes automatizados, aunque se los entregues manualmente en 72 horas.

## Experimento: “Piloto pagado manual” / concierge smoke test

**Idea central:**  
No construyas la herramienta. Vende el resultado por $200/mes, con entrega manual, transparente, rápida y reembolsable si no cumples. Si nadie paga, matas la hipótesis sin codear.

| Item | Detalle |
|---|---|
| Duración | 5 días hábiles, máximo 7 |
| Costo en plata | $0–$100 USD |
| Costo en tiempo | 12–20 horas |
| Muestra mínima | 30 agencias calificadas, 10–12 llamadas de venta con precio |
| Oferta | $200 el primer mes, entrega manual en 72h, cancelable, devolución si no entregas lo acordado |
| Métrica de muerte | 0 pagos con tarjeta después de 10+ demos calificadas |
| Qué NO haces | Encuestas, waitlist, demo gratis sin pago, construir MVP, pedir “opinión” |

---

# 1. Convierte la hipótesis en algo falsable

Tu hipótesis original:

> “Las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.”

Versión operacional para matarla:

> “Si contacto agencias pequeñas calificadas y les ofrezco reportes mensuales automatizados por $200 el primer mes, con entrega manual en 72h, al menos algunas pagarán con tarjeta. Si 0 de 10 llamadas calificadas pagan, la hipótesis está muerta para este segmento/precio/posicionamiento.”

Importante: esto prueba **willingness to pay por el resultado**, no todavía que quieran una herramienta self-service. Por eso agregaremos una pregunta clave en la llamada.

---

# 2. Qué preparar en el Día 1

Meta: tener todo listo en 3–5 horas.

## A. Crea una página simple, no un producto

Puedes usar Carrd, Notion, Framer, Google Sites o incluso un PDF bien armado.

La página debe decir claramente:

**Headline:**

> Reportes mensuales para tus clientes, sin que tu equipo los arme manualmente.

**Subheadline:**

> Piloto para 3 agencias pequeñas: $200 USD el primer mes.  
> Nosotros configuramos y entregamos dashboard/PDF en 72 horas.  
> No es un software maduro todavía: es un servicio manual con plantilla.  
> Cancelable. Devolución si no entregamos lo acordado.

**Qué incluye:**

- Hasta 5 clientes/cuentas activas.
- Datos desde Google Ads, Meta Ads, GA4, Search Console, CRM o CSV.
- Reporte mensual en dashboard + PDF exportable.
- Métricas base: gasto, impresiones, clics, conversions, CPL/CPA, ROAS si aplica.
- Entrega en 72 horas hábiles después de recibir accesos o archivos.
- 1 ronda de ajustes.

**Botón:**

> Pagar $200 e iniciar piloto

No pongas “Registrarme”, “Unirme a waitlist” ni “Quiero saber más”.  
Pon **pagar**.

## B. Graba un Loom de 4–6 minutos

No construyas automatización real. Solo muestra el resultado.

Puedes usar datos demo o anonymizados.

Estructura del video:

1. “Esto es lo que recibiría tu cliente.”
2. Muestra un dashboard o PDF ejemplo.
3. Explica: “Hoy esto lo hacemos manualmente usando plantillas, pero el resultado es el mismo: reportes listos sin que tu equipo pierda horas.”
4. Cierra: “Si quieres, podemos montar tu primer reporte en 72 horas por $200.”

Transparencia obligatoria:

> “No te voy a vender un SaaS terminado. Es un piloto manual. Si funciona, lo escalamos; si no, cancelas.”

Eso aumenta credibilidad y filtra curiosos.

## C. Crea un link de pago real

Usa Stripe, PayPal, Mercado Pago, Wompi, Culqi, etc. Lo importante: **pago con tarjeta o transferencia inmediata**, no “luego te paso los datos”.

Descripción del pago:

> Piloto mensual de reportes automatizados para agencias.  
> $200 USD.  
> Entrega manual en 72h hábiles tras recibir datos/accesos.  
> Hasta 5 clientes.  
> Cancelable.  
> Devolución si no entregamos lo acordado.

Si no puedes cobrar con tarjeta por tu país, usa el método de pago local más frictionless posible. Pero tiene que ser dinero real.

## D. Haz una lista de 75 agencias pequeñas

No necesitas 1,000 leads. Necesitas 75 bien dirigidos para conseguir 10–15 llamadas útiles.

Perfil calificado:

- Agencia de marketing digital, ads, SEO, social media, performance, content, growth.
- Entre 1 y 15 empleados.
- Dueño o manager toma la decisión.
- Tiene clientes recurrentes con reportes mensuales.
- Actualmente arma reportes manualmente o con planillas.
- Probablemente pierde 2–10 horas al mes por cliente o en consolidación.

Fuentes:

- LinkedIn.
- Instagram.
- Google Maps.
- Clutch.
- Upwork/Fiverr si venden servicios a agencias.
- Grupos de Facebook/Slack/Discord de dueños de agencias.
- Comunidades locales de marketing.
- Agencias que ya usan Looker Studio, AgencyAnalytics, DashThis, Swydo, etc., pero podrían estar insatisfechas.

Guarda en un Google Sheet:

| Campo | Ejemplo |
|---|---|
| Agencia | XYZ Ads |
| Contacto | Juan Pérez |
| Cargo | Founder |
| Canal | LinkedIn |
| Clientes aprox. | 8 |
| Horas reporte/mes | 6 |
| Calificada? | Sí |
| Llamada agendada? | Sí |
| Demo mostrada? | Sí |
| Precio presentado? | Sí |
| Objeción principal | “Está caro” |
| Pago? | No |
| Motivo | No urgente |

---

# 3. Outreach: Días 2 a 4

No pidas “feedback”. Ofrece un piloto pagado.

## Mensaje inicial, frío o semicálido

Asunto si es email:

> Piloto de reportes para agencias: $200/mes, entrega en 72h

Cuerpo:

> Hola [nombre],  
>   
> Vi que [agencia] maneja cuentas de [sector/tipo de cliente].  
>   
> Estoy tomando 3 agencias para un piloto de reportes mensuales automáticos: ustedes nos dan acceso o un CSV, y nosotros entregamos dashboard + PDF en 72 horas.  
>   
> Es un piloto manual, no un software terminado. Cuesta $200 el primer mes, es cancelable y devuelvo la plata si no entrego lo acordado.  
>   
> Si te interesa, te muestro un demo de 8 minutos. ¿Tienes espacio mañana o pasado?

Si es DM:

> Hola [nombre], hago un piloto para agencias pequeñas: reportes mensuales automáticos para clientes, entregados en 72h. Es manual al inicio, $200 el primer mes, cancelable. ¿Te muestro un demo corto de 8 min?

## Follow-up 1, 48 horas después

> Hola [nombre], solo confirmo si viste el mensaje.  
>   
> El piloto es simple: tú sigues vendiendo, nosotros armamos los reportes.  
>   
> Si no es prioridad, me dices “no” y lo cierro sin problema.

## Follow-up 2, último día

> Cierro cupos del piloto hoy a las [hora].  
>   
> Si quieres entrar, te paso el link de pago y el formulario de accesos.  
>   
> Si no, igual agradezco la respuesta.

Regla: si dicen “me interesa” pero no agendan o no pagan, cuenta como **no**.

---

# 4. La llamada: 15 minutos maximum

Objetivo: diagnosticar, mostrar demo, decir precio, pedir pago.

No hagas discovery eterno. Estás vendiendo, no investigando por cortesía.

## Script

### 1. Framing, 1 minuto

> Gracias por la llamada.  
>   
> No vengo a venderte un software terminado. Estoy buscando 3 agencias para un piloto manual de reportes.  
>   
> La idea es simple: tú me das acceso o datos de tus clientes, yo te devuelvo un dashboard/PDF listo para enviar, en 72 horas.  
>   
> Cuesta $200 el primer mes. Si no entregamos lo acordado, devolución.  
>   
> ¿Te parece si reviso rápidamente cómo hacen hoy los reportes y te muestro cómo quedaría?

### 2. Diagnóstico rápido, 4–5 minutos

Pregunta:

- ¿Cuántos clientes activos reportan mensualmente?
- ¿Quién arma los reportes hoy?
- ¿Cuántas horas toma por cliente o en total al mes?
- ¿Usan planillas, Looker Studio, AgencyAnalytics, PDFs, PowerPoint?
- ¿Qué parte duele más: juntar datos, diseñar, explicar, aprobar, enviar?
- ¿Han probado alguna herramienta? ¿Por qué no funciona?
- ¿Si esto les ahorrara 5 horas al mes, valdría $200?

No aceptes respuestas vagas. Si dicen “depende”, profundiza:

> “¿Hoy perderías una tarde entera armando reportes o es algo de 30 minutos?”

### 3. Demo, 3 minutos

Muestra el Loom o pantalla compartida.

Di:

> Esto es lo que recibirías.  
>   
> Hoy esto lo hacemos manualmente con plantillas.  
>   
> La versión futura sería una herramienta, pero para el piloto nosotros hacemos el trabajo pesado.

### 4. Pregunta clave para matar la hipótesis de “herramienta”

Agrega esto:

> Importante: el piloto es manual.  
>   
> Pero quiero entender si te interesa más:  
> A) una herramienta para que tu equipo la use y genere reportes solos, o  
> B) un servicio donde nosotros te entregamos los reportes listos.  
>   
> ¿Cuál prefieres?

Interpretación:

- Si quieren A pero no pagan: hipótesis de herramienta muerta por precio/valor.
- Si solo quieren B: puede haber negocio de servicio/productizado, pero no necesariamente SaaS.
- Si dicen “me da igual, solo quiero que salga bien”: posible señal de que comprarían outcome, no tool.

### 5. Precio y cierre, 2 minutos

> El piloto cuesta $200 por el primer mes.  
>   
> Incluye hasta 5 clientes, dashboard + PDF, 1 ronda de ajustes y entrega en 72 horas hábiles después de recibir datos/accesos.  
>   
> Si no entregamos lo acordado, te devuelvo la plata.  
>   
> ¿Te paso el link de pago para arrancar hoy?

Si dicen “lo pienso”:

> Perfecto. Para no hacerte perder tiempo: ¿lo que te frena es el precio, la confianza, el momento o que no ves el dolor suficiente?

No regales descuentos. No bajes a $99. Si bajás el precio, ya no estás testeando la hipótesis original.

Si dicen “está caro”:

> Entendido. Este piloto es a $200 porque implica trabajo manual. Si para ti el valor no llega a ese monto, mejor no lo forzamos.  
>   
> ¿Aproximadamente cuánto pagarías si te ahorra X horas al mes?

Anota el número. Si todos dicen $50, tu hipótesis de $200 está muerta, aunque exista otro negocio.

Si dicen “confío en ti pero no tengo presupuesto ahora”:

> Ok. ¿Significa que no pagarías $200 aunque el reporte te ahorre tiempo, o que es solo timing?

Si es timing, no cuenta como validación fuerte. Si es “no tengo presupuesto para esto”, señal de muerte.

---

# 5. Resultado que te hace abandonar la idea

## Criterio de muerte principal

Abandonas la idea de construir la herramienta durante 2 meses si se cumplen todas estas condiciones:

1. Contactaste al menos **75 agencias** con perfil calificado.
2. Conseguiste al menos **10 llamadas** con dueños o decisores reales.
3. En esas 10 llamadas:
   - Mostraste el demo.
   - Dijiste claramente **$200/mes**.
   - Ofreciste entrega manual en 72h.
   - Enviaste link de pago.
4. Resultado: **0 pagos con tarjeta/transferencia confirmada**.

Entonces:

> **Mata la hipótesis. No construyas.**

No necesitas más pruebas. Si 10 compradores potenciales calificados ven el resultado, entienden el precio y aun así no pagan, el problema no es el código. Es valor, precio, segmento, urgencia o confianza.

## Criterio de muerte anticipada

Puedes matar antes si en 8–10 llamadas calificadas ocurre esto:

- 0 pagos.
- 7 o más dicen que hoy resuelven reportes en menos de 1 hora total al mes.
- O usan una herramienta gratuita/barata que ya les sirve.
- O el dueñno no siente dolor, solo cortesía.
- O todos piden descuento fuerte sin compromiso.

Eso indica que el problema no es suficientemente caro.

## Lo que NO cuenta para matar

No mates la hipótesis si:

- No conseguiste llamadas.
- Solo hablaste con marketers junior que no deciden presupuesto.
- No mostraste precio.
- Ofrecest free trial sin tarjeta.
- Solo tuviste gente curiosa.
- Tu mensaje fue genérico y nadie respondió.

Eso es fallo de canal o mensaje, no necesariamente fallo de willingness to pay.

En ese caso, itera outreach por 2–3 días más. Pero sigue sin construir.

---

# 6. Cómo interpretar los resultados

## Escenario A: 0 pagos

**Decisión:** abandonar la hipótesis tal como está.

No construyas la herramienta.

Posibles lecturas:

- $200 es demasiado para ese segmento.
- El dolor no es suficiente.
- Ya tienen solución acceptable.
- Prefieren done-for-you, no software.
- No confían en un piloto nuevo.
- El reporte no es un problema prioritario.

Siguiente experimento posible, no construcción:

- Bajar precio? No automáticamente. Primero entender si el problema existe.
- Vender como servicio productizado a otro precio.
- Atacar otro segmento: agencias más grandes, freelancers, consultores, e-commerce internos.
- Resolver otro dolor: propuesta comercial, onboarding de clientes, dashboards en vivo, alertas, white-label.

Pero la hipótesis original muere.

## Escenario B: 1 o 2 pagos

**Decisión:** no construir todavía. Hacer concierge.

Con 1–2 pagos no matas la hipótesis, pero tampoco justificas 2 meses de desarrollo.

Haz esto:

- Entrega manualmente.
- Mide cuánto tiempo te toma por cliente.
- Pide feedback semanal.
- Observa si usan el reporte con sus clientes.
- Pregunta si renovarían el segundo mes.
- Intenta vender 3 más con ese aprendizaje.

Mata después si:

- No renuevan.
- No usan los reportes.
- Te toman más de 2–3 horas por cliente.
- Solo querían “que se los hagas tú” y no pagarían por herramienta.
- El churn del primer mes es alto.

## Escenario C: 3 o más pagos de agencias calificadas no amigas

**Decisión:** continuar, pero todavía sin construir el producto completo.

Esa es señal de que al menos hay willingness to pay por el outcome.

Siguiente paso:

- Vender 10 pilotos manuales.
- Estandarizar el proceso.
- Automatizar solo lo más repetitivo con no-code/scripts internos.
- Construir MVP solo cuando tengas 10 clientes pagando y el proceso manual sea claro.

Regla dura:

> No escribas código de producto hasta que hayas entregado manualmente al menos 10 reportes pagados y sepas exactamente qué parte duele automatizar.

---

# 7. Costo exacto recomendado

## Opción ultra barata: $0

- Google Sites o Notion: $0.
- Loom free: $0.
- Stripe/PayPal: $0 upfront, solo fees.
- Outreach manual: $0.
- Google Sheets: $0.

Costo cash: **$0**.  
Costo tiempo: **12–18 horas**.

## Opción rápida y profesional: hasta $100

- Dominio: $10–15.
- Carrd Pro: $19/año.
- Loom: $0–15.
- Email finder o LinkedIn Sales Navigator trial: $0–50.
- Stripe fees: solo si cobran.

Costo cash recomendado: **$50–$80**.  
Tiempo: **5 días**.

No gastes en ads todavía. Ads sin mensaje validado queman plata. Primero outreach directo.

---

# 8. Calendario concreto de 5 días

## Día 1: Setup

Tararea:

- Definir oferta.
- Crear página.
- Grabar Loom.
- Crear link de pago.
- Armar lista de 75 agencias.
- Preparar sheet de tracking.

Tiempo: 4–6 horas.

## Día 2: Outreach oleada 1

- Enviar 30 mensajes personalizados.
- Hacer 2–3 llamadas si caen.
- Follow-ups.

Tiempo: 3–4 horas.

## Día 3: Outreach oleada 2

- Enviar 30 mensajes más.
- Hacer llamadas.
- Segundo follow-up.

Tiempo: 3–4 horas.

## Día 4: Llamadas y cierre

- Hacer 5–8 demos.
- Enviar links de pago.
- Follow-up mismo día.

Tiempo: 3–5 horas.

## Día 5: Último intento

- Hacer llamadas restantes.
- Enviar mensaje final con deadline.
- Cerrar experimento.

Tiempo: 2–4 horas.

Total: **15–23 horas**, dependiendo de tu red y velocidad.

---

# 9. Errores que invalidarían el experimento

No cometas estos.

## Error 1: Encuesta

“¿Pagarías $200?”  
Respuesta típica: “Sí, claro.”  
Realidad: nadie paga.

Inútil para matar.

## Error 2: Waitlist

“Deja tu email.”  
No prueba pago. Solo prueba curiosidad.

## Error 3: Demo gratis sin tarjeta

Puedes tener 50 demos y 0 clientes.

## Error 4: No decir precio

Si no mencionas $200, no estás testeando la hipótesis.

## Error 5: Aceptar “me interesa”

“Me interesa” no es dinero.

Solo cuenta:

- Pago confirmado.
- Tarjeta procesada.
- Transferencia recibida.
- Contrato firmado con depósito, si no puedes cobrar online.

## Error 6: Hablar con personas equivocadas

Si hablas con coordinadores sin presupuesto, no mataste la hipótesis. Mataste tu outreach.

## Error 7: Construir el demo demasiado

No pases 2 días haciendo un dashboard perfecto.  
Un Loom feo pero claro basta.

## Error 8: Descuentos inmediatos

Si todos dicen “está caro” y tú bajas a $99, ya no sabes si la hipótesis original era falsa o solo tu pricing era rígido.

Primero testa $200. Después, si hay señal, explora otros precios.

---

# 10. Tu regla de decisión final

Imprime esto mentalmente:

> Si después de 10 llamadas con dueños de agencias pequeñas calificadas, mostrando demo, diciendo $200/mes y ofreciendo entrega manual en 72h, consigo **0 pagos**, no construyo nada.

Ese es el resultado que te hace abandonar.

Y si consigues 1 o 2 pagos:

> Tampoco construyas. Cobra, entrega manualmente, mide renovación y solo desarrolla si el dolor se repite y el proceso es rentable.

El objetivo no es tener razón. El objetivo es descubrir barato que estabas equivocado.  
Este test te puede cost menos de $100 y menos de una semana, y te evita 2 meses de construcción ciega.