# Claude Opus 4.7 (suscripción) — business_audit/churn_mezcla_free_y_pago

- model_id: `claude-opus-4-7`
- success: True  | final: 2.69 | quality: 2.4
- latency_total: 40.869s | tokens_per_second: 38.2
- input_tokens: 6 | output_tokens: 1560

## Respuesta completa

Respiro. El panel te está mintiendo por agregación, no porque tu negocio se esté cayendo.

## Lo que en realidad muestra tu panel

Estás dividiendo 62 / 200 = 31%. Eso mezcla dos poblaciones que no tienen nada que ver entre sí:

| Segmento | Base inicio de mes | Bajas | Churn real |
|---|---|---|---|
| Free | 178 | 60 | **33.7%** |
| Pago | 22 | 2 | **9.1%** |
| "Total" (el del panel) | 200 | 62 | 31% ← número inútil |

El 31% no mide **nada** que puedas accionar. Es un promedio ponderado dominado por el free (89% de tu base), que se comporta como una lista de correo, no como clientes.

## Qué tan grave es, de verdad

**Churn de pago = 9.1% mensual.** Ahí sí hay señal, y no es catastrófico pero no es sano:

- Benchmark SaaS B2C sano: 3-7% mensual.
- 9.1% mensual ≈ **~67% anual** si se sostiene. Ojo con eso.
- Pero son **2 bajas sobre 22**. Muestra chica: una baja más o menos mueve el número del 4.5% al 13.6%. No puedes concluir tendencia con este N.

**Churn de free = 33.7%.** Casi siempre es ruido, no problema. Free churn suele ser gente que probó, no volvió, y el sistema los marca inactivos. No pierdes revenue, pierdes ilusión de tamaño de audiencia.

## Antes de hacer nada, verifica 3 cosas

1. **¿Qué define "baja" el panel?** ¿Cancelación explícita, o inactividad X días? Si es inactividad, el free churn es mentira operativa.
2. **¿Los 2 pagos que se fueron son del mismo cohorte / mismo plan / mismo motivo?** Con N=2 necesitas hablar con esas 2 personas, no correr un análisis.
3. **¿Tienes revenue churn separado de user churn?** Si los 2 que se fueron eran tus 2 planes más caros, el impacto en MRR es muy distinto a si eran los 2 más baratos.

## Plan concreto (esta semana)

**Hoy:**
- Contactar a los 2 pagos que cancelaron. Preguntar por qué. 2 llamadas, no encuesta.
- Calcular **revenue churn** ($ perdido / MRR inicio de mes), no user churn. Esa es la métrica que importa.

**Esta semana:**
- Arreglar el panel: separar dashboards de free y pago. Nunca mires el agregado otra vez.
- Definir "churn" con precisión (cancelación activa vs. inactividad). Documentarlo.
- Traer 3 meses de historia para ver si 9.1% es tendencia o pico. Con un solo mes no sabes nada.

**Este mes:**
- Con 22 pagos, tu palanca no es reducir churn, es **subir la base**. Bajar de 9.1% a 5% te "salva" 1 usuario. Sumar 10 pagos nuevos te cambia la vida.
- Setear alerta cuando el churn de pago supere 15% en un mes con N ≥ 30. Antes de eso, es ruido estadístico.

## La lección para el panel

Nunca reportes una métrica de retención sin la pregunta: **¿de qué población?** Un número agregado sobre poblaciones heterogéneas (free vs. pago, trial vs. activo, self-serve vs. enterprise) siempre miente. Segmenta primero, mide después.

No estás en 31%. Estás en 9.1% de pago con muestra chica y 33.7% de free que probablemente es limpieza de inactivos. Muy distinto plan de acción.