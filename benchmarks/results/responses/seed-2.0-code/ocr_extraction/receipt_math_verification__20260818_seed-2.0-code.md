# Seed 2.0 Code — ocr_extraction/receipt_math_verification

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.64 | quality: 8.75
- latency_total: 39.048s | tokens_per_second: 52.4
- input_tokens: 409 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo un recibo de restaurante:

===============================
  RESTAURANTE EL PARRILLERO
  Av. Italia 1890, Nunoa
  Boleta N° 0082341
  Fecha: 12/04/2026 21:45
===============================
Mesa: 7          Mesero: Carlos

2x Lomo vetado         $18.900 c/u
1x Ensalada cesar      $7.500
3x Pisco sour          $6.900 c/u
1x Postre brownie      $5.800
1x Agua mineral 1.5L   $3.200

-------------------------------
Subtotal:              $73.000
Propina sugerida (10%): $7.300
-------------------------------
TOTAL:                 $80.300
===============================
Pago: Tarjeta credito ****4521

Tareas:
1. Extrae todos los items con sus precios en JSON
2. Verifica si el subtotal esta correcto sumando los items
3. Verifica si la propina esta bien calculada
4. Indica si hay algun error en los calculos

Responde en JSON con formato:
{
  "items": [...],
  "subtotal_facturado": 0,
  "subtotal_calculado": 0,
  "subtotal_correcto": true/false,
  "propina_correcta": true/false,
  "total_correcto": true/false,
  "errores": []
}


## Respuesta completa


El usuario quiere que procese el recibo del restaurante, haga las tareas y devuelva el JSON como pide. Primero, voy a extraer los items bien:
Primero, los items:
1. 2x Lomo vetado: cantidad 2, nombre "Lomo vetado", precio unitario 18900 (quitar los puntos, porque son separadores de miles en CLP? Wait, el recibo usa $18.900 c/u, entonces en números es 18900, no? Porque en Chile el punto es separador de miles, coma decimal. Pero los montos son enteros, así que hay que quitar los puntos para calcular.

Primero, extraer cada item:
- Cantidad 2, nombre "Lomo vetado", precio_unitario 18900, total_item: 2*18900=37800
- Cantidad 1, "Ensalada cesar", precio_unitario 7500, total_item 7500
- Cantidad 3, "Pisco sour", precio_unitario 6900, total_item 3*6900=20700
- Cantidad 1, "Postre brownie", 5800, total 5800
- Cantidad 1, "Agua mineral 1.5L", 3200, total 3200

Ahora calcular subtotal_calculado: sumar todos los total_items: 37800 +7500=45300, +20700=66000, +5800=71800, +3200=75000? Wait wait, wait el recibo dice Subtotal $73.000. Oh, hay un error aquí.

Wait vamos a calcular de nuevo, paso por paso, sin errores:

1. Lomo vetado: 2 unidades * 18900 = 37800
2. Ensalada César: 1 *7500=7500 → acumulado 45300
3. Pisco sour: 3 *6900=20700 → 45300 +20700=66000
4. Postre brownie: 5800 → 66000+5800=71800
5. Agua mineral: 3200 → 71800+3200=75000. Oh! El subtotal facturado es 73000, pero el calculado es 75000. Así que subtotal_correcto es false.

Luego, propina sugerida es 10% del subtotal facturado? O del calculado? El recibo dice propina sugerida 10% del subtotal (el facturado, $73000 → 10% es 7300, que es lo que pone. Pero si el subtotal es incorrecto, la propina está calculada sobre el subtotal erróneo. Wait, la tarea 3 es verificar si la propina está bien calculada: ¿sobre el subtotal facturado o el correcto? El enunciado de la tarea 3 dice "verifica si la propina esta bien calculada" → según el recibo, la propina es 10% del subtotal (el que dice el recibo). Pero primero, vamos a ver:

Subtotal facturado: 73000 → 10% es 7300, que es lo que pone. Pero el subtotal correcto es 75000, así que la propina correcta sería 7500, pero la tarea 3 es ver si la propina está calculada como 10% del subtotal facturado? Wait, el recibo dice "Propina sugerida (10%): $7.300" → el 10% de $73.000 es $7.300, así que la propina está bien calculada SOBRE EL SUBTOTAL FACTURADO, PERO el subtotal es incorrecto.

Luego el total facturado es 80300, que es 73000 +7300=80300, pero el total correcto sería 75000 +7500=82500? Wait no, la tarea 4 es indicar errores en los cálculos.

Ahora, vamos a estructurar el JSON:

Primero, los items: cada item debe tener? El formato de items: ¿qué campos? El usuario dijo "extrae todos los items con sus precios en JSON". Entonces cada item debería tener cantidad, nombre, precio_unitario, total_item? O como? Wait el formato de respuesta tiene "items": [...], así que cada item puede ser un objeto con, por ejemplo:
{
  "cantidad": 2,
  "nombre": "Lomo vetado",
  "precio_unitario": 18900,
  "total_item": 37800
}

Sí, porque es necesario para calcular el subtotal.

Ahora, subtotal_facturado es 73000 (lo que dice el recibo, sin el punto, como número entero).

subtotal_calculado es 75000, como lo calculamos.

subtotal_correcto es false, porque 73000 ≠75000.

Propina_correcta: ¿qué? El recibo dice que es 10% del subtotal facturado. El 10% de 73000 es 7300, que es lo que pone. Pero si el subtotal es incorrecto, ¿la propina está bien calculada según el recibo? O según el subtotal correcto? El enunciado de la tarea 3: "Verifica si la propina esta bien calculada" → probablemente, se refiere a si es el 10% del subtotal que figura en el recibo, porque es lo que indica la boleta. Pero wait, vamos a leer el recibo otra vez: "Propina sugerida (10%): $7.300" → el 10% del subtotal (que es $73.000) es $7.300, así que la propina está calculada correctamente EN BASE AL SUBTOTAL FACTURADO, PERO el subtotal es erróneo.

Luego, total_correcto: el total facturado es 73000 +7300=80300, que es correcto si tomando el subtotal y propina del recibo, PERO el total correcto (si el subtotal fuera correcto sería 75000 +7500=82500, pero ¿qué es total_correcto? El formato de respuesta tiene "total_correcto": true/false. Probablemente, se refiere a si el total facturado es la suma del subtotal facturado más la propina facturada. Porque 73000 +7300=80300, que es lo que pone, así que total_correcto? O es el total correcto de todos los ítems más la propina correspondiente?

Wait, vamos a re-leer las tareas paso por paso:

Tareas:
1. Extrae todos los items con sus precios en JSON → cada item con cantidad, nombre, precio unitario, y tal vez total por item.
2. Verifica si el subtotal esta correcto sumando los items → suma de (cantidad * precio unitario) de cada item, comparado con el subtotal del recibo.
3. Verifica si la propina esta bien calculada → ¿qué base? El recibo dice "Propina sugerida (10%)" → 10% de qué? De la suma de los ítems, o del subtotal facturado? El recibo lo pone después del subtotal, así que es 10% del subtotal facturado. Pero si el subtotal es incorrecto, la propina está calculada sobre un monto erróneo, pero la operación de la propina (10% del subtotal facturado) es correcta? O la propina correcta sería 10% del subtotal calculado?
4. Indica si hay algun error en los calculos → errores como subtotal erróneo, etc.

Ahora, vamos a calcular de nuevo los montos sin errores:

Ítems:
1. 2x Lomo vetado: 2 * 18900 = 37800
2. 1x Ensalada cesar: 1 *7500 =7500
3. 3x Pisco sour:3*6900=20700
4