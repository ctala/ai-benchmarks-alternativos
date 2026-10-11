# MiMo V2.6 Flash — sales_outreach/campaign_optimization

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 742.917s | tokens_per_second: 5.1
- input_tokens: 306 | output_tokens: 3759

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estos resultados de mi campana de Google Ads del ultimo mes:

Campana A (Landing principal):
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100
- Keywords: "software gestion inventario", "inventario pymes"

Campana B (Blog content):
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800
- Keywords: "como gestionar inventario", "problemas inventario restaurante"

Campana C (Competidor):
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200
- Keywords: "alternativa a [competidor]", "[competidor] vs"

Mi presupuesto total es $5,000/mes.

1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?


## Respuesta completa

# 📊 Análisis Completo de Campañas de Google Ads

## 1. MÉTRICAS CALCULADAS

### Fórmulas aplicadas
| Métrica | Fórmula |
|---------|---------|
| **CTR** | Clicks ÷ Impresiones × 100 |
| **CPC** | Costo ÷ Clicks |
| **CPA** | Costo ÷ Signups |
| **Conv. Rate** | Signups ÷ Clicks × 100 |

---

### 📋 Tabla Comparativa

| Métrica | **Campaña A** | **Campaña B** | **Campaña C** |
|---------|:---:|:---:|:---:|
| **CTR** | **3.00%** | **4.00%** | **6.00%** |
| **CPC** | **$1.40** | **$0.375** | **$3.56** |
| **CPA** | **$46.67** ✅ | **$75.00** | **$88.89** ❌ |
| **Conv. Rate** | **3.00%** | **0.50%** ❌ | **4.00%** ✅ |
| **Costo** | $2,100 | $1,800 | $3,200 |
| **Signups** | 45 | 24 | 36 |

> ⚠️ **Nota:** El costo total actual ($7,100) **supera tu presupuesto de $5,000**. Esto es algo a corregir inmediatamente.

---

## 2. ¿Qué escalar y qué pausar?

### 🟢 ESCALAR → Campaña A (Landing Principal)

```
Razones:
├── ✅ Mejor CPA: $46.67 (47% más barato que C, 38% más barato que B)
├── ✅ Conv. Rate sólida: 3% (6x mejor que B)
├── ✅ CPC moderado: $1.40 (manejable)
├── ✅ Volumen razonable: 45 signups con $2,100
└── ✅ Keywords de alta intención comercial
    "software gestion inventario" = el usuario busca comprar
```

**Por qué escalarla:** Es la única campaña con un CPA por debajo de $50 y una tasa de conversión que no depende de tráfico barato (a diferencia de B). Si la duplicas a $4,200, proyectas ~90 signups.

---

### 🟡 OPTIMIZAR (no pausar del todo) → Campaña B (Blog Content)

```
Problemas:
├── ❌ Conv. Rate pésima: 0.50% (1 de cada 200 visitantes convierte)
├── ❌ CPA alto: $75.00
├── ❌ Tráfico barato pero inútil: CPC de $0.375
└── ❌ Top-funnel puro: "como gestionar inventario" 
    = el usuario quiere aprender, NO comprar
```

**Diagnóstico:** El problema no es la campaña en sí, sino que **el tráfico top-funnel llega a una landing de conversión**. Un usuario que busca *"como gestionar inventario"* no está listo para dar sus datos. Necesita **nurturing**, no una landing de signup.

---

### 🔴 REDUCIR → Campaña C (Competidor)

```
Problemas:
├── ❌ CPA más alto: $88.89 (el más caro de las 3)
├── ❌ CPC excesivo: $3.56 (keywords de competidor son carísimas)
├── ❌ 58% del presupuesto actual para el 18% de las impresiones
└── ❌ Comió $3,200 = 64% de tu presupuesto de $5,000

PERO también tiene:
├── ✅ Mejor Conv. Rate: 4% (el más alto)
├── ✅ Mejor CTR: 6% (el más alto)
└── ✅ Alto intento de compra (comparan alternativas)
```

**Diagnóstico:** Los leads de C probablemente son de **mayor calidad** (están comparando, listos para decidir), pero el CPA es insostenible a este volumen. **No la pauses, pero reduce su presupuesto** y optimiza las keywords para bajar el CPC.

---

### Resumen de decisión:

```
Campaña A → 🟢 ESCALAR    (mejor ROI absoluto)
Campaña B → 🟡 OPTIMIZAR   (bajar presupuesto, cambiar landing)
Campaña C → 🔴 REDUCIR     (mantener presencia, bajar costo)
```

---

## 3. Redistribución del presupuesto ($5,000)

### Propuesta:

| Campaña | Actual | Propuesto | Cambio | Justificación |
|---------|:---:|:---:|:---:|---|
| **A** | $2,100 | **$2,500** | +$400 📈 | Escalar lo que funciona |
| **B** | $1,800 | **$700** | -$1,100 📉 | Reducir hasta optimizar |
| **C** | $3,200 | **$1,500** | -$1,700 📉 | Reducir CPA insostenible |
| **Reserva A/B** | $0 | **$300** | +$300 | Tests del próximo mes |
| **TOTAL** | $7,100 | **$5,000** | ✅ | Dentro de presupuesto |

### Proyección con nueva distribución:

```
Campaña A: $2,500 ÷ $46.67 CPA = ~53 signups
Campaña B: $700  ÷ $75.00 CPA = ~9 signups  (hasta optimizar)
Campaña C: $1,500 ÷ $88.89 CPA = ~17 signups
           ─────────────────────────────────
TOTAL PROYECTADO: ~79 signups (vs. 105 actuales con $7,100)
```

> **Pero con $5,000 en lugar de $7,100, pasas de 105 signups a ~79 signups = 75% de eficiencia con 70% del gasto.** El CPA promedio baja de **$67.62** a **$63.29**.

### Visualización del cambio:

```
ANTES ($7,100):                    DESPUÉS ($5,000):
┌──────────────┐ 30%              ┌──────────────┐ 50%  📈
│  A: $2,100   │                  │  A: $2,500   │
├──────────────┤ 25%              ├──────────────┤ 30%  📉
│  B: $1,800   │                  │  C: $1,500   │
├──────────────┤ 45%  ⚠️          ├──────────────┤ 14%  📉
│  C: $3,200   │                  │  B: $700     │
└──────────────┘                  ├──────────────┤  6%
                                  │ Reserva:300  │
                                  └──────────────┘
```

---

## 4. A/B Tests para el próximo mes

### 🧪 Test 1: Landing Page de Campaña A
```
Hipótesis: Una landing con formulario de 3 campos 
           convierte mejor que uno de 5 campos

Variante A: Formulario actual (5 campos: nombre, email, empresa, 
            cargo, teléfono)
Variante B: Formulario simplificado (3 campos: nombre, email, empresa)
            + "Llénalo después"

Métrica: Conversion Rate
Duración: 2 semanas
Tamaño mínimo: 1,000 clicks por variante
```

### 🧪 Test 2: Campaña B - Cambio de Landing
```
Hipótesis: Enviar tráfico blog → landing de producto es el error.
           Un lead magnet convierte mejor.

Variante A (actual): Blog → Landing de signup directo (CVR: 0.5%)
Variante B (nuevo):  Blog → Página de descarga gratuita 
                     ("Checklist: 10 errores de inventario 
                      que cuestan dinero") → Captura email → 
                     Secuencia de nurturing → Signup

Métrica: Costo por lead capturado
Duración: 4 semanas
```

### 🧪 Test 3: Campaña C - Reducción de CPC
```
Hipótesis: Eliminar keywords genéricas de competidor y usar 
           solo long-tail reduce el CPC sin perder calidad

Variante A (actual): "alternativa a [competidor]" 
Variante B (nuevo):  "alternativa a [competidor] para pymes"
                     "migrar de [competidor] a [otro]"
                     "[competidor] precio vs [nuestro] precio"

Métrica: CPC y CPA
Duración: 2 semanas
```

### 🧪 Test 4: Copy de anuncios (todas las campañas)
```
Hipótesis: Los anuncios con prueba social en el título 
           generan mayor CTR

Variante A: "Software de Gestión de Inventario - Empieza Gratis"
Variante B: "Software de Gestión de Inventario - 500+ pymes 
            ya confían en nosotros - Empieza Gratis"

Métrica: CTR
Duración: 1 semana
```

### 🧪 Test 5: Campaña A - Horario de activación
```
Hipótesis: Mostrar anuncios solo en horario laboral (8am-6pm) 
           mejora CPA porque los compradores deciden en horario 
           de trabajo

Variante A: 24/7 (actual)
Variante B: L-V 8am-6pm (hora local del público objetivo)

Métrica: CPA
Duración: 2 semanas
```

---

## 📌 Plan de Acción Resumido

```
SEMANA 1:
  ├── Pausar Campaña B (o reducir a $700/mes)
  ├── Reducir presupuesto de Campaña C a $1,500/mes
  ├── Escalar Campaña A a $2,500/mes
  └── Configurar límites de presupuesto diarios

SEMANA 2-3:
  ├── Lanzar Test 1 (formularios)
  ├── Lanzar Test 4 (copy de anuncios)
  └── Construir landing de lead magnet para Campaña B

SEMANA 4:
  ├── Lanzar Test 3 (keywords long-tail en C)
  ├── Revisar resultados de Tests 1 y 4
  └── Preparar Test 5 para el mes siguiente

FIN DE MES:
  ├── Revisar métricas actualizadas
  └── Reasignar presupuesto según resultados
```

> **Objetivo del próximo mes:** Bajar el **CPA promedio de $67.62 a menos de $55** y lograr al menos **75 signups con $5,000**.