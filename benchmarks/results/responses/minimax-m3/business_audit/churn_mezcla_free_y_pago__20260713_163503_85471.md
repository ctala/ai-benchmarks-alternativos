# MiniMax M3 — business_audit/churn_mezcla_free_y_pago

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.64 | quality: 6.94
- latency_total: 21.713s | tokens_per_second: 127.5
- input_tokens: 318 | output_tokens: 2768
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y un plan de acción práctico.

## Respuesta completa

Respira. El 31% es aritméticamente correcto, pero **mide una mezcla de poblaciones que no son comparables**. Te explico qué está pasando y qué hacer.

**El cálculo de tu plataforma**

62 bajas / 200 usuarios a inicio de mes = 31%

Pero esos 200 usuarios son dos productos distintos combinados:

| Segmento | Inicio de mes | Bajas | Churn real |
|---|---|---|---|
| Plan gratuito | 178 | 60 | **33.7%** |
| Plan de pago | 22 | 2 | **9.1%** |
| Total agregado | 200 | 62 | 31% |

Ese 5% que recordabas probablemente era el de pago. Está en 9.1%, peor de lo que pensabas, **pero lejos del 31%**.

**Por qué el 31% agregado no sirve**

El plan gratuito tiene churn estructural alto por diseño: gente que solo quería probar, cuentas que nunca iban a convertir, ciclo de vida distinto. Sumarlo con el de pago distorsiona todo. Es como promediar los tiempos de espera de un cajero automático con los tiempos de espera de una cirugía cardíaca: ambos son "tiempos de espera", pero juntos no te dicen nada útil.

Antes de interpretar cualquier métrica, hay que verificar qué población está midiendo. Tu plataforma mezcló dos poblaciones distintas y eso invalidó el número para toma de decisiones.

**Lo que todavía no sé y necesitas validar**

1. ¿Tu 5% histórico era **logo churn** de pago o **revenue churn** (MRR perdido)?
2. ¿Las 60 bajas gratuitas incluyen cuentas que estaban inactivas y el sistema marcó como churned automáticamente?
3. ¿Los 200 del denominador incluyen a quienes se dieron de alta durante el mes?
4. ¿Las 2 bajas de pago fueron voluntarias o por fallo de tarjeta?

**Plan de acción**

**Hoy, en las próximas 2 horas:**
- Reporta internamente el 9.1% de pago, no el 31%
- Cambia la métrica principal de tu dashboard a **churn de pago segmentado**

**Esta semana:**
- Configura dos métricas separadas: free churn y paid churn
- Si tu plataforma no permite separar, calcula con los exports manuales

**Este mes:**
- Implementa cohort retention real (mes de alta → % que sigue activo)
- Mide **revenue churn** (MRR perdido / MRR inicio), no solo logo churn. Si perdiste 2 cuentas pequeñas, el impacto en revenue es mínimo aunque el logo churn sea 9%
- Investiga las 2 bajas de pago con el equipo de customer success: ¿se podían haber evitado?

**Una pregunta que vale la pena hacerte**

Si tu plataforma mezcló free y paid en un solo número sin avisarte, ¿qué otras métricas está midiendo mal? Vale la pena auditar el resto antes de tomar decisiones grandes sobre ellas.