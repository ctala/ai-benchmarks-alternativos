# Seed 2.1 Turbo — business_strategy/plan_aritmetica_no_cierra

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.27 | quality: 10.0
- latency_total: 158.137s | tokens_per_second: 56.8
- input_tokens: 252 | output_tokens: 8981

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

❌ No lo aprobamos todavía. El plan tiene un error de cálculo básico que hace que ni siquiera llegue al 30% del objetivo, además de supuestos ocultos que lo invalidan de entrada. Como dice la regla: la mayoría de los planes mueren en la multiplicación, y este no es la excepción.

---

## Primero: la cuenta básica con LOS MISMOS NÚMEROS que pone el plan (sin agregar nada):
Partimos de los datos que tu socio considera "conservadores y realistas":
1. 200.000 visitas/mes × 1,5% de conversión a suscriptor = **3.000 suscriptores NUEVOS por mes**
2. 3.000 suscriptores × 2% de compra = **60 ventas NUEVAS por mes**
3. 60 ventas × $30 por curso = **$1.800 USD de ingresos BRUTOS por mes**

O sea, con los números que él mismo eligió, llegas a $1.800/mes, no a $6.000. Es el 30% del objetivo. Tu socio se equivocó de cuenta, punto.

---

## Los 3 errores conceptuales que matan el plan (más allá del cálculo):
### 1. Confunde ingresos por ventas nuevas con ingresos recurrentes
El plan dice que llega a "$6.000/mes recurrentes", pero un curso de $30 es de pago único: la gente lo compra una sola vez. Los ingresos que generas son solo de ventas nuevas cada mes, no son recurrentes.

Con los números del plan, te quedas **estancado en $1.800/mes desde el primer mes** (porque el tráfico y las conversiones son estables, así que cada mes tenés las mismas 60 ventas nuevas). No hay camino de crecimiento hasta los $6k.

> *Nota: si el curso fuera una suscripción mensual de $30 (cosa que el plan no menciona), la cuenta cambia, pero tampoco llegas de golpe: necesitarías 200 suscriptores activos para los $6k, lo que tardarías ~4 meses sin bajas, o 5-6 meses con bajas normales (5%/mes). Pero un curso no es una suscripción, a menos que tengas contenido nuevo todos los meses para justificarlo.*

### 2. Asume que los porcentajes se aplican a TODO el tráfico y TODA la lista, sin matices
El 1,5% de conversión a suscriptor es "realista para el sector" solo si:
- El formulario está en páginas de contenido 100% relacionado con el curso (no en todo el sitio: páginas de contacto, acerca de, contenido de temas tangenciales bajan la conversión a la mitad o más).
- Tienes un lead magnet de valor (no solo "suscríbete a nuestro boletín").

Si solo el 40% de tus 200k visitas son de contenido relevante, la conversión real se aplica a 80k visitas, no a 200k: te quedan 1.200 suscriptores/mes, 24 ventas, **$720/mes**. Menos de la mitad del cálculo básico.

Lo mismo con el 2% de compra: es realista solo si tienes una secuencia de nutrición armada y probada, y la lista es cálida. Si envías un solo correo de venta, la conversión puede ser del 0,3% o menos.

### 3. No resta ningún costo
Los $1.800 son ingresos brutos. Después de restar:
- Comisiones de pasarela (3-5% + $0,30 por transacción): ~$70
- Herramientas de email marketing, hosting del curso: ~$100
- Impuestos (si corresponden): 10-30%

Te quedan entre $1.200 y $1.400 netos por mes. Ni siquiera llegas a la cuarta parte del objetivo.

---

## ¿Qué hay que cambiar para que SÍ llegue a $6k/mes en 6 meses?
Tienes 5 palancas de crecimiento, y el plan solo usa 3 con valores muy bajos para el objetivo. Aquí las opciones factibles, con números que cierran:

### Opción 1: Subir el precio del curso a $100 USD (la más sencilla)
Con los mismos porcentajes "conservadores" (3k suscriptores/mes, 60 ventas):
> 60 ventas × $100 = $6.000 USD/mes brutos.

*Requisito: que el curso tenga valor suficiente para justificar $100 (si es un curso de 10 módulos con plantillas, casos prácticos y soporte, sí lo es; si es un pdf de 20 páginas, no).*

### Opción 2: Aumentar la conversión a suscriptor al 5% (dejando el precio en $30)
Para llegar a 200 ventas/mes (que ×$30 = $6k) necesitas 10.000 suscriptores/mes. Con 200k visitas, la conversión a suscriptor tiene que ser del 5%.
*Es alcanzable si creas lead magnets específicos por tema de contenido, pones formularios en puntos de alta intención (final de artículos, popups con descuento) y optimizas la oferta. Pero no es "conservador", es ambicioso, requiere trabajo.*

### Opción 3: Subir el valor promedio por cliente (AOV) a $100 con upsells
Dejando el curso en $30, agregas productos complementarios:
- Upsell 1: Plantillas editables por $47 (lo compra el 40% de los clientes)
- Upsell 2: Sesión de consultoría grupal por $150 (lo compra el 10% de los clientes)

El AOV pasa a ser: $30 + ($47×0,4) + ($150×0,1) = $63,8. Con 60 ventas, son $3.828/mes. Todavía falta, pero si agregas una membresía mensual de $20 para comunidad (que se suscribe el 30% de los compradores), en 6 meses acumulas suficientes miembros para llegar a los $6k.

### Opción 4: Convertir el curso en una membresía mensual de $30 (si querés ingresos recurrentes de verdad)
Cada mes agregas 60 nuevos miembros (con los porcentajes actuales). Para llegar a $6k necesitas 200 miembros activos. Con una tasa de cancelación del 5% mensual (normal para membresías), llegas a los 200 miembros en ~6 meses exactos.
*Requisito: tener contenido nuevo cada mes, o una comunidad activa, para justificar el pago recurrente.*

---

## Paso a paso para validar el plan ANTES de ejecutarlo a lo grande (no te fíes de supuestos):
1. **Valida la conversión a suscriptor primero**: Pon el formulario con el lead magnet en tu artículo de mayor tráfico relacionado con el curso. Medí 7-14 días. Si la conversión es mayor al 1%, el 1,5% es alcanzable con optimización. Si es menor al 0,5%, el supuesto es erróneo.
2. **Valida la conversión a venta**: Si ya tenés una lista de aunque sea 500 suscriptores, enviá la oferta del curso y medí cuántos compran. Si es mayor al 1,5%, el 2% es realista. Si es menor, tenés que mejorar la oferta o la secuencia de nutrición.
3. **Calcula el AOV y los costos netos**: No trabajes con ingresos brutos, sabé cuánto te quedás por cada venta.
4. **Ajusta el plan con números reales**: No uses porcentajes "de sector", usa tus propios números.

---

### Conclusión:
El plan actual no se aprueba, porque su cálculo básico no llega ni a la tercera parte del objetivo, y confunde conceptos clave (recurrente vs pago único). Pero se puede arreglar tocando 1 o 2 palancas, y validando los supuestos en 2 semanas antes de invertir tiempo en ejecutarlo a lo grande.