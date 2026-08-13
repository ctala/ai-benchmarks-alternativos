# GPT-5.6 Luna Pro — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 7.26 | quality: 8.0
- latency_total: 56.991s | tokens_per_second: 155.0
- input_tokens: 10403 | output_tokens: 8835

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## Experimento: preventa concierge por $200

No construyas la herramienta. Vende el resultado y entrega el primer reporte manualmente usando herramientas existentes. La única señal válida será **dinero cobrado**.

### Qué estás probando

> “Una agencia pequeña pagará $200 al mes por recibir reportes de marketing listos para enviar a sus clientes, sin tener que armarlos manualmente.”

No estás probando si les gusta la idea ni si dicen que la usarían.

---

## Oferta exacta

Ofrece solamente 3 plazas:

> “Estoy probando un servicio de reporting para agencias. Cada mes recibes un reporte branded, con métricas de Meta Ads, Google Ads y GA4, comentarios sobre variaciones importantes y una versión lista para enviar al cliente.  
>   
> Durante el piloto lo preparo manualmente para asegurar calidad. El precio es $200 por el primer mes, sin contrato anual. Si el primer reporte no llega en 48 horas desde que recibo los accesos, te devuelvo el dinero.”

No ofrezcas descuentos, prueba gratuita ni “precio especial por ser early adopter”. Eso contamina la prueba del precio.

El cliente debe pagar **antes** de que prepares el reporte.

---

## Perfil objetivo

Contacta agencias que cumplan todos estos criterios:

- 2–20 empleados.
- Al menos 5 clientes activos.
- Gestionan campañas de Google Ads, Meta Ads o ambas.
- Envían reportes mensuales a clientes.
- El fundador, account manager o director de operaciones participa en los reportes.
- No tienen un sistema de reporting claramente automatizado.

No incluy freelancers que solo tienen uno o dos clientes ni grandes agencias con departamentos de BI.

---

# Plan de 7 días

## Día 1: prepara lo mínimo

Tiempo: 2 horas.  
Coste: $0–20.

Necesitas:

1. Una página o documento de una pantalla en Notion/Google Docs con:
   - Qué recibe la agencia.
   - Qué canales cubres.
   - Plazo de entrega.
   - Precio: $200.
   - Botón de pago.

2. Un enlace de pago de Stripe, PayPal o Mercado Pago.

3. Una plantilla manual de reporte en:
   - Google Slides, Canva o Looker Studio.
   - Google Sheets para consolidar datos.
   - Opcionalmente, ChatGPT para ayudarte a redactar observaciones.

4. Un formulario simple para recoger:
   - Nombre de agencia.
   - Número de clientes.
   - Canales usados.
   - Ejemplo del reporte actual.
   - Accesos o exportaciones de datos.

No compres software específico ni desarrolles integraciones.

---

## Días 1–3: contacta a 50 agencias

Haz una lista de 50 agencias cualificadas:

- 20 de tu red personal o profesional.
- 20 encontradas en LinkedIn, Google Maps, Clutch, directorios locales o comunidades.
- 10 que parezcan especialmente ajustadas al perfil.

Envía mensajes personalizados, no una campaña masiva genérica.

### Mensaje inicial

> Hola, [nombre]. Vi que [agencia] trabaja con [tipo de clientes/canales].  
>   
> Estoy hablando con agencias pequeñas que todavía preparan manualmente los reportes mensuales para sus clientes. ¿Cómo resolvéis actualmente esa parte?  
>   
> No te quiero vender nada todavía; estoy intentando entender cuánto tiempo consume y qué partes son más problemáticas.

Si responden que sí hacen reportes, pregunta:

> ¿Cuántas horas al mes os lleva aproximadamente preparar y revisar esos reportes?

Después:

> ¿Qué suele ser lo más molesto: recopilar datos, revisar errores, diseñar el informe o escribir las conclusiones?

No menciones inicialmente tu solución. Primero confirma que el problema existe y que la persona está cerca del proceso.

---

## La prueba de pago

Cuando la persona describa un problema real, di:

> Tiene sentido. Estoy probando justamente un servicio para resolver eso.  
>   
> Puedo prepararos manualmente un reporte branded para uno de vuestros clientes, con los datos de [canales], conclusiones ejecutivas y formato listo para enviar. Lo entrego en 48 horas. El piloto cuesta $200 por el primer mes y no hay contrato.  
>   
> Si te interesa probarlo, puedes reservar una plaza aquí: [enlace de pago].

Después, cállate.

No preguntes:

- “¿Pagarías $200?”
- “¿Te parece interesante?”
- “¿Qué te parecería?”
- “¿Cuánto pagarías?”

Pide la compra real.

### Qué cuenta como señal positiva

Cuenta únicamente:

- Pago de $200.
- Pago pendiente por una razón administrativa concreta, con fecha definida.
- Acceso a los datos después del pago.

No cuentan:

- “Me interesa.”
- “Mándame información.”
- “Lo hablamos más adelante.”
- Una encuesta positiva.
- Una carta de intención.
- Una reunión sin pago.
- Que pidan un piloto gratuito.

---

## Días 3–6: entrega manualmente

A quien pague:

1. Pide datos exportados o accesos de solo lectura.
2. Prepara el reporte en un máximo de 90 minutos.
3. Entrégalo en 48 horas.
4. Pregunta después:
   - ¿Lo enviarías directamente a tu cliente?
   - ¿Qué cambiarías?
   - ¿Cuánto tiempo te ahorró?
   - ¿Pagarías de nuevo $200 el mes próximo?

No intentes automatizar nada. El objetivo es descubrir si pagarían por el resultado, no si puedes construir el producto.

Si el reporte manual tarda más de 90–120 minutos, anótalo. Quizá exista demanda, pero no para una herramienta viable a ese precio sin un alcance mucho más limitado.

---

# Criterio de abandono

Establece esto antes de comenzar:

## Abandona la idea si ocurre cualquiera de estos casos

1. Después de hablar con **20 agencias cualificadas**, tienes **cero pagos de $200**.
2. Después de 50 contactos, no consigues al menos 10 conversaciones con personas que realmente preparen reportes. Esto indica que el segmento o el problema están mal definidos.
3. Dos o más agencias pagan, pero ninguna estaría dispuesta a renovar después del primer reporte.
4. Para entregar el reporte necesitas más de 2 horas por cliente y las agencias no aceptan pagar más de $200 ni reducir el alcance.

Mi regla principal sería:

> **0 pagos de 20 conversaciones cualificadas = abandonar la hipótesis de una herramienta de reporting de $200/mes para agencias pequeñas.**

Si obtienes solo un pago, no lo trates como validación. Haz cinco conversaciones adicionales. Si terminas con menos de dos pagos entre 25 conversaciones, abandona o cambia radicalmente el segmento, el problema o el precio.

---

## Coste y tiempo

### Coste

- Google Docs, Sheets, Slides, Notion: $0.
- Stripe/PayPal/Mercado Pago: sin coste fijo; solo comisión sobre ventas.
- Canva opcional: $0.
- Dominio o landing page: innecesario.
- Base de datos de prospectos: $0 usando búsquedas manuales.

**Coste total máximo recomendado: $50.**

### Tiempo

- Preparación: 2 horas.
- Investigación y contacto de 50 agencias: 5–7 horas.
- 20 conversaciones de 15–20 minutos: 6 horas.
- Entrega de pilotos: solo si alguien paga.

**Duración: 5–7 días laborables.**

---

## Lo que no debes hacer

- Construir integraciones.
- Crear un dashboard completo.
- Hacer una encuesta.
- Ofrecer un piloto gratis.
- Bajar el precio para “facilitar la decisión”.
- Contar respuestas positivas como validación.
- Preguntar cuánto pagarían.
- Pasar dos meses desarrollando antes de cobrar.

El experimento termina cuando el mercado tiene la oportunidad de comprar a $200 y decide hacerlo o no.