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

## Clase 6 - Miércoles 14 de Mayo de 2025

## Volver en el tiempo en nuestro repositorio utilizando `reset` y `checkout` (Parte 6)

### Instrucciones iniciales
1. **Abrir Git Bash** en Windows *o* la **terminal** en Linux/Mac.  
2. En Git Bash, **abrir como administrador**.  
3. En terminal, usar `sudo` para permisos especiales si es necesario.

### Tarea
Agregar **comentarios explicativos** a cada comando para entender su función.

### Comandos y pasos
```bash
cd tecnicatura              # Cambia al directorio 'tecnicatura'
cd class-git                # Cambia al directorio 'class-git'
ls                          # Lista los archivos en el directorio actual
touch historia.txt          # Crea un archivo vacío llamado 'historia.txt'
cd ..                       # Retrocede al directorio superior
code .                      # Abre el proyecto en VS Code para editar 'historia.txt'

git commit -a               # Realiza un commit de todos los archivos modificados
# En el editor Vim:
#   Presionar 'Esc + i' para entrar en modo escritura
#   Presionar 'Esc' para salir del modo escritura
#   Escribir ':wq!' y Enter para guardar y salir

git log                     # Muestra el historial de commits
git show                    # Muestra los detalles del commit más reciente
git log --oneline           # Muestra el historial de commits en una sola línea por commit
# Copiar el hash corto del commit seleccionado

git reset <hash>            # Vuelve a una versión anterior del repositorio (reset suave por defecto)
git status                  # Verifica el estado del repositorio y muestra cambios pendientes
git add .                   # Agrega todos los cambios al staging
git commit -m "Agregamos datos de estudios en historia.txt"  # Crea un nuevo commit

git config --list           # Muestra la configuración de Git (nombre, email, etc.)
git log --oneline           # Muestra nuevamente el historial de commits
# Copiar el hash del commit deseado
git reset --hard <hash>     # Reset duro: restaura el repo al estado del commit y elimina cambios posteriores

# Crear, modificar y commitear nuevamente 'historia.txt', dejando cambios en staging
git reset --soft <hash>     # Reset suave: conserva cambios en staging
git diff                    # Muestra diferencias entre el working directory y el staging
git add .                   # Agrega todos los cambios al staging
git status                  # Verifica que los cambios están en staging
git commit -m "Commiteamos lo último de hoy"  # Crea un nuevo commit

git log                     # Muestra el historial de commits
# Hacer cambios en 'historia.txt', guardar con Ctrl + S
git diff                    # Muestra los cambios realizados
# Agregar más cambios a 'historia.txt'
git commit -am "cambio en la última línea del historia.txt"  # Agrega y commitea los cambios

git log                     # Muestra el historial de commits
# Presionar 'q' para salir
git log --stat              # Muestra estadísticas de cambios por commit (archivos modificados, bits)
# Presionar 'q' para salir
# Copiar el hash del primer commit
git checkout <hash>         # Cambia al estado del archivo en el commit especificado
git status                  # Verifica el estado actual del repositorio
git checkout master         # Vuelve a la rama principal (master)

git checkout <hash>         # Vuelve al estado del commit especificado
# Modificar 'historia.txt'
git commit -am "Reemplazo de una versión por otra de la historia"  # Commitea los cambios
git log                     # Muestra el historial actualizado

git branch cambios          # Crea una nueva rama llamada 'cambios'
git checkout master         # Vuelve a la rama principal

# CLASE 7 - Git reset vs. Git rm (Parte 7)

Los comandos **`git reset`** y **`git rm`** tienen utilidades muy diferentes, pero pueden confundirse fácilmente.

---

## GIT RESET

El comando `git reset` es una herramienta poderosa que te permite **deshacer o revertir cambios** en tu repositorio de Git. Lo puedes ejecutar de tres maneras diferentes, con las líneas de comando `--soft`, `--mixed` y `--hard`.

> Como `git checkout` nos deja ir, mirar, pasear y volver.  
> Con `git reset` volvemos al pasado sin la posibilidad de volver al futuro.  
> **Borramos la historia y la debemos sobreescribir. No hay vuelta atrás.**

Variaciones de Git Reset
git reset --soft
Borra el historial y los registros de Git de commits anteriores, pero guarda los cambios en Staging para aplicar las últimas actualizaciones a un nuevo commit.

git reset --hard
Deshace todo, absolutamente todo. Toda la información de los commits y del área de staging se elimina del historial.

git reset --mixed
Borra todo, exactamente todo. Toda la información de los commits y del área de staging se elimina del historial.

git reset HEAD
El comando git reset saca archivos del área de staging sin borrarlos ni realizar otras acciones. Esto impide que los últimos cambios en estos archivos se envíen al último commit. Podemos incluirlos de nuevo en staging con git add si cambiamos de opinión.

---
## GIT RM
GIT RM
Por otro lado, es un comando que nos ayuda a eliminar archivos de Git sin eliminar su historial del sistema de versiones.
Para recuperar el archivo eliminado, necesitamos retroceder en la historia del proyecto, recuperar el último commit y obtener la última confirmación antes de la eliminación del archivo.

Es importante tener en cuenta que git rm no puede usarse sin evaluarlo antes.
Debemos usar uno de los flags siguientes para indicarle a Git cómo eliminar los archivos que ya no necesitamos en la última versión del proyecto.

Variaciones de Git rm
git rm --cached
Elimina archivos del repositorio local y del área de staging, pero los mantiene en el disco duro.
Deja de trackear el historial de cambios de estos archivos, por lo que quedan en estado untracked, que significa que un archivo no está siendo rastreado por Git.

git rm --force
Elimina los archivos de Git y del disco duro.
Git guarda todo, por lo que podemos recuperar archivos eliminados si es necesario (empleando comandos avanzados).
¡Al usar git rm lo que haremos será eliminar este archivo completamente de git!

¿Cuál es la diferencia entre git rm y git reset HEAD?
La diferencia principal entre git rm y git reset HEAD radica en que
git rm elimina archivos del repositorio y de la historia del proyecto,
mientras que git reset saca los cambios del área de preparación y los mueve del espacio de trabajo, sin afectar la historia del repositorio.

Es importante tener en cuenta el efecto que cada comando tiene en el proyecto y usarlos según tus necesidades y objetivos específicos.

¿Cuándo utilizar git reset en lugar de git revert?
Para reescribir la historia del repositorio y eliminar confirmaciones anteriores, se utiliza git reset.
Para deshacer cambios de confirmaciones anteriores de forma segura sin modificar la historia del repositorio, se emplea git revert.

Resumen
Para evitar problemas en el trabajo, es valioso entender las implicaciones y riesgos de cada comando y elegir el enfoque adecuado según las necesidades y el flujo de trabajo del proyecto.

Con git rm eliminamos un archivo de Git, pero mantenemos su historial de cambios.
Si no queremos borrar un archivo, sino dejarlo como está y actualizarlo después, no debemos usar este comando en este commit.

Empleando git reset HEAD, movemos los cambios de Staging a Unstaged, pero mantenemos el archivo en el repositorio con los últimos cambios en los que hicimos commit.
Así, no perdemos nada relevante.


---

## **Práctica guiada**

1. **Abrir git bash en Windows, terminal de Linux o Mac**  
   - Al abrir Git Bash hacerlo como administrador, en terminal también o usar `sudo` para permisos especiales.

2. **TAREA → AGREGAR LOS COMENTARIOS EN LOS COMANDOS, PARA SABER QUÉ PASA CON CADA UNO.**

3. **Hacer pruebas:**

```bash
cd tecnicatura            # Vamos a hacer pruebas, es por esto que creamos una carpeta nueva
cd practicas              # Entramos en la carpeta

touch reset_file.txt      # Agregar información y hacer uno a dos commits

git add reset_file.txt    # Agregamos el archivo al área de staging

git add .                 # Agregamos todos los archivos del directorio actual

git commit -m "Iniciando el primer commit"  # Confirmamos los cambios (primer commit)

# CLASE 8 - MIÉRCOLES 28 DE MAYO DEL 2025  
## Portafolio 2  
### Flujo de trabajo básico con un repositorio remoto (parte 8)

---

Cuando empiezas a trabajar en un entorno local, el proyecto vive únicamente en tu computadora. Esto significa que no hay forma de que otros miembros del equipo trabajen en él.

Para solucionar esto, utilizamos los **servidores remotos**: un nuevo estado que deben seguir nuestros archivos para conectarse y trabajar con equipos de cualquier parte del mundo.

Estos servidores remotos pueden estar alojados en **GitHub**, **GitLab**, **BitBucket**, entre otros. Lo que van a hacer es guardar el mismo repositorio que tienes en tu computadora y darnos una URL con la que todos podremos acceder a los archivos del proyecto. Así, el equipo podrá descargarlos, hacer cambios y volverlos a enviar al servidor remoto para que otras personas vean los cambios, comparen sus versiones y creen nuevas propuestas para el proyecto.

Esto significa que debes aprender algunos nuevos comandos:

---

## Comandos para trabajo remoto con GIT

- `git clone url_del_servidor_remoto`  
  Nos permite descargar los archivos de la última versión de la rama principal y todo el historial de cambios en la carpeta `.git`

- `git push`  
  Luego de hacer `git add` y `git commit` debemos ejecutar este comando para mandar los cambios al servidor remoto.

- `git fetch`  
  Lo usamos para traer actualizaciones del servidor remoto y guardarlas en nuestro repositorio local (en caso de que hayan, por supuesto).

- `git merge`  
  También usamos el comando git merge con servidores remotos. Lo necesitamos para combinar los últimos cambios del servidor remoto y nuestro directorio de trabajo.

- `git pull`  
  Básicamente, git fetch y git merge al mismo tiempo.

---

## Adicionalmente, tenemos otros comandos que nos sirven para trabajar en proyectos muy grandes:

- `git log --oneline`  
  Te muestra el id commit y el título del commit.

- `git log --decorate`  
  Te muestra dónde se encuentra el head point en el log.

- `git log --stat`  
  Explica el número de líneas que se cambiaron brevemente.

- `git log -p`  
  Explica el número de líneas que se cambiaron y te muestra qué se cambió en el contenido.

- `git shortlog`  
  Indica qué commits ha realizado un usuario, mostrando el usuario y el título de sus commits.

- `git log --graph --oneline --decorate --all`  
  Muestra un gráfico resumido de las ramas y commits.

- `git log -3`  
  Limitamos el número de commits.

- `git log --after="2018-1-2"`  
- `git log --after="today"`  
- `git log --after="2018-1-2" --before="today"`  
  Commits para localizar por fechas.

- `git log --author="Name Author"`  
  Commits hechos por autor que cumplan exactamente con el nombre.

- `git log --grep="INVIE"`  
  Busca los commits que cumplan tal cual está escrito entre las comillas.

- `git log --grep="INVIE" -i`  
  Busca los commits que cumplan sin importar mayúsculas o minúsculas.

- `git log -- index.html`  
  Busca los commits en un archivo en específico.

- `git log -S "Por contenido"`  
  Buscar los commits con el contenido dentro del archivo.

- `git log > log.txt`  
  Guardar los logs en un archivo txt.

---

> **Resumen:**  
> Aprender estos comandos te permite trabajar en equipo y llevar un control detallado del historial de tu proyecto en servidores remotos.

# CLASE 9-A  
## MIÉRCOLES 4 DE JUNIO DEL 2025  
## Portafolio 3: Introducción a las ramas o branches de Git (Parte 9)

---

### **¿Qué son las ramas en Git?**

Cuando entramos en el proyecto veremos que nos encontramos con la rama `master`, y es a partir de allí que debe saber que esta es la **rama madre o principal**, y las otras ramas se crean para no afectar a la `master`.

Las **ramas (branches)** son la forma de hacer cambios en nuestro proyecto sin afectar el flujo de trabajo de la rama principal. Esto es útil cuando queremos trabajar una parte muy específica de la aplicación o simplemente experimentar.

La **cabecera o HEAD** representa la rama y el commit de esa rama donde estamos trabajando.  
Por defecto, esta cabecera aparecerá en el último commit de nuestra rama principal.  
Pero podemos cambiarlo al crear una rama (`git branch rama`, `git checkout -b rama`) o movernos en el tiempo a cualquier otro commit de cualquier otra rama con los comandos:

- `git reset id-commit`
- `git checkout rama-o-id-commit`

---

### **Repasa: ¿Qué es Git?**

Git es un sistema de control de versiones que permite gestionar los cambios en proyectos de código, facilitando el trabajo colaborativo y el control de versiones.

---

### **¿Cómo funcionan las ramas en Git?**

Las ramas nos permiten trabajar de forma independiente sobre distintas características o soluciones, sin interferir con la rama principal.  
Así, podemos experimentar, desarrollar nuevas funcionalidades, o corregir errores sin interrumpir el trabajo principal.

#### **Comandos útiles de ramas en Git:**

```bash
git branch nombre-rama            # Genera una nueva rama.
git checkout nombre-rama          # Cambia de una rama a otra.
git checkout -b rama              # Crea una rama y nos mueve a ella automáticamente.
git reset id-commit               # Nos lleva a cualquier commit, eliminando los posteriores a ese commit.
git checkout rama-o-id-commit     # Nos lleva a cualquier commit SIN borrar los posteriores.

Práctica guiada:
Mientras la rama master cambia normalmente, vamos a crear una rama paralela llamada second para crear nuevas secciones.
Luego, fusionaremos (merge) esta rama con master para ver cómo quedan los cambios y entender el flujo de ramas en Git.

Al crear otra rama, estamos haciendo una copia de todos los commits de la rama principal. Todos los cambios que hagamos en la nueva rama no afectarán a la rama principal hasta que realicemos un merge.

Pasos básicos en terminal:
En Ubuntu:

Abrir terminal.

En Windows:

Abrir Git Bash como administrador.

bash
Copiar
Editar
cd Tecnicatura
cd class-git
code .          # Abrir proyecto en VS Code (Ubuntu y Windows)
touch index.html # Crear archivo HTML y agregar un <h1> con tu nombre
Guardar y previsualizar:

Ctrl + S para guardar.

Clic derecho para abrir con Live Server y ver los cambios.

Comandos de seguimiento y commit:

bash
Copiar
Editar
git status
git commit -am "mensaje del commit"        # Solo con archivos ya controlados
git commit -a -m "Mensaje del commit"      # Igual al anterior
git commit -a                              # Se abrirá VIM para mensaje de commit
# En VIM: esc + i para escribir mensaje, luego esc, :wq! (Windows) o ctrl + x (Linux)
Visualización de historial:

bash
Copiar
Editar
git log                # Ver los cambios guardados
git log --stat         # Ver cambios nombrando cada archivo
git branch             # Muestra en qué rama estamos
git show               # Muestra el último cambio realizado
Pulsa q para salir de los logs.

Crear y cambiar ramas:

bash
Copiar
Editar
git branch second      # Crea una nueva rama llamada 'second'
git checkout second    # Cambia a la rama 'second'
git branch             # Muestra la rama actual
git status             # Muestra HEAD actual
Limpiar consola:

bash
Copiar
Editar
ctrl + l               # Limpia la consola
Notas importantes:
Al crear una nueva rama, todos los commits anteriores de la rama principal se copian.

Los cambios hechos en la nueva rama no afectan a la rama principal hasta que se realiza un merge.

El uso de ramas facilita el desarrollo colaborativo y la experimentación segura en proyectos de software.

## Ejemplo paso a paso: flujo básico de trabajo con ramas

1. **Guarda el archivo del portafolio:**
    ```bash
    ctrl + s     # Guardamos la clase del portafolio
    F5           # Actualizamos el navegador para ver los cambios
    ```

2. **Verifica el estado de tus archivos:**
    ```bash
    git status   # Vemos el archivo que modificamos
    ```

3. **Agrega los cambios al área de preparación:**
    ```bash
    git add .
    ```

4. **Realiza un commit de los cambios:**
    ```bash
    git commit
    ```
    - En el editor VIM:
        - `esc + i` para escribir el mensaje del commit
        - Escribe el mensaje
        - `esc` para salir del modo edición
        - `:wq!` en Windows / `ctrl + x` en Linux para guardar y salir
        - Si pide confirmación, escribe `s` y luego `Enter`

5. **Verifica nuevamente el estado:**
    ```bash
    git status   # No hay nada más para commitear, estamos en la rama 'segunda'
    ```

6. **Visualiza los cambios realizados:**
    ```bash
    git show     # Vemos todo lo que cambiamos
    q            # Para salir
    ```

7. **Consulta el historial de commits:**
    ```bash
    git log      # Vemos el historial y cómo el HEAD pasó a la rama cabecera
    q            # Para salir
    ```

8. **Cambia a la rama principal (`master`):**
    ```bash
    git checkout master    # Volvemos a la rama master, desaparecen los cambios hechos en 'segunda'
    git log               # El historial no muestra lo realizado en la rama secundaria
    q                     # Para salir
    ```

9. **Regresa a la rama secundaria (`segunda`):**
    ```bash
    git checkout segunda   # Vuelven a aparecer todos los cambios realizados en la rama secundaria
    ```

---

> **Nota:**  
> Así puedes comprobar cómo los cambios hechos en una rama no afectan a la principal hasta que se fusionan (merge). Este es uno de los pilares del trabajo en equipo y la experimentación segura en proyectos con Git.

# CLASE 9-B  
## MIÉRCOLES 4 DE JUNIO DEL 2025  
## Portafolio 4: Fusión de ramas con Git merge (Parte 10)

---

### **¿Qué es la fusión en Git?**

La **fusión (merge)** en Git es el proceso por el cual el sistema une un historial bifurcado. El comando `git merge` permite integrar líneas de desarrollo independientes, generadas por `git branch`, en una sola rama.  
Con este comando, podemos crear un nuevo commit que combina dos ramas: la rama actual y la rama que se indica después del comando.

---

### **¿Cómo unir dos ramas en Git?**

Para combinar ramas en tu repositorio local:

1. Usa `git checkout` para cambiarte a la rama donde deseas fusionar (normalmente, la rama principal).
2. Emplea `git merge` seguido del nombre de la otra rama que deseas integrar.

Esto suele ser una combinación de avance rápido si no hay cambios intermedios.

**Ejemplo:**
```bash
git checkout master
git merge segunda
Recomendaciones importantes
Antes de hacer un merge, guarda y commitea tus cambios.

Utiliza comandos básicos como git fetch, git push y git pull para mantener tu repositorio actualizado.

En caso de conflictos durante el merge, resuélvelos cuidadosamente antes de continuar.

git init                    # Crear un repositorio (solo si es nuevo)
git add .                   # Agregar archivos al área de staging
git commit -m "mensaje"     # Guardar cambios con un mensaje
git branch nombre_rama      # Crear una nueva rama
git checkout nombre_rama    # Cambiar entre ramas
git push origin rama        # Subir rama al servidor remoto
git fetch                   # Traer actualizaciones del remoto
git merge rama              # Fusionar otra rama a la actual
git pull origin rama        # fetch y merge al mismo tiempo
git checkout "commit" "archivo"  # Volver a la versión anterior de un archivo
git reset                   # Volver a un commit anterior (irreversible)
git reset --soft            # Mantiene cambios en staging
git reset --hard            # Todo vuelve a la versión seleccionada
git reset HEAD              # Quita archivos del staging
git rm                      # Elimina archivos del proyecto (no del historial)
git rm --cached             # Elimina archivos solo del staging
git rm --force              # Elimina archivos del proyecto y del disco duro
git status                  # Estado actual del repositorio
git log                     # Historial de commits
git log --stat              # Historial con detalle de archivos cambiados
git show                    # Cambios de un commit específico
git diff "commit1" "commit2" # Comparar cambios entre versiones
git diff                    # Comparar el directorio con staging

# En rama 'segunda': hacemos cambios y los guardamos
git status
git commit -am "Finalizado el cambio en rama segunda"
git status

# Cambiamos a 'master', agregamos un nuevo párrafo y guardamos
git checkout master
git commit -am "Agregado el contenido adicional del archivo y un mejor aporte"

# Cambiamos entre ramas para ver los cambios
git checkout segunda
git checkout master

# Realizamos el merge
git merge segunda   # Si hay conflictos, se resuelven desde el editor

# Una vez solucionados los conflictos:
git commit -am "Arreglando conflicto"
git status   # Revisar en el navegador y código si algo quedó mal
git commit -am "Solucionado el conflicto 2"

git merge segunda   # Ahora todo va bien
git commit -am "Volví a comentar sobre mi área laboral"
git log
git commit -am "Guardar estos cambios en el README.md"

# Traer cambios a la rama secundaria
git checkout segunda
git merge master
git commit -am "Cargamos esto ahora"

# Volvemos a master y hacemos el último merge
git checkout master
git merge segunda

¿Cómo funciona Git merge?
Git merge fusiona secuencias de confirmaciones en un solo historial, generalmente para combinar dos ramas. Busca una confirmación de base común y genera una confirmación de fusión que representa la combinación de ambas ramas hasta el resultado final.

# CLASE 11 – Configura tus llaves SSH en local

## ¿Por qué usar llaves SSH?

Si usamos GitHub solo con usuario y contraseña, si un día perdemos nuestra PC, perdemos todo. Nuestras contraseñas y los proyectos de nuestros clientes estarían en riesgo. Así es como muchos sitios web son hackeados. Para evitar esto, debemos agregar una capa de seguridad más fuerte usando llaves públicas y privadas.

Esto tiene varias ventajas:
- Nuestra seguridad será mucho mayor.
- Ya no tendrás que poner nunca más tu usuario y contraseña.

## ¿Cómo funciona el sistema de llaves SSH?

- En nuestra máquina, creamos una **llave privada** y una **llave pública**.
- La llave pública se envía a GitHub y le decimos:  
  _"Para este repositorio, usa esta llave pública"_
- A partir de ahí, nos conectamos por el protocolo **SSH** en vez de HTTPS.
- La primera vez, GitHub verifica la relación entre la llave pública (que tiene) y la privada (que está en tu PC).
- Todo esto sucede automáticamente.
- Puedes añadir una contraseña a tu llave privada para sumar más seguridad.
- **Importante:** Las llaves SSH son por persona y por máquina (no por repositorio o proyecto).

---

## Crear y configurar llaves SSH en local

### **1. Abrir la terminal**

- **En Windows:**  
  Abrir **Git Bash** como administrador para tener todos los permisos necesarios.
- **En Ubuntu/Linux:**  
  Abrir una terminal sin entrar a ningún proyecto o carpeta específica.

### **2. Ver tu configuración en Git**

```bash
git config -l
```

Puedes ejecutar esto desde cualquier ruta de tu PC.

### **3. Actualizar el correo que usas en GitHub**

```bash
git config --global user.email "alumnos@mail.com"
```

---

### **4. Generar tus llaves SSH**

```bash
ssh-keygen -t rsa -b 4096 -C "alumnos@mail.com"
```
- Esto genera tu llave pública y privada.
- El programa preguntará dónde guardar la llave: presiona **Enter** para usar la ubicación por defecto.
- Puedes crear una contraseña para tu llave privada.  
  **IMPORTANTE:** Debes recordarla, porque se pedirá cada vez que uses la clave.

---

### **5. Encender el servidor de llaves SSH**

```bash
eval $(ssh-agent -s)
```
Esto deja listo el _servidor_ que gestionará tus llaves SSH.

---

### **6. Añadir tu llave SSH al servidor**

```bash
ssh-add ~/.ssh/id_gd456123
```
- Usa la **ruta de la llave privada** (no la `.pub` que es la pública).
- `~` es la virgulilla y refiere a tu carpeta home.

---

## ¿Qué es una ruta?

Una ruta es la dirección (ubicación) de un archivo o carpeta en tu computadora.  
Por ejemplo:  
`/home/usuario/.ssh/id_rsa` o `C:\Users\TuUsuario\.ssh\id_rsa`

---

## Resumen: Comandos para generar y usar llaves SSH

### **a. Generar llaves SSH**

```bash
ssh-keygen -t rsa -b 4096 -C "tu@email.com"
```

### **b. Configurar el sistema**

**Windows/Linux:**

```bash
eval $(ssh-agent -s)
ssh-add ruta-donde-guardaste-tu-llave-privada
```

**Mac:**

```bash
eval "$(ssh-agent -s)"
```
- Si usas OSX Sierra (v10.12) o superior, crea/modifica el archivo `config` en tu carpeta de usuario:
  
  ```
  Host *
      AddKeysToAgent yes
      UseKeychain yes
      IdentityFile ruta-donde-guardaste-tu-llave-privada
  ```

- Para añadir la llave SSH:
  
  ```bash
  ssh-add -K ruta-donde-guardaste-tu-llave-privada
  ```
  (Si da error, prueba sin el argumento `-K`).

---

## Activar el Segundo Factor de Autenticación (2FA) en GitHub

El 2FA agrega una capa más de seguridad a tu cuenta. Si pierdes un dispositivo, tendrás respaldo. Puedes usar apps que generan códigos temporales.

### **Cómo activarlo:**

1. Haz clic en tu perfil (arriba a la derecha).
2. Ve a **Settings**.
3. Selecciona **Password and Authentication**.
4. **GitHub Mobile:**  
   Instala la app de GitHub Mobile y úsala para la autenticación 2FA.
5. **Authenticator app:**  
   Elige "Edit" para agregar una app que genere códigos (por ejemplo, Twilio Authy Authenticator).  
   Escanea el QR y guarda los datos para tener acceso si cambias de dispositivo.

---

