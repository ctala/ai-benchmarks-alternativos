# Tencent Hy3 — strategy/pricing_strategy

- model_id: `tencent/hy3`
- success: True  | final: 6.87 | quality: 7.5
- latency_total: 82.152s | tokens_per_second: 83.0
- input_tokens: 207 | output_tokens: 6816

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

Tu SaaS tiene métricas muy sólidas de por sí (un LTV/CAC de 7.0x es excelente, el benchmark de la industria es >3.0x). Subir el precio de $60 a $89 representa un aumento del **48%**, pero sigues estando en la mitad del rango de tus competidores ($29-$149), lo cual te da un espacio seguro.

Aquí está el análisis detallado:

### 1. LTV/CAC Ratio Actual y Proyectado
*   **Actual:** $840 / $120 = **7.0x** (Muy saludable).
*   **Proyectado (si el churn se mantiene en 7%):** 14 meses * $89 = $1,246. Nuevo Ratio = **10.4x**.
*   **Perspectiva de Margen (Clave):** Tu costo es fijo en ~$8/mes. Tu margen de ganancia por cliente pasa de $52/mes a $81/mes (**+56%**). El LTV en términos de ganancia bruta pasa de $728 a $1,134.

### 2. Impacto en Churn (Benchmarks de Industria)
Un aumento de precio de 20% a 50% en SaaS suele provocar:
*   Un incremento absoluto en el churn de **1% a 3% mensual**.
*   Una caída en la conversión de nuevos leads de un 10-15% (lo que podría subir tu CAC ligeramente si no ajustas el mensaje).
*   **Tu punto de quiebre:** Para que el LTV de *margen* (ganancia real) baje del nivel actual ($728), tu churn tendría que superar el **11.1% mensual**. Tienes un colchón de seguridad de +4 puntos de churn antes de perder rentabilidad por cliente.

### 3. Modelo de 3 Escenarios
*(Aplicado a tu base actual de 200 clientes y a nuevos usuarios)*

| Escenario | Nuevo Churn | Vida Útil | Nuevo LTV | Ratio LTV/CAC | Clientes que se quedan | Nuevo MRR |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Optimista** | 7.5% | 13.3 meses | $1,183 | 9.8x | 196 (2% se va) | $17,444 |
| **Realista** | 9.0% | 11.1 meses | $988 | 8.2x | 190 (5% se va) | $16,910 |
| **Pesimista** | 11.0% | 9.0 meses | $801 | 6.6x | 170 (15% se va) | $15,130 |

*Nota: Incluso en el escenario pesimista, el ratio sigue siendo 6.6x y el LTV de margen ($729) es casi idéntico al actual, pero con más ingresos mensuales.*

### 4. Recomendación con Números Concretos
**Sí, sube el precio.** El riesgo de destruir valor es matemáticamente bajo.

*   **Ganancia inmediata:** Si asumimos el escenario realista (190 clientes se quedan), pasas de $12,000 MRR a **$16,910 MRR**.
*   **Impacto anual:** Generas **+$58,920 al año** de ingresos recurrentes adicionales con el mismo CAC.
*   **Acción sugerida:** Usa ese excedente para bajar ese 7% de churn (mejorando onboarding) o para invertir en adquisición, ya que ahora tu CAC de $120 es aún más eficiente.

### 5. Estrategia de Implementación
No apliques el cambio a todos mañana (evita el *bill shock*). Usa una **Estrategia Híbrida de Grandfathering + Anclaje**:

1.  **Nuevos clientes:** Cobrar $89 desde mañana. Ajusta tu sitio web y propuesta de valor.
2.  **Aviso de 60 días (Base actual):** Comunica el cambio con antelación. Ofrece una "ventana de oportunidad" para pagar anualmente al precio viejo ($720) y congelar el precio. Esto retiene efectivo y evita churn.
3.  **Migración escalonada:** A los que no paguen anual, súbeles a $75 en el mes 3 y a $89 en el mes 6.
4.  **Value-Add (Justificación):** No lo vendas como un simple "aumento". Empaqueta los $89 con 1 o 2 mejoras (ej. reportes de inventario en PDF o alertas de stock bajo) para que perciban un *upgrade* y no solo un cobro mayor.