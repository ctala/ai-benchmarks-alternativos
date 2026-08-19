# Sakana Namazu — sales_outreach/cold_email_personalized

- model_id: `sakana/sakana-namazu`
- success: True  | final: 6.23 | quality: 6.5
- latency_total: 7.595s | tokens_per_second: 269.7
- input_tokens: 211 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un experto en cold outreach B2B. Reglas:
- NUNCA uses frases genericas como "Espero que este email te encuentre bien"
- El email debe ser corto (max 150 palabras)
- Personalizado al destinatario
- Un solo CTA claro
- No vendas, genera curiosidad

**user:**

Escribe un cold email para:
- Destinatario: Maria Lopez, Head of Marketing en FintechCo (startup fintech en Colombia, 50 empleados, Serie A)
- Mi producto: herramienta de automatizacion de contenido con IA para startups
- Dato de personalizacion: Maria publico un post en LinkedIn la semana pasada sobre "como escalar content marketing sin contratar"
- Objetivo: conseguir una call de 15 min

Escribe SOLO el email (subject + body). Nada mas.


## Respuesta completa

El usuario solicita un cold email B2B personalizado para María Lopez, Head of Marketing en FintechCo, una startup fintech en Colombia con 50 empleados y Serie A. Mi producto es una herramienta de automatización de contenido con IA para startups. El dato de personalización es que María publicó un post en LinkedIn la semana pasada sobre "cómo escalar content marketing sin contratar". El objetivo es conseguir una call de 15 minutos.

Debo seguir las reglas:
- NUNCA usar frases genéricas como "Espero que este email te encuentre bien"
- El email debe ser corto (máximo 150 palabras)
- Personalizado al destinatario
- Un solo CTA claro
- No vender, generar curiosidad
- Escribir SOLO el email (subject + body). Nada más.

Debo contar las palabras para asegurar que no exceda 150 palabras.

Posible estructura:
Subject: Algo que conecte con su post y su desafío
Body:
- Referencia directa al post de LinkedIn sobre escalar content marketing sin contratar
- Conectar con su situación en FintechCo (startup Serie A, 50 empleados)
- Plantear el problema de escalar contenido sin aumentar headcount
- Mencionar brevemente que trabajo con startups fintech para automatizar contenido con IA
- CTA claro para una call de 15 min

Veamos un borrador:

Subject: Escalar content sin contratar - vi tu post en LinkedIn

María,

Leí tu post en LinkedIn sobre cómo escalar content marketing sin aumentar el equipo. Me quedé pensando en lo difícil que debe ser mantener la calidad y frecuencia en FintechCo estando en Serie A y con el equipo enfocado en otros frentes.

Trabajo con heads de marketing de startups fintech ayudándoles a automatizar la creación de contenido (blogs, casos de uso, posts redes) con IA, sin que parezca robótico ni requiera contratar a más gente.

¿Te va si agendamos una call de 15 min esta semana para que veas cómo otras startups en tu misma etapa lo están haciendo?

[Mi nombre]

Contemos palabras:
Subject: Escalar content sin contratar - vi tu post en LinkedIn (10)

María, (1)

Leí tu post en LinkedIn sobre cómo escalar content marketing sin aumentar el equipo. (12) Me quedé pensando en lo difícil que debe ser mantener la calidad y frecuencia en FintechCo estando en Serie A y con el equipo enfocado en otros frentes. (24)

Trabajo con heads de marketing de startups fintech ayudándoles a automatizar la creación de contenido (blogs, casos de uso, posts redes) con IA, sin que parezca robótico ni requiera contratar a más gente. (26)

¿Te va si agendamos una call de 15 min esta semana para que veas cómo otras startups en tu misma etapa lo están haciendo? (20)

Total aprox: 93 palabras. Bien, está dentro del límite.

Ajustemos para que sea fluido y natural. También podría ser más directo.

Otra opción:

Subject: Tu post sobre escalar content sin contratar

María,

Vi tu post en LinkedIn sobre escalar content marketing sin aumentar headcount. Me resonó porque varios heads de marketing en startups fintech Serie A me han comentado lo mismo: necesitan más contenido pero no el overhead de contratar.

En FintechCo seguramente pasa lo mismo —escalar sin perder calidad ni quemar al equipo.

Ayudo a startups como la tuya a automatizar la creación de contenido con IA (blogs, casos de uso, social) manteniendo el tono humano y reduciendo horas de trabajo.

¿Tenés 15 minutos esta semana para ver cómo otras fintechs Colombianas en tu misma etapa lo están haciendo?

Contemos:
Subject: Tu post sobre escalar content sin contratar (7)

María, (1)

Vi tu post en LinkedIn sobre escalar content marketing sin aumentar headcount. (11) Me resonó porque varios heads de marketing en startups fintech Serie A me han comentado lo mismo: necesitan más contenido pero no el overhead de contratar. (21)

En FintechCo seguramente pasa lo mismo —escalar sin perder calidad ni quemar al equipo. (13)

Ayudo a startups como la tuya a automatizar la creación de contenido con IA (blogs, casos de uso, social) manteniendo el tono humano y reduciendo horas de trabajo. (20)

¿Tenés 15 minutos esta semana para ver cómo otras fintechs Colombianas en tu misma etapa lo están haciendo? (17)

Total: ~89 palabras. Muy bien.

Espera, el usuario pidió "Escribe SOLO el email (subject + body). Nada mas." Así que no debo incluir firma con nombre propio? El problema es que un cold email necesita una firma mínima para que sepan quién escribe. Pero si el usuario dijo "Nada mas", quizás deba omitir placeholders como [Mi nombre] o [Company]? O quizás incluir solo "Juan" o lo que sea? El usuario no dijo cuál es mi nombre. Entonces quizás debo poner un placeholder simple o simplemente no poner nada? Pero un email sin firma es raro.

Creo que es mejor no usar placeholders tipo [Tu nombre] porque rompe la regla de "Nada mas" y puede parecer instrucción. Sin embargo, dado que no tengo el nombre del remitente, tal vez debería simplemente no incluir firma? O poner algo muy breve como "—"?

Revisando la instrucción original del sistema: "Escribe SOLO el email (subject + body). Nada mas." Esto significa que no debo incluir explicaciones previas o posteriores, solo el email. Pero dentro del email, probablemente necesite una firma. Como no sé el nombre del remitente, quizás puedo omitirla o poner un genérico mínimo. Pero mejor evito placeholders. Puedo estructurarlo sin firma? Es un poco impersonalo, pero funciona.

Otra opción: terminar con una pregunta y no firma. Es aceptable en cold email muy corto.

Veamos el tono. "headcount" es más anglicismo, quizás mejor "sin sumar gente al equipo". "Me resonó" puede sonar un poco español de España, María es de Colombia. Quizás usar algo más latino: "Me hizo sentido" o "Me identifiqué".

Ajuste para tono latinoamericano:

Subject: Escalar content sin contratar - tu post en LinkedIn

María,

Vi tu post en LinkedIn sobre cómo escalar content marketing sin sumar gente al equipo.

Justo lastimó en el punto donde muchas startups fintech Serie A están hoy: necesitan publicar más para crecer, pero no quieren (ni pueden) expandir el equipo.

En FintechCo debe ser igual —mantener frecuencia y calidad sin quemar al equipo.

Trabajo heads de marketing ayudándoles a automatizar la creación de contenido (blogs, casos de uso, posts) con IA, sin perder el tono humano ni contratar más.

¿Tenés 15 minutos esta semana para ver cómo otras fintechs colombianas en tu misma etapa lo están haciendo?

Contemos:
Subject: Escalar content sin contratar - tu post en LinkedIn (9)

María, (1)

Vi tu post en LinkedIn sobre cómo escalar content marketing sin sumar gente al equipo. (13) Justo lastimó en el punto donde muchas startups fintech Serie A están hoy: necesitan publicar más para crecer, pero no quieren (ni pueden) expandir el equipo. (21)

En FintechCo debe ser igual —mantener frecuencia y calidad sin quemar al equipo. (12)

Trabajo heads de marketing ayudándoles a automatizar la creación de contenido (blogs, casos de uso, posts) con IA, sin perder el tono humano ni contratar más. (20)

¿Tenés 15 minutos esta semana para ver cómo otras fintechs colombianas en tu misma etapa lo están haciendo? (17)

Total: ~93 palabras. Perfecto.

Espera, "lastimó" puede interpretarse como "hit the nail on the head"? No, eso sería "dio en el clavo".