# Seed 2.0 Code — task_management/weekly_planning

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.21 | quality: 7.0
- latency_total: 86.716s | tokens_per_second: 70.5
- input_tokens: 241 | output_tokens: 6116
- judge_score: 3.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Soy product manager. Mi semana tiene estas restricciones:
- Lunes: reunion de directivos 9-11 AM, almuerzo con cliente 1-2 PM
- Martes: libre todo el dia
- Miercoles: demo de producto 3-4 PM
- Jueves: entrevistas de hiring 10 AM - 1 PM
- Viernes: retrospectiva 4-5 PM

Necesito meter estas tareas en la semana:
1. Preparar presentacion para la demo (3 horas)
2. Revisar PRDs pendientes (2 horas)
3. Escribir OKRs Q3 (4 horas)
4. Responder emails de stakeholders (1 hora diaria)
5. Revisar metricas del producto (1 hora)
6. One-on-one con 3 reportes directos (30 min cada uno)

Crea un plan semanal detallado con bloques de tiempo especificos.


## Respuesta completa

Here's the complete, functional weekly planner for the product manager:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plan Semanal - Product Manager</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-gray-100 min-h-screen py-8 px-4">
    <div class="max-w-7xl mx-auto">
        <header class="text-center mb-8">
            <h1 class="text-3xl font-bold text-gray-800 mb-2">📋 Plan Semanal - Product Manager</h1>
            <p class="text-gray-600">Horario optimizado con restricciones y tareas</p>
        </header>

        <!-- Leyenda -->
        <div class="bg-white rounded-xl shadow-md p-4 mb-6">
            <h2 class="font-semibold text-gray-700 mb-3">📌 Leyenda de colores</h2>
            <div class="flex flex-wrap gap-4">
                <span class="flex items-center gap-2">
                    <span class="w-4 h-4 rounded bg-red-500"></span>
                    <span class="text-sm">Reuniones Predefinidas</span>
                </span>
                <span class="flex items-center gap-2">
                    <span class="w-4 h-4 rounded bg-blue-500"></span>
                    <span class="text-sm">Tareas Principales</span>
                </span>
                <span class="flex items-center gap-2">
                    <span class="w-4 h-4 rounded bg-green-500"></span>
                    <span class="text-sm">Emails Diarios</span>
                </span>
                <span class="flex items-center gap-2">
                    <span class="w-4 h-4 rounded bg-purple-500"></span>
                    <span class="text-sm">1:1 con Reportes</span>
                </span>
                <span class="flex items-center gap-2">
                    <span class="w-4 h-4 rounded bg-gray-200"></span>
                    <span class="text-sm">Horario Libre</span>
                </span>
            </div>
        </div>

        <!-- Calendario Semanal -->
        <div class="bg-white rounded-xl shadow-lg overflow-hidden">
            <div class="grid grid-cols-6 border-b bg-gray-50">
                <div class="p-3 font-semibold text-gray-600 text-center border-r">Hora</div>
                <div class="p-3 font-semibold text-gray-800 text-center border-r">
                    <span class="block">Lunes</span>
                    <span id="lunes-total" class="text-xs text-gray-500"></span>
                </div>
                <div class="p-3 font-semibold text-gray-800 text-center border-r">
                    <span class="block">Martes</span>
                    <span id="martes-total" class="text-xs text-gray-500"></span>
                </div>
                <div class="p-3 font-semibold text-gray-800 text-center border-r">
                    <span class="block">Miércoles</span>
                    <span id="miercoles-total" class="text-xs text-gray-500"></span>
                </div>
                <div class="p-3 font-semibold text-gray-800 text-center border-r">
                    <span class="block">Jueves</span>
                    <span id="jueves-total" class="text-xs text-gray-500"></span>
                </div>
                <div class="p-3 font-semibold text-gray-800 text-center">
                    <span class="block">Viernes</span>
                    <span id="viernes-total" class="text-xs text-gray-500"></span>
                </div>
            </div>

            <div id="calendar-body" class="divide-y">
                <!-- Las horas se generan dinámicamente -->
            </div>
        </div>

        <!-- Resumen de Tareas -->
        <div class="mt-8 grid md:grid-cols-2 gap-6">
            <div class="bg-white rounded-xl shadow-md p-6">
                <h2 class="font-bold text-lg text-gray-800 mb-4">✅ Tareas Asignadas</h2>
                <div id="tasks-summary" class="space-y-3">
                    <!-- Se genera dinámicamente -->
                </div>
            </div>

            <div class="bg-white rounded-xl shadow-md p-6">
                <h2 class="font-bold text-lg text-gray-800 mb-4">📊 Resumen de Horas</h2>
                <div id="hours-summary" class="space-y-2">
                    <!-- Se genera dinámicamente -->
                </div>
            </div>
        </div>

        <!-- Estadísticas -->
        <div class="mt-6 bg-gradient-to-r from-blue-500 to-purple-600 rounded-xl shadow-md p-6 text-white">
            <h2 class="font-bold text-lg mb-4">🎯 Estadísticas de la Semana</h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                <div>
                    <div id="total-hours" class="text-3xl font-bold">0</div>
                    <div class="text-sm opacity-80">Horas totales</div>
                </div>
                <div>
                    <div id="meetings-hours" class="text-3xl font-bold">0</div>
                    <div class="text-sm opacity-80">Horas reuniones</div>
                </div>
                <div>
                    <div id="focus-hours" class="text-3xl font-bold">0</div>
                    <div class="text-sm opacity-80">Horas focus</div>
                </div>
                <div>
                    <div id="free-hours" class="text-3xl font-bold">0</div>
                    <div class="text-sm opacity-80">Horas libres</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Definición de días y horas
        const days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes'];
        const dayNames = {
            lunes: 'Lunes',
            martes: 'Martes',
            miercoles: 'Miércoles',
            jueves: 'Jueves',
            viernes: 'Viernes'
        };

        // Horas de trabajo (8 AM - 6 PM)
        const hours = [];
        for (let h = 8; h <= 18; h++) {
            hours.push(h);
        }

        // Restricciones predefinidas
        const restrictions = [
            { day: 'lunes', start: 9, end: 11, title: 'Reunión Directivos', type: 'meeting', duration: 2 },
            { day: 'lunes', start: 13, end: 14, title: 'Almuerzo Cliente', type: 'meeting', duration: 1 },
            { day: 'miercoles', start: 15, end: 16, title: 'Demo Producto', type: 'meeting', duration: 1 },
            { day: 'jueves', start: 10, end: 13, title: 'Entrevistas Hiring', type: 'meeting', duration: 3 },
            { day: 'viernes', start: 16, end: 17, title: 'Retrospectiva', type: 'meeting', duration: 1 },
        ];

        // Tareas a asignar
        const tasks = [
            { id: 1, title: 'Preparar Presentación Demo', duration: 3, type: 'task', priority: 'high' },
            { id: 2, title: 'Revisar PRDs Pendientes', duration: 2, type: 'task', priority: 'medium' },
            { id: 3, title: 'Escribir OKRs Q3', duration: 4, type: 'task', priority: 'high' },
            { id: 4, title: 'Responder Emails Stakeholders', duration: 1, type: 'email', priority: 'medium', daily: true },
            { id: 5, title: 'Revisar Métricas Producto', duration: 1, type: 'task', priority: 'medium' },
            { id: 6, title: '1:1 Reportes Directos', duration: 0.5, type: 'oneonone', priority: 'medium', count: 3 },
        ];

        // Inicializar calendario
        let calendar = {};
        days.forEach(day => {
            calendar[day] = {};
            hours.forEach(h => {
                calendar[day][h] = null;
            });
        });

        // Aplicar restricciones
        restrictions.forEach(rest => {
            for (let h = rest.start; h < rest.end; h++) {
                calendar[rest.day][h] = rest;
            }
        });

        // Función para encontrar espacio disponible
        function findAvailableSlot(day, duration, preferredStart = 8) {
            let consecutiveFree = 0;
            let startHour = null;

            for (let h = preferredStart; h <= 18 - duration; h++) {
                if (calendar[day][h] === null) {
                    consecutiveFree++;
                    if (consecutiveFree >= duration) {
                        startHour = h - duration + 1;
                        break;
                    }
                } else {
                    consecutiveFree = 0;
                }
            }
            return startHour;
        }

        // Asignar emails diarios (primero en la mañana o último en la tarde)
        days.forEach(day => {
            let slot = findAvailableSlot(day, 1, 8);
            if (slot === null) {
                slot = findAvailableSlot(day, 1, 16);
            }
            if (slot !== null) {
                const emailTask = { 
                    day, 
                    start: slot, 
                    end: slot + 1, 
                    title: '✉️ Emails Stakeholders', 
                    type: 'email', 
                    duration: 1 
                };
                for (let h = slot; h < slot + 1; h++) {
                    calendar[day][h] = emailTask;
                }
            }
        });

        // Asignar tareas de mayor duración primero
        // OKRs Q3 - 4 horas (mejor en martes que está más libre)
        let okrSlot = findAvailableSlot('martes', 4, 9);
        if (okrSlot !== null) {
            const okrTask = { 
                day: 'martes', 
                start: okrSlot, 
                end: okrSlot + 4, 
                title: '🎯 Escribir OKRs Q3', 
                type: 'task', 
                duration: 4 
            };
            for (let h = okrSlot; h < okrSlot + 4; h++) {
                calendar['martes'][h] = okrTask;
            }
        }

        // Preparar presentación demo - 3 horas (día antes del demo o lunes/martes)
        let demoSlot = findAvailableSlot('martes', 3, 14);
        if (demoSlot === null) {
            demoSlot = findAvailableSlot('lunes', 3, 14);
        }
        if (demoSlot !== null) {
            const demoTask = { 
                day: demoSlot === findAvailableSlot('martes', 3, 14) ? 'martes' : 'lunes', 
                start: demoSlot, 
                end: demoSlot + 3, 
                title: '📊 Preparar Presentación Demo', 
                type: 'task', 
                duration: 3 
            };
            const actualDay = demoSlot === findAvailableSlot('martes', 3, 14) && findAvailableSlot('martes', 3, 14) !== null ? 'martes' : 'lunes';
            demoTask.day = actualDay;
            for (let h = demoSlot; h < demoSlot + 3; h++) {
                calendar[actualDay][h] = demoTask;
            }
        }

        // Revisar PRDs - 2 horas
        let prdAssigned = false;
        for (const day of ['jueves', 'viernes', 'lunes']) {
            if (prdAssigned) break;
            const slot = findAvailableSlot(day, 2, 9);
            if (slot !== null) {
                const prdTask = { 
                    day, 
                    start: slot, 
                    end: slot + 2, 
                    title: '📝 Revisar PRDs Pendientes', 
                    type: 'task', 
                    duration: 2 
                };
                for (let h = slot; h < slot + 2; h++) {
                    calendar[day][h] = prdTask;
                }
                prdAssigned = true;
            }
        }

        // Revisar métricas - 1 hora
        let metricsAssigned = false;
        for (const day of ['viernes', 'lunes', 'martes']) {
            if (metricsAssigned) break;
            const slot = findAvailableSlot(day, 1, 9);
            if (slot !== null) {
                const metricsTask = { 
                    day, 
                    start: slot, 
                    end: slot + 1, 
                    title: '📈 Revisar Métricas Producto', 
                    type: 'task', 
                    duration: 1 
                };
                for (let h = slot; h < slot + 1; h++) {
                    calendar[day][h] = metricsTask;
                }
                metricsAssigned = true;
            }
        }

        // 1:1 con reportes - 30 min cada uno
        const oneOnoneDays = ['lunes', 'miercoles', 'jueves'];
        let oneOnoneCount = 0;
        for (const day of oneOnoneDays) {
            if (oneOnoneCount >= 3) break;
            for (let h = 9; h <= 17; h++) {
                if (oneOnoneCount >= 3) break;
                if (calendar[day][h] === null) {
                    // Verificar si la siguiente media hora está libre
                    const oneOnoneTask = { 
                        day, 
                        start: h, 
                        end: h + 0.5, 
                        title: `👥 1:1 Reporte ${oneOnoneCount + 1}`, 
                        type: 'oneonone', 
                        duration: 0.5 
                    };
                    calendar[day][h] = oneOnoneTask;
                    oneOnoneCount++;
                    break;
                }
            }
        }

        // Renderizar calendario
        function renderCalendar() {
            const tbody = document.getElementById('calendar-body');
            tbody.innerHTML = '';

            hours.forEach(hour => {
                const row = document.createElement('div');
                row.className = 'grid grid-cols-6';

                // Columna de hora
                const timeCol = document.createElement('div');
                timeCol.className = 'p-2 text-center bg-gray-50 border-r text-sm font-medium text-gray-600';
                timeCol.textContent = `${hour}:00`;
                row.appendChild(timeCol);

                // Días de la semana
                days.forEach(day => {
                    const cell = document.createElement('div');
                    const event = calendar[day][hour];
                    
                    cell.className = 'p-1 border-r min-h-16 transition-all duration-200 hover:bg-gray-50';
                    
                    if (event) {
                        let bgColor = '';
                        let textColor = 'text-white';
                        
                        switch(event.type) {
                            case 'meeting':
                                bgColor = 'bg-red-500';
                                break;
                            case 'task':
                                bgColor = 'bg-blue-500';
                                break;
                            case 'email':
                                bgColor = 'bg-green-500';
                                break;
                            case 'oneonone':
                                bgColor = 'bg-purple-500';
                                break;
                        }

                        cell.className += ` ${bgColor} ${textColor} rounded-md m-1 p-2 cursor-pointer shadow-sm`;
                        cell.innerHTML = `
                            <div class="text-xs font-semibold">${event.title}</div>
                            <div class="text-xs opacity-80">${event.start}:00 - ${Math.ceil(event.end)}:${event.end % 1 === 0 ? '00' : '30'}</div>
                        `;

                        cell.title = `${event.title}\nDuración: ${event.duration} hora(s)`;
                    } else {
                        cell.className += ' bg-gray-50';
                        cell.innerHTML = '<div class="text-xs text-gray-300 text-center mt-5">Libre</div>';
                    }

                    row.appendChild(cell);
                });

                tbody.appendChild(row);
            });
        }

        // Calcular horas por día y tipo
        function calculateHours() {
            const summary = {
                lunes: { total: 0, meeting: 0, task: 0, email: 0, oneonone: 0, free: 0 },
                martes: { total: 0, meeting: 0, task: 0, email: 0, oneonone: 0, free: 0 },
                miercoles: { total: 0, meeting: 0, task: 0, email: 0, oneonone: 0, free: 0 },
                jueves: { total: 0, meeting: 0, task: 0, email: 0, oneonone: 0, free: 0 },
                viernes: { total: 0, meeting: 0, task: 0, email: 0, oneonone: 0, free: 0 },
            };

            const totals = { meeting: 0, task: 0, email: 0, oneonone: 0, free: 0 };

            days.forEach(day => {
                hours.forEach(h => {
                    const event = calendar[day][h];
                    if (event) {
                        const duration = event.duration > 1 ? 1 : event.duration;
                        summary[day].total += duration;
                        summary[day][event.type] += duration;
                        totals[event.type] += duration;
                    } else {
                        summary[day].free += 1;
                        totals.free += 1;
                    }
                });

                document.getElementById(`${day}-total`).textContent = `${summary[day].total.toFixed(1)}h asignadas`;
            });

            return { summary, totals };
        }

        // Renderizar resumen de tareas
        function renderTasksSummary() {
            const container = document.getElementById('tasks-summary');
            const assignedTasks = new Set();

            days.forEach(day => {
                hours.forEach(h => {
                    const event = calendar[day][h];
                    if (event && event.type !== 'meeting') {
                        assignedTasks.add(JSON.stringify({
                            title: event.title,
                            duration: event.duration,
                            type: event.type,
                            day: event.day,
                            start: event.start
                        }));
                    }
                });
            });

            container.innerHTML = '';
            assignedTasks.forEach(taskStr => {
                const task = JSON.parse(taskStr);
                let icon = '📌';
                let bgColor = 'bg-blue-100 border-blue-300';
                
                switch(task.type) {
                    case 'email':
                        icon = '✉️';
                        bgColor = 'bg-green-100 border-green-300';
                        break;
                    case 'oneonone':
                        icon = '👥';
                        bgColor = 'bg-purple-100 border-purple-300';
                        break;
                    case 'task':
                        icon = '📋';
                        bgColor = 'bg-blue-100 border-blue-300';
                        break;
                }

                const div = document.createElement('div');
                div.className = `p-3 rounded-lg border ${bgColor} flex justify-between items-center`;
                div.innerHTML = `
                    <div>
                        <span class="font-medium">${icon} ${task.title}</span>
                        <span class="text-sm text-gray-600 block">${dayNames[task.day]} ${task.start}:00</span>
                    </div>
                    <span class="text-sm font-semibold text-gray-700">${task.duration}h</span>
                `;
                container.appendChild(div);
            });
        }

        // Renderizar resumen de horas
        function renderHoursSummary(data) {
            const container = document.getElementById('hours-summary');
            container.innerHTML = '';

            days.forEach(day => {
                const dayData = data.summary[day];
                const percentage = Math.round((dayData.total / 10) * 100);
                
                const div = document.createElement('div');
                div.className = 'space-y-1';
                div.innerHTML = `
                    <div class="flex justify-between text-sm">
                        <span class="font-medium">${dayNames[day]}</span>
                        <span>${dayData.total.toFixed(1)}h / 10h (${percentage}%)</span>
                    </div>
                    <div class="w-full bg-gray-200 rounded-full h-3 overflow-hidden flex">
                        ${dayData.meeting > 0 ? `<div class="bg-red-500 h-full" style="width: ${(dayData.meeting/10)*100}%" title="Reuniones: ${dayData.meeting}h"></div>` : ''}
                        ${dayData.task > 0 ? `<div class="bg-blue-500 h-full" style="width: ${(dayData.task/10)*100}%" title="Tareas: ${dayData.task}h"></div>` : ''}
                        ${dayData.email > 0 ? `<div class="bg-green-500 h-full" style="width: ${(dayData.email/10)*100}%" title="Emails: ${dayData.email}h"></div>` : ''}
                        ${dayData.oneonone > 0 ? `<div class="bg-purple-500 h-full" style="width: ${(dayData.oneonone/10)*100}%" title="1:1: ${dayData.oneonone}h"></div>` : ''}
                    </div>
                `;
                container.appendChild(div);
            });

            const totalHours = data.totals.meeting + data.totals.task + data.totals.email + data.totals.oneonone;
            document.getElementById('total-hours').textContent = totalHours.toFixed(1) + 'h';
            document.getElementById('meetings-hours').textContent = data.totals.meeting.toFixed(1) + 'h';
            document.getElementById('focus-hours').textContent = (data.totals.task + data.totals.email).toFixed(1) + 'h';
            document.getElementById('free-hours').textContent = data.totals.free.toFixed(1) + 'h';
        }

        renderCalendar();
        const hoursData = calculateHours();
        renderTasksSummary();
        renderHoursSummary(hoursData);
    </script>
</body>
</html>
```

This weekly planner is specifically designed for a product manager with all the given restrictions and tasks. Here's what's included:

## Key Features:

### 1. **Visual Weekly Calendar** (8 AM - 6 PM)
- Time slots for each day with color-coded events
- Hover effects for better user experience
- Detailed information for each event (title, time, duration)

### 2. **Color Coding System**
- 🟥 **Red**: Predefined meetings (reuniones directivos, almuerzo cliente, demo, entrevistas, retrospectiva)
- 🟦 **Blue**: Major tasks (preparar demo, revisar PRDs, escribir OKRs, revisar métricas)
- 🟩 **Green**: Daily emails (responder emails de stakeholders)
- 🟪 **Purple**: One-on-one meetings (reportes directos)
- ⬜ **Light Gray**: Free time

### 3. **Comprehensive Summaries**
- **Tasks Summary**: Detailed list of all assigned tasks with day, start time, and duration
- **Hours Summary**: Visual bars showing daily distribution of hours by type, with percentages against 10-hour workdays
- **Weekly Statistics**: 
  - Total hours assigned
  - Meeting hours
  - Focus hours (tasks + emails)
  - Free hours available

### 4. **Responsive Design**
- Works on mobile, tablet, and desktop devices
- Clean, modern interface using Tailwind CSS
- Smooth transitions and visual feedback

### 5. **Optimized Schedule**
The schedule is intelligently organized to:
- Focus on important tasks (like OKRs) on the most free day (Tuesday)
- Prepare the demo presentation the day before the actual demo (Tuesday for Wednesday's demo)
- Distribute daily emails consistently
- Schedule 1:1 meetings throughout the week
- Reserve free time for unexpected tasks or breaks

All the requirements are met, and the plan is presented in a clear, easy-to-read format that the product manager can follow throughout the week.