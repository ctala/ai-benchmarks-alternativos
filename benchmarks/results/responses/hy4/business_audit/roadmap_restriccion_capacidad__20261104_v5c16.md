# Tencent Hy4 — business_audit/roadmap_restriccion_capacidad

- model_id: `tencent/hy4`
- success: True  | final: 5.76 | quality: 6.0
- latency_total: 42.109s | tokens_per_second: 92.2
- input_tokens: 291 | output_tokens: 3883

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

## 1. La matemática real (antes de tocar el roadmap)

Tienes **8 semanas-fundador** (4h/día de construcción). Tus estimaciones están escritas en reloj de equipo ideal (~8h de foco), así que en tu calendario **todo cuesta el doble**. Planifico con ese factor 2x (si ya las habías ajustado a tus 4h, mejor: el plan te da aún más aire).

| Iniciativa | Estimación | Coste en TU reloj | ¿Cabe? |
| :--- | :--- | :--- | :--- |
| **A** (Rewrite) | 3 meses (12 sem) | **24 semanas** | ❌ Son 3 trimestres |
| **B** (Alta) | 1 sem | **2 semanas** | ✅ |
| **C** (Métricas) | 3 sem | **6 semanas** | ⛔ Bloqueada por A |
| **D** (Videos) | 2 sem | **4 semanas** | ✅ |

**Presupuesto:** 8 semanas. **Gasto comprometido (B + D):** 6 semanas. **Colchón:** 2 semanas.

---

## 2. El orden del trimestre

🟢 **Semanas 1–2 → B (Arreglar el paso 2)**
Va primera sin discusión, y no solo por el impacto alto:
1. Cada día que pasa estás tirando el 60% del tráfico que *ya* tienes.
2. **Ataca tu verdadera restricción**: gente atascada en el alta = tickets. Es la única palanca que puede convertir tus 2h/día innegociables de soporte en 1,5h. Arreglar B te devuelve capacidad para el Q que viene.

🟢 **Semanas 3–6 → D (Los 10 videos)**
Justo detrás de B. Traer audiencia antes de arreglar el embudo es regalarla. Con el paso 2 ya sano, cada video cae en una puerta que abre. Es el multiplicador del trimestre y no depende de nada.

🟡 **Semanas 7–8 → Medir, buffer y un *spike* (que NO es empezar A)**
No metas un tercer feature. Reserva estas dos semanas para:
- Comprobar que el drop bajó de verdad (y darle un último ajuste si sigue en ~40%).
- Absorber picos de operación y descansar. Eres uno solo: 8 semanas sin colchón se pagan con burnout en la semana 1 del próximo trimestre.
- **1 o 2 días sueltos** para partir A en migas (decidir qué módulo migrar primero, escribir el plan). Papel, no código.

---

## 3. Lo que dejas fuera (y por qué es la decisión de producto)

🔴 **A se pospone entera. No la arranques "un poquito".**
Son 24 semanas reales. Si la inicias en la semana 1 —o peor, en la 7 con el subidón de haber terminado D— llegas al cierre con dos frameworks conviviendo, ramas divergentes y **más soporte del que ya no puedes delegar**. Para un equipo de 1, un rewrite a medias es peor que el framework viejo. El Q que viene, en vez de *"reescribir la plataforma"*, pon en el roadmap *"migrar el módulo de facturación en 3 semanas"*.

🔴 **C ni se toca.**
Está bloqueada por diseño al depender de A. Y aunque la desacoplaras con un parche temporal, son 6 de tus 8 semanas por impacto medio: cambiarías el arreglo del 60% de abandono por un dashboard. Mal trueque.

---

**En una frase:** *Arregla la puerta, mete gente por la puerta, guarda dos semanas de aire y deja el cambio de cimientos para cuando no estés sosteniendo el techo con la otra mano.*