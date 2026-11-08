# Tencent Hy4 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `tencent/hy4`
- success: True  | final: 7.08 | quality: 8.0
- latency_total: 73.399s | tokens_per_second: 79.2
- input_tokens: 213 | output_tokens: 5812

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

No construyas nada. El único dato que puede matar esta hipótesis es **un pago rechazado con la oferta encima de la mesa**. Un email, un click, un "me interesa" o un "avísame cuando esté listo" no matan nada: son exactamente el ruido que te mete 2 meses de trabajo.

El experimento: **vende el primer mes antes de que exista y entrégalo a mano.**

---

## Paso 0 — 15 min, $0 (puede matarla antes de hablar con nadie)

Busca qué usan hoy esas agencias: Looker Studio (gratis), DashThis, Whatagraph, AgencyAnalytics, o la plantilla de Sheets del analista. Si en 15 min encuentras que el reporte ya les sale gratis o en 20 min y **no se quejan de ello**, la hipótesis ya está muerta: no hay dolor de $200. Cierra el portátil.

Si sí hay quejas ("cada fin de mes es un infierno", "se me olvida mandarlo", "el cliente me pide cambios"), sigue.

---

## El protocolo (1 día, 6 horas, $0)

**09:00–09:30 · La "muestra" (cero código)**
Un PDF de 2 páginas con un reporte mensual realista: logo, 4 métricas, gráfico, comparativa vs mes anterior, texto de "qué hicimos / qué sigue". Google Sheets + Canva o incluso maquetado a mano. **No es una demo genérica**: cuando hables con cada agencia, le pones el nombre de un cliente suyo y sus métricas (se las pides por DM: "pásame 4 números de cualquier cliente y te lo armo"). 10 min por agencia.

**09:30–09:35 · Link de pago real**
Stripe / MercadoPago Payment Link: **$200, cobro del primer mes ahora**, con una línea escrita: *"Si el lunes no te sirve, te devuelvo el dinero, sin preguntas"*. Sin landing, sin dominio, sin logo, sin formulario. La garantía es clave: elimina la desconfianza y deja vivas solo dos variables → **el dolor y el precio**. Si aun así no pagan, no fue por miedo a que no existiera.

**10:00–11:00 · 20 nombres, pero SOLO decisores**
Dueño / socio de agencia de 1–10 personas con clientes recurrentes y reporte mensual. **No hables con el analista**: él te dirá que sí porque le quita trabajo, pero no firma el gasto, y su "sí" es el falso positivo más caro de este mercado. LinkedIn, grupos de agencias, directorio local, o mejor: responde a gente que se esté quejando del tema públicamente. 20 contactos para lograr 10 conversaciones.

**11:00–17:00 · 10 conversaciones, guion literal**

> "Te armé el reporte de [su cliente] con tus números, así quedaría cada mes sin que nadie lo toque. [adjuntas PDF]. Lo entrego yo el lunes, y este mes lo hago solo con unas pocas agencias. Son **$200/mes** y te cobro el primero ahora por aquí [link]. Si el lunes no te ahorra el fin de mes, te devuelvo el dinero. ¿Lo activo?"

Tres reglas del guion:
- No preguntes *"¿pagarías?"*. Di *"te cobro ahora"*. La pregunta invita a la cortesía; el cobro invita a la verdad.
- No digas "es una idea / estoy validando". Vendes el **reporte hecho por ti**, que existe y vas a entregar. Es honesto: es exactamente lo que haría el software, y es lo único que el cliente compra.
- No muestres la herramienta. Muestra el **resultado**.

**17:00 · Decisión.**

---

## Coste y tiempo

| | |
|---|---|
| Dinero | **$0** (Stripe/MercadoPago solo cobra comisión si hay venta… y si hay venta, ya no estás matando nada) |
| Tiempo | **6 h en un día**. Tope 48 h si cuesta agendar las 10 llamadas |
| Código | **0 líneas** |

---

## El resultado que te hace abandonar (escríbelo ANTES de empezar)

> **Si de 10 dueños que vieron SU reporte, escucharon "$200/mes", tuvieron el link vivo y la garantía de reembolso, 0 pagan → abandono la idea. Ese mismo día.**

Y sin mover el listón después. Pre-regístralo, porque el fundador que se equivoca siempre renegocia el criterio a las 18:00.

**Cuenta como NO** (y por tanto suma al kill):
- "Muy caro" / "nuestro margen no da"
- "Lo vemos el mes que viene"
- "Mándame info" / "avísame cuando esté listo" ← **este es el que te roba los 2 meses. Es un no con sonrisa.**
- Silencio *después* de que dijiste el precio

**No cuenta** (ruido, no señal):
- Mensaje no leído, analista en vez de socio, agencia que no manda reportes mensuales

**Condición de validez:** si solo logras 4 conversaciones con el precio dicho en voz alta, **no has matado nada**, has fallado en distribución. Extiende 24 h para llegar a 10. Pero sigues sin construir.

**1 pago de 10** ≠ muerto, pero está gravemente herido: el siguiente experimento es de **precio** ($99, o pago por reporte), no de producto. Y sigue sin una línea de código.

---

## El output de verdad no es el sí/no: son las objeciones

Apunta literalmente cada negativa. Si la misma aparece 3 veces, tienes el diagnóstico, no solo el cadáver:

- *"Eso lo hacemos en Looker Studio en 15 min"* → no hay dolor
- *"El cliente ni lo abre"* → el reporte no es un problema de negocio, es un trámite
- *"Ya lo absorbe el analista dentro del fee"* → el coste existe pero es invisible, nadie le pone presupuesto
- *"¿$200 por agencia? Con 8 clientes me como el margen"* → el precio está mal anclado a su unidad económica
- *"Pagaría por cliente, no por mes"* → muere la hipótesis tal como la formulaste ($200/mes)

---

Si hoy mueres, perdiste 6 horas y ganaste la razón exacta por la que no debías construir. Si construyes 2 meses y descubres esto al final, perdiste 2 meses y además tendrás un producto que te va a costar abandonar. Ese es todo el experimento.