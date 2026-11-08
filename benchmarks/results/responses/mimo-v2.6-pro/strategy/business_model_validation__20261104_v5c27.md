# MiMo V2.6 Pro — strategy/business_model_validation

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 91.344s | tokens_per_second: 31.4
- input_tokens: 188 | output_tokens: 2872

## Entrada exacta (lo que recibió el modelo)

**user:**

Quiero crear una app que conecta restaurantes pequenos con proveedores de ingredientes locales. El modelo es marketplace con 15% de comision por transaccion.

Mi hipotesis: los restaurantes pequenos pierden mucho tiempo llamando a multiples proveedores y quieren una solucion digital.

Actua como un VC esceperico. Hazme las preguntas dificiles que me harian en un pitch:
1. Identifica los 5 riesgos principales de este modelo
2. Por que podria NO funcionar en LATAM especificamente?
3. Que tendria que ser verdad para que funcione? (key assumptions)
4. Cual es el escenario donde fracaso rapido y por que?
5. Si solo tuviera $10K para validar, que harias?

No seas amable. Se brutalmente honesto.


## Respuesta completa

# VC Sceptical Review — Marketplaces LATAM

Voy a ser brutal. Si no aguantas estas preguntas, tu startup no va a sobrevivir un pitch real.

---

## 1. LOS 5 RIESGOS PRINCIPALES DE TU MODELO

**🔴 Riesgo 1: El "disintermediation risk" te va a matar.**
¿Qué impide que tu restaurante y tu proveedor se llamen directamente después de la primera transacción? En LATAM las relaciones comerciales son personales. El dueño del restaurante va a querer negociar por WhatsApp, por cerveza, por confianza de años. Tu app es el intermediario que se puede eliminar. ¿Cuál es tu moat? Si tu respuesta es "la tecnología", ya perdiste.

**🔴 Riesgo 2: El 15% de comisión es un robo para ingredientes.**
Los márgenes brutales de los ingredientes frescos en restaurantes son del 25-35%. Si tú te llevas 15% de la transacción, estás destruyendo el margen del proveedor O subiendo el precio para el restaurante. Ninguno de los dos lo va a tolerar. En LATAM, los proveedores de ingredientes frescos trabajan con márgenes del 8-15%. ¿De dónde sale tu 15%? ¿Quién lo paga? ¿Cómo compites con el proveedor que entrega directo y no cobra esa comisión?

**🔴 Riesgo 3: Operaciones logísticas que no controlas.**
Marketplace de ingredientes frescos ≠ marketplace de software. Un proveedor de tomates que llega 2 horas tarde con un 30% de producto malo = tu restaurante te culpa a TI. Tú no controlas calidad, temperatura de cadena de frío, puntualidad, ni el trato humano. Un mal proveedor destruye tu reputación. ¿Qué porcentaje del tiempo vas a pasar apagando incendios operativos en vez de creciendo?

**🔴 Riesgo 4: Problema del "huevo y la gallina" (cold start problem).**
Necesitas restaurantes para atraer proveedores y proveedores para atraer restaurantes. Nadie quiere ser el primero. Los restaurantes no van a instalar otra app si solo tienen 2 proveedores. Los proveedores no van a hacer el esfuerzo de cargar su catálogo si solo hay 5 restaurantes. ¿Cómo resuelves esto en cada ciudad que abres?

**🔴 Riesgo 5: Capital intensity = burn rate brutal.**
A diferencia de un marketplace de software, aquí vas a necesitar soporte al cliente, verificación de proveedores, manejo de quejas, posiblemente logística, y ventas on-the-ground en cada ciudad. Tu CAC (costo de adquisición de cliente) va a ser altísimo porque son negocios pequeños que no compran SaaS fácilmente. ¿Cuánto cuesta conseguir un restaurante activo? ¿Cuánto cuesta conseguir un proveedor activo? ¿Tu LTV cubre eso?

---

## 2. ¿POR QUÉ PODRÍA NO FUNCIONAR EN LATAM?

**Cultura de confianza presencial.**
En LATAM, un proveedor de ingredientes visita al restaurante. Se conoce con el chef. Habla. Degusta. Negocia. Se toma un café. Es un modelo **relacional**, no transaccional. Tu app convierte una relación humana en una pantalla fría. Los dueños de restaurantes pequeños en Lima, Bogotá o Ciudad de México no son early adopters tech. Son personas de 40-55 años que usan WhatsApp y punto.

**Fragmentación absoluta.**
No existe un "Mercado Libre de ingredientes" porque el mercado es hiperlocal. El provejo de tomate en Polanco (CDMX) no es el mismo que en Iztapalapa. Cada colonia/barrio tiene su propia red de proveedores. Tu marketplace tendría que construirse ciudad por ciudad, barrio por barrio. Eso es un negocio de operaciones, no de tech. Tu escala es lineal, no exponencial.

**Informalidad.**
El 50-70% de los proveedores de ingredientes en LATAM son informales. No tienen factura, no tienen registro, no pagan impuestos. ¿Cómo los vas a onboardear en tu plataforma? ¿Cómo vas a procesar pagos con alguien que cobra en efectivo? ¿Cómo vas a hacer tu modelo de comisión del 15% cuando la transacción es informal?

**Infraestructura de pagos.**
Los restaurantes pequeños pagan en efectivo o transferencia directa al proveedor. Muchos no aceptan tarjeta de crédito. Si quieres procesar los pagos para cobrar tu comisión, vas a necesitar que ambos extremos adopten tu sistema de pago. Eso es una barrera masiva.

**Competition no-tech.**
En LATAM ya existe la solución: **WhatsApp**. El restaurante tiene un grupo con sus 5-6 proveedores. Les manda un audio, recibe precios por foto, negocia, y listo. ¿Por qué va a cambiar eso por tu app? ¿Qué le resuelves que WhatsApp no le resuelve?

**Macroeconomía.**
Inflación, devaluación, inestabilidad política. Los restaurantes pequeños cierran a un ritmo de 30-40% al año. Tu tasa de churn de clientes va a ser brutal. ¿Cuál es tu modelo de retención?

---

## 3. ¿QUÉ TENDRÍA QUE SER VERDAD PARA QUE FUNCIONE?

Estas son tus key assumptions. Si alguna de estas es falsa, tu startup muere:

| # | Supuesto | ¿Cómo lo validas? |
|---|----------|-------------------|
| 1 | Los restaurantes pequeños están dispuestos a **pagar más** (o mantener el precio) a cambio de **conveniencia** | ¿Cuántos están pagando actualmente por soluciones de conveniencia? ¿$0? Problema. |
| 2 | Los restaurantes pierden **≥3 horas/semana** coordinando con proveedores | ¿Lo has medido? ¿O es tu percepción? Necesitas datos de campo, no tu intuición. |
| 3 | Los proveedores van a aceptar **abrir información de precios** en una plataforma transparente | Los proveedores en LATAM odian la transparencia de precios. Les encanta cobrar diferente a cada cliente. Tu marketplace los expone. |
| 4 | Puedes cobrar **15% sin que nadie te lo recorte** | La tasa de "side deals" (tratos por fuera) va a ser del 40-60%. Los dos extremos van a encontrar cómo evitarte. |
| 5 | El proceso de onboarding (restaurantes + proveedores) puede ser **rápido y barato** | ¿Cuánto tiempo toma convencer a un provejo de tacos de usar tu app? ¿Un mes? ¿Dos? Eso es CAC brutal. |
| 6 | Hay **suficiente densidad** de restaurantes + proveedores en una zona geográfica para crear liquidez del marketplace | Si en un barrio solo hay 3 restaurantes y 5 proveedores, no hay marketplace que valga la pena. |
| 7 | Puedes **retener** a los restaurantes en tu plataforma después de las primeras transacciones | El churn será tu enemigo #1. |

---

## 4. ESCENARIO DE FRACASO RÁPIDO

**El escenario más probable de muerte rápida:**

> Construyes un MVP bonito. Vas a un barrio en CDMX. Conviences 15 restaurantes y 8 proveedores. Las primeras 2 semanas hay entusiasmo. Se hacen 40 transacciones. Y entonces:
>
> - El proveedor más popular se da cuenta que los restaurantes lo contactan directamente por WhatsApp y **se sale de tu plataforma**.
> - El restaurante que más compraba negocia por fuera porque el proveedor le da **5% de descuento** en efectivo.
> - 3 de los 15 restaurantes cierran en 3 meses.
> - Tu tasa de retención mensual es del 15%.
> - Necesitas re-aquirir constantemente. Tu CAC sube. Tu runway se acorta.
> - A los 4-6 meses, no hay transacciones. Quemas $50K-100K. Mueres.

**¿Por qué es tan probable?** Porque la dinámica económica de LATAM premia la informalidad, la confianza personal, y la evasión de intermediarios. Tu modelo es literalmente un intermediario digital. Eres presa de la disintermediación en un mercado que ya tiene un sistema informal funcional (WhatsApp + confianza).

---

## 5. CON $10K: ¿QUÉ HARÍA?

No construiría una app. Las apps no validan nada. Lo que valida es comportamiento real.

**Fase 1: Manual (Semanas 1-4) — $2,000**
- Elige **UN solo barrio/zona** con alta densidad de restaurantes pequeños (ej: Roma-Condesa, Miraflores, Chapinero).
- Ve puerta por puerta a 50 restaurantes. Entrevístralos. Pero NO les vendas nada. Pregunta: *"¿Cuánto tiempo pierdes comprando ingredientes? ¿Cómo lo haces? ¿Cuánto pagarías por ahorrarte eso?"*
- Identifica los 3-5 proveedores más comunes.
- **Si más de 30 de 50 restaurantes te dicen que pierden >3 horas/semana y estarían dispuestos a pagar, sigues.** Si no, pivotas o mueres rápido.

**Fase 2: Concierge MVP (Semanas 5-8) — $4,000**
- Actúa como **agente manual** entre restaurantes y proveedores.
- Recibe pedidos por WhatsApp de 10 restaurantes. Los consolidas con 3-5 proveedores. Coordinas la entrega. Cobras una comisión (aunque sea 5%, no 15%, para validar la disposición a pagar).
- Usa Google Sheets + WhatsApp. CERO código.
- Mide: ¿cuántas transacciones hay? ¿repiten? ¿cuánto pagan? ¿te evitan después de la 2da transacción?

**Fase 3: Medición de disintermediación (Semanas 9-12) — $2,000**
- Este es el test más importante: **¿te eliminan?**
- Si el 40%+ de las parejas restaurante-proveedor hacen trato directo después de la primera transacción, tu modelo está muerto. Necesitas cambiar el moat.
- Si te retienen, mide LTV, churn, y ticket promedio.

**Fase 4: Decisión (Semana 12) — $2,000 para el pitch deck**
- Si tienes datos de retención, ticket promedio, y CAC manual, ahora SÍ puedes ir a un inversor con evidencia real.
- Si no, pivoteas o cierras.

**TOTAL: $10K, 12 semanas, y tienes una respuesta real a tu hipótesis.**

---

## MI VEREDICTO COMO VC:

> Tu idea no es mala. El problema que describes es real. Pero la solución (marketplace con 15%) probablemente no funciona en LATAM en su forma actual. Las 3 preguntas que necesitas responder antes de levantar dinero:
>
> 1. **¿Puedes evitar la disintermediación?** Si no, necesitas un modelo diferente (SaaS, logística, financiamiento).
> 2. **¿De dónde sale tu 15%?** En un margen del 10%, eso no se paga solo.
> 3. **¿Por qué WhatsApp no es suficiente?** Si no puedes responder esto con un diferenciador brutal, no tienes startup. Tienes un feature de WhatsApp.
>
> **Prefiero verte quemar $10K en 3 meses con datos que $500K en 12 meses con una app bonita que nadie usa.**

No me pidas dinero hasta que tengas las respuestas 1-3. Y las quiero con datos, no con slides.