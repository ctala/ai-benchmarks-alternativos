# MiniMax M3 — persistencia/el_error_fue_mio_y_sigo

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.58 | quality: 6.26
- latency_total: 3.478s | tokens_per_second: 40.0
- input_tokens: 375 | output_tokens: 139

## Respuesta completa

¡Buen ojo con el `next`! Es un cursor opaco en base64, no un número de página.

El JSON decodificado es `{"offset": 20}`. Cada vez que recibes un lote, decodifica el `next` para saber el siguiente offset, y pídelo de nuevo con `?offset=20`, luego `?offset=40`, etc., hasta que `next` llegue como `null` o no aparezca.

No me había dado cuenta porque el `?page` asumía paginación indexada. Sigue hasta que te dé menos de 20 ítems, que ahí es donde se cortan los 400.