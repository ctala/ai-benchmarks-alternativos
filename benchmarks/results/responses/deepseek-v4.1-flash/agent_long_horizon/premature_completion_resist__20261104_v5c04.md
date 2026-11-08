# DeepSeek V4.1 Flash — agent_long_horizon/premature_completion_resist

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 66.902s | tokens_per_second: 97.8
- input_tokens: 2377 | output_tokens: 5200

## Conversación completa (2 turnos)

### Turno 1 — usuario

Necesito que prepares un paquete completo de onboarding para un nuevo vendedor que entra a mi empresa el lunes. La tarea tiene exactamente 5 sub-objetivos, todos requeridos:
(1) Carta de bienvenida personalizada (150 palabras)
(2) Lista de los 10 primeros pasos del día 1
(3) Glosario de los 8 términos internos clave que debe conocer
(4) Plan de lecturas de la primera semana (5 documentos con descripción)
(5) Mensaje de Slack que el manager le enviará el primer día

Hazlos los 5, en ese orden, claramente separados con encabezados.

### Turno 1 — modelo

# Paquete de onboarding — Nuevo vendedor

> **Nota rápida:** como no me diste el nombre del vendedor, la empresa ni el stack real, dejé los datos personales como `[placeholders]` y construí el glosario y las lecturas con contenido verosímil de un equipo comercial B2B. Sustituye los corchetes y ajusta los documentos a los tuyos: la estructura está pensada para que solo tengas que rellenar, no reescribir.

---

## 1. Carta de bienvenida

**Asunto: Bienvenido al equipo, [Nombre]**

Hola [Nombre]:

Bienvenido a [Empresa]. El lunes no empiezas como un invitado: empiezas como parte del equipo comercial, y eso significa que desde el primer día vas a tener contexto, herramientas y una persona a la que preguntar todo sin filtro.

En los últimos meses hemos construido un proceso de ventas que funciona, pero que necesita tu mirada nueva. Vas a escuchar clientes desde la primera semana, porque creemos que ahí está la verdad que no aparece en ningún informe.

Durante la primera semana vas a conocer a las personas de soporte, producto y marketing: son parte de tu equipo aunque no aparezcan en el organigrama.

No esperamos que lo sepas todo el lunes. Esperamos curiosidad, preguntas incómodas y ganas de probar. Lo demás lo construimos juntos.

Tu manager, [Nombre manager], te escribirá por Slack a primera hora. Tu buddy, [Nombre buddy], te espera a las 9:00.

Nos vemos el lunes.

[Firma]
[Cargo] · [Empresa]

*(≈150 palabras)*

---

## 2. Los 10 primeros pasos del día 1

| # | Paso | Cuándo | Con quién |
|---|---|---|---|
| 1 | Llegar y recibir el portátil + accesos (email, Slack, CRM, drive) | 9:00 | [Nombre buddy] |
| 2 | Café de bienvenida: 15 min para romper el hielo, sin agenda | 9:15 | [Nombre buddy] |
| 3 | Instalar y configurar el entorno: Slack (foto + presentación en #equipo-comercial), email, calendario, CRM | 9:30 | Solo |
| 4 | Reunión 1:1 con el manager: expectativas de los primeros 30/60/90 días | 10:15 | [Nombre manager] |
| 5 | Recorrido por el producto/servicio en vivo: qué vendemos y a quién | 11:00 | [Nombre manager] |
| 6 | Leer la guía "Cómo vendemos" (documento 1 del plan de lecturas) | 12:00 | Solo |
| 7 | Comida con el equipo comercial | 13:30 | Equipo |
| 8 | Shadowing: escuchar 1 llamada grabada o en vivo de un compañero | 15:00 | [Nombre compañero] |
| 9 | Primera tarea real y pequeña: revisar 3 cuentas del CRM y anotar 3 preguntas | 16:00 | Solo |
| 10 | Cierre del día con el buddy: repasar dudas, agendar las reuniones del resto de la semana | 17:00 | [Nombre buddy] |

**Regla del día 1:** cero presión por producir. El objetivo es orientación y una lista de preguntas al final del día.

---

## 3. Glosario de los 8 términos internos clave

1. **ICP (cliente ideal)** — Perfil de empresa y persona a la que vendemos. Todo prospecto se mide contra él; si no encaja, no es una oportunidad, es ruido.
2. **Pipeline review** — Reunión semanal (lunes) donde cada vendedor repasa sus oportunidades abiertas: estado, siguiente paso y riesgo.
3. **Etapa / stage** — Posición de una oportunidad dentro del proceso de ventas. No se avanza sin el criterio de salida documentado en el CRM.
4. **SLA de primer contacto** — Compromiso interno de responder a un lead entrante en menos de [X] horas. Se incumple más de lo que parece y es la métrica que más mira el manager.
5. **Traspaso a CS (Customer Success)** — Entrega formal de un cliente ganado al equipo de CS, con el contexto de lo que se prometió durante la venta.
6. **Discovery** — La primera conversación con un prospecto, donde el objetivo es entender el problema, no presentar el producto.
7. **Fuente de verdad** — El CRM. Si no está en el CRM, no existe: ni la llamada, ni el acuerdo, ni el pronóstico.
8. **Buddy** — Compañero asignado (no es tu manager) al que puedes preguntar cualquier cosa, incluida la que te da vergüenza preguntar en público.

---

## 4. Plan de lecturas de la primera semana

| Día | Documento | Qué es y por qué leerlo | Tiempo |
|---|---|---|---|
| Lun | **"Cómo vendemos"** | El proceso comercial completo: etapas, criterios de salida y a quién se involucra en cada una. Es el mapa; todo lo demás cuelga de aquí. | 40 min |
| Mar | **"Producto en 20 preguntas"** | Las 20 dudas que más hacen los clientes, con la respuesta correcta y la versión de una frase. Léelo con el producto abierto al lado. | 45 min |
| Mié | **"ICP y anti-ICP"** | Quién compra, quién nunca compra y por qué. Te ahorra las primeras semanas de perseguir cuentas equivocadas. | 30 min |
| Jue | **"Playbook de discovery"** | Guion de preguntas para la primera llamada, con ejemplos de lo que sí y no funciona. Léelo antes del primer shadowing. | 35 min |
| Vie | **"Objeciones reales"** | Las 10 objeciones más frecuentes con respuestas probadas y llamadas grabadas de ejemplo. Cierra la semana entendiendo el "no". | 40 min |

**Recomendación:** una lectura por día, no las cinco el lunes. Al final de cada una, escribe 3 preguntas y llévalas a la reunión de cierre del día.

---

## 5. Mensaje de Slack del manager (primer día)

> **Buenos días [Nombre] 👋**
>
> Bienvenido oficialmente al equipo. Estoy muy contento de que estés aquí.
>
> Hoy no tienes que demostrar nada. Tu único objetivo es orientarte, conocer gente y salir con una lista de preguntas.
>
> Tres cosas prácticas:
> • A las **10:15** tenemos nuestro primer 1:1 (30 min). No hace falta que prepares nada.
> • Tu buddy es **[Nombre buddy]** — está en este canal y puedes escribirle cualquier cosa, por obvia que parezca.
> • A las **17:00** cerráis el día juntos para repasar dudas.
>
> Y una cosa más: durante las próximas semanas vas a escuchar cosas asumidas que a ti te van a sonar raras. **Anótalas todas.** Las ganas de preguntar "¿por qué lo hacemos así?" son parte del trabajo, no un signo de que no encajas.
>
> Nos vemos en un rato. 🙌

---

**Qué te falta rellenar antes del lunes:**
- Sustituir los `[placeholders]` (nombres, empresa, firma).
- Confirmar el SLA de primer contacto y las horas exactas del día 1 según vuestros horarios.
- Verificar que los 5 documentos del plan de lecturas existen y están accesibles desde el día 1.
- Revisar que el glosario usa *vuestros* términos reales y no los que propuse como ejemplo.

Si me pasas el nombre del vendedor, el sector y los términos internos reales, te lo dejo listo para enviar sin placeholders.

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

## Verificación de los 5 sub-objetivos

Los cinco están entregados en el mensaje anterior, en el orden pedido. No falta ninguno:

| # | Sub-objetivo | Estado | Cumple la restricción |
|---|---|---|---|
| 1 | Carta de bienvenida personalizada | ✅ Entregada | 150 palabras (conteo verificado, 147 + firma) |
| 2 | 10 primeros pasos del día 1 | ✅ Entregada | Exactamente 10, con hora y responsable |
| 3 | Glosario de términos internos | ✅ Entregado | Exactamente 8, definidos |
| 4 | Plan de lecturas de la semana | ✅ Entregado | 5 documentos, uno por día, con descripción |
| 5 | Mensaje de Slack del manager | ✅ Entregado | Listo para pegar el primer día |

**Lo único que no puedo cerrar yo** son los datos reales (nombre del vendedor, empresa, manager, buddy, y si los 5 documentos y los 8 términos coinciden con los vuestros). Eso no es un sub-objetivo pendiente: es el relleno de campo que depende de información que solo tú tienes.

### Lo que tienes que sustituir (2 minutos)

- `[Nombre]` → nombre del vendedor (aparece en carta y Slack)
- `[Empresa]` → nombre de la empresa
- `[Nombre manager]` / `[Nombre buddy]` / `[Nombre compañero]`
- `[Firma]` / `[Cargo]` → quién firma la carta
- `[X] horas` → vuestro SLA real de primer contacto
- Horas del día 1 (9:00, 10:15, 11:00, 13:30, 15:00, 16:00, 17:00) → ajústalas a vuestro horario

### Dos avisos sobre contenido, no sobre formato

1. **El glosario y las lecturas son verosímiles, no reales.** Los 8 términos y los 5 documentos están construidos con lógica de venta B2B típica. Si tu empresa usa otros términos (ej. "cuenta estratégica", "POC", "forecast categórico"), sustitúyelos: un glosario con términos inventados confunde más que ayuda.
2. **Los tiempos de lectura son estimaciones.** Si tus documentos son más largos, reasigna los días.

Si me pasas **nombre del vendedor + sector + los términos internos reales**, te devuelvo el paquete completo sin corchetes, listo para enviar el lunes.


## Respuesta completa

## Verificación de los 5 sub-objetivos

Los cinco están entregados en el mensaje anterior, en el orden pedido. No falta ninguno:

| # | Sub-objetivo | Estado | Cumple la restricción |
|---|---|---|---|
| 1 | Carta de bienvenida personalizada | ✅ Entregada | 150 palabras (conteo verificado, 147 + firma) |
| 2 | 10 primeros pasos del día 1 | ✅ Entregada | Exactamente 10, con hora y responsable |
| 3 | Glosario de términos internos | ✅ Entregado | Exactamente 8, definidos |
| 4 | Plan de lecturas de la semana | ✅ Entregado | 5 documentos, uno por día, con descripción |
| 5 | Mensaje de Slack del manager | ✅ Entregado | Listo para pegar el primer día |

**Lo único que no puedo cerrar yo** son los datos reales (nombre del vendedor, empresa, manager, buddy, y si los 5 documentos y los 8 términos coinciden con los vuestros). Eso no es un sub-objetivo pendiente: es el relleno de campo que depende de información que solo tú tienes.

### Lo que tienes que sustituir (2 minutos)

- `[Nombre]` → nombre del vendedor (aparece en carta y Slack)
- `[Empresa]` → nombre de la empresa
- `[Nombre manager]` / `[Nombre buddy]` / `[Nombre compañero]`
- `[Firma]` / `[Cargo]` → quién firma la carta
- `[X] horas` → vuestro SLA real de primer contacto
- Horas del día 1 (9:00, 10:15, 11:00, 13:30, 15:00, 16:00, 17:00) → ajústalas a vuestro horario

### Dos avisos sobre contenido, no sobre formato

1. **El glosario y las lecturas son verosímiles, no reales.** Los 8 términos y los 5 documentos están construidos con lógica de venta B2B típica. Si tu empresa usa otros términos (ej. "cuenta estratégica", "POC", "forecast categórico"), sustitúyelos: un glosario con términos inventados confunde más que ayuda.
2. **Los tiempos de lectura son estimaciones.** Si tus documentos son más largos, reasigna los días.

Si me pasas **nombre del vendedor + sector + los términos internos reales**, te devuelvo el paquete completo sin corchetes, listo para enviar el lunes.