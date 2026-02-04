# Primer Proyecto de Programacion CC1 - Estudio Musical "Botaos Gang"

## Requisitos

- Python 3.10+
- `customtkinter`
- `pillow`

Instalar dependencias:

```bash
python -m pip install customtkinter pillow
```

## Ejecutar

```bash
python gui.py
```

## Estructura principal

- `gui.py` — interfaz; arranca la app y contiene la mayor parte de la interacción con el usuario.
- `classes.py` — modelos (EVENTOS, SALAS, EQUIPOS) y funciones auxiliares (p. ej. `meses()`, carga de `eventos.json`).
- `validation.py` — reglas de negocio: validación de horarios, recursos, solapamientos y búsqueda de huecos.
- `eventos.json` — persistencia: lista de eventos guardados (edítalo con cuidado; el formato es una lista JSON de eventos).
- `Images/` — imágenes usadas por la interfaz.

> Nota: en el README uso `backticks` para resaltar nombres de archivos y comandos. También puedes abrir los archivos enlazados directamente desde el repositorio si tu editor lo soporta.