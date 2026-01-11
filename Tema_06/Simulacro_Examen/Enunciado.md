# Simulcaro de Examen Python

> Este simulacro cuenta con un apartado para realizarlo usando JSON y otro usando TXT con campos de longitud fíja.

> Si estás abriendo este fichero en VScode, es **posible** que necesites instalar estas 2 extensiones, pero debería ser suficiente con pulsar ```Crtl + Shift + V```:
> 1. Markdown Preview Enhanced (Para visualizar Markdown)
> 2. Markdown Preview Mermaid Support (Para visualizar Mermaid dentro de Markdown)

## Enunciado
El ministerio de Magia ha pedido una aplicación de consola en **Python** que permita gestionar los magos y brujas de Hogwarts.
Un mago/bruja debe contener los siguientes atributos:
- Nombre: Único, le diferenciará del resto. 2 Magos son iguales si tienen el mismo nombre.
- Edad
- Sangre
- Casa
- Nota media del curso

Al hacer un ```print(harry)``` el resultado debe ser el siguiene ```Nombre: Harry | Edad: 12 | Sangre: Limpia | Casa: Gryffindor | Nota media: 9.5```
Aparte de esto, debe tener un método de clase que debe enfrentar a dos magos, y ganará aquél que tenga más nota media.
Se debe controlar que los datos introducidos sean válidos. El nombre no puede contener espacios (Una única palabra), la edad no puede ser nagativa, la nota media no puede ser inferior a 0 ni superior a 10 y no puede tener ningún atributo vacío.

La aplicación debe mostrar un menú con las siguientes opciones:
1. Registrar: Registra un mago que NO exista.
2. Listar: Muestra todos los magos.
3. Enfrentar Magos: Solicita el nombre de dos magos y muestra al ganador. Se debe solicitar el nombre de los magos separados por espacios. Ej: Harry Draco.
4. Expulsar: Elimina un mago del registro.
5. Modificar: Modifica los atributos de un mago MENOS su nombre
6. Salir: Finaliza el programa con un mensaje de despedida.

El menú se debe mostrar con un método llamado mostrar_menu() en la clase Menu. Dicho método debe ser un método de clase.
Debes generar 3 ficheros en total:
1. Mago.py
2. Menu.py
3. ExamenNombreApellido.py (Main) Donde NombreApellido debe ser _tu_ Nomb y Apellido.

La información debe ser **persistente**. Es decir, si se termina el programa, no debe perderse, debe guardarse en el fichero que se entrega con este enunciado.
Tanto si se hace con JSON como con TXT de longitúd fija, el fichero se debe leer cuando se inicia el programa, y debe guardar los datos durante su ejecución.
Y debe guardar los cambios cuando se termina el programa.


### TXT de longitúd fija
Si sobran caracteres, se debe cortar, si falta, se rellena con espacios.
Nombre: Longitúd fija de 10 caracteres. Si sobra, se debe cortar, si falta, se rellena con espacios.
Edad: Longitúd de 2 caracteres 0 menos.
Tipo de Sangre: Longitúd fija de 5 caracteres.
Nota media: 4 caracteres en total, 2 enteros y 2 decimales, ten en cuenta que la coma ES un caracter.

### Diagrama de Clases.
````mermaid
classDiagram
direction LR
class Mago {
    +str nombre
    +int edad
    +str sangre
    +str casa
    +float nota_media
    +void enfrentar(mago_uno, mago_dos) (Método de clase)
}

class Menu {
    + mostrar_menu() (Método de clase)
}
```