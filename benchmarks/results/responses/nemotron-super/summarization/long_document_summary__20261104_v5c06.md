# Nemotron 3 Super — summarization/long_document_summary

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.16 | quality: 7.8
- latency_total: 1.545s | tokens_per_second: 181.9
- input_tokens: 486 | output_tokens: 281
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, proporcionando insights útiles y estructurados, aunque no profundiza en todos los aspectos del informe original.

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

**Reporte Ejecutivo Q1 2026 – TechFlow**

**Métricas clave:** Ventas de $2.3M (+18% vs. Q4 2025), margen bruto 72%, burn rate $380K/mes, runway 14 meses, CAC $980, LTV $8,400, NPS 48 y uptime 99.97%.

**Logros:** Crecimiento del segmento Enterprise (+32%) con 3 contratos Fortune 500; expansión internacional al 28% de ventas; lanzamiento de 47 features, incluido IA predictiva con 120 clientes activos; mejora en unit economics y satisfacción del equipo (4.1/5).

**Preocupaciones:** Rendimiento del módulo de reportes afecta al 8% de usuarios Enterprise; dependencia de AWS (85% de infraestructura); ronda de $50M del competidor DirectFlow; y posible impacto de regulación de datos en la UE.

**Próximos pasos:** Priorizar corrección de rendimiento en reportes; diversificar proveedores de nube; acelerar cumplimiento normativo UE; y monitorear movimiento competitivo de DirectFlow para ajustar estrategia de precios y retención.