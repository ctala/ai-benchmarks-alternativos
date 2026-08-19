# Sakana Namazu — content_verificable/audiencia_que_ya_sabe

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 8.43s | tokens_per_second: 211.9
- input_tokens: 120 | output_tokens: 1786

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

El peor bug en n8n no es el que pinta de rojo el execution. Es el que se queda verde.

Tu workflow acaba de marcar "Success", pero el registro no aparece en la base de datos, el lead no recibió el correo y la factura sigue sin generarse. ¿Qué pasó? Nada. Y eso es exactamente el problema.

En n8n, "Success" significa únicamente que ningún nodo lanzó un error de ejecución. No garantiza que tus condiciones IF hayan dejado pasar items, que el HTTP Request haya devuelto datos útiles ni que un nodo anterior no haya salido con un array vacío. Si tienes activado "Continue On Fail", incluso una respuesta errónea de una API puede pintar de verde la rama. Para la plataforma, todo bien. Para el negocio, fue un día sin operaciones.

Para detectar el "success fantasma", deja de confiar en el estado del execution y empieza a medir el volumen de items. Inserta nodos Set o Code después de filtros y APIs para contar y comparar: si entran cincuenta items a un IF y cero salen por la rama "true" durante más tiempo del esperado, tu alarma debe saltar. Configura nodos Stop and Error cuando una respuesta HTTP devuelva un body vacío pero el status sea 200. Usa un workflow paralelo de auditoría que lea tus execution logs vía API y alerte cuando detecte ejecuciones con cero operaciones de escritura en tus nodos críticos.

Monitoriza la tasa de items procesados, no el color del status. Un gráfico plano en cero es más peligroso que uno con picos rojos.