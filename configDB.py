#Declaramos una clase llamada Configuracion con las configuraciones propias de la app
class Configuracion():
    #Habilitamos el debug de la app flask para cada vez que hagamos un cambio en nuestro código  se reinicie el servidor
    # y no tener que hacerlo manualmente para que los cambios se tengan en cuenta
    DEBUG = True
    #Desactivamos las notificaciones sobre modificaciones hechas a la instancia SQlAlchemist
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Establecemos configuraciones sobre la instancia creada previamente para hacer conexión y mapear la base de datos creada
    #Indicamos el URI( identificador uniforme de recursos) de la base de datos que debe usarse para la conexión. En este caso se compone de:
    #                         basededatosusada://usuario:contrase;a@host/nombredelaBD
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/modelocompras'
    #En mi caso, como dije previamente lo configure con usuario ROOT, sin password y cree la BD “modelocompras”.