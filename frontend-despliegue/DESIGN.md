# DESIGN.md — Guía de estilo de mi frontend

## Guía elegida

- **Nombre:** Material Design 3 (Google).
- **Enlace oficial:** https://m3.material.io/
- **Por qué la he elegido:** He elegido Material Design 3 porque permite desarrollar interfaces modernas, intuitivas, accesibles y adaptables a diferentes dispositivos. Además, ofrece componentes reutilizables y un sistema de diseño coherente, ideal para una tienda online como La Pitayera.

## Colores (design tokens)

Se utiliza como referencia la paleta base de Material Design 3 para tema claro.

| Token | Valor | Uso |
|---|---|---|
| color-primary | #6750A4 | Botones principales, enlaces y elementos destacados |
| color-on-primary | #FFFFFF | Texto e iconos sobre el color primario |
| color-surface | #FEF7FF | Fondo principal de la página |
| color-on-surface | #1D1B20 | Texto principal |
| color-error | #B3261E | Mensajes de error y acciones destructivas |

## Tipografía

- **Familia:** Roboto.
- **Tamaño de título:** 22 px (Title Large).
- **Tamaño de texto normal:** 16 px (Body Large).
- **Pesos utilizados:**
  - Regular (400): texto normal.
  - Medium (500): títulos secundarios, etiquetas y botones.
  - Bold (700): énfasis puntual.

## Espaciado y forma

- **Unidad base de espaciado:** 4 px.
- **Espaciados:**
  - s = 8 px.
  - m = 16 px.
  - l = 24 px.
- **Radio de los bordes:**
  - 8 px para campos y botones.
  - 12 px para tarjetas.
  - 28 px para contenedores destacados.

## Componentes

- **Botón principal:** Botón de estilo Filled Button, con fondo del color primario (#6750A4), texto blanco, bordes redondeados y texto en formato oración (sin escribirlo todo en mayúsculas). Cuando esté deshabilitado tendrá una apariencia atenuada y no permitirá interacciones.

- **Campo de texto:** Campo con borde visible, fondo claro y etiqueta flotante. Tendrá un relleno interior suficiente para facilitar la lectura y la interacción.

- **Zona de resultado o mensaje:** Se utilizarán tarjetas (Cards) para mostrar información de productos, precios y resultados. Los mensajes informativos se mostrarán mediante avisos o textos de apoyo.

- **Mensaje de error:** Color rojo (#B3261E), acompañado de un icono de advertencia y un texto explicativo. Se mostrará cerca del campo o elemento que haya provocado el error.

## Accesibilidad

- **Contraste mínimo del texto:** 4.5:1 para texto normal y 3:1 para texto grande, siguiendo WCAG AA.
- **Foco visible:** Los elementos interactivos mostrarán un contorno visible de 2 px al recibir el foco mediante el teclado.
- Todos los campos tendrán una etiqueta visible.
- Los botones y enlaces tendrán nombres descriptivos.
- Los errores no se comunicarán únicamente mediante el color, sino también mediante texto e iconos.
- La interfaz será adaptable a diferentes tamaños de pantalla.

## Tono de los textos

- **Tono:** Cercano, claro y profesional.
- **Tratamiento:** Tuteo.
- **Longitud:** Mensajes breves y directos.
- **Estilo:** Lenguaje sencillo, evitando tecnicismos innecesarios.
- **Ejemplos:** "Añadir al carrito", "Tu pedido se ha realizado correctamente" y "Introduce un correo electrónico válido".