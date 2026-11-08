# Tencent Hy4 — business_strategy/plan_aritmetica_no_cierra

- model_id: `tencent/hy4`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 36.663s | tokens_per_second: 89.5
- input_tokens: 231 | output_tokens: 3283

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

**Veredicto: no. No lo aprobamos ni lo ejecutamos todavía.**

Tu intuición sobre los porcentajes probablemente es correcta: 1,5% de captura y 2% de conversión son números sanos. El problema no está en los rates, está en que nadie los llevó hasta el dólar.

### La multiplicación

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas/mes | — | 200.000 |
| Suscriptores | × 1,5% | 3.000 |
| Compradores | × 2% | 60 |
| Ingreso | × $30 | **$1.800/mes** |

Objetivo: **$6.000**. Están en el **30%**. Faltan $4.200, o lo que es lo mismo, **3,33x**. "Cómodos" es justo lo contrario de lo que dice la cuenta.

La métrica que lo resume todo: **$0,009 de ingreso por visita** (0,015 × 0,02 × 30). Con 200.000 visitas, para facturar $6.000 necesitás **$0,03 por visita**. Toda la discusión debería ser sobre ese número, no sobre si el 1,5% es conservador.

### Dos grietas más en el plan

**1. "Recurrentes" no es recurrente.** Un curso de $30 es pago único. Cada cohorte de 3.000 suscriptores compra una vez y ahí termina. Que la lista crezca mes a mes no genera MRR por sí solo: genera $1.800 por cohorte. Si la idea era acumulación, falta modelar suscripción, recompra o upsell —y churn—. Tal como está escrito, el modelo de ingresos es incorrecto además de insuficiente.

**2. "En 6 meses" no tiene rampa.** El plan es una foto estática. Sin crecimiento de tráfico ni mejora de conversión, el mes 6 es idéntico al mes 1: $1.800. Llegar a $6.000 en el mes 6 exige ~22% compuesto mensual de ingreso por visita, y el documento no dice de dónde sale ese crecimiento.

### Qué sí cerraría el número (manteniendo 200.000 visitas)

- Precio **$100** → 60 × 100 = $6.000
- Conversión suscriptor→compra **6,67%** → $6.000
- Captura **5%** → 10.000 × 2% × $30 = $6.000
- O, con los rates actuales, **~667.000 visitas/mes**

Aviso importante: esas palancas **no son independientes**. Subir de $30 a $100 casi seguro deprime el 2%; triplicar el tráfico normalmente deteriora la captura. Un plan que mueve tres variables a la vez sin testear no es un plan, es un deseo.

### Aprobación condicionada

Pedile a tu socio que vuelva con cuatro cosas:

1. El modelo explícito hasta el dólar, con el **ingreso por visita** como métrica de control.
2. Definición clara: ¿pago único por cohorte o ingreso realmente recurrente?
3. **Una o dos** palancas a testear, con impacto esperado y riesgo sobre las otras variables.
4. Rampa mes a mes hasta el mes 6, no una foto del mes 1.

Mi apuesta: la palanca más barata no es el tráfico (3,3x es caro), es precio u oferta. Pero eso se prueba, no se asume.

Con esos cuatro puntos, se aprueba y se ejecuta. Con el plan actual, se aprueba un déficit de $4.200 mensuales.