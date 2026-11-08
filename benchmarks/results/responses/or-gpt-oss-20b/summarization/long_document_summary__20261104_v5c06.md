# GPT-OSS 20B — summarization/long_document_summary

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.13 | quality: 9.4
- latency_total: 4.654s | tokens_per_second: 104.0
- input_tokens: 464 | output_tokens: 484
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando un resumen conciso y detallado con insights estratégicos.

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

**Resumen Ejecutivo – Q1 2026 (TechFlow)**  

**Métricas Clave**  
- **Ventas**: $2.3 M (+18 % vs. Q4 2025). Enterprise +32 % (3 contratos Fortune 500). SMB estable (+ 2 % caída). Ventas internacionales 28 % (↑ 6 pp).  
- **Producto**: 47 nuevas features; módulo IA predictiva con 120 clientes activos. Uptime 99.97 %. 234 tickets resueltos, 4.2 h promedio. NPS 48 (+6 pts). Problemas de rendimiento en reportes afectan 8 % de enterprise.  
- **Equipo**: +12 hires (5 eng, 3 sales, 2 CS, 2 marketing). Rotación 4 % (2 personas). 60 % remoto. Encuesta satisfacción 4.1/5.  
- **Finanzas**: Burn $380 K/mes, runway 14 meses. CAC $980 (↓ $220), LTV $8,400, margen bruto 72 %.  

**Logros**  
- Aceleración de crecimiento enterprise y expansión internacional (LATAM, Europa).  
- Lanzamiento de IA predictiva y mejora del NPS.  
- Completar transición a trabajo híbrido y fortalecer la cultura laboral.  

**Preocupaciones**  
1. Dependencia del 85 % de infra en AWS.  
2. Competidor DirectFlow recaudó $50 M Serie B.  
3. Nueva regulación EU de datos que podría requerir re‑arquitectura.  

**Próximos Pasos**  
- Diversificar infra (multi‑cloud) y plan de contingencia.  
- Escalar el módulo IA y resolver el problema de reportes antes del Q3.  
- Evaluar impacto de la regulación EU y actualizar roadmap de compliance.  
- Intensificar go‑to‑market en SMB con campañas de valor agregado.  
- Mantener el ritmo de hires en ingeniería y CS para soportar el crecimiento.