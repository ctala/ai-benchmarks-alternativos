# Mistral Large 4.0 — business_strategy/plan_aritmetica_no_cierra

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 42.293s | tokens_per_second: 66.3
- input_tokens: 198 | output_tokens: 2803

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

No. **No le damos.** La multiplicación mata este plan antes de empezar.

Hagamos la autopsia con sus propios números:

| Paso | Cálculo | Resultado |
|------|---------|-----------|
| Visitas/mes | 200.000 | 200.000 |
| → Suscriptores (1,5%) | 200.000 × 0,015 | **3.000** |
| → Compradores (2%) | 3.000 × 0,02 | **60** |
| → Ingresos ($30) | 60 × $30 | **$1.800/mes** |

**Están en $1.800, no en $6.000.** Les faltan $4.200. Necesitan un factor de **×3,33** que no existe en ninguna parte del plan.

### El error de "los porcentajes son sanos"
1,5% y 2% suenan razonables por separado, pero **se multiplican, no se suman**:
- 1,5% × 2% = **0,03%** de conversión total de visita a venta.
- 200.000 × 0,0003 = 60 ventas.

Ese 0,03% es el número real del embudo, y con $30 de ticket da $1.800. La frase "llegamos cómodos" es la primera mentira: nunca es cómodo cuando la mate no cierra.

### El segundo problema: "recurrentes"
Dicen $6.000 **recurrentes**, pero venden un curso de $30 *one-time*. Eso no es recurrencia, es un ingreso puntual. Para que sean recurrentes necesitarían:
- Una suscripción mensual ($30/mes), o
- Vender a la misma lista mes tras mes (la conversión decae drásticamente con el tiempo; no es lineal).

Si el curso es único, esos $1.800 son de un solo mes, no un flujo mensual sostenido.

### ¿Qué necesitarían para llegar de verdad a $6.000/mes?
Con sus 200.000 visitas actuales, tienen estas palancas (elige una o combina):

1. **Más tráfico**: Necesitan 666.667 visitas/mes (×3,33). Difícil y caro.
2. **Mejor captura**: Subir a 5% de conversión a suscriptor → 10.000 suscriptores → 200 compradores (2%) → $6.000. El 5% es posible con un lead magnet fuerte, pero ya no es "conservador" para tráfico frío.
3. **Mayor conversión de venta**: Sobre los 3.000 suscriptores, necesitarían 6,67% de compra (200 ventas). Irreal para un curso de $30 en cold email.
4. **Ticket más alto**: Con 60 compradores, necesitarían vender a **$100** en vez de $30 (upsell, bundle, o curso premium).
5. **Modelo recurrente real**: Si cambian a suscripción de $30/mes, necesitan **200 suscriptores pagando cada mes**. Con 3.000 nuevos/mes y 2% de conversión a pago recurrente = 60 nuevos pagadores/mes. Sin churn, en el mes 4 ya tendrían 240 pagadores ($7.200/mes). **Pero con churn realista (5-10%/mes), recién en el mes 6-8 llegan a $6.000**, no antes.

### Veredicto
El plan como está escrito produce **$1.800/mes**, no $6.000, y no es recurrente. Aprobarlo sería quemar 6 meses persiguiendo un número que no existe en la hoja de cálculo.

**Rediseñen antes de ejecutar**: o suben el ticket a $100+, o cambian a modelo de suscripción y aceptan que los $6.000 llegan en el mes 6-8 por acumulación (no en el mes 1), o aumentan el tráfico ×3. Pero con $30 one-time y esos porcentajes, la mate dice que no.