# Qwen 3.8 Max — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 6.44 | quality: 8.0
- latency_total: 349.797s | tokens_per_second: 43.0
- input_tokens: 217 | output_tokens: 15051

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

No construyas nada durante 2 meses.  
El experimento para **MATAR** tu hipótesis no es una encuesta, ni una landing bonita, ni una demo. Es una **preventa manual con dinero real**.

Tu hipótesis:

> “Las agencias de marketing pequeñas pagarían $200/mes por automatizar reportes.”

La única forma seria de falsarla es:

> Si agencias pequeñas, con dolor real de reportes, no están dispuestas a pagar $200 por adelantado con una oferta clara y garantía, la hipótesis está muerta.

---

# Experimento: “Piloto pagado de 5 agencias”

Objetivo: conseguir que agencias reales paguen $200 antes de que exista producto.

No quieres que te digan “qué buena idea”.  
Quieres que paguen o no paguen.

---

## 1. La oferta exacta

Vas a ofrecer esto:

> “Automatizo los reportes mensuales de tu agencia para hasta 5 clientes por $200/mes.  
> Setup en 72 horas.  
> Sin permanencia.  
> Si no te ahorro mínimo 6 horas al mes, te devuelvo el dinero.”

Por qué esta oferta:

- Es específica.
- Tiene precio claro.
- Tiene riesgo reducido.
- Fuerza una decisión.
- No depende de que “les guste” la idea.
- Te permite cobrar antes de construir.

No digas:

> “Estoy creando una herramienta…”

Di:

> “Estoy aceptando 5 agencias para un piloto de automatización de reportes.”

Si alguien paga, luego lo entregas de forma manual, semiautomática o con herramientas existentes: Looker Studio, Google Sheets, Supermetrics, Whatagraph trial, Make, Zapier, etc.

No necesitas construir el SaaS.

---

# 2. Qué tienes que montar

Tiempo: 2-4 horas.  
Coste: $0-$30.

Necesitas:

## a) Link de pago

Usa Stripe o PayPal.

Crea un producto:

- Nombre: “Piloto automatización reportes — primer mes”
- Precio: $200
- Descripción: “Primer mes de automatización de reportes para agencia. Reembolsable si no se ahorran mínimo 6 horas/mes.”

No necesitas suscripción automática si eso te frena. Cobra el primer mes como pago único.

Si alguien paga, ya tienes señal.

## b) Calendly o similar

Para agendar llamadas de 10-15 minutos.

## c) Una página simple

Puede ser Notion, Carr, Google Sites o un documento PDF.

Contenido:

```
Automatización de reportes para agencias de marketing

¿Tu equipo pierde horas armando reportes mensuales para clientes?

Te ayudo a automatizar los reportes de hasta 5 clientes por $200/mes.

Qué incluye:
- Reporte mensual por cliente.
- Conexión de fuentes principales: Google Ads, Meta Ads, GA4, Search Console, etc.
- Entrega en 72 horas.
- Sin permanencia.

Garantía:
Si no te ahorro mínimo 6 horas al mes, te devuelvo el dinero.

Solo 5 cupos para este piloto.

[Pagar $200]
[Agendar llamada]
```

No hagas una web enorme.  
No expliques features.  
No pongas logos falsos.  
No inventes clientes.

## d) Hoja de tracking

Columnas:

- Nombre agencia
- Contacto
- Canal
- Respondió
- Califica
- Horas/mes haciendo reportes
- Llamada agendada
- Llamada hecha
- Pagó
- Motivo de no pago
- Objeción principal

---

# 3. A quién contactar

Tu ICP:

Agencias de marketing pequeñas con:

- 1 a 10 empleados.
- Clientes recurrentes.
- Reportes mensuales o quincenales.
- Dolor operativo haciendo reportes.
- Founder, CEO, Director o responsable de operaciones.

No contactes:

- Grandes agencias.
- Freelancers sin clientes.
- Empresas que solo hacen branding y no manejan performance.
- Gente que no tenga clientes activos.

Necesitas 100 agencias.

Fuentes rápidas:

1. LinkedIn: buscar “founder marketing agency”, “CEO agencia marketing”, “director agencia digital”.
2. Facebook Groups: grupos de agencias, media buyers, marketing digital.
3. Clutch, DesignRush, Sortlist, directorios locales.
4. Instagram/LinkedIn: agencias pequeñas que publican casos pero parecen operar manualmente.
5. Comunidades de Slack/Discord de marketing.

No compres listas caras.  
No gastes en ads.  
No pierdas 3 días haciendo lead scraping perfecto.

Con 100 contactos reales alcanza.

---

# 4. Mensajes de contacto

Vas a usar 3 variantes. No una sola. Así evitas matar la hipótesis por mal copy.

## Variante A: dolor directo

Asunto / primer mensaje:

```
¿Cuántas horas pierde tu agencia armando reportes mensuales?
```

Cuerpo:

```
Hola [Nombre], veo que diriges [Agencia].

Pregunta rápida: ¿cuántas horas pierde tu equipo cada mes armando reportes para clientes?

Estoy aceptando 5 agencias para automatizar esos reportes por $200/mes.

Si no te ahorro mínimo 6 horas/mes, te devuelvo el dinero.

¿Te interesa una llamada de 10 minutos?
[Calendly]
```

## Variante B: oferta directa

```
Hola [Nombre].

Si tu agencia todavía arma reportes manuales para clientes, te ofrezco automatizarlos por $200/mes.

Incluye hasta 5 clientes, setup en 72 horas y garantía de reembolso si no te ahorro mínimo 6 horas/mes.

Solo 5 cupos.

¿Te interesa? Puedes agendar aquí: [Calendly]
```

## Variante C: dolor + escasez

```
Hola [Nombre].

Muchas agencias pequeñas pierden fines de semana armando reportes para clientes.

Estoy lanzando un piloto para automatizar eso: $200/mes, hasta 5 clientes, entrega en 72 horas.

Si no te ahorro mínimo 6 horas/mes, te devuelvo el dinero.

Tengo 5 cupos. ¿Te interesa verlo en 10 minutos?
```

Seguimiento a las 24-48 horas:

```
Hola [Nombre], te escribí por el tema de reportes.

Si no es un dolor real para tu agencia, ignórame.

Si están perdiendo horas cada mes, te puedo mostrar cómo automatizarlo por $200/mes con garantía.

¿Te interesa una llamada corta?
```

---

# 5. La llamada: no vendas humo, cobra

Duración: 10-15 minutos.

Objetivo: calificar y pedir pago.

No hagas una demo larga.  
No prometas lo que no puedas cumplir.  
No regales trabajo.  
No aceptes “me lo pienso” como resultado.

## Guión

### Paso 1: Calificar

Pregunta:

```
¿Hoy cuántas horas al mes dedican a armar reportes para clientes?
```

Si dice menos de 3-4 horas, probablemente no califica.

Pregunta:

```
¿Cuántos clientes requieren reporte mensual?
```

Pregunta:

```
¿Quién los arma? ¿Tú, un account, un analista?
```

Pregunta:

```
¿Qué herramientas usan? ¿Google Ads, Meta, GA4, Looker Studio, Excel, Whatagraph?
```

Califica si:

- Agencia pequeña.
- Decision maker en la llamada.
- Mínimo 3 clientes con reporte.
- Pierde 6+ horas/mes.
- Puede pagar con tarjeta.

Si no califica, no lo cuentes como “no”. Simplemente no es tu muestra.

---

### Paso 2: Hacer el dolor tangible

```
Si pierden 8 horas al mes y tu hora vale $40, son $320/mes.
Si tu hora vale $60, son $480/mes.
Además del riesgo de errores, retrasos y clientes preguntando.
```

No discutas. Solo haz visible el costo.

---

### Paso 3: Oferta

```
Te propongo esto: por $200/mes te automatizo los reportes de hasta 5 clientes.
Setup en 72 horas.
Sin permanencia.
Si no te ahorro mínimo 6 horas al mes, te devuelvo el dinero.
```

---

### Paso 4: Cerrar con pago

```
Para reservar uno de los 5 cupos, te envío el link de pago ahora.
¿Prefieres pagar con tarjeta directamente?
```

Envías el link en vivo.

Si dice “sí”, pero no paga en la llamada:

```
Perfecto. Te lo dejo activo por 24 horas. Si mañana no está pagado, libero el cupo.
```

Solo cuenta como válido si:

- Paga en la llamada.
- Paga dentro de 24 horas.
- Deja tarjeta autorizada de forma real.
- O hace transferencia inmediata.

“Me interesa” = 0.  
“Mándame propuesta” = 0.  
“Lo hablo con mi socio” = 0.  
“Cuando tenga más clientes” = 0.  
“Suena bien” = 0.

---

# 6. Si te piden demo

No tienes producto. No mientas.

Puedes decir:

```
No es una demo tradicional porque es un piloto. Puedo mostrarte un ejemplo de reporte automatizado y explicarte el proceso. Si te encaja, reservas el cupo. Si no, no pasa nada.
```

Puedes tener un reporte de ejemplo hecho con Looker Studio y datos dummy.

Pero no construyas nada complejo.

---

# 7. Kill criteria: cuándo abandonar

Aquí está la parte importante.

## Regla principal de abandono

> Si hablas con 10 agencias calificadas y ninguna paga $200 o deja tarjeta autorizada en menos de 24 horas, abandona la idea.

Eso es:

```
0 pagos / 10 llamadas calificadas = abandonar.
```

Ese es el resultado que mata la hipótesis.

---

## Regla un poco más robusta

Si consigues 1 pago, no celebres ni construyas todavía.

Haz 5 llamadas calificadas más.

Abandona si:

```
<= 1 pago / 15 llamadas calificadas
```

En resumen:

| Resultado | Decisión |
|---|---|
| 0 pagos en 10 llamadas calificadas | Abandona |
| 1 pago en 10 llamadas | Haz 5 llamadas más |
| 1 pago o menos en 15 llamadas | Abandona |
| 2+ pagos en 15 llamadas | No está muerta; sigue, pero manual |

---

## Segundo motivo de abandono

Si después de contactar 150 agencias con 3 mensajes distintos no consigues al menos 10 llamadas calificadas, también abandona o pausa.

Eso indica:

- El problema no es lo suficientemente urgente.
- No sabes llegar al cliente.
- El mensaje no conecta.
- O el segmento no tiene el dolor que supones.

Para una herramienta de $200/mes, necesitas demanda clara. Si no puedes conseguir 10 conversaciones calificadas, mala señal.

---

# 8. Qué cuenta como “pago”

Solo cuenta si:

- Pagó $200.
- Dejó tarjeta cargada.
- Hizo transferencia.
- Aceptó pago con link y se procesó.

No cuenta si:

- Dijo que sí.
- Dijo “me parece útil”.
- Pidió propuesta.
- Dijo “escríbeme el mes que viene”.
- Dijo “si tuviera más clientes, sí”.
- Dijo “¿me lo haces gratis primero?”.
- Dijo “¿puedo probarlo?”.
- Dijo “cuando tenga tiempo lo vemos”.

Eso no valida nada.

---

# 9. Qué hacer si alguien paga

No construyas el SaaS.

Entrega manual o semiautomático:

1. Pide accesos: Google Ads, Meta, GA4, Search Console, etc.
2. Pide logo, colores y estructura mínima.
3. Arma un reporte con Looker Studio, Sheets, Whatagraph trial, Power BI, Make/Zapier o lo que puedas.
4. Entrega en 72 horas.
5. Pregunta: “¿Cuántas horas te ahorró esto?”
6. Si no ahorras 6 horas, devuelve el dinero.

Si 2-3 agencias pagan y se quedan después del primer mes, recién ahí puedes pensar en construir.

Pero no antes.

---

# 10. Coste exacto

## Dinero

Versión mínima:

- Stripe/PayPal: $0 fijo. Solo comisión si cobras.
- Calendly: $0.
- Notion/Carr/Google Sites: $0.
- Dominio opcional: $10.
- Email profesional opcional: $5-$10.
- Sales Navigator trial: $0 si cancelas.
- Facebook groups / LinkedIn free: $0.

Total realista:

```
$0 - $30
```

Si alguien paga y luego pides reembolso, puedes perder la comisión de Stripe/PayPal: unos $3-$6 por pago.

Aun así, el experimento cuesta menos de $50.

---

## Tiempo

Estimación:

- Montar oferta, link, página y tracking: 3 horas.
- Conseguir 100 agencias: 2 horas.
- Enviar mensajes y follow-ups: 3 horas repartidas en 3 días.
- Llamadas: 15 minutos x 10 = 2.5 horas.
- Análisis: 1 hora.

Total:

```
10-12 horas de trabajo
5 días calendario
```

Si usas la extensión de 15 llamadas:

```
7-10 días calendario
```

---

# 11. Resultado que te hace abandonar

La respuesta corta:

> Abandona si contactas 100 agencias, consigues 10 llamadas calificadas con agencias que realmente pierden tiempo haciendo reportes, y ninguna paga $200 o deja tarjeta en 24 horas.

Eso mata la hipótesis.

No porque “no les gustó”.  
Sino porque con una oferta clara, precio claro, riesgo reducido y dolor identificado, nadie quiso poner dinero.

Si eso pasa, no construyas durante 2 meses.

---

# 12. Errores que invalidan el experimento

No hagas esto:

## 1. Preguntar “¿pagarías?”

No. Pide pago.

## 2. Contactar amigos

No. Tienen sesgo de simpatía.

## 3. Aceptar “me interesa” como validación

No. Interés sin dinero es ruido.

## 4. Bajar el precio a $50

No. Tu hipótesis es $200/mes. Si solo pagan $50, esa hipótesis murió.

## 5. Dar gratis el piloto

No. Gratis no testea disposición a pagar.

## 6. Construir algo antes de cobrar

No. Primero dinero.

## 7. Hacer una landing con tráfico frío

No. Eso añade ruido. Haz outbound directo primero.

## 8. No calificar

Si hablas con agencias que no hacen reportes, el resultado no sirve.

## 9. No pedir pago en la llamada

Si no pides pago, no estás testeando nada.

---

# 13. Resumen ejecutivo

Experimento:

```
Preventa manual de un piloto de automatización de reportes para agencias pequeñas.
```

Oferta:

```
$200/mes, hasta 5 clientes, setup 72h, garantía de reembolso si no ahorras 6h/mes.
```

Muestra:

```
100 agencias contactadas.
10 llamadas calificadas.
```

Métrica:

```
Pagos reales o tarjeta autorizada.
```

Kill criteria:

```
0 pagos / 10 llamadas calificadas = abandonar.
<=1 pago / 15 llamadas calificadas = abandonar.
```

Coste:

```
$0-$30
```

Tiempo:

```
5 días
```

Si consigues 2+ pagos, no construyas todavía: entrega manual y observa si se quedan.  
Si consigues 0 pagos, ahórrate los 2 meses de desarrollo.