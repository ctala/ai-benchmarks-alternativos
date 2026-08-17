# Claude Opus 5 (suscripción) — business_strategy/plan_aritmetica_no_cierra

- model_id: `claude-opus-5`
- success: True  | final: 7.94 | quality: 10.0
- latency_total: 81.785s | tokens_per_second: 57.5
- input_tokens: 2 | output_tokens: 4705

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

## No. El plan no llega a $6.000. Llega a $1.800.

Antes de discutir si los porcentajes son sanos, hay que multiplicarlos:

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas | — | 200.000/mes |
| Captura 1,5% | 200.000 × 0,015 | **3.000 suscriptores/mes** |
| Compra 2% | 3.000 × 0,02 | **60 compradores/mes** |
| Ticket $30 | 60 × $30 | **$1.800/mes** |

Falta 3,3x. No es un ajuste fino, es un plan distinto.

---

## Tres problemas, en orden de gravedad

**1. La aritmética.** Ninguno de los dos porcentajes es el problema por separado; el problema es que se multiplican. Es el error más común: cada supuesto suena razonable aislado y el producto de todos queda a un tercio del objetivo. Un plan de embudo se aprueba o se rechaza en la multiplicación, no en la lectura de cada línea.

**2. "Recurrentes" no aplica.** Un curso de $30 se vende una vez a cada persona. Ese $1.800 no es MRR: es la facturación de una cohorte nueva de 3.000 suscriptores, y hay que reconstruirla íntegra el mes siguiente. Si el tráfico cae, la cifra cae el mismo mes. Si en el mes 6 tienes 18.000 suscriptores acumulados, no puedes venderle el mismo curso otra vez a los 15.000 que ya lo vieron. El 2% es una conversión de cohorte, no una tasa mensual sobre la lista total.

**3. Los porcentajes no son conservadores. Son de buena ejecución.** Un formulario genérico en footer captura 0,3%–0,8% del tráfico; el 1,5% exige lead magnet real, ubicación inline y exit intent. Y el 2% de compra corresponde a una lista cálida y trabajada, no a alguien que se suscribió hace tres días y recibe una oferta.

Mira la sensibilidad, que es lo que asusta:

- Escenario del plan: 1,5% × 2% → **$1.800**
- Escenario realista de primera versión: 0,8% × 1% → **$480**

Entre el caso planteado y un caso perfectamente posible hay 12x de diferencia. Con márgenes así, comprometer 6 meses a estimaciones es apostar, no planificar.

---

## Qué tendría que ser cierto para llegar a $6.000

Solo hay cuatro palancas. Tres son fantasía a 6 meses y una es viable:

- **Más tráfico:** necesitas 666.000 visitas/mes. Triplicar en 6 meses, descartado.
- **Mejores tasas:** necesitas 3,3x combinado — por ejemplo captura 2,5% *y* compra 4%. El 4% en lista fría es decil superior. Descartado como plan base.
- **Más ticket (viable):** $6.000 ÷ 60 compradores = **$100 de ticket promedio**. No se logra subiendo el curso a $100; se logra con escalera. Ejemplo: 60 compras a $30 ($1.800) + order bump de $200 que toma el 25% ($3.000) + oferta de $500 que toma el 3% ($900) = **$5.700**. Ahí sí aparece el número, con el mismo tráfico y las mismas tasas.
- **Recurrencia real (viable, más lento):** membresía de $30/mes. Necesitas ~200 miembros activos. Pero la conversión a suscripción recurrente es la mitad o un tercio que a un pago único: cuenta 0,5%–1%, no 2%. Con 1% son 30 altas/mes, y con 8% de churn llegas cerca de $4.600 en el mes 6, no a $6.000. Es un buen negocio; no cumple el plazo.

---

## Lo que yo aprobaría en vez de esto

No 6 meses de ejecución sobre estimaciones. **3 semanas para reemplazar las dos estimaciones por dos números medidos:**

1. Semana 1: formulario arriba. Con ~50.000 visitas ya sabes tu tasa de captura real, no la del sector.
2. Semanas 2–3: le vendes el curso a esa primera cohorte. Si la captura real fue 1,5%, son 750 suscriptores; al 2% son 15 compradores. Muestra chica, pero suficiente para distinguir un 2% de un 0,5%, que es la decisión que importa.
3. Con esos dos números reales, rehaces la multiplicación y recién ahí defines objetivo y producto.

Y dos preguntas que pueden invalidar el número base antes de todo esto: **¿las 200.000 son sesiones o pageviews?** Y **¿ese tráfico tiene relación con el tema del curso?** 200.000 visitas que llegan por otra intención convierten a una fracción de lo estimado, y ese sería un cuarto multiplicador escondido.

El activo es bueno: 200.000 visitas propias es más de lo que tiene la mayoría. El modelo de monetización es el que está mal calibrado. Arregla el ticket, no el optimismo.