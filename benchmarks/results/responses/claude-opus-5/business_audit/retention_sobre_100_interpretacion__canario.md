# Claude Opus 5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 33.33s | tokens_per_second: 61.4
- input_tokens: 216 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## Respuesta corta

No. Estás leyendo una métrica de **ingresos** como si fuera una métrica de **clientes**. Son cosas distintas, y en tu caso apuntan en direcciones opuestas.

## Qué mide realmente ese 114%

"Retención de ingresos" en la mayoría de paneles es **NRR (Net Revenue Retention)**:

```
NRR = (MRR inicial + expansión − contracción − churn) / MRR inicial
```

La clave es que la **expansión está en el numerador**. Eso significa que unos pocos upgrades pueden compensar —y ocultar— la pérdida de varios clientes. El 114% no dice "casi nadie se va"; dice "el dinero que queda, más lo que subió de plan, supera lo que había".

## Tus números reales

- **Retención de clientes (logo retention): 36/40 = 90%**
- **Churn de clientes: 10% mensual**

Si eso se sostiene: `0,9^12 ≈ 28%`. Es decir, **perderías ~72% de tu base en un año**. Un 10% mensual es un churn alto en casi cualquier segmento B2B SaaS.

Y una advertencia importante: **¿esos 36 incluyen clientes nuevos de este mes?** Si captaste, digamos, 3 nuevos, entonces de los 40 originales solo sobrevivieron 33 → retención real del 82,5%, churn del 17,5%. El neto (40 → 36) enmascara el bruto. Necesitas separar: *retenidos + nuevos − perdidos*.

## La métrica que te falta: GRR

Pide o calcula la **GRR (Gross Revenue Retention)**, que excluye la expansión:

```
GRR = (MRR inicial − contracción − churn) / MRR inicial
```

La GRR **nunca puede pasar de 100%**. Es tu métrica de fugas real. Un patrón típico de tu situación sería algo como GRR 88-92% y expansión +24 puntos → NRR 114%. Eso no es un negocio sin churn: es un negocio con churn notable y unos pocos clientes tapando el agujero.

## Por qué esto es frágil

1. **La expansión tiene techo, el churn no.** Un cliente puede subir de plan 2 o 3 veces; irse solo lo hace una vez, y es definitivo.
2. **Concentración.** Con 40 clientes, "varios subieron de plan" puede significar que 2 cuentas explican todo tu 114%. Si una de ellas se va el mes que viene, tu NRR se desploma por debajo de 100% sin que haya cambiado nada más.
3. **Ruido estadístico.** A esta escala, un solo movimiento mueve la métrica varios puntos. No tomes decisiones estratégicas sobre una lectura mensual de una base de 40.
4. **Te comes tu propio funnel de expansión.** Si los 4 que se fueron eran cuentas pequeñas, hoy no te duele en ingresos, pero eran precisamente los que iban a subir de plan en 6-12 meses.
5. **Encarece la captación.** Con un 10% mensual de fuga, buena parte de cada nuevo cliente que traigas solo repone el hueco. Es un cubo agujereado: subir el caudal no arregla el agujero, solo aumenta la factura.

## Qué haría yo antes de reasignar presupuesto

- **Separar las tres métricas** en el panel: logo retention, GRR y NRR. Nunca mires solo la última.
- **Contar los 4 que se fueron uno a uno.** Con 40 clientes puedes hablar con todos. ¿Mismo segmento? ¿Se fueron antes de los 90 días (problema de onboarding/fit) o después de 12 meses (problema de valor sostenido)?
- **Calcular la concentración:** ¿qué % de