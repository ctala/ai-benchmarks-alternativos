# Solar Pro 4 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `upstage/solar-pro4`
- success: True  | final: 7.07 | quality: 6.67
- latency_total: 9.652s | tokens_per_second: 108.3
- input_tokens: 266 | output_tokens: 1045
- judge_score: 5.0 | justificación: 

## Respuesta completa

No le doy. Su intuición de crecer es correcta, pero su aritmética tiene tres fallas que, corregidas, cambian la decisión.

### 1. LTV está mal calculado (sin descuento ni margen)
- **Churn 8 % mensual** → vida media = 1 / 0.08 ≈ **12.5 meses**, no 24.  
  La fórmula `1 / churn` asume pérdida constante y no lineal; 2 años de retención con 8 % de fuga mensual es estadísticamente insostenible.
- **LTV económico** (lo que importa para decidir inversión) debe usar margen bruto y descuento:  
  `LTV = (Precio × Margen) / (Churn + tasa de descuento)`  
  Con tasa de descuento ~1 % mensual:  
  `(35 × 0.70) / (0.08 + 0.01) ≈ 24.5 / 0.09 ≈ $272`  
  Incluso sin descuento: `24.5 × 24.5 ≈ $600` de ingreso bruto, pero el margen neto sobre ese periodo es ~`$420`.

### 2. LTV/CAC real es ~0.9–1.4, no 2.9
- Con LTV económico ≈ $272 y CAC = $290 → **LTV/CAC ≈ 0.94**.  
- Con LTV sin descuento pero con margen ≈ $420 → **≈ 1.45**.  
- La regla de salud escalable suele ser **LTV/CAC ≥ 3** (y payback < 12 meses). Aquí estamos por debajo o en el límite bajo.

### 3. Payback es demasiado lento
- Contribución mensual por cliente = $35 × 0.70 = **$24.5**.  
- CAC $290 → meses para recuperar = 290 / 24.5 ≈ **11.8 meses**.  
- Con churn 8 %, la mitad de esos clientes se van antes de mes 9. En la práctica, el ciclo de recuperación se alarga y el riesgo de escala con cash flow crece.

### 4. Efecto escala y riesgo de cash
- $10.000 de ads a $290 CAC = ~34 clientes nuevos.  
- Si la curva de adquisición se mantiene, en el mes 1 ingresan ~$850 de contribución contra $10.000 gastados. El resto del recuperación depende de retención que, con 8 % de churn, es frágil.  
- Escalar así puede generar un hueco de caja grande antes de que el flujo se vuelva positivo.

### Qué haría antes de gastar los $10.000
1. **Corrija el modelo de LTV** con margen bruto, tasa de descuento y la distribución real de retención (no solo el promedio).  
2. **Meta de CAC**: para LTV/CAC ≥ 3 con LTV económico ~$272, el CAC objetivo sería ≤ ~$90. Con LTV sin descuento ~$420, ≤ ~$140. $290 está lejos.  
3. **Acelerar el payback**: pruebe precios más altos, bundles, planes anuales con descuento, o segmentos con menor churn. Cada punto de churn que baje o cada $5 de margen que suba mejora el ratio rápidamente.  
4. **Escalado gradual**: empece con un test controlado (ej. $1.000–$2.000), mida CPA real por canal, retención a 30/60/90 días y payback por cohort. Escale solo si el CAC efectivo baja o el LTV sube.  
5. **Si ya es rentable**, use ese colchón para crecer, pero no con una unidad económica que no cierra. Mejor primero mejorar la unidad, luego escalar con confianza.

**Resumen**: el plan tal como está no pasa la prueba de aritmética. No es que no deba crecer, es que con LTV/CAC ~1 y payback ~12 meses, $10.000 en ads pagados es alto riesgo. Ajuste precios/margen, baje CAC o suba retención, y luego escale.