# Claude Opus 4.7 (suscripción) — business_audit/retention_sobre_100_interpretacion

- model_id: `claude-opus-4-7`
- success: True  | final: 6.1 | quality: 7.2
- latency_total: 37.573s | tokens_per_second: 31.2
- input_tokens: 6 | output_tokens: 1173

## Respuesta completa

# No. Estás leyendo dos cosas distintas como si fueran la misma.

## Qué dice realmente ese 114%

**Retención de ingresos ≠ retención de clientes.** Son métricas diferentes y en tu caso están apuntando en direcciones opuestas.

Lo que tenés es **NRR (Net Revenue Retention)** — mide cuánto dinero recurrente conservás de la cohorte anterior, sumando expansión (upgrades) y restando churn + downgrades. Que dé 114% significa una sola cosa: **el revenue expandido de los que se quedaron compensó con creces el revenue perdido por los que se fueron.**

No dice nada sobre cuánta gente conservaste.

## Tus números, sin maquillaje

| Métrica | Valor | Lectura |
|---|---|---|
| Clientes mes anterior | 40 | — |
| Clientes este mes (de esa cohorte) | 36 | Perdiste 4 |
| **Customer churn** | **10%** | Alto |
| **Logo retention** | **90%** | Mediocre para SaaS |
| **NRR** | **114%** | Bueno, pero engañoso en este contexto |

Un churn de clientes del 10% mensual anualizado es **~72% de la base perdida al año**. Eso es una fuga grave, no una situación bajo control.

## Por qué la intuición falla acá

El 114% te está ocultando el problema porque **los upgrades de unos pocos están tapando la salida de otros**. Es un patrón clásico y peligroso:

- Si los que se quedan son tus clientes grandes haciendo upgrade, el NRR se ve espectacular.
- Pero la base de clientes se está achicando.
- Cuando se te acabe el "colchón" de upgrades disponibles en la cohorte que queda, el NRR se desploma sin aviso.

Es lo que en la industria llaman **concentración de revenue enmascarando churn de logos**. Slack, Notion y muchos otros lo sufrieron en etapas tempranas.

## Qué hacer con esto

**No, no podés dejar de preocuparte por el churn.** Al contrario: tenés dos frentes abiertos.

1. **Investigá por qué se fueron esos 4.** Con 40 clientes, 4 salidas es una muestra chica pero accionable — hablá con cada uno. Cancel interviews, no encuestas.
2. **Segmentá el NRR.** Calculalo separando expansión, contracción y churn. Vas a ver el tamaño real del hueco que están tapando los upgrades.
3. **Recién después pensás en adquisición.** Meter clientes nuevos a un balde que pierde 10% mensual es quemar CAC.

## La regla mental

- **NRR > 100%** = tu revenue por cliente que se queda crece.
- **GRR (Gross Revenue Retention)** = cuánto revenue conservás *sin contar* expansión. Ese es el que te dice si hay fuga real.
- **Logo/Customer retention** = cuánta gente se queda.

Las tres tienen que estar sanas. La tuya tiene una sana (NRR) y dos con señales feas (logos -10%, y GRR seguramente <100% aunque no lo veas en el panel).

El panel no te está mintiendo. Te está mostrando una métrica que, sola, no alcanza para decidir dónde poner el esfuerzo.