# Claude Fable 5.1 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 24.259s | tokens_per_second: 61.5
- input_tokens: 320 | output_tokens: 1492

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

**No. El plan se cae en el paso 4, que es justamente el único que no tiene número.**

Hagamos la multiplicación que el plan omite:

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas | — | 200.000/mes |
| Suscriptores | 200.000 × 1,5% | **3.000/mes** |
| Compradores | 3.000 × 2% | **60/mes** |
| Ingreso | 60 × $30 | **$1.800/mes** |

Objetivo: $6.000. Resultado: $1.800. **Llegan al 30%.** No es "cómodo", es un faltante de 3,3x.

Y ojo a dos cosas más:

**1. Los porcentajes están bien; el problema es que los porcentajes sanos multiplicados entre sí dan números chicos.** 1,5% × 2% = 0,03% del tráfico compra. Tres de cada diez mil visitantes. Con un ticket de $30 eso no da para $6.000 ni cerca. El plan no falla por optimista, falla por nunca haber hecho la cuenta.

**2. "Recurrentes" no es recurrente.** Un curso de $30 se vende una vez por persona. Los $1.800 se sostienen solo mientras entren 3.000 suscriptores nuevos cada mes. No hay ingreso que se acumule. Si el tráfico baja, baja el ingreso ese mismo mes.

**Qué tendría que cambiar para que cierre** (necesitan 200 ventas/mes, no 60):

- **Precio a $100** → 60 × $100 = $6.000. Justo, sin margen. ¿El curso aguanta ese precio?
- **Conversión a compra de ~6,7%** en vez de 2% → tendrían que triplicar la tasa que ustedes mismos llaman "conservadora". Poco creíble.
- **Captura al 5%** en vez de 1,5% → 10.000 suscriptores/mes. Posible con un lead magnet fuerte, pero ya no es "conservador".
- **Combinar**: captura 2,5% + precio $50 → 5.000 × 2% × $50 = $5.000. Casi.
- **Agregar algo realmente recurrente** (membresía, upsell) a los 60 compradores/mes, para que la lista acumulada (18.000 personas al mes 6) genere algo más que una venta única.

**Mi recomendación:** no aprueben el plan como está. Pídanle a tu socio que lo reescriba con la tabla de arriba incluida y que el paso 4 diga cuántas ventas necesita y de dónde salen. Si después de eso llega a $6.000 con supuestos que ambos aceptan, ejecuten. Hoy no llega.