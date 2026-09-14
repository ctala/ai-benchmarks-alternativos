# Qwen 3.8 Max 0902 — strategy/business_model_validation

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 296.46s | tokens_per_second: 33.3
- input_tokens: 230 | output_tokens: 9885

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

Primero, sin adornos: tu hipótesis está floja.

“Los restaurantes pequeños pierden mucho tiempo llamando a múltiples proveedores” puede ser verdad, pero **no es necesariamente un dolor por el que paguen 15%**. En restaurantes pequeños, el dolor real suele ser otro: precio, crédito, disponibilidad, calidad consistente, entrega a tiempo, factura, confianza y supervivencia financiera. Si tu propuesta es “digitalizar llamadas”, estás vendiendo conveniencia, no un analgésico. Y en LATAM, la conveniencia sola no paga comisión.

Como VC, mi primera pregunta sería:

> **¿Estás resolviendo un problema de tiempo o estás resolviendo un problema de dinero, confianza y suministro?**

Si solo resuelves tiempo, probablemente fracases.

Ahora, vamos por partes.

---

## 1. Los 5 riesgos principales de este modelo

### Riesgo 1: El dolor no es lo suficientemente fuerte

Tu hipótesis dice que los restaurantes pierden tiempo llamando proveedores. Puede ser. Pero la pregunta difícil es:

> ¿Ese tiempo perdido les cuesta más que el 15% de comisión?

Un restaurante pequeño normalmente ya tiene proveedores conocidos por WhatsApp, teléfono, confianza, crédito informal y precios negociados. Llamar o mandar WhatsApp no es gratis, pero sí es barato y conocido.

Si tu app solo reemplaza llamadas con una interfaz, el restaurante puede pensar:

> “¿Para qué me meto a otra plataforma si ya lo resuelvo por WhatsApp?”

Preguntas duras:

- ¿Cuántas horas reales pierde un restaurante pequeño a la semana haciendo pedidos?
- ¿Cuánto vale esa hora para el dueño?
- ¿Tu solución ahorra dinero o solo ahorra minutos?
- ¿El restaurante estaría dispuesto a pagar 15% indirectamente por ese ahorro?
- ¿El problema es llamar proveedores o conseguir mejor precio, crédito y entrega confiable?

Si el restaurante no puede cuantificar el ahorro, no hay negocio.

---

### Riesgo 2: Marketplace líquido es dificilísimo

Un marketplace necesita oferta y demanda al mismo tiempo, en la misma zona, con inventario real, precios reales y cumplimiento real.

Si entras con restaurantes pero no tienes proveedores suficientes, los restaurantes se frustran.

Si entras con proveedores pero no tienes restaurantes suficientes, los proveedores te abandonan.

Preguntas duras:

- ¿Cuántos proveedores necesitas para cubrir el 80% del pedido típico de un restaurante?
- ¿Puedes garantizar stock real?
- ¿Puedes garantizar precios actualizados?
- ¿Puedes garantizar entrega a tiempo?
- ¿Qué pasa si un proveedor falla?
- ¿Quién responde por calidad, faltantes, mermas y devoluciones?

Si no puedes resolver la liquidez local, no tienes marketplace; tienes un catálogo muerto.

---

### Riesgo 3: El 15% de comisión probablemente es demasiado alto

Este es uno de los puntos más débiles de tu modelo.

En alimentos, muchos proveedores trabajan con márgenes brutos bajos, especialmente en perecederos. Si un proveedor tiene margen bruto de 15%, 20% o 25%, cobrarle 15% de comisión sobre la transacción puede hacerlo inviable.

Ejemplo simple:

- Pedido promedio: $100
- Comisión 15%: $15
- Si el proveedor tiene margen bruto de 20%: $20
- Después de tu comisión: $5
- Todavía tiene operación, transporte, empaque, merma, cobranza, impuestos.

Eso no cierra.

Si el proveedor traslada tu comisión al precio, el restaurante termina pagando más caro. Entonces tu propuesta de valor se rompe.

Preguntas duras:

- ¿Quién paga realmente el 15%: el restaurante, el proveedor o ambos?
- ¿El proveedor puede absorber 15% sin subir precios?
- ¿El restaurante aceptaría precios más altos por usar tu plataforma?
- ¿Tu comisión financia logística, crédito, cobranza, devoluciones o solo software?
- ¿Por qué un proveedor no te usaría solo para descubrir clientes y luego vender por fuera?

Si tu comisión no está ligada a un valor claro, es un impuesto que el mercado intentará evitar.

---

### Riesgo 4: Desintermediación / fuga por WhatsApp

Este riesgo puede matarte.

Conectas restaurante con proveedor. La primera transacción ocurre por tu plataforma. La segunda quizá también. Pero en la tercera, el restaurante dice:

> “Mándame el pedido directo al WhatsApp y ahórrate la comisión.”

Y el proveedor responde:

> “Claro, te hago descuento.”

Eso es especialmente probable en LATAM, donde WhatsApp es gratis, universal y ya es la infraestructura real de muchos negocios.

Preguntas duras:

- ¿Qué evita que restaurante y proveedor se salten la plataforma?
- ¿Tu valor está solo en conectarlos o en operar la transacción?
- ¿Ofreces pagos, crédito, facturación, logística, garantía, trazabilidad o datos?
- ¿Qué incentivo tienen para quedarse contigo después del primer pedido?
- ¿Cómo detectas y reduces la fuga?

Si tu única defensa es “confiamos en que no se salten”, no tienes modelo.

---

### Riesgo 5: Te conviertes en un negocio operativo, no tecnológico

Muchos marketplaces de alimentos dicen ser software, pero en realidad terminan siendo empresas de logística, cobranza, atención al cliente, control de calidad y gestión de proveedores.

Si solo conectas, eres débil.  
Si operas, eres más necesario pero más costoso.

Preguntas duras:

- ¿Tú entregas o entrega el proveedor?
- ¿Tú cobras o cobra el proveedor?
- ¿Tú asumes el riesgo de impago?
- ¿Tú respondes por producto dañado?
- ¿Tú gestionas devoluciones?
- ¿Tú verificas calidad?
- ¿Tú consolidas pedidos?
- ¿Tú almacenas?
- ¿Tú financias inventario o crédito?

Si respondes “todo lo hace el proveedor”, entonces tu control es bajo.  
Si respondes “todo lo hago yo”, entonces necesitas capital, operación y márgenes mucho más altos.

---

## 2. ¿Por qué podría NO funcionar en LATAM específicamente?

LATAM no es Silicon Valley. Muchas hipótesis de marketplace se ven bonitas en PowerPoint pero se rompen en la realidad local.

### a) WhatsApp ya es tu competencia gratuita

En LATAM, el restaurante pequeño ya usa WhatsApp para todo:

- Pedir proveedores
- Negociar precios
- Confirmar entregas
- Mandar fotos
- Resolver problemas
- Mantener relaciones personales

Tu competencia no es otro software. Tu competencia es:

> WhatsApp + confianza + crédito informal + precio.

Si tu app no es radicalmente mejor que eso, no hay razón para cambiar.

---

### b) La relación personal pesa más que la eficiencia digital

Muchos restaurantes pequeños no compran solo por precio o conveniencia. Compran por confianza.

El proveedor que conoce al dueño, que le fía, que le salva un sábado, que le cambia un producto malo, que le da crédito cuando el restaurante está apretado, vale más que una app bonita.

Pregunta difícil:

> ¿Tu plataforma puede replicar la confianza de una relación humana existente?

Si no, estás en desventaja.

---

### c) El crédito informal es una barrera enorme

En muchos mercados LATAM, el restaurante compra a crédito con proveedores conocidos. No siempre es crédito formal, pero existe:

- “Te pago el viernes.”
- “Te pago a fin de mes.”
- “Te debo la semana pasada.”
- “Me fías porque llevamos años trabajando.”

Si tu plataforma exige pago inmediato y el restaurante está acostumbrado a crédito, vas a sufrir.

Pero si tú das crédito, asumes riesgo financiero. Y eso puede matarte rápido.

Preguntas duras:

- ¿Vas a ofrecer crédito?
- ¿Con qué capital?
- ¿Cómo evalúas riesgo?
- ¿Cómo cobras?
- ¿Qué pasa si el restaurante no paga?
- ¿Puedes sobrevivir con cartera vencida?

Si no resuelves crédito, puede que no resuelvas el problema real.

---

### d) Alta informalidad y baja digitalización de proveedores

Muchos proveedores locales no tienen:

- Catálogo digital
- Inventario actualizado
- Precios estables
- Facturación electrónica
- Pagos digitales
- Logística confiable
- Control sanitario
- Capacidad de respuesta rápida

Si el proveedor no puede operar con datos confiables, tu marketplace se llena de fricción.

Pregunta difícil:

> ¿Vas a digitalizar proveedores informales? Eso no es solo tecnología, es educación, operación y paciencia.

---

### e) Logística y cadena de frío débiles

Ingredientes frescos requieren:

- Refrigeración
- Tiempos cortos
- Manejo cuidadoso
- Entregas puntuales
- Control de merma
- Rutas eficientes

En muchas ciudades LATAM, la logística urbana es caótica: tráfico, inseguridad, direcciones imprecisas, costos altos y baja densidad.

Si prometes entrega confiable y no puedes cumplirla, el restaurante te abandona.

---

### f) Márgenes bajos y sensibilidad al precio

Restaurantes pequeños operan con márgenes muy ajustados. Proveedores locales también.

Un 15% adicional puede ser imposible de absorber.

En LATAM, muchos negocios no pagan software fácilmente si no ven retorno inmediato y claro. La pregunta será:

> “¿Me traes más ventas, me bajas costos o me das crédito? Si no, ¿por qué te pago?”

---

### g) Alta mortalidad de restaurantes pequeños

Los restaurantes pequeños cierran con frecuencia. Eso aumenta tu churn.

Si tu cliente promedio vive poco, tu CAC tiene que recuperarse muy rápido.

Pregunta difícil:

> ¿Tu LTV soporta la mortalidad natural de restaurantes pequeños?

Si necesitas 12 meses para recuperar CAC pero el restaurante cierra en 8, estás muerto.

---

### h) Fragmentación extrema

Puede que necesites muchos proveedores para cubrir pocas categorías. Y muchos restaurantes pequeños para generar volumen suficiente. Eso hace que la densidad sea difícil y cara de construir.

En un marketplace de alimentos, no basta con tener “muchos usuarios”. Necesitas densidad geográfica y profundidad de catálogo.

---

## 3. ¿Qué tendría que ser verdad para que funcione?

Para que esto funcione, varias hipótesis tienen que cumplirse. No una. Varias. Al mismo tiempo.

### Supuesto clave 1: El restaurante tiene un dolor recurrente y costoso

Tendría que ser verdad que el restaurante pierde dinero o ventas por:

- Pedidos mal hechos
- Proveedores que fallan
- Falta de stock
- Precios no comparables
- Tiempo administrativo excesivo
- Errores de inventario
- Compras urgentes más caras
- Falta de trazabilidad

Métricas para validarlo:

- ¿El restaurante hace pedidos varias veces por semana?
- ¿Cuánto gasta por semana en insumos?
- ¿Cuántos proveedores maneja?
- ¿Cuánto tiempo dedica a comprar?
- ¿Ha perdido platos o ventas por falta de insumos?
- ¿Ha pagado sobrecostos por urgencias?

Si el restaurante solo dice “sería útil”, no sirve. Necesitas evidencia de dolor económico.

---

### Supuesto clave 2: Los proveedores quieren volumen incremental y están dispuestos a pagar por él

Tendría que ser verdad que el proveedor local:

- Tiene capacidad ociosa
- Quiere nuevos clientes
- Puede cumplir
- Puede aceptar digitalización
- Puede pagar comisión o aceptar margen compartido
- No te usará solo como canal de adquisición para luego irse por fuera

Métricas:

- ¿El proveedor acepta pedidos recurrentes?
- ¿Su margen bruto permite comisión?
- ¿Está dispuesto a firmar exclusividad parcial o condiciones?
- ¿Puede facturar o formalizarse?
- ¿Tiene logística o necesita la tuya?

Si el proveedor no gana claramente, no se quedará.

---

### Supuesto clave 3: Puedes construir densidad local

Tendría que ser verdad que puedes dominar una zona pequeña antes de expandirte.

Por ejemplo:

- 20-30 restaurantes activos
- 5-10 proveedores clave
- 80% de los insumos más comprados cubiertos
- Pedidos recurrentes semanales
- Entrega confiable en una zona específica

Métricas:

- Tasa de cobertura de catálogo
- Fill rate: porcentaje del pedido cumplido
- On-time delivery
- Frecuencia de compra
- Retención semanal
- Participación del gasto del restaurante

Si intentas lanzar toda una ciudad desde el inicio, probablemente fracases.

---

### Supuesto clave 4: El unit economics funciona

Tendría que ser verdad que cada pedido genera contribución positiva después de costos variables.

Fórmula básica:

> Ingreso por pedido = ticket promedio × take rate  
> Costo variable por pedido = pagos, soporte, logística, merma, cobranza, devoluciones, incentivos  
> Contribución = ingreso por pedido - costo variable

Ejemplo:

- Ticket promedio: $80
- Comisión: 15%
- Ingreso bruto por pedido: $12
- Costo variable real: $8
- Contribución: $4

Si un restaurante pide 2 veces por semana, son $8/semana, $32/mes.

Ahora pregúntate:

- ¿Cuánto te cuesta adquirir ese restaurante?
- ¿Cuánto te cuesta adquirir ese proveedor?
- ¿Cuánto te cuesta dar soporte?
- ¿Cuántos meses necesitas para recuperar CAC?

Si tu CAC es $200 y tu contribución mensual es $32, necesitas más de 6 meses solo para recuperar adquisición, sin contar operación, tecnología, capital de trabajo, etc.

Para restaurantes pequeños, necesitas payback corto. Idealmente menos de 2-3 meses.

---

### Supuesto clave 5: Puedes evitar o reducir la fuga

Tendría que ser verdad que tu plataforma ofrece algo que no pueden replicar fácilmente por fuera.

Por ejemplo:

- Crédito
- Facturación
- Pagos
- Logística consolidada
- Garantía de calidad
- Trazabilidad
- Historial de pedidos
- Comparación de precios
- Descuentos por volumen
- Agregación de demanda
- Acceso a más proveedores
- Soporte operativo
- Datos de consumo

Si solo eres un conector, la fuga será alta.

---

### Supuesto clave 6: Puedes cobrar y pagar sin fricción

Tendría que ser verdad que puedes manejar pagos en un entorno con baja bancarización, informalidad y desconfianza.

Preguntas:

- ¿Pagos digitales, transferencia, efectivo, crédito?
- ¿Quién factura?
- ¿Cómo concilias?
- ¿Cómo evitas impagos?
- ¿Cómo pagas a proveedores?
- ¿Retienes comisión antes o después?
- ¿Qué pasa con devoluciones?

Si el flujo de dinero es sucio, el negocio se vuelve operativo y riesgoso.

---

### Supuesto clave 7: La calidad y el cumplimiento son consistentes

En alimentos, un mal pedido puede matar la confianza.

Tendría que ser verdad que puedes mantener:

- Producto fresco
- Cantidades correctas
- Sustituciones inteligentes
- Entregas a tiempo
- Proveedores confiables
- Control de incidencias

Métricas:

- Fill rate > 90%
- On-time delivery > 90%
- Tasa de incidencia < 5%
- Recompra semanal > 60-70%

Si no puedes cumplir, el restaurante vuelve a su proveedor de confianza.

---

### Supuesto clave 8: Tu equipo puede operar en el barro

Esto no es solo producto. Es un negocio de campo:

- Visitar restaurantes
- Convencer proveedores
- Resolver entregas
- Cobrar
- Apagar incendios
- Gestionar calidad
- Soportar márgenes bajos

Si el equipo solo quiere construir app y no quiere operar, no va a funcionar.

---

## 4. ¿Cuál es el escenario donde fracasas rápido y por qué?

El escenario clásico de fracaso rápido sería este:

### Mes 1-2: Lanzas con entusiasmo

- Haces una app simple o un MVP.
- Convences a 30 restaurantes pequeños.
- Afilias a 10 proveedores locales.
- Prometes pedidos digitales, ahorro de tiempo y mejores proveedores.
- Ofreces 15% de comisión.

### Mes 2-3: Aparece la realidad

Los restaurantes piden, pero:

- Algunos proveedores no tienen stock actualizado.
- Los precios cambian.
- Las entregas llegan tarde.
- Faltan productos.
- La calidad no es consistente.
- El restaurante tiene que reclamar.
- Tú terminas haciendo soporte manual.

Los proveedores dicen:

- “El volumen es bajo.”
- “La comisión es alta.”
- “Mejor que me pidan directo.”
- “No puedo mantener precios en la plataforma.”

Los restaurantes dicen:

- “Está bueno, pero más caro.”
- “Prefiero llamar al de siempre.”
- “El proveedor me fía y tú no.”
- “La app no me ahorra tanto.”

### Mes 3-5: Fuga y churn

Restaurantes y proveedores se conectan entre sí. Empiezan a transar por WhatsApp para evitar la comisión. Tú te quedas con:

- Menos transacciones
- Menos ingresos
- Más soporte
- Más costo operativo
- Menos liquidez
- Menos razones para seguir

### Mes 5-8: Te quedas sin caja

Si levantaste algo de capital o pusiste dinero propio, empiezas a quemar en:

- Ventas
- Marketing
- Operación
- Soporte
- Descuentos
- Logística
- Desarrollo

Pero no ves retención fuerte.

### Causa raíz del fracaso

No fracasaste porque la tecnología fuera mala. Fracasaste porque:

1. El dolor no era lo suficientemente monetizable.
2. La comisión era demasiado alta para el margen del sector.
3. No tenías densidad local.
4. No controlabas la experiencia de cumplimiento.
5. No evitaste la desintermediación.
6. No resolviste crédito, confianza o precio.
7. Subestimaste la operación.

El fracaso rápido ocurre si lanzas amplio, sin densidad, con comisión alta, sin control operativo y sin un motivo fuerte para que ambos lados se queden.

---

## 5. Si solo tuviera $10K para validar, ¿qué haría?

No construiría una app.

Con $10K, tu objetivo no es crear una plataforma bonita. Tu objetivo es responder:

> ¿Existe una transacción repetible, rentable y deseada entre restaurantes pequeños y proveedores locales?

Haría un experimento manual, concentrado y brutalmente medible.

---

### Paso 1: Elegir un micro-mercado

No lances ciudad completa. Elige una zona con:

- Alta densidad de restaurantes pequeños
- Proveedores locales accesibles
- Distancia corta de entrega
- Categorías repetitivas: verduras, proteínas, abarrotes, lácteos, pan, etc.

Ejemplo:

- Una colonia/barrio específico
- 20 restaurantes objetivo
- 5-8 proveedores objetivo

No intentes cubrir todo. Cubre una zona y unas categorías clave.

---

### Paso 2: No vender “app”, vender servicio

Tu propuesta inicial debería ser algo como:

> “Mándame tu pedido antes de las 6 pm. Yo te consolido proveedores, confirmo disponibilidad, coordinamos entrega y te ahorro tiempo. Si algo falla, yo respondo.”

Eso es un servicio, no una app.

Usa:

- WhatsApp Business
- Google Sheets / Airtable
- Formularios simples
- Llamadas
- Pagos manuales
- Confirmaciones humanas

No gastes en desarrollo.

---

### Paso 3: Reclutar proveedores con incentivos claros

Busca 5-8 proveedores que:

- Tengan capacidad de entrega
- Precios competitivos
- Productos recurrentes
- Disposición a probar
- Margen suficiente para pagar comisión reducida o margen compartido

Ofrece:

- Clientes nuevos
- Volumen agregado
- Pagos rápidos, si puedes
- Pedidos consolidados
- Menos costo comercial

Al inicio, no intentes cobrar 15% completo. Mejor prueba:

- 5%
- 8%
- 10%
- O margen sobre precio
- O fee por pedido
- O suscripción piloto

El objetivo es medir disposición real a pagar, no imponer tu modelo ideal.

---

### Paso 4: Reclutar restaurantes con una promesa concreta

No digas “digitalizamos tus compras”.

Di algo como:

- “Consolidamos tus pedidos en un solo lugar.”
- “Te ahorramos X horas por semana.”
- “Te damos precios comparables.”
- “Coordinamos entrega.”
- “Si algo falla, lo resolvemos.”

Ofrece un incentivo inicial:

- Primer pedido con descuento
- Envío gratis piloto
- Precio especial en categoría ancla
- Soporte dedicado

Pero cuidado: si solo compran por descuento y no repiten sin descuento, no validaste nada.

---

### Paso 5: Operar manualmente durante 6 semanas

Durante 6 semanas, tú y un asistente hacen todo:

- Reciben pedidos
- Confirman stock
- Cotizan
- Consolidan
- Coordinan entrega
- Cobran
- Pagan proveedores
- Resuelven incidencias
- Miden todo

No automatices todavía. El dolor manual te mostrará la verdad.

---

### Paso 6: Medir métricas clave

No midas “likes”, “registros” o “descargas”. Mide transacción y retención.

Métricas mínimas:

#### Demanda

- Restaurantes que hicieron primer pedido
- Restaurantes que repiten
- Frecuencia semanal
- Ticket promedio
- Categorías compradas
- Retención semana 1, 2, 3, 4
- Razones de abandono

#### Oferta

- Proveedores activos
- Fill rate
- On-time delivery
- Incidencias
- Margen por proveedor
- Disposición a pagar comisión
- Intentos de fuga

#### Economía

- Ingreso por pedido
- Costo variable por pedido
- Contribución por pedido
- CAC por restaurante
- CAC por proveedor
- Payback estimado
- Fuga estimada

#### Dolor

- Tiempo ahorrado real
- Costo evitado
- Mejora de precio
- Reducción de faltantes
- Nivel de satisfacción
- Intención de pago

---

### Presupuesto sugerido con $10K

Aquí hay una asignación práctica:

| Concepto | Monto | Uso |
|---|---:|---|
| Ventas de campo / operaciones | $2,500 | Persona que visita restaurantes, coordina pedidos, llama proveedores |
| Marketing local / adquisición | $1,500 | Volantes, visitas, pequeñas campañas, materiales, tiempo de prospección |
| Incentivos para primeros pedidos | $2,000 | Descuentos controlados, envío gratis piloto, promociones |
| Herramientas / telefonía / datos | $700 | WhatsApp Business, Airtable, Sheets, CRM simple, teléfono |
| Logística / pruebas de entrega | $1,300 | Mensajería puntual, transporte, frío, empaques, incidencias |
| Legal / contabilidad básica | $700 | Contratos simples, términos, facturación, asesoría mínima |
| Caja de emergencia | $1,300 | Imprevistos, devoluciones, faltantes, ajustes |
| Total | $10,000 |  |

No gastes $5K en una agencia. Eso sería un error.

---

### Diseño del experimento

Duración: 6 semanas.

Objetivo mínimo:

- 15-20 restaurantes contactados profundamente
- 8-12 restaurantes haciendo pedidos reales
- 5-8 proveedores activos
- 3 categorías recurrentes
- Al menos 2 ciclos de pedido por semana

No necesitas miles de usuarios. Necesitas señales fuertes.

---

### Criterios de éxito

Consideraría señales positivas si, después de 6 semanas:

- Al menos 8-10 restaurantes piden 2+ veces por semana.
- Ticket promedio suficiente para que la comisión importe.
- Fill rate mayor a 90%.
- Entrega a tiempo mayor a 90%.
- Incidencias menores a 5%.
- Restaurantes reportan ahorro real de tiempo o dinero.
- Proveedores repiten y aceptan pagar al menos 5-8%.
- Menos de 20% de fuga detectada.
- Contribución por pedido positiva, aunque sea pequeña, antes de tu sueldo completo.
- Hay intención explícita de pago sin subsidio.

Si ves eso, puedes pensar en construir software.

---

### Criterios de muerte

Deberías parar o pivotar si:

- Menos de 5 restaurantes repiten semanalmente.
- El ticket promedio es demasiado bajo para sostener 15%.
- Los proveedores no aceptan comisión ni margen.
- Más de 20-30% de los pedidos se intentan ir por fuera.
- Fill rate menor a 80%.
- On-time delivery menor a 80%.
- Necesitas subsidiar cada pedido para que ocurra.
- Los restaurantes dicen “está bueno” pero no pagan ni repiten.
- El costo operativo por pedido supera el ingreso.
- Pasas más tiempo apagando incendios que generando transacciones.

Si después de 6 semanas no hay repetición orgánica, no tienes producto. Tienes un experimento caro.

---

## Las preguntas difíciles que te haría en un pitch

Si estuvieras frente a mí, te preguntaría esto:

1. ¿Tu cliente realmente pierde dinero o solo pierde tiempo?
2. ¿Cuánto dinero, en números?
3. ¿Por qué pagarían 15% indirectamente por resolverlo?
4. ¿Quién paga la comisión: restaurante, proveedor o ambos?
5. ¿El proveedor puede absorber 15% sin quebrar?
6. ¿Qué haces para evitar que se salten por WhatsApp?
7. ¿Tu marketplace resuelve precio, crédito, logística o solo conexión?
8. ¿Por qué un restaurante dejaría a su proveedor de confianza por ti?
9. ¿Cómo construyes liquidez local con poco capital?
10. ¿Cuál es tu fill rate objetivo y cómo lo garantizas?
11. ¿Quién responde si el producto llega malo?
12. ¿Quién responde si la entrega llega tarde?
13. ¿Vas a manejar crédito? Si sí, ¿con qué capital y riesgo?
14. ¿Cuál es tu ticket promedio esperado?
15. ¿Cuál es tu frecuencia de compra esperada?
16. ¿Cuál es tu ingreso bruto mensual por restaurante?
17. ¿Cuál es tu CAC por restaurante?
18. ¿En cuántos meses recuperas CAC?
19. ¿Cuál es tu churn esperado dado que muchos restaurantes cierran?
20. ¿Por qué esto no es solo un directorio con WhatsApp?
21. ¿Qué proveedor gana contigo que no gane sin ti?
22. ¿Qué restaurante gana contigo que no gane con su proveedor actual?
23. ¿Tu ventaja es precio, surtido, crédito, logística, datos o confianza?
24. ¿Puedes demostrar una transacción repetible manualmente antes de escribir código?
25. Si te doy $10K, ¿qué evidencia me traes en 6 semanas?

---

## Mi veredicto brutal

Tu idea no es mala por definición, pero está planteada de forma peligrosa.

El error más probable es creer que el problema es “llamar proveedores” y que la solución es “una app”. En alimentos pequeños, eso suele ser insuficiente.

Para que funcione, probablemente tengas que convertirte en algo más profundo:

- Un agregador de demanda.
- Un operador de compras.
- Un coordinador logístico.
- Un facilitador de crédito.
- Un sistema de abastecimiento confiable.
- Un comprador digital para restaurantes.
- O un canal de ventas incremental para proveedores.

Si solo eres un intermediario digital con 15% de comisión, vas a sufrir.

La versión más fuerte de tu idea sería:

> “Ayudamos a restaurantes pequeños a comprar mejor, con proveedores confiables, precios claros, pedidos consolidados, entrega coordinada y menos caos operativo.”

No:

> “Hacemos una app para que no llamen.”

La primera versión puede valer dinero. La segunda puede ser una feature que nadie paga.

---

## Lo que haría mañana

1. No construiría app.
2. Elegiría una sola zona.
3. Conseguiría 10 restaurantes comprometidos.
4. Conseguiría 5 proveedores con margen.
5. Operaría pedidos manualmente por WhatsApp/Sheets.
6. Cobraría una comisión baja o margen de prueba.
7. Mediría repetición, fill rate, ticket, fuga y contribución.
8. Después de 6 semanas, decidiría con datos.

Si no puedes hacerlo manualmente con $10K, una app no te salvará.

Y si después del experimento los restaurantes no repiten sin descuento, los proveedores no pagan, y la fuga es alta, entonces mata la idea rápido y pivota antes de quemar más dinero.