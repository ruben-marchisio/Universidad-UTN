# Comandos básicos en la terminal (Git Bash, Ubuntu, Mac)

Abrimos la terminal de Git Bash en Windows, o la terminal de Ubuntu o Mac, y comenzamos con los siguientes comandos y creación de directorios.<br><br>

---

## Navegación y comandos básicos

`pwd`  → Vemos la ruta de la carpeta en la que estamos<br>
`cd`  → Navegar a una carpeta: *change directory*<br>
`cd /`  → Nos lleva al home, en la raíz del disco<br>
`cd ~`  → La virgulilla (~) significa que estamos en la carpeta del usuario<br>
`ls`  → Lista los archivos en la ruta actual<br>
`ls -al`  → Muestra todos los archivos, incluyendo los ocultos<br>
`ls -l`  → Lista los archivos en formato detallado (sin ocultos)<br>
`ls -a`  → Muestra todos los archivos, pero no en lista detallada<br>
`clear`  → Limpia la consola (también Ctrl + L)<br>
`cd ..`  → Regresa a la carpeta anterior<br>
`cd U` + `TAB`  → Autocompleta una ruta o nombre de carpeta<br>
`cd /D`  → Cambiamos de disco (solo en Windows)<br>
`df -h`  → Muestra el uso de disco en Ubuntu<br>
`cd /mnt/d`  → Cambia de directorio usando WSL Ubuntu en Windows<br><br>

---

## Creación de carpetas

`cd ..`<br>
`cd ..`<br>
`cd /mnt/c`<br>
`cd ~`  → Volvemos a la carpeta raíz del usuario<br><br>

`mkdir Tecnicatura`  → En Windows las mayúsculas no importan, pero en Linux sí<br>
`cd tecnicatura`<br>
`mkdir Python`<br>
`mkdir Java`<br>
`mkdir JavaScript`<br><br>

> **Nota:** Revisar y ejecutar cada comando como práctica.<br><br>

**Profesor:** Ariel Betancud

# Clase 2 - Terminal y Git

Abrir Git Bash en Windows o la terminal de Linux o Mac.  
> Al abrir Git Bash, hacerlo **como administrador**.<br><br>

---

## Comandos básicos de archivos

`touch vacio.txt` → Crea un archivo con su extensión: **ESCRIBIR DENTRO**<br>
`Ctrl + S` → Guardamos lo que escribimos en el archivo<br>
`./` → Significa la carpeta actual<br>
`../` → Significa la carpeta anterior<br>
`cat vacio.txt` → Vemos el contenido del archivo<br>
`history` → Veremos la historia completa de los comandos utilizados<br>
`!72` + `Enter` → Ejecuta el comando número 72 del historial<br>
`rm vacio.txt` → Borra el archivo seleccionado (**¡CUIDADO!**)<br>
`rm --help` → Muestra cómo funciona el comando `rm`<br><br>

---

## Crear un repositorio de Git y hacer el primer commit

`cd tecnicatura`<br>
`mkdir class-git`<br>
`cd class-git` → Entramos en la carpeta que necesitamos trabajar<br>
`git init` → Creamos un repositorio en la carpeta, se crea el archivo oculto `.git`<br>
`code .` → Abrimos Visual Studio Code en la carpeta actual<br>
`Ctrl + N` → Creamos un archivo nuevo y escribimos en él<br>
`Ctrl + S` → Guardamos con el nombre `historia.txt`<br>
`git status` → Vemos el estado del proyecto en tiempo real<br>
`git add historia.txt` → Enviamos el archivo al área de preparación<br>
`git status` → Verificamos que el archivo está listo para el commit<br>
`git rm --cached historia.txt` → Quitamos el archivo del área de preparación (estaba en RAM)<br><br>

---

## Configurar Git

`git config` → Lista general de configuraciones disponibles<br>
`git config --list` → Muestra las configuraciones por defecto<br>
`git config --list --show-origin` → Muestra de dónde vienen las configuraciones<br>
`git config --global user.name "Ariel Betancud"`<br>
`git config --global user.email "betancudariel@gmail.com"` → Este correo debe ser el mismo que se usará en GitHub<br>
`git config --list` → Ahora veremos todos los datos correctamente configurados<br><br>

---

## Primeros commits

`git add .` → Agrega todos los archivos al área de preparación<br>
`git commit -m "Mensaje importante del commit"` → Se realiza el primer commit<br>
`code .` → Hacemos cambios en el archivo y guardamos<br>
`git status` → Verifica los cambios que están listos para un nuevo commit<br>
`git add .`<br>
`git commit -m "Mi segundo commit"`<br><br>

---

## Ver historial

`git log historia.txt` → Vemos toda la historia del archivo `historia.txt`.  
> El número largo que aparece es el **hash** del commit.<br><br>

---

> **Revisar y ejecutar cada comando, hacerlo como práctica.**<br><br>

**Profesor:** Ariel Betancud

# Clase 3 - Analizar cambios en archivos de Git

Analizar cambios en los archivos de tu proyecto Git - Parte 3<br><br>

---

## Ingreso y preparación

Abrir Git Bash en Windows o la terminal de Linux o Mac.  
> Al abrir Git Bash, hacerlo como **administrador**. En terminal de Linux, usar `sudo` para permisos especiales.<br><br>

---

## Navegación y eliminación de archivos

`cd tecnicaturagit` → Ingresamos al directorio donde están nuestras carpetas de trabajo<br>
`ls` → Vemos los archivos y directorios existentes<br>
`cd git` → Entramos (en este ejemplo, no hay nada)<br>
`cd ..` → Salimos de la carpeta<br>
`rm historia.txt` → Eliminamos el archivo anterior (solo práctica)<br>
`rm Git` → Error esperado: *rm: cannot remove 'Git': Is a directory*<br>
`rm --recursive -R Git` → Elimina el directorio y su contenido<br>
> *By default, rm does not remove directories. Use the --recursive (-r or -R) arguments to remove each listed directory, too, along with all of its contents.*<br>
`rm --help` → Muestra documentación del comando `rm`<br><br>

---

## Crear nuevo repositorio local

`mkdir class-git` → Creamos una nueva carpeta para trabajar<br>
`cd class-git` → Entramos a la carpeta<br>
`touch README.md` → Creamos un archivo nuevo en formato Markdown<br>
> `.md` significa *markdown*, un lenguaje que permite transformar texto plano a HTML. Puede trabajarse con editores como Visual Studio Code.<br><br>

---

## Documentación y edición

Leemos la [documentación de Markdown en GitHub](https://docs.github.com/es/get-started/writing-on-github) para escribir correctamente el `README.md`.<br>
`code .` → Abrimos Visual Studio Code para editar el archivo<br><br>

Empezamos a cargar lo aprendido en las clases anteriores dentro del archivo `README.md`.<br><br>

---

## Control de versiones con Git

`git status`<br>
`git add .`<br>
`git status`<br>
`git commit -m "Cargamos el README dentro del directorio class-git"`<br>
`git status`<br>
`git log` → Para ver el historial de commits<br>
> Si tenés commits de clases anteriores, verás más registros que en este ejemplo.<br><br>

`cd ..`<br>
`cd ..`<br><br>

---

> **Revisar y ejecutar cada comando, hacerlo como práctica.**<br><br>

**Profesor:** Ariel Betancud




# Clase 4 - Analizar cambios en los archivos de Git (Parte 4)

Ingresamos de la siguiente manera:<br><br>

Abrir Git Bash en Windows o la terminal de Linux o Mac.  
> Al abrir Git Bash, hacerlo como **administrador**. En terminal de Linux, usar `sudo` para permisos especiales.<br><br>

---

## Navegación al directorio de trabajo

`cd tecnicatura` → Entramos a la carpeta principal del proyecto<br>
`cd class-git` → Entramos al directorio donde trabajamos con Git<br>
`ls` → Listamos el contenido de la carpeta actual<br><br>

---

## Crear y editar archivo

`touch historia.txt` → Creamos un nuevo archivo vacío llamado `historia.txt`<br>
`code .` → Abrimos Visual Studio Code en la carpeta actual<br><br>

> **Modificar dentro de `historia.txt`**:<br>
Escribir:  
`Bienvenido     mi nombre es` (Ruben marchisio)<br>

`Ctrl + S` → Guardamos los cambios<br><br>

---

## Guardar los cambios con Git

`git status` → Verificamos qué archivos han sido modificados<br>
`git add .` → Añadimos todos los archivos modificados al área de preparación<br>
`git status` → Confirmamos que están listos para commitear<br>

`git commit` → Sin `-m`, se abre un editor para escribir el mensaje del commit<br><br>

### Para guardar el mensaje en el editor Vim (Git Bash - Windows):

1. `Esc` → Salimos del modo de escritura  
2. `:wq!` + `Enter` → Guardamos y salimos<br>

### Alternativa en algunas terminales de Linux:

- `Esc` + `Shift + Z + Z` → Guardamos y salimos<br><br>

---

## Agregar más cambios

Agregar otra línea en `historia.txt`:  
`Estoy estudiando programación`<br>

`Ctrl + S` → Guardamos<br>
`git add .` → Preparamos los cambios<br>
`git commit` → Se abre nuevamente el editor Vim<br><br>

### En Vim (si es necesario):

- `Esc` + `i` → Para escribir el mensaje del commit  
- `Ctrl + X` → Para salir (Linux, en algunos casos)  
- `s` + `Enter` → Confirmamos con "sí" (también puede ser `y` para "yes")<br><br>

---

## Visualizar historial y diferencias

`git show` → Muestra los detalles del último commit<br>
`git log historia.txt` → Lista todos los commits realizados sobre `historia.txt`<br>
`q` → Salimos del log de commits<br><br>

### Comparar versiones

1. Copiar un hash antiguo y otro más reciente del log<br>
2. Ejecutar:<br>
`git diff hash_antiguo hash_reciente` → Compara ambos commits y muestra sus diferencias<br>
3. `q` → Para salir<br><br>

---

## Salir del proyecto

`cd ..`<br>
`cd ..`<br><br>

---

## Tarea

Agregar esta clase al archivo `README.md` usando lenguaje Markdown, como en la clase anterior.  
Luego hacer el commit correspondiente al cambio agregado.<br><br>

> **Revisar y ejecutar cada comando, hacerlo como práctica.**<br><br>

**Profesor:** Ariel Betancud


# Clase 5: ¿Qué es el staging?

Cuando trabajamos en un proyecto, tenemos una carpeta o directorio con los archivos, por ejemplo, `historia.txt`. Al ejecutar `git init` en la consola, se crea un área en la memoria RAM llamada **staging** y un repositorio, que es la carpeta `.git` donde se almacenan todos los cambios del proyecto.

### Flujo de trabajo:
1. **Área de trabajo**: Donde editamos los archivos.
2. **Staging (área de preparación)**: Al usar `git add historia.txt`, los cambios pasan al staging, que está en la memoria RAM.
3. **Repositorio**: Con `git commit -m "Mensaje"`, los cambios se guardan en la rama `master` del repositorio, generando un **hash** (identificador único del commit con letras y números).

---

# ¿Qué es Gitflow?

**Gitflow** es un modelo alternativo para gestionar ramas en Git, propuesto por Vincent Driessen. Utiliza ramas de función y varias ramas principales para organizar el desarrollo.

---

# ¿Qué es una rama (branch) y cómo funciona un merge en Git?

- **Rama (branch)**: La rama principal, llamada `master`, contiene los cambios estables de los archivos. Cada `commit` crea una nueva versión.
- **Ramas adicionales**:
  - **Development**: Rama experimental para nuevas versiones.
  - **Hotfix**: Rama para corregir errores urgentes (bugs).
- **Merge**: Proceso de unir los cambios de una rama (como `development` o `hotfix`) a la rama `master` cuando los resultados son satisfactorios.

### Características de las ramas principales:
- Solo existe una rama de cada tipo (`master`, `develop`).
- No reciben código directamente mediante commits; siempre se integran a través de ramas auxiliares (`Feature`, `Release`, `Hotfix`).
- Recibir código directamente en `master` es arriesgado, ya que puede introducir defectos en producción. Por eso, se integran cambios primero en otras ramas.

Gitflow es una metodología estricta, pero puede adaptarse según el equipo. En casos excepcionales, expertos pueden omitir algunas normas, pero siempre con precaución.

---

# Ramas auxiliares

1. **Feature**: Para desarrollar nuevas características, requisitos o historias de usuario. Se crean tantas como sea necesario.
2. **Release**: Para estandarizar o depurar código desarrollado en `develop` antes de integrarlo a `master`.
3. **Hotfix**: Para corregir defectos críticos en producción, generando una release puntual.

Estas ramas tienen un ciclo de vida definido: se crean, se mergean con `master` o `develop`, y luego se eliminan.

---

# Consideraciones importantes

- Podemos crear tantas ramas y repositorios como necesitemos.
- Es crucial gestionar bien los **merges**, ya que pueden surgir **conflictos** o **bugs** si los archivos interfieren entre sí.

---

# Resumen

Hoy fue una sesión teórica, repasando los conceptos de Git y Gitflow explicados por la profesora Naty.

**Profesor: Ariel Betancud**
