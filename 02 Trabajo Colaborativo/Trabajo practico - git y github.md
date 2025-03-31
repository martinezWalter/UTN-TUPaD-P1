# Trabajo práctico Git & GitHub
## Actividad 1 - Preguntas y Respuestas
### ¿Qué es GitHub?
**Respuesta**
Git es un sistema de control de versiones que realiza un seguimiento de los cambios en los archivos.
### ¿Cómo crear un repositorio en GitHub?
**Respuesta**
En github debemos entrar a la opción 'Mis repositorios', luego la opción 'Nuevo' y debemos seleccionar el nombre del repositorio, una descripción(opcional), y si será de acceso privado o público. También si queremos incluir el archivo README, el archivo gitIgnore, y la licencia. Una vez completado los campos le damos a Crear repositorio.
### ¿Cómo crear una rama en Git?
**Respuesta**
Para crear una rama debemos hacerlo desde la terminal, ubicados en la dirección del repositorio clonado, lo podremos hacer con el siguiente comando;
```bash
git branch nombre-branch
```
### ¿Cómo cambiar a una rama en Git?
**Respuesta**
Para cambiar a una rama ya existente en Git lo podremos hacer con el comando;
```bash
git checkout nombre-branch-existente
```
### ¿Cómo fusionar ramas en Git?
**Respuesta**
Para fusionar dos ramas en Git debemos;

Ubicarnos en la rama que deseemos que contenga los cambios, ejemplo 'main'
```bash
git checkout main
```
Posteriormente, realizamos la fusión con el comando seguido del nombre de la otra rama, ejemplo 'feature';
```bash
git merge feature
```
En caso de haber conflictos los resolvemos, luego debemos realizar el commit y subir los cambios.
### ¿Cómo crear un commit en Git?
**Respuesta** 
Para realizar un commit primero debemos agregar los cambios a guardar con el comando .add, esto agregará los cambios de todos los archivos;
```bash
git add.
```
Posteriormente haremos el commit agregando una descripción;
```bash
git commit -m "Breve descripcion de los cambios a guardar"
```
### ¿Cómo enviar un commit a GitHub?
**Respuesta**
Para mandar un commit a Github debemos hacer el commit previamente,  y posteriormente ejecutar el comando push seguido de 'origin' y el nombre de la rama remota, esto indica que enviaremos los cambios a la rama remota, y de no existir la branch se creará automáticamente;
```bash
git push origin feature
```
### ¿Qué es un repositorio remoto?
**Respuesta** Un repositorio remoto es una versión del proyecto almacenada en un servidor (como GitHub), que permite compartir y sincronizar los cambios entre varios colaboradores.
### ¿Cómo agregar un repositorio remoto a Git?
**Respuesta**
Para agregar un repositorio remoto a Git se utiliza este comando;
```bash
git remote add origin URL-del-repositorio
```
### ¿Cómo empujar cambios a un repositorio remoto?
**Respuesta**
Para empujar cambios a un repositorio remoto lo haremos con el comando push, o push origin nombre-branch;
```bash
git push origin nombre-branch
```
### ¿Cómo tirar de cambios de un repositorio remoto?
**Respuesta**
Para tirar cambios a un repositorio remoto lo haremos con el comando pull, o pull origin nombre-branch;
```bash
git pull origin nombre-branch
```
### ¿Qué es un fork de repositorio?
**Respuesta**
Un fork de repositorio es una copia completa de un repositorio que se realiza en tu propia cuenta de usuario.
### ¿Cómo crear un fork de un repositorio?
**Respuesta**
Para realizar un fork de un repositorio debemos ubicarnos en el mismo, luego dar al botón 'Fork', completar los campos requeridos como nombre del nuevo repositorio que almacenará la copia del repositorio, y con el botón Create Fork finalizaremos la operación.
### ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?
**Respuesta**
Para realizar un pull request en GitHub previamente debemos haber creado y subido cambios a una branch remota. Luego en Github desde la opción Pull request del repositorio debemos seleccionar la rama, seleccionar 'New pull request' y completar los campos requeridos.
### ¿Cómo aceptar una solicitud de extracción?
**Respuesta**
En la sección Pull requests debemos seleccionar la solicitud a aceptar, revisamos los cambios, luego seleccionar Merge Pull Request y luego confirm merge.
### ¿Qué es un etiqueta en Git?
**Respuesta**
Una etiqueta en git es una referencia para marcar un punto específico en el historial del repositorio, normalmente para indicar las versiones importantes.
### ¿Cómo crear una etiqueta en Git?
**Respuesta**
Para crear una etiqueta lo podremos hacer con el comango tag;
```bash
git tag v1.0
```
### ¿Cómo enviar una etiqueta a GitHub?
**Respuesta**
Para enviar una etiqueta lo podemos hacer con el comando push;
```bash
git push origin v1.0
```
### ¿Qué es un historial de Git?
**Respuesta**
Un historial en git es un registro de los cambios realizados en un repositorio.
### ¿Cómo ver el historial de Git?
**Respuesta**
Para ver el historial en Git lo haremos con el comando log, tambien podremos ver una vista compacta concatenando --oneline, o para mas detalles usar --stat;
```bash
git log
```
### ¿Cómo buscar en el historial de Git?
**Respuesta**
Para buscar en el historial de Git podemos usar el comando git log combinado con diversas opciones. Por ejemplo, si deseamos buscar un término específico en los mensajes de commit, podemos usar git log --grep="palabraClave". Si buscamos los commits realizados por un autor específico utilizamos git log --author="nombreAutor". También podemos filtrar por fechas con git log --since="fecha" y git log --until="fecha" o buscar cambios en un archivo concreto con git log ruta-del-archivo. Además para ver los cambios específicos de código en los commits, podemos usar git log -S"palabraClave" o git log -p -G"expresion".
### ¿Cómo borrar el historial de Git?
**Respuesta**
Para borrar el historial de Git debemos hacer un hard reset al primer commit y luego eliminar todas las ramas;
```bash
git checkout --orphan nueva-branch
git add -A
git commit -m "Primer commit"
git push origin nueva-branch --force
```
### ¿Qué es un repositorio privado en GitHub?
**Respuesta**
Es un repositorio en GitHub que solo puede ser accesible por usuarios autorizados.
### ¿Cómo crear un repositorio privado en GitHub?
**Respuesta**
Al crear un nuevo repositorio nos da un campo tipo radio button a seleccionar Private o public, debemos seleccionar la opción Private y posteriormente darle a Crear repositorio.
### ¿Cómo invitar a alguien a un repositorio privado en GitHub?
**Respuesta**
Desde la pestaña "Settings" del repositorio, selecciona "Manage access" y agrega un colaborador con su nombre de usuario.
### ¿Qué es un repositorio público en GitHub?
**Respuesta**
Un repositorio público es un repositorio accesible públicamente, donde cualquier persona puede ver y contribuir.
### ¿Cómo crear un repositorio público en GitHub?
**Respuesta**
Al crear un nuevo repositorio nos da un campo tipo radio button a seleccionar Private o public, debemos seleccionar la opción Public y posteriormente darle a Crear repositorio.
### ¿Cómo compartir un repositorio público en GitHub? 
**Respuesta**
Podemos hacerlo compartiendo la URL del repositorio desde la barra de direcciones del navegador.

## Actividad 2 y 3
Los ejercicios de ejecución de comandos git de la Actividad 2, y los puntos a realizar de la Actividad 3 con los comandos y el archivo README.md fueron hechos en [Este repositorio](https://github.com/martinezWalter/UTP_Programacion_1).
