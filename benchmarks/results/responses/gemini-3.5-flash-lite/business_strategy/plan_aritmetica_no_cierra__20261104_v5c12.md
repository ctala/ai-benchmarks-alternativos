# Gemini 3.5 Flash Lite — business_strategy/plan_aritmetica_no_cierra

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 2.994s | tokens_per_second: 175.3
- input_tokens: 197 | output_tokens: 525

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

**user:**

Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. ¿Lo aprobamos y lo ejecutamos?

PLAN:
1. Tenemos 200.000 visitas al mes en el sitio.
2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor del 1,5% (es un número conservador y realista para nuestro sector).
3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los suscriptores compra (también conservador).
4. Con eso llegamos cómodos a los $6.000/mes recurrentes.

Los porcentajes me parecen sanos y alcanzables. ¿Le damos?


## Respuesta completa

**Negativo. El plan muere en la multiplicación.** 

Guarda el entusiasmo, porque tu socio confundió "porcentaje razonable" con "realidad financiera". 

Vamos a abrir la hoja de cálculo y hacer la única pregunta que importa: **¿Los números dan?**

### La Auditoría del Embudo (Mes 6)

1. **Tráfico:** 200.000 visitas. (Ok, esto lo compramos).
2. **Conversión a Lead (1,5%):** 
   * 200.000 x 1,5% = **3.000 suscriptores nuevos al mes.**
3. **Conversión a Venta (2%):** 
   * 3.000 x 2% = **60 clientes al mes.**
4. **Facturación:** 
   * 60 clientes x $30 USD = **$1.800 USD.**

### El Veredicto
Tu socio calculó que llegaría a **$6.000 USD**, pero la matemática real del embudo arroja **$1.800 USD**. 

Te faltan **$4.200 USD** (un 70% del objetivo). Y eso sin contar la tasa de bajas si es un modelo de suscripción (recurentes), o el hecho de que en el mes 2 ya le habrás vendido a los más propensos y la conversión del 2% se va al piso.

### ¿Lo aprobamos?
**No se aprueba.** 

Si quieres llegar a los $6.000 con los mismos volúmenes y precios, tu socio tiene que corregir el plan con una de estas tres opciones (o una mezcla):
* **Opción A (Tráfico):** Necesitan triplicar las visitas a **600.000 al mes**.
* **Opción B (Conversión):** Subir la conversión del formulario al **5%** y la de venta al **4%** (lo cual es sumamente agresivo).
* **Opción C (Precio):** El curso no puede costar $30. Para facturar $6.000 con 60 ventas, el ticket debería ser de **$100 USD**.

Dile a tu socio que vuelva a la pizarra. Los porcentajes suenan bonitos, pero la multiplicación no perdona.