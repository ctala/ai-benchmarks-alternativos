# Claude Haiku 5.5 — reasoning/multi_constraint_decision

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 29.372s | tokens_per_second: 196.1
- input_tokens: 282 | output_tokens: 5759
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

# Stack para MVP de marketplace freelance de nicho

## Requisitos clave que condicionan la decisión

- **Chat en tiempo real** y **auth** son las partes más propensas a errores de seguridad o a consumir semanas si se construyen desde cero.
- **Pagos tipo marketplace** (Stripe Connect: cobrar al cliente, retener comisión, pagar al freelancer, onboarding y KYC) son complejos sin importar el stack.
- **1 desarrollador** en **6 semanas** significa que cada componente que tengas que operar y mantener cuenta contra ti.

## Las 3 opciones

### Opción A: Next.js + Supabase + Stripe Connect (BaaS)

**Arquitectura:** Next.js (React/TypeScript) en Vercel. Supabase aporta PostgreSQL, Auth, Realtime (chat), Storage y Row Level Security. Stripe Connect para pagos. Búsqueda con Postgres full-text (`tsvector`, `pg_trgm`). Admin con Supabase Studio más una ruta `/admin` protegida.

| Pros | Contras |
|---|---|
| Auth, chat en tiempo real y storage salen de la caja | Lock-in parcial con Supabase (mitigado porque es Postgres estándar) |
| Menos código de backend que mantener | RLS tiene curva de aprendizaje y errores de config son peligrosos |
| Next.js es React: aprovechas lo que ya sabes | Lógica de negocio pesada en TypeScript, no en Python |
| Un solo repo, un solo deploy | Límites de conexiones concurrentes en Realtime (suficiente para el alcance, pero hay que vigilarlo) |
| Escala a miles de usuarios sin rediseño | Menos control fino sobre infraestructura |

### Opción B: React (Vite) + FastAPI + PostgreSQL self-hosted + Stripe Connect

**Arquitectura:** SPA en React, API en FastAPI, PostgreSQL, Redis y WebSockets nativos de FastAPI para el chat, Meilisearch para búsqueda, Refine o React-admin para el panel. Todo en un VPS (Hetzner, DigitalOcean) con Docker Compose. Auth con `fastapi-users` o Clerk.

| Pros | Contras |
|---|---|
| Control total y lógica en Python | Tú operas todo: backups, seguridad, SSL, actualizaciones, monitoreo |
| Barato en infraestructura | Implementar auth y WebSockets con reconexión y presencia toma semanas |
| Sin lock-in de proveedor | Más piezas móviles (API, DB, Redis, Meilisearch, frontend) para 1 persona |
| FastAPI es rápido de escribir y documentar | Riesgo alto de que el chat y auth consuman el timeline de 6 semanas |

### Opción C: Django monolítico + Django Channels + PostgreSQL + Stripe

**Arquitectura:** Django con Django REST Framework para la API, Django Channels + Redis para el chat, `django-allauth` para auth, Django Admin para el panel, búsqueda con `SearchVector` de PostgreSQL. Frontend en React consumiendo la API, o HTMX si quieres evitar el doble stack.

| Pros | Contras |
|---|---|
| Django Admin te da un panel completo casi gratis (requisito cubierto) | Channels + Redis es más complejo de lo que parece |
| Auth, permisos, migraciones y ORM maduros | Mantener frontend React separado + backend Django duplica esfuerzo |
| Todo en Python, idioma que dominas | Menos moderno para UX tipo app (sin HMR/SPA natural si usas templates) |
| Monolito fácil de desplegar y entender | Escalar el chat requiere tuning de ASGI y Redis |

**Descartado: Go.** Tienes nivel básico. En 6 semanas, con auth, pagos y chat, aprender Go mientras construyes el producto es un riesgo que no conviene asumir.

---

## Costos de infraestructura mensual estimados (USD)

| Concepto | Opción A | Opción B | Opción C |
|---|---|---|---|
| Hosting frontend/backend | Vercel Pro ~$20 | VPS Hetzner ~$10–15 | Render/Railway ~$25–40 |
| Base de datos | Supabase Pro ~$25 (incluye auth, realtime, storage) | Incluida en VPS, backups S3 ~$3–5 | Postgres gestionado ~$10–15 |
| Chat/realtime | Incluido | Redis incluido en VPS | Redis gestionado ~$10 |
| Auth | Incluido | Clerk gratis hasta 10k MAU o $0 self-built | Incluido (allauth) |
| Búsqueda | Postgres FTS $0 | Meilisearch self-hosted $0 | Postgres FTS $0 |
| Email transaccional | Resend ~$0–20 | Resend ~$0–20 | Resend ~$0–20 |
| Monitoreo (Sentry, uptime) | ~$0–26 | ~$0–26 | ~$0–26 |
| Dominio + Cloudflare | ~$2 | ~$2 | ~$2 |
| **Total aprox. (sin Stripe)** | **~$50–95/mes** | **~$25–60/mes** | **~$50–100/mes** |

**Stripe** cobra por transacción (~2.9% + $0.30 en tarjetas) y Connect agrega fees por payouts y, en algunas regiones, por cuenta activa. Verifica el pricing vigente porque cambia. Estos cargos salen de la comisión del marketplace, no del presupuesto de infra.

**Proyección a 6 meses:** con la Opción A, unos $60–100/mes son ~$400–600 en infra. Con herramientas (dominio, email, monitoreo) cabes holgadamente en los $5,000, incluso con un colchón para pruebas, legal básico y servicios de terceros.

---

## Comparación resumida

| Criterio (peso) | A: Next + Supabase | B: FastAPI self-hosted | C: Django |
|---|---|---|---|
| Velocidad para MVP en 6 semanas (alto) | ★★★★★ | ★★ | ★★★★ |
| Facilidad de mantenimiento por 1 persona (alto) | ★★★★ | ★★ | ★★★★ |
| Cubre auth + chat + admin sin trabajo extra (alto) | ★★★★★ | ★★ | ★★★★ |
| Afinidad con tu stack (medio) | ★★★★ (React) | ★★★★ (React + Python) | ★★★ (Python, pero frontend duplicado) |
| Costo mensual (medio) | ★★★ | ★★★★★ | ★★★ |
| Control y portabilidad (medio) | ★★★ | ★★★★★ | ★★★★ |
| Escala a 5k usuarios (medio) | ★★★★ | ★★★★ | ★★★★ |

---

## Recomendación: Opción A (Next.js + Supabase + Stripe Connect)

**Justificación:**

1. **Los dos componentes más riesgosos ya están resueltos.** Auth y chat en tiempo real son las partes que más tiempo consumen y más fallan. Supabase te los da probados, así que tus 6 semanas van al producto de nicho.
2. **Mantenimiento mínimo para una persona.** Sin servidores que parchear, sin Redis que monitorear, sin backups manuales. Un repo, un deploy.
3. **Aprovechas lo que ya sabes.** React domina el frontend y Next.js te da API routes o server actions para la lógica que no quieras exponer.
4. **La escala no es un problema.** 5,000 usuarios en 6 meses es un volumen cómodo para Supabase Pro y Vercel Pro. Si algún día necesitas más, migras a un VPS con Postgres sin reescribir la app, porque Postgres es el núcleo.
5. **Costo predecible y bajo.** Entre $50 y $100 al mes, muy por debajo del presupuesto.

**Cuándo elegiría otra opción:**
- Si la lógica de negocio (matching, scoring, reglas de pago complejas) es muy pesada y quieres Python, elige **C (Django)**.
- Si necesitas control total por regulación de datos o quieres evitar proveedores, elige **B**, pero acepta que las 6 semanas se vuelven 8–10.

---

## Riesgos a vigilar con la recomendación

- **RLS mal configurado** puede exponer datos entre usuarios. Escribe tests de políticas desde el día 1.
- **Stripe Connect** es la parte más compleja del proyecto. Usa Express con onboarding hospedado por Stripe y no intentes construir el KYC tú mismo.
- **Límites de Supabase Realtime:** mide conexiones concurrentes antes del lanzamiento.
- **Lock-in:** mantén la lógica de negocio en funciones TypeScript y el esquema en migraciones SQL versionadas, para que la migración futura sea viable.

---

## Plan sugerido de 6 semanas

| Semana | Entregable |
|---|---|
| 1 | Setup (Next.js, Supabase, CI), esquema de datos, auth con roles (cliente, freelancer, admin) |
| 2 | Perfiles de freelancers, publicación de servicios, Storage para portafolios |
| 3 | Búsqueda con filtros y paginación; flujo de contratación (orden) |
| 4 | Stripe Connect: onboarding de freelancers, cobro, retención de comisión, payouts |
| 5 | Chat en tiempo real ligado a órdenes, notificaciones por email |
| 6 | Panel admin (moderación, órdenes, disputas básicas), pruebas de RLS y pagos, deploy y beta cerrada |

Si quieres, puedo bajar esto a un esquema de base de datos concreto con políticas RLS, o a una estructura de carpetas para el proyecto.