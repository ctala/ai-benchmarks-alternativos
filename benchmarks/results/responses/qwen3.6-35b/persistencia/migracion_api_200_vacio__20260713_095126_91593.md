# Qwen 3.6 35B base (OpenRouter FP8) — persistencia/migracion_api_200_vacio

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 6.62 | quality: 7.2
- latency_total: 50.73s | tokens_per_second: 40.4
- input_tokens: 270 | output_tokens: 2048

## Respuesta completa

HTTP 200 con body vacío no es un fallo de red ni de autenticación. Es un problema de **contexto de datos**: la API está ejecutando la consulta, pero el filtro implícito o la estructura del ID está descartando los registros.

Aplica estas vías en orden. Cada una es ejecutable y descartable en <5 minutos.

### 1. Desecha la concatenación de IDs
La v2 probablemente cambió el esquema de identificaciones. En v2, `{post_id}` suele ser el ID nativo de la publicación, no una composición de `account_id:post_id` o similar.
```bash
# Prueba primero con el ID exacto que usabas en v1 (sin concatenar)
curl -X GET "https://api.example.com/v2/posts/{post_id}/comments?limit=100" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```
Si devuelve datos, el problema era el formato del ID. Si sigue vacío, pasa al paso 2.

### 2. Fuerza los parámetros de query que la v2 exige por defecto
Las v2 suelen cambiar el comportamiento de paginación y expansión de recursos. Prueba esto:
```bash
curl -X GET "https://api.example.com/v2/posts/{post_id}/comments?include=author,body,status&limit=50&sort=created_at" \
  -H "Authorization: Bearer $TOKEN"
```
- `include=`: muchas APIs v2 no expanden relaciones por defecto y devuelven solo IDs.
- `limit=`: si no se envía, algunas APIs devuelven `0` por seguridad o rendimiento.
- `status=`: filtra por `published`, `active`, o `visible`. La v1 podía devolver todo; la v2 suele filtrar por defecto.

### 3. Espía la petición real de la interfaz web
La doc está incompleta, pero la UI ya consume la v2. Haz esto:
1. Abre DevTools → Network.
2. Filtra por `comments` o `posts`.
3. Encuentra la petición que carga los 40 comentarios.
4. Copia la URL exacta, headers y body.
5. Ejecuta `curl` con esa misma cadena.

Si la UI usa un endpoint como `/v2/comments?filter[post_id]=...` o `/v2/posts/{id}/threads/comments`, usa ese. La web es tu documentación de facto.

### 4. Verifica el scope del token
La v2 suele separar permisos por recurso. Un token que funcionaba en v1 puede carecer de `comments:read` o `posts:comments`.
- Pide a infra/API un token con scope `admin` o `full` temporalmente.
- Si con scope ampliado devuelve datos, tu token actual está recortado. Actualiza la generación del token o solicita el scope faltante al proveedor.

### 5. Ruta de contención (si el endpoint está roto o la doc es un espejo)
Si tras lo anterior sigue vacío:
- **Endpoint alternativo:** Prueba `GET /v2/comments