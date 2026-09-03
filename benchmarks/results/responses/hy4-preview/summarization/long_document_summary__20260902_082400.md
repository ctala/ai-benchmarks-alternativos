# Tencent Hy4 preview — summarization/long_document_summary

- model_id: `tencent/hy4-preview`
- success: True  | final: 7.34 | quality: 8.64
- latency_total: 116.37s | tokens_per_second: 68.0
- input_tokens: 480 | output_tokens: 7909
- judge_score: 4.6 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Resume el siguiente reporte trimestral en formato ejecutivo (max 200 palabras):

REPORTE Q1 2026 - EMPRESA TECHFLOW

VENTAS: Las ventas totales alcanzaron $2.3M, un incremento del 18% respecto a Q4 2025 ($1.95M). El segmento enterprise crecio 32% impulsado por 3 contratos nuevos con Fortune 500. El segmento SMB se mantuvo plano con una ligera caida del 2%. Las ventas internacionales representaron el 28% del total, arriba del 22% del trimestre anterior, con fuerte traccion en LATAM y Europa.

PRODUCTO: Se lanzaron 47 features nuevas, incluyendo el modulo de IA predictiva que ya tiene 120 clientes activos. El uptime fue 99.97%. Se resolvieron 234 tickets de soporte con un tiempo promedio de 4.2 horas. El NPS subio de 42 a 48. Se identificaron problemas de rendimiento en el modulo de reportes que afectan al 8% de los usuarios enterprise.

EQUIPO: Se contrataron 12 personas (5 engineering, 3 sales, 2 CS, 2 marketing). La rotacion fue del 4% (2 personas). Se completo la migracion a trabajo hibrido con 60% remoto. La encuesta de satisfaccion dio 4.1/5.

FINANZAS: El burn rate mensual es $380K. El runway actual es 14 meses. Los unit economics mejoraron: CAC bajo de $1,200 a $980, LTV subio a $8,400. El margen bruto es 72%.

RIESGOS: 1) Dependencia de AWS (85% de infra) 2) Competidor DirectFlow levanto $50M Serie B 3) Regulacion de datos EU puede requerir cambios en arquitectura.

El resumen debe incluir: metricas clave, logros, preocupaciones, y proximos pasos recomendados.


## Respuesta completa

**Resumen Ejecutivo Q1 2026 – TechFlow**

**Métricas clave:** ventas $2.3M (+18% vs Q4 2025); enterprise +32% (3 Fortune 500); SMB -2%; internacional 28% (desde 22%, con tracción en LATAM/Europa); margen bruto 72%; burn rate $380K/mes; runway 14 meses; CAC $980 (-18%) y LTV $8,400 (ratio ~8.6x).

**Logros:** lanzamiento de 47 features y módulo de IA predictiva (120 clientes); uptime 99.97%; NPS 42→48; 234 tickets resueltos (4.2h); 12 contrataciones (5 eng, 3 sales, 2 CS, 2 marketing), rotación 4% y modelo híbrido (60% remoto, satisfacción 4.1/5).

**Preocupaciones:** rendimiento en reportes afecta al 8% de usuarios enterprise; dependencia de AWS (85%); competidor DirectFlow con $50M Serie B; regulación UE de datos podría exigir cambios de arquitectura; SMB estancado.

**Próximos pasos:** 1) escalar IA predictiva y expansión internacional/enterprise; 2) optimizar módulo de reportes y diversificar infraestructura; 3) reactivar SMB y adecuar arquitectura a normativa UE; 4) preservar eficiencia para ampliar runway.