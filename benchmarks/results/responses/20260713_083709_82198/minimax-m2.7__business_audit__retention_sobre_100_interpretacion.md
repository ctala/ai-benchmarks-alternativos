# MiniMax M2.7 — business_audit/retention_sobre_100_interpretacion

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 4.07 | quality: 3.34
- latency_total: 19.848s | tokens_per_second: 38.2
- input_tokens: 128 | output_tokens: 758

## Respuesta completa

No es correcto, y el problema que describes es precisamente el tipo de situación donde confiar ciegamente en esta métrica puede ser peligroso.

## Lo que el 114% realmente te dice

La retención de ingresos mide cuánto de los ingresos recurrentes del período anterior se mantienen, **incluyendo expansiones y restando churns**. No incluye nuevos clientes.

**En tu caso concreto:**

- Ingresos de clientes que se fueron: los que se fueron (~4) contributing revenue
- Ingresos de clientes que quedaron: la subida de plan compensó esas salidas y dejó un +14% neto

El 114% te dice: "tu base existente generó más dinero que antes". **No te dice nada sobre si esa base se encogió.**

## Lo que te está ocultando

```
40 clientes → 36 clientes
```

Perdiste el 10% de tus clientes en un mes. Eso es un churn del 10% mensual, que es alto. Si esto se mantiene, en 7 meses te quedas sin clientes, por muchos upsells que hagas.

## Por qué el NRR alto puede ser un problema aquí

| Escenario | NRR | Clientes | Lectura real |
|-----------|-----|----------|--------------|
| Tu situación actual | 114% | -10% | **Alerta roja** |
| Caso típico que genera confusión | 114% | estable | Saludable |

Has compensado la pérdida de clientes con upgrades. Eso funciona **mientras queden clientes a los que hacer upgrade**. Si la tendencia continúa, eventualmente no tendrás base sobre la que expandir.

## Lo que deberías vigilar en paralelo

- **Churn rate de clientes**: 4 de 40 en un mes es la cifra que realmente importa aquí
- **NRR por cohorte**: cómo retienen los clientes que llevan X meses
- **Tiempo hasta el churn**: si los que se van son clientes nuevos, el problema es de onboarding; si son antiguos, es de éxito del cliente

**Conclusión directa:** Tienes churn problemático y eso requiere acción. El 114% es una buena señal de que los clientes que *se quedan* están satisfechos y dispuestos a pagar más. Pero el 10% de pérdida de clientes mensuales necesita atención, no despreocupación.