# Qwen 3.8 2.4T (A95B) — reasoning/multi_constraint_decision

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 119.561s | tokens_per_second: 127.2
- input_tokens: 222 | output_tokens: 15206
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando una comparación detallada de opciones de stack tecnológico con pros y contras bien articulados.

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



## Recomendación rápida

Para ese MVP, yo elegiría:

> **Django + React + PostgreSQL + Redis + Stripe Connect + Django Channels**  
> Búsqueda inicial con **PostgreSQL Full Text Search**  
> Admin con **Django Admin**  
> Deploy simple en **Render / Railway / Hetzner + Postgres gestionado**

Es la opción más equilibrada para un equipo de **1 persona**, con presupuesto acotado, 6 semanas de timeline y requisitos de marketplace: auth, pagos, chat, búsqueda y admin panel.

Go lo dejaría descartado para este MVP salvo que el producto tenga una necesidad muy fuerte de concurrencia o performance desde el día 1, que no parece ser el caso.

---

# 1. Supuestos importantes

Antes de comparar stacks, asumo esto:

- **500 usuarios el primer mes** y **5,000 usuarios en 6 meses** probablemente signifiquen una concurrencia baja/moderada.
- No necesitas Kubernetes, microservicios, Elasticsearch ni arquitectura distribuida compleja.
- Los pagos deben resolverse con un proveedor serio: **Stripe Connect**, no un ledger propio complejo.
- La búsqueda puede comenzar con **PostgreSQL**, sin pagar Algolia/Elasticsearch.
- El chat en tiempo real puede ser simple: mensajes de texto, estado leído/no leído, notificaciones básicas.
- El admin panel debe requerir poco desarrollo custom.
- El stack debe ser mantenible por **1 fullstack dev**.

Con eso, la prioridad es:

> **Velocidad de entrega + bajo costo + poca complejidad operativa + facilidad de mantenimiento.**

---

# 2. Comparación de 3 opciones de stack

## Opción A: Django + React + PostgreSQL + Redis + Stripe Connect

### Stack sugerido

| Capa | Tecnología |
|---|---|
| Backend | Django 5 + Django REST Framework o Inertia.js |
| Frontend | React con Next.js, Vite o Inertia.js |
| Base de datos | PostgreSQL |
| Cache / colas / realtime | Redis |
| Chat | Django Channels + Redis |
| Pagos | Stripe Connect |
| Búsqueda | PostgreSQL Full Text Search + `pg_trgm` |
| Admin | Django Admin |
| Auth | Django Allauth |
| Storage | Cloudflare R2 / S3 compatible |
| Email | Resend / Postmark / Amazon SES |
| Monitoring | Sentry + logs básicos |
| Deploy | Render, Railway, Fly.io, Hetzner o DigitalOcean |

### Pros

- **Mejor fit con el equipo**: el dev sabe Python.
- Django trae muchas cosas resueltas:
  - Auth
  - Admin panel
  - ORM
  - Migrations
  - Formularios
  - Validaciones
  - Testing
  - Seguridad básica
- **Django Admin es una ventaja enorme** para un MVP de marketplace.
- Permite construir un **monolito mantenible**, que es ideal para 1 persona.
- PostgreSQL puede resolver búsqueda inicial sin pagar servicios externos.
- Stripe Connect se integra bien con Python.
- Redis + Django Channels puede manejar chat en tiempo real para 500-5,000 usuarios sin problemas si el MVP es simple.
- Es un stack barato de operar.
- Fácil de testear y evolucionar.
- Si luego necesitas separar servicios, puedes hacerlo modularmente.

### Contras

- Tienes que manejar backend y frontend como dos piezas, salvo que uses Inertia.js.
- Django Channels tiene una curva de aprendizaje pequeña/media.
- No es serverless; necesitas pensar un poco más en deploy, workers y Redis.
- Si quieres realtime muy robusto desde el día 1, puede requerir más trabajo que una solución managed.
- Para SEO avanzado, si usas Django como API + React SPA, necesitas cuidar SSR/hydration. Esto se resuelve usando Next.js o Inertia, pero agrega decisión técnica.

### Costo mensual estimado

#### Versión mínima / low cost

| Servicio | Costo aproximado |
|---|---:|
| VPS pequeño / app en Railway o Render | $5 - $25 |
| PostgreSQL gestionado | $10 - $25 |
| Redis gestionado o Upstash | $0 - $10 |
| Storage / CDN | $0 - $5 |
| Email transaccional | $0 - $20 |
| Monitoring básico | $0 - $10 |
| Dominio amortizado | $1 |
| **Total aproximado** | **$16 - $96/mes** |

#### Versión recomendada para producción

| Servicio | Costo aproximado |
|---|---:|
| Backend/app | $20 - $50 |
| PostgreSQL gestionado | $15 - $30 |
| Redis | $5 - $15 |
| Storage/CDN | $5 - $10 |
| Email | $15 - $25 |
| Sentry / logs | $0 - $30 |
| Dominio | $1 |
| **Total aproximado** | **$61 - $161/mes** |

Para 5,000 usuarios en 6 meses, yo presupuestaría:

> **$80 - $150/mes** para ir tranquilo.

Costo 6 meses:

> **$480 - $900**

---

## Opción B: Next.js + Supabase + Stripe Connect + Vercel

### Stack sugerido

| Capa | Tecnología |
|---|---|
| Frontend | Next.js |
| Backend | Supabase: Postgres + Auth + Storage + Realtime |
| Lógica server | Supabase Edge Functions / Next.js API routes |
| Pagos | Stripe Connect |
| Búsqueda | PostgreSQL Full Text Search |
| Chat | Supabase Realtime |
| Admin | Custom admin en Next.js o herramienta interna |
| Deploy | Vercel |
| Email | Resend / Postmark / Supabase Auth emails |
| Monitoring | Sentry / Vercel Analytics |

### Pros

- Muy rápido para lanzar MVP.
- Menos infraestructura propia.
- Supabase resuelve:
  - Auth
  - Base de datos
  - Storage
  - Realtime
  - Row Level Security
- Vercel simplifica deploy del frontend.
- Si el dev se siente cómodo con React/TypeScript, la experiencia de desarrollo puede ser muy buena.
- Buen fit si el producto es web-first y no quieres administrar servidores.
- Realtime integrado puede simplificar el chat básico.
- Costos iniciales bajos.

### Contras

- Para un marketplace con pagos, la lógica de negocio puede quedar dispersa:
  - Next.js API routes
  - Supabase Edge Functions
  - Row Level Security
  - Webhooks de Stripe
  - SQL functions
- El admin panel no viene resuelto como en Django; tendrás que construirlo.
- Stripe Connect con marketplace puede volverse más complejo de mantener si no tienes un backend tradicional claro.
- Mayor dependencia de Supabase/Vercel.
- Si necesitas reglas de negocio complejas, puede terminar siendo más difícil de mantener.
- Realtime es cómodo, pero debes controlar límites de uso.
- Si el dev no domina TypeScript o el ecosistema Next/Supabase, puede perder velocidad.
- Postgres FTS funciona, pero la búsqueda puede requerir más tuning que en Django con ORM.

### Costo mensual estimado

#### Versión mínima

| Servicio | Costo aproximado |
|---|---:|
| Vercel Hobby | $0 |
| Supabase Free | $0 |
| Stripe | $0 fijo |
| Email free tier | $0 |
| Dominio | $1 |
| **Total aproximado** | **$1/mes** |

Pero para producción yo no dependería solo de free tiers.

#### Versión recomendada

| Servicio | Costo aproximado |
|---|---:|
| Vercel Pro | $20 |
| Supabase Pro | $25 |
| Uso extra de Supabase/Realtime | $0 - $30 |
| Email | $0 - $20 |
| Storage/CDN extra | $0 - $10 |
| Monitoring | $0 - $30 |
| Dominio | $1 |
| **Total aproximado** | **$46 - $136/mes** |

Si agregas búsqueda externa o chat managed:

| Servicio | Costo aproximado |
|---|---:|
| Meilisearch/Typesense | $20 - $50 |
| Ably/Pusher/Stream Chat | $0 - $100+ |

Con extras:

> **$80 - $200/mes**

Costo 6 meses:

> **$480 - $1,200**

---

## Opción C: Go + React + PostgreSQL + Redis + WebSockets + Stripe

### Stack sugerido

| Capa | Tecnología |
|---|---|
| Backend | Go con Chi, Echo, Fiber o Gin |
| Frontend | React / Next.js |
| Base de datos | PostgreSQL |
| ORM/query | sqlc, GORM o pgx |
| Cache/colas | Redis |
| Chat | Gorilla WebSocket / nhooyr websocket / Redis pub-sub |
| Pagos | Stripe Go SDK |
| Búsqueda | PostgreSQL FTS o Meilisearch |
| Admin | Custom admin |
| Auth | Custom, Clerk, Auth0, Ory o Supabase Auth |
| Deploy | Fly.io, Render, Railway, Hetzner |

### Pros

- Excelente performance.
- Bajo consumo de recursos.
- Muy bueno para concurrencia.
- Binarios simples de desplegar.
- Puede ser muy barato en infraestructura.
- Si el producto escala mucho, Go aguanta bien.
- Buen lenguaje para servicios de chat, proxies, APIs de alto tráfico, etc.

### Contras

- El equipo solo tiene **Go básico**.
- Para 6 semanas, es riesgoso.
- No trae ecosystem “batteries included” como Django.
- Tendrás que construir o integrar manualmente:
  - Auth
  - Admin
  - Validaciones
  - Migraciones
  - Webhooks
  - Testing
  - Middleware
  - Sesiones/JWT
  - Rate limiting
  - Background jobs
- El admin panel será custom o requerirá una herramienta externa.
- La integración de pagos, chat y marketplace puede tomar más tiempo.
- Para un MVP de 1 persona, es probable que escribas más código del necesario.
- Go es excelente, pero aquí la prioridad es velocidad y mantenibilidad, no performance extrema.

### Costo mensual estimado

| Servicio | Costo aproximado |
|---|---:|
| App Go | $5 - $30 |
| PostgreSQL gestionado | $15 - $30 |
| Redis | $0 - $15 |
| Auth managed opcional | $0 - $50 |
| Storage/CDN | $0 - $10 |
| Email | $0 - $20 |
| Monitoring | $0 - $30 |
| Búsqueda opcional | $0 - $40 |
| Dominio | $1 |
| **Total aproximado** | **$21 - $226/mes** |

Versión razonable para producción:

> **$80 - $160/mes**

Costo 6 meses:

> **$480 - $960**

El problema principal no es el costo de infraestructura, sino el **costo de desarrollo y mantenimiento**.

---

# 3. Tabla comparativa rápida

| Criterio | Django + React | Next.js + Supabase | Go + React |
|---|---:|---:|---:|
| Fit con equipo actual | Alto | Medio/alto | Bajo |
| Velocidad para MVP | Alta | Muy alta | Media/baja |
| Facilidad de mantenimiento 1 persona | Muy alta | Alta | Media |
| Admin panel | Excelente con Django Admin | Hay que construirlo | Hay que construirlo |
| Auth | Muy bueno | Muy bueno | Requiere más trabajo |
| Pagos con Stripe Connect | Muy bueno | Bueno, pero más disperso | Bueno, pero más manual |
| Chat realtime | Bueno con Channels | Muy bueno con Supabase Realtime | Bueno, pero más trabajo |
| Búsqueda inicial | Muy buena con Postgres | Buena con Postgres | Buena con Postgres |
| Costo infra | Bajo | Bajo/medio | Bajo |
| Riesgo técnico | Bajo | Medio | Alto para este caso |
| Escala a 5,000 usuarios | Suficiente | Suficiente | Sobrado |
| Recomendación para este MVP | ✅ Sí | Alternativa válida | No recomendado ahora |

---

# 4. Mi recomendación: Django + React + PostgreSQL + Redis

## ¿Por qué Django?

Porque para este caso no necesitas el stack más moderno ni más performante. Necesitas el stack que te permita:

1. Lanzar en 6 semanas.
2. Gastar poco.
3. Mantenerlo fácilmente.
4. Resolver requisitos de marketplace sin sobreingeniería.
5. Tener un admin panel rápido.
6. No depender de múltiples servicios externos.

Django cumple muy bien con todo.

Además, el dev ya sabe Python. Eso reduce riesgo.

---

# 5. Arquitectura recomendada para el MVP

## Backend

- **Django 5**
- **Django REST Framework** si quieres API para React/Next.
- O **Inertia.js + React** si quieres una app más monolítica y simple.
- **Django Allauth** para auth con email, Google, etc.
- **PostgreSQL** como base principal.
- **Redis** para:
  - cache
  - colas simples
  - channel layer para WebSockets
- **Django Channels** para chat en tiempo real.
- **Celery o Django-RQ** para tareas background:
  - emails
  - webhooks de Stripe
  - notificaciones
  - generación de reportes
- **Django Admin** para backoffice.
- **Sentry** para errores.

## Frontend

Aquí tienes dos rutas:

### Ruta A: Django + Inertia.js + React

Recomendada si quieres máxima simplicidad.

Ventajas:

- No construyes una API completa.
- Usas rutas y controllers de Django.
- React como capa de UI.
- Menos duplicación entre backend/frontend.
- Muy bueno para MVP.

Desventajas:

- Menos preparado si luego necesitas app móvil nativa.
- Si necesitas SSR avanzado, hay que configurarlo bien.

### Ruta B: Django REST + Next.js

Recomendada si el SEO es crítico desde el inicio.

Ventajas:

- Mejor control de SEO.
- API lista para futura app móvil.
- Frontend moderno y flexible.

Desventajas:

- Más complejidad.
- Debes manejar auth, CORS, CSRF, tokens, estados de carga, etc.
- Dos deployments más claros: backend y frontend.

Para un marketplace de servicios, SEO puede importar. Pero para MVP, si el tráfico inicial viene de nicho, ads, redes o comunidad, no necesariamente necesitas SSR perfecto desde el día 1.

Mi recomendación práctica:

> Si quieres velocidad y simplicidad: **Django + Inertia + React**.  
> Si SEO público es clave desde el día 1: **Django REST + Next.js**.

---

# 6. Cómo resolver cada requisito

## Auth

Usa:

- Django Allauth
- Login con email/password
- Login con Google opcional
- Confirmación de email
- Reset password
- Roles básicos:
  - cliente
  - freelancer
  - admin

No inventes auth desde cero.

---

## Pagos

Usa:

> **Stripe Connect**

Para marketplace, no uses solo Stripe Checkout normal. Necesitas pensar en:

- Freelancer onboarding
- Cuentas Express o Standard
- Pagos del cliente
- Comisión de la plataforma
- Payouts al freelancer
- Refunds
- Disputes

Para MVP, yo usaría:

- Stripe Connect Express
- PaymentIntents o Checkout Sessions
- Application fee o destination charges
- Webhooks idempotentes
- Estados claros de orden:
  - pending
  - paid
  - in_progress
  - delivered
  - approved
  - completed
  - refunded
  - disputed

No construyas un sistema contable complejo al inicio. Apóyate en Stripe.

---

## Chat en tiempo real

Para MVP:

- Conversaciones entre cliente y freelancer.
- Mensajes de texto.
- Adjuntos simples opcionalmente.
- Read receipts.
- Notificación si el usuario no está conectado.

Implementación recomendada:

- Modelo `Conversation`
- Modelo `Message`
- Django Channels para WebSocket
- Redis como channel layer
- Postgres para persistencia

No necesitas:

- Kafka
- RabbitMQ
- Microservicio de chat
- WebRTC
- Video chat
- E2E encryption

Si más adelante el chat se vuelve crítico, puedes migrar a:

- Ably
- Pusher
- Stream Chat
- Supabase Realtime
- Firebase

Pero para MVP, Django Channels + Redis es suficiente.

---

## Búsqueda

No empieces con Elasticsearch ni Algolia.

Usa PostgreSQL:

- Full Text Search
- `pg_trgm`
- `unaccent`
- índices GIN
- filtros por:
  - categoría
  - precio
  - rating
  - disponibilidad
  - país
  - tags

Para 5,000 usuarios y probablemente unos pocos miles de listings, Postgres puede funcionar bien.

Si luego necesitas mejor relevancia, autocomplete o tolerancia a errores avanzada, agregas:

- Meilisearch
- Typesense
- Algolia

Pero no lo hagas desde el día 1.

---

## Admin panel

Django Admin puede cubrir:

- Usuarios
- Freelancers
- Servicios/listings
- Órdenes
- Pagos
- Conversaciones
- Reportes
- Disputas
- Flags
- Categorías
- Reviews
- Comisiones
- Feature flags

Puedes mejorarlo con:

- Django Jazzmin
- Django Admin Interface
- Acciones custom
- Filtros
- Búsquedas
- Read-only fields
- Permisos por rol

Esto ahorra fácilmente **1-2 semanas** de desarrollo.

---

# 7. Costos estimados de infraestructura mensual

## Opción recomendada: Django + React + Postgres + Redis

### Escenario barato

| Servicio | Costo |
|---|---:|
| Hetzner VPS / Railway / Render | $5 - $20 |
| Postgres gestionado | $10 - $20 |
| Redis | $0 - $10 |
| Storage | $0 - $5 |
| Email | $0 - $20 |
| Sentry free / logs básicos | $0 |
| Dominio | $1 |
| **Total** | **$16 - $76/mes** |

### Escenario recomendado para producción

| Servicio | Costo |
|---|---:|
| App backend | $20 - $50 |
| Postgres gestionado | $15 - $30 |
| Redis | $5 - $15 |
| Storage/CDN | $5 - $10 |
| Email | $15 - $25 |
| Sentry/logs | $10 - $30 |
| Dominio | $1 |
| **Total** | **$71 - $161/mes** |

### Presupuesto razonable para 6 meses

> **$500 - $1,000**

Dentro de un presupuesto de $5,000 para infra + herramientas, queda espacio para contingencia, herramientas pagadas o servicios externos.

---

## Opción Next.js + Supabase

### Escenario recomendado

| Servicio | Costo |
|---|---:|
| Vercel Pro | $20 |
| Supabase Pro | $25 |
| Uso extra | $0 - $30 |
| Email | $0 - $20 |
| Storage/CDN | $0 - $10 |
| Monitoring | $0 - $30 |
| Dominio | $1 |
| **Total** | **$46 - $136/mes** |

### Con servicios externos de búsqueda/chat

| Servicio | Costo |
|---|---:|
| Meilisearch/Typesense | $20 - $50 |
| Ably/Pusher/Stream | $0 - $100+ |
| **Total con extras** | **$80 - $250/mes** |

### Presupuesto razonable para 6 meses

> **$450 - $1,500**

---

## Opción Go + React

### Escenario recomendado

| Servicio | Costo |
|---|---:|
| App Go | $10 - $30 |
| Postgres gestionado | $15 - $30 |
| Redis | $5 - $15 |
| Auth managed opcional | $0 - $50 |
| Storage/CDN | $0 - $10 |
| Email | $0 - $20 |
| Monitoring | $0 - $30 |
| Dominio | $1 |
| **Total** | **$31 - $186/mes** |

### Presupuesto razonable para 6 meses

> **$450 - $1,000**

Pero el costo real más alto es el tiempo de desarrollo.

---

# 8. Presupuesto total aproximado para 6 meses

Para la opción recomendada:

| Concepto | Costo estimado |
|---|---:|
| Infraestructura mensual | $80 - $150 |
| 6 meses de infra | $480 - $900 |
| Dominio | $10 - $20 anual |
| Email | $0 - $150 |
| Monitoring | $0 - $150 |
| Storage/CDN | $0 - $60 |
| Herramientas dev | $0 - $200 |
| Contingencia | $300 - $700 |
| **Total aproximado** | **$800 - $2,200** |

Esto deja margen dentro de los **$5,000**.

Importante:

> Las comisiones de Stripe no son infraestructura fija, pero afectan el modelo de negocio. Normalmente serán un porcentaje por transacción más un fee fijo. Debes incluirlas en tu pricing.

---

# 9. Qué stack elegir según tu prioridad

## Elige Django + React si:

- Quieres máxima velocidad con Python.
- Quieres admin panel rápido.
- Quieres un backend claro y mantenible.
- Quieres controlar pagos, usuarios, órdenes y admin sin depender demasiado de servicios externos.
- Quieres bajo costo.
- Quieres algo robusto pero simple.

Esta es mi recomendación principal.

---

## Elige Next.js + Supabase si:

- El dev se siente muy cómodo con React/TypeScript.
- Quieres minimizar backend propio.
- Quieres auth, storage y realtime managed.
- El MVP es relativamente simple.
- No tienes lógica de pagos muy compleja.
- Prefieres Vercel + Supabase antes que mantener Django.

Es una buena alternativa, pero para marketplace con pagos y admin, Django me parece más sólido para 1 persona.

---

## Elige Go + React si:

- Ya tienes experiencia real con Go.
- El producto requiere alta concurrencia desde el inicio.
- Tienes más tiempo de desarrollo.
- Puedes construir auth, admin, pagos y chat sin frameworks batteries-included.
- El equipo no es de 1 persona o el dev es muy fuerte en backend.

Para tu caso actual, **no lo recomiendo**.

---

# 10. Stack concreto que yo usaría

Si yo fuera el responsable de este MVP, usaría:

```text
Backend:
- Python 3.12
- Django 5
- Django REST Framework o Inertia.js
- Django Allauth
- Django Channels
- Redis
- Celery o Django-RQ
- Stripe Python SDK

Base de datos:
- PostgreSQL 16
- pg_trgm
- unaccent
- Full Text Search

Frontend:
- React
- Tailwind CSS
- shadcn/ui
- TanStack Query
- Inertia.js o Next.js

Pagos:
- Stripe Connect
- Stripe Checkout
- Webhooks idempotentes

Chat:
- Django Channels
- Redis pub/sub
- Postgres para mensajes

Búsqueda:
- PostgreSQL FTS

Admin:
- Django Admin
- Jazzmin opcional

Storage:
- Cloudflare R2 o S3 compatible

Email:
- Resend o Postmark

Monitoring:
- Sentry
- Uptime check básico

Deploy:
- Render/Railway para simplicidad
o
- Hetzner + Docker Compose + Coolify para menor costo
```

---

# 11. Plan de 6 semanas

## Semana 1: Fundación

- Setup de repo
- Auth
- Modelos principales:
  - User
  - Profile
  - ServiceListing
  - Category
  - Order
- Django Admin básico
- Configuración de entorno
- Deploy inicial
- Sentry

Entregable:

> Usuarios pueden registrarse, iniciar sesión y ver perfiles básicos.

---

## Semana 2: Marketplace y listings

- CRUD de servicios
- Subida de imágenes
- Categorías
- Filtros básicos
- Búsqueda con Postgres
- Página pública de servicio
- Página de perfil freelancer

Entregable:

> Usuarios pueden publicar y descubrir servicios.

---

## Semana 3: Pagos y órdenes

- Integración Stripe Connect
- Onboarding de freelancer
- Checkout
- Webhooks
- Estados de orden
- Comisión de plataforma
- Página de compra
- Historial de órdenes

Entregable:

> Cliente puede pagar un servicio y el sistema registra la orden correctamente.

---

## Semana 4: Chat en tiempo real

- Modelo de conversación
- Modelo de mensajes
- WebSocket con Django Channels
- Redis channel layer
- UI de chat
- Notificación básica
- Read receipts simple

Entregable:

> Cliente y freelancer pueden chatear dentro de la plataforma.

---

## Semana 5: Admin, reviews y pulido

- Admin avanzado
- Moderación de listings
- Manejo de órdenes
- Refunds básicos
- Reviews simples
- Validaciones
- Responsive
- Emails transaccionales
- SEO básico

Entregable:

> MVP más usable, administrable y presentable.

---

## Semana 6: Testing, deploy final y lanzamiento

- Tests críticos:
  - auth
  - pagos
  - órdenes
  - chat
- Backups
- Logging
- Rate limiting
- Seguridad básica
- Staging
- Producción
- Monitoreo
- Corrección de bugs

Entregable:

> MVP lanzable.

---

# 12. Cosas que evitaría para no quemar presupuesto

No hagas esto en el MVP:

- Microservicios
- Kubernetes
- Elasticsearch
- Kafka
- RabbitMQ
- App móvil nativa
- Sistema de recomendaciones complejo
- Chat con video
- Wallet interna compleja
- Ledger contable propio
- Multi-región
- Machine learning
- Admin panel custom desde cero si Django Admin sirve
- Búsqueda externa pagada antes de validar el producto
- Infraestructura serverless compleja para lógica de marketplace

---

# 13. Decisión final

## Recomendación principal

> **Django + React + PostgreSQL + Redis + Stripe Connect + Django Channels**

### ¿Por qué?

Porque es el stack que mejor balancea:

- Conocimiento del equipo
- Velocidad de desarrollo
- Costo bajo
- Mantenibilidad por 1 persona
- Admin panel rápido
- Capacidad suficiente para 5,000 usuarios
- Flexibilidad para evolucionar

### Alternativa válida

> **Next.js + Supabase + Stripe Connect**

Si el dev prefiere TypeScript, quiere menos backend propio y el MVP tiene lógica de negocio no demasiado compleja.

### No recomendado para este caso

> **Go + React**

No porque Go sea malo, sino porque para 6 semanas, 1 dev, presupuesto limitado y requisitos de marketplace, te obligaría a construir demasiado manualmente. Es una excelente tecnología, pero no es la mejor para este MVP.

---

# 14. Resumen ejecutivo

| Decisión | Recomendación |
|---|---|
| Backend | Django |
| Frontend | React con Inertia.js o Next.js |
| Base de datos | PostgreSQL |
| Cache/colas/realtime | Redis |
| Chat | Django Channels |
| Pagos | Stripe Connect |
| Búsqueda | PostgreSQL Full Text Search |
| Admin | Django Admin |
| Deploy | Render/Railway o Hetzner |
| Costo infra mensual estimado | $70 - $150 |
| Costo 6 meses estimado | $500 - $1,000 |
| Mejor opción para 1 dev | Sí |
| Riesgo técnico | Bajo |
| Escalabilidad para 5,000 usuarios | Suficiente |

En una frase:

> Para este MVP, yo apostaría por un **monolito Django bien modularizado**, frontend React, PostgreSQL, Redis, Stripe Connect y Django Admin. Es aburrido en el buen sentido: barato, mantenible, productivo y suficiente para la escala esperada.