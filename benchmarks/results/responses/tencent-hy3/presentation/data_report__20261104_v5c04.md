# Tencent Hy3 — presentation/data_report

- model_id: `tencent/hy3`
- success: True  | final: 8.53 | quality: 9.28
- latency_total: 15.496s | tokens_per_second: 52.7
- input_tokens: 186 | output_tokens: 817
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Con estos datos de ventas, genera un reporte en formato markdown con tablas y analisis:

Producto A: Ene $45K, Feb $52K, Mar $48K, Abr $61K
Producto B: Ene $23K, Feb $25K, Mar $31K, Abr $29K
Producto C: Ene $12K, Feb $15K, Mar $18K, Abr $22K

Incluye:
1. Tabla de datos mensuales con totales por producto y por mes
2. Tabla de crecimiento % mes a mes
3. Analisis de tendencias
4. Producto estrella y producto preocupante
5. Proyeccion para mayo basada en tendencia


## Respuesta completa

# Reporte de Ventas (Ene – Abr)

## 1. Datos Mensuales y Totales

| Mes      | Producto A | Producto B | Producto C | Total Mes |
|----------|------------|------------|------------|-----------|
| Enero    | $45K       | $23K       | $12K       | $80K      |
| Febrero  | $52K       | $25K       | $15K       | $92K      |
| Marzo    | $48K       | $31K       | $18K       | $97K      |
| Abril    | $61K       | $29K       | $22K       | $112K     |
| **Total**| **$206K**  | **$108K**  | **$67K**   | **$381K** |

## 2. Crecimiento % Mes a Mes

*Cálculo: (Mes actual - Mes anterior) / Mes anterior × 100*

| Periodo        | Producto A | Producto B | Producto C | Total |
|----------------|------------|------------|------------|-------|
| Ene → Feb      | +15.6%     | +8.7%      | +25.0%     | +15.0%|
| Feb → Mar      | -7.7%      | +24.0%     | +20.0%     | +5.4% |
| Mar → Abr      | +27.1%     | -6.5%      | +22.2%     | +15.5%|
| **Acum. Ene→Abr**| **+35.6%** | **+26.1%** | **+83.3%** | **+40.0%** |

## 3. Análisis de Tendencias

- **Crecimiento general:** El negocio creció de $80K en enero a $112K en abril (+40% en 4 meses).
- **Producto A:** Mayor volumen absoluto; caída leve en marzo pero fuerte rebote en abril (+27%).
- **Producto B:** Volátil; subió bien en marzo pero retrocedió en abril.
- **Producto C:** Pequeño pero consistente; crecimiento sostenido todos los meses, sin caídas.

## 4. Producto Estrella y Producto Preocupante

- ⭐ **Producto estrella:** **Producto C**  
  Crecimiento acumulado del 83.3% y trayectoria 100% positiva mes a mes.
- ⚠️ **Producto preocupante:** **Producto B**  
  Aunque creció en el trimestre, mostró retroceso en abril (-6.5%) tras un pico en marzo; señal de inestabilidad.

## 5. Proyección para Mayo (por tendencia)

- **Producto A:** Promedio crecimiento trimestral ~11.7% → ~$68K
- **Producto B:** Tendencia inestable; si se mantiene nivel marzo–abril ~$30K
- **Producto C:** Ritmo ~22% mensual → ~$27K

**Estimado mayo:**  
| Producto | Proyección Mayo |
|----------|-----------------|
| A        | $68K            |
| B        | $30K            |
| C        | $27K            |
| **Total**| **$125K**       |

*Nota: Proyección basada en tendencias simples; no considera estacionalidad externa.*