# Claude Haiku 5.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.53 | quality: 8.0
- latency_total: 18.966s | tokens_per_second: 169.6
- input_tokens: 291 | output_tokens: 3216

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento para matar la hipótesis: pre-venta en 3 semanas por ~$150

## 1. Desarmar la hipótesis

Tu hipótesis tiene cuatro supuestos. El más frágil, y el que más dinero te ahorra matar, es **que pagarían $200/mes**. Si no pagan, lo demás no importa. Por eso el experimento apunta ahí, no a "¿les duele el problema?", que casi siempre responde que sí.

Supuestos:
1. Las agencias pequeñas (5-20 personas) pierden tiempo significativo en reportes.
2. Ese tiempo es lo bastante caro como para justificar $200/mes.
3. Usarían una herramienta nueva en vez de su Google Sheets o de lo que ya tienen.
4. **Pagarían $200/mes antes de que exista el producto.** ← Este es el que matas primero.

## 2. El experimento: landing + pre-venta real + outreach

**Paso A: Landing de una página (1 día)**
- Herramienta: Carrd, Framer o Webflow (~$10-20/mes) o una página simple.
- Contenido: el problema concreto ("ahorra 6 horas al mes en reportes de cliente"), una captura o mockup, el precio de **$200/mes**, y un botón que dice **"Reservar plaza de fundador"** que cobra un depósito de $200 (o $50 si prefieres bajar la fricción; ver abajo).
- Stripe para cobrar, con reembolso garantizado si el producto no sale en 90 días.
- Sin funcionalidades inventadas: el mockup debe ser honesto sobre lo que no existe.

**Paso B: Outreach dirigido (1 semana)**
- Lista: 300 agencias que cumplan el perfil (5-20 personas, servicios de paid media, SEO o social, en tu idioma y mercado). Apollo, Lusha o LinkedIn Sales Navigator.
- Mensaje corto, en primera persona, pidiendo 20 minutos para entender cómo hacen reportes hoy, con el link a la landing.
- Objetivo: 300 contactos → 20-30 conversaciones → 1 pre-venta de forma consistente.

**Paso C: Entrevistas de 20 minutos (en paralelo)**
Con quien responda, no preguntes "¿pagarías?" (siempre dicen que sí). Pregunta:
- "¿Cuántas horas al mes les toma hacer los reportes? ¿Quién los hace?"
- "¿Qué usan hoy? ¿Cuánto pagan por eso?"
- "Si mañana esto existiera, ¿cuál sería el paso siguiente para usarlo?"
- "¿Me puedes mostrar tu último reporte?" (comportamiento, no opinión)

Si no pueden decirte cuánto les cuesta hoy el problema, probablemente no es un dolor fuerte.

**Variante de precio (opcional, sin costo extra):** muestra $200 a la mitad del tráfico y $99 a la otra mitad. Si el precio bajo convierte mucho más, el problema existe pero $200 no es el precio correcto, y eso también es información valiosa.

## 3. Costo y tiempo

| Concepto | Costo | Tiempo |
|---|---|---|
| Landing + dominio | ~$30 | 1 día |
| Apollo/Lusha (1 mes) | ~$50-100 | 1 día |
| Stripe | $0 (comisión por cobro) | — |
| Outreach y entrevistas | $0 (tu tiempo) | 3 semanas |
| **Total** | **~$100-150** | **~3 semanas** |

Opcional: $200 en anuncios de LinkedIn dirigidos a dueños de agencias, si el outreach frío no alcanza volumen.

## 4. Criterios de muerte (escríbelos ANTES de empezar)

Esto es lo que más importa. Si los defines después, los vas a mover.

- **Mata la hipótesis de $200/mes si:** después de ~300 contactos calificados y al menos 20 conversaciones, **menos de 3 agencias pagan o dejan tarjeta registrada** a $200.
- **Mata la hipótesis de pagar por la herramienta si:** más de la mitad de las agencias que hablan contigo dicen que no tienen un problema de reportes que les cueste más de unas 3 horas al mes.
- **Señal de alerta, no de muerte:** les gusta la idea pero solo pagarían $50-99. Eso no mata el negocio, pero cambia el modelo y probablemente el mercado (agencias más pequeñas o más volumen).
- **Señal de competencia:** si la mayoría ya paga por AgencyAnalytics, Whatagraph, DashThis o Databox, no es que no tengan el problema: ya lo resolvieron. Tu pregunta cambia a por qué cambiarían o añadirían otra herramienta.

Si matas la hipótesis en 3 semanas y $150, ganaste 2 meses de construcción. Eso es un buen resultado del experimento, no un fracaso.

## 5. Lo que NO debes hacer

- No pidas "feedback" a tus amigos o a otros founders. Solo importa la gente que paga o que pone su tarjeta.
- No hagas la herramienta "solo un poquito" antes del test. Ese es el costo que estás intentando evitar.
- No cuentes los "me interesa, mándame info" como validación. Son ruido.
- No cambies el precio o el perfil a mitad de camino para salvar los números. Si lo haces, empieza un experimento nuevo con criterios nuevos.

## Resumen

1. Landing con precio de $200 y pre-venta reembolsable.
2. 300 contactos del perfil exacto, 20+ entrevistas de comportamiento.
3. Criterio de muerte fijado hoy: menos de 3 pagos o tarjetas a $200 en 3 semanas.
4. Si matas la idea: ahorraste 2 meses. Si no, tienes tus primeros clientes antes de escribir una línea de código.