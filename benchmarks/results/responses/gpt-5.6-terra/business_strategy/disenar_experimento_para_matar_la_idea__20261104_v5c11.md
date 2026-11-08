# GPT-5.6 Terra — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 6.73 | quality: 8.0
- latency_total: 42.969s | tokens_per_second: 86.8
- input_tokens: 167 | output_tokens: 3731

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## Experimento: preventa transparente, sin producto

No construyas nada. Vende primero una **beta pagada** de la herramienta.

El único resultado que cuenta es: **una agencia mete su tarjeta y paga $200**.

“No suena interesante”, “agenda una demo”, “te presento a alguien” y “lo usaría” son señales débiles. No cuentan.

---

# 1. Define un segmento muy específico

No pruebes “agencias pequeñas” en general. Es demasiado amplio y hará que el resultado sea ambiguo.

Prueba este segmento durante 7 días:

> Agencias de performance de 2–15 personas, con al menos 8 clientes recurrentes, que gestionan Google Ads, Meta Ads y/o GA4, y que envían reportes periódicos a clientes.

Solo habla con fundadores, dueños o quien sea responsable de operaciones/reporting.

El motivo: son quienes sufren el problema y pueden aprobar $200/mes.

---

# 2. La oferta exacta

No vendas “una herramienta de reportes”. Vende un resultado concreto.

> **Beta: reportes de cliente automáticos y con marca de tu agencia.**  
> Conectas Meta Ads, Google Ads y GA4; tus clientes reciben un reporte semanal o mensual con los KPIs que importan.  
> **$200/mes por agencia**, cancelable en cualquier momento.  
> Primera versión operativa en 14 días o reembolso total.

Sé explícito:

- Es una **beta**, no un producto terminado.
- Estás aceptando máximo 5 agencias.
- Cobras desde hoy: $200.
- Si no puedes ponerla en funcionamiento en 14 días, reembolsas.
- Durante la beta, parte del trabajo puede ser manual detrás de escena. No necesitas explicarlo salvo que te lo pregunten; tampoco debes mentir.

Esto es ético y te permite cobrar antes de construir.

---

# 3. Qué necesitas preparar

Máximo: **4–6 horas**.

| Activo | Cómo hacerlo | Coste |
|---|---|---:|
| Página simple | Notion, Google Sites o Carrd | $0–19 |
| Demo visual | Un reporte ficticio en Looker Studio o Figma | $0 |
| Video demo | Loom de 2 minutos | $0 |
| Checkout | Stripe Payment Link: “Beta reporting automation — $200/month” | $0 |
| Lista de prospectos | Google Maps, LinkedIn, Clutch, webs de agencias | $0 |
| Dominio opcional | Un dominio simple | ~$12 |

**Coste total:** $0–31.  
No uses anuncios. No construyas integraciones. No diseñes una app.

### La página debe tener solo esto

1. Titular:
   > Deja de pasar horas armando reportes para clientes.

2. Promesa:
   > Reportes automáticos y con tu branding desde Meta Ads, Google Ads y GA4.

3. Para quién:
   > Para agencias de performance con 8+ clientes recurrentes.

4. Precio:
   > Beta limitada: $200/mes. Cancela cuando quieras.

5. Garantía:
   > Si no tienes tu primer reporte operativo en 14 días, reembolso completo.

6. Botón:
   > “Reservar una de las 5 plazas beta — $200/mes”

Ese botón lleva directamente a Stripe. Debajo, opcionalmente: “¿Preguntas? Agenda 15 minutos.”

---

# 4. Consigue 80 agencias y contáctalas personalmente

No compres una base de datos. Haz una lista manual de 80 agencias que cumplan el perfil.

Busca:

- “agencia Google Ads [ciudad]”
- “agencia performance marketing [ciudad]”
- LinkedIn: fundadores de “performance marketing agency”
- Clutch / Sortlist / directorios locales
- Agencias que muestren servicios de Google Ads, Meta Ads y reporting.

Para cada una, consigue:

- Nombre del fundador/dueño.
- Email o LinkedIn.
- Número aproximado de empleados.
- Servicios de performance que ofrece.
- Una personalización real de una frase.

---

# 5. Envía este mensaje

### Email / LinkedIn inicial

> Asunto: reportes para clientes de [Agencia]
>
> Hola, [Nombre]. Vi que en [Agencia] gestionan campañas de [Google/Meta Ads] para clientes.
>
> Estoy abriendo una beta para agencias de performance que quieren dejar de armar reportes manualmente: conecta Google Ads, Meta y GA4, y entrega reportes con el branding de la agencia de forma automática.
>
> Cuesta $200/mes, no hay contrato, y si no está funcionando en 14 días devuelvo el dinero.
>
> No te escribo para hacer investigación ni para pedir feedback: busco 5 agencias dispuestas a pagar y usarlo este mes.
>
> Si hoy mandas reportes manualmente y tienes 8+ clientes, ¿te interesaría verlo 15 minutos esta semana?
>
> [Tu nombre]

### Seguimiento 1, dos días después

> Hola, [Nombre]. Te cierro el loop: ¿los reportes a clientes son algo que ya tienen resuelto o siguen requiriendo trabajo manual cada mes?
>
> Si el problema existe y $200/mes no es un precio absurdo, te muestro la beta en 15 minutos. Si no, no te vuelvo a escribir.

### Seguimiento 2, dos días después

> Último mensaje, [Nombre]. Estoy cerrando las plazas beta esta semana.  
> Si automatizar reportes para [Google/Meta/GA4] no merece $200/mes para [Agencia], un “no” me sirve también.

No ofrezcas una prueba gratis. No preguntes “¿usarías esto?”. No hagas una encuesta.

---

# 6. La llamada: máximo 15 minutos

Tu objetivo no es aprender todo sobre sus reportes. Tu objetivo es llegar a una transacción o a un “no” claro.

Guion:

1. **Confirmar cualificación**
   - “¿Cuántos clientes recurrentes gestionan?”
   - “¿Qué canales reportan?”
   - “¿Quién prepara los reportes hoy?”
   - “¿Cuánto tiempo les toma al mes?”

2. **Mostrar demo ficticia**
   - Máximo 3 minutos.
   - Enseña un reporte con branding, métricas y envío periódico.

3. **Hacer la oferta**
   - “La beta cuesta $200/mes, cancelable cuando quieras. Se activa en 14 días o te devuelvo el dinero. ¿Quieres reservar una plaza ahora?”

4. **Callar.**

Si responde “sí, pero…”:

> “Entiendo. Para no convertir esto en otra conversación de feedback: ¿qué tendría que ser distinto para que pagaras $200 hoy?”

Si pide descuento:

> “No para esta prueba. Estoy probando específicamente si esto merece $200/mes. Si no lo merece para ustedes, prefiero saberlo.”

Si pide una prueba gratis:

> “No estoy ofreciendo pruebas gratis porque necesito saber si es un problema por el que una agencia paga. Si prefieres esperar a que el producto esté terminado, lo entiendo, pero no te cuento como cliente beta.”

---

# 7. Regla de decisión: cuándo abandonar

## Abandona la idea de construir durante dos meses si ocurre esto:

Después de:

- contactar a **80 agencias** que encajen en el segmento;
- realizar al menos **20 conversaciones calificadas** con decisores;
- presentar la oferta exacta a $200/mes;
- y pedir el pago en la llamada;

obtienes:

> **0 pagos reales, 0 depósitos o 0 tarjetas ingresadas.**

Ese es tu criterio de muerte.

No lo racionalices con:

- “Necesito mejorar el onboarding.”
- “La landing no era suficientemente bonita.”
- “Quizá con más funcionalidades.”
- “Les gustó mucho la idea.”
- “Me pidieron que les avise cuando esté listo.”
- “El mercado no estaba listo.”

Si 20 agencias que realmente tienen el problema no pagan $200 por resolverlo, **no tienes evidencia para invertir dos meses construyendo**. Mata o pausa la hipótesis.

---

# 8. Qué significan los resultados

| Resultado en 20 conversaciones calificadas | Decisión |
|---|---|
| 0 pagos | Mata la hipótesis actual: ese segmento no compra esta oferta a $200/mes. |
| 1 pago | No construyas aún. Puede ser suerte o un caso excepcional. Haz otras 20 conversaciones. |
| 2 pagos | Sigue vendiendo, pero aún no construyas una plataforma completa. Entrega manualmente y busca retención. |
| 3+ pagos | Hay señal suficiente para un siguiente experimento: entregar el servicio manualmente durante 30 días y comprobar uso/renovación. |
| Muchos interesados, ningún pago | No es validación. Tu propuesta, precio o urgencia no justifican compra. Trátalo como un “no”. |

Incluso con 3 pagos, todavía no deberías dedicar dos meses a construir. Primero cobra y entrega el resultado manualmente durante un mes. La siguiente pregunta sería: **¿renuevan a $200 sin que tengas que perseguirlos?**

---

# Calendario y coste

## Calendario

| Día | Acción | Tiempo |
|---|---|---:|
| Día 1 | Landing, demo ficticia, Stripe | 4–6 h |
| Día 2 | Lista de 80 agencias | 3–4 h |
| Días 2–5 | Envío de mensajes | 2–3 h |
| Días 3–8 | Seguimientos y llamadas | 5–8 h |
| Día 8 | Decisión | 15 min |

**Tiempo total:** 14–21 horas repartidas en una semana.  
**Tiempo calendario:** 7–8 días.  
**Coste:** $0–31, más comisión de Stripe solo si alguien paga.

---

## La frase que debes recordar

> La hipótesis no es “las agencias odian hacer reportes”.  
> La hipótesis es “las agencias pequeñas pagan $200/mes ahora por dejar de hacerlos”.

Solo un cobro responde esa pregunta.