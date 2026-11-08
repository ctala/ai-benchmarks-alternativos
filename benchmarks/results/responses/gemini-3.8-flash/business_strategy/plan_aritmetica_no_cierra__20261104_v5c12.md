# Gemini 3.8 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.65 | quality: 10.0
- latency_total: 11.972s | tokens_per_second: 144.7
- input_tokens: 197 | output_tokens: 1732

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

**No lo aprueben.** El plan muere en la multiplicación más básica.

Hagamos los números paso a paso:

1. **Visitas:** 200.000/mes
2. **Nuevos suscriptores (1,5%):** 3.000 leads/mes
3. **Compradores (2%):** 60 clientes/mes
4. **Facturación mensual:** 60 clientes × $30 USD = **$1.800 USD/mes**

Están a **$4.200 USD de distancia** del objetivo (un 70% por debajo).

---

### Además, hay una trampa de concepto: "Recurrente"
Un curso de $30 se paga **una sola vez**. 
* Para que esos $1.800 fueran "recurrentes" mes a mes, tendrías que conseguir 60 compradores *nuevos* todos los meses al infinito (lo cual depende de mantener el tráfico constante).
* Si lo que tu socio llama "recurrente" es que la lista se acumula, la realidad del email marketing es que la intención de compra decae drásticamente después de los primeros 14-30 días. No le vas a vender el mismo curso de $30 dos veces al mismo usuario.

---

### ¿Qué tendría que pasar para que la matemática dé $6.000 USD/mes?

Para cerrar la brecha de $4.200 con el tráfico que ya tienen, necesitan mover al menos una de estas palancas:

1. **Subir el ticket (la vía más realista):**
   * Con los mismos 60 compradores al mes, necesitan un ticket promedio de **$100 USD** (o un curso de $30 con un *order bump* y un *upsell* que eleven el promedio a $100).
2. **Subir drásticamente la conversión de compra:**
   * Pasar del 2% al **6,67%** (venderle a 200 personas de las 3.000). Muy difícil para tráfico frío en un primer embudo.
3. **Subir la captura:**
   * Pasar del 1,5% al **5%** de opt-in (10.000 suscriptores/mes). Al 2% de compra = 200 ventas × $30 = $6.000. Factible si ofrecen un imán de prospectos (*lead magnet*) extraordinario, pero agresivo para arrancar.

**Veredicto:** Rechaza la propuesta actual. Pídele a tu socio que recalcule el embudo apuntando a un **ticket promedio de $100** o introduciendo un producto backend/recurrente real antes de tirar una sola línea de código o redactar un email.