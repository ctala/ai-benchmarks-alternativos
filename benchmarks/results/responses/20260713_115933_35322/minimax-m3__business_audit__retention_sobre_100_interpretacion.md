# MiniMax M3 — business_audit/retention_sobre_100_interpretacion

- model_id: `minimax/minimax-m3`
- success: True  | final: 5.9 | quality: 6.0
- latency_total: 21.425s | tokens_per_second: 92.8
- input_tokens: 284 | output_tokens: 1989

## Respuesta completa

No, esa lectura es incorrecta — y peligrosa. Vamos por partes.

## Qué mide realmente ese 114%

Eso es **Net Revenue Retention (NRR)**, no retención de clientes. La fórmula conceptualmente es:

> NRR = (MRR inicial + Expansión − Churn − Downgrades) / MRR inicial

Puede estar por encima del 100% **porque las subidas de plan de los que se quedan compensan con creces la pérdida de ingresos por las cancelaciones**. Eso es lo que ha pasado en tu caso: "varios subieron de plan" generó más MRR del que perdiste con las 4 bajas. NRR > 100% es una métrica celebrada en SaaS (las empresas top rondan 110–130%).

## Lo que tu panel no te está diciendo

Tú confundes **retención de logos** (clientes) con **retención de ingresos**. Son cosas distintas:

| Métrica | Tu dato | Lectura |
|---|---|---|
| Retención de logos | 36 / 40 = **90%** | Has perdido 4 clientes |
| Gross Revenue Retention | < 100% | Seguro, porque hubo bajas |
| Net Revenue Retention | **114%** | Expansión > Churn en € |

**Perdiste el 10% de tu cartera de pago en un mes.** Eso no es "prácticamente no se me va nadie". Si esa tasa se sostiene de forma compuesta, 0.9¹² = 28% de retención anual de logos — un negocio en caída libre.

## Por qué NRR > 100% no es licencia para ignorar el churn

1. **La expansión tiene concentración.** Las subidas de plan suelen venir de unos pocos power users. Si esos se van, tu NRR se desploma de un mes para otro.
2. **El logo churn es lagging respecto a la causa.** Los clientes que cancelan este mes probablemente llevan meses insatisfechos. Para cuando el NRR se resiente, ya es tarde.
3. **El boca a boca negativo no aparece en el panel.** Cada cliente perdido suele hablar con 3–5 prospectos.
4. **Estás quemando tu motor de acquisition.** Si pierdes 10% al mes y capta digamos 8% al mes, tu base neta decrece sin que el NRR lo refleje.

## Qué hacer ahora mismo

- **Averigua quiénes son esos 4 y por qué se fueron.** Entrevista, no presupongas.
- **Calcula tu GRR** (Gross Revenue Retention, sin contar expansión). Probablemente verás el lado feo.
- **Segmenta la expansión**: ¿viene de 2 clientes grandes o está distribuida? Si son 2, tienes un riesgo de concentración enorme.
- **No abandones el trabajo de retención.** NRR > 100% con logo churn del 10% mensual es un edificio con buenas vistas pero cimientos podridos.

En resumen: el 114% te dice que los que se quedan gastan más. Lo que no te dice — pero tus datos sí — es que uno de cada diez se va cada mes. Eso segundo es lo que debería quitarte el sueño.