# Claude Opus 5.5 — strategy/business_model_validation

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.94 | quality: 10.0
- latency_total: 69.167s | tokens_per_second: 87.4
- input_tokens: 290 | output_tokens: 6043

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

# Pitch con un VC escéptico

Antes de tus 5 preguntas, lo primero que te diría al sentarte:

**"Tu hipótesis describe una molestia, no un dolor. Y el mayor jugador de B2B food en LATAM ya quemó cientos de millones de dólares intentando algo parecido."**

Frubana (Colombia) levantó cientos de millones, se expandió a México y Brasil, y terminó retirándose de mercados y despidiendo gente. Tenía más capital, más equipo y más datos que tú. Tu primera respuesta tiene que ser: **¿qué sabes tú que ellos no sabían?**

---

## 1. Los 5 riesgos principales

### Riesgo #1: Desintermediación (el que te mata)
Los marketplaces funcionan cuando la transacción es **infrecuente, de alto valor y entre desconocidos** (Airbnb, MercadoLibre). Tu caso es lo contrario: **alta frecuencia, recurrente, entre las mismas dos partes.**

Semana 1: el restaurante conoce al productor de tomates por tu app.
Semana 3: "Don José, mejor le escribo directo por WhatsApp y nos ahorramos la comisión."

Ambos ganan sacándote. **¿Qué impide que lo hagan?** Si tu respuesta es "términos y condiciones", ya perdiste.

### Riesgo #2: El 15% no cabe en los márgenes
- Un restaurante pequeño opera con margen neto de 3-10%.
- El costo de alimentos es ~28-35% de sus ventas.
- Un pequeño productor o distribuidor local trabaja con márgenes delgados.

¿Quién paga el 15%? Si es el proveedor, sube precios o se va. Si es el restaurante, eres 15% más caro que la Central de Abastos o el mayorista de siempre. **Estás cobrando comisión de software sobre un producto commodity con márgenes de commodity.**

### Riesgo #3: Te vas a convertir en empresa de logística sin quererlo
El restaurante no quiere "conectar" con proveedores; quiere que **el producto llegue a las 7am, completo y en buen estado.** Cuando el pequeño productor falle (y fallará), el restaurante te culpará a ti. Para controlar la calidad terminarás manejando bodega, camiones, cadena de frío y devoluciones. Ahí ya no eres marketplace con márgenes de software. Eres distribuidor con márgenes de distribuidor, financiado con capital de riesgo.

### Riesgo #4: El crédito informal es el verdadero producto
Muchos restaurantes pequeños pagan a 8, 15 o 30 días, de palabra, "fiado". Esa relación de crédito es lo que los ata a su proveedor actual. Para competir tendrás que financiar capital de trabajo, lo que implica riesgo crediticio con negocios que cierran a tasas altísimas.

### Riesgo #5: Densidad hiperlocal y CAC con trabajo de campo
Esto no escala con Facebook Ads. El dueño de una fonda no busca "plataforma de proveedores" en Google. Necesitas vendedores tocando puertas, barrio por barrio, en ambos lados del mercado. Cada ciudad nueva es empezar de cero. **¿Cuál es tu CAC real, y cuántos meses tarda en recuperarse si el restaurante promedio quiebra en 2-3 años?**

---

## 2. ¿Por qué podría NO funcionar en LATAM específicamente?

1. **WhatsApp ya resolvió tu problema.** El dueño manda una nota de voz a las 11pm ("mañana 10 kilos de jitomate, 5 de cebolla") y listo. Le toma 3 minutos y es gratis. Tu competencia no es otra app: es WhatsApp más 15 años de relación personal.

2. **La confianza es personal, no institucional.** En LATAM el dueño confía en "Don Beto", no en una plataforma. Don Beto le cambia el producto malo sin discutir y le fía cuando el mes está flojo. Tu app no puede ser Don Beto.

3. **Informalidad fiscal.** Muchos pequeños proveedores no facturan, o no quieren. Una plataforma digital crea rastro: muchos se van a negar, y otros te traerán problemas de cumplimiento (CFDI en México, facturación electrónica DIAN en Colombia, etc.).

4. **Efectivo y costos de pago.** Si transaccionas dentro de la app, alguien absorbe 3-4% de procesamiento además de tu 15%. Si es contra entrega en efectivo, no controlas el flujo y la desintermediación es trivial.

5. **Comprar es control de calidad.** Muchos dueños o cocineros van al mercado a las 5am porque quieren ver, tocar y escoger el producto. No es tiempo perdido, es parte del oficio. Tu hipótesis asume que quieren delegarlo. ¿Lo verificaste?

6. **Volatilidad de precios.** Los precios de frescos cambian diario o semanalmente por clima e inflación. Un catálogo digital con precios fijos se rompe rápido.

---

## 3. ¿Qué tendría que ser verdad? (Key assumptions)

Ordenadas de más riesgosa a menos. **Si la #1 o la #2 son falsas, nada más importa.**

| # | Supuesto | Cómo se ve si es verdad |
|---|----------|------------------------|
| 1 | El dolor real es tiempo/coordinación, no precio, crédito o calidad | Los restaurantes eligen tu solución aunque no sea más barata |
| 2 | Puedes aportar valor continuo que justifique no saltarte | La recompra a la semana 8 sigue siendo alta y casi todo pasa por la plataforma |
| 3 | Alguien acepta pagar ~15% | Proveedores o restaurantes aceptan el costo sin subir precios ni irse |
| 4 | Los proveedores locales pueden cumplir consistentemente | Entregas completas y a tiempo en más de 90% de los pedidos |
| 5 | La economía por pedido es positiva sin logística propia | Margen de contribución positivo por pedido |
| 6 | Puedes adquirir restaurantes con un CAC recuperable | Payback razonable considerando la mortalidad de restaurantes |
| 7 | Hay suficiente densidad en una zona pequeña | Suficientes restaurantes y proveedores en pocos km² |

**La pregunta de fondo:** ¿qué le das al restaurante cada semana que no consiga gratis por WhatsApp? Candidatos reales: **crédito, consolidación de pedidos (un solo pedido, una sola entrega, una sola factura) y garantía de calidad con reposición.** Fíjate que los tres implican que te parezcas más a un distribuidor que a un marketplace.

---

## 4. El escenario de fracaso rápido

Así se ve, mes por mes:

- **Mes 1-3:** Construyes la app (gastas la mayoría del dinero aquí, error #1). Contratas 2 vendedores y consigues 40 restaurantes y 15 proveedores con descuentos de bienvenida.
- **Mes 4:** El GMV se ve prometedor. Lo pones en tu deck.
- **Mes 5:** Un proveedor entrega aguacates podridos un viernes. El restaurante no puede servir su platillo principal en el día de más ventas. Te culpa a ti. Cancela.
- **Mes 5-6:** Los restaurantes que sí quedaron contentos ya tienen el WhatsApp de sus proveedores. El GMV en la plataforma cae 40-60% mientras las transacciones reales siguen ocurriendo fuera de ella.
- **Mes 6:** Quitas los descuentos y los pedidos caen otra vez. Descubres que la "tracción" era subsidio.
- **Mes 7:** Para retener, empiezas a hacer entregas tú mismo. Cada pedido ahora pierde dinero.
- **Mes 9:** Se acaba el runway. Ningún inversionista financia un marketplace con fuga creciente y unit economics negativos.

**Causa raíz:** construiste un directorio con cobro, no un producto con valor recurrente. El valor de "conectar" se consume una sola vez; la comisión la quieres cobrar para siempre.

---

## 5. Si solo tuvieras $10K para validar

**Regla #1: no construyas la app. Ni un dólar en desarrollo.** Si gastas $10K en código antes de validar, tu respuesta a esta pregunta te descalifica.

### Fase 1: Descubrimiento (semanas 1-3, ~$1,000)
- **25-30 entrevistas con dueños de restaurantes** en UNA zona. Pregunta por comportamiento pasado, no hipotético (lee *The Mom Test*):
  - ❌ "¿Usarías una app para pedir ingredientes?" (todos dicen que sí)
  - ✅ "Cuéntame cómo compraste la semana pasada. ¿A quién? ¿Cómo? ¿Cuánto tardaste? ¿Qué salió mal? ¿Cómo pagaste?"
- **Acompaña a 3-5 dueños en su proceso de compra real** (al mercado a las 5am si hace falta).
- **10 entrevistas con proveedores:** ¿cómo consiguen clientes? ¿cuánto les cuesta? ¿pagarían por más clientes, y cuánto?
- **Pregunta clave:** ¿el dolor es tiempo, precio, crédito, calidad o confiabilidad? Probablemente no es tiempo.

### Fase 2: Concierge MVP (semanas 4-12, ~$7,000)
Hazlo todo a mano: **un número de WhatsApp Business + Google Sheets + tú.**
- 10-15 restaurantes en una sola zona y 5-8 proveedores.
- Los restaurantes te mandan el pedido a ti, tú coordinas con proveedores y das seguimiento a la entrega.
- **Cobra desde el día 1.** Prueba el 15% o un margen sobre el precio. Sin cobro real, no estás validando nada.
- Presupuesto: tu tiempo, un ayudante de medio tiempo o logística ocasional (~$3-4K), pequeño fondo para cubrir errores de calidad (~$1-2K) y transporte, teléfono y herramientas.

### Fase 3: Métricas (y criterios para matar la idea)
Define **antes de empezar** qué número te hace abandonar:

| Métrica | Señal verde | Señal de matar o pivotar |
|---------|-------------|--------------------------|
| Restaurantes que piden en la semana 8 | >60% | <30% |
| Fuga (transacciones que ocurren por fuera) | Baja, verificable | La mayoría se brinca la plataforma |
| Aceptación del cobro | Pagan sin renegociar | Se van cuando cobras |
| Margen de contribución por pedido | Positivo sin subsidio | Negativo |
| Entregas completas y a tiempo | >90% | <80% |

### Fase 4: Reserva (~$2,000)
Guárdala para probar la hipótesis alternativa que surja de las entrevistas.

---

## Mi veredicto como VC

**Hoy no invierto.** No porque el mercado no exista (es enorme), sino porque el modelo que propones (marketplace puro con 15%) es probablemente el peor modelo posible para este problema.

Lo que me haría volver a escucharte es que regreses con datos de Fase 2 y alguna de estas tesis más defendibles:

1. **Software para proveedores, no marketplace:** dale al productor una herramienta gratis o barata para recibir pedidos, cobrar y facturar. Los restaurantes llegan solos y no hay fuga porque no eres intermediario.
2. **Fintech disfrazada:** el valor está en financiar el capital de trabajo del restaurante. Monetizas con el crédito, no con comisión.
3. **Distribuidor enfocado y eficiente:** acepta que eres distribuidor, con un nicho claro (orgánico, producto local premium para restaurantes de ticket alto) donde el margen sí aguanta.
4. **Compras consolidadas:** agregas la demanda de 50 restaurantes para negociar mejores precios. Ahorrarles dinero vende mucho más que ahorrarles tiempo.

**Tu tarea:** sal a hablar con 30 restaurantes esta semana. Si después de esas conversaciones sigues creyendo que el problema es "tiempo llamando proveedores", vuelve y te escucho. Apuesto a que descubres que el problema es otro, y ese otro problema puede ser tu verdadera empresa.