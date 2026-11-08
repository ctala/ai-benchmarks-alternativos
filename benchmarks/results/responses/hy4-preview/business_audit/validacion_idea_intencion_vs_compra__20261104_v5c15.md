# Tencent Hy4 preview — business_audit/validacion_idea_intencion_vs_compra

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 155.408s | tokens_per_second: 54.0
- input_tokens: 193 | output_tokens: 8387

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un inversor que ha visto morir muchos proyectos por validar mal. Distingues sin piedad entre lo que la gente DICE y lo que la gente PAGA.

**user:**

Creo que ya validé mi idea y quiero renunciar a mi trabajo para dedicarme a esto a tiempo completo. Mis datos:

- Hice una encuesta a 40 personas de mi red.
- El 85% dijo que el problema les duele.
- El 72% dijo que pagaría $30 al mes por una solución.
- Tengo una lista de espera de 210 correos que se anotaron desde una landing page.
- Ingresos hasta hoy: $0. Todavía no cobré nada porque el producto no está listo.

¿Está validado? ¿Renuncio?


## Respuesta completa

Te respondo como inversor, no como amigo: **no, no está validado. Y no, no renuncies con estos datos.**

Lo que tienes hoy no es validación. Es **interés**. Y el interés no paga facturas.

---

## 1. DICE vs. PAGA (la única tabla que importa)

| Lo que tienes | Qué significa en realidad |
|---|---|
| **85% dice que el problema les duele** | Te dijeron que sí a ti, que eres de su red. No han gastado un peso ni una hora en resolverlo. |
| **72% dice que pagaría $30/mes** | Eso es ~29 personas. **0 han pagado.** Decir “pagaría” es gratis. Pagar duele. |
| **210 correos en waitlist** | Dar un email cuesta $0. Es menos compromiso que un like. No es intención de compra. |
| **$0 ingresos** | El mercado no ha votado. Hasta que no haya dinero, no hay negocio. |

Tu métrica real hoy es: **0 de ~29 dijeron que sí y 0 de 210 dieron la tarjeta.**

---

## 2. Por qué tus números te están engañando

**a) Muestra chica y sesgada.**  
Encuestaste a 40 personas de tu red. Te quieren. El 85% es cortesía, no dolor de mercado. Aunque hubieras encuestado a 4.000, si la pregunta es hipotética, sigue siendo humo.

**b) “¿Pagarías?” es la pregunta más inútil de los negocios.**  
La gente es terrible prediciendo su propio comportamiento. Todos decimos que haríamos ejercicio y comeríamos ensalada. Después pedimos pizza.

**c) Una waitlist no es un funnel.**  
210 correos sin tarjeta son 210 “quizás”. La mayoría ni va a abrir tu próximo correo. La conversión típica de waitlist a cliente pagado es 1–5%. Eso significa que 210 correos probablemente sean **2 a 10 clientes**, con suerte.

**d) “Todavía no cobré porque el producto no está listo” es una bandera roja gigante.**  
Esa frase ha matado más startups que la competencia. **No necesitas el producto listo para cobrar.** Necesitas cobrar para saber si vale la pena construirlo. Dropbox vendió con un video. Muchos SaaS venden con una landing y un botón de pago antes de escribir la primera línea de código.

---

## 3. Lo que SÍ es validación

Validar es ver a alguien hacer algo que le cuesta algo:

- **Dinero real:** tarjeta, transferencia, contrato, factura. Aunque sean $10.
- **Dolor real:** que ya estén pagando por un parche hoy (“gasto $50 al mes en Excel + Zapier + la hora de mi asistente”).
- **Pre-venta:** founding members, depósitos reembolsables, pilots pagos.
- **Retención:** que paguen el mes 1, y el 2, y el 3.

---

## 4. El experimento que tienes que hacer ANTES de renunciar

Haz esto en las próximas 2 a 4 semanas. Sin construir más producto.

**1. Presell a tu waitlist.**  
Manda un correo a los 210:

> “Vamos a lanzar. Para entrar como *founding member* y fijar tu precio de $30/mes para siempre (o $299/año), paga hoy. Si no lanzamos en X fecha, te devuelvo el 100%.”

Pon un link de pago. Cuenta cuántos pagan.

- Si pagan **20+ personas**: hay señal real.
- Si pagan **menos de 10**: tu lista no es real o el dolor no es suficiente.
- Si pagan **0 o 2**: ya validaste. No hay negocio ahí.

**2. Sube el precio para medir intensidad.**  
Si dicen que pagarían $30, pide $50/mes o un *setup fee* de $200. Los que pagan más son los que de verdad tienen el problema.

**3. Habla con 20–30 desconocidos de tu segmento.**  
Nada de amigos. Pregunta por comportamiento pasado, no por opiniones:

- “¿Qué usaste la última vez que tuviste este problema?”
- “¿Cuánto pagaste por eso?”
- “¿Cuánto tiempo perdiste?”
- “¿Qué intentaste y abandonaste?”

Si no hay historial de gasto, es **vitamina**, no analgésico. Y las vitaminas no hacen renunciar a nadie a su trabajo.

**4. Vende un MVP hecho a mano.**  
Consigue 5 clientes y cóbrales por resolverles el problema manualmente (aunque sea feo, lento y no escalable). Si puedes cobrar por hacerlo tú detrás de cámaras, luego lo automatizas. Si no puedes cobrar ni así, el producto tampoco lo hará.

---

## 5. Cuándo SÍ tiene sentido renunciar

No renuncies por emoción. Renuncia cuando se cumplan mínimos así:

- Tienes **6–12 meses de gastos personales ahorrados**. Sin runway, tu trabajo es tu inversionista; no lo eches a la calle.
- Tienes al menos **$1,000–$2,000 MRR de clientes reales** (tarjeta, no amigos, no familia) o **5–10 clientes B2B con contrato o piloto pago**.
- Esos clientes ya renovaron al menos **2 o 3 meses**.
- La demanda te desborda: no puedes atender nuevos clientes en tus ratos libres.
- Sabes repetir la adquisición: cuánto cuesta conseguir un lead y cuánto un cliente.

Con 210 correos y $0, no sabes nada de eso.

---

## 6. Si decides dejar el trabajo igual

No renuncies de un día para otro. Pide media jornada, haz freelance o usa vacaciones. Date **60–90 días** con un hito claro y brutal:

> “Si en 90 días no tengo al menos 30–50 clientes pagando (o $1,500 MRR), vuelvo a mi trabajo.”

Sin ese hito, estás jugando a la ruleta rusa con tu vida financiera.

---

## Veredicto final

Hoy tu única métrica real es **0/29 y 0/210**. Eso no es un negocio validado; es una hipótesis con buenas relaciones públicas.

Consigue que alguien que **no te deba nada** te pase su tarjeta de crédito. Cuando eso pase —y se quede— renuncia.

**No antes.**