# Seed 2.1 Turbo — agent_long_horizon/skill_dependency_chain

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: False  | final: 1.83 | quality: 0.0
- latency_total: 20.626s | tokens_per_second: 0
- input_tokens: 653 | output_tokens: 945
- error: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'bytedance-seed/seed-2-1-turbo is temporarily rate-limited upstream. Please retry shortly, or add yo...

## Conversación completa (3 turnos)

### Turno 1 — usuario

Necesito el siguiente flujo completo: (1) consulta la DB para obtener las ventas del mes pasado por categoría, (2) genera un reporte PDF con esos datos, (3) guárdalo en /reports/sales_monthly.pdf, y (4) envíalo por email al gerente comercial (gerente@empresa.com). Hazlo todo en orden.

### Turno 1 — modelo

TOOL: query_database("SELECT c.nombre AS categoria, SUM(v.monto_total) AS total_ventas, COUNT(v.id_venta) AS cantidad_ventas FROM ventas v JOIN productos p ON v.id_producto = p.id_producto JOIN categorias c ON p.id_categoria = c.id_categoria WHERE v.fecha_venta >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month') AND v.fecha_venta < DATE_TRUNC('month', CURRENT_DATE) GROUP BY c.nombre ORDER BY total_ventas DESC;")

### Turno 2 — usuario

TOOL_RESULT (query_database): [{categoria: 'electronica', ventas: 145000}, {categoria: 'hogar', ventas: 87000}, {categoria: 'moda', ventas: 64000}]

### Turno 2 — modelo

TOOL: generate_report(data=[{"categoria": "electronica", "ventas": 145000}, {"categoria": "hogar", "ventas": 87000}, {"categoria": "moda", "ventas": 64000}], format="pdf")

### Turno 3 — usuario

TOOL_RESULT (generate_report): Reporte generado correctamente. Tamaño 2.4MB, 8 páginas, formato PDF. Contenido en variable report_pdf_bytes (base64 omitido).

### Turno 3 — modelo

Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'bytedance-seed/seed-2-1-turbo is temporarily rate-limited upstream. Please retry shortly, or add yo...


## Respuesta completa

Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'bytedance-seed/seed-2-1-turbo is temporarily rate-limited upstream. Please retry shortly, or add yo...