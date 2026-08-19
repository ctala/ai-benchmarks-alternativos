# Seed 2.0 Code — ocr_extraction/business_card_extraction

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 36.218s | tokens_per_second: 56.5
- input_tokens: 294 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un sistema de OCR. Extraes informacion de contacto de tarjetas de presentacion.

**user:**

Tengo una tarjeta de presentacion que dice:

Lado frontal:
  MARIA JOSE RODRIGUEZ SOTO
  Chief Technology Officer

  NexaFlow Intelligence
  "Transforming Data into Decisions"

  +56 9 8765 4321
  mj.rodriguez@nexaflow.ai
  linkedin.com/in/mjrodriguez

Lado trasero:
  Av. Apoquindo 4500, Piso 12
  Las Condes, Santiago, Chile
  www.nexaflow.ai

Extrae la informacion en este formato JSON exacto:
{
  "nombre_completo": "",
  "cargo": "",
  "empresa": "",
  "slogan": "",
  "telefono": "",
  "email": "",
  "linkedin": "",
  "direccion": "",
  "ciudad": "",
  "pais": "",
  "website": ""
}

Solo el JSON, nada mas.


## Respuesta completa


El usuario quiere el JSON exacto con la información de la tarjeta. Primero, voy a extraer cada campo:

1. nombre_completo: MARIA JOSE RODRIGUEZ SOTO (está claro en el frente)
2. cargo: Chief Technology Officer (directo)
3. empresa: NexaFlow Intelligence (el nombre de la empresa)
4. slogan: Transforming Data into Decisions (sin las comillas? Wait, mira, el texto dice "Transforming Data into Decisions" con comillas, pero voy a ver: el slogan es el contenido, pero si las comillas son parte del formato, no, espera, en la tarjeta es el eslogan entre comillas, pero el valor es el texto. Wait no, mejor extraer tal cual pero sin las comillas? No, espera, mira el dato: el eslogan es "Transforming Data into Decisions", pero cuando lo pongo en el string JSON, no necesitamos las comillas internas a menos que sean parte, pero no, las comillas son para resaltar el eslogan. Wait, no, mejor extraer exactamente el contenido: el eslogan es Transforming Data into Decisions? O con comillas? Wait, no, en la tarjeta, el texto entre comillas es el eslogan, así que el valor del campo slogan es "Transforming Data into Decisions"? No, no, porque en JSON los strings van entre comillas, así que si el eslogan tiene comillas, habría que escaparlas, pero wait, mira el usuario puso en el lado frontal: "Transforming Data into Decisions" — son comillas de resalte, no parte del eslogan. Wait, mejor ver todos los campos uno por uno:

- nombre_completo: MARIA JOSE RODRIGUEZ SOTO (correcto)
- cargo: Chief Technology Officer (correcto)
- empresa: NexaFlow Intelligence (correcto)
- slogan: Transforming Data into Decisions (quitando las comillas de resalte, o no? Wait, si el usuario lo escribió con comillas, pero tal vez son parte del formato de la tarjeta, no del contenido. Wait, no, mejor chequear el resto:
- telefono: +56 9 8765 4321 (correcto)
- email: mj.rodriguez@nexaflow.ai (correcto)
- linkedin: linkedin.com/in/mjrodriguez (correcto)
- direccion: Av. Apoquindo 4500, Piso 12 (lado trasero)
- ciudad: Santiago (porque Las Condes es una comuna de Santiago, Chile; wait, el lado trasero dice: Av. Apoquindo 4500, Piso 12 | Las Condes, Santiago, Chile. Entonces:
  - direccion: Av. Apoquindo 4500, Piso 12
  - ciudad: Santiago (o Las Condes? Wait, no, Las Condes es una comuna de la ciudad de Santiago, Chile. Pero vamos a extraer tal cual está estructurado: el lado trasero tiene tres líneas:
    1. Av. Apoquindo 4500, Piso 12 (dirección)
    2. Las Condes, Santiago, Chile (comuna, ciudad, país)
  Entonces:
  - direccion: Av. Apoquindo 4500, Piso 12
  - ciudad: Santiago
  - pais: Chile
  - pero wait, Las Condes? No, porque el campo es ciudad, Santiago es la ciudad. Luego el website: www.nexaflow.ai (correcto)

Ahora, armar el JSON exactamente como el formato que pide, sin nada más. Vamos a ver si todos los campos están:

Wait, el slogan: el texto está entre comillas, pero en el JSON, si lo ponemos sin comillas, o con? Wait, no, las comillas en la tarjeta son para marcar el eslogan, no parte del texto. Así que slogan es "Transforming Data into Decisions"? No, no, en JSON el string es el valor, así que:

Wait, vamos a escribir cada campo con el valor EXACTO extraído:

1. nombre_completo: "MARIA JOSE RODRIGUEZ SOTO" (todo en mayúsculas, tal cual)
2. cargo: "Chief Technology Officer" (tal cual)
3. empresa: "NexaFlow Intelligence" (tal cual)
4. slogan: "Transforming Data into Decisions" (quitando las comillas de resalte, porque son parte del diseño de la tarjeta, no del contenido del eslogan; si las pusiera, tendría que escaparlas: "\"Transforming Data into Decisions\"", pero no, es mejor extraer el contenido sin las comillas de resalte)
5. telefono: "+56 9 8765 4321" (tal cual)
6. email: "mj.rodriguez@nexaflow.ai" (tal cual)
7. linkedin: "linkedin.com/in/mjrodriguez" (tal cual)
8. direccion: "Av. Apoquindo 4500, Piso 12" (tal cual del lado trasero)
9. ciudad: "Santiago" (porque en el lado trasero es Las Condes, Santiago, Chile; Las Condes es comuna, Santiago es ciudad)
10. pais: "Chile" (tal cual)
11. website: "www.nexaflow.ai" (tal cual)

Wait, pero ¿y Las Condes? El campo es ciudad, no comuna. El usuario pide ciudad, así que Santiago es correcto. Ahora, armar el JSON sin espacios extra, exactamente como el formato que pide, sin ningún texto adicional.

Vamos a verificar el formato que el usuario dio: es un JSON con esos 11 campos, cada uno un string vacío, hay que rellenarlos.

Ahora, escribirlo correctamente, sin errores de sintaxis:

{
  "nombre_completo": "MARIA JOSE RODRIGUEZ SOTO",
  "cargo": "Chief Technology Officer",
  "empresa": "NexaFlow Intelligence",
  "slogan": "Transforming Data into Decisions",
  "telefono": "+56 9 8765 4321",
  "email": "mj.rodriguez@nexaflow.ai",
  "linkedin": "linkedin.com/in/mjrodriguez",
  "direccion": "Av. Apoquindo 4500, Piso 12",
  "ciudad": "Santiago",
  "pais": "Chile",
  "website": "www.nexaflow.ai"
}

Wait, ¿el slogan debería tener las comillas? El usuario escribió en el lado frontal: "Transforming Data into Decisions" — con comillas. Pero si lo ponemos en el JSON, tendríamos que escaparlas, por ejemplo: "\"Transforming Data into Decisions\"". Pero ¿son parte del eslogan o solo resalte? En tarjetas de presentación, los eslóganes suelen ir entre comillas como resalte, no como parte del texto. Pero para estar seguro, vamos a ver: si el usuario lo escribió con comillas, tal vez quiera que se incluyan? Wait, no, porque en el ejemplo de formato, el slogan es un string vacío. Vamos a pensar: si el eslogan es "Transforming Data into Decisions" (con comillas), entonces en JSON es "\"Transforming Data into Decisions\"". Pero tal vez el usuario puso las comillas para indicar que es el eslogan, no que forman parte del texto.

Wait, otra cosa: la ciudad. El lado trasero dice "Las Condes, Santiago, Chile". Las Condes es una comuna de la Región Metropolitana de Santiago, Chile. Entonces, la ciudad es Santiago, la comuna es Las Condes. Pero el campo es "ciudad", así que Santiago es correcto. Si el campo fuera "comuna", sería Las Condes, pero no.

Otra verificación: todos los campos están rellenados, no hay campos vacíos. ¿Hay algún dato que falte? No, todos los datos de la tarjeta están distribuidos en los campos.

Wait, el teléfono: +56 9 8765 4321 — correcto, tal cual está.

Email: mj.rodriguez@nexaflow.ai — correcto.

LinkedIn: linkedin.com/in/mjrodriguez — correcto, sin el https://? Tal cual está en la tarjeta, sí, porque la tarjeta no tiene https://, así que lo ponemos tal cual.

Dirección: Av. Apoquindo 4500, Piso 12 — correcto, tal cual del lado trasero.

Ciudad: Santiago — correcto.

País: Chile