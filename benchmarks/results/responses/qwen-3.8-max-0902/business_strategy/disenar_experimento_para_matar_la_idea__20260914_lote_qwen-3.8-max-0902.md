# Qwen 3.8 Max 0902 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 6.41 | quality: 8.0
- latency_total: 509.192s | tokens_per_second: 35.0
- input_tokens: 217 | output_tokens: 17816

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

No construyas nada durante 2 meses.  
Haz una **preventa manual / concierge** de la herramienta antes de que exista.

El experimento no es preguntar “¿pagarías?”.  
Eso no mata hipótesis.  
El experimento es: **pedir $200 reales por adelantado** por una versión manual del servicio.

Si no pagan ni siquiera cuando tú haces el trabajo por ellos, con garantía y fricción baja, difícilmente pagarán por un software que aún no existe.

---

## Experimento: “Vender el reporte antes de automatizarlo”

### Hipótesis que quieres matar

> Las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice reportes a clientes.

### Versión falsable

> Si ofrezco reportes de clientes listos en 24 horas por $200/mes, con garantía de devolución, a agencias pequeñas que hoy hacen reportes manualmente, al menos unas pocas pagarán el primer mes por adelantado.

### Por qué este test puede matar la idea

Ataca los supuestos más débiles:

1. ¿Realmente les duele el problema?
2. ¿Están dispuestas a pagar $200/mes?
3. ¿El problema es lo suficientemente urgente?
4. ¿Puedes llegar a ellas sin gastar una fortuna?
5. ¿Tu promesa es clara?

Si no pagan cuando les quitas riesgo, no construyas.

---

# El experimento exacto

## 1. Define un segmento muy específico

No hables con “agencias” en general. Elige un nicho donde el dolor de reportes sea evidente.

### ICP recomendado para el test

Agencias pequeñas que cumplan esto:

- 2 a 10 personas.
- Manejan clientes activos.
- Al menos 3 clientes.
- Hacen reportes mensuales o semanales.
- Usan Google Ads, Meta Ads, GA4, SEO o redes sociales.
- El fundador/CEO/director puede decidir sin comité.
- Actualmente hacen reportes manualmente o con hojas sueltas.

### Mejor subnicho para empezar

Agencias de performance marketing / paid media pequeñas.

Ejemplo:

> Agencias de 2-10 personas que gestionan campañas en Google Ads y Meta Ads para clientes.

¿Por qué?  
Porque suelen tener datos medibles, clientes que piden resultados y dolor recurrente de reporting.

---

# 2. La oferta que vas a vender

No vendas “una herramienta”.  
Vende el resultado.

## Oferta piloto

> “Reportes de clientes listos en 24 horas para tu agencia.  
> Piloto para 5 agencias: $200/mes. Incluye hasta 3 clientes. Si no te ahorra al menos 5 horas al mes, te devuelvo el primer mes.”

### Entregable

Durante el piloto, tú entregarás manualmente:

- 1 reporte mensual por cliente.
- Hasta 3 clientes por agencia.
- Métricas básicas: gasto, leads, conversiones, CTR, CPC, ROAS, tráfico, engagement, según el canal.
- Formato: PDF, Looker Studio o Google Slides.
- Marca blanca con logo de la agencia.
- Entrega en menos de 24 horas desde que te dan acceso a los datos.

### Importante

No construyas software.

Si alguien paga, resuélvelo con:

- Looker Studio.
- Google Sheets.
- Plantillas.
- Zapier/Make solo si es muy rápido.
- Extracción manual de datos si hace falta.

El objetivo no es escalar.  
Es descubrir si alguien paga.

---

# 3. Lo único que necesitas montar

No necesitas web bonita.  
No necesitas producto.  
No necesitas demo.  
No necesitas logo.

Necesitas:

1. Una lista de 100 agencias.
2. Una página simple con precio y botón de pago.
3. Un link de pago de Stripe, PayPal o transferencia.
4. Un calendario para llamadas de 10-15 minutos.
5. Un guion de contacto.

## Página simple

Puede ser Notion, Carrd, Framer, Google Docs o una página básica.

### Copy sugerido

**Título:**  
Reportes de clientes listos en 24 horas para tu agencia

**Subtítulo:**  
Piloto para 5 agencias. Entregamos reportes marca blanca de hasta 3 clientes por $200/mes. Si no te ahorra al menos 5 horas al mes, te devolvemos el primer mes.

**Qué incluye:**

- Reportes mensuales para hasta 3 clientes.
- Datos de Google Ads, Meta Ads, GA4 o redes sociales.
- Entrega en menos de 24 horas desde que nos das acceso.
- Formato marca blanca.
- Sin permanencia.
- Garantía de devolución del primer mes si no te ahorra tiempo.

**Precio:**  
$200/mes

**CTA:**  
Pagar $200 y reservar cupo

**Nota:**  
Solo 5 cupos para el piloto.

No pongas features infinitas.  
No pongas “próximamente”.  
No pongas “únete a la lista”.  
Pon precio y pago.

---

# 4. Consigue 100 agencias

No compres bases gigantes. Hazlo manual.

### Fuentes rápidas

- LinkedIn.
- Clutch.
- Directorios de agencias.
- Google Maps.
- Grupos de Facebook de agencias.
- Comunidades de marketing.
- Instagram/Twitter buscando “agencia marketing”.
- Tu propia red si tienes contactos.

### Cómo elegir

Busca:

- “Founder”, “CEO”, “Director”, “Managing Director”.
- Agencias pequeñas.
- Que digan que trabajan con clientes.
- Que no sean enterprise.
- Que no tengan pinta de tener departamento de data enorme.

### Meta

100 contactos válidos.

Cada contacto debe tener:

- Nombre del dueño/decisor.
- Agencia.
- Email o LinkedIn.
- Motivo mínimo de personalización.

Ejemplo:

> “Vi que trabajan con clientes de e-commerce / salud / real estate / servicios.”

---

# 5. El mensaje de contacto

No preguntes si les interesa una idea.  
Ofrece el piloto con precio.

## Email 1

**Asunto:** ¿Cuántas horas pierde [Nombre Agencia] en reportes?

**Cuerpo:**

> Hola [Nombre],
>
> Vi que en [Agencia] gestionan campañas/clientes para [tipo de cliente o industria].
>
> Estoy abriendo 5 cupos para un piloto: entregamos reportes marca blanca de hasta 3 clientes en menos de 24 horas por $200/mes.
>
> Si no te ahorra al menos 5 horas al mes, te devuelvo el primer mes.
>
> Si esto es una prioridad para ti, responde “PILOTO” y te mando el link de pago.
>
> Si prefieres, agenda 10 minutos aquí: [link].
>
> [Tu nombre]

No mandes PDF de 10 páginas.  
No mandes deck.  
No mandas propuesta.  
Mandas una oferta concreta.

---

## Follow-up 1, día +2

**Asunto:** ¿Siguen haciendo reportes manualmente?

> Hola [Nombre],
>
> Te escribí porque estoy cerrando los 5 cupos del piloto de reportes para agencias.
>
> Si hoy están perdiendo horas armando reportes para clientes, esto les puede ahorrar 5+ horas al mes por $200.
>
> ¿Te interesa que te reserve un cupo?

---

## Follow-up 2, día +4

**Asunto:** Cierro hoy

> Hola [Nombre],
>
> Cierro hoy los cupos del piloto.
>
> Si los reportes no son un dolor importante para [Agencia], dime “NO” y no vuelvo a escribir.
>
> Si sí lo son, te mando el link de pago y empezamos esta semana.

---

## LinkedIn message corto

> Hola [Nombre], estoy seleccionando 5 agencias pequeñas para un piloto: reportes de clientes listos en 24h por $200/mes. Si no les ahorra 5 horas al mes, devuelvo el primer mes. ¿Es algo que les sirva ahora?

---

# 6. La llamada de cierre

No hagas una entrevista de producto.  
Haz una llamada de venta y calificación.

Duración: 10-15 minutos.

## Guion

### 1. Dolor actual

> “¿Hoy quién arma los reportes de clientes?”

> “¿Cuántas horas al mes se van en eso?”

> “¿Para cuántos clientes?”

> “¿Qué herramientas usan?”

> “¿Qué pasa si el reporte llega tarde o con errores?”

### Calificación

Si responden:

- “No nos toma tiempo.”
- “Ya tenemos un equipo.”
- “El cliente no pide reportes.”
- “Usamos un dashboard y ya está.”
- “No es un problema.”

Entonces no califica. No lo cuentes como demanda.

Si dicen:

- “Nos toma 8-20 horas al mes.”
- “Lo hace el account manager.”
- “Siempre estamos corriendo.”
- “El cliente pregunta y no tenemos visibilidad.”
- “Es un desorden.”

Ese sí califica.

---

### 2. Oferta

> “Te propongo esto: durante el piloto, me das acceso a hasta 3 cuentas de clientes. En menos de 24 horas te entregamos el reporte mensual marca blanca. Cuesta $200 al mes. Si no te ahorra al menos 5 horas al mes, te devuelvo el primer mes. ¿Empezamos?”

### 3. Cierre

> “Perfecto. Te mando ahora mismo el link de pago. En cuanto quede el pago, te mando el formulario de onboarding para acceder a las cuentas.”

No digas:

> “Te mando propuesta.”

No digas:

> “Lo piensas y me dices.”

No digas:

> “Cuando tengas tiempo.”

El test es dinero.

Si dicen “sí” pero no pagan, no cuenta.

---

# 7. Manejo de objeciones

## “Mándame más información”

> “Claro. La info principal es esta: $200/mes, hasta 3 clientes, entrega en 24h, garantía de devolución del primer mes. Si te encaja, te reservo cupo. Si no, no pasa nada.”

No conviertas la llamada en una clase.

---

## “Necesito pensarlo”

> “Entiendo. Solo para saber si lo descarto: ¿el problema de reportes es prioridad hoy o no?”

Si dice que sí pero no paga, cuenta como no.

---

## “¿Me lo puedes hacer gratis?”

> “No. Es un piloto pago porque el compromiso es real. Si funciona, continúas. Si no, te devuelvo el primer mes.”

Gratis no valida $200/mes.

---

## “¿Puedes hacerlo para 20 clientes?”

> “Para el piloto solo hasta 3 clientes. Si funciona, luego vemos más volumen.”

No te metas en custom enterprise.

---

## “¿Ya está automatizado?”

Sé transparente:

> “Es un piloto de entrega asistida. El objetivo es validar el flujo y el valor antes de automatizarlo completamente. Tú recibes el reporte listo.”

No mientas.  
No vendas humo.  
Pero tampoco pidas permiso para construir.

---

## “¿Puedes integrar HubSpot / CRM / TikTok / Shopify?”

> “En el piloto solo trabajamos con Google Ads, Meta Ads y GA4. Si necesitas otra fuente, por ahora no califica.”

Si la mayoría exige integraciones custom, la hipótesis de herramienta simple de $200/mes se debilita mucho.

---

# 8. Métricas que importan

No midas:

- Likes.
- “Me interesa”.
- “Suena bien”.
- “Escríbeme cuando esté listo”.
- “Qué buena idea”.
- Reuniones sin pago.

Solo midas:

## Métrica principal

**Pagos reales de $200.**

No promesas.  
No LOIs.  
No “te pago después”.  
No “me lo mandas y te transfiero”.

Pago recibido.

---

## Métricas secundarias

- Contactados: 100.
- Respuestas: cuántas.
- Conversaciones calificadas: cuántas.
- Llamadas realizadas: cuántas.
- Pagos: cuántos.
- Objeción principal: precio, confianza, integración, timing, ya lo resuelven.

---

# 9. Coste del experimento

## Versión mínima

- Notion/Carrd free: $0.
- Stripe/PayPal: $0 hasta que cobras.
- Calendly free: $0.
- Gmail: $0.
- LinkedIn free: $0.
- Lista manual: $0.

**Coste total: $0 en efectivo.**

## Versión mínimamente profesional

- Dominio: $10-$15.
- Email profesional: $0-$6.
- Carrd Pro opcional: $19/año.

**Coste máximo razonable: $20-$40.**

No gastes más.

Si compras una base de datos cara, estás procrastinando.

---

# 10. Tiempo

## Día 1: Setup

- Definir oferta: 1 hora.
- Crear landing simple: 1 hora.
- Crear link de pago: 30 minutos.
- Armar lista de 100 agencias: 2-3 horas.
- Escribir mensajes: 30 minutos.

Total: 5 horas.

## Días 2-4: Outreach

- Contactar 50 agencias.
- Contactar otras 50.
- Hacer follow-ups.
- Agendar llamadas.

Total: 4-6 horas.

## Días 5-7: Llamadas y cierre

- Hacer llamadas.
- Mandar links de pago.
- Hacer follow-up a pagos pendientes.
- Cerrar pilotos.

Total: 4-6 horas.

## Día 8: Decisión

Si no hay pagos, abandonas.

Si hay pagos, entregas manualmente el primer reporte y observas reembolso/uso.

**Tiempo total para matar la idea: 7 días.**  
**Tiempo total si hay pagos y quieres confirmar reembolso: 14 días.**

---

# 11. Regla de abandono

Esta es la parte importante.

Antes de empezar, escribe esto:

> Si después de contactar 100 agencias calificadas y tener al menos 10 conversaciones reales con dueños/decision-makers, obtengo menos de 2 pagos reales de $200, abandono la idea tal como está formulada.

## Resultado que te hace abandonar

Abandonas si ocurre cualquiera de estos:

### 1. No consigues conversaciones

Contactas 100 agencias correctas, haces 3-4 toques, y no logras al menos 10 conversaciones calificadas.

Interpretación:

- El segmento no está accesible.
- El mensaje no conecta.
- El dolor no es tan urgente.
- O el canal hace inviable un producto de $200/mes.

Para tu objetivo: abandona o cambia radicalmente el segmento. No construyas.

---

### 2. Conversan pero no pagan

Tienes 10+ conversaciones calificadas y obtienes:

- 0 pagos: muerto.
- 1 pago: no construyas. Es demasiado débil.
- Menos de 2 pagos: abandona la hipótesis principal.

Para que un pago cuente:

- Debe ser de una agencia real.
- Debe cumplir el ICP.
- Debe ser un decisor.
- No puede ser tu amigo, familiar o contacto cercano que te quiere ayudar.
- Debe pagar $200 reales.
- Debe aceptar las condiciones del piloto.

---

### 3. Pagan pero piden reembolso

Si consigues pagos, pero:

- 50% o más pide reembolso antes del día 7,
- o no te dan acceso a datos,
- o no usan el reporte,
- o dicen que no les ahorró tiempo,

entonces también abandonas.

Eso significa que había curiosidad, pero no dolor suficiente.

---

# 12. Qué resultado sí justifica seguir

No te emociones con poco.

Para seguir, mínimo quiero ver:

- 2 pagos reales de $200.
- Agencias que cumplen el ICP.
- Sin relación personal.
- Sin descuento.
- Sin promesas de pago futuro.
- Sin “cuando tenga presupuesto”.
- Sin custom excesivo.

Incluso con 2 pagos, todavía no construyas.

Haz esto:

1. Entrega manualmente durante 30 días.
2. Mide cuánto tiempo te toma.
3. Pregunta si continuarían.
4. Cobra el segundo mes.
5. Si al menos 1-2 renuevan sin pelear, recién piensa en automatizar.

Si 2 pagan pero no renuevan, la hipótesis de $200/mes sigue muerta.

---

# 13. Señales cualitativas que también matan la idea

Además del pago, presta atención a estas respuestas.

## Si dicen:

> “Sí, estaría bien, pero no es prioridad.”

Muerto.

---

> “Ya lo hacemos con Looker Studio gratis.”

Si no pagan por quitarse el trabajo de encima, muerto.

---

> “Nuestro equipo ya lo hace.”

No es tu cliente, o el dolor no es suficiente.

---

> “¿Puedes hacerlo por $50?”

La hipótesis de $200/mes murió. Podrás tener otro negocio, pero no este.

---

> “Necesitamos muchas integraciones.”

Si muchos dicen esto, la herramienta simple no es suficiente. El producto se vuelve más complejo y el precio probablemente también.

---

> “Mándame una demo cuando esté lista.”

Eso no es demanda. Es cortesía.

---

# 14. Trampas que debes evitar

## 1. Preguntar “¿pagarías?”

La gente miente por educación.

Pregunta con dinero:

> “El piloto cuesta $200. ¿Empezamos?”

---

## 2. Aceptar “me interesa”

“Me interesa” no paga servidores.

Solo cuenta pago.

---

## 3. Hacer una landing sin precio

Si no pones precio, no estás testeando la hipótesis.

Pon $200/mes.

---

## 4. Dar descuento

Si descuentas, invalidas el test de precio.

Si alguien pide descuento, anótalo como objeción, pero no lo cuentes como validación de $200.

---

## 5. Construir “un poquito” antes de vender

No.

Ni dashboard.  
Ni backend.  
Ni integración.  
Ni MVP.  
Ni “una cosita rápida”.

Primero cobra.

---

## 6. Hablar con empleados que no deciden

Si hablas con un account manager junior, puede decir “sí, qué bueno”, pero no paga.

Necesitas dueño, CEO, director o responsable de presupuesto.

---

## 7. Vender a agencias demasiado grandes

Agencias grandes ya tienen herramientas, equipos o procesos.

Tu hipótesis es agencias pequeñas. Mantén eso.

---

## 8. Interpretar silencio como “tal vez”

Silencio = no.  
No responde después de 3 toques = no.  
No paga después de la llamada = no.

---

# 15. Resumen ejecutivo

## Experimento

Vender manualmente un servicio de reportes para agencias pequeñas antes de construir la herramienta.

## Oferta

Reportes listos en 24 horas para hasta 3 clientes.

## Precio

$200/mes.

## Garantía

Devolución del primer mes si no ahorra al menos 5 horas.

## Muestra

100 agencias pequeñas contactadas directamente.

## Canal

Email + LinkedIn + mensajes directos.

## Duración

7 días.

## Coste

$0-$40.

## Métrica de verdad

Pagos reales de $200.

## Resultado que te hace abandonar

Si contactas 100 agencias calificadas, tienes al menos 10 conversaciones reales con decisores y obtienes menos de 2 pagos reales de $200, abandonas la idea.

Si obtienes 0 pagos, muerto.

Si obtienes 1 pago, no construyas. Es demasiado débil.

Si obtienes pagos pero la mitad pide reembolso, muerto también.

---

# Frase final

Tu trabajo ahora no es construir.  
Tu trabajo es poner la hipótesis frente al mercado y dejar que el mercado te diga si estás equivocado.

Si nadie paga $200 por el resultado, aunque sea manual, no necesitas pasar 2 meses construyendo una herramienta para descubrirlo.