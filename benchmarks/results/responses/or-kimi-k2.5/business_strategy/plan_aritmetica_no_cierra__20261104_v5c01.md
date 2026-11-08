# Kimi K2.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 79.279s | tokens_per_second: 27.3
- input_tokens: 237 | output_tokens: 2168

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

**No. No se aprueba.**

El plan muere en la multiplicación. Tu socio hizo las suposiciones más comunes del emprendedor: porcentajes que *suenan* conservadores, pero que al multiplicarse no llegan ni cerca del objetivo.

Hagamos la cuenta que él omitió:

| Variable | Cálculo | Resultado |
|----------|---------|-----------|
| Tráfico | 200.000 visitas | 200.000 |
| Suscriptores | × 1,5 % | **3.000 suscriptores/mes** |
| Compradores | × 2 % | **60 ventas/mes** |
| Ingreso | × $30 | **$1.800/mes** |

**Generan $1.800. No $6.000.**  
Les faltan $4.200, es decir, el plan solo cubre el **30 %** de la meta.

---

### Qué se necesitaría para que los números cierren

Con ese tráfico y esas conversiones, tienen tres palancas. Eligen una (o una combinación):

| Palanca | Qué debería pasar para llegar a $6.000 |
|---------|----------------------------------------|
| **Precio** | Pasar de $30 a **$100** (con 60 ventas) |
| **Conversión a compra** | Pasar del 2 % al **6,7 %** (con 3.000 suscriptores) |
| **Conversión a suscriptor** | Pasar del 1,5 % al **5 %** (manteniendo el 2 % de ventas) |
| **Tráfico** | Crecer a **~667.000 visitas/mes** (manteniendo todo lo demás) |

Ninguna de esas palancas es un ajuste menor. Subir la conversión de email a 6,7 % no es "conservador"; es un embudo de ventas muy sofisticado. Subir el precio 3x requiere reposicionar el producto por completo.

---

### Dos problemas adicionales que matan al plan

**1. "Recurrente" es una trampa.**  
Un curso de $30 de pago único **no genera ingresos recurrentes**. Si cierran 60 ventas este mes, el mes que viene empiezan de cero. Para que sea recurrente necesitan:
- Un modelo de suscripción/membership, o
- Volver a venderle cada mes a la lista (y ahí entra el agotamiento de audiencia).

**2. El mes 6 no empieza en el mes 1.**  
El plan asume que desde el día 1 tendrán el formulario optimizado, la secuencia de mails funcionando y la oferta validada. En la realidad, los primeros 2-3 meses se van en testear copy, lead magnet y frecuencia de envío. Los $1.800 (que son el techo realista) probablemente no los vean hasta el mes 4.

---

### Mi veredicto como analista

**Devuélvanlo a la mesa.** El plan no es malo como estrategia inicial; es peligroso porque *parece conservador* pero es matemáticamente imposible.

Para aprobarlo, necesito ver una de estas dos cosas:

1. **Una hoja con los escenarios corregidos** (por ejemplo: curso de $100 + 4 % de conversión de suscriptores, o un membership de $30/mes con churn controlado).
2. **Un plan de tráfico escalable** que explique cómo pasan de 200.000 a 600.000+ visitas mensuales en 6 meses.

¿Quieren que les arme el escenario que *sí* cierra con las palancas que tienen hoy?