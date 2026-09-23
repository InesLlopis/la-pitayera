# La Pitayera

Tienda online de pitahayas - Proyecto Intermodular de 2º DAW.

## Autoría

**Alumna**: Inés Llopis Martínez
**Centro**: IES Severo Ochoa - Elche
**Curso**: 2026/2027

## Descripción

La Pitayera es una aplicación web Fullstack de comercio electrónico especializada en la venta de pitahayas.

El objetivo del proyecto es desarrollar una plataforma que permita a los usuarios consultar un catálogo de productos, registrarse e iniciar sesión, gestionar un carrito de compra y realizar pedidos.

La aplicación contará también con un área privada para administradores, desde la que será posible gestionar los productos, el stock, los usuarios y los pedidos.

El proyecto se desarrolla como parte del Proyecto Intermodular de 2º curso del ciclo formativo de Desarrollo de Aplicaciones Web.

La aplicación estará dividida en un frontend desarrollado con React y un backend desarrollado con Java 21 y Spring Boot.

Ambas partes se comunicarán mediante una API REST utilizando JSON.

---

## Tecnologías

### Guía de estilo y diseño

Se utilizará un sistema de diseño desarrollado específicamente para La Pitayera.

La interfaz buscará representar la temática natural y fresca asociada a la pitahaya, manteniendo una estructura visual clara y priorizando la usabilidad.

Se utilizarán HTML5 y CSS3 para la estructura y presentación de la interfaz.

El diseño será responsive para permitir el uso de la aplicación desde ordenadores, tablets y dispositivos móviles.

---

### Backend

**Java 21 + Spring Boot**

Java 21 será utilizado como lenguaje principal del backend debido a que permite desarrollar una aplicación orientada a objetos y facilita la implementación de una arquitectura estructurada y mantenible.

Spring Boot será utilizado como framework para desarrollar la API REST y gestionar los diferentes componentes del backend.

Se utilizará una arquitectura por capas para separar las responsabilidades de los controladores, servicios y acceso a datos.

El backend será responsable de:
- Gestionar los usuarios.
- Gestionar la autenticación.
- Gestionar la autorización mediante roles.
- Gestionar los productos.
- Gestionar el stock.
- Gestionar los carritos.
- Gestionar los pedidos.
- Aplicar las reglas de negocio.
- Validar los datos recibidos.
- Gestionar el acceso a la base de datos.

---

### Frontend

**React + Vite**

React será utilizado para desarrollar la interfaz de usuario mediante componentes reutilizables.

La elección de React permitirá separar la aplicación en diferentes componentes y gestionar de forma estructurada el estado de la interfaz.

Vite será utilizado como herramienta de desarrollo y construcción del frontend debido a su integración con React y a su rapidez durante el desarrollo.

Se utilizarán también:

- React Router para la navegación.
- JavaScript para la lógica del frontend.
- HTML5 para la estructura.
- CSS3 para los estilos.

El frontend será responsable de:

- Mostrar el catálogo.
- Mostrar los detalles de los productos.
- Gestionar el registro y login.
- Gestionar el carrito.
- Mostrar el proceso de compra.
- Mostrar los pedidos del usuario.
- Gestionar la interfaz del administrador.

---

### Base de datos

**MariaDB**

Se utilizará MariaDB como sistema gestor de base de datos relacional.

Se ha elegido una base de datos relacional debido a que el proyecto contiene diferentes entidades relacionadas entre sí, como usuarios, productos, pedidos y líneas de pedido.

Las relaciones entre estas entidades son importantes para garantizar la integridad y consistencia de la información.

Entre los datos que se almacenarán se encuentran:

- Usuarios.
- Roles.
- Productos.
- Categorías.
- Stock.
- Pedidos.
- Líneas de pedido.

El acceso a la base de datos desde el backend se realizará mediante Spring Data JPA y Hibernate.

---

## Seguridad

La aplicación utilizará **Spring Security** para gestionar la autenticación y autorización.

La autenticación se realizará mediante **JWT (JSON Web Token)**.

Se establecerán diferentes roles de usuario, principalmente:

- Cliente.
- Administrador.

Las operaciones de administración estarán protegidas para impedir el acceso de usuarios que no dispongan de los permisos necesarios.

Las contraseñas de los usuarios no se almacenarán directamente, sino que se utilizará un sistema de hash seguro mediante BCrypt.

---

## API REST

La comunicación entre el frontend y el backend se realizará mediante una API REST.

Los datos se intercambiarán utilizando JSON.

Algunos de los recursos previstos serán:

- `/api/auth`
- `/api/users`
- `/api/products`
- `/api/categories`
- `/api/cart`
- `/api/orders`

La API utilizará los métodos HTTP correspondientes según la operación realizada:

- GET
- POST
- PUT
- DELETE

---

## Documentación

La documentación del proyecto se realizará principalmente mediante:

- README.md para la documentación general del repositorio.
- Javadoc para documentar elementos relevantes del backend.
- JSDoc cuando resulte útil en el frontend.
- Documentación de la API mediante OpenAPI/Swagger.

La documentación se irá ampliando a medida que avance el desarrollo.

---

## Librerías y dependencias relevantes

### Backend

- Spring Web
- Spring Data JPA
- Spring Security
- JWT
- Hibernate
- Bean Validation
- MariaDB Driver
- Maven

### Frontend

- React
- React Router
- Vite

Las dependencias definitivas podrán ampliarse durante el desarrollo cuando sea necesario incorporar nuevas funcionalidades.

---

## Control de versiones

El proyecto utilizará **Git** como sistema de control de versiones y **GitHub** como plataforma para alojar el repositorio.

La rama principal será:

```text
main
```

Durante el desarrollo se utilizarán ramas independientes para implementar nuevas funcionalidades o realizar correcciones.

La nomenclatura prevista para las ramas será:

- feat/nombre-funcionalidad
- fix/nombre-error

Una vez finalizado y comprobado el trabajo de una rama, los cambios se integrarán en ```main```.

### Convención de commits
 Se utilizará una convención para identificar de forma clara el tipo de cambio realizado:

 
 - feat: nueva funcionalidad
 - fix: correción de errores
 - docs: cambios en documentación
 - refactor: modificación interna del código
 - chore: configuración o mantenimiento
 

