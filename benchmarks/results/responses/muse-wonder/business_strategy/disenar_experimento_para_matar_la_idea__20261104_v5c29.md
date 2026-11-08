# Muse Wonder — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `meta/muse-wonder`
- success: True  | final: 6.72 | quality: 8.0
- latency_total: 27.331s | tokens_per_second: 85.4
- input_tokens: 180 | output_tokens: 2333

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

No construyas nada. Ni un MVP. Ni una landing bonita.

Tu hipótesis no es "¿les duele hacer reportes?" A todo el mundo le duele todo.

Tu hipótesis real es esta:

> **Un dueño de agencia pequeña pierde suficiente tiempo/dinero haciendo reportes como para sacar su tarjeta HOY y pagar $200/mes a un desconocido.**

Eso solo se testea con una tarjeta. Todo lo demás es mentira educada.

Aquí está el experimento diseñado para matarla:

### LA SENTENCIA DE MUERTE (escríbela antes de empezar)

> **Si en 5 días, tras contactar 60 agencias calificadas y tener al menos 15 conversaciones reales con decisores, menos de 3 pagan $200 por adelantado, abandono la idea. No bajo el precio. No alargo el plazo. No "hago más entrevistas".**

Si no aceptas esa regla ahora, no hagas el experimento. Vas a autoengañarte después.

### EL EXPERIMENTO: Vende el reporte hecho a mano

No vendes software. Vendes el *resultado final* entregado por ti manualmente en 48h, como si ya existiera.

Si nadie lo compra hecho, perfecto y sin tener que aprender una herramienta nueva, nadie lo comprará en formato SaaS.

**Costo total: $0 - $19**
**Tiempo total: 5 días, unas 10 horas**
**Herramientas:** LinkedIn, Gmail, Tally gratuito, Calendly gratuito, 1 link de pago de Stripe.

#### Día 1 (2 horas): La lista

Busca en LinkedIn/Google 60 agencias que cumplan TODO esto. Si no cumplen, no cuentan para el test:

1.  3 a 15 empleados
2.  Gestionan mínimo 5 clientes con retainer mensual
3.  Ofrecen Ads, SEO o Social Media (servicios que exigen reporte mensual)
4.  Contactas al fundador o Head of Ops, no a un empleado

Sin esto, un "no" no significa nada.

#### Día 2-4 (30 contactos/día): El outreach

Nada de encuestas. Nada de "¿pagarías por...?". Mensaje directo y un Loom de 60 segundos opcional mostrando un reporte de ejemplo feo que hiciste en Sheets.

Copia y pega esto:

> Hola [Nombre], estoy probando un servicio para agencias de [su nicho] que les entrega el reporte mensual de cada cliente listo para enviar, en 48h, sin que tu equipo lo toque.
>
> Lo estoy abriendo para 5 agencias a $200/mes fijo, sin importar el nº de clientes hasta 10. Esta semana lo hago yo a mano para los primeros.
>
> ¿Quieres que te haga el de un cliente gratis como muestra y me dices si te ahorra tiempo? Si no te sirve, no seguimos.

Si acepta la llamada, la llamada dura 15 min y termina SIEMPRE así:

> Perfecto. Para meterte en los 5 de este mes necesito dejarlo reservado hoy con el primer pago de $200. Te lo entrego en 7 días y si no te vale para enviar a tu cliente, te devuelvo el 100%. ¿Lo dejamos con tarjeta?

Y te callas. No descuentes. No ofrezcas "pilotito gratis de 14 días". Eso invalida el test.

El link de Stripe lo creas en 5 minutos. No necesitas web.

#### Día 5: Contar cadáveres

Solo cuenta UNA métrica: **pagos reales.**

No cuentan: "me encanta la idea", "mándame info", "hablemos el mes que viene", 200 visitas a tu landing, 40 apuntados a una waitlist.

Eso es vanidad.

### RESULTADO QUE MATA LA IDEA

Abandonas si pasa cualquiera de estas 3 cosas:

**1. Muerte por dinero (la principal):**
Menos de 3 pagos de $200 tras 15 conversaciones calificadas.
0, 1 o 2 pagos = ruido, suerte o lástima. No es un negocio.

**2. Muerte por dolor insuficiente:**
En las llamadas descubres que la mediana dedica menos de 3 horas AL MES a todos los reportes juntos. A $200, les estás vendiendo un ahorro que vale menos que tu precio.

Pregunta clave para descubrirlo: *"El mes pasado, ¿quién hizo los reportes, cuánto tardó y qué dejó de hacer por hacerlos?"* Si no hay un coste claro, muere.

**3. Muerte por indiferencia del cliente final:**
Más de la mitad te dice: "Nuestro cliente ni abre el reporte, ya usamos Looker Studio gratis y nos vale". Entonces no vendes automatización, tendrías que vender otra cosa.

### Si sobrevive (que no es lo mismo que validarse)

Si 3+ pagan, NO construyas el software todavía.

Entrégales los reportes tú a mano durante ese primer mes con Sheets/Looker. Vas a tardar horas y vas a odiarlo. Perfecto. Ahí descubrirás qué 20% del reporte es el que realmente valoran y por el que renovarían el mes 2.

La renovación del mes 2 es el siguiente experimento que puede matarte.

Si no sobrevive, te acabas de ahorrar 2 meses y solo has perdido 5 días y $19.

Esa es la ganga.