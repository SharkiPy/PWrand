# PWrand
Genera contraseñas aleatorias de longitud variable.

La idea surge de querer inscribirme a un foro dónde la contraseña debía contener > 12 caracteres. Como no se me ocurría ninguna, y las que se me ocurrían me parecían una chapuza, cogí Atom (que por cierto, el IDE de github da para hablar... -y para bien-) y diseñé un script de unas pocas lineas para solucionar todo este enrollo.

A raiz de la demostración con GetLetter de que montar una contraseña en base a algo no es sofisticado, y menos si ésta sigue un patrón, (en el caso de GetLetter el patrón era un refrán.) no era para nada seguro, continue con el script que había hecho para mi situación, dejándolo en algo bastante simple y ligero. 798 Bytes...


# Usage

Es sencillo, y solo tiene un argumento válido. 
>PWrand <int>

Tan sencillo como eso. Solo se necesita ejecutar el programa y decirle de cuántos caracteres será la contraseña que pretendéis generar.

Si hablamos de aleatoriedad, es bien sabido que en programación nada es aleatorio, sino más bien pseudoaleatorio, se puede recrear un mismo escenario para que devuelva una misma contraseña, por ejemplo algunas funciones Rand, como puede ser las de C++ devuelven el valor aleatorio en función de X números de procesos en ese momento, o X tiempo en la pila, una de las formas de crear una secuencia totalmente aleatoria sería en función del sonido que emite un dispositivo.

En definitiva, son números que no son verdaderamente aleatorios pero sirven para una aplicacion que espera algun grado de aleatoridad, y para este caso va perfecto.
