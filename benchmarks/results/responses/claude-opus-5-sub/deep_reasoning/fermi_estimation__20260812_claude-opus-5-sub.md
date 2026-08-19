# Claude Opus 5 (suscripción) — deep_reasoning/fermi_estimation

- model_id: `claude-opus-5`
- success: True  | final: 0.97 | quality: 0.0
- latency_total: 67.878s | tokens_per_second: 58.9
- input_tokens: 2 | output_tokens: 4001

## Entrada exacta (lo que recibió el modelo)

**user:**

Estima cuantos litros de cafe se consumen al dia en todas las oficinas de Santiago de Chile.

Muestra tu razonamiento paso a paso con cada supuesto numerado.
Da un rango (minimo-maximo) ademas de tu mejor estimacion.
Explica que supuesto tiene mas impacto en el resultado.


## Respuesta completa

# Café en oficinas de Santiago — estimación Fermi

## Cadena de cálculo

| # | Supuesto | Bajo | Central | Alto |
|---|---|---|---|---|
| 1 | Población Gran Santiago | 7,5M | **8,0M** | 8,5M |
| 2 | Ocupados en la RM (participación ~60%, desempleo ~9%) | 3,3M | **3,6M** | 3,9M |
| 3 | % que trabaja en oficina (escritorio, no terreno/retail/construcción) | 22% | **30%** | 38% |
| 4 | % presente en la oficina un día hábil (descuenta teletrabajo, vacaciones, licencias) | 65% | **75%** | 85% |
| 5 | % de esos que toma café en el trabajo | 50% | **65%** | 75% |
| 6 | Tazas por bebedor por día | 1,5 | **2,0** | 3,0 |
| 7 | Litros por taza (mug 250 ml, cortado 150 ml) | 0,15 | **0,20** | 0,25 |

**Cálculo central:**

```
3.600.000 ocupados
× 0,30 (oficina)      = 1.080.000 oficinistas
× 0,75 (presentes)    =   810.000 presentes
× 0,65 (toman café)   =   526.500 bebedores
× 2,0  (tazas/día)    = 1.053.000 tazas
× 0,20 L              =   210.600 litros
```

## Mejor estimación

**≈ 210.000 litros por día hábil** (orden de magnitud: 2×10⁵ L).

Equivale a unos 8 camiones aljibe, o llenar el 8% de una piscina olímpica. Diario.

## Rango

- **Multiplicando todos los extremos:** 58.000 – 655.000 L
- **Rango razonable a reportar: 120.000 – 350.000 L/día**

La segunda cifra es la útil. Que las siete variables caigan simultáneamente en su extremo bajo (o alto) es estadísticamente improbable: los errores independientes se cancelan parcialmente. El rango naive de 11× exagera la incertidumbre real, que está más cerca de 3×.

## Chequeo por otra vía (masa de café)

Consumo per cápita en Chile ≈ 0,9 kg/año de café. Con 20M de habitantes → ~18.000 t/año. Santiago concentra ~40% de la población pero con mayor ingreso → asumo 50% del consumo = 9.000 t/año. Si ~25% se toma en oficinas → 2.250 t/año ÷ 250 días hábiles = **9 t/día**.

Chile es país de café instantáneo (~2 g/taza) mezclado con filtrado y espresso (~8 g). Promedio ponderado ~6 g/taza → 9.000 kg ÷ 0,006 = **1,5 millones de tazas/día** → ~300.000 L.

Las dos rutas dan 1,05M y 1,5M de tazas. Coinciden dentro de un factor 1,4. Eso da confianza en el orden de magnitud, no en el segundo dígito.

## El supuesto que más pesa

**#6: tazas por bebedor por día** (rango 1,5–3,0 = factor 2,0, el más ancho de la cadena).

No es solo el rango: es que depende de una variable binaria que no está en el modelo — **si el café es gratis o se paga**. En una oficina con máquina automática libre el consumo se va a 3-4 tazas; donde cada uno compra el suyo en la esquina, baja a 1. La distribución real probablemente es bimodal, no una campana alrededor de 2.

Segundo en impacto, **#3: qué cuenta como "oficina"** (factor 1,7). Este es un problema de definición, no de medición: ¿el vendedor con tablet en terreno? ¿la recepcionista de una clínica? Mover la frontera cambia el resultado 70% sin que ningún dato esté mal.

**Cómo reducir el error rápido:** una encuesta de 200 personas en 10 edificios de Providencia/Las Condes fijando #5, #6 y #7 (todo lo demás sale de datos INE) colapsaría el rango de 3× a ~1,4×. Los tres supuestos más blandos son también los más baratos de medir.