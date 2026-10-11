# Bonsai 2 27B — business_strategy/plan_monetizar_medio_con_restricciones

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 6.86 | quality: 8.0
- latency_total: 556.442s | tokens_per_second: 37.8
- input_tokens: 407 | output_tokens: 21026

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



Te doy el plan con tus reglas intactas:

- **No AdSense.**
- **No display.**
- **No programática.**
- **No publicidad pagada.**
- **No contratar a nadie en 90 días.**
- **Solo tú, ~4 horas/día.**
- **Objetivo: $5,000 USD/mes a día 90.**

La forma de llegar no es “vender más anuncios”. Es **convertir tu tráfico orgánico en una lista de email** y monetizar por:

1. **Afiliados en sitio.**
2. **Afiliados por email.**
3. **Patrocinios directos por artículo/newsletter.**
4. **Newsletter/paid tier.**

Si por “no display” también descargas cualquier patrocinio directo o native, entonces **no llega** con tus restricciones. Pero si aceptas patrocinios directos por texto/email y afiliados, sí hay plan.

---

# 1. El modelo de ingresos

## A. Afiliados en sitio

No dependes de display. Usas enlaces de afiliado dentro del contenido: hosting, cloud, SaaS, IA, cursos, herramientas, fintech, e-commerce, etc.

**Supuesto conservador:**

- 300,000 visitas/mes.
- 1.0% de visitas hacen clic en un CTA de afiliado.
- EPC: $0.50 por click.

Aritmética:

```text
300,000 visitas × 1.0% = 3,000 clicks
3,000 clicks × $0.50 = $1,500/mes
```

EPC de $0.50 es conservador para tecnología B2B/SaaS. No es magia: significa que de cada click te queda $0.50 en promedio.

---

## B. Afiliados por email

Aquí está la diferencia: hoy no tienes lista, pero con 300,000 visitas/mes puedes construir una lista real en 90 días.

**Supuesto:**

- Captura de email: 2.0% de visitas.
- 300,000 × 2.0% = 6,000 nuevos suscriptores/mes.
- A día 90: 18,000 suscriptores aproximados.
- Envías 3 newsletters/mes.
- Open rate: 30%.
- CTR: 3.0%.
- Conversión a afiliado: 8%.
- Ticket promedio: $20.

Aritmética:

```text
18,000 suscriptores × 3 envíos = 54,000 envíos
54,000 × 30% open = 16,200 aperturas
16,200 × 3.0% CTR = 486 clicks
486 × 8% conversión = 38.88 ventas
38.88 × $20 = $778/mes
```

Rondeado:

```text
Email affiliate ≈ $780/mes
```

---

## C. Patrocinios directos

No display. No programática. No AdSense.

Vendes **patrocinios directos**:

- Artículo patrocinado por texto.
- Newsletter patrocinada.
- Briefing mensual patrocinado.
- Mención editorial con enlaces.
- Bloque de texto en email.

**Paquete de precio:**

| Producto | Precio |
|---|---:|
| Artículo patrocinado | $250 |
| Newsletter patrocinada | $200 |
| Briefing mensual patrocinado | $800 |

Para la aritmética uso un promedio simple:

```text
10 patrocinios/mes × $300 = $3,000/mes
```

¿Es realista?

Con 300,000 visitas/mes, nicho tech, audiencia LATAM y sin display, $300 por patrocinio directo es conservador.

Necesitas:

```text
10 patrocinios/mes = 2.5 por semana
```

Con 1 hora/día de outreach, es viable.

Aritmética de outreach:

```text
30 correos/día × 90 días = 2,700 correos
2,700 × 1% de cierre = 27 patrocinios en 90 días
```

Eso te permite tener:

```text
Mes 1: 3 patrocinios
Mes 2: 6 patrocinios
Mes 3: 10 patrocinios
Total: 19 patrocinios
```

Con 1% de cierre de outreach, es conservador.

---

## D. Paid newsletter / membership ligera

Como ya tienes contenido generado, puedes vender una versión premium de tu briefing.

**Producto:**

```text
Briefing Tech LATAM Pro
$9/mes
```

Contenido:

- Resumen extendido.
- Herramientas seleccionadas.
- Oportunidades laborales/funding.
- Análisis corto.
- Recursos descargables.
- Ofertas exclusivas.

**Supuesto:**

- 18,000 suscriptores.
- 0.6% pasan a pago.
- Precio: $9/mes.

Aritmética:

```text
18,000 × 0.6% = 108 suscriptores de pago
108 × $9 = $972/mes
```

Rondeado:

```text
Paid tier ≈ $970/mes
```

---

# 2. Run-rate a día 90

Con los números propuestos:

| Fuente | Cálculo | Ingreso/mes |
|---|---:|---:|
| Afiliados en sitio | 3,000 clicks × $0.50 | $1,500 |
| Afiliados por email | 38.88 ventas × $20 | $778 |
| Patrocinios directos | 10 × $300 | $3,000 |
| Paid newsletter | 108 × $9 | $972 |
| **Total** |  | **$6,250** |

```text
$1,500 + $778 + $3,000 + $972 = $6,250/mes
```

**Llega a $5,000/mes con $1,250 de margen.**

---

# 3. Rampa de 90 días

No esperes que el mes 3 sea igual al mes 1. La rampa sería:

| Mes | Suscriptores acumulados | Patrocinios/mes | Ingreso estimado |
|---|---:|---:|---:|
| Mes 1 | 6,000 | 3 | $1,500 |
| Mes 2 | 12,000 | 6 | $3,000 |
| Mes 3 | 18,000 | 10 | $6,250 |

Total aproximado en 90 días:

```text
$1,500 + $3,000 + $6,250 = $10,750
```

El objetivo no es total, es run-rate:

```text
A día 90: $6,250/mes
```

---

# 4. Plan operativo de 90 días

## Semana 1: Infraestructura

Objetivo: dejar listo todo para monetizar tráfico.

### Email

- Elegir proveedor de email.
- Crear lead magnet.
- Crear secuencia de bienvenida.
- Añadir CTA de captura en los artículos principales.
- Configurar double opt-in.

Lead magnet recomendado:

```text
Briefing Tech LATAM
```

Contenido:

- 5 noticias tech relevantes.
- 1 herramienta nueva.
- 1 oportunidad laboral/funding.
- 1 recurso práctico.
- 1 recomendación rápida.

CTA:

```text
Recibe el briefing semanal sin spam.
```

No necesitas pop-up agresivo. Usa:

- CTA inline al final del artículo.
- CTA en la parte superior de artículos clave.
- CTA sticky discreto.
- CTA al hacer clic en enlaces de valor.

### Afiliados

Crear cuentas en programas relevantes:

- Hosting/cloud.
- SaaS.
- IA.
- Productividad.
- Cursos.
- Fintech.
- E-commerce.
- Herramientas B2B.

Añadir disclosure:

```text
Algunos enlaces son de afiliado.
```

### Media kit

Crear un media kit simple:

- 300,000 visitas/mes.
- Nicho: tecnología.
- Audiencia: profesionales y curiosos.
- Mercado: LATAM.
- Sin display/programática.
- Editorial tech.
- Top páginas.
- Crecimiento orgánico.
- Lista de email en crecimiento.
- Oportunidades de patrocinio directo.

---

## Semana 2: Primer outreach

Objetivo: iniciar pipeline de patrocinios.

### Outreach

Meta:

```text
30 correos/día
```

A quién contactar:

- Vendors de hosting/cloud.
- SaaS con producto en LATAM.
- Plataformas de IA.
- Cursos online.
- Herramientas de productividad.
- Fintech.
- Job boards tech.
- Empresas de e-commerce tech.
- Proveedores de infraestructura.
- Startups que venden a LATAM.

Mensaje base:

```text
Hola [nombre],

Tengo un medio de tecnología con 300,000 visitas orgánicas mensuales, audiencia de profesionales y curiosos de tech, mayormente LATAM.

No usamos display ni programática. Monetizamos con patrocinios directos y email.

¿Le interesa un patrocinio directo para su producto en un artículo o en nuestra newsletter?

Les envío media kit y opciones.

Saludos,
[Tu nombre]
```

### KPI semana 2

```text
100 prospectos listados
50 correos enviados
Media kit listo
CTA de email activo
```

---

## Semana 3: Primeros patrocinios y email

Objetivo: cerrar primeros patrocinios.

### Acciones

- Enviar 30 correos/día.
- Hacer follow-up a los que respondieron.
- Preparar 2-3 paquetes de patrocinio.
- Enviar primera newsletter semanal.
- Añadir afiliados a top 50 artículos.

### Paquetes de patrocinio

| Opción | Precio | Qué incluye |
|---|---:|---|
| Artículo patrocinado | $250 | Texto nativo, 2-3 enlaces, sin banner |
| Newsletter patrocinada | $200 | Bloque de texto en email, CTA |
| Briefing mensual | $800 | 4 newsletters + 1 artículo patrocinado |

---

## Semana 4: Revisión y ajuste

Objetivo: validar si el plan sigue vivo.

### KPIs mínimos

| KPI | Mínimo viable |
|---|---:|
| Suscriptores a día 30 | 6,000 |
| Captura | 2.0% |
| Patrocinios cerrados | 2-3 |
| Pipeline en negociación | 5+ |
| CTR de email | 2.5%+ |
| EPC afiliados en sitio | $0.35+ |

Si a día 30:

- Tienes menos de 4,500 suscriptores.
- No tienes pipeline real de patrocinios.
- Tu EPC es menor a $0.35.

Entonces **el plan no llega a $5,000/mes con estas restricciones**. No lo maquillo.

---

# 5. Cómo se usan tus 4 horas diarias

Asumo 4 horas/día, 90 días:

```text
4 horas × 90 días = 360 horas
```

Distribución:

| Bloque | Tiempo/día | Acción |
|---|---:|---|
| Outreach patrocinios | 1h | 30 correos, follow-up, negociación |
| Email/producto | 1h | Captura, newsletter, paid tier |
| Afiliados | 1h | Enlaces, CTA, optimización |
| Analytics/experimentos | 1h | KPIs, A/B, ajuste |

Total:

```text
4 horas/día
```

---

# 6. Aritmética de captación de email

Tu ventaja principal:

```text
300,000 visitas/mes
```

Si logras 2.0% de captura:

```text
300,000 × 2.0% = 6,000 nuevos suscriptores/mes
```

Acumulados:

| Mes | Nuevos | Acumulados |
|---|---:|---:|
| 1 | 6,000 | 6,000 |
| 2 | 6,000 | 12,000 |
| 3 | 6,000 | 18,000 |

Con 18,000 suscriptores, ya tienes una audiencia que no depende del SEO de cada día.

Eso cambia la monetización.

---

# 7. Aritmética de patrocinios

Necesitas 10 patrocinios/mes a día 90.

Equivale a:

```text
10 patrocinios/mes × 30 días = 0.33 patrocinios/día
```

O:

```text
2.5 patrocinios/semana
```

Con 30 correos/día de outreach:

```text
30 × 90 = 2,700 correos
```

Si cierras 1%:

```text
2,700 × 1% = 27 patrocinios en 90 días
```

Distribución:

| Mes | Patrocinios |
|---|---:|
| 1 | 3 |
| 2 | 6 |
| 3 | 10 |
| Total | 19 |

Quedan 8 patrocinios de margen en la proyección.

---

# 8. Escenarios de sensibilidad

## Escenario base

| Variable | Valor |
|---|---:|
| Captura email | 2.0% |
| Suscriptores a día 90 | 18,000 |
| Patrocinios/mes | 10 |
| EPC afiliados | $0.50 |
| Ingresos | $6,250 |

---

## Escenario mínimo viable

| Variable | Valor |
|---|---:|
| Captura email | 1.5% |
| Suscriptores a día 90 | 13,500 |
| Patrocinios/mes | 8 |
| EPC afiliados | $0.45 |
| Ingresos | $5,062 |

Aritmética:

```text
Afiliados en sitio:
300,000 × 1.0% × $0.45 = $1,350

Email affiliate:
13,500 × 3 × 30% = 12,150 aperturas
12,150 × 3% = 364.5 clicks
364.5 × 8% = 29.16 ventas
29.16 × $20 = $583

Paid tier:
13,500 × 0.6% = 81
81 × $9 = $729

Patrocinios:
8 × $300 = $2,400

Total:
$1,350 + $583 + $729 + $2,400 = $5,062
```

**Llega, pero apenas.**

---

## Escenario donde no llega

| Variable | Valor |
|---|---:|
| Captura email | 1.5% |
| Suscriptores a día 90 | 13,500 |
| Patrocinios/mes | 7 |
| EPC afiliados | $0.45 |
| Ingresos | $4,762 |

Aritmética:

```text
$1,350 + $583 + $729 + $2,100 = $4,762
```

**No llega.**

Entonces la línea roja es:

```text
Necesitas mínimo:
- Captura ≥ 1.5%
- Patrocinios ≥ 8/mes
- EPC ≥ $0.45
```

Si no cumples eso a día 60, ya sabes que no llegas a $5,000/mes con estas restricciones.

---

# 9. Qué no voy a proponerte

No te voy a proponer:

- AdSense.
- Display.
- Programática.
- Retargeting.
- Banners.
- CPMs.
- Traffic networks.
- Payouts por clic.
- Contratar gente.
- Publicidad pagada.

El plan depende de:

1. **Email.**
2. **Afiliados.**
3. **Patrocinios directos.**
4. **Producto de email.**

Si no aceptas patrocinios directos, el plan no llega.

---

# 10. Checklist de implementación

## Semana 1

- [ ] Crear lead magnet.
- [ ] Configurar email.
- [ ] Añadir CTA de captura.
- [ ] Crear media kit.
- [ ] Crear lista de 200 prospectos.
- [ ] Crear cuentas de afiliados.
- [ ] Añadir disclosure de afiliados.
- [ ] Elegir top 100 artículos para monetizar.

## Semana 2

- [ ] Enviar 50 correos de outreach.
- [ ] Preparar paquetes de patrocinio.
- [ ] Enviar primera newsletter.
- [ ] Añadir afiliados a top 50 artículos.
- [ ] Medir captura.

## Semana 3

- [ ] Enviar 30 correos/día.
- [ ] Hacer follow-ups.
- [ ] Cerrar 1-2 patrocinios.
- [ ] Publicar paid tier en waitlist.
- [ ] Optimizar CTA de email.

## Semana 4

- [ ] Revisar KPIs.
- [ ] Ajustar lead magnet.
- [ ] Ajustar subject lines.
- [ ] Aumentar afiliados en top 100.
- [ ] Negociar 3-5 patrocinios.

## Mes 2

- [ ] 12,000 suscriptores.
- [ ] 6 patrocinios cerrados.
- [ ] Paid tier activo.
- [ ] Ingresos run-rate ~$3,000.

## Mes 3

- [ ] 18,000 suscriptores.
- [ ] 10 patrocinios/mes.
- [ ] Paid tier ~$970/mes.
- [ ] Afiliados ~$2,280/mes.
- [ ] Total ~$6,250/mes.

---

# 11. KPIs diarios

Cada día revisa esto:

| KPI | Meta |
|---|---:|
| Emails enviados | 30 |
| Respuestas de outreach | 5%+ |
| Nuevos suscriptores | 100-200/día |
| Captura de sitio | 2.0%+ |
| Opens de email | 30%+ |
| CTR de email | 3.0%+ |
| Clicks de afiliados | 100+/día |
| EPC | $0.50+ |
| Patrocinios en negociación | 5+ |

---

# 12. Regla de decisión

A día 30, si tienes:

```text
≥ 6,000 suscriptores
≥ 2 patrocinios cerrados
≥ 5 patrocinios en pipeline
EPC ≥ $0.35
CTR email ≥ 2.5%
```

El plan sigue vivo.

Si tienes:

```text
< 4,500 suscriptores
< 2 patrocinios cerrados
Pipeline débil
EPC < $0.30
```

El plan **no llega a $5,000/mes** con tus restricciones.

En ese caso, las únicas opciones serían:

- Bajar el objetivo.
- Permitir display/programática.
- Invertir en tráfico.
- Contratar.
- Cambiar de modelo.

Pero con los números base que propongo, **sí llega a $5,000/mes a día 90, y con margen llega a $6,250/mes**.