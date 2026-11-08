# DeepSeek V4 Pro (0813) — strategy/business_model_validation

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 180.911s | tokens_per_second: 54.2
- input_tokens: 267 | output_tokens: 9799

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

Voy a ser directo: tu hipótesis es débil porque confunde “pierdo tiempo llamando” con “pagaré 15% por no llamar”. En abastecimiento de alimentos, 15% es una comisión enorme. No te voy a preguntar por el TAM; te voy a preguntar por qué no te saltan en la segunda transacción.

---

## 1. Los 5 riesgos principales de este modelo

**1. Desintermediación post-primera compra.**  
*Pregunta de pitch: “¿Qué impide que el restaurante y el proveedor se salten la app después del primer pedido?”*  
Si no controlas logística, pago, crédito o calidad, el 15% es un incentivo gigante para que ambos se vayan por WhatsApp. Te conviertes en un directorio gratuito.

**2. Liquidez hiperlocal / chicken-egg.**  
*Pregunta: “¿Cuántos proveedores con precios reales tienes a 5 km de cada restaurante?”*  
El abasto no es nacional; es de barrio, de colonia, de relación. Si el restaurante abre la app y no ve a sus proveedores o no ve mejor precio, no vuelve. Y los proveedores no entran si no hay demanda densa.

**3. La comisión del 15% es confiscatoria para el margen.**  
*Pregunta: “¿Quién absorbe el 15%?”*  
Si lo absorbe el proveedor, desaparece su utilidad. Si lo traslada al restaurante, es más caro que el canal directo. Si lo pagas tú con subsidios, no es negocio. En distribución de alimentos, los márgenes netos suelen ser de un dígito. Un 15% no es comisión de software, es un socio con participación alta.

**4. Logística, perecederos y calidad.**  
*Pregunta: “Si llega tomate podrido o no llega, ¿quién responde por la cocina parada?”*  
Un marketplace sin fulfillment se lleva la culpa de una entrega fallida. La confianza con el proveedor actual vale más que un catálogo bonito. Si no garantizas calidad y entrega, la app empeora el problema.

**5. Adopción y retención de usuarios poco digitales.**  
*Pregunta: “¿Por qué un dueño de restaurante va a dejar de pedir por teléfono/WhatsApp?”*  
El status quo es gratis, flexible, con crédito y relación personal. La app no resuelve solo “tiempo”; agrega fricción. Cambiar hábitos en este segmento es caro y lento.

---

## 2. Por qué podría NO funcionar en LATAM específicamente

- **Informalidad y efectivo:** Muchos proveedores y restaurantes no facturan, manejan efectivo y no quieren dejar rastro digital. Una plataforma formal con comisión del 15% es un impuesto operativo y fiscal implícito.
- **Crédito “fiado”:** El restaurante pequeño vive de pagar a 7–15 días. Si tu marketplace exige pago en línea o no da crédito, no compite con el proveedor de siempre.
- **Centrales de abasto y mercados mayoristas:** El precio real se descubre cada mañana en el mercado, con regateo y disponibilidad volátil. Un catálogo digital se vuelve obsoleto en horas.
- **Márgenes mínimos:** El restaurantero pequeño opera al día. No paga 15% por comodidad si eso lo saca de precio frente al proveedor de la esquina.
- **Logística urbana y seguridad:** Tráfico, inseguridad, cadena de frío irregular, direcciones informales. Los proveedores locales entregan como pueden; una app no resuelve eso.
- **Cultura de relación:** El abasto se basa en confianza, favores y flexibilidad. La tecnología no reemplaza eso si no construye confianza desde el día uno.

Ya hubo intentos de digitalizar abastecimiento B2B en LATAM con capital. El problema no es falta de app; es retención, margen y comportamiento.

---

## 3. Qué tendría que ser verdad para que funcione

Estos son los supuestos clave, probablemente falsos hasta que demuestres lo contrario:

- Que el dolor de coordinar proveedores es tan intenso que el restaurantero está dispuesto a pagar 15% o cambiar de proveedor.
- Que puedes lograr densidad de oferta y demanda en una zona geográfica pequeña sin gastar demasiado en adquirir usuarios.
- Que la plataforma agrega algo más que contacto: logística, crédito, estandarización, garantía de calidad o poder de compra.
- Que los proveedores actualizan precios e inventario y no usan la app solo como captador de clientes.
- Que la frecuencia y el ticket alcanzan para pagar CAC: por ejemplo, ticket >$100, >3 pedidos/semana, margen bruto >30%.
- Que la retención es alta: >50% de restaurantes activos después de 90 días sin subsidios.
- Que existe una ventaja defendible frente a distribuidores, centrales de abasto y apps de delivery que pueden entrar a B2B.

En resumen: tendría que ser verdad que no eres un marketplace de contactos, sino una infraestructura de abastecimiento.

---

## 4. Escenario de fracaso rápido

Lanzas en una zona. A bordo de 80 restaurantes y 20 proveedores. Como cobras 15%, los proveedores suben 10–20% el precio en plataforma. El restaurante pide una vez por un descuento de lanzamiento. El pedido llega tarde o con calidad inconsistente. El restaurante se comunica directo con el proveedor; el proveedor le da su WhatsApp. Nadie te dice.

Al tercer mes: retención <15%, proveedores que no actualizan, GMV artificial por descuentos, CAC alto. La app se convierte en catálogo gratuito para encontrar proveedores y luego saltarte. Mueres como lead gen sin ingresos.

Ese fracaso es rápido no por falta de app, sino porque la propuesta de valor no supera el status quo.

---

## 5. Si solo tuviera $10K para validar, haría esto

No construiría app. Haría un marketplace manual/concierge en un micro-mercado.

**Plan de 6–8 semanas:**

1. **Zona:** 2–3 barrios densos en restaurantes. Nada de ciudad entera.
2. **Mapeo:** 50–60 restaurantes pequeños y 15–20 proveedores locales.
3. **Calle:** Entrevistar y acompañar compras a 20 restaurantes. Medir tiempo, llamadas, precios, crédito. No preguntar “¿usarías una app?”; observar.
4. **Central de pedidos manual:** WhatsApp/Google Sheets. Consolida precios cada mañana y toma pedidos.
5. **Operación:** 15–20 restaurantes, 10 proveedores. Coordina entregas tú mismo o con un repartidor.
6. **Cobro:** Primeras 2–3 semanas gratis; luego cobra 5–8% para ver si se quedan; luego prueba si 15% es viable.
7. **Métricas clave:** % de restaurantes que repiten >3 pedidos sin subsidio, frecuencia, ticket, intentos de desintermediación, actualización de precios.
8. **Criterio de muerte:** Si después de 6 semanas no tienes al menos 30% de restaurantes activos semanales y retención >50%, no levantes capital.

**Presupuesto $10K:**
- $2,500: calle, transporte, entrevistas.
- $2,000: incentivos iniciales para primeras órdenes, midiendo luego sin subsidio.
- $1,500: herramientas no-code, WhatsApp Business, Google Sheets, landing simple.
- $1,500: logística piloto / fletes.
- $1,000: legal básico y contratos simples.
- $1,500: reserva.

**Conclusión brutal:** si no funciona manualmente con WhatsApp y una persona coordinando, no funcionará con app. Y si la gente se salta tu comisión al segundo pedido, no tienes un marketplace; tienes un directorio gratuito con gastos.