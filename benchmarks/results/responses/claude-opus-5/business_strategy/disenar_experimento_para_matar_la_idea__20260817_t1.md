# Claude Opus 5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.57 | quality: 8.0
- latency_total: 66.1s | tokens_per_second: 60.2
- input_tokens: 289 | output_tokens: 3982

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## Primero: tu hipótesis tiene 4 hipótesis escondidas

Escrita así, "pagarían $200/mes", es infalsificable en la práctica: cualquiera te dice "sí, suena interesante". Descompuesta:

1. Las agencias pequeñas sienten dolor real haciendo reportes (probablemente cierto)
2. Ese dolor no está ya resuelto (**dudoso** — acá se muere la mayoría)
3. Vale $200/mes, no $50 (**muy dudoso**)
4. Los reportes son lo bastante homogéneos como para automatizarlos en 2 meses (**el asesino silencioso**)

El experimento tiene que atacar 2, 3 y 4. El 1 no te sirve para nada.

---

## Día 0 — Kill check de escritorio (2 horas, $0)

Antes de hablar con nadie. Buscá y anotá precios de: AgencyAnalytics, DashThis, Whatagraph, Swydo, Databox, Metrics Watch, ReportGarden, y Looker Studio (gratis).

**Criterio de muerte inmediata:** si ya existen 3+ productos maduros haciendo exactamente esto en el rango $49–$179/mes, tu hipótesis *tal como está escrita* ya está muerta. No porque no haya mercado, sino porque estás proponiendo cobrar 2–4x el precio de mercado por un commodity, siendo desconocido.

Si eso pasa, no abandones todavía — pero reformulá la hipótesis antes de gastar un peso más. La pregunta ya no es "¿pagarían $200?" sino **"¿por qué las agencias que YA pagan una de estas la odian lo suficiente para cambiarse?"**. Es una hipótesis distinta y mucho más específica.

---

## Días 1–3 — Test de homogeneidad (4 horas, $0)

El más barato de todos y el que casi nadie hace.

**Qué hacés:** contactás 15 agencias (grupos de Facebook de agencias, r/agency, r/PPC, comunidades de Slack, Clutch.co filtrando por 2–10 empleados). Pedido único:

> "Estoy investigando cómo hacen los reportes mensuales las agencias chicas. ¿Me mandás un reporte real de un cliente, con los datos tachados? A cambio te mando un resumen de los 15 que junte, con lo que hacen los demás."

Nadie te está comprando nada. Es gratis y la tasa de respuesta es alta porque estás dando algo.

**Criterio de muerte:** juntá 8–10 reportes. Si tienen **más de 5 estructuras fundamentalmente distintas** (distintas fuentes de datos, distintas métricas core, mitad con narrativa escrita a mano, mitad con KPIs custom por cliente), tu build de 2 meses es una fantasía. Estás mirando 8–12 meses o un producto tan rígido que nadie lo usa. Este es el hallazgo que más plata te ahorra y cuesta $0.

---

## Días 3–8 — El test que de verdad mata: pre-venta con entrega manual

Nada de encuestas. Nada de "¿pagarías?". **Cobrás plata hoy por un servicio que hacés a mano.**

**La oferta (usá exactamente el precio de tu hipótesis):**

> "Te hago los reportes de tus clientes este mes. Vos me das acceso de lectura a las cuentas y tu template. Yo te entrego el día 5 del mes que viene, listo para mandarle al cliente. $200 por el mes. Si no te sirve, te devuelvo todo."

**Infra necesaria:** un link de pago de Stripe (gratis) + un Loom de 90 segundos + opcionalmente un Carrd ($19/año). Nada más. **Sin producto.**

**Volumen mínimo para que el test sea concluyente:** 100 contactos calificados en frío o tibio (agencias de 2–15 personas, con clientes de performance/paid media). Contactos en frío, no tus amigos — un "sí" de tu red es un falso positivo y te va a costar 2 meses.

Esperá ~15–20 respuestas y ~8–12 conversaciones reales.

---

## Criterios pre-registrados (escribilos ANTES de empezar)

| Resultado sobre 100 contactos / ~10 conversaciones | Veredicto |
|---|---|
| **0 pagos** y el objeción dominante es "ya uso X y está bien" | **Muerta.** Abandonar o pivotear a otro problema. |
| **0 pagos**, objeción dominante "no te doy acceso a las cuentas de mis clientes" | Muerta como SaaS de terceros. El bloqueante es confianza/seguridad, no software. |
| **1 pago** | Ambigua = negativa. 1/100 no es un negocio, es un favor. No construyas. |
| **Contraofertan $50–80 sistemáticamente** (3+ personas) | Hipótesis del precio muerta. A $60/mes necesitás 10x los clientes: ¿tenés canal para eso? |
| **3+ pagos a $200** | Señal real. **Pero igual no construyas.** Seguí 2 meses más entregando a mano. |
| **Nadie responde nada (0 respuestas)** | Test inválido, no resultado negativo. Tu mensaje o tu targeting están mal. Rehacé. |

**Trampa a evitar:** "me dijeron que sí pero querían esperar al producto terminado" **cuenta como NO**. Si no pasa la tarjeta, no existe. Ese es el único filtro que importa.

---

## Costo total

- **Plata:** $0 a $70 (Carrd + quizá algo de LinkedIn/listas)
- **Tu tiempo:** 15–20 horas repartidas en 8–10 días
- **Vs. lo que estabas por gastar:** 2 meses de tu vida (~320 horas)

Ratio: **20 horas para proteger 320.**

---

## El bonus que casi nadie ve

Si conseguís 3+ pagos, tenés algo mejor que validación: **tenés clientes pagando y estás haciendo el trabajo a mano.** Eso te enseña exactamente qué automatizar primero — y probablemente descubrás que el 80% del valor está en el 20% del producto que imaginaste.

Y si el test da negativo, en el proceso vas a haber escuchado 10 veces cuál *sí* es el dolor caro. Mi apuesta, por lo que suele pasar en este vertical: no es "armar el reporte", es **"que el cliente no lee el reporte y se va igual"** — retención, no reporting. Es un problema distinto y vale mucho más de $200.

Anotá tus criterios de muerte ahora, antes de enamorarte de la primera respuesta amable.