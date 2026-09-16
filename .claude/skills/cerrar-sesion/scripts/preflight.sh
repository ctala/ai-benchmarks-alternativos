#!/usr/bin/env bash
# preflight.sh — diagnóstico READ-ONLY del cierre de sesión del benchmark.
# NO modifica nada. Adaptado del homónimo del repo padre: allá recorre `.gitmodules`,
# acá los repos son tres y fijos — este submodule, el blog (repo hermano) y el padre,
# que sólo lleva el pointer.
#
# Uso:  bash .claude/skills/cerrar-sesion/scripts/preflight.sh
set -uo pipefail

SECRET_PATTERNS='sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{20,}|apify_api_[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|gh[ous]_[A-Za-z0-9]{30,}|eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}|(TOKEN|SECRET|API[-_]?KEY|APIKEY|PASSWORD)["'"'"' ]*[:=]["'"'"' ]*[A-Za-z0-9/+._=-]{16,}'

SUCIO=0

scan_repo () {
  local dir="$1" label="$2" solo_propio="${3:-no}"
  git -C "$dir" rev-parse --show-toplevel >/dev/null 2>&1 || { printf '  ?  %s — no es un repo\n' "$label"; return 0; }
  local branch estado sin_pushear
  branch="$(git -C "$dir" branch --show-current 2>/dev/null || echo '?')"
  estado="$(git -C "$dir" status --short 2>/dev/null)"
  sin_pushear="$(git -C "$dir" log --oneline '@{u}..HEAD' 2>/dev/null)"

  # En el padre lo ajeno es la norma: se cuenta, no se lista entero.
  if [ "$solo_propio" = "si" ] && [ -n "$estado" ]; then
    local n; n="$(printf '%s\n' "$estado" | wc -l | tr -d ' ')"
    estado="$(printf '%s\n' "$estado" | grep -E '^[ AMD?]{2}benchmarks$' || true)"
    [ -z "$estado" ] && estado="" || estado="$estado    (+ $((n-1)) cambios ajenos, se dejan)"
  fi

  if [ -z "$estado" ] && [ -z "$sin_pushear" ]; then
    printf '  ✓ %-28s [%s] limpio y pusheado\n' "$label" "$branch"
    return 0
  fi
  SUCIO=1
  echo "──────────────────────────────────────────────────────"
  echo "▶ $label   [$branch]"
  [ -n "$estado" ] && { echo "  Working tree:"; echo "$estado" | sed 's/^/    /'; }
  [ -n "$sin_pushear" ] && { echo "  Commiteado pero SIN pushear:"; echo "$sin_pushear" | sed 's/^/    /'; }

  # Secret scan: sólo reporta el path, nunca el valor, y no sigue symlinks.
  local hits
  hits="$( { git -C "$dir" diff --name-only --diff-filter=ACMR HEAD -z 2>/dev/null
             git -C "$dir" ls-files --others --exclude-standard -z 2>/dev/null
           } | while IFS= read -r -d '' f; do
                 [ -f "$dir/$f" ] && [ ! -L "$dir/$f" ] || continue
                 grep -Iq . "$dir/$f" 2>/dev/null || continue
                 grep -qEi "$SECRET_PATTERNS" "$dir/$f" 2>/dev/null && printf '%s\n' "$f"
               done | head -5 )"
  [ -n "$hits" ] && { echo "  ⚠️  POSIBLE SECRETO — no commitear sin revisar:"; echo "$hits" | sed 's/^/    archivo: /'; }
}

BENCH="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -z "${BENCH:-}" ] && { echo "No estás dentro del repo del benchmark."; exit 1; }
PADRE="$(cd "$BENCH/.." && pwd -P)"
BLOG="$HOME/Playground/sitios/cristiantala-blog"

echo "════════════════════════════════════════════════════════"
echo " CIERRE DE SESIÓN · benchmark · preflight (read-only)"
echo "════════════════════════════════════════════════════════"
scan_repo "$BENCH" "benchmarks (este)"
[ -d "$BLOG/.git" ] && scan_repo "$BLOG" "blog (repo hermano)" || echo "  ⏭️  blog no clonado acá"
scan_repo "$PADRE" "Estrategias (padre)" "si"

# El pointer es el error silencioso clásico: el padre apuntando a un commit que no está
# en el remoto, o a uno viejo. Se compara contra el HEAD de este repo.
puntero="$(git -C "$PADRE" ls-tree HEAD benchmarks 2>/dev/null | awk '{print $3}')"
head_bench="$(git -C "$BENCH" rev-parse HEAD 2>/dev/null)"
echo "──────────────────────────────────────────────────────"
if [ "$puntero" = "$head_bench" ]; then
  echo "  ✓ el pointer del padre apunta al HEAD de benchmarks"
else
  SUCIO=1
  echo "  ⚠️  el pointer del padre (${puntero:0:9}) NO es el HEAD de benchmarks (${head_bench:0:9})"
  echo "     → commitear el pointer DESPUÉS de pushear este repo"
fi

echo "──────────────────────────────────────────────────────"
if [ "$SUCIO" -eq 0 ]; then
  echo "RESULTADO: todo limpio y pusheado. Nada que cerrar."
else
  echo "RESULTADO: hay trabajo pendiente. Staging SELECTIVO, este repo antes que el padre."
fi
echo "════════════════════════════════════════════════════════"
