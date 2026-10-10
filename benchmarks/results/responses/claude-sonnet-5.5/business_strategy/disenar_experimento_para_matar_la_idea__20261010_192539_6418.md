# Claude Sonnet 5.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 6.92 | quality: 8.0
- latency_total: 33.352s | tokens_per_second: 106.5
- input_tokens: 291 | output_tokens: 3553

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento: preventa concierge con outreach en frío

**Principio:** la única evidencia válida es dinero o compromiso costoso, no opiniones. "Me parece útil" no cuenta. Tarjeta puesta, sí.

## Qué hipótesis estás matando realmente

Tu frase esconde cuatro apuestas, y basta con que una falle:

1. El dolor es agudo (pierden horas reales cada mes).
2. No está resuelto (Looker Studio es gratis, y AgencyAnalytics, DashThis, Swydo y Whatagraph ya existen. Verifica sus precios hoy).
3. Pagarían **$200** (probablemente 3-5x lo que pagan hoy por algo similar).
4. Puedes llegar a ellos sin quemar plata.

## Qué haces (10-14 días)

### Día 1-2: preparación (~$0-30)
- **Define el ICP estrecho:** dueño o director de agencia de 2-15 personas, 5+ clientes recurrentes, que reporta mensualmente (SEO, ads, social).
- **Haz una lista de 100 prospectos en frío** (LinkedIn, Clutch, directorios, grupos de Facebook/Slack de agencias). **Nada de amigos ni contactos que te tengan cariño.** Sesgan todo.
- **Escribe el criterio de muerte (abajo) y guárdalo antes de empezar.**
- **Crea una página de una pantalla** (Carrd, ~$20/año) con la promesa, el precio de $200 y un botón de pago (Stripe Payment Link, reembolsable). Es una herramienta para cerrar, no para captar tráfico.

### Día 3-9: outreach y llamadas (~$0-100)
Mensaje corto: *"Estoy investigando cómo las agencias arman los reportes mensuales a clientes. ¿15 min? No vendo nada todavía."*

Meta: **15-20 llamadas con ICP calificado**. Con 100 mensajes, esperarías 15-25% de respuesta. Si no llegas a 10 llamadas, eso ya es una señal (el problema no es suficientemente urgente como para que respondan).

**En la llamada (15 min):**
1. "Muéstrame el último reporte que le mandaste a un cliente." (Pide verlo, no que lo describan.)
2. "¿Cuánto tiempo toma por cliente? ¿Quién lo hace?"
3. "¿Qué usas hoy? ¿Cuánto pagas?" (Si no usan nada o usan hojas de cálculo a mano, es buena señal. Si pagan algo y están contentos, mala.)
4. "¿Cuándo fue la última vez que buscaste una solución? ¿Qué probaste y por qué no te sirvió?" (Si nunca buscaron, el dolor no es tan agudo.)
5. **El cierre:** *"Estoy armando esto. Te propongo: durante 1 mes yo genero los reportes de tus [N] clientes con tu marca, por $200. Si no te ahorra tiempo, te devuelvo el dinero. ¿Te mando el link de pago?"*

Si dudan, no insistas. Anota la objeción exacta.

### Día 10-14: entrega concierge a quienes paguen (~$0-50)
Si alguien paga, hazle los reportes **a mano** (Looker Studio, Sheets, ChatGPT). Esto prueba dos cosas que de otro modo descubrirías después de 2 meses de código:
- ¿Les parece valioso el output?
- ¿Qué tan difícil es conectar GA4, Meta Ads, Google Ads, etc.? Es el verdadero riesgo técnico.

## Costo total
| Concepto | Costo |
|---|---|
| Landing + dominio | $20-30 |
| Stripe | comisión solo si cobras |
| Herramientas de outreach | $0-50 |
| Tu tiempo | ~25-35 horas |
| **Total** | **~$50-100** |

Compara con 2 meses de tu vida construyendo.

## Criterio de muerte (fíjalo hoy)

Sobre 15-20 conversaciones con ICP calificado:

| Resultado | Decisión |
|---|---|
| **0 pagos** y objeciones de precio o "ya tengo algo" | **Mata la idea** tal como está |
| **1-2 pagos** | Zona gris: una sola iteración (precio, segmento o propuesta) antes de decidir |
| **3+ pagos (≥15%)** | Tienes señal real. Construye, pero solo lo que entregaste a mano |

**Señales de muerte adicionales, aunque alguien pague:**
- Menos del 50% reporta más de ~5 horas/mes en reportes.
- Más del 50% ya usa una herramienta con la que está conforme.
- Menos de 10 respuestas a 100 mensajes.
- Quienes pagan lo hacen a $50-80, no a $200 (la hipótesis de precio murió, aunque haya mercado).

## Cómo evitar engañarte

- **"Avísame cuando esté listo" = 0.** No lo cuentes como interés.
- **No ofrezcas descuento para cerrar.** Contaminas la hipótesis de $200.
- **Si fallas, diagnostica dónde:**
  - No responden → el problema no duele o tu canal es malo.
  - Responden pero ya tienen solución → competencia.
  - Les duele pero no pagan $200 → precio o segmento.
  - Pagan pero la entrega manual es un infierno → riesgo técnico.
- **Tu pitch puede ser el culpable.** Por eso, si hay 0 pagos, haz una ronda extra de 5-8 llamadas cambiando solo una variable (precio o segmento) antes de enterrarla.

## Qué NO hacer
- Construir un MVP "mínimo".
- Encuestas ("¿pagarías $200?": la gente miente con amabilidad).
- Anuncios pagados a una landing: caro, ruidoso y con poca información.
- Validar con tu red.

Si en dos semanas y ~$100 no consigues que 3 desconocidos te den $200, acabas de ahorrarte 2 meses. Y si lo consigues, ya tienes tus primeros clientes y sabes qué construir.