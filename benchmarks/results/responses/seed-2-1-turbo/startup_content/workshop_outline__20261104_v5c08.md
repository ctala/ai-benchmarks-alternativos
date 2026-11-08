# Seed 2.1 Turbo — startup_content/workshop_outline

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.2 | quality: 9.72
- latency_total: 62.914s | tokens_per_second: 71.4
- input_tokens: 237 | output_tokens: 4494
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un facilitador de workshops de emprendimiento y tecnologia con experiencia en Latinoamerica.

**user:**

Crea el outline completo para un workshop presencial de 3 horas titulado:
"Construye tu Asistente de IA para tu Startup - Workshop Practico"

La audiencia son emprendedores early-stage no-tecnicos (20-30 personas).

Incluye:
1. Agenda detallada con tiempos (3 horas)
2. Materiales necesarios (que preparar antes)
3. Para cada bloque:
   - Titulo y duracion
   - Objetivo
   - Dinamica (charla, ejercicio, demo, discusion)
   - Key takeaway
4. Ejercicio principal del workshop (que todos puedan hacer)
5. Recursos para llevar a casa
6. Slide count estimado por seccion

El tono debe ser energico y practico, no academico.


## Respuesta completa

# Workshop Presencial: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"  
**Duración**: 3 horas | **Audiencia**: 20-30 emprendedores early-stage no técnicos | **Tono**: Energético, práctico, sin jerga técnica

---

## 1. Agenda Detallada con Tiempos
| Bloque | Duración | Título |
|--------|----------|--------|
| 1 | 15 min | Bienvenida + Desmitificación de la IA para emprendedores |
| 2 | 25 min | ¿Qué puede hacer tu asistente de IA? Define tu caso de uso |
| 3 | 10 min | Break rápido + Networking |
| 4 | 60 min | Ejercicio principal: Construye tu asistente en 60 minutos (sin código) |
| 5 | 25 min | Optimiza tu asistente: Trucos para que no sea un robot tonto |
| 6 | 20 min | Casos reales de startups latinas + Q&A |
| 7 | 15 min | Siguientes pasos + Cierre |
| **Total** | **3h (180 min)** | |

---

## 2. Materiales Necesarios (Preparar Antes)
### Para el equipo organizador:
- Proyector + pantalla + sonido
- Tablero de papel o pizarra blanca + marcadores de colores
- Post-its (paquetes de 5 colores por mesa) + bolígrafos
- Hojas de trabajo impresas (plantilla de caso de uso + checklist de prompts)
- Acceso a WiFi estable (con contraseña visible en carteles)
- Cuenta de demostración premium de ChatGPT (para evitar límites de GPT-4)
- Backup: Slides descargadas + capturas de pantalla del ejercicio (por si falla el WiFi)
- Snacks para el break (café, galletas, agua)
- Stickers o swag pequeño con marca del workshop (para premiar participaciones)

### Para los asistentes (avisar con 48h de antelación):
- Laptop o tablet (no es obligatorio, pero recomendado)
- Cuenta gratuita de ChatGPT (creada en chat.openai.com) o de Gemini (google.com/gemini)
- Celular con datos (como backup de internet)
- Una hoja con 2-3 dolores de su startup que quieren resolver

---

## 3. Detalle por Bloque
### Bloque 1: Bienvenida + Desmitificación de la IA para emprendedores  
**Duración**: 15 min | **Dinamica**: Charla interactiva + encuesta en vivo  
**Objetivo**: Romper el hielo, eliminar el miedo a la "tecnología complicada" y alinear expectativas de lo que sí y no se hará en el workshop.  
**Desarrollo de la dinámica**:
1. (3 min) Presentación del facilitador: ejemplo rápido de un asistente de IA que armó en 20 minutos para automatizar respuestas de clientes de una empanadería (demo de 30 segundos para sorprender).
2. (5 min) Encuesta levantando la mano:
   - ¿Cuántos han usado ChatGPT/Gemini alguna vez?
   - ¿Cuántos creen que necesitan saber programar para construir un asistente de IA?
   - ¿Cuántos tienen un dolor de su startup que les gustaría resolver con IA hoy?
3. (5 min) Desmitificación: "La IA no es un robot que reemplaza tu equipo, es un pasante sin sueño que cuesta $0 al mes y hace el trabajo aburrido por vos". Ejemplos de usos para emprendedores early-stage: responder WhatsApp de clientes, redactar posts de redes, analizar encuestas, armar propuestas comerciales.
4. (2 min) Reglas del workshop: "Sin preguntas tontas, sin jargon, si algo no lo entienden gritan ¡PARE! y lo explicamos de nuevo con empanadas o tacos como ejemplo".
**Key takeaway**: No necesitas ser ingeniero para construir un asistente de IA que te ahorre 5+ horas a la semana en tu startup.
**Slides estimados**: 8

---

### Bloque 2: ¿Qué puede hacer tu asistente de IA? Define tu caso de uso  
**Duración**: 25 min | **Dinamica**: Charla + ejercicio individual + compartir en parejas  
**Objetivo**: Que cada asistente identifique un caso de uso concreto, medible y fácil de implementar para su asistente (no ideas vagas).  
**Desarrollo de la dinámica**:
1. (7 min) Presentación de los 4 casos de uso más útiles para emprendedores early-stage (con ejemplos de startups latinas):
   - Asistente de atención al cliente (responde consultas frecuentes de WhatsApp/Instagram)
   - Asistente de ventas (arma propuestas comerciales personalizadas en 2 minutos)
   - Asistente de contenido (genera ideas de posts + redacciones adaptadas a tu marca)
   - Asistente de operaciones (analiza gastos, organiza tareas del equipo, arma reportes)
2. (10 min) Ejercicio individual con hoja de trabajo impresa: "Define tu caso de uso ideal" con 3 preguntas obligatorias:
   1. ¿Qué tarea aburrida te quita más tiempo a la semana? (ej: responder 20 consultas iguales de clientes por delivery)
   2. ¿Qué resultado quieres obtener? (ej: responder 80% de las consultas sin que yo intervenga)
   3. ¿Qué información ya tienes para darle a la IA? (ej: lista de precios, horarios, zonas de delivery, preguntas frecuentes)
3. (6 min) Compartir en parejas: cada uno le cuenta su caso a la persona al lado, y le da una idea de mejora. Luego se invitan a 2-3 personas a compartir su caso con todo el grupo (premio con sticker/swag).
4. (2 min) Aclaración: "Hoy vamos a construir el asistente de atención al cliente como ejemplo, pero ustedes podrán adaptarlo a su caso de uso en 5 minutos después del workshop".
**Key takeaway**: El mejor asistente de IA no es el más complejo, es el que resuelve una tarea concreta que te roba tiempo hoy.
**Slides estimados**: 12

---

### Bloque 3: Break rápido + Networking  
**Duración**: 10 min | **Dinamica**: Descanso + intercambio informal  
**Objetivo**: Recargar energías, permitir que los asistentes resuelvan dudas rápidas con el facilitador y se conecten entre ellos.  
**Desarrollo de la dinámica**:
- Avisar que el break es de solo 10 minutos, que los snacks están al fondo del salón.
- Invitar a los asistentes a preguntarle al facilitador o a los ayudantes cualquier duda sobre su cuenta de ChatGPT/Gemini antes de empezar el ejercicio principal.
- Poner música alegre de fondo.
**Key takeaway**: (No aplica, es un break)
**Slides estimados**: 1 (slide con tiempo de regreso + QR a grupo de WhatsApp de emprendedores)

---

### Bloque 4: Ejercicio Principal: Construye tu asistente en 60 minutos (sin código)  
**Duración**: 60 min | **Dinamica**: Demo paso a paso + ejercicio guiado + apoyo personalizado  
**Objetivo**: Que cada asistente salga con un asistente de IA funcional y probado al final del bloque, sin escribir una sola línea de código.  
**Desarrollo de la dinámica**:
1. (5 min) Presentación de la herramienta: "Usaremos los GPTs de ChatGPT, que son asistentes personalizados que se arman en 10 pasos sin código. Si tienen cuenta gratuita, pueden usar los Custom Instructions de ChatGPT, que funcionan casi igual".
2. (30 min) Demo paso a paso (el facilitador va haciendo en pantalla, los asistentes van siguiendo en sus laptops/tablets/celulares):
   - Paso 1: Abrir ChatGPT > ir a "Explorar" > "Crear un GPT" (o en cuenta gratuita: Settings > Custom Instructions)
   - Paso 2: Darle un nombre a tu asistente (ej: "Asistente de Delivery de Mi Empanadería")
   - Paso 3: Cargar la "personalidad" del asistente: "Eres un asistente amable, cercano, que habla como yo, no usa lenguaje formal. Nunca inventas información, si no sabes algo le dices al cliente que se comunicará con el dueño en 10 minutos".
   - Paso 4: Cargar la base de conocimientos: subir un archivo PDF con tu lista de precios, horarios, zonas de delivery, preguntas frecuentes (o pegar el texto directamente en las instrucciones).
   - Paso 5: Definir reglas de funcionamiento: "Solo respondes consultas de clientes, no hablas de otros temas. Si el cliente quiere hacer un pedido, le pides nombre, dirección, cantidad y producto, y se lo resumas al final para confirmar".
   - Paso 6: Probar el asistente en la ventana de previsualización: hacer una consulta de ejemplo (ej: "¿A qué hora abren y entregan en Caballito?") y corregir lo que no funcione.
3. (20 min) Tiempo libre para personalizar: cada asistente adapta el asistente a su caso de uso, carga su propia información y prueba 3 consultas diferentes. El facilitador y los ayudantes recorren las mesas para resolver dudas.
4. (5 min) Muestra de resultados: invitar a 3 asistentes a mostrar su asistente funcionando al grupo (premio con swag).
**Key takeaway**: En menos de una hora puedes tener un asistente de IA funcional que resuelva tareas de tu startup sin invertir dinero.
**Slides estimados**: 15 (cada paso con captura de pantalla, sin texto largo)

---

### Bloque 5: Optimiza tu asistente: Trucos para que no sea un robot tonto  
**Duración**: 25 min | **Dinamica**: Charla + mini-ejercicio de prompts  
**Objetivo**: Enseñar 5 trucos sencillos para mejorar la precisión del asistente y evitar errores comunes.  
**Desarrollo de la dinámica**:
1. (12 min) Presentación de los 5 trucos (cada uno con ejemplo práctico):
   1. Truco 1: Dale contexto de tu startup (no solo "eres un asistente", sino "eres el asistente de Mi Empanadería, que vende empanadas artesanales en Buenos Aires desde 2022, nuestro diferencial es la masa casera").
   2. Truco 2: Dile exactamente qué NO hacer (ej: "Nunca descuentes más de 10% sin aprobación del dueño, nunca inventas productos que no están en la lista de precios").
   3. Truco 3: Usa ejemplos de respuestas que te gusten (ej: "Si un cliente pregunta por precios, responde así: 'Claro! Nuestras empanadas de carne son $500, de jamón y queso $550. ¿Cuántas te llevas?'").
   4. Truco 4: Actualízalo cada semana (agrega nuevas preguntas frecuentes, cambia precios, agrega promociones).
   5. Truco 5: Conéctalo a tus herramientas de trabajo (ej: conecta el asistente a tu WhatsApp con herramientas sin código como ManyChat o Wati, en 10 pasos).
2. (10 min) Mini-ejercicio: cada asistente escribe un prompt para mejorar su asistente usando al menos 2 de los trucos, y lo prueba en vivo. Luego comparten con la persona al lado si el resultado mejoró.
3. (3 min) Aclaración de errores comunes: "No esperes que el asistente sea perfecto el primer día. Lo importante es que resuelva el 70% de la tarea, y tú te encargas del 30% más complejo. Eso ya te ahorra muchísimo tiempo".
**Key takeaway**: La calidad de tu asistente de IA depende de la calidad de la información y las reglas que le des, no de tu conocimiento técnico.
**Slides estimados**: 10

---

### Bloque 6: Casos reales de startups latinas + Q&A  
**Duración**: 20 min | **Dinamica**: Charla + discusión abierta  
**Objetivo**: Mostrar ejemplos tangibles de emprendedores como ellos que usan asistentes de IA para crecer, y resolver todas sus dudas.  
**Desarrollo de la dinámica**:
1. (8 min) 3 casos de éxito de startups latinas early-stage:
   - Caso 1: Tienda de ropa sostenible en Colombia: usó un asistente de IA para responder consultas de Instagram, redujo el tiempo de respuesta de 2 horas a 2 minutos, aumentó las ventas en 25%.
   - Caso 2: Agencia de marketing en México: usó un asistente de IA para redactar propuestas comerciales, redujo el tiempo de armado de 4 horas a 30 minutos, pudo tomar 3 clientes más al mes.
   - Caso 3: Emprendimiento de comida saludable en Chile: usó un asistente de IA para analizar encuestas de clientes, identificó que el 60% quería opciones sin gluten, lanzó una nueva línea que aumentó los ingresos en 30%.
2. (12 min) Q&A abierta: invitar a los asistentes a hacer preguntas, el facilitador responde con ejemplos prácticos. Si hay preguntas muy técnicas, las simplifica: "No te preocupes por cómo funciona por dentro, lo importante es que te funcione a vos".
**Key takeaway**: Emprendedores de toda Latinoamérica ya están usando asistentes de IA para ahorrar tiempo y ganar dinero, sin ser expertos en tecnología.
**Slides estimados**: 7

---

### Bloque 7: Siguientes pasos + Cierre  
**Duración**: 15 min | **Dinamica**: Charla + cierre energético  
**Objetivo**: Darles un plan de acción para los próximos 7 días, y cerrar el workshop con motivación.  
**Desarrollo de la dinámica**:
1. (5 min) Plan de acción de 7 días:
   - Día 1: Probar tu asistente con 10 consultas reales (tus amigos o clientes de prueba).
   - Día 3: Actualizar el asistente con los errores que encontraste.
   - Día 5: Conectar el asistente a una de tus herramientas (WhatsApp, Instagram, correo).
   - Día 7: Medir cuánto tiempo te ahorró la primera semana.
2. (3 min) Presentación de recursos para llevar a casa (ver sección 5).
3. (4 min) Agradecimientos: invitar a los asistentes a unirse al grupo de WhatsApp de emprendedores, compartir sus resultados en redes sociales con el hashtag del workshop.
4. (3 min) Cierre energético: "Hoy no solo construyeron un asistente de IA, se ganaron un pasante que trabaja 24/7 para que ustedes se enfoquen en lo que realmente importa: crecer su startup. ¡Nos vemos en la próxima!".
**Key takeaway**: El siguiente paso es probar tu asistente en la vida real en los próximos 7 días, no dejarlo guardado en tu cuenta de ChatGPT.
**Slides estimados**: 5

---

## 4. Ejercicio Principal del Workshop (Detalle)
### Nombre: "Tu Asistente de IA Funcional en 60 Minutos"
### Objetivo: Que cada asistente salga con un asistente de IA personalizado y probado, adaptado a su startup, sin escribir código.
### Pasos del ejercicio:
1. **Preparación (5 min)**: Cada asistente abre su cuenta de ChatGPT/Gemini, y tiene a mano la información de su startup (lista de precios, preguntas frecuentes, etc.) que trajo o que anotó en el bloque 2.
2. **Construcción guiada (30 min)**: El facilitador va paso a paso mostrando en pantalla cómo armar el asistente:
   - Si usan ChatGPT Plus: Crear un GPT con nombre, personalidad, base de conocimientos y reglas.
   - Si usan ChatGPT gratuito: Configurar los Custom Instructions con la misma información.
   - Si usan Gemini: Usar la opción de "Personalizar asistente" con las mismas reglas.
3. **Personalización y prueba (20 min)**: Cada asistente adapta el asistente a su caso de uso (atención al cliente, ventas, contenido, operaciones) y prueba al menos 3 consultas diferentes para ver si funciona. Los ayudantes recorren las mesas para resolver dudas.
4. **Muestra de resultados (5 min)**: 3 asistentes comparten su asistente funcionando con el grupo, y el facilitador da feedback positivo y una idea de mejora.
### Resultado final por asistente: Un asistente de IA listo para usar en su startup, que resuelve una tarea concreta que le quitaba tiempo.

---

## 5. Recursos para Llevar a Casa
1. **Kit de inicio digital (accedible por QR)**:
   - Plantilla de prompts para personalizar tu asistente (para los 4 casos de uso más comunes).
   - Checklist de optimización de asistentes de IA (para revisar cada semana).
   - Lista de herramientas sin código para conectar tu asistente a WhatsApp, Instagram, correo y CRM (ManyChat, Wati, Zapier, Make, con tutoriales en español).
   - Ejemplos de bases de conocimientos para diferentes rubros (restaurantes, tiendas de ropa, servicios profesionales, etc.).
2. **Grupo de WhatsApp de emprendedores**: Para compartir dudas, resultados y nuevas ideas de IA para startups.
3. **Acceso a la grabación del workshop** (si se graba) + slides descargables.
4. **Cupón de descuento** para herramientas sin código de IA (conseguir alianzas con proveedores para dar valor agregado).

---

## 6. Slide Count Estimado Total
| Sección | Cantidad de slides |
|---------|---------------------|
| Bloque 1 | 8 |
| Bloque 2 | 12 |
| Break | 1 |
| Bloque 4 (Ejercicio principal) | 15 |
| Bloque 5 | 10 |
| Bloque 6 | 7 |
| Bloque 7 | 5 |
| **Total** | **58 slides** |

*Nota: Las slides son mayormente visuales, con poco texto, muchas capturas de pantalla y ejemplos prácticos, para no abrumar a los asistentes no técnicos.*