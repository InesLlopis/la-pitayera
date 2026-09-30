# Guía de estilo — La Pitayera

> Guía visual inicial para la tienda online de pitahayas. La identidad busca una sensación natural, fresca, clara y usable. Los valores cromáticos y tipográficos son propuestas iniciales que pueden evolucionar con el proyecto. [Abrir el diseño editable en Figma](https://www.figma.com/design/x9jdm0klpScIKnZ5HgtYSC).

## Esencia de marca

**Idea:** fruta tropical de calidad, presentada de forma cercana y contemporánea.

**Atributos:** fresca · natural · alegre · honesta · accesible.

**Principios de interfaz:**
- Poner el producto y su origen visual en primer plano.
- Mantener una jerarquía clara entre nombre, variedad, precio y acción.
- Usar el color intenso de la pitahaya como acento y reservar fondos claros para facilitar la lectura.
- Repetir patrones, radios y espaciados para que tienda, carrito y administración se sientan parte del mismo sistema.

## Paleta propuesta

| Token | Hex | Uso |
|---|---|---|
| Pitaya / principal | `#C93668` | CTA primario, enlaces activos, acentos |
| Pitaya / oscuro | `#8F2048` | Hover, texto sobre fondos claros, énfasis |
| Hoja / principal | `#356B4B` | Acento natural, etiquetas de disponibilidad |
| Hoja / suave | `#E8F1E8` | Fondos de apoyo y mensajes positivos |
| Crema / fondo | `#FFF8EF` | Fondo cálido de páginas |
| Blanco / superficie | `#FFFFFF` | Tarjetas, formularios y paneles |
| Tinta / principal | `#292522` | Texto principal |
| Tinta / secundaria | `#6F6963` | Texto auxiliar y metadatos |
| Borde / suave | `#E8DED4` | Divisores y contornos |
| Error | `#B42332` | Errores y acciones destructivas |

Usar texto oscuro en los fondos claros. Para botones de color, validar contraste antes de cerrar los estilos definitivos.

## Tipografía propuesta

- **Titulares y marca:** `DM Sans`, peso 700–800; alternativa de sistema: `Arial`.
- **Interfaz y lectura:** `Inter`, pesos 400–700; alternativa de sistema: `Arial`.
- **Escala:** título de portada 48/56 px; H1 36/44; H2 28/36; H3 22/28; cuerpo 16/24; secundario 14/20; etiqueta 12/16.
- Evitar párrafos largos en mayúsculas. Usar peso y tamaño para crear jerarquía, no muchos colores a la vez.

## Forma y espaciado

- Sistema base de espaciado: 4 px. Valores frecuentes: 4, 8, 12, 16, 24, 32, 48, 64.
- Radio pequeño: 8 px; controles y tarjetas: 12 px; bloques destacados: 20 px.
- Bordes de 1 px, suaves y funcionales. Sombras discretas solo para elevar elementos interactivos.
- Iconos sencillos, de trazo uniforme y sin mezclar estilos.

## Componentes de tienda

- **Botón principal:** fondo Pitaya, texto blanco, altura mínima 48 px, radio 12 px. Estados: reposo, hover, foco visible, desactivado y carga.
- **Botón secundario:** superficie blanca, borde Hoja, texto Hoja.
- **Tarjeta de producto:** foto dominante, nombre, variedad o formato, precio y CTA. Mantener alineados los precios y botones en la rejilla.
- **Etiqueta:** “De temporada”, “Agotado” o “Nuevo”; fondo suave con contraste legible.
- **Campo:** etiqueta persistente, ayuda y error claramente asociados; foco con contorno visible.
- **Navegación:** logo, enlaces esenciales y carrito siempre reconocible; menú móvil compacto.
- **Mensajes:** éxito en verde, aviso en ámbar y error en rojo, acompañados por texto, no solo por color.

## Fotografía y recursos gráficos

- Preferir fotografías luminosas, con detalle de la piel y pulpa de la pitahaya.
- Fondos cálidos y naturales; evitar saturar simultáneamente fotografía, ilustración y acentos.
- Recortar de forma consistente, con el producto centrado y espacio suficiente alrededor.
- Usar ilustraciones botánicas como apoyo editorial, no como sustituto de la fotografía del producto.

## Voz y microcopy

Cercana, directa y optimista. Explicar qué ocurre y cuál es el siguiente paso. Preferir “Añadir al carrito”, “Ver variedades” y “El producto se ha añadido al carrito” frente a mensajes vagos.

## Accesibilidad y responsive

- Contraste legible y foco de teclado visible en todos los controles.
- Objetivos táctiles de al menos 44 × 44 px.
- No transmitir estado solo mediante color; incluir texto o icono con etiqueta.
- En móvil, priorizar catálogo, precio y compra; apilar columnas y conservar márgenes cómodos.
- Probar como mínimo anchos de 360, 768 y 1280 px.