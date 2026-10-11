# Investigación: Cuelgue SSL en Qwen 3.8 Omni Flash y Bonsai 2 27B

**Fecha:** 10 octubre 2026  
**Tiempo invertido:** ~10 minutos  
**Costo:** <$0.20  
**Estado:** DOCUMENTADO, no resuelto  

## Síntoma

Los benchmarks de `qwen3.8-omni-flash` y `bonsai-2-27b` se cuelgan indefinidamente durante la ejecución, quedando los procesos en estado `do_poll.constprop.0` (polling SSL/socket a nivel kernel).

## Datos

- **Qwen 3.8 Omni Flash:** 114/213 tests completados (53%) antes del cuelgue
- **Bonsai 2 27B:** 105/213 tests completados (49%) antes del cuelgue
- **Suites completadas:** 27/35 (Qwen), 24/35 (Bonsai)
- **Archivos de respuesta preservados:** sí, en `benchmarks/results/responses/`

## Configuración Actual

- **HTTP_READ_TIMEOUT_S:** 360.0s (6 minutos) en `providers/adapters.py`
- **Provider:** OpenRouter
- **Streaming:** habilitado (default)

## Posibles Causas

1. **Routing de OpenRouter:** el modelo se rutea a un proveedor upstream que tiene latencia extrema o cuelgues intermitentes
2. **Handshake SSL/TLS:** el handshake se cuelga antes de que el read timeout aplique
3. **Modelo específico:** ambos modelos comparten alguna característica (multimodal, tamaño, proveedor upstream) que trigger un bug
4. **Socket timeout faltante:** el httpx timeout podría no estar aplicándose correctamente a nivel de socket

## Intentos de Solución NO Implementados

Por restricción de tiempo (45 min) y presupuesto ($1), NO se probaron:

- ❌ Desactivar streaming (`stream=False`)
- ❌ Forzar otro provider via OpenRouter provider routing
- ❌ Socket timeout a nivel TCP (`SO_RCVTIMEO`)
- ❌ Correr tests de a uno con subprocess timeout
- ❌ Probar con timeout más agresivo (<60s)
- ❌ Probar directamente contra provider upstream (sin OpenRouter)

## Recomendación

**SKIP estos modelos por ahora.** Los 209 runs restantes (99 + 108 + Harbor) cuestan ~$1.07 pero el tiempo de investigación excede el presupuesto de la sesión. 

### Opciones futuras:

1. **Contactar a OpenRouter:** reportar el modelo_id específico que causa el hang
2. **Probar en diferido:** con un runner que mate procesos colgados después de N minutos
3. **Medir con otro provider:** si Qwen/Bonsai están en APIs directas que no exhiban el bug

## Logs Relevantes

Los últimos runs exitosos fueron del 26 de septiembre 2026 (`benchmark_20260926_093952_86790`). Las respuestas completas están preservadas y muestran que ambos modelos **funcionan correctamente** cuando no se cuelgan.

---

**Decisión:** pasar a implementar las 5 suites de noticias (prioridad inmediata) y retomar Qwen/Bonsai en sesión futura con más tiempo.
