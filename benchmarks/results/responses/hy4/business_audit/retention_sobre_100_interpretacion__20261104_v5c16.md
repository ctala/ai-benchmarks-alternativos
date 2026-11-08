# Tencent Hy4 — business_audit/retention_sobre_100_interpretacion

- model_id: `tencent/hy4`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 52.804s | tokens_per_second: 86.3
- input_tokens: 155 | output_tokens: 4556

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Las dos lecturas son incorrectas, y la segunda —«puedo dejar de preocuparme por el churn»— es justo la decisión que el 114% está ocultando.

## 1. Lo que dice el panel (y lo que no dice)

Un valor >100% en «retención de ingresos» solo puede ser **NRR** (*Net Revenue Retention* / *Net Dollar Retention*):

```
NRR = (MRR_inicial − MRR_perdido − contracción + expansión) / MRR_inicial
```

Se calcula **sobre la cohorte del mes pasado y excluye a los clientes nuevos**. O sea: mide cuánto facturan hoy *los que ya eran tuyos*, no cuántos siguen siendo tuyos ni cuánto creció el negocio total.

Dos consecuencias inmediatas:

- **La retención de clientes nunca puede superar 100%.** Es un recuento de cuentas: `(40 − bajas) / 40`. Como máximo 100%. Si un panel te mostrara >100% en «clientes», estaría midiendo crecimiento neto de logos, no retención.
- **Ironía relevante:** estás usando una métrica que explícitamente *ignora* la captación nueva para justificar volcar todo el esfuerzo en captación nueva. El 114% no dice nada sobre tu capacidad de adquirir.

> ⚠️ Primer chequeo: confirma la definición del panel. Si ese 114% mete las altas del mes en el numerador, no es retención, es crecimiento de MRR mal etiquetado, y es aún menos informativo.

## 2. Tus números reales

Con 40 → 36:

| Métrica | Valor | Lectura |
|---|---|---|
| Retención de logos | **90%** (como máximo) | 4 de 40 se fueron |
| Logo churn mensual | **10%** | No es «prácticamente nadie» |
| Logo churn anualizado* | **~72%** | `(0,90)^12 ≈ 28%` supervivientes |
| NRR | 114% | Expansión tapando el agujero |

\*Extrapolación con churn constante; sirve para dimensionar, no como pronóstico.

Y hay un escenario peor: si entre esos 36 hay altas nuevas, de los 40 originales quedan **menos de 36**. Con 2 nuevos, la retención de cohorte es 34/40 = **85%**, churn del 15% mensual.

Normalizando el MRR inicial a 100 (ARPA 2,5), el desglose que produce tu 114% es aproximadamente:

```
GRR  ≈ 90%   → 100 − 10 de MRR perdido (las 4 bajas)
Expansión ≈ +24 pts  →  los 36 supervivientes suben de plan
─────────────────────────────────────────────
NRR  = 114%
```

**El 24% de upsell está cubriendo un 10% de churn.** El agregado neto es precioso; el bruto no lo es. Pide siempre el **GRR** (*Gross Revenue Retention*, sin expansión): ese sí tiene techo en 100% y es el que te dice si la base está sana.

## 3. El matiz que hace esto especialmente engañoso

Que el NRR esté en 114% *mientras pierdes 4 cuentas* sugiere que se fue gente de ticket bajo y crecieron cuentas grandes. Es la combinación más tramposa posible: el indicador de dinero mejora justo cuando estás **podando el embudo por abajo**. Esos clientes pequeños son el pipeline futuro de upsell. Los estás cambiando por un upgrade hoy.

## 4. Por qué no puedes relajar el churn

1. **La expansión es un stock; el churn es un flujo.** Un cliente que pasó a Enterprise no puede subir de plan todos los meses. El churn del 10% sí se repite cada mes. Para sostener 114% con menos cuentas, necesitas exprimir más a los que quedan, mes tras mes. Es una rueda que se acelera hasta que se rompe.
2. **Concentración.** «Varios subieron de plan» significa que ~24 puntos de MRR dependen de unas pocas cuentas. Si una de esas se va en noviembre, el NRR cae por debajo de 100% de golpe. Mira la distribución, no la media.
3. **LTV/CAC se desploma.** Con 10% de churn mensual de logos, la vida media es `1/0,10 ≈ 10 meses`. Con margen del 80%, el LTV ronda **8 × ARPA**. Ese es el CAC que puedes permitirte pagar, y es bastante más bajo de lo que un 114% en el panel invita a presupuestar. Meter todo en captación, con ese churn, es comprar agua en un cubo agujereado —y pagar CAC por cada litro.
4. **Coste asimétrico.** Sustituir MRR con upsell es barato. Sustituir *cuentas* con adquisición es caro. Estás proponiendo cambiar el mecanismo barato por el caro.

## 5. Qué mirar mañana

Pídele al panel que desglose, no que netee:

- **GRR** separado del NRR → el daño real sin maquillaje
- **Churn de MRR (gross)**, **contracción/downgrades** y **expansión** por separado
- **Retención de logos** por cohorte, y altas nuevas separadas de supervivientes
- **NRR por segmento y por cuenta top-10** → detectar concentración
- **Quick ratio** `(nuevo + expansión) / (churn + contracción)` si quieres crecimiento, sabiendo que ese sí incluye nuevos y **no** es retención
- **LTV/CAC y payback** recalculados con el churn de logos, no con el NRR

## 6. Cuándo sí sería una buena noticia

El 114% no es malo en sí. Es excelente **si** viene acompañado de GRR ≥ 95% y logo churn de 1–2% mensual: ahí significa que retienes casi todo y además expandes. Con GRR ~90% y 10% de churn de cuentas, significa que estás creciendo sobre una base que se encoge.

En una frase: **no te va «prácticamente nadie»; te va el 10% en un mes, y unos pocos clientes grandes están pagando la factura para que el panel no lo note.** Preocúpate por el churn antes de acelerar la captación.