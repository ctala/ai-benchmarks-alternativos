# Gemma 4 26B MoE (3.8B activos) — reasoning/logical_reasoning

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.46 | quality: 9.04
- latency_total: 21.0s | tokens_per_second: 50.5
- input_tokens: 137 | output_tokens: 1061
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para resolver este problema, vamos a organizar la información disponible y utilizar el álgebra para encontrar los valores desconocidos.

### 1. Identificación de los datos (Variables)
Llamemos a la cantidad de personas de cada equipo por su letra: $A, B, C, D, E$.

De los enunciados extraemos lo siguiente:
1.  $B < A < C$
2.  $D = A$
3.  $E$ es el valor más pequeño de todos.
4.  $A + B + C + D + E = 60$
5.  Todos los equipos $\ge 5$
6.  $C = 2E$
7.  $B = 10$

### 2. Sustitución de valores conocidos
Sabemos que **$B = 10$**. Sustituimos este valor en las condiciones para simplificar:

*   De la condición 1: $10 < A < C$
*   De la condición 2: $D = A$
*   De la condición 4 (Suma total): $A + 10 + C + A + E = 60$
    Simplificando la ecuación de la suma:
    $2A + C + E = 50$

### 3. Relación entre C y E
Sabemos por la condición 6 que $C = 2E$. Vamos a sustituir $C$ en la ecuación de la suma para tener solo dos variables ($A$ y $E$):

$2A + (2E) + E = 50$
$2A + 3E = 50$

### 4. Búsqueda de valores mediante restricciones
Ahora debemos encontrar valores para $A$ y $E$ que cumplan con todas las reglas:
*   **Regla A:** $A > 10$ (porque $A > B$ y $B=10$).
*   **Regla B:** $E < 10$ (porque $E$ es el menor de todos y $B=10$).
*   **Regla C:** $C > A$ (donde $C = 2E$).

Probemos valores para **$E$** (recordando que $E$ debe ser menor que 10 y que $2A + 3E = 50$):

*   **Si $E = 9$:**
    $2A + 3(9) = 50 \Rightarrow 2A + 27 = 50 \Rightarrow 2A = 23 \Rightarrow A = 11.5$ (No es posible, las personas deben ser números enteros).

*   **Si $E = 8$:**
    $2A + 3(8) = 50 \Rightarrow 2A + 24 = 50 \Rightarrow 2A = 26 \Rightarrow \mathbf{A = 13}$
    *Verifiquemos este resultado:*
    Si $A = 13$, entonces $D = 13$ (porque $D=A$).
    Si $E = 8$, entonces $C = 16$ (porque $C=2E$).
    $B = 10$.
    *Comprobemos las condiciones:*
    1. ¿$B < A < C$? $\rightarrow 10 < 13 < 16$ (**SÍ**)
    2. ¿$D = A$? $\rightarrow 13 = 13$ (**SÍ**)
    3. ¿$E$ es el menor? $\rightarrow 8$ es menor que 10, 13 y 16 (**SÍ**)
    4. ¿La suma es 60? $\rightarrow 13 + 10 + 16 + 13 + 8 = 60$ (**SÍ**)
    5. ¿Ninguno tiene menos de 5? (**SÍ**)
    6. ¿$C$ es el doble de $E$? $\rightarrow 16 = 2(8)$ (**SÍ**)

*Nota: Si probáramos con $E=6$, $2A + 18 = 50 \Rightarrow 2A = 32 \Rightarrow A = 16$. Pero si $A=16$, entonces $C=2E=12$. Esto rompería la regla $A < C$ (16 no es menor que 12). Por tanto, $E=8$ es la única solución lógica.*

### Resultado Final:
*   **Equipo A:** 13 personas
*   **Equipo B:** 10 personas
*   **Equipo C:** 16 personas
*   **Equipo D:** 13 personas
*   **Equipo E:** 8 personas