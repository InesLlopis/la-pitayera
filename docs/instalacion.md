# Instalación y configuración

## Requisitos

- Windows y PowerShell.
- Git con acceso HTTPS al repositorio.
- Python 3.14.8.
- Node.js 24.21.0 y npm 11.19.0.
- MariaDB Server 11.4.13, como servicio local en el puerto `3306`.
- Un navegador web moderno.

## Preparar MariaDB en local

1. Instalar MariaDB Server 11.4.13 para Windows desde el [sitio oficial](https://mariadb.org/download/).
2. Durante la instalación, crear la instancia como servicio de Windows, habilitar TCP/IP en el puerto `3306` y establecer una contraseña de `root`.
3. Abrir **MariaDB Command Prompt** y conectarse como administrador:

```cmd
mysql -u root -p
```

4. En el indicador de MariaDB, crear una base vacía y una cuenta para que Django se conecte:

   ```sql
   CREATE DATABASE IF NOT EXISTS la_pitayera
     CHARACTER SET utf8mb4
     COLLATE utf8mb4_unicode_ci;

   CREATE USER IF NOT EXISTS 'pitayera_app'@'localhost'
     IDENTIFIED BY 'ESCRIBE_AQUI_TU_CLAVE_LOCAL';

   GRANT ALL PRIVILEGES ON la_pitayera.* TO 'pitayera_app'@'localhost';

   EXIT;
   ```

   Sustituir `ESCRIBE_AQUI_TU_CLAVE_LOCAL` por una contraseña local propia. No guardar la contraseña real en este documento ni subirla al repositorio.

## Configurar el backend

Desde la raíz del repositorio, crear el entorno virtual e instalar las dependencias:

```powershell
Set-Location backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

`(.venv)` al principio de la línea indica que el entorno virtual está activo. Si se abre otra terminal, hay que volver a `backend` y activarlo.

En esa misma terminal, configurar la conexión con MariaDB local:

```powershell
$env:MARIADB_HOST = "localhost"
$env:MARIADB_PORT = "3306"
$env:MARIADB_DATABASE = "la_pitayera"
$env:MARIADB_USER = "pitayera_app"

$dbPasswordSecure = Read-Host "Contraseña local de pitayera_app" -AsSecureString
$env:MARIADB_PASSWORD = [System.Net.NetworkCredential]::new("", $dbPasswordSecure).Password
```

La contraseña se introduce sin mostrarla en pantalla. Estas variables solo duran mientras la terminal permanezca abierta.

Para arrancar el backend:

```powershell
python manage.py runserver
```

El servidor queda disponible en <http://127.0.0.1:8000/> y el endpoint de salud en <http://127.0.0.1:8000/api/health/>. Para detenerlo, pulsar `Ctrl+C`.

## Configurar el frontend

Desde la carpeta raíz del proyecto, abre una terminal de PowerShell y ejecuta:

```powershell
Set-Location frontend
npm ci
npm run dev
```

`npm ci` instala las dependencias indicadas en `package-lock.json`. `npm run dev` inicia el servidor local de Vite. Abre la dirección que aparezca en la terminal, normalmente <http://localhost:5173/>.

Para detener el servidor, pulsa `Ctrl+C`.

## Comprobar la comunicación

Con el backend y el frontend en ejecución, abre <http://localhost:5173/>. La página debe mostrar el título «La Pitayera» y el resultado de la comprobación de conexión con el backend.

También se puede comprobar directamente el endpoint en <http://127.0.0.1:8000/api/health/>. Una respuesta con `"status": "ok"` confirma que el endpoint está disponible. La página del frontend obtiene esa respuesta a través del proxy configurado en Vite.

## Capturas

Las capturas de la comprobación del hito 1 se guardan en `docs/capturas/`.

- `hito1BackendHealth.png`: respuesta del endpoint de salud del backend.
- `hito1Integración.png`: frontend mostrando la respuesta recibida del backend.

## Problemas encontrados y soluciones

- **El comando `mariadb` no se reconoce en PowerShell.** Se comprobó que MariaDB estaba instalado y funcionando como servicio. Para conectarse se utilizó MariaDB Command Prompt y el cliente `mysql`.
- **El backend intentaba conectarse a un servidor llamado `db`.** Ese nombre se usaba en la configuración de Docker. Al trabajar en local, se configuro `MARIADB_HOTS` como `localhost` en la terminal del backend.
- **`npm ci` fallaba con el error `Class extends value undefined is not a constructor or null`.** Se seleccionó Node.js 24.21.0 con nvm y se volvió a ejecutar `npm ci`, que terminó correctamente.
- **Las variables de conexión no estaban disponibles en una nueva terminal.** Las variables de entorno de PowerShell pertenecen a la sesión donde se definen; al abrir otra terminal, hay que volver a configurarlas antes de iniciar el backend.