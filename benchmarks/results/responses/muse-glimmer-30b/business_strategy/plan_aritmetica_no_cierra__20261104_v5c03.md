# Muse Glimmer 30B — business_strategy/plan_aritmetica_no_cierra

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 11.306s | tokens_per_second: 140.6
- input_tokens: 213 | output_tokens: 1590

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

No. Los números no llegan y además no son recurrentes.

Tu fórmula es: **Visitas x CR opt-in x CR compra x Precio = Ingresos**

Con los números que pusiste:

* Visitas: 200.000 / mes
* Suscriptores nuevos: 200.000 x 1,5% = **3.000 suscriptores / mes**
* Compras: 3.000 x 2% = **60 compras / mes**
* Ingresos: 60 x $30 = **$1.800 / mes**

Estás en $1.800, no en $6.000. Te faltan 3,33x.

Y no es recurrente. Un curso de $30 es ingreso one-time. Para que sea recurrente necesitarías una suscripción o un LTV repetido.

### ¿Qué necesitarías realmente para $6.000/mes con esos supuestos?

Necesitas 200 compras al mes porque 200 x $30 = $6.000

Con 2% de compra necesitas: 200 / 0,02 = **10.000 suscriptores nuevos por mes**

Con 200k visitas necesitas un CR opt-in de: 10.000 / 200.000 = **5%**

O con 1,5% de opt-in necesitas: 10.000 / 0,015 = **666.667 visitas / mes**

### Opciones realistas para cerrar la brecha

No tienes que hacer todo a la vez, elige 1-2 palancas:

1. **Subir el precio / LTV.** Con 60 compras actuales necesitas $100 por compra para llegar a $6.000. Curso de $30 -> $100 o un upsell de $70.
2. **Mejorar la compra en lista.** 60 compras -> 200 compras con los mismos 3.000 suscriptores = 6,67% de compra. Necesitas un embudo de ventas real, no un email único.
3. **Mejorar captación.** 1,5% -> 5% de opt-in con lead magnet más fuerte, pop-ups bien segmentados y tráfico cualificado.
4. **Aumentar tráfico.** De 200k a ~667k visitas/mes.

La más rápida es combinar precio + conversión de lista. Con 3.000 suscriptores/mes y un CR de compra del 4% ya estarías en $3.600/mes. Añade un upsell y llegas.

Si quieres que el $6k sea realmente recurrente, necesitas un modelo de suscripción. Con 200k visitas, 1,5% opt-in y 2% de compra a $30, tendrías que vender una suscripción de $6k / 60 = $100/mes por cliente.

**Veredicto:** No ejecutes el plan tal cual. Haz un test de 2-4 semanas con los números reales de opt-in y compra antes de escalar. Con los datos actuales el plan llega a $1.800/mes one-time, no a $6.000/mes recurrentes.