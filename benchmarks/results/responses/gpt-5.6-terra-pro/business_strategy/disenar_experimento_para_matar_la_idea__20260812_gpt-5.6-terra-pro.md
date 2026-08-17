# GPT-5.6 Terra Pro — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 6.72 | quality: 8.0
- latency_total: 104.182s | tokens_per_second: 139.5
- input_tokens: 15626 | output_tokens: 14532

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## Experimento: vender el piloto antes de construir

No pruebes interés. No hagas entrevistas abiertas. No pidas “feedback”.

Tu hipótesis solo sobrevive si una agencia **paga $200 hoy** por el resultado que tu software promete, aunque inicialmente lo entregues con una operación manual detrás.

### 1. Define el segmento de forma brutalmente específica

No pruebes “agencias pequeñas” en general. Prueba este segmento:

- Agencia de performance marketing de **3–15 personas**
- Tiene **10+ clientes recurrentes**
- Usa al menos **GA4 + Google Ads o Meta Ads**
- Hoy arma reportes para clientes manualmente
- Dedica al menos **3 horas/mes** a reporting
- Hablas con el dueño, director de operaciones o quien puede pagar software

Si no cumplen eso, no cuentan en la muestra.

---

## La oferta exacta

No construyas producto. Haz una demo falsa pero honesta en Figma, Canva o Google Slides.

Oferta:

> “Reportes mensuales white-label para tus clientes, combinando GA4, Google Ads y Meta Ads, enviados automáticamente con tu marca.  
>   
> Precio: **$200/mes por agencia**.  
>   
> Estamos aceptando 5 agencias piloto. El producto está en beta: para asegurar que funcione desde el primer mes, yo haré la configuración inicial y supervisaré las primeras entregas por detrás. No es un servicio de analista ni habrá reportes a medida.  
>   
> Si en los primeros 30 días no recibes el reporte acordado, te devuelvo el 100%.”

Importante:

- Cobra **$200 ahora**, no una carta de intención.
- No ofrezcas descuento.
- No ofrezcas “trial gratis”.
- No digas “¿lo usarías?”.
- No prometas funcionalidades que no puedas simular o entregar manualmente.
- Sé transparente: está en beta y usarás procesos manuales temporalmente. No mientas sobre que ya está automatizado.

Crea un enlace de pago de Stripe con el producto:  
**“Piloto — reporting automatizado para agencias — $200/mes”**.

---

## Material mínimo que necesitas

No necesitas landing page ni código.

En 2–3 horas crea:

1. **Una demo de 4 pantallas**
   - Conectar fuentes: GA4, Meta, Google Ads.
   - Elegir una plantilla de reporte.
   - Añadir logo/colores de la agencia.
   - Programar envío mensual al cliente.

2. **Un ejemplo de reporte terminado**
   - PDF o Google Slides.
   - Usa datos ficticios.
   - Que parezca algo que una agencia enviaría a un cliente.

3. **Un Google Doc de una página**
   - Qué incluye.
   - Qué no incluye.
   - Precio: $200/mes.
   - Garantía de devolución a 30 días.
   - Que es un piloto beta.

4. **Un link de Stripe para cobrar $200.**

Coste: **$0** usando Google Slides/Canva/Figma gratis + Stripe.  
Stripe solo cobra comisión si alguien paga.

---

## Ejecución: 7 días, máximo

### Día 1: lista de 100 agencias

Busca 100 agencias que encajen usando LinkedIn, Google Maps, Clutch, directorios de agencias, Instagram o tu red.

No compres bases de datos. No uses anuncios. No hagas SEO.

Para cada una consigue:

- Nombre de agencia
- Nombre del fundador/operador
- Email o LinkedIn
- Una señal de que hace performance marketing
- Una señal de que trabaja con varios clientes

Tu objetivo no es volumen masivo. Es llegar a gente que realmente compra software para su agencia.

---

### Días 1–3: contacto directo

Envía este mensaje por email o LinkedIn. Personaliza solo la primera línea.

> Hola, [Nombre]. Vi que [señal concreta: gestionan campañas de Meta/Google para clientes / trabajan con e-commerce / etc.].  
>   
> Estoy abriendo 5 plazas piloto para agencias que pierden tiempo armando reportes mensuales para clientes.  
>   
> La herramienta reúne GA4, Meta y Google Ads, genera un reporte white-label con la marca de la agencia y lo programa para envío mensual. Costará **$200/mes por agencia**.  
>   
> No busco feedback ni una entrevista: busco agencias que puedan decidir si pagarían por dejar de armar esos reportes manualmente.  
>   
> Si hoy gestionan al menos 10 clientes y usan esas fuentes, ¿te muestro una demo de 7 minutos esta semana?

Envía 100 mensajes. Haz un follow-up 48 horas después:

> Solo cierro el loop: ¿los reportes mensuales los armáis manualmente hoy o ya tenéis esto resuelto?

No cambies el precio. No cambies el mensaje a mitad de experimento.

---

### Días 3–7: demos de 7 minutos y cierre

En cada llamada, primero filtra. Haz estas preguntas:

1. ¿Cuántos clientes recurrentes tienen?
2. ¿Qué fuentes usan para los reportes?
3. ¿Quién arma hoy los reportes?
4. ¿Cuántas horas al mes gastan?
5. ¿Qué usan actualmente?
6. ¿Tú puedes decidir pagar $200/mes por software?

Si no encajan, termina la llamada. No cuentan.

Si encajan, muestra la demo y cierra así:

> “No quiero una opinión hipotética. El piloto cuesta $200/mes y el primer pago es hoy. Si en 30 días no recibes el reporte acordado, te devuelvo el dinero.  
>   
> ¿Quieres entrar al piloto?”

Luego envía el link de Stripe **durante la llamada** y espera.

La única métrica que importa es:

## Pagos reales de $200

No cuentan como validación:

- “Me interesa”
- “Vuelve cuando esté listo”
- “Lo probaría”
- “Mándame información”
- “Quizá el próximo mes”
- Una LOI no pagada
- Una promesa verbal
- Un email diciendo que pagarían

---

# Regla de abandono

## Mata la idea si ocurre esto:

> Hablas con **30 decisores que cumplen el perfil**, ven la demo, entienden que cuesta $200/mes, tienen garantía de devolución, y **0 paga**.

En ese caso, abandona la hipótesis:

> “Las agencias pequeñas de performance con 10+ clientes pagarán $200/mes por automatizar reportes.”

No bajes el precio.  
No añadas funciones.  
No construyas durante dos meses “para que se entienda mejor”.  
No interpretes “interés” como demanda.

Con 30 oportunidades reales y cero pagos, si una oferta de este tipo tuviera siquiera una probabilidad razonable de compra inmediata —por ejemplo, 10%— la probabilidad de conseguir cero pagos sería aproximadamente 4%. Es una señal suficientemente fuerte para no invertir dos meses.

---

## Regla para resultados intermedios

| Resultado tras 30 ofertas calificadas | Decisión |
|---|---|
| 0 pagos | Abandona la idea/segmento/precio. |
| 1–2 pagos | No construyas aún. Hay señal débil; repite con otro segmento o mejora la definición del problema. |
| 3+ pagos ($600+ cobrados) | No has validado el producto, pero sí has ganado el derecho a construir el mínimo necesario para entregar. |
| 5+ pagos | Fuerte señal de disposición a pagar. Construye solo lo necesario para cumplir a esos clientes. |

---

## Qué puede fallar y qué significa

- **Nadie responde a tus mensajes:** no has matado la hipótesis; has fallado en canal o mensaje. Busca otro canal, pero no construyas todavía.
- **Responden y dicen que ya usan AgencyAnalytics, Looker Studio, DashThis, Swydo, etc.:** pregunta cuánto pagan y por qué no cambiarían. Si el coste de cambio es la objeción dominante, tu idea probablemente no tiene una cuña suficiente.
- **Les duele el problema pero no pagan $200:** mata la hipótesis de precio, aunque no necesariamente la de problema.
- **Pagan solo si haces reportes a medida:** no has validado SaaS; has validado una agencia de reporting. No te engañes.
- **Pagan por la promesa concreta sin pedir personalización:** esa es la señal que buscas.

---

## Coste y duración

- Herramientas: **$0**
- Comisiones Stripe: solo si cobras
- Tiempo de preparación: **2–3 horas**
- Lista y outreach: **4–6 horas**
- Demos: hasta **3,5 horas** para 30 llamadas de 7 minutos, más coordinación
- Duración total: **5–7 días**
- Dinero gastado antes de validar: **$0–20**

El experimento no intenta demostrar que tienes razón. Intenta obligar a 30 compradores reales a decirte “no” con su tarjeta. Si no consigues ni un pago bajo estas condiciones, no mereces dos meses de construcción.