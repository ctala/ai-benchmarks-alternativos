# GPT-OSS 20B — strategy/business_model_validation

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.28 | quality: 10.0
- latency_total: 15.832s | tokens_per_second: 116.9
- input_tokens: 213 | output_tokens: 1850

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

## 1. 5 Riesgos que un VC le tirará al “pitch”  
*(Preguntas que me harían en la sala de reuniones, sin filtrar)*

1. **Liquidez de la red**  
   - ¿Qué pasa si la mayoría de los restaurantes se quedan en “solo visualización” y no generan pedidos?  
   - ¿Cómo garantizas que haya suficientes proveedores activos para que el marketplace no sea una base de datos sin transacciones?

2. **Calidad y trazabilidad de los ingredientes**  
   - ¿Qué sucede si un proveedor entrega un lote contaminado o de calidad inconsistente?  
   - ¿Tienes un proceso de verificación de calidad y un mecanismo de reclamaciones rápido?

3. **Logística de entrega**  
   - ¿Quién entrega los ingredientes? ¿Tienes una red de mensajería propia o dependerás de terceros?  
   - ¿Cómo manejas la logística de tiempo crítico (p. ej., productos perecederos) en ciudades con infraestructuras de transporte pobres?

4. **Sostenibilidad de la comisión**  
   - ¿Qué tan rentable es una comisión del 15 % cuando la operación de un restaurante es tan frágil?  
   - ¿Cuál es el margen de beneficio que los restaurantes pueden absorber antes de buscar alternativas?

5. **Regulación y cumplimiento**  
   - ¿Estás al día con las regulaciones de manipulación de alimentos, impuestos de ventas y requisitos de importación/exportación locales?  
   - ¿Qué pasa si una jurisdicción impone restricciones de precios o de venta al por mayor por ley?

---

## 2. Por qué *podría* no funcionar en LATAM específicamente

1. **Fragmentación de la cadena de suministro**  
   - ¿Cómo vas a estandarizar los estándares de calidad a través de un territorio con tantos sistemas logísticos distintos?  

2. **Diferencias culturales y de negociación**  
   - En muchas comunidades la relación personal es la base de la trade, no una plataforma digital. ¿Cómo vas a romper esa barrera?  

3. **Problemas de infraestructura**  
   - ¿Qué tan fiable es la conectividad móvil y la entrega de pagos en zonas rurales donde los pequeños restaurantes están ubicados?  

4. **Regulación fiscal y de aduanas**  
   - LATAM tiene una compleja matriz de impuestos y aranceles que pueden afectar tanto a los proveedores como a los restaurantes. ¿Tienes un plan para automatizar el cumplimiento?  

5. **Competencia local y de mercado informal**  
   - ¿Qué diferencia competitiva tienes frente a los “agentes” tradicionales que ya operan en la zona? ¿Puedes ofrecer algo que la informalidad no tenga?

---

## 3. Key assumptions que deben ser verdad para que funcione

1. **Adopción masiva temprana**  
   - Suposición: Al menos el 30 % de los restaurantes pequeños en una ciudad objetivo usarán la app en los primeros 12 meses.  
   - **Prueba**: Encuestas de intención y pruebas piloto.

2. **Red de proveedores fiable**  
   - Suposición: Hay al menos 3‑5 proveedores locales que pueden cubrir la demanda de 70 % de los restaurantes en la zona.  
   - **Prueba**: Agreements de exclusividad o contratos de mínimo de volumen.

3. **Logística de entrega escalable**  
   - Suposición: La entrega puede realizarse en menos de 2 horas con un costo que no supere el 10 % del precio del pedido.  
   - **Prueba**: Piloto con un único proveedor logístico.

4. **Modelo de comisión sostenible**  
   - Suposición: Un 15 % de comisión cubre costos operativos y deja un margen de beneficio aceptable para la plataforma.  
   - **Prueba**: Análisis de flujo de caja con diferentes volúmenes.

5. **Cumplimiento regulatorio**  
   - Suposición: Se puede obtener todas las licencias y cumplir con la normativa en menos de 6 meses.  
   - **Prueba**: Asesoría legal y estudio de casos.

---

## 4. Escenario de fracaso rápido y por qué

1. **Falta de tráfico en la plataforma**  
   - Si tras 6 meses no hay más de 50 pedidos diarios, la comunidad de usuarios se vuelve inactiva. Los restaurantes no ven valor en usar algo que no se comercializa.

2. **Problemas de calidad repetidos**  
   - Un lote contaminado o entregado tarde puede generar una reputación negativa que se propaga de inmediato en redes sociales locales y en la comunidad de chefs.

3. **Competencia de mercado informal**  
   - Los “agentes” locales pueden ofrecer precios más bajos y entregas más rápidas. Si la app no puede competir en tiempo y costo, los usuarios migran de inmediato.

4. **Regulación inesperada**  
   - Una nueva ley que limite las comisiones de marketplaces o exija licencias de venta al por mayor para productos perecederos puede hacer que la operación sea ilegal o prohibitivamente costosa.

5. **Escasez de proveedores clave**  
   - Si un proveedor esencial se cierra o cambia a un modelo de venta directa a restaurantes, la oferta de la plataforma se reduce drásticamente y la demanda cae.

---

## 5. Con $10 K solo para validar, ¿qué harías?

1. **Validación de demanda con una sola ciudad**  
   - Compra una pequeña cantidad de ingredientes (≈$500) y envíalos a 10 restaurantes que ya no están en la app. Pregunta si estarían dispuestos a pagar una comisión del 15 % si la entrega fuera digital.

2. **Construye una landing page con mensajes claros**  
   - Usa los $4 K para crear una página de aterrizaje y un funnel de captura de emails. Luego envía un email a 200 restaurantes con un incentivo (p. ej., 10 % de descuento en el primer pedido) para que se registren.

3. **Realiza una prueba piloto de logística**  
   - Contrata a un mensajero local (≈$2 K) para entregar pedidos de 5 restaurantes. Mide el tiempo de entrega, el costo y la satisfacción del cliente.

4. **Entrevistas cualitativas con proveedores**  
   - Invierte $1 K en viajes y alimentación para visitar 3 proveedores locales. Pregunta sobre sus necesidades, su disposición a participar y su percepción de la comisión.

5. **Ajuste rápido del modelo de negocio**  
   - Con los resultados de las pruebas, decide si el 15 % es viable o si necesitas otro esquema de precios. Usa el resto de presupuesto para iterar la landing page y el pitch a inversores.

En resumen, con $10 K puedes probar la **demanda real**, la **capacidad logística** y la **disposición de los proveedores** sin lanzar la plataforma completa. Si algo de esto falla, sabrás que tu modelo de negocio necesita un rediseño antes de escalar.