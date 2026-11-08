# MiMo V2.6 Pro — business_strategy/plan_aritmetica_no_cierra

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 33.463s | tokens_per_second: 31.1
- input_tokens: 226 | output_tokens: 1042

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

## No. El plan no llega. Se cae en la multiplicación.

Hagamos la cuenta exacta que tu socio no hizo:

| Paso | Operación | Resultado |
|---|---|---|
| Visitas | 200.000 | — |
| → Suscriptores (1,5%) | 200.000 × 0,015 | **3.000 suscriptores/mes** |
| → Compradores (2%) | 3.000 × 0,02 | **60 compradores/mes** |
| → Ingresos | 60 × $30 | **$1.800/mes** |

### La brecha: $1.800 vs $6.000 → falta el **70%** del objetivo.

No es un redondeo ni un margen de error. El plan genera **menos de un tercio** de lo prometido.

---

### Por qué "los porcentajes conservadores" engañan

Tu socio hizo la trampa clásica: etiquetó cada tasa suelta como "conservadora y realista", pero **nunca multiplicó los tres números juntos**. Tres tasas de 98,5% / 98% / 98% parecen gigantes; multiplicadas dan el 94,7%. Al revés: tasas chicas que parecen inocentes se devoran entre sí. 1,5% × 2% = **3%**. Solo 3 de cada 100 visitantes pagan. Ese es el número real, y el 97% restante lo ocultan los decimales.

---

### Problema adicional: "recurso recurrente"

Un curso de $30 que se compra **una vez** no es ingreso recurrente. Ese $1.800 es *inicial*. El mes 2 no es $1.800 + $1.800, es ~$1.800 (quizás algo más si el tráfico crece, o menos si la audiencia se satura).

---

### ¿Cuánto tráfico necesitarías para los $6.000?

```
$6.000 ÷ $30 = 200 compradores/mes
200 ÷ 2%     = 10.000 suscriptores/mes
10.000 ÷ 1,5% = 666.667 visitas/mes
```

**Necesitás 666.667 visitas/mes.** Tenés 200.000. Hace falta **3,3× más tráfico** que el plan da por sentado que ya existe.

---

### Veredicto

❌ **No aprobar como está.** Las tasas pueden ser realistas, pero el resultado no es $6.000 — es $1.800. El objetivo y el plan no se tocan.

### Rutas para cerrar la brecha (combinar varias):

1. **Más tráfico** → llegar a ~667K visitas/mes (difícil en 6 meses).
2. **Producto más caro** → un curso de $100 en vez de $30 triplica la factura.
3. **Más productos / suscripción** → vender upsells, mentorías, membresía.
4. **Mejorar la tasa de compra** → email nurturing largo, 2% → 5% con una secuencia fuerte (3.000 × 5% × $30 = $4.500, ya más cerca).
5. **Mejorar la captura** → 1,5% → 3% con lead magnet potente (dobla todo lo demás).

Ninguna de estas está en el plan actual. **Pedile a tu socio que rehaga las cuentas con un número final, no solo con porcentajes verosímiles.** Un plan con tasas verosímiles que suma mal sigue siendo un plan malo.