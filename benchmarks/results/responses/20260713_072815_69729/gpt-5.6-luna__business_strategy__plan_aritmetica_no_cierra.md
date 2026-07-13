# GPT-5.6 Luna — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 4.84 | quality: 4.4
- latency_total: 6.93s | tokens_per_second: 133.6
- input_tokens: 198 | output_tokens: 926

## Respuesta completa

No lo aprobaría tal como está: **la multiplicación no llega al objetivo**.

### Cálculo real

- Visitas: **200.000/mes**
- Conversión a suscriptor: **1,5%**
- Suscriptores nuevos:  
  **200.000 × 1,5% = 3.000**
- Conversión a compradores: **2%**
- Compradores:  
  **3.000 × 2% = 60**
- Ingresos:  
  **60 × USD 30 = USD 1.800/mes**

El plan llega a **USD 1.800/mes**, no a USD 6.000. Está corto por **USD 4.200**, o alcanza apenas el **30% del objetivo**.

Además, hay un problema conceptual: si el curso cuesta **USD 30 como pago único**, no son ingresos “recurrentes”. Serían ventas mensuales provenientes del tráfico y de la lista, pero cada cliente no necesariamente vuelve a pagar.

### Qué tendría que cambiar

Para generar USD 6.000 con un producto de USD 30 hacen falta:

- **200 compradores/mes**

Con una conversión de suscriptor a comprador del 2%, necesitarían:

- **10.000 suscriptores nuevos/mes**

Con 200.000 visitas, eso implica una conversión visitante → suscriptor del:

- **5%**, no 1,5%.

Alternativamente, manteniendo el 1,5% de captura y el 2% de compra, necesitarían aproximadamente:

- **666.667 visitas/mes**

Otras combinaciones posibles:

| Visitas | Captura | Compra sobre lista | Ingreso |
|---:|---:|---:|---:|
| 200.000 | 1,5% | 2% | USD 1.800 |
| 200.000 | 1,5% | 6,67% | USD 6.000 |
| 200.000 | 5% | 2% | USD 6.000 |
| 666.667 | 1,5% | 2% | USD 6.000 |
| 200.000 | 1,5% | 2% | USD 1.800, pero con producto de USD 100 |

También habría que descontar reembolsos, comisiones de pago, impuestos y, si fuera una suscripción, la cancelación mensual.

### Veredicto

**No ejecutar como plan aprobado.** Primero corregiría el modelo y validaría con datos reales:

1. Medir conversión por fuente y página, no usar el 1,5% como promedio general.
2. Medir ventas por cohorte de suscriptores.
3. Separar ingresos brutos de ingresos netos.
4. Definir si los USD 30 son pago único o mensual.
5. Elegir una palanca principal: más tráfico, mayor captura, mayor conversión de venta, mayor precio o un embudo con upsells.

La primera versión realista del plan debería presentarse como **USD 1.800/mes de ingresos brutos**, salvo que se demuestre una mejora sustancial en alguna de esas métricas.