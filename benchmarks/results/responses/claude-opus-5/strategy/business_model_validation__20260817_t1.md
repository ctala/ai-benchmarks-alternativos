# Claude Opus 5 — strategy/business_model_validation

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.83 | quality: 10.0
- latency_total: 135.927s | tokens_per_second: 60.3
- input_tokens: 288 | output_tokens: 8192

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

# Sesión con un VC escéptico

Antes de empezar: tu hipótesis está mal formulada. "Los restaurantes pierden tiempo y **quieren** una solución digital" es una hipótesis que se valida sola — nadie te va a decir "no, amo llamar por teléfono a las 5am". Es una pregunta de deseabilidad social. La hipótesis que importa es: *¿el tiempo en el teléfono es el dolor #1, o es el dolor #7 detrás de precio, crédito, calidad y flujo de caja?* Mi apuesta: es el #7.

Ahora sí.

---

## 1. Los 5 riesgos principales

**Riesgo 1: Tu take rate de 15% es matemáticamente imposible.**
Este es el riesgo que mata la tesis, no la ejecución. La distribución de alimentos frescos opera con márgenes brutos de ~10-20%. Un mayorista de verduras en Corabastos o la Central de Abasto vive con 8-15% de margen. Le estás pidiendo el 100%+ de su margen para que le pases un pedido que igual iba a recibir por WhatsApp.

Y del lado del restaurante: el food cost es ~28-35% de sus ventas, y su margen neto es 5-10%. Un 15% sobre insumos le sube el food cost ~4-5 puntos. Le estás borrando la mitad de su utilidad.

Entonces la pregunta que te haría en el pitch: **¿quién paga el 15% y por qué acepta empobrecerse?** Si la respuesta es "el proveedor lo absorbe porque le traemos volumen", necesito ver el número: cuánto volumen incremental, a qué costo marginal de entrega, y por qué no puede conseguirlo con un vendedor que le cuesta 3% de comisión.

Dato relevante: Choco (el jugador mejor financiado del mundo en este espacio, ~$240M levantados) es **gratis** para restaurantes y no cobra comisión transaccional. No fue por generosidad. Fue porque el take rate no existe.

**Riesgo 2: Fuga (disintermediation). El asesino silencioso de los marketplaces de suministro B2B.**
En un marketplace B2C de baja frecuencia (Airbnb), la fuga es difícil. Aquí el restaurante le compra al *mismo* proveedor 3 veces por semana durante 4 años. La segunda transacción ya es una relación. Al pedido #3 se intercambian el WhatsApp y tú desapareces.

No tienes ningún mecanismo de retención estructural: no tienes el inventario, no tienes la flota, no tienes el crédito, no tienes datos que ellos no tengan. Tu producto es un directorio con checkout. Los directorios con checkout tienen fuga del 60-80% después del tercer pedido.

**Riesgo 3: Es una empresa de operaciones y logística disfrazada de app.**
El pedido no es el trabajo. El trabajo es: el proveedor mandó 8 kilos en vez de 10, los tomates venían golpeados, llegó a las 11am cuando el servicio abre a las 12, y el chef necesita cilantro *ahora*. ¿Quién resuelve eso? Si es el marketplace, tienes que construir operaciones, calidad, servicio al cliente y devoluciones — con el margen de un software y los costos de un distribuidor. Si no lo resuelves, tu NPS se muere y vuelven a su proveedor de siempre.

Frubana (Colombia/Brasil/México) entendió esto y se convirtió en **distribuidor 1P** con bodega y flota propia, no marketplace. Y aun así reportó recortes fuertes en 2022-2023. Muni, Favo y Merqueo cerraron. El cementerio en este vertical está bien documentado — pregúntate por qué los que tenían $50-100M no pudieron.

**Riesgo 4: Doble churn brutal.**
Los restaurantes pequeños tienen tasas de cierre altísimas (dependiendo del mercado, algo entre 30-60% en los primeros 2-3 años). Tu cohorte se erosiona sin que hagas nada mal. Y del lado de la oferta, el proveedor pequeño también rota. Estás construyendo sobre arena en los dos lados.

**Riesgo 5: Fragmentación local = no hay efectos de red globales, solo locales y débiles.**
Tu red en Polanco no vale nada en Guadalajara. Cada ciudad — de hecho, cada *zona* de cada ciudad, porque la logística de fresco es radial y de corto radio — es un lanzamiento desde cero: nuevos proveedores, nueva densidad, nuevos costos. Eso significa CAC repetido, no compuesto. Es el modelo económico de una cadena de restaurantes, no de un marketplace de software.

---

## 2. ¿Por qué podría NO funcionar en LATAM específicamente?

**a) La informalidad no es un bug, es el modelo de negocio de tu proveedor.**
Buena parte de la cadena de fresco opera en efectivo, sin factura. Digitalizar la transacción crea rastro fiscal: IVA (16% en México, 19% en Colombia), retenciones, ISR. Tu plataforma no le está cobrando 15% de comisión — le está cobrando 15% + el impuesto que antes no pagaba. Para que la matemática cierre, tendrías que generarle un ahorro superior a ~30%. No existe.

Este punto solo, mal manejado, invalida la tesis. Y la respuesta "vamos a los proveedores formales" reduce tu mercado a un subconjunto que ya tiene vendedores, rutas y clientes.

**b) El crédito es el producto, no el software.**
En LATAM el proveedor que gana no es el más barato ni el más rápido: es el que da 15-30 días de plazo. Ese es el switching cost real. Si tú exiges pago contra entrega o con tarjeta, estás compitiendo contra alguien que financia el capital de trabajo del restaurante. Vas a perder. Si das crédito, ya no eres un marketplace de 15% — eres una fintech con riesgo de crédito sobre PyMEs informales sin estados financieros. Negocio válido, pero completamente distinto, con otro balance y otro perfil de inversionista.

**c) Los mercados centrales ya son el marketplace, y son brutalmente eficientes.**
Central de Abasto (CDMX), Corabastos (Bogotá), CEAGESP (São Paulo), Mercado Modelo... descubrimiento de precio diario, competencia feroz, márgenes ya comprimidos y bodegueros que ya reparten. No estás digitalizando un mercado opaco e ineficiente; estás intentando meterte encima de un mercado hiper-competitivo con precios que cambian dos veces al día. ¿Cómo publicas precio en una app cuando el aguacate se mueve 20% en 48 horas?

**d) Coimas, comisiones informales y relaciones.**
En muchos casos el que compra (chef, encargado) recibe algo del proveedor: un descuento no reportado, un regalo, un "extra". Tu plataforma hace visible y auditable algo que a la persona que decide **le conviene que sea opaco**. Estás vendiéndole transparencia a quien se beneficia de la opacidad. El dueño quiere tu app; el que la usaría no.

**e) Ticket bajo, ARPU bajo, CAC de venta consultiva.**
Un restaurante pequeño en LATAM compra tal vez USD $3,000-8,000/mes de insumos, repartidos entre 4-6 proveedores. Aunque capturaras *todo* con un take neto realista de 4%, son $120-320/mes. Con venta de campo (la única que funciona con este perfil), tu CAC es fácilmente $150-400. Payback de 12+ meses en un cliente que quizá cierra en 18. Y no lo puedes vender por self-serve digital: es un negocio de piso, calle y confianza.

**f) WhatsApp ya ganó.**
Tu competencia no es otro software. Es un grupo de WhatsApp con nota de voz. Es gratis, es instantáneo, ya lo tienen instalado, permite negociar, permite mandar foto del producto malo, y no cobra 15%.

---

## 3. ¿Qué tendría que ser verdad? (key assumptions, en orden de riesgo)

| # | Supuesto | Por qué es frágil | Cómo se falsifica |
|---|---|---|---|
| 1 | Alguien está dispuesto a pagar 8-15% de take **con dinero real, repetidamente** | Contradice los márgenes de la industria | Cobra desde la transacción #1. Nada de pilotos gratis |
| 2 | El restaurante ahorra ≥10% en precio o ≥5h/semana **medible** | Si no ahorra dinero, el tiempo no alcanza para justificar el cambio | Compara facturas reales antes/después, mismo SKU, mismo mes |
| 3 | El proveedor te ve como canal incremental, no como costo | Si canibaliza su cliente actual, es margen destruido | Pregúntale por su capacidad ociosa y su costo de adquirir un cliente hoy |
| 4 | La fuga a WhatsApp es <30% al pedido #5 | Es el default económicamente racional para ambos | Cohortes: % de pares que siguen transando dentro de la plataforma al mes 3 |
| 5 | Puedes garantizar fill rate >92% y entrega en ventana | Es lo que decide la recompra, y no controlas la operación | Mide fill rate y on-time desde el día 1 |
| 6 | Puedes operar sin dar crédito, o el riesgo de crédito es <3% | En LATAM el crédito es el moat de tu competidor | Ofrece dos versiones de precio: contra entrega vs. 21 días |
| 7 | La unidad económica funciona a densidad alcanzable en 1 zona | Los costos de fresco son radiales | Contribución margen positivo en 1 polígono de 3km antes de expandir |

Si el #1 y el #4 no son verdad, no hay negocio. Punto. Todos los demás son secundarios.

---

## 4. El escenario donde fracasas rápido (y es el más probable)

Te lo narro porque lo he visto:

**Mes 0-3.** Consigues 25 restaurantes y 15 proveedores. Es fácil: no cobras comisión "durante el piloto", subsidias la primera entrega, y tú personalmente cierras cada pedido. GMV crece 40% mes a mes. Escribes un update de inversionistas eufórico.

**Mes 4-6.** Levantas un pre-seed sobre ese gráfico. Intentas activar el 15%. El proveedor te dice: "hermano, yo gano 12%". El restaurante te dice: "si me subes el precio, le compro a Don Jorge". Bajas a 8%. Luego a "5% pagado por el proveedor". Ahora tu ARPU es $80/mes/cuenta.

**Mes 7-9.** Descubres que el 60% de tu GMV son 4 cuentas y que 3 de ellas ya cerraron pedidos por fuera. Tu "retención" era en realidad tu WhatsApp personal. La recompra sin tu intervención manual es del 20%.

**Mes 10-14.** Para salvar la retención empiezas a resolver la operación: consolidas pedidos, contratas una camioneta, tomas la merma. Ahora eres un distribuidor con costos de distribuidor y precio de marketplace. Quemas $25-40K/mes. El siguiente inversionista te pide "eficiencia de capital" y no te da el puente.

**Mes 15-18.** Cierras o pivotas a SaaS de $49/mes para proveedores, con un mercado alcanzable 20x más chico que el que pitcheaste.

**El mecanismo del fracaso en una frase:** tracción falsa comprada con subsidio y trabajo manual, sobre un take rate que la cadena de valor no puede pagar, sin ningún mecanismo estructural que impida la fuga.

---

## 5. Con $10K, ¿qué haría yo?

**No construyas la app.** Cero código. Si gastas $10K en desarrollo, quemaste el presupuesto en la parte que no tiene riesgo.

**Semana 1-2 — Descubrimiento con revelación de preferencia ($0).**
30 conversaciones: 20 restaurantes, 10 proveedores. Prohibido preguntar "¿usarías una app?". Solo preguntas de pasado y de evidencia:
- "Muéstrame cómo pediste ayer." (que te enseñen el WhatsApp en pantalla — cronometra el tiempo real, vas a encontrar 4-9 minutos, no horas)
- "¿Cuántos proveedores? ¿Cuánto le debes hoy a cada uno? ¿A qué plazo?"
- "¿Cuándo fue la última vez que cambiaste de proveedor y por qué?" ← **esta es la pregunta de oro.** Si la respuesta nunca es "porque era más fácil pedir" y siempre es "precio / crédito / me falló", tu tesis está muerta y lo sabes en 2 semanas por $0.
- A proveedores: margen bruto real por categoría, capacidad ociosa de reparto, costo actual de conseguir un cliente nuevo.

**Semana 3-6 — Concierge manual con dinero real (~$3-4K).**
Un número de WhatsApp Business. Un Google Sheet. Tú eres el "algoritmo". Solo **un polígono de 3km** y **una categoría** (elige frutas/verduras: alta frecuencia, alta merma, mayor dolor).
Objetivo: 10 restaurantes, 4-8 semanas, **cobrando comisión desde el pedido #1**. Sin descuentos, sin subsidios, sin "gratis por ahora". El presupuesto es para cubrir tu propia merma/errores operativos y una moto para entregas de emergencia.

**Semana 7-8 — Pruebas de precio y de fuga (~$1-2K).**
- Tres cohortes de comisión: 5% / 10% / 15%. Mide dónde se rompe la conversión. Este es el experimento más importante de todo el plan.
- Prueba crédito: mismo producto a "contra entrega" vs. "+3% a 21 días". Si el 80% elige el crédito, tu negocio es financiamiento y deberías dejar de llamarlo marketplace.
- **Test de fuga:** después del pedido #3, deja de dar seguimiento proactivo por 2 semanas. ¿Cuántos vuelven solos? Ese número es tu retención real.

**Semana 9-10 — Números y decisión (~$1K de análisis/asesoría).**
Los únicos KPIs que me importarían:

| Métrica | Umbral para seguir |
|---|---|
| Retención semanal a la semana 4 (sin empuje manual) | ≥50% |
| Take rate neto sostenido cobrado en efectivo | ≥7% |
| Fuga al pedido #5 | ≤30% |
| Fill rate | ≥92% |
| Contribución margen por pedido | >$0 sin subsidio |
| GMV/cuenta/mes | ≥$1,500 |
| Ahorro documentado del restaurante (facturas) | ≥8% o ≥4h/sem |

Reserva ~$1-2K de contingencia. Y define **antes de empezar** tu criterio de kill: "si al día 60 el take rate sostenible es <5% y la fuga >40%, mato la tesis marketplace". Escríbelo y fírmalo hoy, cuando todavía eres objetivo.

---

## Preguntas que te haría en la mesa (prepáralas)

1. Muéstrame la factura de un restaurante y dime exactamente de dónde sale mi 15%.
2. ¿Por qué el proveedor no te salta al tercer pedido? Dame el mecanismo, no la esperanza.
3. ¿Por qué Frubana con $80M+ tuvo que convertirse en distribuidor 1P, y por qué Choco con $240M no cobra comisión? ¿Qué sabes tú que ellos no?
4. ¿Cómo publicas precio en un mercado donde el insumo se mueve 20% en 48 horas?
5. ¿Qué haces cuando el chef prefiere a su proveedor porque le da algo por debajo de la mesa?
6. ¿Cómo compites contra 21 días de crédito sin volverte una fintech?
7. ¿Cuál es tu founder-market fit? Esto es una empresa de operaciones. ¿Has manejado una flota, una bodega, una merma?
8. ¿Cuál es el mercado real? No "el gasto en alimentos de LATAM". Dame: # de restaurantes en tu polígono × GMV capturable × take rate defendible.
9. ¿Por qué ahora? ¿Qué cambió en 2024-2025 que no era verdad en 2019, cuando esto se intentó con más capital?

---

## Lo que me haría cambiar de opinión

No estoy diciendo que el problema no exista. La distribución de alimentos frescos en LATAM es ineficiente y hay valor real que capturar. Estoy diciendo que **tu modelo de captura de valor (marketplace 3P, 15%) es el que ya se probó y falló repetidamente.**

Tesis adyacentes que sí me sentaría a escuchar:
- **Fintech de capital de trabajo** para restaurantes, donde el flujo de pedidos es la fuente de datos para suscribir crédito. El pedido no es el producto; es el score.
- **Vertical dominante en una categoría** (proteína, o café, o pescado) donde la fragmentación y la merma son tan altas que hay 20-30 puntos de margen que redistribuir, y donde tú controlas la cadena de frío.
- **Herramienta de operación para el pro