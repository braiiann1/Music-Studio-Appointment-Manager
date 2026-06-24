# Primer Proyecto de Programación CC1 - Estudio Musical 'Botaos Gang' 🎶

[![python-version](https://img.shields.io/badge/python-3.10%2B-blue)](#)
[![license](https://img.shields.io/badge/license-MIT-lightgrey)](#)

Mi proyecto consiste de una aplicación de escritorio hecha en el lenguaje **Python** usando como interfaz gráfica **customtkinter**, pensada para gestionar y reservar sesiones de grabación en un estudio musical: crear turnos, asignar sala, comprobar precios, seleccionar equipos necesarios y validar conflictos de horario y/o inventario.

## Instalación ⚙️

Requisitos mínimos de instalacion:

- Python 3.10 o una version superior
- pip

Se recomienda crear y usar un entorno virtual para de esta forma asegurar que las dependencias no entren en conflicto con otras instalaciones actuales del sistema. Con este proyecto incluye un `requirements.txt` en la raíz, el cual funciona para instalar todo lo necesario para la ejecucion correcta.

Pasos (Linux / macOS):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
# Si prefieres instalar manualmente:
# pip install customtkinter Pillow
```

Pasos (Windows - PowerShell):

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
pip install -r requirements.txt
# o: pip install customtkinter Pillow
```

Ejecución rápida (una vez instalado):

```bash
python gui.py
```

Caputa de muestra de la pantalla principal:
![Captura del gestor](./Images/Readme_img/image.png "Vista del gestor de turnos")

## Dominio escogido y por qué

Escogí el dominio de gestión de un estudio musical por razones personales y prácticas. La música para mi ha sido siempre una de mis formas de expresión artistica favorita, y diseñar una herramienta que facilite la organización de sesiones nace a partir de una necesidad real de coordinar tiempos, espacios y equipos cuando trabajas con músicos, técnicos y productores.

Además, este dominio ofrece reglas de negocio interesantes (dependencias de equipos, compatibilidades, superposición de horarios, precios) que lo hacen un buen ejercicio para aprender a modelar restricciones en software real ante un dominio objetivo. Me permitió practicar diseño de interfaces, validación de datos y persistencia simple con archivos JSON.

## Funciones principales ✨

La aplicación incluye las siguientes funcionalidades diseñadas para cubrir las necesidades básicas de gestión de un estudio musical a la hora de verificar una reserva de turno solicitado por el cliente:

- Añadir evento: al pulsar el botón de Añadir **+** se abre un formulario donde el usuario define el nombre del evento, la sala, la franja horaria, el inventario requerido y las fechas. Al confirmar, los datos se validan con el script `validation.py` para evitar conflictos y entradas inválidas.
- Editar evento: al pulsar el botón **Editar** se despliega una columna con un icono de bote de basura, el cual funciona como el boton encargado de eliminar el evento especifico de su columna, la idea para esta implementacion surge de programas como la alarma del movil, o Whatsapp.
- Eliminar evento: como se explica anteriormente, dentro del modo edicion el usuario tiene la opcion de borrar un turno de la lista, es decir la funcion de "Eliminar evento" se encuentra implicta en la funcion de "Editar".
- Lista de Eventos: La pantalla principal muestra, a través de una vista desplazable, los eventos actuales del programa en orden (el más reciente arriba).
- Boton de informacion: cada evento dispone de un boton **i** que al pulsarlo despliega una vista detallada que muestra descripción, sala, inventario, fechas y un cálculo estimado del coste.
- Gestión de dependencias y exclusiones: al crear o editar un evento, el sistema comprueba si existen dependencias (por ejemplo, un micrófono que requiere cierta interfaz) o exclusiones entre recursos, bloqueando la reserva si hay conflictos.

Estas funcionalidades están pensadas para ser intuitivas y reducir al mínimo el número de pasos necesarios para reservar una sesión de grabacion. Como es facil de notar, se diseño con la idea de que cada funcion se encuentre integrada dentro de la otra siempre y cuando resulte conveniente, en vez de optar por un boton para cada funcion, lo cual lo hace inconsistente (es molesto tener un boton para desplegar la lista de eventos, y otro de eliminar el cual tambien abrira la lista para decidir el evento a eliminar, por esto es mejor incluir la funcion de eliminar, informacion, directamente sobre la lista de eventos de forma implicita y de esta forma minorizar en la medida de lo posible la carga para el usuario)

## Estética y diseño (inspirado en Material UI) 🎨

La apariencia del programa busca un equilibrio entre el minimalismo y la funcionalidad a pesar de lo simple que resulta la mayoria de aplicaciones desarrolladas con la libreria escogida. Algunas decisiones de diseño relevantes tomadas:

- Colores: paleta con un color primario oscuro (para la cabecera y fondos de panel), un color secundario para acciones destacadas y acentos en tonos cálidos para botones de estado. Se prioriza un contraste alto para legibilidad y se contempla una variante en modo oscuro.
- Tipografía: uso de una fuente clara y consistente (Roboto) con tamaños y espaciado constantes.
- Elevación y tarjetas: los elementos de lista (turnos) se presentan como tarjetas con sombreado suave (elevación) y bordes ligeramente redondeados para separar visualmente bloques sin recargar la pantalla, mostrados en forma de grid (filas x columnas).
- Espaciado: sistema de rejilla y márgenes basados en unidades consistentes (8px / 16px) para alinear controles, etiquetas y botones, simplificando asi la forma de mostrar la informacion partiendo del backend.
- Iconografía y botones: iconos claros para acciones principales (añadir, eliminar, info). El botón flotante (FAB) o el botón con icono "+" se utiliza para añadir eventos y destaca con color secundario separandose asi de la cabecera.
- Menús y navegación: barra superior (AppBar) con título y acciones primarias a la derecha; filtros y opciones en menús desplegables o en un navigation drawer lateral cuando sea necesario.
- Accesibilidad: colores con contraste suficiente, foco visible en controles y etiquetas claras para lectores de pantalla.

## Dependencias y exclusiones 🔗

A la hora de crear un evento, el sistema comprueba a traves de `validation.py` las dependencias entre equipos o dependencia equipo-sala (por ejemplo, una guitarra electrica requieren de un amplificador, la acustica de la sala B es requerida para la grabacion de un Album). Si falla alguna de las dependencias, la reserva se rechaza y se le muestra al usuario un mensaje que indica qué recurso es necesario reservar para realizar la sesion.

También existen recursos incompatibles entre sí o con determinadas salas; en esos casos la operación de confirmacion se cancela y se le informa al usuario. En las siguiente graficas son visibles, para facilidad del usuario, los dependientes y excluyentes de forma respectiva.

![Dependencias](./Images/Readme_img/dependencias.png "Dependencias (recurso requerido)")

![Exclusiones](./Images/Readme_img/excluyentes.png "Recursos incompatibles")

Esta implementado a su vez una **resource pool**, por lo que el estudio presenta una cantidad definida de recursos a su disposicion, una vez que en un mismo rango de horario entre turnos esten agendados todos los recursos de un mismo tipo, no se le permitira al usuario agendar el evento, por un problema de insuficiencia.

A continuacion en forma de lista se muestran el nombre de los objetos en funcion de su cantidad:

- *Microfono Profesional*: 10
- *Guitarra Fender Stratocaster*: 1
- *Bateria Acustica Yamaha*: 2
- *Bajo Fender American Vintage*: 1
- *Sintetizador 808*: 1
- *Monitores de Audio Profesional*: 3
- *Tarjeta de Sonido*: 4
- *Antares Autotune*: 1
- *Microfono para bateria*: 2
- *Amplificador Fender*: 2
- *Guitarra Fender Telecaster*: 2


## Estructura de datos (formato de evento) 🧾

Un evento se representa internamente, tanto en el codigo como en el archivo `json` como una lista con la siguiente forma (orden fijo):

```text
[ nombre_evento, nombre_sala, (hora_inicio, hora_fin), [inventario...], (dia_inicio, dia_fin), mes, año ]
```

Tipos y ejemplo:
- `nombre_evento`: string
- `nombre_sala`: string
- `hora_inicio`, `hora_fin`: strings, de formato "HH:MM"
- `inventario`: lista de strings con los nombres de los equipos
- `(dia_inicio`, `dia_fin)`: tupla de strings representando enteros
- `mes`, `año`: strings representando enteros

Internamente el formato es intencionalmente simple para facilitar lectura y edición manual de los archivos JSON que contienen los turnos. Esta simplicidad facilita probar diferentes escenarios sin herramientas complejas.

Ejemplo real de un evento (En formato JSON):

```json
["Grabacion de mixtape", "Sala A - Singular", ["18:00", "21:00"], ["Batería", "Micrófono Profesional", "Tarjeta de Sonido"], ["12", "12"], "10", "2024"]
```

Si se desea migrar a una estructura de persistencia de datos más robusta (diccionarios con claves o una base de datos pequeña como SQLite), es un cambio directo el cual puede ser añadido en futuras versiones del programa.

## Lo aprendido en el proceso

Trabajar en este proyecto fue una experiencia muy formativa. Fue mi primer acercamiento serio al desarrollo de una aplicacion de escritorio con interfaz gráfica de usuario, y aprendí varias lecciones técnicas durante el proceso:

- Manejo de tiempo y fechas: `datetime` y la representación de franjas horarias plantearon retos sobre validación y normalización de formatos. Tambien aprendí a manejar objetos de tiempo para comparar horarios y detectar superposiciones.
- Manipulación de imágenes en GUI: `PIL`/`Pillow` para cargar y mostrar imágenes al usuario de forma optima en distintos sistemas operativos. 
- Persistencia sencilla con `json`: Fue mi primera vez trabajando con una libreria destinada para la persistencia de datos de un programa, me decidi por `json` pues luego de una investigacion de mi partesuficiente para prototipos y para entender cómo modelar datos sin la complejidad de una base de datos mas avanzada para el nivel.
- Control de versiones con Git/GitHub: Tambien fue mi primera practica a la hora de trabajar con un programa de control de versiones, apoyandome de herramientas como los repositorios, los commits e issues siendo una plataforma util a nivel de development, llegando a facilitar el volver atrás cuando algo falla y de documentar el proceso de desarrollo y evolucion del proyecto. (Perdon de antemano por el nombre de los commits tempranos, todavia no estaba planteado que se revisarian :3)

También hubo aprendizajes no tan técnicos: priorizar UX en pequeñas decisiones mejora mucho la experiencia del usuario y reduce el soporte necesario. Fijarme en detalles como el contraste de colores y la legibilidad ayudó a que la aplicación se sienta cuidada.

## Dificultades y desafíos encontrados

Algunas de las dificultades con las que me encontre durante el desarrollo:

- Durante una fase temprana de desarrollo, se habia escogido para la interfaz grafica `tkinter`, pero luego de un choque frente a las limitaciones y restricciones de la libreria ante la idea y ambicion original me decidi optar por `customtkinter` (abreviado ctk), el cual funcion como una capa la cual le otorga a la biblioteca original de tkinter una mayor capacidad de personalizacion en aspectos como la fuente, estilo, seleccion color, funcionalidad de objetos, y una integracion mas limpia con el Sistema Operativo ya sea Windows o Linux. La experiencia fue positiva ante este cambio.
- Validación de inconsistencia: diseñar reglas que detecten superposiciones de horario, inventario no disponible o conflictos entre dependencias fue el reto más técnico con el que me enfrente. Escribir un comportamiento algoritmico especifico para cada condicion de fallo posible que rompiera el programa fue un trabajo de razonamiento logico muy exhausto y agotador el cual requirio de muchas pruebas para asegurar que no se escapara ningún caso durante la validacion de los eventos. 
- Rendimiento: En fase de desarollo temprana, la escalabilidad de los datos y la eficiencia del programa ante esta fue un factor de mucha importancia durante el tiempo de desarrollo pues para mi era esencial la capacidad de manejar una cantidad de datos superior a lo esperado en condiciones cotidianas de uso, al principio, encontre dificultades para esto debido a un algoritmo ineficiente por parte de la funcion de renderizacion por parte del customtkinter grid a la hora de renderizar la lista principal de turnos, el gestor era incapaz de procesar con estabilidad +10 turnos, tomando tiempos de cargas los cuales eran superiores al minuto o mas, pero luego de muchas arreglos, cambios, revisiones, y noches sin dormir, puedo asegurar que todo problema de eficiencia se encuentra actualmente resuelto :D.
- La situacion nacional: el simple hecho de tener que llevar este readme de las 713 palabras originales a las 2000, 6 meses luego de haber dado por finalizado el proyecto, sin servicio de electricidad y una conexion nula para asistirme por el Copilot, es de por si mismo un desafio. Pero espero que, luego de tanto esfuerzo, haya quedado lo mas comprensible posible. 

---

Quiero darle las gracias a mis dos gatos, a pepe, a sergio, y a jacob forever por el feedback durante el desarrollo, con amor, **Brayan Miguel Rivero Horta** <3.
