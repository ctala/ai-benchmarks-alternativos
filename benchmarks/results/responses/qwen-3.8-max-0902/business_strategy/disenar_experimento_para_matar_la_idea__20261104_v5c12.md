# Qwen 3.8 Max 0902 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 6.42 | quality: 8.0
- latency_total: 418.973s | tokens_per_second: 41.6
- input_tokens: 217 | output_tokens: 17430

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento para MATAR la hipótesis: “Cobra antes de construir”

Tu hipótesis no se valida con “me interesa”.  
Se mata o se valida con **dinero real**.

El experimento más barato y rápido no es una landing con ads, ni una encuesta, ni una demo. Es esto:

> **Vender un piloto de $200/mes a agencias pequeñas antes de construir la herramienta.**  
> Si no pagan, la hipótesis está muerta.

---

## Resumen ejecutivo

| Pregunta | Respuesta |
|---|---|
| **Qué vas a hacer** | Contactar agencias pequeñas, ofrecer un piloto de automatización de reportes por $200/mes y pedir pago del primer mes. |
| **Coste** | $0-$30. |
| **Tiempo** | 5 días hábiles. |
| **Métrica de muerte** | Menos de 2 pagos reales de $200 después de 20 conversaciones cualificadas. |
| **Resultado que te hace abandonar** | Si tras 20 cierres con dueños/directores de agencias cualificadas tienes 0 o 1 pago real, abandonas. |

---

# 1. La regla del experimento

No quieres confirmar que tu idea suena bien.  
Quieres descubrir si alguien está dispuesto a pagar.

Por tanto:

- “Me interesa” = **no cuenta**.
- “Suena útil” = **no cuenta**.
- “Mándame información” = **no cuenta**.
- “Cuando lo tengas me avisas” = **no cuenta**.
- “Te lo pagaría si fuera más barato” = **no cuenta para $200/mes**.
- “Sí, pero gratis/prueba” = **no cuenta**.
- **Pago real o tarjeta cargada = cuenta.**

---

# 2. Qué vendes exactamente

No vendas una herramienta terminada si no existe. Eso es engañoso y además ensucia el experimento.

Vende un **piloto fundador**:

> “Reportes automáticos para tus clientes por $200/mes, sin permanencia, con garantía de 7 días.”

Puedes decirlo así:

> “Estoy seleccionando 5 agencias pequeñas para un piloto de reportes automáticos. La idea es que tus clientes reciban reportes de campañas/analítica sin que tu equipo los arme manualmente. Cuesta $200/mes, sin permanencia. Si en 7 días no ves valor, te devuelvo el dinero.”

No prometas features infinitas.

Promesa simple:

- Reporte automático o semi-automático.
- Para clientes de la agencia.
- Con datos de fuentes típicas: Google Ads, Meta Ads, GA4, etc.
- Entrega semanal o mensual.
- Ahorro de tiempo operativo.
- Precio: $200/mes.
- Garantía: 7 días.
- Sin permanencia.

Si alguien paga, luego puedes entregarlo manualmente, con Looker Studio, Sheets, Make/Zapier, plantillas, o herramientas existentes. Eso no importa ahora. El experimento es saber si pagan.

---

# 3. Perfil exacto de agencia cualificada

No hables con cualquiera. Necesitas agencias que realmente puedan necesitar esto.

Cualificada:

- Agencia pequeña: 1-10 personas.
- Con al menos 3 clientes activos.
- Que entregue reportes a clientes mensual o semanalmente.
- Hablas con dueño/a, CEO, director/a, responsable de operaciones o marketing.
- No es amigo, familiar ni alguien que te quiere ayudar.

No cualificada:

- Freelancer sin clientes recurrentes.
- Agencia grande con equipo de BI.
- Empresa que no hace reporting para clientes.
- Junior que no decide.
- Conocido que te dice “sí” por quedar bien.

---

# 4. Infraestructura mínima

No construyas producto.

Solo necesitas:

1. **Lista de 60 agencias.**
2. **Mensaje de contacto.**
3. **Calendly o similar gratis.**
4. **Stripe Payment Link o PayPal para cobrar $200.**
5. **Una página simple opcional**, pero no necesaria.

Coste:

- Stripe: $0 hasta que cobras.
- Calendly: gratis.
- Notion/Carrd/Google Docs: gratis.
- LinkedIn/Google Maps/Clutch: gratis.
- Opcional: dominio $10.
- Opcional: LinkedIn Sales Navigator trial $0, cancelas.

Presupuesto máximo recomendado: **$30**.

---

# 5. Plan de ejecución en 5 días

## Día 1: Preparación y primeros 30 contactos

Haz esto:

1. Define la oferta en una frase.
2. Crea link de pago de $200 en Stripe.
3. Crea Calendly.
4. Arma lista de 60 agencias.
5. Envía 30 mensajes.

Fuentes para encontrar agencias:

- Google Maps: “agencia de marketing + ciudad”.
- LinkedIn: “fundador agencia marketing”, “CEO agencia digital”, “director agencia performance”.
- Clutch.co.
- Instagram: agencias pequeñas que publican casos.
- Directorios locales.
- Grupos de Facebook/Slack/Discord de agencias, si tienes acceso.

Objetivo del día:

- 60 leads identificados.
- 30 mensajes enviados.

---

## Día 2: 30 contactos más y follow-ups

Envía 30 mensajes nuevos.

Haz follow-up a los del día anterior.

Objetivo:

- 60 mensajes enviados en total.
- Agendar 5-8 llamadas.

---

## Día 3: Llamadas y cierre

Haz llamadas.

No hagas demos largas.  
No hagas “consultoría gratis”.  
No preguntes “¿qué te parecería?”.

Tu objetivo es cerrar:

> “¿Pagas $200/mes por este piloto?”

Objetivo:

- 10 conversaciones cualificadas acumuladas.

---

## Día 4: Más llamadas y follow-ups agresivos

Continúa llamadas.

Follow-up corto:

> “Hola [Nombre], ¿pudiste revisar el piloto? Necesito cerrar los cupos hoy. ¿te envío el link de pago o prefieres no avanzar?”

Objetivo:

- 15 conversaciones cualificadas acumuladas.

---

## Día 5: Cierre final

Envía último mensaje:

> “[Nombre], cierro hoy los cupos del piloto. Si quieres entrar, el pago del primer mes es $200 y te garantizo devolución en 7 días si no ves valor. ¿te paso el link?”

Objetivo final:

- 20 conversaciones cualificadas con precio puesto.
- Decisión: matar o continuar.

---

# 6. Mensaje exacto para contactar

## Mensaje frío por LinkedIn/email

Asunto:

> Reportes de clientes

Mensaje:

> Hola [Nombre], veo que lideras [Agencia].  
>   
> Estoy seleccionando 5 agencias pequeñas para un piloto: reportes automáticos para clientes por $200/mes, sin permanencia y garantía de 7 días.  
>   
> Si hoy pierden horas armando reportes manualmente, puede interesarles.  
>   
> ¿Tienes 10 minutos mañana?

Versión más directa:

> Hola [Nombre]. Estoy lanzando un piloto para agencias pequeñas: reportes automáticos para clientes por $200/mes. Sin permanencia. Garantía 7 días.  
>   
> Si en tu agencia todavía arman reportes manualmente, ¿te interesa verlo 10 minutos?

No mandes un PDF.  
No mandes un deck.  
No mandes un video largo.

Solo busca conversación.

---

## Follow-up 1, después de 24h

> Hola [Nombre], ¿viste el mensaje? Si no es prioridad, no pasa nada. Solo cierro cupos esta semana.

---

## Follow-up 2, después de 48h

> [Nombre], último mensaje: si los reportes de clientes siguen siendo manuales y consumen horas, el piloto de $200/mes puede ahorrarles tiempo. Si no, no insisto. ¿te interesa?

---

# 7. Guion exacto de la llamada

La llamada debe durar 10-15 minutos.

No es una demo.  
Es una llamada de cualificación y cierre.

## Parte 1: Cualificar

Pregunta:

1. “¿Cuántos clientes activos manejan?”
2. “¿Cada cuánto entregan reportes?”
3. “¿Quién los arma hoy?”
4. “¿Cuántas horas al mes dirías que pierden en reportes?”
5. “¿Qué herramientas usan?”
6. “¿El reporting lo cobran aparte o está incluido en el fee?”

Descalifica si:

- No tienen clientes activos.
- No hacen reportes.
- No les duele.
- No tienen presupuesto.
- No decide.
- Te dice que ya lo resuelve gratis con Looker Studio y no pagaría por mejorarlo.

---

## Parte 2: Presentar la oferta

Di:

> “Perfecto. Lo que estoy haciendo es un piloto para agencias pequeñas: dejamos reportes automáticos para tus clientes, con datos de fuentes como Google Ads, Meta, GA4, etc., para que tu equipo no tenga que armarlos manualmente.  
>   
> El precio del piloto es $200/mes, sin permanencia. Setup gratis para los primeros cupos. Si en 7 días no ves valor, te devuelvo el dinero.”

No te extiendas.

---

## Parte 3: Cerrar

Di:

> “Para reservar el cupo necesito el pago del primer mes. Te paso el link ahora. ¿Lo hacemos con tarjeta?”

Silencio.

No bajes precio.  
No ofrezcas gratis.  
No digas “luego lo vemos”.

---

## Objeciones comunes y respuesta

### “Me interesa, mándame info.”

> “Claro, te mando el link de pago y una explicación corta. Pero el cupo se reserva con el pago. Si quieres entrar, tendríamos que hacerlo hoy.”

Si no paga, no cuenta.

---

### “Necesito pensarlo.”

> “Perfecto. ¿Qué necesitas para decidir hoy? Si no puedes decidir hoy, no pasa nada, pero no puedo reservar el cupo sin pago.”

Si no paga, no cuenta.

---

### “¿Me lo dejas probar gratis?”

> “No tengo prueba gratis. Es un piloto pago de $200/mes, pero con garantía de 7 días. Si no ves valor, te devuelvo el dinero.”

Si solo acepta gratis, hipótesis de $200/mes muerta.

---

### “¿Puedes hacer descuento?”

> “El precio del piloto es $200/mes. No tengo descuento. Si más adelante hay otro plan, te aviso.”

Si solo paga con descuento fuerte, la hipótesis original muere.

---

### “Ya lo hacemos con Looker/Data Studio.”

> “Entiendo. ¿ese proceso les consume tiempo igualmente? ¿Pagarían $200/mes por reducirlo?”

Si dice no, no cuenta.

---

### “Ya usamos AgencyAnalytics/Whatagraph/Swante/DashThis.”

> “¿Están contentos? ¿Pagarían $200/mes por cambiar o mejorar eso?”

Si no, no cuenta.

---

### “Cuando lo tengas listo me avisas.”

> “Perfecto, pero el piloto es ahora. Si quieres entrar, es con pago hoy. Si no, no te molesto más.”

Si no paga, no cuenta.

---

# 8. Qué cuenta como victoria real

Solo cuenta si:

1. Es una agencia cualificada.
2. Hablaste con decisor.
3. Escuchó el precio exacto: $200/mes.
4. No fue amigo/familiar.
5. Pagó el primer mes o dejó tarjeta cargada.
6. No pidió reembolso inmediato.
7. Responde al onboarding básico en 48h.

Onboarding básico:

- Te dice qué cliente usar primero.
- Te da accesos o acepta recibir el primer reporte.
- Agenda kickoff.
- Responde.

Si alguien paga pero desaparece, reembolsa y no lo cuentes.

---

# 9. Resultado exacto que mata la hipótesis

Aquí está la regla dura:

> **Si después de 20 conversaciones cualificadas con dueños/directores de agencias pequeñas, con precio explícito de $200/mes y cierre directo, tienes menos de 2 pagos reales, abandonas la idea.**

Eso significa:

- 0 pagos: abandonas.
- 1 pago: abandonas.
- 2 pagos: no está muerta, pero tampoco construyas todavía.
- 3+ pagos: señal más fuerte, pero sigue sin construir 2 meses.

¿Por qué menos de 2 pagos mata?

Porque un pago puede ser:

- un favor;
- una anomalía;
- alguien educado;
- alguien que entendió otra cosa;
- un cliente mal cualificado.

Dos pagos independientes son una señal mínima de que existe demanda real.

---

# 10. Otras señales que también matan la idea

Abandona también si:

### 1. Todos te dicen “interesante” pero nadie paga

Eso es educación, no demanda.

---

### 2. Solo aceptarían gratis

Si la única forma de conseguir interés es con prueba gratis, la hipótesis de $200/mes está muerta.

---

### 3. Solo pagarían $50 o menos

Puede ser otro negocio, pero tu hipótesis era $200/mes. Si solo pagan $50, la hipótesis original murió.

---

### 4. Te piden mil features antes de pagar

Si no pagan por la promesa simple, no están comprando el problema. Están negociando un proyecto custom.

---

### 5. No consigues conversaciones cualificadas

Si después de 7 días y 80-100 contactos no conseguiste al menos 15 conversaciones con dueños/directores de agencias pequeñas, también hay un problema serio de acceso/mercado/canal.

Para una herramienta de $200/mes, si no puedes hablar manualmente con tu mercado, difícilmente podrás escalar.

---

# 11. Cuánto cuesta y cuánto tarda

## Coste

Versión mínima:

- $0 si usas herramientas gratuitas.

Versión profesional rápida:

- Dominio: $10.
- Carrd o landing simple: $0-$19.
- Stripe: $0 hasta cobrar.
- Calendly: $0.
- LinkedIn/Google/Clutch: $0.

Total: **$0-$30**.

No gastes en ads.  
No gastes en branding.  
No gastes en logo.  
No gastes en desarrollo.

---

## Tiempo

- Preparación: 2-3 horas.
- Ejecución: 2-3 horas/día durante 5 días.
- Total: 12-18 horas en 5 días hábiles.

Si ya tienes contactos de agencias, puede estar en 48-72 horas.

---

# 12. Qué no debes hacer

## No construyas nada

Ni MVP.  
Ni dashboard.  
Ni backend.  
Ni integración.  
Ni base de datos.  
Ni 2 meses de desarrollo.

---

## No hagas encuestas

“¿Pagarías $200/mes?” en una encuesta no sirve.  
La gente miente por quedar bien.

---

## No preguntes si les gusta

“¿Te gusta?” no valida pago.

---

## No ofrezcas descuento

Si bajas a $99, $49 o gratis, contaminas el test de $200/mes.

---

## No aceptes “sí” verbales

Sí sin dinero = no.

---

## No cuentes amigos

Si tu amigo te paga para ayudarte, no cuenta.

---

## No hagas una demo falsa

No digas que el producto existe si no existe.  
Di que es un piloto.

---

# 13. Si el experimento no mata la idea, todavía no construyas

Si consigues 2 o más pagos, no te metas 2 meses a programar.

Haz esto:

1. Cobra.
2. Entrega manualmente o con herramientas existentes.
3. Onboarding rápido.
4. Entrega el primer reporte en 7 días.
5. Pregunta: “¿Esto te ahorra tiempo real?”
6. Intenta cobrar el segundo mes.

Si después del primer mes:

- pagan el segundo mes;
- te dan más clientes;
- te piden más fuentes;
- no piden reembolso;
- no te exigen desarrollo custom imposible;

entonces recién tienes permiso para construir algo más serio.

Si piden reembolso, se quejan, no usan el reporte o no renuevan, la hipótesis sigue muerta.

---

# 14. Frase final para tu decisión

Tu experimento no es:

> “¿Las agencias dicen que pagarían?”

Tu experimento es:

> “¿Dos agencias reales, cualificadas y sin relación personal me pagan $200/mes por una promesa de reportes automáticos?”

Si la respuesta es no:

> **Abandonas.**

No porque la idea sea mala para siempre, sino porque para ti, en este momento, con ese precio y ese segmento, no hay evidencia suficiente para quemar 2 meses construyendo.