# GLM 5.3 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 108.671s | tokens_per_second: 42.9
- input_tokens: 212 | output_tokens: 4659

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

**No. El plan llega a $1.800/mes, no a $6.000. Queda 70% corto.**

Dónde muere, exactamente en la multiplicación:

- 200.000 visitas × 1,5% = 3.000 suscriptores/mes ✓ (ese número sí es razonable)
- 3.000 suscriptores × 2% = **60 ventas/mes**
- 60 × $30 = **$1.800/mes**

Tu intuición de que los porcentajes "son sanos" es correcta **en aislado**. El problema es el producto de los dos: 1,5% × 2% = 0,03% de las visitas termina en venta. Para $6.000 con ticket de $30 necesitás 200 ventas/mes, o sea 0,1% de punta a punta: **triplicar la conversión combinada**. Los planes casi nunca mueren en un supuesto; mueren en el producto de los supuestos.

**Dos agujeros estructurales además de la aritmética:**

1. **Nada de esto es recurrente.** Un curso de $30 es compra única. Ni siquiera los $1.800 son MRR: cada mes arrancás de cero y dependés de suscriptores nuevos; los del mes 1 no recompran en el mes 2. Y si tu socio está pensando "2% de la lista acumulada compra cada mes", está asumiendo que el que no compró en 5 campañas sí compra en la sexta.
2. **El ramp-up.** $1.800 es el techo con el embudo maduro. Los meses 1-2 la conversión a compra será menor (falta secuencia de nutrición, confianza, lanzamientos). El objetivo de "mes 6" está aún más lejos de lo que muestra la cuenta.

**Cómo sí cierra a $6.000/mes** (necesitás 200 ventas o su equivalente en valor):

| Palanca | Cambio | Resultado |
|---|---|---|
| **Precio** | Curso de $100 en vez de $30 | 60 × $100 = $6.000 ✓ mismo embudo, cero supuestos nuevos |
| **Ticket promedio** | $30 + order bump/upsell que lleve el AOV a ~$100 | $6.000 ✓ |
| **Conversión a suscriptor** | 5% en vez de 1,5% | 10.000 subs × 2% × $30 = $6.000 (posible, pero ya no es "conservador") |
| **Producto recurrente real** | Membresía ~$12/mes | Necesitás ~500 miembros activos; con 3.000 subs/mes es alcanzable hacia el mes 5-6 si la retención acompaña |

Subir el precio puede bajar la conversión, hay que testearlo — pero es el camino con menos supuestos nuevos.

**Mi recomendación:** no aprobarlo como está. Aprobarlo con dos condiciones:

1. Cerrar la multiplicación primero: definir precio, AOV o producto recurrente para que la cuenta dé $6.000 sobre el papel *antes* de invertir un mes de ejecución.
2. Validar con datos reales en 30-60 días: conversión real del formulario y tasa de compra real sobre los primeros 3.000-6.000 suscriptores. Si en el mes 2 tenés $1.800, ya sabés qué palanca mover en vez de descubrirlo en el mes 6.

Una pregunta antes de dar el visto bueno: ¿el $30 es fijo o hay margen para precio/upsells? Con esa respuesta te armo la versión que sí llega.