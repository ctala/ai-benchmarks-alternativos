# Gemini 3.6 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 10.857s | tokens_per_second: 185.0
- input_tokens: 197 | output_tokens: 2009

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

**NO. No lo apruebes.** 

El plan acaba de morir en la multiplicación. Si ejecutas esto tal cual, en 6 meses vas a estar estrellado contra la realidad y ganando menos de un tercio de lo que proyectaron.

Hagamos la matemática básica que tu socio no hizo:

### La corrida de números:

1. **Visitas al mes:** 200.000
2. **Captura (1,5%):** 3.000 nuevos suscriptores/mes.
3. **Venta del curso (2% de los suscriptores):** 60 compradores/mes.
4. **Ingreso por venta ($30 USD):** 60 × $30 = **$1.800 USD/mes.**

**Resultado real: $1.800 USD. Tu objetivo: $6.000 USD.**
El plan tiene un **déficit del 70%**. Te faltan $4.200 dólares todos los meses.

---

### Además de la matemática, hay 2 errores graves de concepto:

#### 1. El mito de la "recurrencia"
Mencionas "$6.000/mes **recurrentes**". 
Un curso de $30 suele ser un pago único, no un modelo de suscripción. Si vendes un curso, **no tienes ingresos recurrentes**. El mes 2 no empiezas con $1.800 acumulados; empiezas de cero y necesitas volver a conseguir 60 compradores nuevos. 

Si le vuelves a vender a la lista vieja, la conversión cae drásticamente porque los que querían comprar ya compraron.

#### 2. La ilusión de los porcentajes "conservadores"
Aunque un 1,5% de opt-in y un 2% de conversión a venta no son descabellados, asumir un 2% de conversión directa a *furgón frío* (gente que acaba de dejar su correo por un recurso gratuito y de inmediato te compra) suele requerir un embudo muy bien optimizado. Si la conversión real resulta ser del 1%, tus ingresos caen a **$900 USD/mes**.

---

### ¿Qué tendría que pasar para que la matemática SÍ dé $6.000/mes?

Para llegar a $6.000 USD con tus 200.000 visitas actuales, tu socio tiene que tocar una de estas palancas:

* **Opción A (Subir el precio):** Mantener las conversiones pero vender un producto/bundle de **$100 USD** (60 compradores × $100 = $6.000).
* **Opción B (Subir la conversión total):** Lograr **200 compradores al mes** (un 6,6% de conversión sobre los 3.000 suscriptores, o subir el opt-in del sitio al 5%).
* **Opción C (Modelo de Suscripción/Membresía):** Vender una membresía de $30/mes en lugar de un curso único, y acumular clientes activos controlando la cancelación (*churn*).

### Dictamen del Analista:
**Rechazado.** Devuélvele el plan a tu socio y pídele que recalcule la oferta o el precio. No ejecuten nada hasta que la hoja de cálculo dé $6.000 en el papel.