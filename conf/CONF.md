# **EXPLICACIÓN***

# **CLAVE: Información**
- "pags": "n" -> "n" representa el número de paginas de la presenbtación.
- "m" representa las dimensiones de la presentación -> (16:9,A4) etc, estos modos se pueden llamar con un alias:
  - "space-pag": m, 
  - "space-mod": m,
- Ejemplo: Una presentación en formato 16:9 -> "space-pag": "DCS"
- space-mod representa el modo de texto/modo de diseño: classic o modern

# COLORES DISPONIBLES

- "color": "color" -> listado de colores disponibles: ["negro", "blanco", "gris_carbon", "gris_oscuro", "gris_grafito", "gris_medio", "azul_marino", "azul_real", "azul_cielo", "verde_esmeralda", "verde_bosque", "violeta", "purpura", "rojo", "naranja", "dorado"] 
# Style Subtitle 

- [anidado] -> **Modo** de texto donde el subtitulo se toma desde una lista (["elemnt1", "element2"]), al agregar este estilo, el texto adquiere el siguente stilo:
 - " element1 | element2"
 - [normal] -> Crea el texto sin estilo, texto puro, sin ningun tipo de estilo, ni diseño.

 # Text body - CONTENIDO DE TEXTO Y IMAGEN
 - [content] -> contiene el contenido de texto que se insertara en la pagina: en lista -> "content": [] o "content": "string"
 - [Key: content] -> Contiene el texto de la pagina. Tiene tres modos de estilo: [format-text]:

  1 - [graph] -> modo de texto insertado en tipado: add_paragraph() (Util para crear listados u puntos de información) se puede usar con o sin imagen -> **"format-text": "graph"**
  2- [i_normal] -> Modo de texto normal, útil cuando la pagina no contiene imagen: "format-text": "i_normal"
  3 - [normal] -> Esto modo de texto es util cuando se contiene una imagen en la pagina. "format-text": "normal"

- **[Letra]**:
 - "typeLetra": "bold" o "typeLetra": "italic"
 - "cuerpoContent": [n] -> "n" representa un número de tamaño de la letra. 

 # Image Mode
  -  "verifyImage": "True", valor boolean, si es False
  - [mode] diseño de imagenes disponibles -> ["tree-d","tree-i","image-a","image-l"] 
    - 1: "tree-d": Imagen a la derecha, texto a la izquierda.
    - 2: "tree-i": Imagen a la izquierda, texto a la derecha.
    - 3: "image-a": imagen arriba, texto abajo.
    - 4: "image-l": Imagen grande con descripción lateral
  - JSON: "mode": "tree-d"