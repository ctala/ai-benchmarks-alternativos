# Qwen 3.8 2.4T (A95B) — strategy/business_model_validation

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 7.87 | quality: 10.0
- latency_total: 328.481s | tokens_per_second: 40.2
- input_tokens: 230 | output_tokens: 13208

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

Voy a ser directo: tu hipótesis “los restaurantes pequeños pierden tiempo llamando a proveedores” es débil. Es un dolor real, pero no necesariamente un dolor monetizable. En restaurantes pequeños, el dolor de verdad suele ser: precio, crédito, disponibilidad, calidad, cumplimiento y no quedarse sin insumos un viernes por la noche. Si tu app solo “ahorra llamadas”, es una vitamina. Si resuelve abastecimiento, pago, crédito y logística, entonces puede ser negocio. Pero ahí ya no eres un marketplace liviano: eres una empresa operativa, logística y casi fintech.

Como VC, mi primera reacción sería: “esto puede morir rápido por liquidez, margen, desintermediación y caja”. Vamos por partes.

---

## 1. Los 5 riesgos principales de este modelo

### Riesgo 1: Liquidez de marketplace y problema del huevo y la gallina

Un marketplace necesita densidad. No sirve tener 200 proveedores dispersos y 100 restaurantes dispersos. Necesitas que, en una zona concreta, haya suficientes proveedores con suficientes productos disponibles para que el restaurante sienta que puede resolver su compra ahí.

El riesgo es que:

- Los restaurantes entran, ven pocos proveedores, pocos productos o poca disponibilidad, y se van.
- Los proveedores entran, ven pocos pedidos, y se van.
- Sin liquidez, no hay retención.
- Sin retención, el modelo se muere.

Preguntas difíciles:

- ¿Cuántos proveedores activos necesitas por kilómetro cuadrado para que un restaurante pueda hacer un pedido útil?
- ¿Cuántos restaurantes necesitas por zona para que un proveedor tenga sentido económico atenderte?
- ¿Cuál es tu wedge? ¿Vas a empezar con una ciudad, una categoría, un tipo de restaurante?
- ¿Por qué un restaurante dejaría de llamar a sus proveedores actuales para usar tu app si todavía no tienes catálogo completo?
- ¿Por qué un proveedor te daría stock, precio y prioridad si todavía no le traes volumen?

Si tu respuesta es “vamos a lanzar en varias ciudades con muchos proveedores y muchos restaurantes”, estás quemando capital antes de entender el problema.

---

### Riesgo 2: Unit economics rotos por ticket bajo, perecederos y operación

Un 15% de comisión suena bonito hasta que haces la cuenta.

Ejemplo simple:

- Pedido promedio: US$30.
- Comisión del 15%: US$4.50.
- Costo de pago: 3% = US$0.90.
- Soporte, cambios, devoluciones, coordinación: US$1.50.
- Logística o garantía de entrega: US$3.
- CAC amortizado por pedido: US$1.
- Margen bruto real: negativo.

Y eso sin contar mermas, productos faltantes, sustituciones, devoluciones, atención al cliente, cobranza y riesgo de crédito.

El problema es que en alimentos frescos el ticket puede ser bajo, la frecuencia alta, pero el costo operativo también alto. Si no controlas logística, calidad y pago, tu comisión es demasiado alta para el valor entregado. Si sí los controlas, tu costo sube y necesitas más escala.

Preguntas difíciles:

- ¿Cuál es tu ticket promedio esperado?
- ¿Cuánto te cuesta adquirir un restaurante?
- ¿Cuánto te cuesta adquirir y activar un proveedor?
- ¿Cuántos pedidos por semana hace un restaurante?
- ¿Cuál es tu margen de contribución por pedido después de pagos, soporte, devoluciones, logística y cobranza?
- ¿Tu 15% lo paga el proveedor, el restaurante, o ambos?
- Si el proveedor paga 15%, ¿su margen aguanta?
- Si el restaurante paga más, ¿por qué lo haría?
- ¿Tu comisión cubre el costo de garantizar disponibilidad, calidad y entrega?

Si tu respuesta es “al inicio perdemos por pedido pero luego escalamos”, cuidado. En marketplaces físicos, los costos variables no siempre bajan tan rápido como en software.

---

### Riesgo 3: Desintermediación brutal vía WhatsApp, efectivo y relación personal

Este es uno de los riesgos más grandes en LATAM.

Tú conectas al restaurante con el proveedor. Una vez que se conocen, se intercambian el WhatsApp, negocian por fuera, pagan en efectivo y tú desapareces.

Si tu marketplace solo presenta a las partes, no tienes defensa.

Preguntas difíciles:

- ¿Qué impide que el proveedor le diga al restaurante: “pídeme directo y te hago descuento”?
- ¿Qué impide que el restaurante le pague por fuera al proveedor para evitar comisión?
- ¿Tú controlas el pago?
- ¿Tú controlas la logística?
- ¿Tú controlas el inventario?
- ¿Tú controlas el crédito?
- ¿Tú controlas la facturación?
- ¿Tú controlas la data de demanda?
- ¿Qué valor queda en tu plataforma después de la primera transacción?

Si tu respuesta es “confianza en la plataforma”, estás muerto. La confianza en LATAM muchas veces está en la relación personal, no en la app.

Para evitar desintermediación, tienes que ser más que un conector. Necesitas al menos uno de estos moats:

1. Pago integrado.
2. Crédito.
3. Logística propia o gestionada.
4. Garantía de calidad.
5. Agregación de demanda.
6. Facturación y cumplimiento.
7. Data de precios, stock y demanda.
8. Contratos y penalización por fuga.
9. Proveedores que realmente necesitan tu canal incremental.

Si no tienes ninguno, eres un directorio con comisión.

---

### Riesgo 4: Calidad, estandarización y cumplimiento de proveedores locales

“Proveedores locales” suena atractivo, pero operar con productores pequeños es difícil:

- Stock inconsistente.
- Calidad variable.
- Capacidad limitada.
- Temporadas.
- Problemas sanitarios.
- Empaques inconsistentes.
- Tiempos de entrega poco confiables.
- Falta de facturación.
- Falta de trazabilidad.
- Dificultad para manejar devoluciones.

Un restaurante no puede permitirse que le falte un ingrediente clave un viernes por la noche. Si tú prometes abastecimiento, el restaurante te va a exigir a ti. Si fallas, no vuelve.

Preguntas difíciles:

- ¿Quién asume la responsabilidad si el producto llega malo?
- ¿Quién paga la merma?
- ¿Quién hace la sustitución si no hay stock?
- ¿Cómo garantizas calidad consistente?
- ¿Cómo verificas a los proveedores?
- ¿Tienes SLA de entrega?
- ¿Qué pasa si un proveedor queda mal repetidamente?
- ¿Tu modelo funciona con proveedores informales?
- ¿Puedes asegurar trazabilidad sanitaria?
- ¿Tu propuesta de “local” realmente mejora precio, calidad y disponibilidad, o solo es narrativa?

Si “local” significa más caro, menos estable y menos profesional, el restaurante pequeño no lo va a adoptar. Quizás el restaurante premium sí, pero ese mercado es más chico y más lento.

---

### Riesgo 5: Crédito, cobranza, informalidad y flujo de caja

En alimentos, el crédito es droga. Muchos restaurantes esperan pagar a 15, 30 o 60 días. Muchos proveedores pequeños necesitan cobrar rápido. Si tú te metes en medio, tienes que decidir quién financia la cadena.

Opciones:

1. Restaurante paga por adelantado: difícil de adoptar.
2. Restaurante paga contra entrega: riesgo operativo y fraude.
3. Restaurante paga a crédito: tú asumes riesgo de cobranza.
4. Pagas al proveedor rápido y cobras después: necesitas working capital.
5. No tocas el pago: pierdes control del marketplace.

Preguntas difíciles:

- ¿Quién pone el capital de trabajo?
- ¿Cómo cobras a restaurantes informales?
- ¿Qué haces si un restaurante no paga?
- ¿Cómo verificas capacidad de pago?
- ¿Puedes facturar legalmente?
- ¿Cómo manejas impuestos y retenciones?
- ¿Los proveedores están formalizados?
- ¿Tu modelo requiere crédito para crecer?
- Si requiere crédito, ¿eres una empresa de logística o una fintech?
- ¿Cuánto capital necesitas para financiar cuentas por cobrar?

Si no resuelves pago y crédito, probablemente no resuelves adopción.

---

## 2. ¿Por qué podría NO funcionar en LATAM específicamente?

No porque LATAM sea imposible, sino porque este modelo choca con varias realidades estructurales.

### a) Alta informalidad

Muchos proveedores locales no están formalizados. Muchos restaurantes pequeños tampoco. Si la transacción no pasa por un canal formal, cobrar comisión es difícil. Si obligas a formalizar, reduces oferta y demanda.

Pregunta dura:  
¿Tu marketplace puede operar con proveedores sin factura, sin cuenta bancaria y sin trazabilidad fiscal? Si sí, ¿cómo cobras y cómo cumples regulación? Si no, tu mercado real es mucho más pequeño de lo que dices.

---

### b) El efectivo sigue siendo rey

En muchos mercados de LATAM, el efectivo todavía domina. Eso genera:

- Menos trazabilidad.
- Más riesgo.
- Más conciliación manual.
- Más fuga de transacciones.
- Más dificultad para cobrar comisión.
- Más fricción para escalar.

Si tu modelo depende de pagos digitales, tienes que validar que restaurantes y proveedores realmente los usen sin fricción.

---

### c) WhatsApp ya es tu competencia

Tu competencia no es solo el distribuidor tradicional. Tu competencia es:

- WhatsApp.
- Llamada.
- Efectivo.
- Transferencia.
- El “casero” del mercado.
- El proveedor de toda la vida.
- El grupo de compras informal.
- El motoquero de confianza.

WhatsApp es gratis, ubicuo y suficiente para coordinar pedidos. Si tu app solo replica eso, no hay razón para cambiar.

Pregunta dura:  
¿Por qué un restaurante usaría tu app en vez de mandar un WhatsApp? Tienes que responder con algo tangible: mejor precio, crédito, entrega garantizada, consolidación de proveedores, facturación, calidad asegurada o menor riesgo de desabasto.

---

### d) Logística fragmentada y costosa

En muchas ciudades de LATAM:

- Las direcciones son malas.
- El tráfico es horrible.
- La seguridad es un problema.
- La cadena de frío es débil.
- La entrega de perecederos es compleja.
- El último kilómetro es caro.
- Los horarios de restaurantes son exigentes.

Si no controlas logística, dependes de terceros. Si la controlas, te vuelves intensivo en capital.

Pregunta dura:  
¿Tu margen de 15% alcanza para pagar logística de perecederos con cumplimiento alto? Si no, no estás construyendo un marketplace, estás construyendo una promesa que no puedes cumplir.

---

### e) Sensibilidad extrema al precio

El restaurante pequeño opera con márgenes bajísimos. No compra “local” porque suena bonito. Compra si:

- Es más barato.
- Es más confiable.
- Le da crédito.
- Le ahorra tiempo real.
- Le evita quedarse sin producto.
- Le simplifica pago/factura.

Si tu solución sube el costo final, aunque ahorre tiempo, puede no ser suficiente.

Pregunta dura:  
¿Cuánto vale realmente el tiempo ahorrado? Si un restaurante pierde 30 minutos al día llamando, ¿eso vale US$3, US$5, US$10? ¿Ese ahorro paga tu comisión, el delivery y el riesgo de cambio de proveedor?

---

### f) Relaciones de confianza y crédito personal

El restaurante le compra al proveedor que conoce, al que le fía, al que le resuelve, al que le cambia un producto malo sin pelear. Esa relación es difícil de reemplazar con una app.

Pregunta dura:  
¿Cómo remplazas la confianza del proveedor de toda la vida? ¿Con garantía? ¿Con reembolso? ¿Con cumplimiento medible? ¿Con crédito? ¿Con precios mejores?

---

### g) Regulación sanitaria y fiscal

Ingredientes locales pueden tener problemas de:

- Registro sanitario.
- Inocuidad.
- Etiquetado.
- Facturación.
- Trazabilidad.
- Transporte adecuado.
- Certificaciones.

Si un restaurante tiene una inspección o un problema sanitario, no va a querer proveedores informales solo porque tu app los conecta.

---

### h) Volatilidad macro

Inflación, tipo de cambio, cambios regulatorios y poder adquisitivo débil pueden hacer que los restaurantes cierren, reduzcan compras o presionen precios.

En resumen: en LATAM, este modelo puede funcionar, pero no como una app liviana. Probablemente funciona si eres una capa operativa fuerte: pagos, logística, crédito, agregación de demanda y garantía de cumplimiento.

---

## 3. ¿Qué tendría que ser verdad para que funcione?

Estas son tus key assumptions. Si no puedes validarlas, no tienes negocio.

### Assumption 1: El dolor del tiempo perdido es monetizable

Tendría que ser verdad que los restaurantes pierden suficiente tiempo y que ese tiempo les cuesta dinero real.

Métrica:

- Horas por semana dedicadas a pedir, confirmar, perseguir proveedores y conciliar pagos.
- Costo de ese tiempo.
- Disposición real a pagar por resolverlo.

Validación:

- Restaurantes hacen pedidos recurrentes sin descuento.
- Restaurantes aceptan una fee o pagan precio completo.
- Restaurantes consolidan gasto contigo aunque no seas el más barato.

Si solo usan tu plataforma cuando hay promoción, no estás resolviendo un dolor fuerte.

---

### Assumption 2: Los restaurantes quieren consolidar proveedores

Tendría que ser verdad que prefieren pedir todo en un solo lugar en vez de mantener múltiples relaciones.

Métrica:

- Número de categorías compradas por restaurante.
- Share of wallet: porcentaje del gasto total de insumos que pasa por ti.
- Frecuencia semanal.

Validación:

- Un restaurante compra al menos 3 categorías contigo.
- Vuelve varias veces por semana.
- No te usa solo para un producto niche.

Si solo te usan para un producto, eres un proveedor más, no un marketplace.

---

### Assumption 3: Los proveedores locales pueden cumplir como proveedores profesionales

Tendría que ser verdad que los proveedores locales tienen capacidad de responder con:

- Stock suficiente.
- Calidad consistente.
- Precio competitivo.
- Entrega confiable.
- Capacidad de sustitución.
- Formalización mínima.

Métrica:

- Fill rate: porcentaje de líneas de pedido cumplidas completas.
- On-time delivery.
- Tasa de devoluciones.
- Tasa de quejas.
- Retención de proveedores.

Validación:

- Fill rate >90%.
- Entrega a tiempo >90%.
- Quejas <5%.
- Proveedores repiten sin subsidio.

Si los proveedores fallan, tu marketplace falla.

---

### Assumption 4: El 15% de comisión es aceptable y sostenible

Tendría que ser verdad que el proveedor puede pagar 15% y seguir ganando dinero, o que el restaurante acepta pagar más porque el valor es claro.

Pregunta clave:  
¿La comisión sale de demanda incremental o solo estás cobrando por transacciones que ya existían?

Si el proveedor ya vendía a ese restaurante, no va a querer pagar 15%. Si tú realmente le traes nuevo volumen, puede aceptarlo.

Métrica:

- Margen del proveedor antes y después de comisión.
- Incremento real de ventas por proveedor.
- Elasticidad de precio.
- Tasa de rechazo a comisión.

Validación:

- Proveedores aceptan comisión sin subir precios totalmente.
- Proveedores ven pedidos incrementales.
- Restaurantes no perciben sobreprecio.
- La comisión cubre costos variables.

Si el proveedor solo traslada el 15% al precio, el restaurante puede rechazar la plataforma.

---

### Assumption 5: Puedes evitar la fuga de transacciones

Tendría que ser verdad que restaurantes y proveedores no se van por fuera después de conocerse.

Métrica:

- Porcentaje de pares restaurante-proveedor que dejan de transaccionar en la plataforma.
- Pedidos repetidos fuera de plataforma.
- Uso de pagos externos.
- Contacto directo posterior a la primera orden.

Validación:

- Menos de 10% de fuga después de la primera transacción.
- Restaurantes y proveedores siguen usando la plataforma por pago, logística, crédito o garantía.
- Tienes control de al menos una parte crítica de la transacción.

Si la fuga es alta, tu marketplace es solo un generador de contactos.

---

### Assumption 6: La densidad geográfica es suficiente

Tendría que ser verdad que puedes crear liquidez en una zona pequeña antes de expandirte.

Métrica:

- Restaurantes activos por zona.
- Proveedores activos por zona.
- Pedidos por proveedor por semana.
- Costo de entrega por zona.
- Fill rate por zona.

Validación:

- Una zona específica tiene retención positiva.
- Los proveedores reciben pedidos suficientes.
- Los restaurantes encuentran disponibilidad suficiente.
- El costo logístico baja con densidad.

Si no puedes ganar una zona, no puedes ganar una ciudad.

---

### Assumption 7: Los unit economics mejoran con escala

Tendría que ser verdad que el costo marginal por pedido baja con densidad, automatización y volumen.

Métrica:

- Margen de contribución por pedido.
- CAC payback.
- Pedidos por restaurante por mes.
- Costo de soporte por pedido.
- Costo logístico por pedido.
- Tasa de recompra.

Validación:

- Margen de contribución positivo o camino claro a positivo.
- CAC recuperado en menos de 3-6 meses.
- Retención semanal fuerte.
- Proveedores y restaurantes activos sin incentivos artificiales.

Si cada pedido pierde dinero y no hay efecto de densidad, no es escalable.

---

## 4. ¿Cuál es el escenario donde fracasas rápido y por qué?

El escenario clásico de fracaso rápido sería este:

### Mes 0: construyes una app antes de validar

Decides que necesitas una plataforma bonita. Gastas tiempo y dinero en:

- Desarrollo.
- Branding.
- Registro de proveedores.
- Catálogo.
- Pasarela de pagos.
- Dashboard.
- Pitch deck.

Pero todavía no has operado manualmente ni una sola transacción real.

Error.

---

### Mes 1: lanzas con oferta amplia

Convences a 50 proveedores locales y 30 restaurantes pequeños. Les dices: “entra, publica, pide, cobra”.

Pero no tienes densidad.

- Los restaurantes entran y ven pocos productos.
- Los proveedores entran y ven pocos pedidos.
- Los pedidos son pequeños.
- La logística es cara.
- El soporte es manual.
- La calidad varía.

---

### Mes 2: los unit economics se ven horribles

Cada pedido tiene ticket bajo. La comisión de 15% no alcanza.

Ejemplo:

- GMV por pedido: US$25.
- Comisión: US$3.75.
- Costo operativo por pedido: US$6-10.
- Resultado: pérdida por pedido.

Para compensar, subsidias delivery o das descuentos. Eso infla métricas falsas.

---

### Mes 3: empieza la desintermediación

Los restaurantes y proveedores se conocen. Se dan WhatsApp. El proveedor dice: “pídeme directo y te dejo mejor precio”. El restaurante acepta. Tú pierdes visibilidad, comisión y control.

---

### Mes 4: los proveedores se frustran

Los proveedores locales ven que:

- Los pedidos son chicos.
- La plataforma cobra 15%.
- Hay devoluciones.
- Hay retrasos.
- Los restaurantes pagan tarde.
- No hay volumen incremental claro.

Entonces dejan de actualizar stock, suben precios o abandonan.

---

### Mes 5: los restaurantes se frustran

Los restaurantes ven que:

- Faltan productos.
- La calidad no es consistente.
- La entrega llega tarde.
- El precio no es mejor.
- El soporte no resuelve.
- No hay crédito.

Entonces vuelven a sus proveedores de siempre.

---

### Mes 6: te quedas sin caja y sin aprendizaje claro

Tienes métricas débiles:

- Baja retención.
- Baja frecuencia.
- Alta fuga.
- Margen negativo.
- CAC alto.
- Proveedores inactivos.
- Restaurantes inactivos.

Y cuando un VC te pregunta: “¿Qué aprendiste?”, tu respuesta es: “que necesitamos más proveedores y más restaurantes”. Eso no es aprendizaje; es excusa.

---

### ¿Por qué fracasas rápido?

Porque intentaste escalar liquidez sin resolver primero:

1. Densidad geográfica.
2. Propuesta de valor para restaurante.
3. Propuesta de valor para proveedor.
4. Control de pago.
5. Control logístico.
6. Unit economics.
7. Confianza.
8. Formalización.
9. Crédito.
10. Retención sin subsidios.

El fracaso rápido no es por falta de tecnología. Es por falta de foco.

---

## 5. Si solo tuviera US$10K para validar, ¿qué harías?

Regla número uno: no construyas una app.

Con US$10K no puedes construir tecnología, adquirir usuarios, operar logística y aprender al mismo tiempo. Tienes que hacer una validación manual, fea, rápida y con dinero real.

Tu objetivo no es facturar mucho. Es responder:

1. ¿Los restaurantes realmente pagan y repiten?
2. ¿Los proveedores aceptan comisión?
3. ¿Hay fuga?
4. ¿El margen por pedido puede ser positivo?
5. ¿La oferta local puede cumplir?
6. ¿Hay densidad suficiente en una zona?

---

### Plan de validación con US$10K

#### Paso 1: Elige un micro-mercado

No elijas una ciudad entera. Elige una zona específica:

- Alta densidad de restaurantes.
- Proveedores cercanos.
- Distancia corta de entrega.
- Categoría de compra frecuente.
- Restaurantes pequeños pero formalizables.
- Proveedores con capacidad mínima de respuesta.

Ejemplo: una colonia/barrio/zona con 50-100 restaurantes pequeños y medianos.

No lances “para todos los restaurantes”. Elige un segmento:

- Cafés.
- Restaurantes de autor.
- Cocina saludable.
- Restaurantes de barrio.
- Dark kitchens.
- Restaurantes premium.

Mi preferencia para validar: restaurantes pequeños con dolor operativo y ticket razonable, no necesariamente los más informales ni los más grandes.

---

#### Paso 2: Elige 1 o 2 categorías de alta frecuencia

No intentes ser el supermercado completo.

Elige categorías donde:

- Haya compra semanal o diaria.
- El proveedor local pueda cumplir.
- El restaurante tenga dolor real.
- La calidad sea verificable.
- El precio no sea imposible.
- La entrega sea manejable.

Ejemplos posibles:

- Verduras frescas.
- Hierbas.
- Huevos.
- Pan.
- Café.
- Proteínas específicas.
- Lácteos locales.
- Insumos para menú saludable.

Evita empezar con categorías demasiado perecederas, complejas o de baja rotación si no tienes operación.

---

#### Paso 3: Haz un concierge MVP por WhatsApp

Nada de app.

Usa:

- WhatsApp Business.
- Google Sheets.
- Catálogo simple en PDF o Notion.
- Formulario simple si ayuda.
- Mercado Pago, Stripe, transferencia o link de pago si es posible.
- Control manual de pedidos.
- Confirmación manual con proveedor.
- Confirmación manual con restaurante.

Tu propuesta:

“Consolida tus pedidos de proveedores locales en un solo canal. Confirmas antes de X hora, recibes al día siguiente, pagas por este medio y nosotros coordinamos la entrega.”

Tú haces el matching manualmente.

---

#### Paso 4: Cobra desde el día uno

No regales. No subsidies. Si subsidias, falsificas la demanda.

Opciones:

1. Comisión al proveedor: 10-15% sobre pedido generado por ti.
2. Fee al restaurante: US$1-5 por pedido o porcentaje pequeño.
3. Delivery fee real.
4. Combinación: proveedor paga comisión y restaurante paga entrega.

Mi recomendación: intenta cobrar al proveedor solo si le estás trayendo demanda incremental. Si el pedido ya existía, no tiene sentido cobrarle. También puedes cobrar al restaurante por consolidación, entrega o crédito, pero eso requiere valor claro.

Si nadie quiere pagar, esa es una señal brutal pero valiosa.

---

#### Paso 5: No des crédito al inicio

Para validar con US$10K, no puedes financiar restaurantes.

Usa:

- Prepago.
- Pago contra entrega si puedes controlar el riesgo.
- Pago inmediato por link.
- Pago semanal consolidado solo si hay confianza y contrato.

Si los restaurantes exigen crédito y no quieren pagar por adelantado, eso te dice que tu modelo requerirá working capital. Puede ser válido, pero no con US$10K.

---

#### Paso 6: Opera manualmente 4-6 semanas

Tu trabajo como fundador:

- Hablar con restaurantes.
- Tomar pedidos.
- Confirmar disponibilidad.
- Coordinar proveedores.
- Coordinar entregas.
- Resolver incidencias.
- Medir todo.
- Cobrar.
- Preguntar por qué sí y por qué no.

No contrates agencia. No hagas branding. No hagas video. No contrates community manager. No construyas app.

---

### Presupuesto sugerido para US$10K

Esto depende del país, pero una asignación razonable sería:

| Concepto | Presupuesto |
|---|---:|
| Herramientas no-code, WhatsApp Business, Sheets, CRM básico, links de pago | US$1,000 |
| Comisiones de pago y costos transaccionales | US$1,000 |
| Operación manual / founder stipend / part-time ops | US$3,000 |
| Fondo para logística de pruebas, courier, entregas urgentes | US$2,500 |
| Fondo de garantía por devoluciones, mermas o errores | US$1,500 |
| Legal básico, contratos simples, términos | US$1,000 |
| Total | US$10,000 |

Si necesitas gastar en pauta para adquirir restaurantes, hazlo pequeño y solo después de confirmar que el canal manual funciona. Con US$10K, la adquisición debe ser founder-led sales: tú tocando puertas, llamando y visitando.

---

### Métricas que debes medir

No midas “likes”, “registros” o “descargas”. Mide dinero y comportamiento.

#### Del lado restaurante

- Número de restaurantes que hacen primer pedido.
- Número de restaurantes que repiten en semana 2, 3 y 4.
- Frecuencia de pedidos por semana.
- Ticket promedio.
- Categorías compradas.
- Share of wallet aproximado.
- Razón de compra: precio, tiempo, calidad, crédito, disponibilidad.
- Razón de abandono.
- Disposición a pagar.
- Tasa de prepago.
- Tasa de pago contra entrega.
- Tasa de impago.

#### Del lado proveedor

- Número de proveedores activos.
- Pedidos por proveedor.
- Fill rate.
- On-time delivery.
- Devoluciones.
- Quejas.
- Margen del proveedor después de comisión.
- Si acepta comisión sin subir precios.
- Si intenta llevarse al restaurante por fuera.
- Si está dispuesto a seguir en la semana 4.

#### Unit economics

- GMV total.
- Take rate real.
- Ingreso por comisión.
- Costo de pagos.
- Costo de entrega.
- Costo de soporte.
- Costo de devoluciones.
- Margen de contribución por pedido.
- Margen de contribución por restaurante.
- CAC manual por restaurante.
- CAC manual por proveedor.
- Payback estimado.

---

### Criterios de éxito mínimos

Si después de 4-6 semanas ves esto, quizás tienes algo:

- Al menos 10 restaurantes haciendo 3+ pedidos por semana sin subsidio.
- Al menos 5 proveedores activos cumpliendo consistentemente.
- Fill rate >90%.
- Entrega a tiempo >90%.
- Tasa de quejas baja.
- Restaurantes repiten en semana 4.
- Proveedores aceptan comisión y ven valor.
- Fuga baja: menos de 10% de pares se va por fuera.
- Margen de contribución por pedido positivo o muy cerca de serlo.
- Restaurantes dicen que volverían a pedir aunque no haya descuento.
- Tienes evidencia de que el tiempo ahorrado o la confiabilidad justifican el costo.

Si ves eso, puedes pensar en levantar capital o reinvertir.

---

### Criterios de fracaso / kill criteria

Si ves esto, para:

- Los restaurantes se registran pero no piden.
- Los restaurantes piden una vez y no vuelven.
- Solo compran si hay descuento.
- Los proveedores no aceptan comisión.
- Los proveedores suben precios para compensar comisión.
- Los restaurantes y proveedores se van por WhatsApp.
- El fill rate es menor a 80%.
- Las entregas fallan constantemente.
- El ticket promedio es tan bajo que la comisión no cubre operación.
- Necesitas subsidiar cada pedido.
- Los proveedores no tienen stock o calidad consistente.
- Los restaurantes exigen crédito y no quieren prepago.
- No puedes cobrar sin fricción.
- Después de 4 semanas, no hay retención.

Si eso pasa, no insistas con la misma tesis. Cambia el modelo o sal.

---

## La pregunta final que te haría como VC

Si solo pudieras responder una pregunta, sería esta:

> ¿Por qué un restaurante pequeño y un proveedor local aceptarían pagar 15% y seguir dentro de tu plataforma después de la primera transacción?

Si tu respuesta es “porque la app es conveniente”, no es suficiente.

Necesitas una respuesta como:

- Porque nosotros garantizamos pago inmediato al proveedor.
- Porque damos crédito al restaurante.
- Porque consolidamos entrega de múltiples proveedores.
- Porque reducimos mermas.
- Porque aseguramos stock.
- Porque damos facturación y trazabilidad.
- Porque traemos demanda incremental real.
- Porque reducimos el costo logístico por densidad.
- Porque evitamos impagos.
- Porque somos más confiables que el canal actual.

Si no puedes defender eso con datos, no tienes un marketplace. Tienes una idea bonita con riesgo operativo alto.

---

## Mi veredicto brutal

Tu hipótesis actual es demasiado blanda: “ahorrar tiempo llamando”. Eso puede ser un feature, no una empresa.

Para que esto funcione, probablemente tienes que convertirte en una de estas tres cosas:

1. **Distribuidor digital con tecnología**: controlas catálogo, precio, cumplimiento y entrega.
2. **Capa de pagos/crédito para restaurantes y proveedores**: el valor está en financiar y cobrar.
3. **Red logística densa de abastecimiento local**: ganas por eficiencia de ruta y agregación de demanda.

Si solo eres una app que conecta, con 15% de comisión y sin controlar pago, logística, crédito o calidad, el modelo se desintermedia rápido.

Con US$10K, no construyas producto. Construye evidencia. Opera manualmente. Cobra. Mide retención. Mide fuga. Mide margen. Si los restaurantes y proveedores no vuelven sin subsidio, no sigas. Si vuelven, paguen y te piden más categorías, entonces tienes algo.