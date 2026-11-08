# Tencent Hy4 preview — strategy/business_model_validation

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 72.356s | tokens_per_second: 50.0
- input_tokens: 206 | output_tokens: 3615

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

Mira, voy a ser directo contigo porque ya he visto este pitch mil veces. El "Uber de los ingredientes" o el "Marketplace B2B de comida" es un cementerio de startups. Suena bonito en un pitch deck, pero en la vida real es una trampa mortal de márgenes, logística y traiciones. 

Tu hipótesis de que "pierden tiempo llamando" es una verdad a medias. En LATAM, el restaurante pequeño *ama* su rutina de compra. Es su momento de control y, a menudo, su momento de negocios turbios.

Si te presentas en mi fondo, esto es lo que te voy a decir y las preguntas que te van a hacer sudar frío:

### 1. Identifica los 5 riesgos principales de este modelo

*   **El riesgo de la Desintermediación (Leaking):** Este es el asesino #1. Los márgenes en comida son de risa (un proveedor netea 5-10% si le va bien). Cobrarles un 15% de comisión es sacarles la sangre. En la orden #1 se conocen. En la orden #2, el restaurante le manda un WhatsApp directo al proveedor: *"Oye, saltémonos la app, te pago en efectivo y me haces 10% de descuento"*. Proveedor feliz, restaurante feliz, tú muerto.
*   **Logística y Cumplimiento (El aguacate podrido):** ¿Quién entrega? Si entrega el proveedor, pierdes el control de calidad. Si el restaurante pide 10kg de tomate y llegan podridos o tarde, ¿a quién le reclama? A ti. Tu plataforma carga con la culpa de los errores de terceros.
*   **Márgenes y Unit Economics:** Un 15% de *take rate* en alimentos es una locura a menos que el ticket promedio (AOV) sea altísimo y la frecuencia diaria. Si el ticket es de $100 USD, tú ganas $15. ¿Cuánto te cuesta adquirir ese restaurante (CAC)? Si es más de $50, estás regalando dinero.
*   **Mantenimiento del Catálogo:** El precio de la cebolla y el pollo cambia todos los días. La disponibilidad cambia por clima o bloqueos. Mantener un catálogo digital actualizado en tiempo real es una pesadilla operativa que te va a costar una fortuna en soporte.
*   **Capital de Trabajo (Working Capital):** El proveedor quiere que le pagues hoy (cash). El restaurante quiere pagar a 15 o 30 días (crédito). Si tú no financias ese hueco (factoraje), la transacción no ocurre. Si lo financias, te quedas sin caja en 3 meses.

### 2. ¿Por qué podría NO funcionar en LATAM específicamente?

*   **La "Mordida" (Corrupción a pequeña escala):** El chef o el encargado de compras del restaurante pequeño en LATAM frecuentemente recibe un sobrecito, una caja de cerveza o un porcentaje por debajo de la mesa del proveedor actual. Tú llegas con tu app transparente a destruir su ingreso extra. Te van a sabotear desde adentro.
*   **La cultura del WhatsApp y la Confianza:** El restaurante pequeño no "pierde tiempo llamando". Le manda un audio de WhatsApp a "Don Juan", que le fía, le guarda la mejor carne y le resuelve si un día no tiene efectivo. Tú no estás compitiendo contra un catálogo, estás compitiendo contra una relación de 10 años.
*   **La sensibilidad al precio:** En LATAM, si el tomate sube 2 pesos, el dueño del restaurante pone el grito en el cielo. Un 15% de comisión encarece el producto final. El restaurante no lo absorberá de su margen, se lo pasará al cliente final, perderá ventas y te culpará a ti.

### 3. ¿Qué tendría que ser verdad para que funcione? (Key Assumptions)

Para que yo siquiera considere sacar la chequera, tienes que probarme que:
*   **Tu 15% no duele:** La única forma de cobrar 15% es si traes un valor agregado brutal. Ejemplo: Tú les das financiamiento (compras hoy, pagas a 30 días sin intereses) o garantizas devoluciones inmediatas sin preguntas.
*   **Efecto "One-Stop-Shop":** El restaurante *odia* pedirle a 5 proveedores. Tienes que probar que tu plataforma consolida el 80% de su compra en un solo clic y una sola entrega. Si solo les resuelves las verduras, no les sirves.
*   **El volumen justifica el riesgo:** Los restaurantes pequeños son un dolor de cabeza (quiebran rápido, pagan tarde). Lo que tiene que ser verdad es que hay suficiente densidad en una misma zona para que una sola ruta de entrega (tuya) sea hiper-rentable.

### 4. ¿Cuál es el escenario donde fracasas rápido y por qué?

Fracasas en el mes 6. 
Invierte $200K en una app hermosa. Consigues 100 restaurantes en una colonia de moda (ej. Roma/Condesa en CDMX o Palermo en BsAs). Haces la primera semana de pedidos. El proveedor llega tarde, le cambia un producto al restaurante sin avisar. El restaurante se queja contigo. Tú le devuelves el dinero para apagar el fuego (quemando tu caja). 
A la semana siguiente, el 30% de tus restaurantes ya no piden por la app. Investigas y descubres que se pusieron de acuerdo con el proveedor por WhatsApp. Tu LTV (Lifetime Value) es de 1 sola orden. Tu CAC (Costo de Adquisición) fue altísimo. Mueres de una hemorragia de efectivo antes de llegar a la Serie A.

### 5. Si solo tuviera $10K para validar, ¿qué harías?

Con $10K no me dejaría ver ni en pintura escribiendo código. **No construyas una app.**

1.  **Elige una zona híper-pequeña:** Una colonia, 10 cuadras a la redonda.
2.  **Elige 2 categorías de alta frecuencia:** Pollo y verduras (o lo que más se mueva ahí).
3.  **Haz "Concierge MVP" (Manual):** Consigue 10 restaurantes y 3 proveedores. Toma los pedidos por un grupo de WhatsApp o un Google Form.
4.  **Haz tú el trabajo sucio:** Tú llamas a los proveedores, tú rentas una moto o un Uber Flash para consolidar y entregar tú mismo. Tú cobras en efectivo o transferencia.
5.  **Mide lo que importa:** 
    *   ¿Aceptan pagar el precio con tu 15% de markup? 
    *   ¿Vuelven a pedirte a la semana siguiente? 
    *   ¿Intentan pasarse de listos y contactar al proveedor directamente?

Si en 4 semanas no logras que 5 de esos 10 restaurantes te compren a ti (con tu sobreprecio del 15%) al menos 3 veces por semana, **mata la idea**. Si lo logras, entonces tal vez, y solo tal vez, tengas el derecho de escribir tu primera línea de código. 

Ahora dime, ¿cómo piensas evitar que se salten tu plataforma en la segunda orden?