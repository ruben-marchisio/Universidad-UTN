# Guía Completa: Comandos de Terminal y Git

## Tabla de Contenidos

* [Introducción](#introducción)
* [Clase 1: Comandos Básicos de Terminal](#clase-1-comandos-básicos-de-terminal)
* [Clase 2: Terminal y Primeros Pasos con Git](#clase-2-terminal-y-primeros-pasos-con-git)
* [Clase 3: Analizar Cambios y Control de Versiones](#clase-3-analizar-cambios-y-control-de-versiones)
* [Clase 4: Edición y Documentación en Markdown](#clase-4-edición-y-documentación-en-markdown)
* [Clase 5: Staging y Conceptos de Gitflow](#clase-5-staging-y-conceptos-de-gitflow)
* [Clase 6: Reset y Checkout – Volver en el Tiempo](#clase-6-reset-y-checkout-–-volver-en-el-tiempo)
* [Clase 7: git reset vs. git rm](#clase-7-git-reset-vs-git-rm)
* [Clase 8: Trabajo Remoto y Repositorios en Equipo](#clase-8-trabajo-remoto-y-repositorios-en-equipo)
* [Clase 9: Ramas y Flujo de Trabajo con Branches](#clase-9-ramas-y-flujo-de-trabajo-con-branches)
* [Clase 10: Fusiones y Merges en Git](#clase-10-fusiones-y-merges-en-git)
* [Clase 11: Seguridad, SSH y 2FA en GitHub](#clase-11-seguridad-ssh-y-2fa-en-github)

---

# Introducción

Esta guía recopila los comandos y conceptos esenciales para el uso de la terminal (Git Bash, Ubuntu, Mac) y el sistema de control de versiones Git. Es útil tanto para quienes se inician como para quienes desean repasar o profundizar en buenas prácticas de desarrollo y colaboración con repositorios remotos.

**Profesor:** Ariel Betancud

---

# Clase 1: Comandos Básicos de Terminal

### Navegación

* `pwd` → Muestra la ruta actual
* `cd [carpeta]` → Cambia de directorio
* `cd /` → Va a la raíz
* `cd ~` → Va al home del usuario
* `ls` → Lista los archivos de la carpeta actual
* `ls -al` → Lista todos los archivos (incluidos ocultos)
* `ls -l` → Lista detallada
* `ls -a` → Todos los archivos, sin detalles
* `clear` → Limpia la consola
* `cd ..` → Sube un nivel
* `cd [letra]:/` → Cambia de disco (Windows)
* `cd /mnt/[letra]` → Cambia de disco en WSL
* `df -h` → Muestra uso de disco (Linux)

### Creación y Manejo de Carpetas

```bash
mkdir Tecnicatura
cd Tecnicatura
mkdir Python Java JavaScript
```

* En Linux, distingue mayúsculas/minúsculas.

---

# Clase 2: Terminal y Primeros Pasos con Git

### Comandos de Archivos

* `touch archivo.txt` → Crea un archivo vacío
* `cat archivo.txt` → Muestra su contenido
* `history` → Ver historial de comandos
* `!número` → Repite comando de historial
* `rm archivo.txt` → Borra archivo
* `rm --help` → Ayuda sobre `rm`

### Iniciando un Repositorio Git

```bash
cd Tecnicatura
mkdir class-git
cd class-git
git init
code .  # Abre VSCode
```

* `git status` → Estado actual
* `git add archivo` → Añadir al staging
* `git commit -m "mensaje"` → Primer commit
* `git rm --cached archivo` → Quitar de staging

### Configuración de Git

* `git config --global user.name "Tu Nombre"`
* `git config --global user.email "tu@email.com"`
* `git config --list` → Ver configuración

---

# Clase 3: Analizar Cambios y Control de Versiones

### Comandos Clave

* `git add .` → Añade todos los cambios
* `git commit -m "mensaje"` → Guardar snapshot
* `git log` → Ver historial de commits
* `git show` → Muestra el último commit
* `git log archivo.txt` → Cambios de un archivo

### Edición con Vim (en commits sin `-m`)

* `Esc` → Salir modo edición
* `:wq!` → Guardar y salir

---

# Clase 4: Edición y Documentación en Markdown

* `touch README.md` → Archivo markdown
* [Guía Markdown de GitHub](https://docs.github.com/es/get-started/writing-on-github)
* Usa `code .` para abrir y editar
* Documenta los pasos y comandos utilizados

---

# Clase 5: Staging y Conceptos de Gitflow

### ¿Qué es el Staging?

* **Working directory**: Edición
* **Staging area**: `git add archivo` (RAM)
* **Repositorio**: `git commit` guarda el snapshot
* Cada commit genera un hash único

### Gitflow

* Modelo de trabajo con ramas: `master`, `develop`, `feature`, `release`, `hotfix`
* Controla el flujo y calidad del código
* Solo se integran cambios en ramas principales a través de merges

### Comandos

```bash
git add .
git commit -m "mensaje"
git log
```

---

# Clase 6: Reset y Checkout – Volver en el Tiempo

### Comandos y Explicación

```bash
cd Tecnicatura/class-git
ls
touch historia.txt
cd ..
code .
git commit -a              # Commit todos los archivos modificados
git log                    # Ver historial
git show                   # Ver detalles del último commit
git log --oneline          # Resumen

# Volver atrás
git reset <hash>           # Soft: mantiene cambios en staging
git reset --hard <hash>    # Duro: borra todo
# Comparar y revisar cambios
git diff
# Volver a versión específica
git checkout <hash>
git checkout master
```

---

# Clase 7: git reset vs. git rm

### git reset

* Deshace cambios de diferentes formas:

  * `--soft`: mantiene cambios en staging
  * `--hard`: borra todo
  * `--mixed`: por defecto, elimina del staging
  * `git reset HEAD archivo` → Saca archivo del staging

### git rm

* Elimina archivos del repo (y disco, con `--force`)
* `git rm --cached` → Elimina solo del staging
* Diferencia: `git reset` saca del staging, `git rm` elimina archivos

### Resumen Visual

```
Working Directory ← git add → Staging ← git commit → Repo
```

---

# Clase 8: Trabajo Remoto y Repositorios en Equipo

### Servidores Remotos: GitHub, GitLab, Bitbucket

#### Comandos para trabajar con repositorios remotos

* `git clone URL` → Descargar repositorio remoto
* `git push` → Subir cambios
* `git fetch` → Traer cambios (no los aplica)
* `git merge` → Fusionar cambios
* `git pull` → Trae y fusiona (fetch + merge)

#### Otros útiles

* `git log --oneline --graph --decorate --all`
* `git log --after="2024-01-01"`
* `git log --author="Nombre"`
* `git log --grep="texto"`
* `git log > log.txt` → Guardar historial

---

# Clase 9: Ramas y Flujo de Trabajo con Branches

### ¿Qué es una rama (branch)?

* Permite aislar cambios y experimentar sin afectar la rama principal (`master`)

#### Comandos de ramas

```bash
git branch nombre-rama      # Crear nueva rama
git checkout nombre-rama    # Cambiar de rama
git checkout -b rama        # Crear y cambiar a la vez
git merge otra-rama         # Fusionar ramas
git log --graph             # Ver flujo de ramas
```

### Ejemplo básico de flujo con ramas

1. Edita un archivo en una rama secundaria
2. Commit de cambios
3. Cambia a master y observa diferencias
4. Realiza merge cuando esté listo

---

# Clase 10: Fusiones y Merges en Git

### ¿Qué es un merge?

* Une el historial de dos ramas
* Se recomienda:

  * Commitear antes de mergear
  * Resolver conflictos manualmente

#### Comandos útiles

```bash
git checkout master
git merge secundaria
# En caso de conflicto: editar archivos, luego
 git add .
 git commit -m "Solucionando conflicto"
```

#### Comandos generales

* `git push origin rama` → Subir rama
* `git fetch` → Traer cambios remotos
* `git pull origin rama` → Traer y fusionar
* `git checkout "commit" archivo` → Restaurar archivo a estado anterior

---

# Clase 11: Seguridad, SSH y 2FA en GitHub

## ¿Por qué usar llaves SSH?

* Mayor seguridad y practicidad para trabajar con GitHub
* Sin necesidad de usuario/contraseña cada vez
* Llaves SSH son por usuario y máquina

### Generar y configurar llaves SSH

```bash
ssh-keygen -t rsa -b 4096 -C "tu@email.com"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```

### Opcional para Mac (añadir a keychain)

```bash
ssh-add -K ~/.ssh/id_rsa
```

### Activar 2FA en GitHub

* Settings → Password and Authentication
* Sumar app de autenticación (recomendado: GitHub Mobile, Authy)
* Escanear QR, guardar backups

---

# Recursos útiles

* [Guía oficial de Git](https://git-scm.com/doc)
* [Guía Markdown de GitHub](https://docs.github.com/es/get-started/writing-on-github)
* [Pro Git Book (Español)](https://git-scm.com/book/es/v2)

---

**Sugerencias:**

* Practica cada comando en tu propio repositorio
* No temas experimentar con ramas
* ¡La mejor forma de aprender es equivocándose y recuperando el historial! ✨

# Clase 11 Actividad en Python

## Crear un Proyecto Python con Entorno Virtual y Git

A continuación, se detalla el proceso para iniciar un proyecto en Python, crear y activar un entorno virtual, y versionar el trabajo utilizando Git y GitHub.

### 1. Abrir la terminal  
- En Windows: Git Bash (ejecutar como administrador)  
- En Linux: terminal normal

### 2. Crear una carpeta para el proyecto
```bash
mkdir python-final
```

### 3. Entrar en la carpeta
```bash
cd python-final
```

### 4. Iniciar un repositorio Git
```bash
git init
```

### 5. Crear el archivo principal
```bash
touch finales.py
```

### 6. Abrir Visual Studio Code en la carpeta
```bash
code .
```

### 7. Verificar la versión de Python instalada
```bash
python -V
python3 -V
```

### 8. Crear un entorno virtual
```bash
python3 -m venv venv
```

### 9. Activar el entorno virtual
- En Linux/Mac:
  ```bash
  source venv/bin/activate
  ```
- En Windows:
  ```bash
  venv\Scripts\activate
  ```

### 10. Actualizar pip
```bash
python3 -m pip install --upgrade pip
```

### 11. ¿Qué es pip y por qué lo actualizamos?

**pip** es el gestor de paquetes por defecto de Python. Permite instalar, actualizar y gestionar librerías que no vienen incluidas con Python, facilitando la incorporación de nuevas funcionalidades a nuestros proyectos.  
Actualizar pip garantiza que disponemos de la versión más reciente y segura, evitando problemas de compatibilidad y aprovechando mejoras y correcciones de errores.

### 12. Primer commit y conexión al repositorio remoto
```bash
git add .
git commit -m "Primer commit del entorno virtual y archivo principal"
git remote add origin https://github.com/ruben-marchisio/Hola_Mundo.git
git branch -M main
git push -u origin main
```

### 13. Enlace al repositorio remoto

[https://github.com/ruben-marchisio/Hola_Mundo](https://github.com/ruben-marchisio/Hola_Mundo)

---