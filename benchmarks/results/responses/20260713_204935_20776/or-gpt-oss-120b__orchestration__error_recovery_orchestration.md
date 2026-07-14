# GPT-OSS 120B — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.95 | quality: 7.5
- latency_total: 1.661s | tokens_per_second: 433.5
- input_tokens: 614 | output_tokens: 720
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una planificación detallada y bien estructurada para manejar el error, proporcionando alternativas prácticas y pasos claros que un emprendedor podría implementar directamente.

## Respuesta completa

**Diagnóstico del fallo**  
- El intento de consultar la base de datos **production** falló porque el servidor está bajo mantenimiento y rechaza conexiones.  
- El mensaje de error indica que la recuperación está prevista en **2 horas**, lo que no nos permite cumplir el plazo de las 5 pm.

**Propuesta de alternativa**  
1. **Intentar con la réplica de respaldo**: normalmente disponemos de una base de datos de solo‑lectura llamada **sales_backup** que contiene los datos sincronizados con un retraso de pocos minutos.  
2. **Si la réplica tampoco está disponible**, buscar un archivo exportado recientemente (por ejemplo, `/data/sales_last_month.csv`) que suele generarse al final de cada mes como respaldo.  
3. **Como último recurso**, solicitar al equipo de operaciones que nos proporcione un dump rápido o que habilite temporalmente un acceso de solo lectura al entorno de producción.

**Plan ajustado para cumplir el deadline (antes de las 5 pm)**  

| Paso | Acción | Herramienta | Comentario |
|------|--------|-------------|------------|
| 1 | Consultar la réplica **sales_backup** para obtener los registros del mes pasado. | `query_database` (base de datos: `sales_backup`) | Si tiene éxito, pasamos al paso 3. |
| 2a | Si la réplica falla, leer el CSV de respaldo. | `read_file` (`/data/sales_last_month.csv`) | El CSV contiene las mismas columnas que la tabla `sales`. |
| 2b | Si el CSV no está disponible, enviar un email al equipo de operaciones pidiendo acceso temporal o un dump. | `send_email` | Asunto: *Urgente – Acceso a datos de ventas*; cuerpo explicando la urgencia y solicitando entrega antes de las 5 pm. |
| 3 | Generar un resumen (total ventas, desglose por categoría, tendencias principales). | `run_script` (Python) | El script tomará los datos obtenidos en el paso 1 o 2a y producirá un texto breve y una tabla. |
| 4 | Enviar el resumen al equipo. | `send_email` (con cuerpo del resumen, posible adjunto CSV) | Destinatario: `equipo@empresa.com`; asunto: *Resumen de ventas del mes pasado*; cuerpo con los puntos clave. |

**Próximos pasos**  

Voy a intentar la primera alternativa: consultar la réplica **sales_backup**. Si recibo otro error, pasaré inmediatamente a leer el CSV y, si eso también falla, notificaré a operaciones.  

---  

Ejecutando la consulta en la réplica…  