# Claude Fable 5 — strategy/business_model_validation

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.88 | quality: 10.0
- latency_total: 55.217s | tokens_per_second: 57.6
- input_tokens: 288 | output_tokens: 3178
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación crítica y detallada del modelo de negocio propuesto.

## Respuesta completa

# Feedback de VC escéptico: prepárate

Antes de empezar: tu hipótesis tiene un problema fundamental que voy a repetir varias veces. **"Pierden tiempo llamando" no es un dolor que la gente paga por resolver.** Los restaurantes pequeños operan con márgenes de 3-8%. Tu 15% de comisión es más grande que su margen neto completo. Alguien lo va a absorber, y nadie quiere ser ese alguien.

---

## 1. Los 5 riesgos principales

**a) Desintermediación inmediata (el asesino #1 de marketplaces B2B)**
El restaurante encuentra al proveedor en tu app, hacen una transacción, intercambian WhatsApp, y nunca vuelven. En compras recurrentes con los mismos 3-5 proveedores, tu app es un directorio caro. ¿Qué valor entregas en la transacción #47 con el mismo proveedor de verduras?

**b) El 15% no cabe en la economía unitaria**
Ingredientes son commodities de bajo margen. El proveedor local trabaja con márgenes de 10-20%. Si le quitas 15%, o sube precios (y el restaurante deja de usar la app porque "es más caro"), o pierde dinero. Compara: Rappi cobra ~25-30% pero en comida preparada con márgenes de 60-70%. Tú estás en la categoría equivocada para esa comisión.

**c) La relación proveedor-restaurante no es transaccional, es de confianza y crédito**
El proveedor le fía al restaurante ("me pagas el viernes"). Le guarda el mejor producto. Le avisa cuando llegó algo bueno. Tu app destruye eso y no ofrece nada equivalente. ¿Vas a dar crédito? Entonces no eres un marketplace, eres una fintech con riesgo de cartera.

**d) Problema de gallina y huevo en un mercado hiperlocal**
Necesitas densidad en un radio de ~10km. No sirve tener 500 proveedores en el país si el restaurante en Coyoacán solo ve 3. Cada zona es un cold start nuevo. Esto quema capital rápido.

**e) La logística no la controlas**
Si el proveedor entrega tarde o el tomate llega podrido, ¿quién responde? El restaurante te culpa a ti. Sin control de calidad ni logística, tu NPS depende de terceros que no te deben nada. Y si haces logística propia, ya no eres un marketplace ligero, eres Frubana — que necesitó cientos de millones y aún así ha tenido que ajustar el modelo brutalmente.

---

## 2. Por qué podría NO funcionar en LATAM específicamente

- **Informalidad masiva**: gran parte de la compra de restaurantes pequeños pasa por el mercado de abasto, en efectivo, sin factura. Tu app introduce trazabilidad fiscal que muchos activamente NO quieren. Esto es una feature negativa para tu usuario.
- **WhatsApp ya resolvió esto gratis**: el dueño manda un audio a las 6am, el proveedor le manda foto de lo que tiene, listo. Tu competencia no son otras apps — es un audio de WhatsApp con costo cero y fricción cero.
- **El dueño va al mercado personalmente por una razón**: quiere VER el producto. Tocar el aguacate. Negociar en persona. La compra de perecederos es sensorial y de regateo. Digitalizar eso elimina lo que el comprador valora.
- **Ya hay cadáveres y heridos en el camino**: Frubana (Colombia/Brasil/México) levantó +$200M y ha tenido despidos masivos y retiradas de mercados. Jüsto pivoteó. Si con esos capitales fue así de difícil, ¿cuál es tu insight que ellos no tuvieron?
- **Crédito informal es la moneda del sector**: sin resolver el "fiado", no tienes producto. Y resolver crédito en LATAM a restaurantes pequeños con alta mortalidad (50%+ cierran en 2 años) es un riesgo de cartera espantoso.

---

## 3. Qué tendría que ser verdad (key assumptions)

Ordenadas de más a menos crítica:

1. **El dolor es precio o disponibilidad, no tiempo.** Si validas que los restaurantes pagarían por ahorrar 10-15% en insumos (agregando demanda), tienes negocio. Si solo "ahorran tiempo", no.
2. **Puedes cobrar sin que se note**: la comisión tiene que salir de eficiencia real (agregación de demanda, menos merma, mejor precio de mayoreo), no de inflar precios.
3. **Hay una razón de retención más allá del descubrimiento**: crédito, facturación automática, garantía de calidad, o precios que solo existen dentro de la plataforma.
4. **El proveedor gana volumen incremental que no conseguiría solo** — si solo le digitalizas clientes que ya tenía, te va a sacar de la ecuación.
5. **Existe densidad alcanzable**: puedes llegar a masa crítica en UNA zona con menos de $50K.

Si la #1 es falsa, todo lo demás no importa.

---

## 4. El escenario de fracaso rápido

**Mes 1-3**: Lanzas con 30 proveedores y 100 restaurantes en una ciudad. GMV crece, celebras.
**Mes 4-6**: Retención por cohorte se desploma. Los restaurantes hicieron 2-3 pedidos, conocieron al proveedor, y ahora le piden directo por WhatsApp con 15% de descuento (tu comisión, repartida entre ambos). Tu take rate real cae a 4-5% porque empiezas a dar descuentos para retener.
**Mes 7-9**: Descubres que tu CAC es de $80-150 por restaurante (ventas en campo, porque estos clientes no se adquieren con ads) y tu LTV real es de $60. Quemas el runway subsidiando transacciones para mostrar tracción.
**Mes 10**: Se acabó el dinero y tu métrica principal es GMV inflado con retención de <20% a 6 meses. Ningún VC te da el siguiente cheque.

Este guion está escrito. Lo he visto ejecutado varias veces.

---

## 5. Si solo tuvieras $10K para validar

**No construyas la app. Cero código.** Haz esto:

- **$0 — Semana 1-2**: Párate en el mercado de abasto a las 5am tres días. Habla con 30 dueños de restaurante mientras compran. Pregunta: ¿cuánto gastas al mes? ¿cuánto te fían? ¿qué te enfurece de tus proveedores? ¿cuándo fue la última vez que cambiaste de proveedor y por qué? La respuesta a la última pregunta te dice todo sobre switching costs.
- **$500 — Semana 3-4**: Concierge MVP con WhatsApp. TÚ eres la app. Toma pedidos de 10 restaurantes, consíguelos con proveedores, coordina entrega. Cobra tu 15% desde el día uno. Si no puedes cobrarlo manualmente con servicio blanco, una app no lo va a lograr.
- **$3,000 — Mes 2-3**: Escala el concierge a 30 restaurantes. Mide: frecuencia de recompra, take rate real después de descuentos, cuántos intentan saltarte, ticket promedio.
- **$2,000 — Mes 3**: Prueba el ángulo alternativo: en vez de comisión, negocia precio de mayoreo agregando demanda de 20 restaurantes y quédate con el spread. Compara qué modelo aguanta.
- **$4,500 — Reserva**: para la iteración que vas a necesitar cuando el modelo original no funcione (spoiler: no va a funcionar como lo planteaste).

**El kill criterion**: si a los 90 días no tienes 15+ restaurantes comprando 2+ veces por semana Y pagando la comisión sin subsidio, mata la idea o pivotea. No te enamores.

---

## La pregunta que te haría al final del pitch

*"Si mañana los proveedores y restaurantes de tu plataforma crearan un grupo de WhatsApp sin ti, ¿qué pierden exactamente?"*

Si no tienes una respuesta contundente a eso, no tienes un negocio — tienes una lista de contactos con interfaz bonita.

Mi lectura honesta: la oportunidad real probablemente no está en el marketplace de descubrimiento, sino en **agregación de demanda + crédito + logística de última milla** — que es un negocio mucho más pesado, más caro y más defendible. Decide cuál quieres construir antes de gastar un peso.