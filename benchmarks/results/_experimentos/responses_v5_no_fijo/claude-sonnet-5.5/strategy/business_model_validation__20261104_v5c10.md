# Claude Sonnet 5.5 — strategy/business_model_validation

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 39.358s | tokens_per_second: 109.8
- input_tokens: 290 | output_tokens: 4320

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

# Pitch con VC escéptico

Tu hipótesis es un **dolor real pero probablemente no un dolor suficiente para pagar 15%**. Que algo sea molesto no significa que alguien pague por resolverlo.

---

## 1. Los 5 riesgos principales

**1. Disintermediación (el riesgo #1 de todo marketplace de oferta recurrente)**
Tu app hace el match en la primera transacción. Después, el restaurante y el proveedor tienen el WhatsApp del otro. ¿Por qué seguirían pagándote 15% por una relación que ya existe? Los pedidos de ingredientes son repetitivos y de alta frecuencia, el peor caso para retener un marketplace.

**2. El 15% no cuadra con la economía del proveedor**
Un proveedor local de frutas, verduras o proteínas opera con márgenes brutos de 15-25% y netos de un dígito. Tu comisión se come la mitad o más de su margen. Solo hay tres salidas: sube precios (el restaurante se va), absorbe la pérdida (se va el proveedor) o saca la venta de la plataforma. Ninguna es buena para ti.

**3. Estás resolviendo "llamar", y el problema real es otro**
Llamar o mandar WhatsApp a 4 proveedores toma 20 minutos al día. Eso es una molestia, no un problema que justifique cambiar de hábito. Los problemas que sí duelen son **crédito** (fiado a 15-30 días), **consistencia de calidad**, **entregas puntuales** y **precio**. Si no resuelves uno de esos, eres un directorio con checkout.

**4. Densidad y logística**
Un marketplace de ingredientes frescos necesita densidad geográfica brutal: suficientes proveedores y restaurantes en la misma zona para que las entregas sean viables. Si no controlas la logística, la experiencia depende de terceros que no controlas. Si la controlas, ya no eres un marketplace asset-light, eres un distribuidor con capex y márgenes de distribuidor.

**5. Restaurantes pequeños: mal cliente**
Alta mortalidad (muchos cierran en 2-3 años), compras pequeñas e irregulares, poca disciplina digital, baja disposición a pagar por software y gran sensibilidad al precio. Tu base de clientes se erosiona sola y tu CAC se amortiza sobre ciclos de vida cortos.

---

## 2. Por qué podría NO funcionar en LATAM

- **WhatsApp ya es tu competidor**, y gratis. Es el sistema de pedidos de facto, con voz, fotos y negociación. Reemplazarlo exige ser 10x mejor, no 2x.
- **Informalidad:** muchos proveedores no facturan, cobran en efectivo y no tienen sistemas. Digitalizarlos es costoso y ellos ven poco incentivo.
- **Negociación como cultura:** el precio se regatea y varía por relación, volumen y día. Un catálogo con precios fijos choca con cómo se hace el negocio.
- **Crédito informal:** el fiado es la verdadera moneda de la relación. Si no financias, pierdes frente al proveedor que sí da crédito. Si financias, necesitas balance y manejo de riesgo.
- **Cadáveres en el camino:** Frubana, Chiper, Merqueo y otros han intentado variantes de esto con cientos de millones levantados. Varios tuvieron que recortar, pivotar o fusionarse porque la unidad económica en logística de alimentos es durísima. Tienes que explicar por qué tú sí y ellos no, con $10K en lugar de $100M.
- **Fragmentación:** cada ciudad es un mercado distinto. Sin escala en una ciudad no hay nada que replicar.

---

## 3. Qué tendría que ser verdad (key assumptions)

| # | Supuesto | Cómo se rompe |
|---|----------|---------------|
| 1 | Los restaurantes pagarán (directa o indirectamente) por conveniencia | Prefieren WhatsApp y precio bajo |
| 2 | Los proveedores aceptarán 15% porque les traes volumen incremental | Ven que solo les quitas margen de clientes que ya tenían |
| 3 | Los usuarios **seguirán transaccionando dentro** de la plataforma después de 3 meses | Se van a canales directos |
| 4 | Hay un diferenciador más allá de "directorio" (crédito, logística, precios, calidad) | No lo hay |
| 5 | CAC de restaurante < 6-9 meses de take rate | La venta es uno a uno, presencial y cara |
| 6 | Puedes lograr densidad en una zona antes de quedarte sin dinero | Te dispersas en muchas zonas con poca tracción |

Si **3** y **2** son falsos, no tienes negocio. Todo lo demás es secundario.

---

## 4. El escenario de fracaso rápido

**Meses 1-3:** Construyes la app (costo: $30-60K o 3 meses de tu tiempo). Con mucho esfuerzo de ventas puerta a puerta consigues 40 restaurantes y 10 proveedores. Hay pedidos. Se ve bien en el deck.

**Meses 4-6:**
- Los proveedores empiezan a quejarse del 15%. Los más grandes suben precios en la app o piden que las ventas "grandes" sigan por fuera.
- Los restaurantes descubren que el mismo tomate cuesta 12% más en tu app que por WhatsApp.
- Un proveedor entrega tarde o mal; el restaurante te culpa a ti porque "es tu plataforma".
- La retención a 90 días cae por debajo de 30%.
- Descubres que el GMV real es pequeño: 40 restaurantes × $1,500/mes × 15% = **$9K/mes de ingreso bruto** si todo va perfecto y nadie se fuga. Eso no paga ventas, soporte, ni tecnología.

**Meses 7-9:** Para arreglar la retención empiezas a ofrecer crédito o logística propia. Quemas efectivo, el modelo ya no es marketplace asset-light, y no hay inversionista que financie un distribuidor pequeño con tracción de 40 clientes.

**Causa raíz:** construiste la solución (app) antes de validar que alguien pagaría 15% por ella, y tu valor desaparece al primer intercambio de contactos.

---

## 5. Con $10K: qué haría

**No construiría una app.** Haría un **concierge MVP** durante 8-10 semanas.

**Semanas 1-2: Entrevistas (costo ≈ $0-300)**
- 30 restaurantes y 15 proveedores. Preguntas clave: ¿cuánto compras por semana?, ¿qué te frustra?, ¿qué has probado?, ¿cuánto pagarías para resolverlo?
- Busca el dolor real. Si nadie menciona "tiempo llamando" como top 3, tu hipótesis está en problemas.

**Semanas 3-8: Operación manual (≈ $6-7K)**
- Una zona, una o dos categorías (ej. verduras + proteínas), 15-20 restaurantes, 4-6 proveedores.
- Recibes pedidos por WhatsApp, los consolidas en una hoja de cálculo y los distribuyes tú. Tú eres la plataforma.
- **Prueba cobrar de verdad.** Pon comisión real, o márgenes sobre el precio, y mira quién se queda.
- Reserva presupuesto para un repartidor o logística mínima y para cubrir errores de entrega.

**Métricas de supervivencia (si no las cumples, mátalo o pivota):**
- ≥ 50% de los restaurantes pilotos repiten semanalmente durante 6 semanas.
- ≥ 60% del gasto de ingredientes de esos restaurantes pasa por ti en las categorías cubiertas.
- Los proveedores aceptan la comisión **sin subir precios** al restaurante.
- Observas explícitamente cuántos intentan saltarte. Mide la disintermediación como métrica principal.
- Margen de contribución positivo por pedido después de logística.

**Semanas 9-10:** Decide. Si el dolor real resulta ser crédito o logística, tu producto es otro (fintech de crédito a restaurantes, o distribución). Eso no es fracaso, es el hallazgo más valioso que podrías obtener.

---

## Veredicto

Hoy tienes una **hipótesis de dolor**, no un negocio. La pregunta que me haría un inversionista y que no has respondido es:

> **¿Por qué un restaurante y un proveedor que ya se conocen seguirían pagándote 15% dentro de un año?**

Si tu respuesta es "por conveniencia", no alcanza. Si es "porque les doy crédito, garantizo calidad o les consigo mejor precio por volumen agregado", empieza a ser interesante, pero entonces tu negocio es más complejo, más intensivo en capital y menos "app" de lo que planteaste.