# Qwen 3.8 27B — reasoning/multi_constraint_decision

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.77 | quality: 10.0
- latency_total: 1278.768s | tokens_per_second: 18.4
- input_tokens: 222 | output_tokens: 23523
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



## Respuesta corta

Con tus restricciones —**$5,000 total**, **6 semanas**, **1 dev fullstack**, producto tipo **marketplace freelance**, y necesidad de ser **mantenible por una sola persona**— mi recomendación es:

> **Stack recomendado: Next.js + Supabase + Stripe Connect + Vercel**, usando **Postgres full-text search** para búsqueda y **Supabase Realtime** para chat.

Es la opción que mejor equilibra:

- velocidad de entrega en 6 semanas,
- baja infraestructura,
- facilidad de mantenimiento para 1 persona,
- costos bajos,
- escalabilidad suficiente para 500 usuarios el primer mes y 5,000 en 6 meses.

Una estimación razonable de infra + herramientas sería:

| Escenario | Costo mensual estimado |
|---|---:|
| Primer mes / 500 usuarios | **$50 - $120 USD** |
| Mes 6 / 5,000 usuarios | **$100 - $200 USD** |
| 6 meses totales | **$500 - $1,200 USD** |

Con eso te quedas muy dentro de los **$5,000**, dejando margen para imprevistos, herramientas opcionales o pruebas.

---

# 1. Supuestos que asumí

Para comparar bien, asumí:

- El producto es un **marketplace web**, no app móvil nativa.
- 5,000 usuarios en 6 meses significa **usuarios registrados**, no 5,000 usuarios concurrentes chateando al mismo tiempo.
- Necesitas:
  - auth de usuarios,
  - perfiles de comprador y vendedor,
  - listado de servicios,
  - búsqueda,
  - pedidos,
  - pagos con Stripe,
  - chat por pedido,
  - panel admin.
- No necesitas microservicios, Kubernetes, AWS complex, ni arquitectura enterprise.
- El dev sabe **React**, **Python** y **básico de Go**, pero no necesariamente es experto en infraestructura.

---

# 2. Comparativa de 3 opciones de stack

## Opción A: Next.js + Supabase + Stripe Connect

### Stack

- **Frontend:** Next.js / React
- **Backend / DB:** Supabase
  - PostgreSQL
  - Auth
  - Storage
  - Realtime
  - Row Level Security
  - Edge Functions opcional
- **Pagos:** Stripe / Stripe Connect
- **Búsqueda:** Postgres full-text search
- **Chat:** Supabase Realtime
- **Admin:** Supabase Studio + panel admin interno en Next.js
- **Deploy frontend:** Vercel
- **Email:** Resend, Postmark o SendGrid
- **Monitoring:** Sentry free tier

### Pros

- **Muy rápido para 6 semanas.**
- Auth, DB, storage y realtime ya vienen resueltos.
- PostgreSQL es ideal para un marketplace:
  - usuarios,
  - servicios,
  - pedidos,
  - mensajes,
  - vendedores,
  - reviews.
- Postgres full-text search es suficiente para MVP.
- Baja infraestructura.
- Fácil de mantener por 1 persona.
- Escala bien para 500 y hasta 5,000 usuarios.
- Costos bajos.
- Supabase te da dashboard, logs, DB, auth, storage y realtime en un solo lugar.

### Contras

- El backend va a estar más orientado a **SQL, RLS, TypeScript/JavaScript o Edge Functions**, no a Python.
- Si el dev es mucho más cómodo en Python que en TypeScript, hay una pequeña curva.
- Supabase puede dar sensación de “caja negra” al principio.
- Row Level Security, si se usa mal, puede ser doloroso.
- Hay cierta dependencia de Supabase, aunque puedes exportar el PostgreSQL y salir.

### Costos mensuales estimados

| Componente | 500 usuarios | 5,000 usuarios |
|---|---:|---:|
| Vercel Hobby / Pro | $0 - $20 | $20 |
| Supabase Free / Pro | $0 - $25 | $25 - $50 |
| Email transaccional | $0 - $20 | $0 - $20 |
| Búsqueda avanzada opcional | $0 | $0 - $20 |
| Dominio | ~$1 | ~$1 |
| Monitoring / uptime | $0 | $0 |
| Buffer por almacenamiento / incidentes | $20 - $50 | $50 - $100 |
| **Total estimado** | **$21 - $136** | **$96 - $211** |

En números redondos:

| Escenario | Mensual |
|---|---:|
| MVP / 500 usuarios | **$50 - $120** |
| Crecimiento / 5,000 usuarios | **$100 - $200** |

Para 6 meses:

| Escenario | 6 meses |
|---|---:|
| Conservador | **$300 - $700** |
| Con crecimiento y buffer | **$600 - $1,200** |

### Veredicto

Es la mejor opción para **MVP en 6 semanas con 1 persona**.

---

## Opción B: React + Django + DRF + Channels + PostgreSQL + Redis

### Stack

- **Frontend:** React / Next.js
- **Backend:** Django + Django REST Framework
- **Realtime:** Django Channels + Redis
- **DB:** PostgreSQL
- **Pagos:** Stripe / Stripe Connect
- **Búsqueda:** PostgreSQL full-text search
- **Admin:** Django Admin
- **Deploy:** Render, Railway, Fly.io o VPS
- **Email:** Resend / Django email
- **Monitoring:** Sentry

### Pros

- Todo el backend en **Python**, que es una de tus fortalezas.
- Django Admin es una ventaja enorme.
- ORM maduro, migrations, formularios, auth, admin, seguridad.
- Muy bueno para reglas de negocio complejas.
- PostgreSQL natural.
- Puedes tener un backend muy sólido a mediano plazo.

### Contras

- Más piezas:
  - app Django,
  - PostgreSQL,
  - Redis,
  - worker opcional,
  - frontend,
  - websockets.
- Django Channels en producción puede ser más complicado que un realtime BaaS.
- Más infraestructura para mantener.
- Con 6 semanas, puede ser **demasiado** si además necesitas Stripe Connect, chat, búsqueda, admin panel y auth.
- Más riesgo de delay.
- Más debugging:
  - asgi,
  - redis,
  - websocket,
  - deploy,
  - workers.

### Costos mensuales estimados

| Componente | 500 usuarios | 5,000 usuarios |
|---|---:|---:|
| App Django en Render/Railway/Fly | $7 - $25 | $20 - $50 |
| PostgreSQL | $10 - $25 | $25 - $50 |
| Redis | $5 - $10 | $10 - $20 |
| Frontend en Vercel/Pages | $0 - $20 | $0 - $20 |
| Email | $0 - $20 | $0 - $20 |
| Buffer | $10 - $20 | $20 - $40 |
| **Total estimado** | **$32 - $120** | **$75 - $200** |

En redondos:

| Escenario | Mensual |
|---|---:|
| MVP / 500 usuarios | **$30 - $100** |
| 5,000 usuarios | **$80 - $180** |

Para 6 meses:

| Escenario | 6 meses |
|---|---:|
| Conservador | **$250 - $600** |
| Con buffer | **$500 - $1,100** |

### Veredicto

Es una buena opción si:

- puedes extenderte a **8-10 semanas**,
- quieres backend en Python,
- valoras mucho Django Admin,
- el marketplace tendrá reglas de negocio complejas desde el inicio.

Pero para **6 semanas con 1 persona**, es más riesgosa que la opción A.

---

## Opción C: React + Go API + PostgreSQL + Redis + VPS / Railway

### Stack

- **Frontend:** React / Next.js
- **Backend:** Go
  - Chi, Fiber o Echo
  - JWT / auth propio o biblioteca
  - WebSockets con gorilla/websocket o similar
- **DB:** PostgreSQL
- **Realtime:** WebSockets + Redis opcional
- **Pagos:** Stripe / Stripe Connect
- **Búsqueda:** PostgreSQL full-text search
- **Admin:** panel custom
- **Deploy:** Hetzner, DigitalOcean, Railway, Render, Fly.io

### Pros

- Infraestructura muy barata.
- Go es eficiente.
- Un solo binario de backend.
- Excelente rendimiento.
- Bajo consumo de recursos.
- Muy escalable.

### Contras

- Con **básico de Go**, probablemente sea demasiado ambiciosa para 6 semanas.
- Tendrías que construir más manualmente:
  - auth,
  - websockets,
  - admin,
  - búsqueda,
  - webhooks de Stripe,
  - roles,
  - permisos,
  - errores,
  - testing.
- Más código = más mantenimiento.
- No tienes un admin panel gratuito como Django Admin.
- Más tiempo en debugging.
- Mayor riesgo de no llegar a lanzamiento.

### Costos mensuales estimados

| Componente | 500 usuarios | 5,000 usuarios |
|---|---:|---:|
| VPS o servicio gestionado | $5 - $30 | $20 - $60 |
| PostgreSQL | $0 - $20 | $15 - $50 |
| Redis | $0 - $10 | $5 - $20 |
| Frontend | $0 - $20 | $0 - $20 |
| Email | $0 - $20 | $0 - $20 |
| Buffer | $10 | $20 - $50 |
| **Total estimado** | **$15 - $100** | **$60 - $220** |

En redondos:

| Escenario | Mensual |
|---|---:|
| MVP / 500 usuarios | **$10 - $60** |
| 5,000 usuarios | **$50 - $120** |

Para 6 meses:

| Escenario | 6 meses |
|---|---:|
| Bajo costo | **$100 - $400** |
| Con buffer | **$300 - $700** |

### Veredicto

Es la opción más barata, pero **no es la más recomendable para un MVP de 6 semanas**.

Usa Go si:

- tienes tiempo extra,
- quieres aprender en producción,
- el producto ya está validado,
- o necesitas performance extrema desde el inicio.

Para tu caso, Go aumentaría el riesgo de no lanzar.

---

# 3. Matriz de decisión

Peso de criterios:

| Criterio | Peso |
|---|---:|
| Velocidad para 6 semanas | 35% |
| Mantenibilidad por 1 persona | 25% |
| Costo | 15% |
| Ajuste a tus skills | 15% |
| Escalabilidad a 5,000 usuarios | 10% |

| Opción | Velocidad | Mantenibilidad | Costo | Skills | Escala | Ponderado |
|---|---:|---:|---:|---:|---:|---:|
| A. Next.js + Supabase + Stripe | 5 | 5 | 4 | 4 | 4 | **4.60** |
| B. Django + React + Channels | 3 | 3 | 4 | 5 | 4 | **3.55** |
| C. Go + React + Postgres | 2 | 3 | 5 | 3 | 5 | **3.15** |

Ganadora: **Opción A**.

---

# 4. Por qué recomiendo Next.js + Supabase + Stripe Connect

## 4.1 Es lo más rápido para 6 semanas

Un marketplace freelance típico requiere:

- registro,
- login,
- perfil de usuario,
- perfil de vendedor,
- listado de servicios,
- categorías,
- filtros,
- búsqueda,
- carrito o pedido simple,
- checkout,
- estado del pedido,
- chat entre comprador y vendedor,
- panel admin,
- emails,
- pagos.

Con Supabase ya resuelves varios frentes a la vez:

- PostgreSQL,
- Auth,
- Storage para imágenes,
- Realtime para chat,
- RLS para permisos,
- Dashboard de administración.

No tienes que montar auth desde cero.
No tienes que montar websockets desde cero.
No tienes que montar storage desde cero.
No tienes que montar backups manuales.
No tienes que gestionar servidores.

---

## 4.2 Un marketplace es relacional

El modelo natural es:

- users
- profiles
- services
- orders
- messages
- reviews
- payments
- admin actions

PostgreSQL es perfecto para esto.

Con NoSQL o Firebase podrías hacerlo, pero:

- consultas de reporte son más incómodas,
- relaciones complejas son más difíciles,
- búsqueda avanzada requiere servicio externo,
- admin panel se vuelve menos natural,
- costos pueden ser menos predecibles.

Para un marketplace, **SQL es la opción más saneada**.

---

## 4.3 Chat en tiempo real sin complicarte

Para MVP, el chat no debe ser una red social.

Debe ser simple:

- chat por pedido,
- solo comprador y vendedor,
- texto plano,
- historial persistente,
- notificación de nuevo mensaje,
- posiblemente “visto” básico.

Con Supabase Realtime puedes hacer:

- insertar mensaje en PostgreSQL,
- broadcast del mensaje a un channel por order_id,
- que el frontend reciba el mensaje en tiempo real.

No necesitas Ably, Pusher, Socket.io, Redis o un servidor websocket propio para el MVP.

---

## 4.4 Búsqueda suficiente para MVP

Para 500 a 5,000 usuarios, no necesitas Elasticsearch.

Postgres full-text search es suficiente.

Puedes buscar por:

- título del servicio,
- descripción,
- tags,
- skills,
- categoría,
- precio,
- rating,
- estado del vendedor.

Ejemplo conceptual:

```sql
UPDATE services
SET search_vector = to_tsvector(
  'spanish',
  coalesce(title, '') || ' ' || coalesce(description, '') || ' ' || coalesce(tags, '')
);

CREATE INDEX idx_services_search_vector
ON services USING GIN(search_vector);
```

Luego consultas con algo similar a:

```sql
SELECT *
FROM services
WHERE search_vector @@ websearch_to_tsquery('spanish', $query)
AND status = 'active'
ORDER BY rank DESC;
```

Si en 1-2 meses la búsqueda se queda corta, puedes agregar:

- Meilisearch,
- Typesense,
- Algolia.

Pero para MVP, **no empieces con eso**.

---

## 4.5 Pagos: Stripe Connect es clave

Como es un marketplace freelance, probablemente necesitas pagar a los vendedores.

No basta con Stripe Checkout simple si la plataforma toma comisión.

Deberías usar:

### Stripe Connect

Opciones:

1. **Standard Account**
   - El vendedor tiene su cuenta Stripe.
   - Tú le pasas los pagos.
   - Es lo más fácil.

2. **Express Account**
   - UX un poco más integrada.
   - Más control que Standard.
   - Aun así, relativamente simple.

3. **Custom Account**
   - Más control.
   - Más complejo.
   - No lo usaría en MVP de 6 semanas.

Para MVP te recomiendo:

> **Stripe Connect Standard o Express + application fee.**

Flujo básico:

1. Vendedor se registra.
2. Vendedor completa onboarding de Stripe Connect.
3. Comprador paga un servicio.
4. Stripe crea payment intent.
5. La comisión de la plataforma se toma con `application_fee_amount`.
6. El dinero va a la cuenta del vendedor.
7. Webhook de Stripe actualiza el estado del pedido.

### Webhooks importantes

- `payment_intent.succeeded`
- `charge.refunded`
- `charge.dispute.created`
- `payout.paid`
- `payout.failed`
- `account.updated`

Importante:

- validar firma de Stripe,
- hacer webhooks idempotentes,
- no actualizar estado solo por UI,
- tener un log de eventos.

### Costo de Stripe

Stripe no tiene costo mensual de infra.

Tiene comisiones por transacción, por ejemplo:

- ~2.9% + 30¢ por pago con tarjeta en muchos casos,
- más fees de Connect si aplica.

Eso no debería salir de tu presupuesto de infra, sino de la operación o del GMV.

---

## 4.6 Admin panel

Para no quemar tiempo, usa dos capas:

### 1. Supabase Studio

Te deja ver:

- usuarios,
- tablas,
- logs,
- storage,
- realtime,
- edge functions,
- backups.

Útil para soporte y debugging.

### 2. Panel admin interno

Un `/admin` en Next.js con acceso solo para role `admin`.

Puede ser simple con:

- React Admin,
- Refine,
- o incluso tablas manuales con TanStack Table.

Funciones mínimas:

- ver usuarios,
- ver servicios,
- deshabilitar usuarios,
- deshabilitar servicios,
- ver pedidos,
- ver mensajes,
- marcar pedido como completado,
- ver estado de pagos en Stripe,
- revisar disputes básicos.

No hagas un admin enterprise al principio.

---

# 5. Arquitectura recomendada

```text
┌────────────────────────────┐
│        Next.js UI          │
│  Vercel                    │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│        Supabase            │
│  - PostgreSQL              │
│  - Auth                    │
│  - Storage                 │
│  - Realtime                │
│  - Row Level Security      │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│   Stripe Connect           │
│   - Checkout / Payment     │
│   - Webhooks               │
│   - Payouts                │
└────────────────────────────┘
```

Flujo general:

1. Usuario se registra con Supabase Auth.
2. Se crea un profile.
3. Vendedor crea servicios.
4. Comprador busca servicios.
5. Comprador hace pedido.
6. Se redirige a Stripe.
7. Stripe envía webhook.
8. Pedido pasa a `paid`.
9. Se abre chat por order_id.
10. Vendedor y comprador chatean.
11. Pedido se marca completado.
12. Opcional: review.

---

# 6. Modelo de datos mínimo

No lo sobrecomplicarías.

Tablas principales:

## users

Viene de Supabase Auth, pero tú puedes tener una tabla `profiles`:

```text
profiles
- id
- user_id
- full_name
- role: buyer | seller | admin
- avatar_url
- bio
- stripe_account_id
- is_active
- created_at
```

## services

```text
services
- id
- seller_id
- title
- slug
- description
- price_usd
- category_id
- status: draft | active | disabled
- search_vector
- created_at
```

## categories

```text
categories
- id
- name
- slug
```

## orders

```text
orders
- id
- buyer_id
- seller_id
- service_id
- status: pending_payment | paid | in_progress | completed | cancelled | refunded
- amount_usd
- stripe_payment_intent_id
- stripe_order_id
- created_at
- completed_at
```

## messages

```text
messages
- id
- order_id
- sender_id
- content
- created_at
```

## reviews opcional

```text
reviews
- id
- order_id
- reviewer_id
- reviewee_id
- rating
- comment
- created_at
```

## admin_actions opcional

```text
admin_actions
- id
- admin_id
- action
- target_table
- target_id
- metadata
- created_at
```

---

# 7. Presupuesto detallado recomendado

## Costos mensuales aproximados

| Herramienta / Infra | Para qué | Costo mensual estimado |
|---|---|---:|
| Vercel Hobby / Pro | Frontend + API routes | $0 - $20 |
| Supabase Free / Pro | DB, auth, storage, realtime | $0 - $50 |
| Resend / Postmark / SendGrid | Emails transaccionales | $0 - $20 |
| Dominio | Producción | ~$1 |
| Sentry | Errores | $0 |
| PostHog / Plausible | Analytics opcional | $0 - $20 |
| Meilisearch / Typesense | Solo si Postgres FTS no alcanza | $0 - $20 |
| Buffer por crecimiento / incidentes | Almacenamiento, logs, imprevistos | $20 - $100 |
| **Total estimado** |  | **$21 - $231** |

En la práctica:

| Escenario | Costo mensual |
|---|---:|
| Lanzamiento, 500 usuarios | **$50 - $120** |
| 5,000 usuarios, crecimiento | **$100 - $200** |

## 6 meses

| Escenario | Costo 6 meses |
|---|---:|
| Bajo / free tiers + buffer mínimo | **$300 - $600** |
| Producción estable con Pro | **$600 - $1,000** |
| Con crecimiento, extras y buffer | **$1,000 - $1,500** |

Con tus **$5,000**, tendrías amplio margen.

### Ejemplo de presupuesto a 6 meses

| Concepto | Costo |
|---|---:|
| Vercel Pro, 6 meses | $120 |
| Supabase Pro, 6 meses | $150 |
| Email, 6 meses | $0 - $120 |
| Dominio, 6 meses | ~$6 |
| Analytics opcional | $0 - $120 |
| Búsqueda avanzada opcional | $0 - $120 |
| Buffer técnico | $200 - $500 |
| **Total** | **$496 - $1,136** |

Aun si todo sale mal y duplicas el costo, estarías cerca de **$2,000 - $3,000**, todavía dentro de presupuesto.

---

# 8. Plan sugerido de 6 semanas

## Semana 1: Fundaciones

- Setup de repo.
- Next.js.
- Supabase project.
- Autenticación.
- Tabla de profiles.
- Roles: buyer, seller, admin.
- RLS básico.
- Deploy staging en Vercel.
- Sentry.
- Variables de entorno.

Objetivo:

> Usuario puede registrarse, logearse y ver su perfil.

---

## Semana 2: Servicios y búsqueda

- CRUD de servicios.
- Categorías.
- Imágenes con Supabase Storage.
- Listado público de servicios.
- Filtros básicos:
  - categoría,
  - precio,
  - texto.
- Postgres full-text search.
- SEO básico:
  - metadata,
  - slugs,
  - sitemap,
  - Open Graph.

Objetivo:

> Un comprador puede buscar y ver servicios.

---

## Semana 3: Pedidos y Stripe

- Modelo de orders.
- Checkout con Stripe.
- Stripe Connect onboarding para vendedores.
- Webhooks de Stripe.
- Estados de pedido.
- Comisión de plataforma.
- Panel básico para ver pedidos.
- Emails:
  - pedido creado,
  - pago exitoso,
  - nuevo mensaje.

Objetivo:

> Un comprador puede pagar un servicio y el pedido queda registrado.

Esta es la semana más crítica.

---

## Semana 4: Chat en tiempo real

- Tabla messages.
- RLS: solo participantes del pedido.
- Supabase Realtime por order_id.
- UI de chat.
- Persistencia de mensajes.
- Rate limit simple.
- Notificaciones básicas.

Objetivo:

> Comprador y vendedor pueden chatear solo si hay un pedido.

No añadas:

- video calls,
- llamadas,
- compartir archivos pesados,
- stickers,
- emojis avanzados,
- grupos,
- canales.

Solo texto por pedido.

---

## Semana 5: Admin y flujos de operación

- Panel admin.
- Ver usuarios.
- Ver servicios.
- Deshabilitar usuario.
- Deshabilitar servicio.
- Ver pedidos.
- Ver mensajes.
- Marcar pedido completado.
- Ver estado de Stripe.
- Logs básicos de administración.
- Emails de soporte básico.

Objetivo:

> Tú puedes operar manualmente el marketplace.

---

## Semana 6: QA, seguridad, performance y lanzamiento

- Tests manuales de flujos críticos.
- Validación de RLS.
- Webhooks idempotentes.
- Manejo de errores.
- Rate limiting.
- Imágenes optimizadas.
- SEO.
- Analytics.
- Uptime monitoring.
- Backups.
- Documentación interna mínima.
- Deploy a producción.

Objetivo:

> Lanzar con estabilidad aceptable.

---

# 9. Scope recomendado para no explotar en 6 semanas

## Incluye

- auth,
- perfiles,
- servicios,
- búsqueda simple,
- filtros básicos,
- checkout,
- pedidos,
- chat por pedido,
- admin mínimo,
- emails transaccionales.

## No incluir al inicio

- app móvil,
- video calls,
- llamadas,
- compartir archivos grandes,
- recomendaciones IA,
- matching avanzado,
- multi-idioma,
- multi-moneda,
- taxes complejos,
- disputes complejos,
- reviews con media,
- chat en grupo,
- notificaciones push móviles.

Para disputes, al inicio puedes hacerlo manualmente:

- estado `disputed`,
- email,
- resolución manual por ti,
- refund desde Stripe si aplica.

---

# 10. Riesgos principales y cómo evitarlos

## Riesgo 1: Stripe Connect se vuelve un pantano

Es el mayor riesgo técnico y de tiempo.

### Mitigación

- Usa **Standard o Express**, no Custom para MVP.
- Prueba todo en test mode desde la semana 3.
- Limita el flujo:
  - 1 tipo de pago,
  - 1 moneda,
  - 1 comisión,
  - 1 flujo de checkout.
- Ten un proceso manual de fallback.

Si Stripe Connect se complica, para las primeras ventas puedes hacer:

- Stripe Checkout simple,
- pago manual al vendedor,
- registro manual en base de datos.

Pero eso no es sostenible, así que no lo extiendas demasiado.

---

## Riesgo 2: Row Level Security mal diseñada

Puede hacer que:

- un usuario vea datos de otro,
- un vendedor edite servicio ajeno,
- un comprador inserte mensajes de otro pedido.

### Mitigación

- Diseña RLS desde la semana 1.
- Usa helpers:

```sql
create function is_admin()
returns boolean
language sql
stable
security definer
as $$
  select exists (
    select 1
    from profiles
    where id = auth.uid()
      and role = 'admin'
  );
$$;
```

- No expongas `service_role` en el frontend.
- Usa `service_role` solo en server-side.

---

## Riesgo 3: Chat se convierte en proyecto enorme

### Mitigación

Solo texto.
Solo por pedido.
Solo 2 participantes.
Sin archivos.
Sin presencia compleja.
Sin typing indicator si no es rápido.

---

## Riesgo 4: Búsqueda avanzada te consume tiempo

### Mitigación

Postgres FTS primero.

Si en 2-4 semanas no está bien, agrega Typesense o Meilisearch.

No empieces con Elasticsearch.

---

## Riesgo 5: Costo de Stripe no entra en infra, pero sí en el negocio

### Mitigación

Define desde el inicio:

- ¿quién paga la comisión de tarjeta?
- ¿la plataforma cobra 10%?
- ¿el vendedor absorbe las fees?
- ¿la comisión se aplica solo al GMV?

Ejemplo simple:

- Servicio: $100
- Comisión plataforma: $10
- Comisión Stripe: ~$3
- Vendedor recibe: ~$87

O si la plataforma se queda con la comisión de Stripe:

- Vendedor recibe: ~$87
- Plataforma recibe: $10

Depende de tu modelo.

---

# 11. Cuándo elegiría otra opción

## Elige Django si:

- prefieres Python,
- puedes extenderte a 8-10 semanas,
- el marketplace tendrá lógica compleja,
- necesitas reports,
- necesitas workers/Celery,
- quieres Django Admin.

Ejemplo:

```text
React + Django + DRF + Channels + PostgreSQL + Redis + Stripe
```

Pero no la elegiría para 6 semanas si tienes 1 persona.

---

## Elige Go si:

- tienes más tiempo,
- quieres aprender Go en producción,
- necesitas performance extrema,
- quieres infraestructura muy barata,
- aceptas mayor riesgo de delay.

Para tu MVP, no.

---

## Elige Firebase si:

- quieres máxima velocidad en auth y realtime,
- aceptas NoSQL,
- aceptas que búsqueda y reports serán más complicados,
- aceptas costo por uso menos predecible.

Para un marketplace relacional, Supabase + PostgreSQL suele ser mejor que Firebase + Firestore.

---

# 12. Recomendación final

## Stack final recomendado

| Capa | Tecnología |
|---|---|
| Frontend | Next.js / React |
| Deploy frontend | Vercel |
| Backend gestionado | Supabase |
| Base de datos | PostgreSQL |
| Auth | Supabase Auth |
| Storage | Supabase Storage |
| Chat | Supabase Realtime |
| Búsqueda | PostgreSQL full-text search |
| Pagos | Stripe Connect |
| Email | Resend o similar |
| Admin | Supabase Studio + panel interno |
| Monitoring | Sentry |
| Analytics opcional | PostHog / Plausible |

## Razón principal

Tu limitación más dura no es el presupuesto, es el **timeline de 6 semanas** y que **una sola persona tenga que mantenerlo**.

La opción ganadora no es la más “elegante” técnicamente, sino la que minimiza:

- servidores,
- websockets propios,
- workers,
- Redis,
- auth custom,
- storage custom,
- admin panel from scratch,
- infraestructura compleja.

Por eso:

> **Next.js + Supabase + Stripe Connect + Vercel** es la mejor elección para tu MVP.

Con esa combinación puedes lanzar un marketplace funcional, con pagos, chat, búsqueda y admin, manteniendo la infra mensual entre **$50 y $200**, y dejando margen suficiente dentro de tus **$5,000**.