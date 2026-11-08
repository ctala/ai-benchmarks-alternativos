# Kimi K3.1 Pro — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 6.23 | quality: 8.0
- latency_total: 552.554s | tokens_per_second: 22.9
- input_tokens: 307 | output_tokens: 12667

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

No haría entrevistas, una landing page ni un prototipo. Haría una **preventa “concierge” con cobro real**: produces tú los reportes manualmente, pero cobras exactamente los **$200/mes**.

Es una prueba deliberadamente generosa: el cliente recibe más ayuda que con el futuro software. **Si ni así compran, la herramienta difícilmente va a salvar la hipótesis.**

## El experimento

| | |
|---|---|
| **Duración** | 7 días naturales |
| **Trabajo** | 12–15 horas |
| **Coste** | $0–50, más comisiones de cobro |
| **Muestra** | 15 ofertas completas a decisores cualificados |
| **Regla para parar** | **Menos de 3 agencias pagan $200: no construyas** |

No necesitas web, logo, anuncios ni código.

### 1. Define un segmento y una oferta que no puedas ir cambiando

Busca agencias que cumplan todo esto:

- 2–20 empleados.
- Al menos 5 clientes con reportes mensuales.
- El fundador, director de operaciones o responsable de cuentas puede decidir una compra de $200.
- Actualmente dedican al menos 4–5 horas mensuales a reporting, o tienen retrasos/errores recurrentes.

Congela una oferta concreta. Por ejemplo:

> “Por $200, te preparo el próximo ciclo de hasta 5 reportes mensuales, con vuestra marca y utilizando vuestras fuentes actuales. Entrega el [fecha concreta]. El primer ciclo lo opero yo manualmente; no tenéis que instalar ni migrar nada. Si no entrego lo acordado, os devuelvo el dinero. Si continuáis, son $200/mes, sin permanencia.”

No ofrezcas descuentos, pilotos gratuitos ni un precio distinto a cada agencia.

### 2. Día 1: prepara solo lo imprescindible — 2 horas

- Un reporte de muestra con datos ficticios, hecho en Slides, Looker Studio o herramientas similares.
- Una página con alcance, fecha de entrega y precio.
- Un enlace de pago o factura de $200.
- Una lista inicial de 50–60 agencias, priorizando contactos cálidos y acceso directo al dueño.

Nada más.

### 3. Días 1–4: consigue 15 conversaciones y vende

Mensaje de contacto:

> “Estoy probando un servicio para agencias que preparan mensualmente reportes de GA4/Ads para sus clientes. Busco 3 agencias para un piloto de pago: entrego el próximo ciclo con su marca y sin que tengan que montar nada. ¿Podemos ver durante 15 minutos cómo hicisteis el último reporte y, si encaja, te explico la oferta?”

En la llamada, no preguntes “¿te parece interesante?” ni “¿pagarías por esto?”. Pregunta por hechos:

- “Enséñame el último reporte que hiciste.”
- “¿Quién lo preparó y cuántas horas llevó?”
- “¿Qué parte tuviste que repetir para cada cliente?”
- “¿Qué pasó la última vez que se retrasó o hubo un error?”

Si cumple los criterios, haz la oferta y cierra:

> “Puedo entregarte el próximo ciclo el [fecha], con este alcance, por $200. ¿Empezamos hoy? Te paso el cobro y, una vez pagado, agendamos el acceso a los datos.”

Haz como máximo un seguimiento antes del día 7.

### 4. Qué cuenta como venta

Solo cuenta si hay estas tres cosas:

1. **$200 efectivamente cobrados**, sin descuento.
2. Una fecha de inicio comprometida.
3. Disposición real a entregar datos o accesos.

No cuentan:

- “Me interesa.”
- “Envíame información.”
- “Te lo pago cuando esté terminado.”
- Una carta de intención.
- Un piloto gratuito.
- Un depósito simbólico.
- La compra de un amigo para ayudarte.

## El resultado que me haría abandonar

Después de **15 ofertas completas** a agencias que reconocen el problema y cumplen el segmento:

- **0 ventas:** mataría la hipótesis comercial tal como está formulada.
- **1–2 ventas:** hay algo de señal, pero no suficiente para justificar dos meses de desarrollo. También pararía y reformularía segmento, problema u oferta.
- **3 o más ventas:** la prueba no ha matado la hipótesis; todavía no significa que el producto esté validado.

No cambies el umbral después de ver los resultados.

Si no consigues completar las 15 ofertas porque nadie acepta hablar, eso **no demuestra** que no exista disposición a pagar. Pero tampoco es una señal para construir: a $200/mes, no tener acceso barato a los decisores ya es un problema serio de adquisición.

## Si consigues las 3 ventas

Todavía no escribas software. Entrega manualmente esos tres ciclos con herramientas existentes y comprueba dos cosas:

1. Que realmente puedes estandarizar el trabajo.
2. Que **al menos 2 de las 3 agencias pagan un segundo mes de $200**.

Esta prueba es excelente para **matar** la idea, pero no para validarla completamente: alguien podría pagar por un servicio hecho por ti y no querer luego una herramienta self-service. Por eso el siguiente desembolso sigue siendo pequeño y el código espera.

**Coste total para descubrir que estás equivocado: como mucho $50, una semana y unas 15 horas. No dos meses.**