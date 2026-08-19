# Nex-N2-Mini — agent_long_horizon/skill_dependency_chain

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 4.85s | tokens_per_second: 98.0
- input_tokens: 2026 | output_tokens: 424

## Conversación completa (5 turnos)

### Turno 1 — usuario

Necesito el siguiente flujo completo: (1) consulta la DB para obtener las ventas del mes pasado por categoría, (2) genera un reporte PDF con esos datos, (3) guárdalo en /reports/sales_monthly.pdf, y (4) envíalo por email al gerente comercial (gerente@empresa.com). Hazlo todo en orden.

### Turno 1 — modelo

TOOL: query_database(sql="SELECT categoria, SUM(ventas) AS ventas_mes_pasado FROM ventas WHERE fecha >= DATE_SUB((SELECT MAX(fecha) FROM ventas), INTERVAL 1 MONTH) AND fecha < (SELECT MAX(fecha) FROM ventas) GROUP BY categoria ORDER BY ventas_mes_pasado DESC;")

### Turno 2 — usuario

TOOL_RESULT (query_database): [{categoria: 'electronica', ventas: 145000}, {categoria: 'hogar', ventas: 87000}, {categoria: 'moda', ventas: 64000}]

### Turno 2 — modelo

TOOL: generate_report(data=[{categoria: 'electronica', ventas_mes_pasado: 145000}, {categoria: 'hogar', ventas_mes_pasado: 87000}, {categoria: 'moda', ventas_mes_pasado: 64000}], format='pdf')

### Turno 3 — usuario

TOOL_RESULT (generate_report): Reporte generado correctamente. Tamaño 2.4MB, 8 páginas, formato PDF. Contenido en variable report_pdf_bytes (base64 omitido).

### Turno 3 — modelo

TOOL: save_file(path='/reports/sales_monthly.pdf', content=report_pdf_bytes)

### Turno 4 — usuario

TOOL_RESULT (save_file): Archivo guardado en /reports/sales_monthly.pdf (2.4MB)

### Turno 4 — modelo

TOOL: send_email(to='gerente@empresa.com', subject='Reporte mensual de ventas por categoría', body='Hola, adjunto el reporte mensual de ventas por categoría correspondiente al mes pasado. Saludos.', attachment_path='/reports/sales_monthly.pdf')

### Turno 5 — usuario

TOOL_RESULT (send_email): Email enviado a gerente@empresa.com con adjunto /reports/sales_monthly.pdf

### Turno 5 — modelo

Flujo completado correctamente:

1. Se consultaron las ventas del mes pasado por categoría.
2. Se generó el reporte PDF con esos datos.
3. Se guardó en `/reports/sales_monthly.pdf`.
4. Se envió por email al gerente comercial en `gerente@empresa.com` con el adjunto correspondiente.


## Respuesta completa

Flujo completado correctamente:

1. Se consultaron las ventas del mes pasado por categoría.
2. Se generó el reporte PDF con esos datos.
3. Se guardó en `/reports/sales_monthly.pdf`.
4. Se envió por email al gerente comercial en `gerente@empresa.com` con el adjunto correspondiente.