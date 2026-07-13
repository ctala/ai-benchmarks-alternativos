# GPT-5.6 Luna — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 7.05 | quality: 8.0
- latency_total: 22.739s | tokens_per_second: 137.0
- input_tokens: 167 | output_tokens: 3116

## Respuesta completa

## Experimento: vender antes de construir

### Qué vas a probar exactamente

No pruebes “¿les gusta la idea?”. Prueba esto:

> “Una agencia pequeña pagará **$200 por adelantado** por un piloto de 30 días que le entregue reportes mensuales a clientes, con su marca, sin que el equipo tenga que prepararlos manualmente.”

El pago debe ser real. Un “sí, suena bien” no cuenta.

---

## Preparación — 2 horas, $0–30

Crea únicamente:

1. **Una página simple** en Notion, Carrd o Google Doc con:
   - Qué problema resuelves.
   - Qué fuentes soportas inicialmente: por ejemplo, GA4, Google Ads y Meta Ads.
   - Qué recibe la agencia: un reporte mensual listo para enviar al cliente.
   - Precio: **$200/mes**.
   - Piloto: **30 días, cancelable, primer reporte en 72 horas**.
   - Aviso explícito: “Durante este piloto, parte del proceso puede ser manual mientras terminamos el producto.”

2. **Un enlace de pago** de Stripe, PayPal o Mercado Pago por $200.

3. **Una plantilla manual de reporte** en Google Slides, Looker Studio o Google Sheets.

No construyas integraciones, dashboard, backend ni automatización.

---

## Define el cliente antes de contactar

Solo cuenta como prospecto cualificado una agencia que cumpla:

- 3–20 empleados.
- Al menos 5 clientes activos.
- Cobra retainers mensuales.
- Envía reportes periódicos a clientes.
- El fundador, director de cuentas o responsable de operaciones puede decidir la compra.
- Actualmente prepara reportes manualmente o usa una solución que le resulta insuficiente.

No cuentes freelancers sin clientes recurrentes ni agencias que solamente hacen campañas puntuales.

---

## Consigue 50 prospectos — 1 día, $0

Haz una lista de 50 agencias usando LinkedIn, Google Maps, directorios de agencias, Clutch, Instagram o referencias.

Para cada una registra:

- Nombre.
- Persona decisora.
- Email o LinkedIn.
- Número aproximado de clientes.
- Qué herramientas parece utilizar.
- Evidencia de que ofrece reporting.

No compres anuncios. No uses una campaña masiva genérica.

---

## Mensaje inicial

Envía algo parecido a esto:

> Hola, [nombre]. Estoy probando una solución para agencias pequeñas que elimina buena parte del trabajo mensual de preparar reportes para clientes.  
>   
> No he construido el producto todavía: primero quiero comprobar si el problema merece ser resuelto.  
>   
> Estoy buscando 3 agencias para un piloto pagado de 30 días por $200/mes. Entregamos los reportes con su marca; parte del proceso será manual al principio.  
>   
> ¿Hoy cuánto tiempo os lleva preparar los reportes mensuales?

No envíes un enlace de pago en el primer mensaje. Primero intenta descubrir si el problema existe.

Haz dos seguimientos durante los siguientes 5 días:

> ¿Te puedo hacer una pregunta directa? Si pudieras eliminar la preparación manual de los reportes por $200/mes, ¿sería una prioridad este trimestre?

Y después:

> Cierro los pilotos esta semana. Si no es un problema suficientemente importante, ningún inconveniente; me ayuda saberlo.

---

## Las llamadas — máximo 15 minutos

Habla con al menos 15 decisores. Antes de presentar tu solución, pregunta:

1. ¿Cuántos clientes reciben reportes?
2. ¿Quién los prepara?
3. ¿Cuántas horas al mes consume?
4. ¿Qué fuentes de datos combinan?
5. ¿Qué ocurre cuando el reporte se retrasa o tiene errores?
6. ¿Qué solución han probado?
7. ¿Cuánto pagan actualmente por herramientas o por trabajo de reporting?
8. ¿Han intentado resolverlo anteriormente?

No aceptes respuestas como “es una molestia”. Pide cifras y ejemplos recientes.

Después haz la oferta:

> Por lo que me cuentas, te propongo un piloto de 30 días. Tú nos das acceso de solo lectura a las cuentas y nosotros entregamos los reportes listos para enviar, con tu marca, en un máximo de 72 horas.  
>   
> Cuesta $200 por adelantado. Si no entregamos el primer reporte acordado, te devuelvo el dinero. ¿Quieres empezar?

Luego guarda silencio. No rebajes el precio ni ofrezcas “avisarme más adelante”.

---

## Qué cuenta como conversión

Cuenta únicamente si la agencia:

1. Paga los $200.
2. Acepta dar acceso a sus datos.
3. Define al menos un cliente real para el piloto.
4. Acepta recibir el primer reporte en los próximos 7 días.

No cuentan:

- Respuestas positivas.
- Entrevistas.
- Listas de espera.
- Cartas de intención.
- “Cuando tengas el producto”.
- Depósitos simbólicos de $1.
- Pagos condicionados a que construyas primero.

El pago puede ser reembolsable si no entregas lo prometido, pero debe hacerse antes de construir.

---

## Criterio de abandono

Establece esto antes de empezar:

### Abandona la hipótesis si, después de:

- Contactar a **50 agencias cualificadas**.
- Hacer al menos **15 conversaciones con decisores**.
- Ejecutar dos seguimientos por prospecto.
- Mantener el precio en $200/mes.

obtienes **menos de 3 pagos reales**.

En particular:

- **0–1 pagos:** mata la idea a $200/mes.
- **2 pagos:** resultado débil; no construyas. Considera que el segmento, el precio o el problema están mal definidos.
- **3 o más pagos:** no construyas todavía. Ejecuta primero los pilotos manuales.
- Si consigues pagos únicamente cuando lo describes como un servicio hecho por ti, pero rechazan la idea de una herramienta que ellos usarían, considera que la hipótesis de **software** falló. Quizá exista una agencia de servicios, pero no el producto planteado.

Una segunda condición de abandono:

> Si de los compradores iniciales menos de 2 de 3 siguen pagando o renuevan después del primer mes, abandona la idea tal como está.

---

## Ejecución del piloto sin construir

Para los compradores:

- Recibe accesos de solo lectura.
- Exporta los datos manualmente.
- Usa Google Sheets, Looker Studio, Slides o plantillas.
- Genera y envía el reporte.
- Registra cuántas horas te consume cada cuenta.
- Pregunta si lo enviarían a su cliente sin editarlo.
- Al día 25 pide explícitamente la renovación a $200.

No escondas el proceso manual. Di:

> “El resultado que recibes es el mismo que tendrá el producto; por ahora parte de la operación es manual.”

Así evitas confundir disposición a pagar por un servicio con disposición a pagar por software.

---

## Tiempo y coste

### Tiempo

- Preparación: 2 horas.
- Crear lista: 4–6 horas.
- Contacto y seguimientos: 4–6 horas.
- 15 llamadas: 4–5 horas.
- Operar los primeros pilotos: 2–4 horas por agencia.

Puedes tener una respuesta bastante concluyente en **7–10 días laborables**, sin escribir código.

### Coste

- Landing page: $0.
- Formularios y documentos: $0.
- Google Sheets/Slides/Looker Studio: $0.
- Stripe/PayPal/Mercado Pago: sin coste fijo; solo comisión por pagos.
- Dominio opcional: $10–15.
- Total esperado: **$0–30**, excluyendo tu tiempo.

La regla importante: **no construyas nada hasta que tres agencias hayan pagado $200 y hayan entregado datos para usarlo**. Si no logras eso vendiendo manualmente el resultado, añadir automatización probablemente solo hará que tardes más en descubrir el mismo rechazo.