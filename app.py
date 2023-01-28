#Importamos las extensiones de Flask necesarias
from flask import Flask, request,render_template,json
from flask_cors import CORS,cross_origin
from clases import *
from configDB import Configuracion


#Instanciamos la aplicacion flask que va a contener todos los recursos
app = Flask(__name__)

CORS(app)

#Aplicamos las configuraciones de la clase Configuracion definida en el archivo configuraciones.py
app.config.from_object(Configuracion)

#Vincular la instancia bd del archivo clases.py a nuestra aplicación Flask
db.init_app(app)


@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/redireccionarAltaContrato')
def altasContrato():
    return render_template("altaContrato.html") # Investigar por que funciona asi

@app.route('/altaContrato',methods = ['POST'])
@cross_origin()
def altaContrato():
    # Recibimos el json con la libreria request, que basicamente nos devuelve el dato que pasa el front
    # al hacer la solicitud a la URL.
    # El request.get_json() permite decodificar el JSON y devuelve un diccionario
    data=request.get_json()
    prove = db.session.query(Proveedor).filter_by(razonSocial=data['nombreProveedor']).first()
    cereal = db.session.query(Cereal).filter_by(nombre=data['nombreCereal']).first()
    encargado = db.session.query(EncargadoDeCompras).filter_by(legajo=data['legajoEncargado']).first()
    # Aca tomamos las distintas claves del diccionario pasado en la socilitud y las vamos ubicando y pasando
    # como parametros a la funcion para instanciar un usuario de acuerdo a lo declarado en models.py
    contrato=Contrato(data['numero'],
                    data['cantidadDeToneladas'],
                    data['precioPorTonelada'],
                    data['cantidadDeCamiones'],
                    data['fechaInicio'],
                    data['fechaFin'],
                    cereal.getId(),
                    prove.getId(),
                    encargado.getId()
                      )
    # db.session vendria a ser como una transaccion que vamos a realizar sobre la base de datos instanciada "db"
    # add--> Hace un insert a la tabla usuarios pasandole la instancia de usuario creada previamente
    # la cual se va a transformar en un registro de la tabla
    db.session.add(contrato)
    # Se comitea la operacion anterior(Se confirma la insercion del usuario en la bd)
    db.session.commit()
    for i in data["arregloValoresIndicadorCalidad"]:
        indicador = db.session.query(indicadorCalidad).filter_by(nombre=data["arregloValoresIndicadorCalidad"][i]['nombreIndicadorCalidad']).first()
        c=ValorIndicadorCalidadContrato(data["arregloValoresIndicadorCalidad"][i]["valorDesde"],data["arregloValoresIndicadorCalidad"][i]["valorHasta"],contrato.getId(),indicador.getId())
        db.session.add(c)
        db.session.commit()
        mensaje={
            "mensaje":"exito"
        }
    return json.jsonify(mensaje)


@app.route('/contratos')
@cross_origin()
def getContratos():
    diccionario={}
    n = db.session.query(Contrato).count()
    d=db.session.query(Contrato).all()
    for i in range(0,n):
        diccionario[i]=d[i].serializarADiccionario()
    return json.dumps(diccionario)

@app.route('/indicadores')
@cross_origin()
def getIndicadores():
    diccionario={}
    n = db.session.query(indicadorCalidad).count()
    d=db.session.query(indicadorCalidad).all()
    for i in range(0,n):
        diccionario[i]=d[i].serializarADiccionario()
    return json.dumps(diccionario)


@app.route('/proveedores')
def getProveedores():
    diccionario={}
    n = db.session.query(Proveedor).count()
    p=db.session.query(Proveedor).all()
    for i in range(0,n):
        diccionario[i]=p[i].serializarADiccionario()
    return json.dumps(diccionario)


@app.route('/cereales')
def getCereales():
    diccionario={}
    n = db.session.query(Cereal).count()
    c=db.session.query(Cereal).all()
    for i in range(0,n):
        diccionario[i]=c[i].serializarADiccionario()
    return json.dumps(diccionario)


@app.route('/encargadosdecompra')
def getEncargadoDeCompras():
    diccionario={}
    n = db.session.query(EncargadoDeCompras).count()
    e=db.session.query(EncargadoDeCompras).all()
    for i in range(0,n):
        diccionario[i]=e[i].serializarADiccionario()
    return json.dumps(diccionario)


#EJEMPLO DE COMO RECORRER UN DICCIONARIO CON UN FOR
#@app.route('/prueba')
#def prueba():
   # data = request.get_json()
    #for i in data["arregloValoresIndicadorCalidad"]:
        #print(i["id"])
    #return "exito"



@app.route('/crearTablas')
#Aca defino en la ruta /crearTablas la funcion de crear todas las tablas definidas en la instancia bd
#En mi caso defino de crear todas porque tengo una sola y es para fines de prueba
def crearTablas():
    db.create_all()
    return "exito"


if __name__ == '__main__':
    app.run()
