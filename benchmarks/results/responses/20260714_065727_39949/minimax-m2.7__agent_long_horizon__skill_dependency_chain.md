# MiniMax M2.7 — agent_long_horizon/skill_dependency_chain

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 21.448s | tokens_per_second: 34.9
- input_tokens: 3170 | output_tokens: 974

## Respuesta completa

✅ **Flujo completado exitosamente:**

| Paso | Acción | Resultado |
|------|--------|-----------|
| 1 | Consulta DB ventas por categoría | 3 categorías: Electrónica ($145K), Hogar ($87K), Moda ($64K) |
| 2 | Generar reporte PDF | 8 páginas, 2.4MB |
| 3 | Guardar archivo | `/reports/sales_monthly.pdf` ✓ |
| 4 | Enviar email | Enviado a gerente@empresa.com ✓ |

**Resumen:** El reporte muestra $296,000 en ventas totales del mes pasado, con Electrónica como categoría líder.