# Claude Haiku 5.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 12.486s | tokens_per_second: 173.2
- input_tokens: 320 | output_tokens: 2163

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

**No lo aprobaría tal como está.** Con sus propios porcentajes, el plan llega a unos **$1.800/mes**, no a $6.000.

## Los números

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas | 200.000/mes | 200.000 |
| Suscriptores nuevos | 200.000 × 1,5% | **3.000/mes** |
| Compradores | 3.000 × 2% | **60/mes** |
| Ingreso | 60 × $30 | **$1.800/mes** |

Faltan **$4.200/mes**, es decir, están al 30% del objetivo.

## Hay tres problemas

1. **Aritmética:** El plan no cierra. Para $6.000/mes con esos porcentajes necesitarían unos **10.000 suscriptores nuevos al mes**, o sea ~667.000 visitas (3,3 veces el tráfico actual).

2. **"Recurrente" no es recurrente:** Un curso de $30 es una compra única. Cada suscriptor compra una vez, así que el ingreso no se acumula mes a mes como un MRR. Si la lista crece 3.000 por mes, a los 6 meses tendrían unos 18.000 suscriptores y unos 360 compradores en total, unos **$10.800 acumulados** en medio año, no $6.000 por mes.

3. **"Conservador" no es el término correcto:** Un 2% de compra sobre una lista fría para un producto de $30 es un supuesto optimista hasta que lo midan. No está validado. Tampoco sabemos si las 200.000 visitas son únicas o sesiones, ni si el 1,5% de captura sale de tráfico frío o de un público ya calificado. Son supuestos, no datos.

## Qué haría antes de aprobar

**Opción A: cambiar la matemática del producto**
- Subir el precio: con 60 compradores/mes, a **$100** se llega a $6.000. Eso exige probar disposición a pagar, no asumirla.
- Crear un producto realmente recurrente (membresía o suscripción): a $20/mes necesitan **300 miembros pagos** activos, lo que implica retención y no solo ventas.

**Opción B: validar antes de comprometer recursos (2 a 4 semanas)**
- Medir la tasa real de captura en una landing con tráfico pagado o orgánico real.
- Hacer una preventa del curso a una muestra de la lista para medir la conversión real.
- Probar dos precios (ej. $30 vs. $60) para ver cuál maximiza ingreso total, no solo ventas.

**Recomendación:** Aprobar la **validación** (Opción B) con un presupuesto y fecha de decisión, no el plan de $6.000/mes. Con los datos reales de captura y compra, recién se puede calcular qué combinación de tráfico, precio y producto recurrente llega al objetivo. Si el resultado sigue sin cerrar, conviene ajustar la meta antes que forzar el plan.

Si me pasan el precio que tienen en mente para una membresía y su tráfico por canal, armo el escenario completo.