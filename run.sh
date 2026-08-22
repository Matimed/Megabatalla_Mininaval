#!/usr/bin/env bash
# Ejecuta Megabatalla Mininaval usando el entorno virtual del proyecto.
# La primera vez crea el venv/ e instala las dependencias automaticamente.

set -e

cd "$(dirname "$0")"

VENV="venv"
SELLO="$VENV/.requirements.sha1"

if [ ! -x "$VENV/bin/python" ]; then
    echo "Creando el entorno virtual en $VENV/ ..."
    python3 -m venv "$VENV"
fi

HASH="$(sha1sum requirements.txt | cut -d ' ' -f 1)"
if [ "$(cat "$SELLO" 2>/dev/null)" != "$HASH" ]; then
    echo "Instalando dependencias..."
    "$VENV/bin/python" -m pip install --quiet --requirement requirements.txt
    echo "$HASH" > "$SELLO"
fi

exec "$VENV/bin/python" MegabatallaMininaval.py "$@"
