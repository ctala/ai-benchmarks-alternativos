# MiMo V2.6 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 7.4 | quality: 8.0
- latency_total: 45.984s | tokens_per_second: 22.5
- input_tokens: 149 | output_tokens: 1036

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

# La lectura es incorrecta. Tus propios números lo demuestran.

## Lo que dice el 114%

Ese porcentaje es **retención de ingresos** (NRR, *Net Revenue Retention*), que mide:

> **Ingresos actuales de los clientes que ya tenías** ÷ **Ingresos que esos mismos clientes generaban el mes anterior**

No mide cuántos clientes tienes. Mide cuánto dinero te dan.

## Lo que dicen tus números

| Métrica | Valor |
|---|---|
| Clientes mes anterior | 40 |
| Clientes actuales | 36 |
| **Churn de clientes** | **4/40 = 10% mensual** |
| Retención de ingresos | 114% |

**Se te fueron 4 clientes de cada 40.** Eso no es "prácticamente no se me va nadie". Es un churn mensual del 10%, que anualizado es brutal (a este ritmo, en 12 meses perderías ~72% de tu base).

## ¿Por qué el panel dice 114% si pierdes clientes?

Porque los que **se quedaron** subieron de plan. La fórmula es algo así:

```
Ingresos de los 36 clientes actuales
────────────────────────────────────── = 114%
Ingresos que los 40 clientes daban antes
```

Los upgrades de los que permanecieron **generan más dinero del que se fue con los 4 que se fueron**. Por eso el número supera el 100%: no es que no pierdas, es que **el expansion revenue tapa el hueco**.

## ¿Puedes dejar de preocuparte por el churn?

**No.** Y te explico por qué el razonamiento es peligroso:

1. **El 114% depende de que los que se quedan sigan subiendo de plan.** Si se satura el upsell (y se satura), el churn deja de estar compensado.

2. **El churn del 10% mensual es sostenible solo mientras el NRR esté alto.** Si mañana un cliente grande se va, el 114% se desploma de golpe.

3. **Captar un cliente nuevo es más caro que retener uno existente.** Si ya estás perdiendo 10% al mes, meter esfuerzo solo en captación es como llenar un balde con un agujero.

4. **NRR alto con churn alto es una bomba de relojería.** Funciona bien mientras el crecimiento de ingresos por cliente compensa, pero es un modelo frágil.

## Qué mirar en paralelo

- **Churn de clientes** (tu 10% mensual): ¿por qué se van los 4? ¿Es el mismo perfil siempre?
- **NRR por cohorte**: ¿los clientes que llevan más tiempo suben de plan, o solo los nuevos?
- **Gross Revenue Retention (GRR)**: es el NRR *sin contar los upgrades*. Si el GRR está por debajo del 100%, significa que **los ingresos de tus clientes base están cayendo** y solo el upsell los disimula.

**El 114% no dice que no pierdes clientes. Dice que los que quedan pagan más.** Son dos problemas distintos y necesitas atender ambos.