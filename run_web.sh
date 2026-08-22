#!/usr/bin/env bash
# Compila Megabatalla Mininaval a WebAssembly con pygbag y lo sirve
# en http://localhost:8000
#
#   ./run_web.sh            compila y levanta el servidor de prueba
#   ./run_web.sh --build    solo compila (deja todo en build/web/)
#
# La primera vez crea el venv/, instala las dependencias y descarga
# el runtime de CPython+SDL2 compilado a wasm (~30 MB, queda cacheado).

set -e

cd "$(dirname "$0")"

VENV="venv"
SELLO="$VENV/.requirements-web.sha1"

if [ ! -x "$VENV/bin/python" ]; then
    echo "Creando el entorno virtual en $VENV/ ..."
    python3 -m venv "$VENV"
fi

HASH="$(cat requirements.txt requirements-web.txt | sha1sum | cut -d ' ' -f 1)"
if [ "$(cat "$SELLO" 2>/dev/null)" != "$HASH" ]; then
    echo "Instalando dependencias..."
    "$VENV/bin/python" -m pip install --quiet \
        --requirement requirements.txt \
        --requirement requirements-web.txt
    echo "$HASH" > "$SELLO"
fi

exec "$VENV/bin/python" -m pygbag \
    --width 960 --height 540 \
    --app_name MegabatallaMininaval \
    --title "Megabatalla Mininaval" \
    --icon resources/graphics/icono.png \
    --port 8000 \
    "$@" main.py
