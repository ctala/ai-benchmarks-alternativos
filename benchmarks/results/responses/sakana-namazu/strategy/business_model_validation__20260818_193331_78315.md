# Sakana Namazu — strategy/business_model_validation

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 22.338s | tokens_per_second: 194.1
- input_tokens: 277 | output_tokens: 4336

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

Aquí va. Pongo mi *sombrero de VC escéptico* y te hablo como si estuvieras en mi sala y ya me hubieras hecho perder 4 minutos de mi vida con una idea que he escuchado —y he visto morir— docenas de veces.

---

### 1. Los 5 riesgos que hacen que este negocio probablemente sea basura

**Riesgo 1: El problema del huevo y la gallina, pero peor.**  
Necesitas densidad simultánea. Si traes 50 restaurantes pero solo 3 proveedores, se quedan sin opciones y se van. Si traes 20 proveedores pero 4 restaurantes, los proveedores no venden y se desconectan. Los marketplaces B2B mueren aquí porque la "liquidez" requiere una coordinación perfecta en una micro-zona geográfica. Tu modelo no escala orgánicamente; requiere un esfuerzo heróico de *onsite* en cada colonia.

**Riesgo 2: Disintermediación (el elefante en la habitación).**  
Una vez que el taquero conoce al mayorista de pollo... ¿por qué diablos seguiría pagándote el 15%? En B2B, especialmente en alimentos, la relación se estabiliza rápido. El pedido es recurrente y los SKU son los mismos. Si tu plataforma solo hace el "match" inicial, eres un directorio caro. Y no me vengas con "bloquearemos los teléfonos"; eso es infantil. En LATAM la confianza se construye cara a cara, no con UX.

**Riesgo 3: Un 15% de comisión es una broma de mal gusto para este sector.**  
Los restaurantes pequeños operan con márgenes netos del 5% al 10%. ¿Y tú quieres comerte el 15% sobre la transacción? Eso no es "conveniencia"; eso es un impuesto confiscatorio. Quejarse de "perder tiempo llamando" suena a problema de primer mundo. Un dueño de una fondita en la Ciudad de México o Lima tiene problemas reales: pagar la luz, la extorsión del local, la inflación de insumos. No le importa tu app si puedes ahorrarle $500 pesos al mes pero cobrarle $2,000 en comisiones.

**Riesgo 4: La logística te matará, y tú no la controlas.**  
Hablamos de perecederos. Tomates, carnes, pescados, hojas. Si el proveedor entrega tarde, si la calidad no es la que dijo, si falta mercancía... ¿quién se chama el problema? Si eres tú (el marketplace), tu *take rate* del 15% se evaporará en atención al cliente y reembolsos. Si no eres tú, entonces tu "plataforma" es un simple catálogo y el valor real lo pone el proveedor. En ese caso, ¿por qué no se van a WhatsApp?

**Riesgo 5: El patrón de compra es "anti-tecnológico".**  
El dueño del restaurante pequeño no quiere una app distinta para cada proveedor. Quiere marcar a don Manuel a las 6:00 a.m., que le deje la caja de aguacates en la puerta y le firme una nota. No quiere un dashboard. Si el pedido es siempre el mismo, la eficiencia de llamar a 3 personas es un problema menor comparado con el costo de adoptar tu sistema.

---

### 2. ¿Por qué específicamente en LATAM esto probablemente no funciona?

Porque en LATAM el comercio de abasto funciona con **credito informal, confianza interpersonal y flujo de caja diferido.** Es decir: el proveedor le deja la mercancía hoy y le cobra a 15, 30 o 60 días. O le hace fiado. O le cambia el precio según la temporada pero le avisa por WhatsApp.

Tu modelo necesita:
- **Formalidad:** El proveedor debe facturar, tener cuenta bancaria, y aceptar que retengas el 15%.
- **Pago instantáneo:** Tu marketplace probablemente detiene dinero o exige prepago. Eso mata al restaurante que vive al día.
- **Logística no regulada pero funcional:** En Londres o Berlín, un camioncito llega a las 11:00 a.m. En Ciudad de México, Bogotá o São Paulo, el tráfico, la inseguridad y la falta de zonas de carga hacen que la entrega sea un caos. El proveedor local no tiene flota GPS; usa su camioneta vieja.
- **WhatsApp como sistema operativo:** En LATAM, WhatsApp *es* el sistema de pedidos, CRM y soporte del 80% de los negocios. Es gratis, flexible y permite "venta conmemorativa". Tu app tiene que ser 10 veces mejor que un grupo de WhatsApp para que valga la pena descargarla. Y no lo es.

---

### 3. ¿Qué tendría que ser verdad para que esto funcione?

Estas son tus *key assumptions*. Si una sola de estas es falsa, tu empresa es carne muerta.

1. **Que exista una "zona de densidad mágica":** Un área geográfica pequeña (ej. 5 km²) con suficientes restaurantes independientes y proveedores para que el marketplace tenga liquidez sin logística propia.
2. **Que el dolor de llamar sea > 15% del valor del pedido:** El restaurante debe estar tan desesperado por eficiencia que esté dispuesto a entregarte literalmente sus utilidades. En un negocio con 7% de EBITDA, pagar 15% es suicidio económico... a menos que tú le *garantices* ahorros de >20% en precio de insumos.
3. **Que la disintermediación sea prevenible o irrelevante:** Tendría que ser estructuralmente imposible o doloroso que restaurante y proveedor hagan negocio fuera de la app. Lo único que logra eso es si tú controlas el crédito, la logística o los datos fiscales. Si no, se van a WhatsApp en semana 3.
4. **Que los proveedores locales necesiten desesperadamente demanda adicional:** Si el proveedor ya vende todo a los restaurantes del mercado municipal, ¿por qué pagaría un 15% por acceso a clientes que ya tiene? Tendrían que tener exceso de inventario perecedero que se pudre.
5. **Que puedas construir una solución de logística o financiamiento con un take rate que no sea el 15% al restaurante, sino un fee al proveedor o un spread financiero.** Es decir, tendrías que ser más un **SaaS+logística+fintech** que un simple marketplace de pedidos. Y eso ya no es lo que describiste.

---

### 4. Escenario de fracaso rápido

Mes 1: Gastas dinero en ads de Facebook para captar 40 restaurantes y 15 proveedores. Haces 80 transacciones. Todo huele bien.

Mes 2: Los restaurantes empiezan a guardar los números de celular de los proveedores. Descubren que si le marcan directo, les hacen precio "sin IVA" y les dan 15 días de crédito. Los pedidos por tu app caen un 60%. Los que quedan son los más pequeños, con tickets bajos y reclamos altos.

Mes 3: Te das cuenta de que el 15% lo sientes tú como un impuesto, pero el restaurante lo siente como un robo. Empiezas a bajar la comisión a 8%, pero ahora tu *unit economics* no cierra. Además, un pedido de aguacates llegó podrido y te reclaman; como "intermediario digital", eres el culpable. Tienes que reembolsar de tu bolsillo.

Mes 4: El 80% de las transacciones ya suceden por WhatsApp entre los mismos actores. Tienes una app hermosa... que nadie usa. Te quedaste sin *runway* porque creíste que el problema era tecnología y no comportamiento humano y financiero.

**Moraleja:** Mueres no por falta de producto, sino porque resolviste un problema que no dolía lo suficiente comparado con el costo de la solución.

---

### 5. Solo tienes $10K. ¿Qué haría?

Ni se te ocurra escribir una línea de código. Usemos el dinero para validar si el perro comerá la comida.

**Semanas 1-2: Identifica la micro-zona.**  
Gasta $1,000 en un estudiante paseador de colonia. Que mapee 50 restaurantes pequeños y 20 proveedores (locales, mercados, mayoristas chicos) en una zona densa (ej. la Roma en CDMX, Barranco en Lima). Pregunta: ¿a quién le compran? ¿a crédito o de contado? ¿cuánto gastan a la semana?

**Semanas 3-6: El "concierge MVP" más rudimental del mundo.**  
- Crea un grupo de WhatsApp Business: "Abasto Roma Express".  
- Ofrece a 10 restaurantes: "Yo consigo tus insumos y te los llevo mañana. Pagas contra entrega."  
- Consigue 5 proveedores dispuestos a darte un descuento por volumen (o a dejarte una utilidad).  
- Opera todo **manualmente**. Tú eres el algoritmo. Tú pasas los pedidos por WhatsApp. Tú cobras en efectivo o transferencia. No hay app.

**Gasto:** $5,000 en horas de operador/fletero de moto para las entregas (tú o un contratado). Otros $2,000 en insumos de prueba o gap de flujo.

**Semanas 7-8: Mide las métricas brutales.**  
- ¿Cuántos de los 10 restaurantes reordenaron en semana 5?  
- ¿Intentaron contactar directo al proveedor?  
- ¿Te pagaron puntual?  
- ¿Cuál fue tu margen real después de pérdidas, tiempo y logística?  
- ¿Te pidieron crédito?

Si la retención a 8 semanas es <40% o si la gente te ve como "el intermediario innecesario", matas el proyecto. Perdiste $8K, no $800K.

Si funciona (y dudo que lo haga al 15%, pero quizás al 5% + logística), entonces pides pre-seed para automatizar el *pain point* real, que probablemente no es el "marketplace", sino la **logística de última milla de abasto** o el **crédito corto plazo**.

---

### Mi pregunta final antes de que salgas de esta sala:

**¿Por qué un restaurante que opera con márgenes del 5% pagaría el 15% a ti en lugar de seguir usando WhatsApp + una libreta, si el único valor que le das es ahorrarle 3 llamadas telefónicas a la semana?**

Piénsalo. Y no me vengas con "porque es más fácil". En LATAM, "más fácil" no paga la renta. El dinero sí.