# Qwen 3.8 27B — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 92.909s | tokens_per_second: 137.7
- input_tokens: 351 | output_tokens: 12794

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



## 1) CTR, CPC, CPA y conversión de cada campaña

Fórmulas usadas:

- **CTR** = Clicks ÷ Impresiones × 100  
- **CPC** = Costo ÷ Clicks  
- **CPA** = Costo ÷ Signups  
- **Conversion rate / CVR** = Signups ÷ Clicks × 100  

| Campaña | Impresiones | Clicks | Signups | Costo | CTR | CPC | CPA | CVR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A — Landing principal** | 50,000 | 1,500 | 45 | $2,100 | **3.00%** | **$1.40** | **$46.67** | **3.00%** |
| **B — Blog content** | 120,000 | 4,800 | 24 | $1,800 | **4.00%** | **$0.38** | **$75.00** | **0.50%** |
| **C — Competidor** | 15,000 | 900 | 36 | $3,200 | **6.00%** | **$3.56** | **$88.89** | **4.00%** |

### Lectura rápida

| Campaña | Signups por cada $1,000 | Interpretación |
|---|---:|---|
| **A** | **21.43** | Mejor costo por signup. Tráfico con intención clara. |
| **B** | **13.33** | Mucha audiencia y clicks baratos, pero muy poca conversión. |
| **C** | **11.25** | Alta intención, pero muy caro por click y por signup. |

Nota: los costos actuales suman **$7,100**, por lo que si tu presupuesto real es **$5,000/mes**, hay que recortar y reasignar.

---

## 2) ¿Qué campaña escalar y cuál pausar?

### Recomendación principal

- **Escalar: Campaña A**
- **Pausar: Campaña B**
- **Campaña C: mantener en nivel de prueba, pero no escalar todavía**

### Justificación con números

#### Campaña A: escalar

Es la más eficiente para conseguir signups:

- **CPA: $46.67**
- **CVR: 3.00%**
- **CTR: 3.00%**
- **CPC: $1.40**
- Genera **21.43 signups por cada $1,000**

Además, sus keywords tienen intención comercial:

- “software gestion inventario”
- “inventario pymes”

Esto significa que la gente ya está buscando una solución, no solo información.

#### Campaña B: pausar o reducir drásticamente

Tiene buen volumen, pero no convierte:

- **CTR: 4.00%**
- **CPC: $0.38**, muy barato
- Pero **CVR: 0.50%**
- **CPA: $75.00**

Sus keywords son más informativas:

- “como gestionar inventario”
- “problemas inventario restaurante”

Es tráfico top-of-funnel: gente buscando aprender, no necesariamente comprar o registrarse. Para el objetivo de signups, está desperdiciando presupuesto.

#### Campaña C: no escalar aún, pero no la mataría

Tiene los mejores indicadores de intención:

- **CTR: 6.00%**
- **CVR: 4.00%**

Pero es muy cara:

- **CPC: $3.56**
- **CPA: $88.89**

Es decir: convierte mejor que A, pero su CPC es **2.5 veces más alto** que el de A, y su CPA es **1.9 veces más alto**.

Por eso: no la escalo todavía, pero sí la mantengo con un presupuesto pequeño porque puede ser valiosa si logras bajar el CPC o si el valor del cliente justifica ese CPA.

---

## 3) ¿Cómo redistribuiría el presupuesto de $5,000?

### Recomendación principal

| Campaña | Presupuesto mensual | % del total | Acción |
|---|---:|---:|---|
| **A — Landing principal** | **$4,000** | **80%** | Escalar |
| **C — Competidor** | **$1,000** | **20%** | Mantener como prueba |
| **B — Blog content** | **$0** | **0%** | Pausar |
| **Total** | **$5,000** | **100%** |  |

### Proyección esperada manteniendo la misma eficiencia actual

| Campaña | Presupuesto | Clicks esperados | Signups esperados | CPA esperado |
|---|---:|---:|---:|---:|
| **A** | $4,000 | 2,857 | 85.7 | $46.67 |
| **C** | $1,000 | 281 | 11.3 | $88.89 |
| **B** | $0 | 0 | 0 | — |
| **Total** | **$5,000** | **3,138** | **~97 signups** | **~$51.57** |

### Por qué no poner todo en A

Si pusieras los $5,000 completos en A, la proyección sería:

- Clicks: 3,571
- Signups: **107.1**
- CPA: **$46.67**

Eso sería mejor en términos puros de signups, pero no lo recomendaría como única opción porque:

1. Aumentar mucho el presupuesto puede subir el CPC.
2. Perderías la señal de la campaña C, que tiene la mejor tasa de conversión.
3. Las keywords de competidor suelen ser estratégicas: alta intención, aunque caras.

Por eso propongo **80% en A y 20% en C**.

### Alternativa más conservadora

Si quieres aprender más de la campaña C:

| Campaña | Presupuesto |
|---|---:|
| A | $3,500 |
| C | $1,500 |
| B | $0 |

Proyección:

- A: ~75 signups
- C: ~16.9 signups
- Total: **~91.9 signups**
- CPA blended: **~$54.42**

Es menos eficiente que $4,000 A + $1,000 C, pero te da más información de la campaña de competidor.

### Alternativa agresiva

Si tu objetivo es maximizar signups este mes y aceptas más riesgo:

| Campaña | Presupuesto |
|---|---:|
| A | $5,000 |
| C | $0 |
| B | $0 |

Proyección:

- **~107 signups**
- CPA: **$46.67**

Pero perderías el test de competidor.

---

## 4) A/B tests que sugeriría para el próximo mes

### Prioridad 1: Landing page de la Campaña A

La Campaña A es la que más presupuesto va a recibir, así que mejorar su conversión impacta directo en el CPA.

#### Test A: reducir fricción en el formulario

**Variante control:** formulario actual.  
**Variante B:** formulario más corto, por ejemplo solo:

- Nombre
- Email
- Empresa
- Botón: “Crear cuenta gratis” o “Probar gratis 14 días”

**Hipótesis:** menos campos aumentan el CVR.  
**Métrica principal:** CVR.  
**Métrica secundaria:** CPA.  
**Meta sugerida:** subir CVR de **3.00%** a **3.50%+** o bajar CPA por debajo de **$40**.

#### Test B: propuesta de valor en el H1

**Variante A:** “Software de gestión de inventario”  
**Variante B:** “Gestiona tu inventario sin Excel y sin errores”  
**Variante C:** “Inventario claro para pymes en minutos”

**Métrica:** CVR y CPA.  
**Objetivo:** encontrar el mensaje que conecta mejor con “software gestion inventario” e “inventario pymes”.

#### Test C: prueba social + CTA

Agregar:

- Testimonio de cliente
- Logo de empresas
- “Prueba gratis 14 días”
- “Sin tarjeta de crédito”
- “Migración asistida” o “soporte en español”

**Meta:** aumentar CVR sin aumentar CPC.

---

### Prioridad 2: Campaña C — Competidor

Aquí el problema no es la conversión, sino el costo por click.

#### Test A: landing page de comparación

En lugar de llevar a la landing genérica, crear una landing específica:

**Título:**  
“¿Usas [competidor]? Compara funciones, precio y facilidad de uso”

Secciones:

- Tabla comparativa
- “Por qué cambiar”
- “Migración gratis”
- “Sin permanencia”
- Testimonio de cliente que cambió
- CTA: “Ver alternativa gratis”

**Meta:** mantener CVR cerca de **4%** y reducir CPC.

#### Test B: anuncios con ángulo de cambio

**Anuncio 1:**  
“¿Cansado de [competidor]? Prueba una alternativa más simple.”  
CTA: “Ver comparación”

**Anuncio 2:**  
“[Competidor] vs [Tu producto]: precio, funciones y soporte.”  
CTA: “Comparar gratis”

**Anuncio 3:**  
“Migra de [competidor] en minutos. Prueba gratis.”  
CTA: “Empieza ahora”

**Meta:** mejorar CTR y reducir CPC.

#### Objetivo de eficiencia para C

Hoy:

- CPC: **$3.56**
- CVR: **4%**
- CPA: **$88.89**

Si logras bajar el CPC a **$2.80** manteniendo CVR en 4%, el CPA bajaría a:

- **$70**

Si logras bajarlo a **$2.00**, el CPA sería:

- **$50**

Eso haría a C mucho más escalable.

---

### Prioridad 3: Keywords y palabras negativas

#### Para Campaña A

Agregar negativas si no están convirtiendo:

- “gratis”
- “excel”
- “plantilla”
- “curso”
- “empleo”
- “pdf”
- “cargos”
- “sueldo”
- “universidad”

Objetivo: evitar clicks de personas que no buscan software.

#### Para Campaña C

Agregar negativas según el caso:

- “precio”
- “opiniones”
- “quejas”
- “salir”
- “cancelar”
- “alternativa gratis”

Objetivo: filtrar tráfico que no está listo para comparar o comprar.

---

### Prioridad 4: Si no quieres pausar totalmente B

La Campaña B tiene buen CTR y CPC bajo, pero mala conversión. Si quieres conservarla, no la uses para pedir signup directo.

#### Opción: convertir B en lead magnet + retargeting

En lugar de “Regístrate”, ofrecer:

- “Checklist de inventario para restaurantes”
- “Plantilla de inventario en Excel”
- “Guía: cómo controlar inventario sin errores”
- “Calculadora de mermas”

Luego, retargetear a quienes descargaron el recurso con anuncios de:

- Demo gratis
- Prueba 14 días
- Caso de éxito
- “Empieza a controlar tu inventario hoy”

**Meta:** no medir solo signups inmediatos, sino leads cualificados y CPA de retargeting.

---

## Resumen ejecutivo

1. **Campaña A es la ganadora**: CPA de **$46.67**, CVR **3%** y keywords comerciales.  
2. **Campaña B debe pausarse**: tiene muchos clicks baratos, pero CVR de solo **0.50%** y CPA de **$75**.  
3. **Campaña C no se escala aún**: tiene buena conversión, **4%**, pero CPC alto, **$3.56**, y CPA de **$88.89**.  
4. **Presupuesto recomendado**:  
   - **A: $4,000**
   - **C: $1,000**
   - **B: $0**
5. **Proyección**: alrededor de **97 signups** con CPA blended de **~$51.57**.  
6. **Tests prioritarios**: mejorar landing de A, crear landing comparativa para C, añadir palabras negativas y, si se mantiene B, convertirla en lead magnet + retargeting.