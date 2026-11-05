# Nemotron 3 Super — reasoning/multi_constraint_decision

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.53 | quality: 9.8
- latency_total: 72.111s | tokens_per_second: 97.4
- input_tokens: 195 | output_tokens: 7024
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Ayudame a elegir un stack tecnologico para un MVP. Restricciones:

- Presupuesto: $5,000 total (infra + herramientas)
- Timeline: 6 semanas
- Equipo: 1 fullstack dev (sabe React, Python, basico de Go)
- Producto: marketplace de servicios freelance (como Fiverr pero nicho)
- Requisitos: auth, pagos, chat en tiempo real, busqueda, admin panel
- Escala esperada: 500 usuarios primer mes, 5,000 en 6 meses
- Debe ser facil de mantener por 1 persona

Compara al menos 3 opciones de stack, analiza pros/contras de cada uno, y recomienda uno con justificacion. Incluye costos estimados de infraestructura mensual.


## Respuesta completa

## Resumen rápido
| Stack | Tiempo estimado de desarrollo (6 sem) | Costo mensual de infraestructura* | Complejidad operativa (1 persona) | Qué tan bien cubre los requisitos |
|-------|--------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| **1️⃣ Django + React + Render/Fly.io** | 5‑6 sem (más boilerplate) | $70‑$120 | Media (necesita gestionar DB, migraciones, workers de WS) | Auth (Django‑Allauth), pagos (Stripe), chat (Django Channels), búsqueda (Postgres Full‑text o Elasticsearch‑lite), admin (Django Admin) |
| **2️⃣ Supabase + React + Vercel** | 4‑5 sem (menos backend) | $30‑$80 | Muy baja (Supabase maneja auth, DB, storage, realtime) | Auth (Supabase Auth), pagos (Stripe), chat (Supabase Realtime), búsqueda (Postgres Full‑text + pg_trgm), admin (React‑Admin o Supabase Studio) |
| **3️⃣ Go (Gin) + React + Railway/Fly.io** | 5‑6 sem (más código backend) | $50‑$100 | Media‑alta (necesita orquestar varios servicios, WS manual) | Auth (Go‑JWT o OAuth2), pagos (Stripe), chat (Gorilla WS), búsqueda (Postgres Full‑text), admin (Retool Free o panel custom) |

\*Los costos incluyen: hosting del frontend, base de datos, almacenamiento, servicio de websockets/realtime y cualquier add‑on necesario (caching, logs). No incluyen las comisiones de Stripe (≈ 2.9 % + $0.30 por transacción) ni licencias de herramientas de pago (ej. Retool tiene plan gratuito suficiente para un MVP).

A continuación detallo cada opción, sus pros/contras y una estimación de costos más granular. Al final, doy mi recomendación y la justificación.

---

## 1️⃣ Stack Django + React + Render/Fly.io

### Arquitectura
- **Frontend**: React (Create‑React‑App o Vite) alojado en **Vercel** (plan Hobby gratis) o **Netlify** (gratis).  
- **Backend**: Django (REST API con Django‑REST‑Framework) corriendo en **Render** (Web Service) o **Fly.io** (Docker).  
- **Base de datos**: PostgreSQL gestionada por el mismo proveedor (Render Postgres o Fly.io Postgres).  
- **Auth**: Django‑Allauth (email/password + social) + JWT para la API.  
- **Pagos**: Integración directa con Stripe SDK (Python).  
- **Chat en tiempo real**: Django Channels + Redis (pub/sub) + WebSockets.  
- **Búsqueda**: PostgreSQL Full‑Text Search (tsvector) o, si se necesita más potencia, Elasticsearch en versión gestionada (añade ~$15/mo).  
- **Admin panel**: Django Admin (out‑of‑the‑box) + posibilidad de customizar con Django‑Admin‑Interface.  
- **Deploy CI/CD**: GitHub Actions → Render/Fly.io (gratis para límites bajos).

### Pros
| ✅ | Razón |
|---|-------|
| **Control total** | Puedes ajustar auth, permisos, lógica de negocio sin depender de terceros. |
| **Admin listo** | Django Admin es potente y prácticamente cero código para CRUD básico. |
| **Madurez** | Django tiene años de estabilidad, documentación abundante y comunidad grande. |
| **Escalable** | PostgreSQL + Redis + Workers pueden escalar verticalmente; en Render/Fly.io basta con subir el plan. |
| **Reutiliza habilidades** | El dev ya conoce Python y React; solo necesita aprender Django‑Channels (bastante directo). |

### Contras
| ❌ | Razón |
|---|-------|
| **Más código backend** | Tener que escribir y mantener modelos, serializers, vistas, migraciones y workers de WS. |
| **Operación de WS** | Necesitas un Redis y gestionar conexiones WebSocket (escalado, sticky sessions). |
| **Deploy más pesado** | Cada cambio requiere rebuild del contenedor y posible downtime si no se usa blue‑green. |
| **Costo ligeramente mayor** | Necesitas al menos un dyno/web service + Redis + Postgres (aunque en niveles gratuitos puedes arrancar, pero para 5k usuarios se recomienda plan pago). |
| **Curva de aprendizaje de Channels** | Aunque el dev conoce Python, el manejo de async y canales puede requerir tiempo extra. |

### Estimación de costos mensuales (nivel “startup”)
| Servicio | Plan | Costo aprox. |
|----------|------|--------------|
| **Frontend (Vercel Hobby)** | Gratis | $0 |
| **Backend (Render Web Service)** | Starter ($7/mo) + 1 GB RAM | $7 |
| **PostgreSQL (Render)** | Starter ($7/mo) | $7 |
| **Redis (Render Upstash)** | Free tier (hasta 10k req/día) – si se necesita más, $8/mo | $0‑$8 |
| **Almacenamiento de archivos (AWS S3 compatible – Render Storage)** | 5 GB gratis + $0.023/GB extra | ~$2 (para uploads de perfiles/portfolios) |
| **Logs / Monitoring (Render)** | Incluido en starter | $0 |
| **Dominio (Namecheap)** | .com básico | $1/mo (aprox.) |
| **Total** |  | **≈ $25‑$32/mo** (con Redis gratis) – si se necesita Redis pago, sube a ~$40/mo. |

> **Nota**: Los planes gratuitos de Render/Fly.io son suficientes para los primeros 500 usuarios; al llegar a 5k usuarios probablemente necesites subir el backend a $15‑$20/mo y la DB a $15/mo, quedando todavía bajo $80/mo.

---

## 2️⃣ Stack Supabase + React + Vercel

### Arquitectura
- **Frontend**: React alojado en **Vercel** (Hobby gratis, Pro $20/mo si se necesita SSL custom o logs avanzados).  
- **Backend as a Service**: **Supabase** (PostgreSQL + Auth + Storage + Realtime).  
- **Auth**: Supabase Auth (email/password, magic link, OAuth2, JWT).  
- **Pagos**: Llamadas directas a Stripe SDK desde el frontend o vía **Supabase Edge Functions** (Node/TypeScript) para mantener la clave secreta fuera del cliente.  
- **Chat en tiempo real**: Supabase Realtime (basado en PostgreSQL replication + WebSocket).  
- **Búsqueda**: PostgreSQL Full‑Text + extensión `pg_trgm` (búsqueda difusa) – todo dentro de la misma DB.  
- **Admin panel**: Opción A) **React‑Admin** conectado directamente a Supabase (casi cero backend). Opción B) **Supabase Studio** (interfaz interna de Supabase) para tareas simples de CRUD.  
- **Funciones de negocio** (validaciones, webhooks de Stripe, etc.): **Supabase Edge Functions** (ejecución en Deno, gratis hasta 500k invocaciones/mes).  
- **CI/CD**: GitHub → Vercel (despliegue automático).  

### Pros
| ✅ | Razón |
|---|-------|
| **Mínimo backend** | Casi todo lo necesario (auth, DB, storage, realtime) viene “listo para usar”. |
| **Velocidad de desarrollo** | Se puede enfocar en UI/UX y lógica de negocio; menos tiempo en configurar servidores, migraciones, WS. |
| **Escalabilidad automática** | Supabase escala la DB y el realtime sin intervención manual (planes de pago aumentan cuotas). |
| **Costos predecibles** | Plan gratuito cubre hasta 500 MB DB y 2 GB storage; el plan “Pro” ($25/mo) da 8 GB DB, 64 GB storage y 2 TB de bandwidth – suficiente para 5k usuarios activos. |
| **Admin rápido** | React‑Admin se monta en menos de un día y se conecta directamente a la API PostgREST de Supabase. |
| **Seguridad por defecto** | RLS (Row Level Security) de Postgres permite definir políticas de acceso sin escribir middleware. |
| **Reutiliza habilidades** | El dev ya conoce React; solo necesita aprender a llamar a Supabase JS client y a escribir Edge Functions (JS/TS, muy parecido a Node). |

### Contras
| ❌ | Razón |
|---|-------|
| **Dependencia de un tercero** | Si Supabase tiene una incidencia, afecta a todo el producto (aunque su SLA es bueno). |
| **Menor control fino** | Algunas personalizaciones avanzadas (ej. lógica de transacciones complejas) pueden requerir trabajar alrededor de los límites de PostgREST o Edge Functions. |
| **Costo de funciones edge** | Si se hacen muchas llamadas a Stripe o lógica pesada, pueden consumir la cuota gratuita; sin embargo, el plan Pro incluye 500k invocaciones/mes (más que suficiente para un MVP). |
| **Búsqueda avanzada** | Para búsqueda tipo “fuzzy” con puntuación y facetas, quizá necesites añadir Algolia o Elasticsearch (costo extra). Pero para un marketplace de servicios, Full‑Text + pg_trgm suele ser suficiente. |
| **Admin menos potente que Django Admin** | React‑Admin requiere definir recursos y campos manualmente; no tiene la generación automática completa de Django Admin (aunque sigue siendo muy productivo). |

### Estimación de costos mensuales
| Servicio | Plan | Costo aprox. |
|----------|------|--------------|
| **Frontend (Vercel Hobby)** | Gratis | $0 |
| **Supabase (Pro)** | $25/mo (8 GB DB, 64 GB storage, 2 TB bandwidth) | $25 |
| **Supabase Edge Functions** | Incluido en plan Pro (500k invocaciones/mes) | $0 |
| **Almacenamiento de archivos (Supabase Storage)** | Incluido en los 64 GB arriba | $0 |
| **Dominio** | Namecheap .com | $1/mo |
| **Email transaccional (opcional)** | Supabase incluye 10k emails/mo gratis; si se necesita más, SendGrid free tier (100/día) o Mailgun (100/día) | $0‑$5 |
| **Total** |  | **≈ $26‑$31/mo** (con email gratis) – incluso si se necesita un plan de email pago, sigue bajo $40/mo. |

> **Escalabilidad**: Con 5k usuarios activos (asumiendo ~10 req/usuario/día y algunos websockets), el uso de DB y bandwidth queda muy por debajo de los límites del plan Pro. En caso de crecimiento inesperado, se puede subir a el plan “Team” ($59/mo) que duplica los recursos.

---

## 3️⃣ Stack Go (Gin) + React + Railway/Fly.io

### Arquitectura
- **Frontend**: React en Vercel (gratis) o Netlify.  
- **Backend**: API REST escrita en Go con el framework **Gin** (ligero, alto rendimiento). Desplegada como contenedor en **Railway** (plan “Hobby” gratis con límites) o **Fly.io** (plan “Shared‑CPU” $5/mo).  
- **Base de datos**: PostgreSQL gestionada por el mismo proveedor (Railway Postgres o Fly.io Postgres).  
- **Auth**: JWT generado en el endpoint de login; integración con Google/GitHub vía OAuth2 (librería `golang.org/x/oauth2`).  
- **Pagos**: Llamada a Stripe SDK Go desde los endpoints de checkout/webhook.  
- **Chat en tiempo real**: Servidor WebSocket usando **Gorilla WebSocket** (conexiones mantenidas en memoria; para escalar se necesita un broker como Redis Pub/Sub).  
- **Búsqueda**: PostgreSQL Full‑Text + `pg_trgm`.  
- **Admin panel**: Opción A) **Retool** (plan gratuito permite hasta 5 usuarios y recursos ilimitados – suficiente para un MVP). Opción B) Panel custom en React conectado a la misma API Go.  
- **CI/CD**: GitHub → Railway/Fly.io (despliegue automático).  

### Pros
| ✅ | Razón |
|---|-------|
| **Alto rendimiento** | Go es rápido y consume poca memoria; ideal si el MVP empieza a tener picos de tráfico. |
| **Control total del backend** | Puedes escribir lógica de negocio compleja, middlewares personalizados, y optimizar consultas sin depender de un BaaS. |
| **WebSocket nativo** | Gorilla WS es maduro y fácil de integrar; con Redis Pub/Sub puedes escalar a múltiples instancias. |
| **Costo bajo en etapas iniciales** | Railway ofrece una instancia gratuita con 500 hrs de CPU/mo (suficiente para bajo tráfico) y Postgres gratis hasta 10 GB. |
| **Admin rápido con Retool** | Retool permite crear paneles admin con arrastrar‑soltar y conectarlos directamente a tu API Go (sin escribir backend extra). |
| **Reutiliza habilidades** | El dev ya conoce Go básico; solo necesita profundizar en Gin y Gorilla WS (bastante documentación). |

### Contras
| ❌ | Razón |
|---|-------|
| **Más código de infra** | Necesitas escribir manejo de errores, validaciones, migraciones de DB (usando `golang-migrate` o similar), y configurar WS + Redis. |
| **Operación de WebSockets** | Para escalar más de una instancia, necesitas un broker (Redis) y sticky sessions o un servidor de mensajería (NATS, RabbitMQ). Esto añade complejidad. |
| **Admin menos “out‑of‑the‑box”** | Retool es gratuito pero tiene límites de usuarios y algunas funciones avanzadas solo en planes de pago; un panel custom requeriría más tiempo de desarrollo. |
| **Curva de aprendizaje de Go avanzada** | Aunque el dev conoce Go básico, construir una API robusta con middleware, testing y despliegue puede consumir tiempo extra dentro de las 6 sem. |
| **Menor ecosistema de auth listo** | No hay un paquete “all‑in‑one” como Django‑Allauth o Supabase Auth; tendrás que armar login, refresh de tokens, recuperación de contraseña, etc. |

### Estimación de costos mensuales (nivel “startup”)
| Servicio | Plan | Costo aprox. |
|----------|------|--------------|
| **Frontend (Vercel Hobby)** | Gratis | $0 |
| **Backend (Railway)** | Hobby gratis (500 hrs CPU/mo) → suficiente para < 500 usuarios; si crece, plan “Pay‑as‑you‑go” ~ $0.0005/CPU‑hr + $0.10/GB‑RAM‑hr. Estimado para 2 instancias pequeñas: $8‑$12/mo. | $8‑$12 |
| **PostgreSQL (Railway)** | Gratis hasta 10 GB, luego $0.10/GB‑mes. Para 5k usuarios, ~2 GB → sigue gratis. | $0 |
| **Redis (Upstash)** | Free tier (10k req/día) – si se necesita más, $8/mo para 100k req/día. Para chat ligero, el free suele alcanzar. | $0‑$8 |
| **Almacenamiento de archivos (AWS S3 compatible – Railway Storage)** | 5 GB gratis + $0.023/GB extra | ~$2 |
| **Dominio** | Namecheap .com | $1/mo |
| **Email transaccional** | SendGrid Free (100 emails/día) → suficiente para notificaciones básicas. | $0 |
| **Retool (Admin)** | Plan gratuito (hasta 5 usuarios, recursos ilimitados) → suficiente para el MVP. | $0 |
| **Total** |  | **≈ $11‑$23/mo** (con Redis gratis) – en el peor caso (Redis pago + backend ligeramente mayor) ~ $35/mo. |

> **Escalabilidad**: Si el tráfico supera los 500 usuarios simultáneos, basta con subir el plan de Railway a “Standard” ($5/mo por instancia) y añadir una segunda instancia; el costo sigue bajo $30/mo. El mayor riesgo es la gestión de WS a escala, pero con Upstash Redis (o un Redis gestionado de Fly.io) el sobrecoste sigue siendo bajo.

---

## Comparativa resumida

| Criterio | Django + React | Supabase + React | Go + React |
|----------|----------------|------------------|------------|
| **Velocidad de desarrollo** | Medio (más boilerplate) | **Alto** (menos código backend) | Medio‑alto (más código que Supabase, menos que Django) |
| **Curva de aprendizaje para el dev** | Baja (conoce Python) | Muy baja (solo JS/TS + poco Go) | Baja‑media (conoce Go básico, necesita profundizar) |
| **Control / personalización** | Alto | Medio (limitado por lo que Supabase expone) | Alto |
| **Costo mensual estimado** | $25‑$40 (con redis gratis) | $26‑$31 (plan Pro) | $11‑$35 (dependiendo de uso de Redis y backend) |
| **Escalabilidad automática** | Medio (necesita escalar contenedores y Redis) | **Alto** (Supabase escala DB y realtime) | Medio (escalado manual de instancias + Redis) |
| **Admin listo para usar** | **Django Admin** (poderoso, cero código) | React‑Admin (requiere definiciones) o Supabase Studio (limitado) | Retool (gratuito) o panel custom |
| **Chat en tiempo real** | Django Channels + Redis (más código) | Supabase Realtime (listo) | Gorilla WS + Redis (más código) |
| **Pagos** | Stripe SDK Python (directo) | Stripe SDK JS/TS o Edge Functions | Stripe SDK Go |
| **Búsqueda** | Postgres FT + pg_trgm (suficiente) | Igual | Igual |
| **Dependencia de terceros** | Media (proveedor de hosting) | **Alta** (Supabase) | Media (hosting + Redis opcional) |
| **Riesgo operativo** | Medio (gestionar DB, migraciones, WS) | Bajo (Supabase maneja mucho) | Medio‑alto (más piezas móviles: API, WS, Redis, auth) |

---

## Recomendación: **Supabase + React + Vercel**

### Por qué es la mejor opción para este MVP

| Factor | Justificación |
|--------|---------------|
| **Tiempo de desarrollo** | Con Supabase no necesitas escribir ni mantener un servidor de auth, ni configurar migraciones de DB, ni montar un servicio de WebSockets. El equipo de una persona puede enfocarse casi exclusivamente en la UI/UX y en la lógica de negocio (flujos de checkout, filtrado de servicios, notificaciones). Esto reduce drásticamente el riesgo de no cumplir con las 6 semanas. |
| **Costo predecible y bajo** | El plan **Pro de Supabase** ($25/mo) cubre cómodamente los requisitos de base de datos, almacenamiento, ancho de banda y funciones edge para varios miles de usuarios activos. Junto con Vercel (gratis) y un dominio barato, el total mensual se mantiene bajo **$35/mo**, muy por debajo del techo de $5k total (≈ $833/mo). Incluso dejando un margen para servicios de email o pequeños add‑ons, seguimos dentro del presupuesto. |
| **Escalabilidad sin fricción** | Supabase escala la capa de datos y el servicio Realtime automáticamente; solo se necesita subir de plan si se superan los límites (lo que ocurriría muy tarde en el ciclo de vida del MVP). No hay que preocuparse por re‑balancear shards, añadir réplicas o configurar clustering. |
| **Admin funcional rápidamente** | Con **React‑Admin** (o incluso usando directamente **Supabase Studio** para tareas simples) se puede tener un panel de administración totalmente funcional en menos de un día. Si más adelante se necesita algo más potente, se puede migrar a un admin custom sin cambiar la capa de datos. |
| **Seguridad y buenas prácticas listas para usar** | Supabase incluye Row Level Security (RLS), autenticación basada en JWT, manejo seguro de tokens de refresh y integración con proveedores OAuth (Google, GitHub, etc.) sin escribir código adicional. Esto reduce la superficie de ataque y el tiempo dedicado a probar auth. |
| **Aprovecha las habilidades existentes** | El desarrollador ya conoce React; solo necesita aprender el cliente de Supabase (JS/TS) y, opcionalmente, escribir algunas **Edge Functions** (en TypeScript/Deno) para proteger la clave secreta de Stripe o ejecutar webhooks. Esto es una curva de aprendizaje muy corta frente a aprender Django‑Channels o Gorilla WS desde cero. |
| **Menor riesgo operativo** | Al delegar auth, DB, storage y realtime a un proveedor especializado, se reducen las tareas de mantenimiento (backups, parches, monitorización de replicas, escalado de WS). El único componente que queda bajo control directo es el frontend y la lógica de pagos, ambas fáciles de testear y desplegar. |
| **Cumple con todos los requisitos** | - **Auth**: Supabase Auth (email/password, social, MFA opcional). <br> - **Pagos**: Stripe SDK llamado desde el frontend o desde una Edge Function (clave de API nunca expuesta). <br> - **Chat en tiempo real**: Supabase Realtime (basado en Postgres replication + WS). <br> - **Búsqueda**: Postgres Full‑Text + `pg_trgm` (suficiente para búsqueda de servicios por título, descripción, tags). <br> - **Admin panel**: React‑Admin conectado a la API PostgREST de Supabase (CRUD instantáneo, filtros, sorting, export). <br> - **Escalado esperado**: 500‑5000 usuarios → bien dentro de los límites del plan Pro. |

### Estimación de costos mensuales (desglosado)

| Concepto | Plan | Costo mensual |
|----------|------|---------------|
| **Frontend (Vercel Hobby)** | Gratis | $0 |
| **Supabase (Pro)** | 8 GB DB, 64 GB storage, 2 TB bandwidth, 500k Edge Function invocaciones | **$25** |
| **Dominio (.com)** | Namecheap / similar | $1 |
| **Email transaccional (SendGrid Free)** | 100 emails/día → suficiente para confirmaciones, resets de pwd | $0 |
| **Total estimado** |  | **≈ $26 / mes** |

> Incluso si en el futuro se necesita más de 500k invocaciones de Edge Functions (p.ej. webhooks de Stripe muy frecuentes), el siguiente salto de precio es el plan **Team** de Supabase ($59/mo) que duplica los recursos y sigue estando muy por debajo del límite presupuestario.

### Plan de trabajo sugerido (6 semanas)

| Semana | Objetivo principal | Tareas clave |
|--------|-------------------|--------------|
| 1 | **Setup y autenticación** | - Crear proyecto Supabase (DB, Auth). <br> - Configurar RLS para tablas `users`, `services`, `orders`, `messages`. <br> - Implementar login/registro con Supabase JS (email/password + Google). <br> - Protegiendo rutas privadas en React (PrivateRoute). |
| 2 | **Catálogo de servicios y búsqueda** | - Diseñar tabla `services` (title, description, price, category, location, owner_id). <br> - Subir datos de ejemplo. <br> - Implementar búsqueda full‑text + `pg_trgm` en el frontend (debounce, filtros). <br> - Paginación y sorting. |
| 3 | **Checkout y pagos** | - Integrar Stripe SDK (client‑side) para crear PaymentIntent. <br> - Crear endpoint Edge Function para validar y registrar la orden (usando la clave secreta de Stripe de forma segura). <br> - Webhook de Stripe → Edge Function para marcar orden como `completed` y notificar al vendedor. |
| 4 | **Chat en tiempo real** | - Habilitar Realtime en la tabla `messages`. <br> - Servicio de chat: escuchar cambios, mostrar mensajes, enviar nuevos mediante `supabase.from('messages').insert`. <br> - Persistencia de conversaciones y marcadores de leído. |
| 5 | **Admin panel** | - Instalar React‑Admin, crear recursos (`users`, `services`, `orders`, `messages`). <br> - Definir campos, filtros, acciones (ban user, refund order, etc.). <br> - Conectar a la URL PostgREST de Supabase (`https://<project>.supabase.co/rest/v1`). <br> - Ajustar permisos vía RLS para que solo admins (rol `admin`) puedan acceder a ciertas acciones. |
| 6 | **Pruebas, despliegue y monitorización** | - Tests de flujo completo (registro → publicar servicio → comprar → chat → reseña). <br> - Configurar logs en Vercel + Supabase (alertas de error). <br> - Optimizar imágenes (Next.js Image o lazy‑load). <br> - Documentar procesos de deploy y backup (Supabase permite backups automáticos). <br> - Handoff: crear checklist de operaciones mensuales (revisar usage, ajustar plan si es necesario). |

Con este plan, el desarrollador tiene un margen de aproximadamente **1‑2 días por semana** para imprevistos, revisión de código o mejoras de UI/UX.

---

## Conclusión

- **Django + React** brinda control total y un admin potente, pero implica más código backend y mayor carga operativa para una sola persona.  
- **Go + React** ofrece alto rendimiento y bajo costo inicial, pero requiere gestionar WebSockets, auth y un admin custom o Retool, lo que aumenta la complejidad operativa.  
- **Supabase + React** minimiza el trabajo de infraestructura, provee auth, DB, storage y realtime listos para usar, y permite lanzar un MVP funcional en menos tiempo y con un costo mensual muy bajo (< $35).  

Dado los ajustes de tiempo (6 sem), presupuesto ajustado ($5k total ≈ $833/mo) y la necesidad de que el producto sea fácil de mantener por una sola persona, **Supabase + React + Vercel** es la opción más equilibrada y recomendada. 

¡Éxito con tu marketplace! 🚀