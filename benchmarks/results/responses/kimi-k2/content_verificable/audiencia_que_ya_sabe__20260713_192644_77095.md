# Kimi K2 — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.91 | quality: 10.0
- latency_total: 13.58s | tokens_per_second: 33.1
- input_tokens: 121 | output_tokens: 450
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**Cuando el check verde te miente**

El peor bug es el que no parece bug.

Tu workflow devuelve 200 OK. El log dice "Success". Pero el registro no existe en la base de datos. El email nunca salió. El archivo sigue en S3.

¿Por qué? Porque n8n ejecutó *correctamente* una rama que no hacía lo que creías.

**Los modus operandi más comunes:**

- **El IF fantasma.** Condición que nunca pasa a true, pero tampoco dispara error. El workflow sigue feliz por la rama "false" y termina sin quejarse.
- **El nodo silencioso.** HTTP Request con "Continue on Fail" activado. Devuelve 404, n8n sonríe.
- **El merge perdido.** Dos ramas que nunca se juntan. Una ejecuta, la otra se queda esperando. El workflow "termina" porque no hay más nodos en esa rama.

**Cómo detectarlo antes de que te des cuenta en producción:**

1. **Assertions explícitos.** Después de operaciones críticas, un nodo Set que verifique `{{ $json.id !== undefined }}`. Si falla, dispara error intencionalmente.

2. **Monitoreo de volumen, no de estado.** Un workflow que siempre procesa 1.200 registros de repente procesa 0. Las métricas de negocio detectan lo que los logs no dicen.

3. **Smoke tests con datos conocidos.** Inyecta un registro de prueba identificable cada hora. Si no aparece donde debe, alerta.

El check verde es tu enemigo cuando confías ciegamente. Diseña para que falle ruidosamente cuando algo va mal, no para que siga en silencio.

---

*¿Te ha pasado? Responde con tu historia de "success" más traumática.*