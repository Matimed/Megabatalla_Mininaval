
# Megabatalla Mininaval

¡Bienvenido a Megabatalla Mininaval! Esta es nuestra primer aplicación creada con Pygame para un proyecto escolar. En este juego, podrás disfrutar de batallas navales con un toque único, donde los barcos son más pequeños y la diversión es gigantesca.

## Características

- Juego multijugador local.
- Personaliza el tamaño del tablero según tus preferencias (máximo de 26x26).
- Decide la cantidad de barcos con los que deseas jugar.
- Interfaz de usuario sencilla y amigable.

## Cómo Jugar

1. Clona este repositorio en tu máquina local.

```bash
git clone https://github.com/Matimed/Megabatalla_Mininaval
```

2.  Ejecuta el juego.

```bash
./run.sh
```

El script crea el entorno virtual (`venv/`) e instala las dependencias la
primera vez, así que no hace falta instalarlas a mano. Si preferís usar tu
propio entorno, también podés ejecutarlo directamente:

```bash
python MegabatallaMininaval.py
```

4.  Personaliza el tamaño del tablero y la cantidad de barcos en el menú de configuración.
    
5.  Invita a un amigo para jugar una emocionante partida de batalla naval en versión mini.
    
6.  ¡Diviértete hundiendo los barcos de tu oponente!


## Jugar en el navegador

El juego también corre en el navegador, compilado a WebAssembly con
[pygbag](https://pygame-web.github.io/) (CPython + SDL2 sobre wasm, sin
reescribir el juego).

```bash
./run_web.sh
```

Después abrí <http://localhost:8000> y hacé click en la pantalla para
arrancar (los navegadores exigen una interacción del usuario antes de
habilitar el audio).

El script compila y levanta un servidor de prueba. Para generar solo los
archivos estáticos, que quedan en `build/web/`:

```bash
./run_web.sh --build
```

Ese directorio es autocontenido (`index.html` + el `.apk` con el juego) y
se puede publicar en cualquier hosting estático: GitHub Pages, Netlify,
itch.io, etc. **No** se puede abrir el `index.html` con `file://`, siempre
tiene que servirse por HTTP.

### Notas de la versión web

- El punto de entrada web es `main.py` (nombre obligatorio para pygbag) y
  usa un bucle asincrónico: en el navegador el bucle principal tiene que
  cederle el control a la pestaña en cada frame con `await`.
  `MegabatallaMininaval.py` sigue siendo la entrada de escritorio.
- Todo el audio está en formato OGG Vorbis: pygbag rechaza MP3 y WAV.
- El botón **Salir** vuelve al menú principal en vez de cerrar el juego,
  porque en el navegador cerrarlo solo deja el canvas congelado. En
  escritorio sigue cerrando; la diferencia se decide en
  `src/controller/controlador_eventos.py` mirando `sys.platform`.
- La pantalla de carga sale de `web/template.tmpl`, una copia del template
  por defecto de pygbag con el splash del juego. La fuente y el sprite del
  barco van embebidos en base64, así que no hace falta servir nada aparte.
- `pygbag.ini` lista lo que no debe entrar en el `.apk` (la carpeta `web/`
  y los scripts de arranque).


## Requisitos

 * Python3
 * Mira el resto de dependencias en los [requirements](requirements.txt)

## Autores

-   **Arcos Juan**  -  [ArcosJuan](https://github.com/ArcosJuan).
-   **Carazo Medley Matías**  -  [Matimed](https://github.com/Matimed).

## Licencia

Este proyecto se encuentra bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

¡Esperamos que disfrutes de Megabatalla Mininaval y que hundas muchos barcos!