# Claude Opus 5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.03 | quality: 10.0
- latency_total: 46.717s | tokens_per_second: 61.9
- input_tokens: 318 | output_tokens: 2892

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

## Veredicto corto

No. El plan no falla por optimismo en los porcentajes — falla en la multiplicación. Con **sus propios números**, el resultado es $1.800/mes, no $6.000.

## La cadena, calculada

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas | — | 200.000 |
| Suscriptores (1,5%) | 200.000 × 0,015 | 3.000 |
| Compradores (2%) | 3.000 × 0,02 | 60 |
| Ingreso | 60 × $30 | **$1.800** |

**$1.800 vs. $6.000 = 30% del objetivo. Falta $4.200/mes.**

Y eso es bruto. Descontando comisión de pasarela (~4%) y devoluciones (~5%), el neto real ronda **$1.630**. Es el 27% del objetivo.

## El tamaño del hueco: 3,3x

Para llegar a $6.000 hacen falta **200 ventas/mes** en lugar de 60. No es un ajuste, es triplicar la cadena entera.

Vías, cada una en solitario:

- **Captura**: pasar de 1,5% a **5%** (3.000 → 10.000 subs/mes)
- **Conversión**: pasar de 2% a **6,7%**
- **Precio**: pasar de $30 a **$100**
- **Tráfico**: pasar de 200k a **660k visitas/mes**

Ninguna es realista por separado. La única vía viable es combinada, y ahí la aritmética es amable: **1,5x en cada palanca ≈ 3,4x total**. Ejemplo: 3% de captura × 3% de compra × $35 = 6.000 subs → 180 ventas → **$6.300**. Eso sí es un plan discutible. Pero es un plan *distinto* al que te trajo tu socio.

## Dos problemas que la tabla no muestra

**1. "$6.000 recurrentes" no existe en este plan.** Un curso de $30 es pago único. Cada mes empezás de cero dependiendo de tráfico nuevo. No hay recurrencia, hay repetición — y es frágil: si el tráfico cae 20%, el ingreso cae 20% el mismo mes.

**2. La lista se quema.** El 2% aplica a suscriptores que aún no compraron. El mes 1, si lanzás sobre una lista acumulada, vas a ver un pico que parecerá validar el plan. Los meses 2 a 6 solo tenés los 3.000 nuevos, y el resto de la lista ya vio la oferta y dijo no. **El pico inicial va a ser malinterpretado como tendencia.** Anticipalo antes de que pase.

## Qué haría antes de aprobar nada

Las dos incógnitas grandes son baratas de medir. No hace falta construir el plan completo para saber si el plan sirve:

1. **Test de captura, 2 semanas.** Formulario en las 5 páginas de más tráfico. ¿El 1,5% es real o es 0,6%? Esto solo cuesta poner un formulario. Si sale 0,6%, todo lo demás es irrelevante.
2. **Preventa a un segmento chico, 1 semana.** Tomá 500 suscriptores existentes (o los primeros que capture el test) y ofreceles el curso. ¿Compra el 2%? Con 500 personas, 10 ventas confirman y 1 venta te ahorra seis meses.
3. **Test de precio en la misma preventa.** Mitad a $30, mitad a $60. Si la conversión no se cae a la mitad, el precio estaba mal puesto — y el precio es la palanca más rápida de las cuatro.

**Regla de decisión:** si captura ≥3% y compra ≥3% en los tests, se reformula el plan con los números reales y se aprueba. Si sale por debajo, $6.000 en 6 meses con este tráfico y este producto no está sobre la mesa, y hay que cambiar el producto (algo con precio de $100+ o con cobro mensual real), no los porcentajes.

## Lo que le diría a tu socio

Sus porcentajes son defendibles. El problema no es que sean optimistas — es que nadie multiplicó la cadena hasta el final antes de escribir "llegamos cómodos". Dos porcentajes conservadores multiplicados dan un número muy chico: 1,5% × 2% = 0,03% de las visitas. 60 personas de 200.000.

Aprobar esto ahora significa descubrir en el mes 4 que vas al 30% del objetivo, con el equipo ya comprometido y el pico del mes 1 usado como argumento de que "está por arrancar".