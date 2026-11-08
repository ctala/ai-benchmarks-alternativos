# Muse Wonder — deep_reasoning/math_word_problem

- model_id: `meta/muse-wonder`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 8.916s | tokens_per_second: 150.5
- input_tokens: 90 | output_tokens: 1342

## Entrada exacta (lo que recibió el modelo)

**user:**

Un tren sale de Santiago a las 8:00 AM hacia Valparaiso a 80 km/h.
Otro tren sale de Valparaiso a las 8:30 AM hacia Santiago a 120 km/h.
La distancia entre ambas ciudades es 120 km.
A que hora se cruzan los trenes y a que distancia de Santiago?

Muestra todo el razonamiento paso a paso.


## Respuesta completa

Vamos a resolverlo paso a paso.

### Datos
* Distancia Santiago - Valparaíso: $120 \text{ km}$
* Tren 1 (desde Santiago): sale a las **8:00 AM** a $80 \text{ km/h}$
* Tren 2 (desde Valparaíso): sale a las **8:30 AM** a $120 \text{ km/h}$

Los trenes van en sentidos opuestos, por lo que se acercan el uno al otro.

### Paso 1: ¿Qué pasa hasta las 8:30 AM?

Entre las 8:00 y las 8:30 solo se mueve el primer tren, durante $0,5$ horas.

Distancia recorrida por el Tren 1:
$$ d = v \cdot t = 80 \text{ km/h} \cdot 0,5 \text{ h} = 40 \text{ km} $$

A las 8:30 AM, el Tren 1 ya está a 40 km de Santiago.

Por lo tanto, la distancia que queda entre ambos trenes en ese momento es:
$$ 120 \text{ km} - 40 \text{ km} = 80 \text{ km} $$

### Paso 2: Calcular el tiempo que tardan en encontrarse desde las 8:30

Desde las 8:30 ambos trenes se mueven hacia el encuentro.

Su velocidad de acercamiento es la suma de sus velocidades:
$$ v_{relativa} = 80 \text{ km/h} + 120 \text{ km/h} = 200 \text{ km/h} $$

Tiempo para cubrir los 80 km que los separan:
$$ t = \frac{d}{v} = \frac{80 \text{ km}}{200 \text{ km/h}} = 0,4 \text{ h} $$

Convertimos a minutos:
$$ 0,4 \text{ h} \cdot 60 \text{ min/h} = 24 \text{ minutos} $$

### Paso 3: Hora del cruce

$$ 8:30 \text{ AM} + 24 \text{ minutos} = \mathbf{8:54 \text{ AM}} $$

### Paso 4: Distancia desde Santiago

El Tren 1 viajó en total:
* 40 km antes de las 8:30
* Más lo que recorre en esos 24 minutos (0,4 h) después:

$$ d_{extra} = 80 \text{ km/h} \cdot 0,4 \text{ h} = 32 \text{ km} $$

Distancia total desde Santiago:
$$ 40 \text{ km} + 32 \text{ km} = \mathbf{72 \text{ km}} $$

**Comprobación:** El Tren 2 recorre en 0,4 h: $120 \cdot 0,4 = 48$ km desde Valparaíso. $120 - 48 = 72$ km desde Santiago. Coincide.

### Respuesta
Los trenes se cruzan a las **8:54 AM**, a **72 km de Santiago** (y a 48 km de Valparaíso).