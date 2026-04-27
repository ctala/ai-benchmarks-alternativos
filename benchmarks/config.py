"""
Configuracion del benchmark — variables, env vars, paths.

Las API keys se leen desde .env (gitignored). El catalogo de modelos vive
en benchmarks/models.py (separado para evitar mezclar metadata publica
con configuracion de runtime).

Setup:
1. cp .env.example .env
2. Editar .env con tus API keys reales (al menos OPENROUTER_API_KEY)
3. Listo, este archivo no necesita edicion local
"""
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass  # si dotenv no esta instalado, se leen las env vars directo

# Catalogo de modelos (publico, en benchmarks/models.py).
# Import flexible: funciona si se importa como `benchmarks.config` (desde la
# raiz del repo, ej. python benchmarks/runner.py) o como `config` (con
# benchmarks/ ya en sys.path, ej. los generators internos).
try:
    from benchmarks.models import MODELS, OLLAMA_MODELS
except ImportError:
    from models import MODELS, OLLAMA_MODELS

# ====== Configuracion del runner ======
RUNS_PER_TEST = 3
REQUEST_TIMEOUT = 300  # segundos. signal.alarm como backup del timeout httpx
RESULTS_DIR = "benchmarks/results"

# ====== Toggle providers (desde .env) ======
# INCLUDE_OLLAMA=true en .env activa el provider Ollama local (puerto 11434)
INCLUDE_OLLAMA = os.getenv("INCLUDE_OLLAMA", "false").lower() == "true"

# ====== API keys (desde .env) ======
# Cada provider se autodesactiva si su key esta vacia (ver runner.py)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY", "")
MINIMAX_BASE_URL = os.getenv("MINIMAX_BASE_URL", "https://api.minimax.io/v1")

OLLAMA_CLOUD_API_KEY = os.getenv("OLLAMA_CLOUD_API_KEY", "")
OLLAMA_CLOUD_BASE_URL = os.getenv("OLLAMA_CLOUD_BASE_URL", "https://ollama.com/v1")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")

# NVIDIA NIM cloud (40 RPM gratis)
NVIDIA_NIM_API_KEY = os.getenv("NVIDIA_NIM_API_KEY", "")
NVIDIA_NIM_BASE_URL = os.getenv("NVIDIA_NIM_BASE_URL", "https://integrate.api.nvidia.com/v1")

# Xiaomi MiMo Token Plan (suscripcion mensual)
XIAOMI_API_KEY = os.getenv("XIAOMI_API_KEY", "")
XIAOMI_BASE_URL = os.getenv("XIAOMI_BASE_URL", "https://token-plan-sgp.xiaomimimo.com/v1")

# NVIDIA NIM Local (containers en DGX Spark / GPU propio)
# Default vacio = desactivado. Ej: http://localhost:8000/v1 o http://<ip-dgx>:8000/v1
NIM_LOCAL_BASE_URL = os.getenv("NIM_LOCAL_BASE_URL", "")
