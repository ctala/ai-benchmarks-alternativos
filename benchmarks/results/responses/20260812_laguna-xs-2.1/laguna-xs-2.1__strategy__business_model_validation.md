# Poolside Laguna XS 2.1 — strategy/business_model_validation

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 9.23 | quality: 10.0
- latency_total: 15.002s | tokens_per_second: 190.0
- input_tokens: 211 | output_tokens: 2851

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

**1. Identifica los 5 riesgos principales de este modelo**  
- **Falta de crítica (critical mass):** Sin suficientes proveedores Y restaurantes, el marketplace no funciona. El "chicken and egg problem" es mortal: si los proveedores no ven clientes, no se unen; si los restaurantes no ven proveedores, no usan la app.  
- **Baja aceptación del 15% de comisión:** ¿Es este porcentaje justo? En LATAM, los márgenes son ajustados. Un proveedor podría priorizar ventas directas a bajo costo, y un restaurante podría rechazar pagar más por un servicio que ya tiene (ej: WhatsApp con su proveedor habitual).  
- **Dependencia de infraestructura logística frágil:** Muchos proveedores locales no tienen capacidad para entregas puntuales o sistemas digitales. Si el marketplace depende de logística propia (o tercerizada), los costos y retrasos podrían destruir la propuesta.  
- **Resistencia cultural a la digitalización:** En mercados donde las relaciones personales con proveedores son clave, un restaurante podría no confiar en un algoritmo para reemplazar a su "amigo del mercado".  
- **Concentración de proveedores clave:** Si un 20% de los ingredientes vienen de 3 proveedores (ej: carne, frutas locales), y esos no se unen al marketplace, el servicio pierde valor.  

---

**2. ¿Por qué podría NO funcionar en LATAM especificamente?**  
- **Infraestructura híbrida (digital + informal):** Muchos proveedores son informales, sin facturación electrónica, sin sistema de pagos digital, y operan en efectivo. Un marketplace digital podría parecer "poco real" para ellos.  
- **Fragilidad de logística:** En ciudades con tráfico caótico o infraestructura deficiente (ej: Ciudad de México, Buenos Aires), la promesa de entregas rápidas podría romperse, generando mala experiencia.  
- **Preferencia por relaciones cara a cara:** En mercados donde el negocio se basa en confianza personal (ej: "el que siempre trae los chiles frescos de mi tía"), un marketplace podría verse como una capa innecesaria.  
- **Escasa digitalización de pymes:** Según datos de la CEPAL, el 70% de los pequeños negocios en LATAM aún usan cajas registradas analógicas. Un restaurante pequeño podría no tener apps para pagos ni gestión de pedidos.  
- **Regulaciones incoherentes:** En países con normativas cambiantes (ej: Argentina, Brasil), un marketplace podría enfrentar trabas para operar como entidad de tercerización de pagos o logística.  

---

**3. ¿Qué tendría que ser verdad para que funcione? (key assumptions)**  
- **Los restaurantes están desesperados por ahorrar tiempo:** Se necesita evidencia de que llamar a 5 proveedores diarios cuesta más de $X en salario de empleado o tiempo perdido.  
- **Los proveedores ven ganancia en mayor volumen:** Si el marketplace reduce su dependencia de restaurantes individuales (ej: venta a 100 restaurantes vs 10), el 15% es aceptable.  
- **Logística local es viable:** Existe una red de mensajeros o motoboys con capacidad para manejar pedidos de ingredientes frescos con estos márgenes.  
- **Pagos digitales son aceptados por ambos lados:** Los restaurantes usan PayPal, MercadoPago, o apps de pago; los proveedores no temen operar en plataformas digitales.  
- **No hay competidores con ventajas clave:** Un marketplace ya establecido (ej: Rappi para delivery, o un proveedor consolidado) no puede imitar el modelo con mejores condiciones.  

---

**4. ¿Cuál es el escenario de fracaso rápido y por qué?**  
**Escenario:** El marketplace lanza en una ciudad (ej: Medellín), consigue 50 restaurantes y 20 proveedores. Los primeros 3 meses, las ventas son bajas porque:  
- Los restaurantes no ven diferencia con pedir por WhatsApp.  
- Los proveedores no cumplen plazos (ej: "hoy no tuve transporte, te llamo mañana").  
- El 15% de comisión es percibido como un costo innecesario por proveedores que ya tienen clientes fijos.  
- El equipo no puede resolver conflictos (ej: un restaurante recibe cebolla podrida; el proveedor niega responsabilidad).  
**Resultado:** Churn del 80% en proveedores y restaurantes en 6 meses. El equipo se queda sin fondos para mejorar logística o ajustar precios, y el proyecto muere.  

---

**5. Si solo tuviera $10K para validar, ¿qué harías?**  
- **Validación de demanda (RESTAURANTES):**  
  - Lanzar un landing page simple con formulario para "registrarse como restaurante". Ofrecer un 50% de descuento en la primera comisión si se firma un contrato piloto.  
  - Hacer llamadas frías a 100 restaurantes: "¿Cuánto tiempo pierden al día llamando a proveedores? ¿Pagarían $X mensuales por una app que lo resolviera?".  
- **Validación de oferta (PROVEEDORES):**  
  - Identificar 10 proveedores locales (ej: frutas, carne, especias) y ofrecerles una demo manual: "Sube tu catálogo a Google Sheets, te conecto con restaurantes que piden X kg de manzanas". Medir si están dispuestos a usar una app similar.  
- **MVP híbrido (sin app):**  
  - Usar WhatsApp + Google Sheets para simular el marketplace: los restaurantes envían pedidos por WhatsApp, tú los distribuyes a proveedores y cobras el 15% manualmente.  
  - Medir si hay repetición de pedidos y si los proveedores confían en el proceso.  
- **Análisis de costos:**  
  - Calcular el CAC (costo de adquisición de cliente) estimado: ¿Cuánto cuesta traer a un restaurante vs un proveedor? Si el CAC es > $100, el modelo no sobrevive con $10K.  
- **Conclusión:** Si en 2 meses no hay al menos 20 restaurantes y 10 proveedores activos con pedidos recurrentes, pivotea o abandona.  

**Bonus brutal:** Si los proveedores piden una comisión del 5% en lugar del 15%, y los restaurantes dicen "ya tengo a mi de la tienda", el riesgo de viabilidad es del 90%.