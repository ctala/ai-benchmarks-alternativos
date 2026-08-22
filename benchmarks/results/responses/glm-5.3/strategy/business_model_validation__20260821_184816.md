# GLM 5.3 — strategy/business_model_validation

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.15 | quality: 10.0
- latency_total: 149.815s | tokens_per_second: 60.5
- input_tokens: 185 | output_tokens: 9059

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

Ok, te lo doy directo. Tu pitch tiene un problema matemático antes de tener un problema de ejecución. Vamos por partes.

## 1. Los 5 riesgos principales

**Riesgo 1: La desintermediación te mata en la transacción #3.**
En cuanto el restaurante y el proveedor se conocen a través de ti, ambos tienen incentivo para saltarte. El proveedor dice "llámame directo y te doy 5% de descuento" — se reparten tu comisión y ambos ganan. Sin un motivo *continuo* para transaccionar dentro de la plataforma, no eres un marketplace: eres un sitio de lead generation que se cobra una vez.

**Riesgo 2: El 15% no cabe en la economía de un restaurante.**
Haz la matemática. Ingredientes: ~30% de las ventas. Margen neto de un restaurante pequeño: 3-6%. Tu comisión de 15% sobre el gasto de ingredientes equivale a ~4.5% de las ventas — te estás llevando el equivalente a **todo el margen neto del restaurante**. Y no especificaste quién paga: si paga el restaurante, le quitas su ganancia; si paga el proveedor, los distribuidores de alimentos operan con márgenes netos de 1-5% — el 15% los destruye y solo pueden subir precios, con lo cual pierdes al restaurante. El 15% es una tasa de App Store: funciona en software con costo marginal cero, no en bienes físicos con logística.

**Riesgo 3: Tu competidor no es "ninguna solución". Es WhatsApp + el proveedor como banco.**
Tu hipótesis tiene un supuesto escondido: "quieren una solución digital". Eso no lo validaste. Las llamadas que describes como tiempo perdido son, en parte, donde ocurre el valor: ahí negocian crédito, calidad, trato preferencial. Y en LATAM el proveedor **es la línea de crédito** del restaurante — le fía a 15 o 30 días. Un marketplace con pago inmediato no compite en conveniencia: le está quitando su capital de trabajo.

**Riesgo 4: Logística y perecibilidad.**
Ingredientes requieren cadena de frío y ventanas de entrega mañaneras. ¿Quién cumple? Si la plataforma: negocio intensivo en capital que no puedes financiar. Si el proveedor: cero control de calidad y cero entrega consolidada — entonces ¿dónde está el valor?

**Riesgo 5: Churn estructural + informalidad.**
Más de la mitad de los restaurantes cierran en 3 años — tu lado de la demanda se evapora solo. Y buena parte de los proveedores vive en efectivo y sin factura, por razones fiscales. Les estás pidiendo formalizarse, lo cual para ellos es un *costo*, no un beneficio.

## 2. Por qué podría NO funcionar en LATAM específicamente

- **Informalidad:** ~la mitad de la economía regional opera fuera del sistema formal. Tu plataforma genera rastro digital. Para muchos proveedores, eso es una amenaza.
- **El crédito es el pegamento:** restaurantes subcapitalizados sobreviven semana a semana gracias al fiado del proveedor. Rompes eso y rompes la adopción.
- **WhatsApp ya ganó:** es gratis, universal, tiene notas de voz, fotos y negociación. Estás compitiendo contra free.
- **LATAM no es un mercado:** son 20+ países con monedas, regulaciones y logísticas distintas. No hay network effects transfronterizos; es una guerra calle por calle.
- **El cementerio está lleno:** Frubana levantó más de $90M con equipo salido de Rappi y terminó pivotando hacia distribuidor con inventario propio. Chiper, Jüsto, MuyCargo — nadie ha ganado con marketplace puro en este espacio. ¿Qué sabes tú que ellos no supieron? Si no tienes respuesta específica, no tienes pitch.

## 3. Key assumptions — qué tendría que ser verdad

1. El dolor es **agudo y cuantificable**, no una molestia tolerable. ¿Cuántas horas/semana? ¿A cuánto dinero equivoca?
2. El valor que entregas **supera el 15% del gasto**: mejores precios por demanda agregada, una entrega consolidada en vez de ocho, menos desperdicio, o crédito. Cada una es especulativa hasta medirla.
3. Puedes **retener la transacción**: el pago pasa obligatoriamente por ti y hay valor continuo post-matching.
4. Puedes **reemplazar el crédito del proveedor** — probablemente con financiamiento propio.
5. La logística funciona sin que la poseas, o puedes pagar el precio de poseerla.
6. CAC < LTV con tickets de $50-500 y comisión de 15%. Haz esa cuenta con números reales, hoy.

Mi lectura honesta: si esto funciona, probablemente **no es un marketplace**. Es fintech (crédito de capital de trabajo para restaurantes) con el procurement como palanca de adquisición, o un distribuidor con software encima. El marketplace puro al 15% es la parte *menos* defendible de tu modelo.

## 4. El escenario de fracaso rápido

Meses 1-6: los proveedores se registran (es gratis, ¿por qué no?). Los restaurantes no cambian su comportamiento — el dueño está 12 horas en la cocina y no quiere aprender una app. Los pocos que prueban hacen 2-3 pedidos, y el proveedor los llama directo con descuento. Mes 9: GMV retenido ≈ cero, 80% de fuga, y descubres que construiste lead generation gratis para proveedores.

**Causa raíz:** resolviste el *matching*, pero el matching nunca fue el problema. El problema era confianza, crédito y logística.

Muerte alternativa: tapan la fuga tomando pagos y logística → ahora eres un distribuidor → las necesidades de capital se multiplican por 100 → mueres en tierra de nadie entre marketplace y distribuidor. Que es exactamente donde sangró Frubana.

## 5. Con $10K para validar

**Regla uno: no construyas nada.** Cero desarrollo. Si gastas el dinero en developers, ya fallaste.

**Semanas 1-2:** 30 entrevistas con dueños de restaurantes. No preguntes "¿usarías una app?" — todos dicen que sí y mienten. Di: "muéstrame tu WhatsApp" y "cuéntame tu última semana de compras: a quién llamaste, cuánto pagaste, quién te fía". Observa cómo ordenan en vivo. Ahí está la verdad.

**Semanas 3-12:** Concierge MVP. **Tú eres la app.** 15-20 restaurantes en UN solo barrio. Recibes pedidos por WhatsApp, los consolidas, negocias con 5-10 proveedores, y cobras la comisión real desde el día uno. Sin subsidio. Si no puedes cobrar 15% siendo un humano haciendo todo el trabajo, jamás lo vas a cobrar con software.

**El experimento clave — la prueba de fuga:** a la semana 6, deja de contactar a la mitad de tus restaurantes. ¿Vuelven a ti o ya tienen guardado el número del proveedor? Ese porcentaje *es* tu modelo de negocio.

**Criterios de muerte (defínelos antes, no después):**
- <50% repite 3+ veces en 90 días sin que los persigas
- >30% de las transacciones se escapan
- No puedes cobrar la comisión sin rebelión

**Presupuesto:** casi nada. WhatsApp Business y una hoja de cálculo son gratis. $2-3K en transporte y visitas. El resto, colchón para 12 semanas de operaciones. El recurso escaso no es el dinero — es tu disciplina para no construir antes de tiempo.

---

La pregunta con la que cerraría la reunión: **"¿Qué sabes tú que el equipo de Frubana, con $90M y gente de Rappi, no supo?"** Si tu respuesta es "nada, pero lo haré mejor", no hay inversión. Si tu respuesta es un insight específico — un nicho, una ciudad, un mecanismo de crédito, un canal que ellos ignoraron — entonces quizás hay algo. Pero el marketplace genérico al 15%, tal como está planteado hoy, no es invertible.