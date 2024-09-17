Quiero que hagas un analisis de los modelos open source que existen en Huggingface y que los filtres
por la capacidad de utilizar imagenes satelitales para el proceso de deteccion de objetos.
Los objetos a detectar son piletas de natación, o sea, piscinas NO industriales y NO comerciales, 
solo las piscinas residenciales.
Las imagenes a utilizar no tienen grandes variaciones, ya que serán tomadas desde QGIS desde capas base
de Google Satellite en escala 1:1000 y el formato de las imagenes puede ser jpg o cualquier otro, ya que serán 
descargadas manualmente desde QGIS.
NO es necesario detección en tiempo real, no hay apuro en cuanto a tiempo de procesamiento.
Los recursos computacionales con que se cuenta NO incluyen GPU. Por lo tanto, al no haber GPU se deberá
utilizar CPU.
La precision requerida es la necesaria para poder hacer una detección precisa de cada piscina.
Estos modelos tienen que poder ser utilizados por medio de la api inference de huggingface.
Y necesito que me recomiendes que modelo utilizar con una guia, paso a paso sobre como 
utilizarlo desde una aplicación NODE.JS. 
