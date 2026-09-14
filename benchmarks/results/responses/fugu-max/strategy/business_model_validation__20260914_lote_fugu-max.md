# Fugu Max — strategy/business_model_validation

- model_id: `sakana/fugu-max`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 31.965s | tokens_per_second: 106.1
- input_tokens: 249 | output_tokens: 3390

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

Si vinieras a mi oficina con este pitch, te detendría en la diapositiva dos. Tu modelo tiene supuestos letales que demuestran que no has operado un restaurante ni has pisado una central de abastos a las 4 de la mañana.

Aquí está el baño de realidad:

---

### 1. Los 5 riesgos principales de este modelo

1. **Un *Take Rate* ridículo e insostenible (15%):**
   Los márgenes netos de los distribuidores de alimentos al por mayor son del **3% al 8%**. Si pretendes cobrar un 15% de comisión, solo hay dos caminos: o el proveedor entra en pérdidas operativas al vender en tu app, o infla los precios un 15-20%. Un restaurante pequeño opera con márgenes de supervivencia; si ven que un kilo de cebolla está 10% más caro en tu app que en la calle, no te vuelven a abrir en la vida.
2. **Desintermediación instantánea (*Platform Leakage*):**
   Tu producto conecta a dos partes que tienen **alta recurrencia** y compran **artículos homogéneos (commodities)**. La dinámica es obvia:
   *Orden 1:* Te usan para conocerse.
   *Orden 2:* El chofer le da una tarjeta de presentación al cocinero y le dice: *"Pídeme directo por WhatsApp y te descuento el 10% que me cobra la app"*.
   Tu LTV (Lifetime Value) real tiende a una sola transacción por usuario. Eres un directorio telefónico caro, no un marketplace.
3. **El infierno de la calidad y la merma (Disputas físicas):**
   Esto no es vender camisetas o software. Si el proveedor envía 20 kg de aguacates verdes o 10 kg de carne golpeada a las 11:30 AM (media hora antes del servicio del almuerzo), ¿quién se come la pérdida? Si no te metes, el restaurante te odia y desinstala la app. Si te metes a mediar o indemnizar, quemas tu margen en 3 disputas.
4. **La trampa del Capital de Trabajo (*Working Capital*):**
   Los restaurantes pequeños sobreviven gracias al **crédito informal** (pago a 15, 30 días o "a la palabra" con su casero/proveedor). Si tu app exige pago contra entrega o tarjeta, pierdes al 80% del mercado. Si permites crédito a 30 días pero tú le pagas de contado al proveedor para atraerlo, necesitas ser un banco, no una app. Tu caja colapsará en dos meses.
5. **CAC astronómico vs. Churn estructural:**
   Adquirir restaurantes pequeños exige venta física, puerta a puerta, hablando con dueños desconfiados o cocineros ocupados (CAC altísimo). A la vez, el 50-70% de los restaurantes independientes quiebran antes de cumplir dos años en el mercado. Vas a gastar fortunas en adquirir clientes que van a cerrar sus puertas en 6 meses.

---

### 2. ¿Por qué NO va a funcionar en LATAM específicamente?

* **WhatsApp ya ganó la batalla:** Tu competencia no es otra app; es WhatsApp. WhatsApp es gratis, no consume memoria, permite enviar audios de 10 segundos pidiendo *"mándame lo de siempre"* y ya está en el bolsillo de todos. Convencer a un parrillero de 50 años de registrarse en un marketplace, recordar una contraseña y cargar un carrito SKU por SKU es pelear contra la gravedad.
* **La economía subterránea y la informalidad:** Gran parte de los proveedores locales y restaurantes operan en efectivo, sin factura o con doble contabilidad para esquivar impuestos. Una app digital deja trazabilidad bancaria y fiscal obligatoria. En el momento en que les digas que la transacción pasa por pasarela de pagos con retención de IVA/ISR, huyen despavoridos.
* **El ecosistema de las Centrales de Abasto:** En LATAM (Corabastos en Bogotá, Central de Abasto en CDMX, Lo Valledor en Santiago), la cadena de intermediarios es brutalmente eficiente a nivel de precios y logística de bajo costo. Tienen economías de escala informales imposibles de vencer desde un software con sede en una incubadora.

---

### 3. ¿Qué tendría que ser verdad para que funcione? (*Key Assumptions*)

Para que yo pusiera un centavo en esto, tendrías que demostrarme empíricamente que:

1. **La conveniencia supera al precio:** Tienes que probar que al dueño de una pizzería de barrio le importa más "ahorrar 20 minutos llamando" que "ahorrar $50 dólares semanales en insumos". *(Pista: en las PYMEs de LATAM, el tiempo del dueño vale $0 en su contabilidad mental, pero $50 dólares en efectivo pagan la luz).*
2. **El Take Rate debe venir del *spread*, no de una comisión plana:** Tienes que ser capaz de negociar con un margen de intermediación del 3% al 5% o cobrar un modelo SaaS/suscripción plana, no un 15% por transacción.
3. **Tienes un *Lock-in* operacional o financiero:** Que el restaurante no pueda salir de tu plataforma porque tú les das algo que el proveedor jamás les dará por fuera: software de gestión de costos de menú (KDS/ERP) o **líneas de crédito embebidas (Fintech)**. Sin eso, no hay retención.

---

### 4. El escenario de fracaso rápido

* **Mes 1-2:** Te gastas el dinero desarrollando la app (o pagando a un desarrollador no-code). Recorres 100 restaurantes. Logras que 25 descarguen la app porque fuiste simpático y les regalaste un cupón.
* **Mes 3:** Ocurren las primeras 40 transacciones. Dos pedidos de mariscos llegan en mal estado. Uno llega tres horas tarde. Los restaurantes te bombardean por WhatsApp a ti para reclamar. Los proveedores te reclaman que por qué les descuentas el 15%.
* **Mes 4:** En la segunda compra de cada restaurante, el proveedor les mete un papelito en la caja con su número privado ofreciéndoles el mismo precio sin comisión. El volumen en tu app cae 85% de la noche a la mañana.
* **Mes 6:** Quemas tu pista de aterrizaje (*runway*). Tienes cero recurrencia, cuentas por cobrar incobrables y el restaurante volvió a pedirle al señor de la camioneta por WhatsApp. Estás muerto.

---

### 5. Si solo tuvieras $10K para validar, ¿qué deberías hacer?

**No toques una sola línea de código.** Si gastas $1 en programar una app, mereces perder tu dinero.

Haz un **MVP estilo *Wizard of Oz*** totalmente manual:

1. **Elige un micro-nicho geográfico e hiperespecífico:** Un solo barrio (ej. 10 cuadras) y un solo insumo no perecedero o de alta rotación (ej. quesos y harinas para pizzerías, o aceite y pollo para pollerías). Olvídate de "todos los ingredientes".
2. **Fase manual:**
   * Ve a 10 pizzerías. Diles: *"Yo te consigo la muzzarella 5% más barata que tu proveedor actual y te la dejo en tu cocina a las 9 AM todos los martes. Si no llega a tiempo, no me pagas"*.
   * Consigue al proveedor mayorista tú mismo. Cómprale al por mayor con tus $10K de fondo rotativo.
   * Coordina todo por un grupo de **WhatsApp Business y una hoja de Google Sheets**.
3. **El experimento ácido de la comisión:**
   * En la tercera entrega, diles la verdad económica: trasládales el costo o cobra tu comisión real.
   * Evalúa la métrica que importa: **¿Se quedan contigo cuando les cobras tu margen, o llaman al proveedor que vieron llegar en la camioneta para saltarte?**

Si en 4 semanas no logras hacer 50 órdenes repetidas de forma manual reteniendo a los clientes a pesar de tu margen, **el software no solucionará absolutamente nada.** Habrás validado que el negocio no vuela y te habrás ahorrado 9 meses de tu vida y miles de dólares.