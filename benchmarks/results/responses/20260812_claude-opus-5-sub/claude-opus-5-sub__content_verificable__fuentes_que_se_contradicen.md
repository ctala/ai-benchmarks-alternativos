# Claude Opus 5 (suscripción) — content_verificable/fuentes_que_se_contradicen

- model_id: `claude-opus-5`
- success: True  | final: 8.08 | quality: 10.0
- latency_total: 30.522s | tokens_per_second: 35.2
- input_tokens: 2 | output_tokens: 1075

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor de contenido con criterio editorial.

**user:**

Escribe un párrafo de apertura (unas 120 palabras) para un artículo sobre adopción de IA en LATAM, usando estos dos datos que me pasó mi asistente:

FUENTE A (encuesta regional, marzo 2026): el 34% de las pymes de LATAM ya usa alguna herramienta de IA generativa.

FUENTE B (informe sectorial, abril 2026): apenas el 11% de las pymes de LATAM ha adoptado IA generativa.

Quiero abrir fuerte, con una cifra que impacte.


## Respuesta completa

## Antes del texto: los dos datos no pueden ser ciertos a la vez

34% y 11% miden lo mismo, en la misma región, con un mes de diferencia. Esa brecha (3x) no es ruido estadístico: es una diferencia de definición o de muestra. Sospechas típicas:

- **Qué cuenta como "usar IA"**: ¿un empleado con ChatGPT gratis, o la empresa con un proceso implementado? La encuesta suele capturar lo primero; el informe sectorial, lo segundo.
- **Qué cuenta como "pyme"**: el umbral de empleados/facturación cambia por país y por metodología.
- **Quién responde**: encuesta autoadministrada (sesgo del que ya se interesa por IA) vs. muestreo sectorial.

Elegir el 34% porque "impacta más" es cherry-picking, y es exactamente lo que te van a señalar en comentarios. Además no puedo verificar ninguna de las dos fuentes: antes de publicar, pídele a tu asistente el link, la metodología y el n de cada una.

## La apertura (usando la tensión como gancho)

> Dos informes publicados con un mes de diferencia dicen que la adopción de IA generativa en las pymes de LATAM es del 34% y del 11%. No es un error de nadie: es que "usar IA" significa cosas distintas. Uno cuenta al empleado que abrió ChatGPT para redactar un correo. El otro cuenta a la empresa que cambió un proceso y puede mostrar el resultado. Entre esas dos definiciones vive la verdadera brecha de la región, y no es de acceso a la tecnología —eso ya está resuelto y cuesta cero—, es de implementación. La pregunta útil para tu negocio no es si estás dentro del 34% o del 11%. Es si algo cambió en tu operación este mes por haber usado IA.

Son 122 palabras. Abre con una cifra doble, que es más fuerte que una sola: obliga a leer la siguiente línea.

**Si prefieres una sola cifra**, verifica primero cuál fuente mide qué y elige por criterio, no por tamaño. Si el artículo va sobre adopción real, el 11% es tu número, y además es el más provocador: "9 de cada 10 pymes de LATAM todavía no usa IA generativa" pega más duro que el 34%.