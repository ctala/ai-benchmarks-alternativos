# Qwen 3.8 Max — business_strategy/plan_monetizar_medio_con_restricciones

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 6.37 | quality: 8.0
- latency_total: 466.165s | tokens_per_second: 47.9
- input_tokens: 407 | output_tokens: 22343

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un estratega de negocio que trabaja con fundadores solos y sin capital. Todo plan que propones respeta las restricciones que te dan y muestra la aritmética que lo sostiene. Si un plan no llega al objetivo con sus propios números, lo dices en vez de maquillarlo.

**user:**

Tengo un medio digital de nicho (noticias de tecnología) y necesito hacerlo rentable. Quiero un plan para llegar a **$5.000 USD/mes** en 90 días.

LO QUE TENGO:
- 300.000 visitas/mes de tráfico orgánico (SEO), creciendo.
- El contenido lo genero de forma automatizada, así que publicar más no me cuesta tiempo.
- Audiencia: profesionales y curiosos de tecnología, mayormente LATAM.
- Autoridad de dominio decente, los artículos rankean.

LO QUE NO TENGO:
- **No tengo lista de correo.** Cero suscriptores hoy.
- **No tengo presupuesto para publicidad pagada.** Cero.
- Soy una sola persona y le puedo dedicar ~4 horas al día.

RESTRICCIONES DURAS (si las rompes, el plan no me sirve):
- **NO quiero publicidad display ni programática** (AdSense y similares). Ya lo decidí: destroza la velocidad del sitio y la experiencia, y el RPM en LATAM es miserable. No insistas con esto.
- No puedo contratar a nadie en 90 días.

Dame el plan. Y muéstrame la aritmética: cómo llegan los $5.000/mes con los números que tú mismo propongas.


## Respuesta completa

## Veredicto honesto antes del plan

Con lo que tienes, **sí existe una ruta aritmética para llegar a ~$5.000/mes en el mes 3**, pero con una condición importante:

**No puedes depender solo de afiliados si tu tráfico es mayormente informativo y LATAM.**  
Para llegar a $5.000 solo con afiliación necesitarías tasas de conversión demasiado optimistas. La vía más realista sin display, sin presupuesto y sin equipo es combinar:

1. **Afiliación de alta intención comercial**  
2. **Patrocinio editorial / contenido patrocinado**, no banners ni programática

Si además de “no display” tampoco quieres contenido patrocinado, entonces **no hay plan realista que llegue a $5.000/mes en 90 días con 300.000 visitas informativas, sin lista de correo y sin presupuesto**. Te lo digo directo: habría que bajar la meta, construir lista, crear un producto propio o vender leads B2B con un ciclo más largo.

Asumo que “$5.000/mes en 90 días” significa **llegar al mes 3 con run-rate de $5.000/mes**, no necesariamente facturar $5.000 promedio durante los tres meses. Si necesitas $5.000 promedio en los 90 días, sin presupuesto y sin lista, es todavía más difícil.

---

# Objetivo mes 3: $5.000+/mes

## Modelo de ingresos propuesto

| Fuente | Supuesto | Ingreso mensual estimado |
|---|---:|---:|
| Afiliados | 33 ventas × $65 comisión media | $2.145 |
| Patrocinios editoriales | 6 patrocinadores × $500/mes | $3.000 |
| **Total** |  | **$5.145/mes** |

No estoy contando display, AdSense, banners, programática ni contratación de personal.

---

# 1. Aritmética de afiliados

## Embudo propuesto

| Métrica | Valor supuesto |
|---|---:|
| Visitas mensuales totales | 300.000 |
| % de tráfico que va a páginas comerciales | 12% |
| Visitas a páginas comerciales | 36.000 |
| CTR hacia links de afiliado | 7% |
| Clics de afiliado | 2.520 |
| Conversión de clic a venta/lead pago | 1,3% |
| Ventas/leads | ~33 |
| Comisión media | $65 |
| Ingreso afiliado | $2.145 |

### Fórmula

300.000 × 12% = 36.000 visitas comerciales  
36.000 × 7% = 2.520 clics  
2.520 × 1,3% = 32,76 ≈ 33 ventas  
33 × $65 = **$2.145**

### ¿Es realista?

Es agresivo pero posible si haces tres cosas:

1. **Migrar parte del tráfico informativo a páginas de decisión.**  
   No basta con noticias de tecnología. Necesitas páginas tipo:
   - “Mejor hosting para WordPress en 2026”
   - “NordVPN vs ExpressVPN para LATAM”
   - “Mejores herramientas de IA para pymes”
   - “Alternativas a ChatGPT para empresas”
   - “Mejor CRM para startups en español”
   - “Semrush precio: ¿vale la pena en LATAM?”
   - “Mejores plataformas de email marketing para negocios”

2. **Elegir programas con comisión suficiente.**  
   Con LATAM, evita depender de Amazon Associates o comisiones de $2-$5. Necesitas programas de:
   - Hosting: Hostinger, Cloudways, Kinsta, SiteGround, etc.
   - VPN: NordVPN, Surfshark, ExpressVPN, etc.
   - SaaS / IA / productividad: herramientas con programas de afiliados o partner programs.
   - Software B2B: CRM, email marketing, analytics, ciberseguridad, facturación, ecommerce.
   - Formación tech si paga bien, pero no como eje principal.

3. **Que las páginas comerciales tengan intención de compra.**  
   No una nota automática genérica. Deben incluir:
   - Tabla comparativa.
   - Botones claros.
   - Pros y contras.
   - Precio.
   - “Mejor opción para LATAM”.
   - “Mejor opción barata”.
   - “Mejor opción para empresas”.
   - Capturas o datos propios si es posible.
   - Fecha de actualización.
   - Links con `rel="sponsored"` o `nofollow` cuando corresponda.

---

# 2. Aritmética de patrocinios editoriales

Aquí está el puente para llegar a $5.000 sin display.

## Objetivo

Cerrar **6 patrocinios editoriales activos en el mes 3**, a un ticket promedio de **$500/mes**.

| Concepto | Cantidad | Precio | Ingreso |
|---|---:|---:|---:|
| Patrocinio editorial mensual | 6 | $500 | $3.000 |

Para hacerlo más realista, puedes cerrar:

- 3 patrocinios iniciales a $400.
- 3 patrocinios a $600.

Total:  
3 × $400 = $1.200  
3 × $600 = $1.800  
Total = **$3.000**

---

## Embudo comercial para cerrar 6 patrocinios

| Métrica | Valor supuesto |
|---|---:|
| Prospectos contactados en 90 días | 1.200 |
| Tasa de respuesta | 5% |
| Respuestas | 60 |
| Tasa de reunión / conversación | 25% |
| Reuniones | 15 |
| Tasa de cierre | 40% |
| Patrocinios cerrados | 6 |

### Fórmula

1.200 prospectos × 5% = 60 respuestas  
60 × 25% = 15 reuniones  
15 × 40% = 6 cierres  
6 × $500 = **$3.000**

Esto requiere disciplina comercial. Sin presupuesto, tu “publicidad” para vender patrocinios es tu outreach manual.

---

# 3. Qué vender como patrocinio sin usar display

No vas a vender banners. Vas a vender **integraciones editoriales**.

## Paquete principal: $500/mes

Incluye, por ejemplo:

- 1 artículo patrocinado al mes, claramente etiquetado como “contenido patrocinado”.
- 1.000-1.500 palabras.
- Enfoque útil, no puramente promocional.
- 2-3 enlaces hacia el patrocinador con `rel="sponsored"`.
- Mención textual dentro de 2 artículos relacionados ya publicados.
- Inclusión en una página de recursos o herramientas recomendadas.
- Reporte simple a 30 días: visitas, clics, tiempo de lectura.

## Paquete premium: $900/mes

- 2 artículos patrocinados.
- Inclusión en 4 artículos relacionados.
- Página de recursos destacada.
- Comparativa donde el patrocinador aparece como una opción relevante.
- Reporte mensual.

## Paquete entrada: $350-$400

Para cerrar los primeros 3 patrocinios rápido:

- 1 artículo patrocinado.
- 1 mención en artículo relacionado.
- Inclusión en página de recursos.
- Precio de lanzamiento a cambio de testimonio o caso de éxito.

Importante: no vendas espacios que parezcan basura. Si el patrocinio no aporta al lector, dañas la confianza del medio y el SEO a largo plazo.

---

# 4. Plan de ejecución 90 días

## Días 1-7: fundamentos y auditoría

### Objetivo

Preparar el sitio para monetizar sin display y crear el motor comercial.

### Tareas

1. **Auditoría de tráfico**
   - Revisa Google Analytics y Search Console.
   - Identifica las 100 URLs con más tráfico.
   - Clasifícalas:
     - Informativas: noticias, tendencias, curiosidades.
     - Semi-comerciales: reviews, herramientas, comparaciones.
     - Comerciales: “mejor X”, “X vs Y”, “alternativas”, “precio”.

2. **Seleccionar 45 temas de páginas comerciales**
   - 15 de hosting / VPN / dominios / infraestructura.
   - 15 de SaaS / IA / productividad.
   - 15 de software para negocios / fintech / ecommerce / ciberseguridad.

3. **Crear media kit simple**
   Una página o PDF gratuito con:
   - Visitas mensuales.
   - Pageviews si los tienes.
   - Países principales.
   - Temáticas principales.
   - Ejemplos de artículos con tráfico.
   - Formatos de patrocinio.
   - Precios.
   - Contacto.

4. **Aplicar a programas de afiliados**
   - Prioriza programas con pago decente y aprobación relativamente rápida.
   - Crea una hoja de cálculo con:
     - Programa.
     - Comisión.
     - Cookie.
     - Estado de aprobación.
     - Links.
     - Páginas donde lo usarás.

5. **Definir estructura de páginas comerciales**
   Cada página debe tener:
   - Título con intención comercial.
   - Tabla comparativa.
   - Ganador claro.
   - Mejor opción por precio.
   - Mejor opción para LATAM.
   - Pros y contras.
   - Precio aproximado.
   - FAQ.
   - CTA visible sin popups ni banners.

---

## Días 8-30: primeras 15 páginas comerciales y arranque comercial

### Contenido

Publica o actualiza **15 páginas comerciales**.

Como puedes generar contenido automáticamente, úsalo para el borrador, pero haz una pasada humana en cada página:

- Corrige datos.
- Agrega precios reales.
- Agrega comparativas.
- Añade contexto LATAM.
- Revisa que la intención comercial sea clara.
- Coloca links de afiliado correctamente.

No publiques 50 páginas automáticas sin control. Para monetizar, las páginas comerciales deben transmitir confianza.

### Tráfico interno

Para cada página comercial nueva, consigue enlaces internos desde artículos existentes:

- Mínimo ideal: 5-10 enlaces internos por página comercial.
- Usa anclas naturales:
  - “mejores herramientas de IA”
  - “comparativa de hosting”
  - “alternativas a X”
  - “ver opciones recomendadas”

Si tienes artículos informativos con mucho tráfico, inserta un bloque simple tipo:

> ¿Buscas herramientas similares? Revisa esta comparativa actualizada.

Sin banners. Solo texto o caja simple.

### Afiliados

Objetivo día 30:

- 15 páginas comerciales live.
- Links de afiliado colocados.
- Eventos de clic medidos en GA4 o al menos UTM/hoja de control.
- Primeras pruebas de CTR.

### Patrocinios

Objetivo día 30:

- 300-400 prospectos contactados.
- Media kit listo.
- 10-20 respuestas.
- 2-5 reuniones.
- Idealmente 1 patrocinio cerrado a $350-$400.

Ritmo de outreach:

- 20 prospectos nuevos por día hábil.
- 3 follow-ups por prospecto.
- 1 hora al día dedicada solo a esto.

---

## Días 31-60: escalar páginas comerciales y cerrar patrocinios

### Contenido

Publica o actualiza **15 páginas comerciales más**.

Total acumulado: 30 páginas comerciales.

Prioriza páginas que puedan rankear rápido o recibir tráfico interno:

- Comparativas de herramientas conocidas.
- Alternativas a herramientas populares.
- Páginas de precio.
- “Mejor X para Y”.
- “X para pymes”.
- “X en español”.
- “X para LATAM”.

### Optimización

Revisa qué páginas comerciales reciben clics:

- Si una página recibe visitas pero pocos clics:
  - Sube la tabla comparativa.
  - Mejora el CTA.
  - Haz el ganador más claro.
  - Agrega confianza: precios, pros/contras, contexto local.

- Si una página recibe clics pero no convierte:
  - Cambia el programa de afiliado.
  - Revisa si el precio es demasiado alto para la audiencia.
  - Prueba una alternativa más barata.
  - Agrega FAQ sobre pago, impuestos, soporte en español.

### Patrocinios

Objetivo día 60:

- 600-800 prospectos contactados acumulados.
- 30-40 respuestas acumuladas.
- 8-10 reuniones acumuladas.
- 2-3 patrocinios cerrados.
- Primeros contenidos patrocinados publicados.

Si no has cerrado patrocinios, ajusta:

- Baja el precio de entrada a $350.
- Ofrece un paquete de prueba.
- Pide pago por adelantado.
- Muestra datos reales de tráfico.
- Propón un ángulo específico para la marca.

---

## Días 61-90: llegar al run-rate de $5.000

### Contenido

Publica o actualiza **15 páginas comerciales más**.

Total acumulado: 45 páginas comerciales.

Si cada página comercial consigue en promedio 800 visitas/mes:

45 × 800 = 36.000 visitas comerciales/mes

Ese es el número que necesitas para el modelo de afiliados.

### Afiliados

Objetivo mes 3:

- 36.000 visitas comerciales.
- 7% CTR = 2.520 clics.
- 1,3% conversión = 33 ventas.
- $65 comisión media = $2.145.

### Patrocinios

Objetivo mes 3:

- 6 patrocinios activos.
- Ticket promedio $500.
- $3.000/mes.

Para lograrlo, tu pipeline debe tener:

- 1.200 prospectos contactados.
- 60 respuestas.
- 15 reuniones.
- 6 cierres.

Si ya cerraste 3 antes, en el último mes necesitas cerrar 3 más y renovar o mantener los anteriores.

---

# 5. Rutina diaria de 4 horas

Este plan cabe en 4 horas/día si eres disciplinado.

## Distribución sugerida

| Bloque | Tiempo | Tarea |
|---|---:|---|
| Contenido comercial | 90 min | Crear/actualizar páginas comerciales |
| Outreach patrocinios | 60 min | Contactar prospectos y follow-ups |
| Optimización | 45 min | Revisar CTR, links, tablas, GA |
| Gestión | 15 min | Hoja de cálculo, afiliados, entregas |
| **Total** | **210 min** | **3,5 horas** |

Te queda margen para imprevistos.

---

# 6. Cómo conseguir 36.000 visitas comerciales/mes

No necesitas que todo el tráfico sea comercial. Solo necesitas mover una parte.

## Meta

300.000 visitas × 12% = 36.000 visitas comerciales.

## Cómo lograrlo

### Opción A: páginas nuevas que rankean

Si publicas 45 páginas comerciales y cada una recibe 800 visitas/mes:

45 × 800 = 36.000

### Opción B: tráfico interno desde artículos existentes

Si tus 100 artículos principales reciben, por ejemplo, 200.000 visitas/mes, y logras que 15% haga clic hacia páginas comerciales:

200.000 × 15% = 30.000 visitas comerciales

Luego sumas tráfico orgánico directo de las páginas nuevas.

### Opción C: mezcla

- 20.000 desde tráfico interno.
- 16.000 desde páginas comerciales nuevas o actualizadas.

Total: 36.000.

---

# 7. Qué páginas comerciales crear

Prioriza intención de compra. No “noticias”. No “curiosidades”.

## 15 páginas de hosting / VPN / infraestructura

Ejemplos:

1. Mejor hosting para WordPress en 2026.
2. Mejor hosting barato para LATAM.
3. Hostinger vs SiteGround.
4. Cloudways vs Hostinger.
5. Mejor hosting para ecommerce.
6. Mejor VPN para trabajar remoto.
7. NordVPN vs ExpressVPN.
8. Mejor VPN para streaming en LATAM.
9. Mejor VPS para desarrolladores.
10. Mejor hosting para Laravel.
11. Mejor hosting para WordPress + WooCommerce.
12. Cómo elegir dominio para startup.
13. Mejor CDN para sitios web en LATAM.
14. Mejor hosting para agencia web.
15. Alternativas a GoDaddy.

## 15 páginas de SaaS / IA / productividad

Ejemplos:

1. Mejores herramientas de IA para pymes.
2. Alternativas a ChatGPT para empresas.
3. Mejor IA para escribir contenido.
4. Mejor IA para atención al cliente.
5. Notion vs ClickUp.
6. Mejor software de gestión de proyectos.
7. Mejor CRM para startups.
8. Mejor CRM en español.
9. Mejor herramienta de email marketing para LATAM.
10. Mejor software para facturar en LATAM.
11. Mejor herramienta para reuniones online.
12. Mejor IA para transcribir reuniones.
13. Mejor automatización para pymes.
14. Mejor herramienta para crear presentaciones.
15. Mejor IA para marketing digital.

## 15 páginas de negocios digitales / fintech / ciberseguridad

Ejemplos:

1. Mejor pasarela de pagos para LATAM.
2. Mejor plataforma para vender cursos.
3. Mejor software para tiendas online.
4. Shopify vs WooCommerce.
5. Mejor herramienta para contabilidad de pymes.
6. Mejor software de ciberseguridad para empresas.
7. Mejor VPN para empresas.
8. Mejor gestor de contraseñas para equipos.
9. Mejor software de firma electrónica.
10. Mejor herramienta para encuestas.
11. Mejor software para recursos humanos.
12. Mejor plataforma para webinars.
13. Mejor herramienta de analítica web.
14. Mejor software para soporte al cliente.
15. Mejor herramienta para chatbots.

---

# 8. Estructura recomendada para cada página comercial

Cada página debe estar pensada para convertir sin destruir la experiencia.

## Estructura

1. **Título con intención clara**
   - “Las 7 mejores herramientas de IA para pymes en 2026”

2. **Resumen rápido arriba**
   - Mejor opción general.
   - Mejor opción barata.
   - Mejor opción para LATAM.
   - Mejor opción para empresas.

3. **Tabla comparativa**
   - Nombre.
   - Precio.
   - Ideal para.
   - Pros.
   - Contras.
   - Botón/link.

4. **Análisis breve por herramienta**
   - Para quién es.
   - Para quién no es.
   - Precio.
   - Diferencial.
   - CTA.

5. **Guía de compra**
   - Cómo elegir.
   - Errores comunes.
   - Qué mirar en LATAM: pagos, soporte en español, impuestos, disponibilidad.

6. **FAQ**
   - ¿Hay versión gratis?
   - ¿Funciona en español?
   - ¿Sirve para pymes?
   - ¿Qué opción es más barata?
   - ¿Hay soporte en LATAM?

7. **Disclosure**
   - Aviso claro de afiliados.
   - Sin exagerar.

---

# 9. Programas de afiliados: qué buscar

No te cases con una red. Busca economía unitaria.

## Criterios

- Comisión mínima ideal: $30-$100 por venta o lead calificado.
- O recurrente: 20%-30% durante varios meses.
- Que acepte tráfico LATAM o global.
- Que el producto tenga demanda real.
- Que el link no rompa la experiencia.
- Que puedas explicar el producto sin mentir.

## Categorías prioritarias

1. **Hosting**
   - Comisiones altas por venta.
   - Buena intención comercial.
   - Relevante para developers, pymes, agencias.

2. **VPN**
   - Buena comisión.
   - Audiencia tech entiende el valor.
   - Fácil de explicar.

3. **SaaS B2B**
   - CRM, email marketing, automatización, analytics.
   - Puede pagar recurring.

4. **IA / productividad**
   - Alta demanda.
   - Muchas herramientas con partner programs.

5. **Fintech / pagos**
   - Relevante para LATAM.
   - Puede pagar por lead calificado.

Evita construir todo el plan alrededor de Amazon Associates si tu tráfico es LATAM. Las comisiones suelen ser demasiado bajas para llegar a $5.000 sin volumen masivo.

---

# 10. Plan comercial para patrocinios

## A quién contactar

Prioriza empresas que ya gastan en marketing:

- SaaS B2B.
- Herramientas de IA.
- Hosting.
- VPN.
- Ciberseguridad.
- Fintech.
- Plataformas de ecommerce.
- Bootcamps de programación.
- Agencias de desarrollo.
- Software para pymes.
- Herramientas de marketing.
- Plataformas de cursos.
- Software de pagos.

También puedes buscar:

- Empresas que ya patrocinian newsletters tech.
- Empresas que aparecen en blogs de la competencia.
- Startups que están lanzando producto para LATAM.
- Empresas que ya anunciaron rondas de inversión.

---

## Mensaje de outreach

No envíes un mensaje genérico. Usa una estructura simple.

### Asunto

`[Empresa] + audiencia tech LATAM`

### Cuerpo

> Hola [nombre],  
>   
> Tengo un medio de tecnología con 300.000 visitas mensuales orgánicas, principalmente profesionales y lectores interesados en tecnología en LATAM.  
>   
> Estamos publicando contenido sobre [tema relevante para la empresa: herramientas de IA, hosting, software para pymes, ciberseguridad, etc.].  
>   
> Creo que [Empresa] encajaría bien como patrocinador editorial. Podemos hacer un artículo útil sobre [idea concreta], sin banners ni publicidad invasiva.  
>   
> Si te interesa, te envío el media kit y una propuesta simple.  
>   
> Saludos,  
> [Tu nombre]

### Follow-up 1, después de 3 días

> Hola [nombre], solo quería subir este correo por si se traspapeló. Si no es el momento, no pasa nada. Si te interesa patrocinio editorial en un medio tech LATAM, te puedo enviar una propuesta de 1 minuto.

### Follow-up 2, después de 7 días

> Hola [nombre], te comparto una idea concreta: un artículo tipo “[Título]”. Suele funcionar bien para herramientas que buscan usuarios en LATAM. ¿Te interesa verlo?

### Follow-up 3, después de 14 días

> Hola [nombre], cierro el seguimiento por ahora. Si en algún momento necesitan visibilidad editorial en audiencia tech LATAM, quedo disponible.

---

# 11. Proceso de venta de patrocinios

## Paso 1: Respuesta

Cuando respondan, contesta el mismo día si es posible.

## Paso 2: Llamada breve

Ofrece 15 minutos:

> ¿Te parece si hacemos una llamada de 15 minutos y te muestro tráfico, formatos y precios?

## Paso 3: Propuesta simple

Una página:

- Tráfico.
- Audiencia.
- Formato.
- Precio.
- Entrega.
- Pago.
- Ejemplo de artículo.

## Paso 4: Cobro

Sin presupuesto, evita herramientas caras.

Usa:

- PayPal.
- Wise.
- Stripe si está disponible en tu país.
- Factura simple.

Cobra por adelantado o 50% antes de publicar.

## Paso 5: Entrega

- Publica en menos de 5 días hábiles.
- Etiqueta como contenido patrocinado.
- Usa `rel="sponsored"` en enlaces pagados.
- Añade UTM para medir clics.
- Entrega reporte a 30 días.

## Paso 6: Renovación

A los 25 días:

> Te comparto el rendimiento del contenido. Si funcionó, podemos renovar el próximo mes con un nuevo ángulo.

---

# 12. Métricas que debes controlar

## Métricas de contenido comercial

| Métrica | Meta mes 3 |
|---|---:|
| Visitas totales | 300.000 |
| Visitas a páginas comerciales | 36.000 |
| % tráfico comercial | 12% |
| CTR hacia afiliados | 7% |
| Clics de afiliado | 2.520 |
| Conversión afiliada | 1,3% |
| Ventas/leads afiliados | 33 |
| Comisión media | $65 |
| Ingreso afiliado | $2.145 |

## Métricas comerciales

| Métrica | Meta 90 días |
|---|---:|
| Prospectos contactados | 1.200 |
| Respuestas | 60 |
| Reuniones | 15 |
| Cierres | 6 |
| Ticket promedio | $500 |
| Ingreso patrocinios | $3.000 |

## Métricas de negocio

| Métrica | Meta |
|---|---:|
| Ingreso total mes 3 | $5.145 |
| Ingreso por visita total | $0,017 |
| RPM efectivo sin display | $17,15 |
| EPC afiliado | $0,85 |

RPM efectivo = $5.145 / 300.000 × 1.000 = $17,15.

Ese RPM no viene de display. Viene de afiliación + patrocinio editorial.

---

# 13. Hitos por día

## Día 15

- 10-15 páginas comerciales en proceso.
- Media kit listo.
- Primeros 150 prospectos contactados.
- Programas de afiliados solicitados.

## Día 30

- 15 páginas comerciales publicadas.
- 300-400 prospectos contactados.
- 1-2 reuniones.
- Idealmente 1 patrocinio cerrado.
- Primeros clics de afiliado.

Ingreso esperado: bajo, quizá $200-$800. El mes 1 es de construcción.

## Día 60

- 30 páginas comerciales publicadas.
- 600-800 prospectos contactados.
- 30-40 respuestas.
- 8-10 reuniones.
- 2-3 patrocinios cerrados.
- Afiliados empezando a convertir.

Ingreso mensualizado esperado: $1.500-$2.500 si vas bien.

## Día 90

- 45 páginas comerciales publicadas.
- 36.000 visitas comerciales/mes.
- 33 ventas/leads afiliados.
- 6 patrocinios activos.
- Run-rate: $5.000+/mes.

---

# 14. Qué hacer si los números no llegan

## Si el tráfico comercial no llega a 36.000

Supongamos que solo logras 24.000 visitas comerciales.

Manteniendo CTR 7% y conversión 1,3%:

24.000 × 7% = 1.680 clics  
1.680 × 1,3% = 21,8 ≈ 22 ventas  
22 × $65 = $1.430

Faltarían $3.570 para llegar a $5.000.

Soluciones:

- Cerrar 2 patrocinios más.
- Subir ticket de patrocinio.
- Conseguir programas con mayor comisión.
- Mejorar conversión con mejores páginas.

## Si la comisión media baja a $50

33 × $50 = $1.650

Faltarían $3.350.

Necesitarías:

- 7 patrocinios de $500, o
- 6 patrocinios de $558, o
- Más ventas afiliadas.

## Si solo cierras 4 patrocinios

4 × $500 = $2.000

Para llegar a $5.000 necesitarías $3.000 de afiliados.

Con comisión de $65:

$3.000 / $65 = 46 ventas.

Con 2.520 clics:

46 / 2.520 = 1,8% de conversión.

No es imposible, pero es más exigente.

## Si no consigues patrocinios

Si al día 45 no tienes al menos 1-2 patrocinios cerrados o 5 reuniones serias, el plan está en riesgo.

Opciones:

1. Bajar precio de entrada a $350.
2. Aumentar outreach a 30 prospectos/día.
3. Ofrecer paquete de prueba.
4. Vender leads B2B si tienes tráfico de alta intención.
5. Aceptar una meta menor en el mes 3.

---

# 15. Escenario solo afiliados: por qué es más difícil

Si intentas llegar a $5.000 solo con afiliados:

$5.000 / $65 = 77 ventas.

Con 36.000 visitas comerciales y 7% CTR:

36.000 × 7% = 2.520 clics.

Para lograr 77 ventas:

77 / 2.520 = 3,06% de conversión.

Una conversión del 3% desde clics de afiliado, con tráfico LATAM y contenido informativo, es alta. Puede pasar en casos muy específicos, pero no es la base de un plan serio.

Por eso el patrocinio editorial es el puente.

---

# 16. Restricciones respetadas

Este plan no usa:

- AdSense.
- Display.
- Programática.
- Banners invasivos.
- Presupuesto pagado.
- Contratación de personal.

Sí usa:

- SEO existente.
- Contenido automatizado con edición estratégica.
- Links de afiliado dentro de contenido.
- Tablas comparativas.
- Patrocinio editorial claramente etiquetado.
- Outreach manual.

---

# 17. La versión mínima viable

Si quieres el plan más simple posible:

## Meta mes 3

- 45 páginas comerciales.
- 36.000 visitas comerciales.
- 33 ventas afiliadas a $65 = $2.145.
- 6 patrocinios a $500 = $3.000.
- Total: $5.145.

## Trabajo diario

- 90 minutos creando/editando páginas comerciales.
- 60 minutos contactando patrocinadores.
- 45 minutos optimizando CTR y links.
- 15 minutos midiendo.

---

# 18. Condición final

Este plan llega a $5.000/mes si se cumplen estos supuestos:

1. Logras que 12% del tráfico vaya a páginas comerciales.
2. Esas páginas convierten clics a afiliados con 7% de CTR.
3. La conversión afiliada llega a 1,3%.
4. La comisión media es de $65.
5. Cierras 6 patrocinios editoriales de ~$500.
6. Mantienes disciplina diaria de contenido y outreach.

Si alguno de estos supuestos falla, el número baja. No hay que maquillarlo.

La palanca más rápida para compensar una caída en afiliados es **patrocinio editorial**.  
La palanca más sostenible para subir afiliados es **mejorar la intención comercial del contenido**, no publicar más noticias genéricas.

Si aceptas patrocinio editorial, este es el plan.  
Si no lo aceptas, la meta de $5.000/mes en 90 días con 300.000 visitas LATAM, sin lista, sin presupuesto y sin display, probablemente no sea alcanzable.