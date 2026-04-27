# MiMo V2.5-Pro (Xiaomi) — reasoning/multi_constraint_decision

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.58 | quality: 8.52
- latency_total: 34.176s | tokens_per_second: 59.9
- input_tokens: 433 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# Stack Tecnológico para MVP de Marketplace Freelance

## Contexto y Análisis Inicial

Antes de comparar, voy a mapear lo que realmente necesitas construir vs. lo que puedes usar pre-hecho:

```
┌─────────────────────────────────────────────────────┐
│              FUNCIONALIDADES DEL MVP                 │
├──────────────────┬──────────────────────────────────┤
│ Auth             │ Registro, login, roles (buyer/    │
│                  │ seller), perfiles                  │
├──────────────────┼──────────────────────────────────┤
│ Pagos            │ Stripe Connect (marketplace),     │
│                  │ escrow, payouts a sellers          │
├──────────────────┼──────────────────────────────────┤
│ Chat realtime    │ Mensajería 1:1 entre buyer/seller │
├──────────────────┼──────────────────────────────────┤
│ Búsqueda         │ Filtros por categoría, precio,   │
│                  │ rating, texto libre                │
├──────────────────┼──────────────────────────────────┤
│ Admin Panel      │ Gestionar usuarios, disputas,     │
│                  │ categorías, métricas básicas       │
├──────────────────┼──────────────────────────────────┤
│ Core Marketplace │ Listings, orders, reviews,        │
│                  │ dashboard de seller                │
└──────────────────┴──────────────────────────────────┘
```

**Dato clave:** Con 6 semanas y 1 dev, cada día cuenta. El 60-70% del tiempo irá a funcionalidades que NO son tu diferenciador (auth, chat, infra). El stack ideal **minimiza trabajo repetitivo**.

---

## Las 3 Opciones

---

### OPCIÓN A: Next.js + Supabase + Vercel

```
┌─────────────────────────────────────────────────────┐
│                   ARQUITECTURA                       │
│                                                     │
│  ┌──────────┐    ┌──────────────────────────────┐   │
│  │  Vercel   │    │        Supabase              │   │
│  │          │    │  ┌─────────┐  ┌───────────┐  │   │
│  │ Next.js  │◄──►│  │PostgreSQL│  │   Auth     │  │   │
│  │ (SSR/SSG)│    │  │  + FTS   │  │ (GoTrue)  │  │   │
│  │          │    │  └─────────┘  └───────────┘  │   │
│  │ React    │    │  ┌─────────┐  ┌───────────┐  │   │
│  │ API Rts  │    │  │Realtime  │  │  Storage   │  │   │
│  │          │    │  │(WebSocks)│  │ (imágenes) │  │   │
│  └──────────┘    │  └─────────┘  └───────────┘  │   │
│                  │  ┌─────────────────────────┐  │   │
│  ┌──────────┐    │  │  Row Level Security     │  │   │
│  │  Stripe   │    │  │  (autorización a nivel  │  │   │
│  │ Connect   │    │  │   de fila)              │  │   │
│  └──────────┘    │  └─────────────────────────┘  │   │
│                  └──────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

**Lo que obtienes gratis/pre-hecho:**
- ✅ Auth completo (email, OAuth, JWT, roles)
- ✅ Base de datos PostgreSQL managed
- ✅ Realtime subscriptions (para el chat)
- ✅ Storage para imágenes de listings
- ✅ Auto-generación de APIs REST desde el schema
- ✅ Row Level Security para autorización
- ✅ Full-text search nativo de PostgreSQL
- ✅ Dashboard de Supabase como admin básico

**Lo que construyes:**
- 🔨 UI del marketplace (React/Next.js)
- 🔨 Lógica de negocio (orders, reviews, escrow)
- 🔨 Integración Stripe Connect
- 🔨 Chat UI (con Supabase Realtime como backend)
- 🔨 Admin panel custom o con herramienta low-code

**Costos estimados mensuales:**

```
┌────────────────────┬──────────┬───────────┐
│ Servicio           │ 0-500usr │ 0-5000usr │
├────────────────────┼──────────┼───────────┤
│ Supabase           │ $0 free  │ $25 pro   │
│ Vercel             │ $0 hobby │