# MiniMax M3 — business_audit/retention_sobre_100_interpretacion

- model_id: `minimax/minimax-m3`
- success: True  | final: 5.1 | quality: 4.8
- latency_total: 24.496s | tokens_per_second: 64.9
- input_tokens: 284 | output_tokens: 1591

## Respuesta completa

No. Tu lectura es incorrecta, y probablemente la más peligrosa que puedes hacer con ese número.

## Qué mide realmente esa cifra

Lo que ves es **Net Revenue Retention (NRR)**, también llamada retención neta de ingresos. La fórmula es:

$$NRR = \frac{MRR_{inicio} + Expansión - Downgrades - Churn}{MRR_{inicio}}$$

El 114% significa que los **ingresos** de tu cohorte crecieron un 14% neto. **No** mide si los clientes se quedan o se van. Mide si los dólares se quedan o se van.

Son cosas distintas.

## Qué está pasando en tu caso concreto

Vamos con tus números:

- Empiezas el mes con 40 clientes → pierdes 4 → te quedas con 36
- **Logo churn: 10%** (4 de 40)
- Varios suben de plan

Para que el NRR te dé 114% a pesar de perder 4 clientes, las subidas de plan tuvieron que generar suficiente revenue extra como para compensar la pérdida **y** añadir un 14% sobre el MRR inicial. Tus 36 clientes restantes están pagando, en promedio, bastante más que antes.

Aquí está la trampa: **el NRR te oculta el churn detrás de la expansión**. Estás pagando tu fuga de clientes con upgrades.

## La métrica que te falta: Gross Revenue Retention (GRR)

$$GRR = \frac{MRR_{inicio} - Downgrades - Churn}{MRR_{inicio}}$$

(Nota: GRR no incluye expansión, solo pérdidas).

Con tus números, si los 40 clientes tenían MRR similar y no hubo downgrades entre los 36 que quedan:

$$GRR ≈ \frac{36}{40} = 90\%$$

Un 90% de GRR es una hemorragia seria. La industria considera saludable un GRR ≥ 90%, y excelente ≥ 95%. Estás justo en el umbral — o por debajo.

## El cuadro real de tu retención

| Métrica | Tu valor | Lectura |
|---|---|---|
| NRR | 114% | "Los ingresos crecen" ✅ |
| GRR | ~90% (o peor) | "Estoy perdiendo clientes a un ritmo preocupante" ⚠️ |
| Logo retention | 90% | "1 de cada 10 clientes se va cada mes" ⚠️ |

## Por qué NO puedes dejar de preocuparte por el churn

1. **La expansión tiene un techo.** No todos los clientes van a subir de plan cada mes. Cuando se te agote ese efecto, el NRR colapsará al GRR, y verás el 90%真实.

2. **El logo churn se acumula.** Un 10% mensual compuesto ≈ 70% anual. En menos de un año has renovado toda tu base, pero solo porque se te fue casi toda.

3. **El coste de adquirir un cliente nuevo es típicamente 5–7× el de retenerlo.** Estás quemando capital en captación para llenar un cubo con agujeros.

4. **El NRR alto con GRR bajo es una señal de alerta para inversores.** Saben leer ambos números. El que muestra tu panel es el que elegiste ver.

## Qué hacer

- **Calcula tu GRR real este mes.** Lo necesitas.
- **Investiga por qué se fueron esos 4 clientes.** Cancelaciones voluntarias vs. pagos fallidos cuentan distinto.
- **No asumas que las subidas compensarán para siempre.** Diversifica: trabaja adquisición **y** retención.
- **Mira el NRR junto al GRR siempre.** Son complementarios, no intercambiables.

El 114% es una buena noticia a medias. La otra mitad dice que estás perdiendo clientes a un ritmo que tu expansión actual está camuflando. Deja de mirar solo la cifra que te halaga.