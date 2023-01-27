#Importamos las extensiones de Flask necesarias
from flask_sqlalchemy import SQLAlchemy

#Instanciamos SQLAlchemy en la variable db
db = SQLAlchemy()

class Proveedor(db.Model):
    __tablename__ = "proveedor"
    id = db.Column(db.Integer, primary_key=True)
    razonSocial = db.Column(db.String(200), nullable=False, unique=True)
    cuit = db.Column(db.String(12), nullable=False, unique=True)

    def __init__(self,razonSocial,cuit):
        self.razonSocial=razonSocial
        self.cuit=cuit

    def serializarADiccionario(self):
        return {"razonSocial": self.razonSocial
                }

    def getId(self):
        return self.id

    def getRazonSocial(self):
        return self.razonSocial

class TipoCereal(db.Model):
    __tablename__="tipocereal"
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(200),nullable=False,unique=True)


class Cereal(db.Model):
    __tablename__ = "cereal"
    id = db.Column(db.Integer, primary_key=True)
    idTipoCereal=db.Column(db.Integer,db.ForeignKey("tipocereal.id"))
    nombre = db.Column(db.String(200), nullable=False,unique=True)

    def serializarADiccionario(self):
        return {"nombre": self.nombre
                }

    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre

class EncargadoDeCompras(db.Model):
    __tablename__ = "encargadodecompras"
    id = db.Column(db.Integer, primary_key=True)
    legajo = db.Column(db.Integer,nullable=False,unique=True)
    nombre = db.Column(db.String(200),nullable=False)
    apellido = db.Column(db.String(200),nullable=False)

    def serializarADiccionario(self):
        return {
                "legajo": self.legajo
                }

    def getId(self):
        return self.id

class Contrato(db.Model):
    __tablename__ = "contrato"
    id = db.Column(db.Integer, primary_key=True)
    numero=db.Column(db.Integer,nullable=False,unique=True)
    cantidadDeToneladas=db.Column(db.Integer,nullable=False)
    precioPorTonelada=db.Column(db.Float,nullable=False)
    cantidadDeCamiones=db.Column(db.Integer,nullable=False)
    fechaInicio=db.Column(db.Date,nullable=False)
    fechaFin=db.Column(db.Date,nullable=False)
    arregloValoresIndicadorCalidad=db.relationship('ValorIndicadorCalidadContrato')
    idCereal = db.Column(db.Integer, db.ForeignKey('cereal.id'))
    idProveedor = db.Column(db.Integer, db.ForeignKey('proveedor.id'))
    idEncargadoDeCompras = db.Column(db.Integer, db.ForeignKey('encargadodecompras.id'))

    def __init__(self,numero,cantidadDeToneladas,precioPorTonelada,cantidadDeCamiones,fechaInicio,fechaFin,idCereal,idProveedor,idEncargadoDeCompras ):
        self.numero=numero
        self.cantidadDeToneladas=cantidadDeToneladas
        self.precioPorTonelada=precioPorTonelada
        self.cantidadDeCamiones=cantidadDeCamiones
        self.fechaInicio=fechaInicio
        self.fechaFin=fechaFin
        self.idCereal=idCereal
        self.idProveedor=idProveedor
        self.idEncargadoDeCompras=idEncargadoDeCompras

    def serializarADiccionario(self):
        prove=db.session.query(Proveedor).filter_by(id=self.idProveedor).first()
        cereal=db.session.query(Cereal).filter_by(id=self.idCereal).first()
        encargado=db.session.query(EncargadoDeCompras).filter_by(id=self.idEncargadoDeCompras).first()
        return {"id": self.id,
                "numero": self.numero,
                "cantidadDeToneladas": self.cantidadDeToneladas,
                "precioPorTonelada":self.precioPorTonelada,
                "cantidadDeCamiones":self.cantidadDeCamiones,
                "fechaInicio":self.fechaInicio,
                "fechaFin":self.fechaFin,
                "nombreCereal":cereal.getNombre(),
                "razonSocialProveedor":prove.getRazonSocial(),
                "nombreEncargadoDeCompras":encargado.nombre +" "+ encargado.apellido}

    def getId(self):
        return self.id


class indicadorCalidad(db.Model):
    __tablename__ = "indicadorcalidad"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200),nullable=False,unique=True)

    def serializarADiccionario(self):
        return {
                "nombre": self.nombre
                }
    def getId(self):
        return self.id
class ValorIndicadorCalidadContrato(db.Model):
    __tablename__ = "valorindicadorcalidadcontrato"
    id = db.Column(db.Integer, primary_key=True)
    valorDesde=db.Column(db.Float,nullable=False)
    valorHasta=db.Column(db.Float,nullable=False)
    idContrato=db.Column(db.Integer,db.ForeignKey('contrato.id'))
    idIndicadorCalidad=db.Column(db.Integer,db.ForeignKey('indicadorcalidad.id'))

    def __init__(self,valorDesde,valorHasta,idContrato,idIndicadorCalidad):
        self.valorDesde=valorDesde
        self.valorHasta=valorHasta
        self.idContrato=idContrato
        self.idIndicadorCalidad=idIndicadorCalidad

