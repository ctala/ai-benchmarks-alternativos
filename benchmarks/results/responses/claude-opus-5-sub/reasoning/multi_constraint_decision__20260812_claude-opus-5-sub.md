# Claude Opus 5 (suscripción) — reasoning/multi_constraint_decision

- model_id: `claude-opus-5`
- success: True  | final: 7.45 | quality: 9.52
- latency_total: 173.202s | tokens_per_second: 60.7
- input_tokens: 2 | output_tokens: 10517
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

# Stack para marketplace de servicios — análisis y recomendación

## Primero: dónde está el cuello real

Antes del stack, tres cosas que cambian la decisión:

**1. Tu restricción no es infra, son horas.** 6 semanas × 1 dev ≈ 200-240 horas productivas. A 5.000 usuarios, cualquiera de estos stacks corre en $60/mes. La pregunta correcta no es "¿qué escala mejor?" sino **"¿qué código NO tengo que escribir?"**.

**2. El ítem que se come el timeline es pagos, no el chat.** Un marketplace no cobra: intermedia. Necesitas onboarding con KYC de vendedores, retención de fondos hasta la entrega, split de comisión, payouts, reembolsos y contracargos. Eso son 1,5-2 semanas de las 6, y es idéntico en los tres stacks. La respuesta es **Stripe Connect (Express)** y no discutirlo.

> Advertencia importante: **no construyas un "wallet" con saldos en tu propia base de datos** y payouts manuales. Eso te convierte en transmisor de dinero y es un problema regulatorio serio. Usa `separate charges and transfers` de Connect con transferencia diferida: Stripe retiene, tú instruyes.

**3. Si estás en LATAM, verifica esto antes de escribir una línea.** Stripe Connect no tiene la misma cobertura en todos los países, y lo que importa es **el país de payout de tus vendedores**, no el tuyo. Si tus freelancers están en Chile, Argentina, Perú o Colombia, revisa Mercado Pago Marketplace (split payments), dLocal o Kushki. Esta verificación es de 2 horas y puede invalidar semanas de trabajo.

---

## Las tres opciones

### Opción A — Next.js + Supabase + Stripe Connect

TypeScript de punta a punta. Supabase aporta Postgres, Auth, Realtime y Storage con Row Level Security. Búsqueda con Postgres full-text (config `spanish` + `pg_trgm` para tolerancia a errores). Admin con shadcn/ui o Refine sobre rutas protegidas. Deploy en Vercel.

**A favor**
- Un solo lenguaje, un solo repo, un solo deploy. Para un mantenedor solo, esto vale más de lo que parece.
- **El chat en tiempo real es prácticamente gratis**: Supabase Realtime + RLS y te ahorras Redis, ASGI, workers y WebSockets propios. Es una semana que te devuelven.
- Auth resuelto de fábrica (social login, magic links, MFA).
- La escotilla de salida existe: es Postgres. Puedes migrar los datos aunque quede acoplado el Auth/Realtime.

**En contra**
- **RLS es el footgun principal.** Un marketplace maneja PII, mensajes privados y datos de payout. Una política mal escrita es una filtración. Con 1 dev sin revisor, es riesgo real.
- No hay panel de administración regalado. Son ~1 semana de trabajo (Supabase Studio es acceso a tablas crudas: no se lo das a nadie de operaciones).
- Asume soltura en TypeScript del lado servidor, no solo React.

### Opción B — Django + HTMX (o React puntual) + Stripe Connect

Monolito Python. Django admin, `django-allauth`, ORM, migraciones. Búsqueda con `django.contrib.postgres.search`. Realtime vía Django Channels + Redis, o comprándolo (Ably/Pusher). Deploy en Render o Fly.io.

**A favor**
- **Juega a la fortaleza del dev** (Python es su lenguaje fuerte; el Go básico no sirve para esto).
- **Django admin elimina un requisito completo.** CRUD, permisos, filtros y acciones masivas para moderar, reembolsar y verificar vendedores, con cero código. Esta es la ventaja más grande de las que hay en la mesa.
- Aburrido en el buen sentido. A 12 meses, un monolito Django lo mantiene una persona sin drama.

**En contra**
- **El realtime es el punto débil.** Channels significa ASGI + Redis + un proceso más que operar y pagar. Comprarlo (Ably) resuelve, pero suma un vendor y ~$30/mes al crecer.
- Decisión de frontend obligada: HTMX cubre el 90% del marketplace (browse, ficha, checkout, dashboard), pero el chat pide un componente JS igual.
- Si vas Django + React SPA, terminas con dos lenguajes y dos deploys para una persona.

### Opción C — Go + React + Postgres, todo propio

**A favor**
- Infra más barata (~$30/mes), binario único, concurrencia excelente para WebSockets.

**En contra, y es decisivo**
- El dev tiene "básico de Go". Aprender el lenguaje mientras escribes auth, sesiones, RBAC, migraciones, panel de admin y la integración de pagos, en 6 semanas, no cabe. Faltan 3-4 semanas como mínimo.
- La ventaja real de Go (concurrencia masiva) es irrelevante a 5.000 usuarios. Estás pagando complejidad por un problema que no tienes.
- Ahorras ~$40/mes de infra. Sobre 6 meses son $240: menos que un día de tu tiempo.

**Descartada.** No por mala, sino por mal calzada al contexto.

### Anti-opciones que quizás te tienten

| Opción | Por qué no |
|---|---|
| Firebase/Firestore | Auth y realtime excelentes, pero un marketplace es relacional (órdenes, disputas, payouts, comisiones). Modelar eso en Firestore duele, y la búsqueda te obliga a Algolia aparte. |
| MongoDB | Mismo problema: transacciones de dinero quieren integridad relacional. |
| Microservicios | A 5.000 usuarios y 1 dev, es autolesión. |
| Phoenix LiveView | Sería técnicamente ideal para esto. No sabes Elixir. Siguiente vida. |

---

## Costos de infraestructura estimados

Precios de referencia, **verifícalos**: cambian seguido.

| Servicio | Opción A | Opción B | Opción C |
|---|---|---|---|
| Hosting app | Vercel Pro ~$20 | Render Starter ~$25 | Fly.io ~$10 |
| Base de datos | incluido en Supabase | Postgres gestionado ~$20 | Neon ~$19 |
| Auth | incluido | incluido (allauth) | propio ($0, +tiempo) |
| Realtime | incluido | Redis ~$10 o Ably $0-29 | propio ($0, +tiempo) |
| Backend/BaaS | Supabase Pro ~$25 | — | — |
| Búsqueda | Postgres FTS $0 | Postgres FTS $0 | Postgres FTS $0 |
| Email transaccional | Resend ~$0-20 | igual | igual |
| Errores + analytics | Sentry/PostHog free | igual | igual |
| **Mes 1 (500 usuarios)** | **~$45-65** | **~$55-75** | **~$30-40** |
| **Mes 6 (5.000 usuarios)** | **~$70-110** | **~$85-130** | **~$45-70** |

Sobre Stripe: no es costo fijo, es porcentaje del GMV (~2,9% + fijo, más ~0,25% + $2 por payout en Connect). Sale del margen, no del presupuesto de infra. Reserva ~$300 para contracargos ($15 cada uno).

**Total infra a 6 meses: $400-700.** Es el 8-14% de tus $5.000.

---

## Recomendación: Opción A (Next.js + Supabase + Stripe Connect)

**Por qué gana**, en orden de peso:

1. **Te devuelve la semana del chat.** Realtime con RLS sin operar Redis ni un proceso ASGI. En un plan de 6 semanas sin holgura, una semana es el 17% del proyecto.
2. **Un lenguaje, un deploy, un mental model.** El criterio de "fácil de mantener por 1 persona" se cumple mejor reduciendo superficie operativa que eligiendo el lenguaje más cómodo.
3. **Auth de fábrica**, incluyendo los casos molestos: verificación de email, recuperación, OAuth.
4. Escala de sobra: 5.000 usuarios en Supabase Pro no despeina a nadie.

**El costo que aceptas:** ~1 semana construyendo el admin, y disciplina con RLS.

**Regla de cambio, sin ambigüedad — vete a Django (Opción B) si se cumple alguna:**
- El dev es fuerte en Python pero flojo en TypeScript del lado servidor. En ese caso B gana claro: pelear con el lenguaje cuesta más que el chat.
- Tu operación es intensiva en back-office desde el día 1 (verificación manual de vendedores, moderación pesada, gestión de disputas). Django admin te regala eso y da vuelta la ecuación.

Las dos son defendibles. **Lo que no es defendible es Go**: pierdes 3-4 semanas para ahorrar $240 en seis meses.

### Mitigaciones obligatorias si tomas A

- `service_role` **nunca** llega al cliente. Solo en server actions y route handlers.
- Todas las tablas con RLS activo y **deny por defecto**. Habilitas acceso explícito, no al revés.
- Tests de políticas para las 4-5 tablas sensibles (mensajes, órdenes, payout_accounts, perfiles). Un archivo SQL con "el usuario X no debe ver la fila Y" te evita el incidente.
- La lógica de dinero vive en el servidor y valida montos contra la base. Nunca confíes en un precio que viene del cliente.

---

## Que quepa en 6 semanas

| Semana | Foco |
|---|---|
| 1 | Modelo de datos, auth, perfiles comprador/vendedor, deploy y CI desde el día 2 |
| 2 | Publicaciones (CRUD), navegación, búsqueda, imágenes |
| 3-4 | **Stripe Connect**: onboarding KYC, checkout, retención, transferencia con comisión, reembolsos. Máquina de estados de la orden |
| 5 | Chat, notificaciones, emails transaccionales |
| 6 | Admin, moderación, términos legales, QA, lanzamiento |

Cero holgura. Para que entre, **recorta ahora**:

- Sin app móvil. Web responsive.
- Sin sistema de disputas en producto: a 500 usuarios se resuelven por email, tú mismo.
- Sin dashboard de analítica para vendedores.
- Sin multi-moneda ni multi-idioma.
- Sin facetas avanzadas de búsqueda: categoría + texto + orden por precio alcanza.
- Reseñas sí van. Un marketplace sin señal de confianza no convierte.

A 500 usuarios puedes hacer manualmente casi todo lo que a 50.000 sería imposible. Aprovéchalo: es la única razón por la que 6 semanas es un plazo realista.

---

## Dónde va realmente el presupuesto

| Ítem | Estimado |
|---|---|
| Infra 7 meses | $500-700 |
| Herramientas (Sentry, PostHog, Resend) | $0-150 |
| Dominio + correo corporativo | $120 |
| UI kit | $0 con shadcn/ui |
| **Términos de marketplace + privacidad** | $200-1.500 |
| Reserva contracargos | $300 |
| **Subtotal** | **$1.100-2.800** |

Te sobran entre $2.200 y $3.900. **No los gastes en infra.** Los marketplaces no mueren por servidores: mueren por falta de liquidez. Ese dinero va a sembrar el lado de la oferta —pagar a los primeros 20-30 vendedores buenos para que estén ahí el día del lanzamiento— porque un marketplace vacío no convierte a ningún comprador, corra sobre Supabase, Django o Go.