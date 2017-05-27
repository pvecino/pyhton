# X-Serv-14.10-CuatroAplis
Ejercicio 14.10 - Clase servidor, cuatro aplis

## Enunciado

Utilizando la clase creada para <a href="https://github.com/CursosWeb/X-Serv-14.10-ServVariasApps">Clase servidor de varias aplicaciones</a>, crea una una aplicación web con varias aplis:

<ul>
  <li>Si se invocan recursos que comiencen por <i>/hola</i>, se devuelve una página HTML en la que se vea el texto <i>Hola</i>.
  <li>Si se invocan recursos que comiencen por <i>/adios</i>, se devuelve una página HTML en la que se vea el texto <i>Adiós</i>.
  <li>Si se invocan recursos que comiencen por <i>/suma/</i>, se proporciona la funcionalidad de <i>Sumador simple</i> (ejercicio 14.4), esperando que los sumandos se incluyan justo a continuación de <i>/suma/</i>.
  <li>Si se invocan recursos que comiencen por <i>/aleat/</i>, se proporciona la funcionalidad de <i>Aplicación web generadora de URLs aleatorias</i> (ejercicio 14.6).
</ul>

## Forma de entrega

Has de tener un repositorio llamado X-Serv-14.10-CuatroAplis en tu cuenta en GitHub
que incluya el fichero de nombre 'webapp.py' que contenga la clase principal webApp,
y los ficheros 'hola.py', 'suma.py' y 'aleat.py' con las clases de las aplicaciones
(nótese que en 'hola.py' deberán estar las clases para los casos de <i>/hola</i> y <i>/adios</i>).

Se proporciona un script, check.py, para comprobar la entrega correcta
del ejercicio. El script de comprobación se ha de ejecutar desde terminal
pasándole como parámetro tu nombre de usuario en GitHub. Así, un ejemplo de
ejecución sería:

$ python check.py gregoriorobles
