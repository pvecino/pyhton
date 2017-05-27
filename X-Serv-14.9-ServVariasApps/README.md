# X-Serv-14.9-ServVariasApps
Ejercicio 14.9 - Clase servidor de varias aplicaciones

## Enunciado

Realizar una nueva clase, similar a la que se construyó en el ejercicio <a href="https://github.com/CursosWeb/X-Serv-14.5-ServAplicaciones">Clase servidor de aplicaciones</a> (ejercicio 14.5), pero preparada para servir varias aplicaciones (<i>aplis</i>). Cada <i>apli</i> se activará cuando se invoquen recursos que comiencen por un cierto prefijo.

Cada una de estas <i>aplis</i> será a su vez una instancia de una clase con origen en una básica con los dos métodos <b>parse</b> y <b>process</b>, con la misma funcionalidad que tenían en <a href="https://github.com/CursosWeb/X-Serv-14.5-ServAplicaciones">Clase servidor de aplicaciones</a>. Por lo tanto, para tener una cierta apli, se extenderá la jerarquía de clases para <i>aplis</i> con una nueva clase, que redefinirá <b>parse</b> y <b>process</b> según la semántica de la apli.

Para especificar qué <i>apli</i> se activará cuando llegue una invocación a un nombre de recurso, se creará un diccionario donde para cada prefijo se indicará la instancia de <i>apli</i> a invocar. Este diccionario se pasará como parámetro al instanciar la clase que sirve varias aplicaciones.

## Entrega

Este ejercicio no ha de ser entregado.
