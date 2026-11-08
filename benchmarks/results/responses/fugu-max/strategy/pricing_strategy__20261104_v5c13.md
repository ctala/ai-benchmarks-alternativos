# Fugu Max — strategy/pricing_strategy

- model_id: `sakana/fugu-max`
- success: True  | final: 6.4 | quality: 7.5
- latency_total: 81.863s | tokens_per_second: 83.5
- input_tokens: 270 | output_tokens: 6836

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

## Resumen ejecutivo

Subir de **$60 a $89** es un aumento del **48,3%**. La economía por cliente mejora si el churn no sube demasiado, pero tu **7% de churn mensual ya es elevado**: equivale aproximadamente a perder el **58% de los clientes en un año** si se mantiene constante.

Mi recomendación: **cobra $89 a los nuevos clientes desde ahora** y prueba el aumento con los actuales antes de aplicarlo a todos. El alza parece rentable en los tres escenarios modelados, pero conviene validar cuánto churn adicional provoca en tu base real.

## 1. LTV/CAC actual y proyectado

Con los datos que das:

- LTV informado: **$840**
- CAC: **$120**
- **LTV/CAC informado: $840 / $120 = 7,0x**
- Usando exactamente el churn del 7%, la vida esperada es `1 / 0,07 = 14,3 meses`; el LTV de ingresos sería **$60 / 0,07 = $857**, o **7,14x**. La diferencia es redondeo.

Para evaluar mejor la rentabilidad, conviene descontar el costo variable:

- Margen bruto mensual actual: **$60 − $8 = $52**
- LTV de margen bruto: **$52 / 0,07 = $743**
- **LTV/CAC sobre margen bruto: $743 / $120 = 6,19x**

Con el nuevo precio, si el costo sigue siendo $8 por cliente:

- Margen bruto mensual: **$89 − $8 = $81**
- Margen bruto porcentual: **91,0%**, frente a 86,7% hoy.
- Recuperación del CAC: pasa de **2,31 meses** a **1,48 meses**.

> Supongo que los $8 son el costo variable mensual por cliente. Si son por usuario y cada cliente tiene varios usuarios, hay que recalcular el margen con el costo real por cuenta.

## 2. Churn: contexto y límites del benchmark

Como referencia amplia, en benchmarks de SaaS B2B suele verse churn mensual de clientes de alrededor de **3–5% en SMB** y **1–2% en segmentos más grandes**, aunque las cifras dependen mucho de cómo se mida y del tipo de producto. Con **7% mensual**, tu churn actual merece atención incluso antes de cambiar el precio.

No existe una regla fiable del tipo “subir el precio 48% aumenta el churn en X puntos”: depende de cuánto valor perciben los clientes, cuánto usan el producto, sus alternativas y la forma de comunicar el cambio. Por eso, los escenarios siguientes son **supuestos de planificación**, no un benchmark que prediga tu resultado.

## 3. Tres escenarios

Para modelar el cambio supongo una cancelación inicial al anunciar o aplicar el aumento, seguida de un churn mensual constante. El LTV de la tabla usa el churn mensual posterior y **no** incluye esa cancelación inicial.

| Escenario | Cancelación inicial supuesta | Churn mensual posterior | LTV/CAC por ingresos | LTV/CAC por margen bruto | Clientes esperados tras 1 mes | MRR tras 1 mes |
|---|---:|---:|---:|---:|---:|---:|
| Optimista | 2% (4 clientes) | 7,5% | 9,89x | **9,00x** | 181,3 | **$16.136** |
| Realista | 8% (16 clientes) | 9% | 8,24x | **7,50x** | 167,4 | **$14.902** |
| Pesimista | 20% (40 clientes) | 12% | 6,18x | **5,63x** | 140,8 | **$12.531** |

Las cantidades de clientes son valores esperados, por eso pueden tener decimales.

Como comparación, si mantuvieras el precio de $60 y el churn actual de 7%, esperarías tener **186 clientes y $11.160 de MRR** tras un mes. Así, incluso el escenario pesimista modelado da más MRR que continuar igual. Pero ese resultado depende de los supuestos: no implica que el aumento sea inocuo a largo plazo.

En el escenario realista, por ejemplo, el margen bruto mensual esperado tras ese primer mes sería aproximadamente **$13.563**, frente a **$9.672** si mantuvieras el precio y el churn actual.

### Punto de equilibrio por pérdida de clientes

Sin contar churn futuro, necesitas conservar al menos **67,4%** de los clientes para que el MRR a $89 iguale los $12.000 actuales: `60 / 89`. En términos de margen bruto, el umbral es aproximadamente **64,2%**: `52 / 81`. Son umbrales matemáticos, no objetivos recomendados: perder un tercio de la base seguiría siendo un resultado muy costoso para la retención y el crecimiento.

## 4. Recomendación concreta

**Sí probaría $89, pero no subiría a toda la base actual de golpe.**

- **Nuevos clientes:** fija $89 como precio de lista inmediatamente.
- **Clientes actuales:** prueba primero con una cohorte representativa. Una alternativa gradual es pasar de $60 a **$74** en la siguiente renovación y a **$89** tres a seis meses después, avisando con anticipación.
- **Protección de clientes sensibles:** permite bajar a un plan más básico si puedes ofrecerlo sin deteriorar demasiado el margen. Para clientes estratégicos o con contratos vigentes, respeta las condiciones acordadas.
- **Objetivos de evaluación:** usa el escenario realista como referencia inicial: hasta **8% de cancelación asociada al cambio** y un churn posterior de **9% mensual**. Si en la cohorte de prueba las cancelaciones superan el 10% en 60 días o el churn mensual sostenido supera el 9%, pausa el despliegue y revisa segmentación, valor ofrecido y comunicación.

Aunque el escenario pesimista todavía arroja un LTV/CAC de margen bruto de **5,63x**, eso no elimina el riesgo: el LTV calculado asume churn constante, CAC fijo y que no cambian otros costos. Además, tu churn actual ya es alto, así que reducirlo puede tener tanto valor como subir el precio.

## 5. Estrategia de implementación

1. **Aísla el efecto del precio.** Registra el churn y las cancelaciones antes del anuncio y compáralos con los de la cohorte que recibe el aumento.
2. **Comunica el cambio con 30–60 días de anticipación.** Explica qué mejoras, soporte o funcionalidades justifican el nuevo precio; evita presentar solo el aumento.
3. **Da una transición clara.** Puedes mantener el precio actual durante un periodo limitado o permitir prepagar un año al precio vigente antes de la fecha de cambio. Evitaría el grandfathering indefinido para todos, porque dificulta mantener una estructura de precios simple.
4. **Mide semanalmente durante los primeros 60–90 días:** cancelaciones y churn de clientes, upgrades/downgrades, MRR retenido, cobros fallidos, conversión de nuevos clientes y motivos de baja.
5. **Revisa por segmento.** Si clientes con bajo uso o menor tamaño cancelan mucho más, considera cobrar $89 por un plan con más valor y conservar una opción de entrada, en vez de aplicar el mismo cambio a todos.

En suma: **$89 parece viable por margen y LTV/CAC, pero conviene desplegarlo por cohortes y tratar el churn actual como un problema paralelo, no como un riesgo que el aumento vaya a resolver.**