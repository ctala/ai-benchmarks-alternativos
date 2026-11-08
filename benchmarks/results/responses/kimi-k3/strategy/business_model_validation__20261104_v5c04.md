# Kimi K3 — strategy/business_model_validation

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.82 | quality: 10.0
- latency_total: 242.409s | tokens_per_second: 32.4
- input_tokens: 279 | output_tokens: 7842

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

Perfecto. Ponte cómodo, porque esto es lo que escucharías en Sand Hill Road o en un fondo de CDMX después de 3 minutos de pitch.

---

## 1. Los 5 riesgos principales

**Desintermediación (leakage).** Este es tu asesino número uno. Restaurante conoce proveedor en tu app, hacen una transacción, intercambian WhatsApp... y nunca vuelven. Te convertiste en un directorio gratis. WhatsApp es tu competidor real y es gratis, instantáneo y ya está instalado en el 100% de tus usuarios.

**Tu take rate del 15% es fantasía.** Los distribuidores de alimentos operan con márgenes brutos de 15-30%. Los mayoristas de perecederos, a veces 5-15%. ¿De dónde sale tu 15%? Nadie puede pagártelo sin subir precios, y si suben precios, pierdes contra el canal actual. ¿Le preguntaste a UN solo proveedor si pagaría 15%? Porque se va a reír.

**Selección adversa en ambos lados.** Los buenos proveedores —los que los restaurantes quieren— no te necesitan; tienen capacidad vendida. Los que se mueren por entrar a tu marketplace son los que tienen producto sobrante o peores precios. Y los restaurantes que cambian de proveedor cada semana suelen ser los que ya les deben a todos.

**Unit economics de ticket chico.** Orden promedio de restaurante pequeño: $80-150 USD. Tu 15% (que será 4-6% real) sobre $100 = $4-6 por orden. Contra CAC, soporte, disputas y procesamiento de pagos. No cierra. Y encima, tus clientes mueren: una fracción enorme de restaurantes pequeños cierra en 2-3 años. Tu base de clientes se evapora sola.

**Esto es una empresa de logística disfrazada de software.** Perecederos = disputas de calidad, devoluciones, cadena de frío, densidad geográfica. Cada ciudad es un marketplace nuevo. Escala como distribuidora, no como app. Los múltiplos de valuación son muy distintos.

## 2. Por qué podría NO funcionar en LATAM específicamente

**Tu hipótesis del dolor probablemente está mal diagnosticada.** El incumbente no es "llamar a 5 proveedores". Es: la Central de Abastos a las 4am + WhatsApp + el repartidor de confianza que conoce al dueño desde hace 8 años. Para muchos dueños, ir al mercado no es "perder tiempo" — es control de calidad.

**El crédito informal es el lubricante de toda esta cadena.** El proveedor le fía al restaurante a 7, 15, 30 días. Tu marketplace con pago por adelantado le rompe el flujo de caja al restaurante. Esto, solo, ha matado modelos idénticos.

**Informalidad fiscal.** Muchos restaurantes pequeños operan en efectivo y sin factura. El proveedor formal que factura cobra IVA y pierde contra el informal. ¿Tu app fuerza facturación? Perdiste al informal. ¿No la fuerza? Problema regulatorio.

**El elefante en la sala: Frubana levantó más de US$250M para hacer EXACTAMENTE esto y en 2022 se retiró de México y Brasil para salvar Colombia.** Choco, en Europa/EE.UU., terminó pivotando a software porque cobrar comisión por pedido no funcionó. Merqueo quebró. Los que siguen vivos (como Cayena en Brasil) lo lograron volviéndose distribuidores con logística y crédito propio — o sea, no marketplaces ligeros con 15%. La pregunta de tu pitch no es "¿hay demanda?". Es: **¿qué sabes tú que Frubana no supo con $250M?**

## 3. Qué tendría que ser verdad (key assumptions)

- Que los restaurantes reordenan por tu plataforma repetidamente sin que tú los persigas — retención orgánica en semanas 4-8, no una primera orden por curiosidad o descuento.
- Que el dinero pasa por ti. Si no capturas el pago, no capturas valor.
- Que ALGUIEN acepta pagarte algo real — aunque sea 3-6% — y no se va.
- Que puedes resolver o esquivar el problema del crédito informal.
- Que un "proveedor local" puede darle a un restaurante consistencia de volumen y calidad todo el año. El restaurante necesita aguacate en febrero; la finca local lo tiene en junio. ¿Quién agrega?
- Que en UNA zona geográfica puedes lograr densidad suficiente para ganar en precio, tiempo O confiabilidad. Necesitas ganar en al menos una, claramente.
- Que procurement es un dolor top-3 para el dueño, y no el dolor #7 detrás de ventas bajas, personal, costos e impuestos.

## 4. Escenario de fracaso rápido

Lanzas en una ciudad. Onboardeas 60 restaurantes con descuento de bienvenida. Semanas 1-2: órdenes, dashboard bonito, te sientes genial. Semana 3: proveedores y restaurantes empiezan a intercambiar números — tu volumen se estanca mientras "la satisfacción" sube. Semana 5: un pedido de aguacates llega golpeado, disputa, dos restaurantes churnean. Semana 8: retención orgánica del 15%. Tu take real terminó en 4% porque los proveedores rechazaron el 15%. CAC de $120 por restaurante, contribución de $3 por pedido. Quemas $50-60K en seis meses.

La trampa mortal: **esto no falla por falta de interés. Todos se registran. Nadie se queda ni paga.** Un "no" claro sería un regalo; lo que vas a recibir son meses de "sí, pero..." que queman tu runway.

## 5. Con $10K: cómo validar de verdad

**No escribas una línea de código.** Tu app es WhatsApp Business + Google Sheets. Tú eres el algoritmo.

**Semanas 1-2 (~$500):** 40 entrevistas conductuales, no de opinión. Nada de "¿te gustaría una app?". Pregunta: "Muéstrame cómo compraste el martes pasado. ¿A quién le llamaste? ¿Cuánto pagaste? ¿Cuándo le pagaste?" Pide ver facturas reales. A proveedores: "¿Cuál es tu margen bruto? ¿Pagarías 15% de comisión? ¿5%?" Si se ríen, acabas de aprender por $500 lo que otros aprenden con $500K.

**Semanas 3-10 (~$6-7K):** Marketplace manual en UN barrio: 12-15 restaurantes, 5-8 proveedores. Tú tomas pedidos, coordinas entregas, cobras. **Cobra comisión real desde la semana 2. Cero subsidios los primeros 30 días — la demanda subsidiada miente.**

Mide solo esto:
- % que reordena sin que tú lo contactes
- Intentos de bypass (¿tratan de saltarte?)
- Take rate que el mercado realmente acepta
- Qué pasa cuando exiges pago por adelantado (esto te dirá todo sobre el problema del crédito)

**Kill criteria, escritos ANTES de empezar:** si después de 8 semanas menos del 40% reordenó dos veces orgánicamente, o nadie acepta pagar más del 5%, mata o pivota. Sin excepciones.

Y un dato que debería obsesionarte: en B2B de alimentos, la plata de verdad históricamente está en **fintech (financiar al restaurante) y logística**, no en la comisión por transacción. Valida también quién pagaría por qué.

---

Si después del piloto manual tienes retención orgánica y gente pagándote sin subsidios, te escucho con atención. Si no, el pitch deck no importa.