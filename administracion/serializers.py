from rest_framework import serializers
from .models import PersonaModel,AcademicoModel,ConocimientoModel,HabilidadModel,HobbieModel,LaboralModel,Usuario
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class PersonaSerializer(serializers.ModelSerializer):
    #Relacion inversa gracias al related_name para traer toda la lista
    # academicos = AcademicoSerializer(source='academicosPersona',many=True,read_only=True)
    # conocimientos = ConocimientoSerializer(source='conocimientosPersona',read_only=True)
    # habilidades = HabilidadSerializer(source='habilidadesPersona',read_only=True)
    # hobbies = HobbieSerializer(source='hobbiesPersona',read_only=True)
    # laborales = LaboralSerializer(source='laboralesPersona',read_only=True)
    class Meta:
        model=PersonaModel
        #se usa o el atributo fielsds o el atributo exclude
        fields='__all__'
        #exclude =[createdAt]
    
    def update(self):
        # print (self.instance.perObservacion)
        # print (self.validated_data)           
        self.instance.perDni = self.validated_data.get('perDni', self.instance.perDni)
        self.instance.perNombres = self.validated_data.get('perNombres',self.instance.perNombres)
        self.instance.perApellidos = self.validated_data.get('perApellidos',self.instance.perApellidos)
        self.instance.perFecnac = self.validated_data.get('perFecnac',self.instance.perFecnac)
        self.instance.perSexo = self.validated_data.get('perSexo',self.instance.perSexo)
        self.instance.perCorreo = self.validated_data.get('perCorreo',self.instance.perCorreo)
        self.instance.perCelular = self.validated_data.get('perCelular',self.instance.perCelular)
        self.instance.perObservacion = self.validated_data.get('perObservacion',self.instance.perObservacion)
        self.instance.save()
        return self.instance
    
    def delete(self):
        self.instance. estado = False
        self.instance.save()
        return self.instance

class AcademicoSerializer(serializers.ModelSerializer):
    #Clase para hacer la relacion con perId y mostrar todo el registro de persona
    persona=PersonaSerializer(source='perId',read_only=True)
    class Meta:
        model=AcademicoModel
        #se usa o el atributo fielsds o el atributo exclude
        fields='__all__'
        #exclude =[createdAt]
    
    def update(self):
        # print (self.instance.perObservacion)
        # print (self.validated_data)           
        self.instance.acadNivel = self.validated_data.get('acadNivel', self.instance.acadNivel)
        self.instance.acadCestudios = self.validated_data.get('acadCestudios',self.instance.acadCestudios)
        self.instance.acadCarrera = self.validated_data.get('acadCarrera',self.instance.acadCarrera)
        self.instance.acadObservacion = self.validated_data.get('acadObservacion',self.instance.acadObservacion)
        self.instance.perId = self.validated_data.get('perId',self.instance.perId)
        self.instance.save()
        return self.instance

    def delete(self):
        self.instance. estado = False
        self.instance.save()
        return self.instance

class ConocimientoSerializer(serializers.ModelSerializer):
    #Clase para hacer la relacion con perId y mostrar todo el registro de persona
    persona=PersonaSerializer(source='perId',read_only=True)
    class Meta:
        model=ConocimientoModel
        #se usa o el atributo fielsds o el atributo exclude
        fields='__all__'
        #exclude =[createdAt]
    
    def update(self):
        # print (self.instance.perObservacion)
        # print (self.validated_data)           
        self.instance.conociDescripcion = self.validated_data.get('conociDescripcion', self.instance.conociDescripcion)
        self.instance.conociFecini = self.validated_data.get('conociFecini',self.instance.conociFecini)
        self.instance.conociFecfin = self.validated_data.get('conociFecfin',self.instance.conociFecfin)
        self.instance.conociCestudios = self.validated_data.get('conociCestudios',self.instance.conociCestudios)
        self.instance.conociHoras = self.validated_data.get('conociHoras',self.instance.conociHoras)
        self.instance.conociObservacion = self.validated_data.get('conociObservacion',self.instance.conociObservacion)        
        self.instance.perId = self.validated_data.get('perId',self.instance.perId)
        self.instance.save()
        return self.instance

    def delete(self):
        self.instance. estado = False
        self.instance.save()
        return self.instance

class HabilidadSerializer(serializers.ModelSerializer):
    #Clase para hacer la relacion con perId y mostrar todo el registro de persona
    persona=PersonaSerializer(source='perId',read_only=True)
    class Meta:
        model=HabilidadModel
        #se usa o el atributo fielsds o el atributo exclude
        fields='__all__'
        #exclude =[createdAt]
    
    def update(self):
        # print (self.instance.perObservacion)
        # print (self.validated_data)           
        self.instance.habDescripcion = self.validated_data.get('habDescripcion', self.instance.habDescripcion)
        self.instance.habObservacion = self.validated_data.get('habObservacion',self.instance.habObservacion)        
        self.instance.perId = self.validated_data.get('perId',self.instance.perId)
        self.instance.save()
        return self.instance
    
    def delete(self):
        self.instance. estado = False
        self.instance.save()
        return self.instance

class HobbieSerializer(serializers.ModelSerializer):
    #Clase para hacer la relacion con perId y mostrar todo el registro de persona
    persona=PersonaSerializer(source='perId',read_only=True)
    class Meta:
        model=HobbieModel
        #se usa o el atributo fielsds o el atributo exclude
        fields='__all__'
        #exclude =[createdAt]
    
    def update(self):
        # print (self.instance.perObservacion)
        # print (self.validated_data)           
        self.instance.hobDescripcion = self.validated_data.get('hobDescripcion', self.instance.hobDescripcion)
        self.instance.hobObservacion = self.validated_data.get('hobObservacion',self.instance.hobObservacion)        
        self.instance.perId = self.validated_data.get('perId',self.instance.perId)
        self.instance.save()
        return self.instance
    
    def delete(self):
        self.instance. estado = False
        self.instance.save()
        return self.instance

class LaboralSerializer(serializers.ModelSerializer):
    #Clase para hacer la relacion con perId y mostrar todo el registro de persona
    persona=PersonaSerializer(source='perId',read_only=True)
    class Meta:
        model=LaboralModel
        #se usa o el atributo fielsds o el atributo exclude
        fields='__all__'
        #exclude =[createdAt]
    
    def update(self):
        # print (self.instance.perObservacion)
        # print (self.validated_data)           
        self.instance.labEmpresa = self.validated_data.get('labEmpresa', self.instance.labEmpresa)
        self.instance.labCargo = self.validated_data.get('labCargo',self.instance.labCargo)
        self.instance.labFecini = self.validated_data.get('labFecini',self.instance.labFecini)
        self.instance.labFecfin = self.validated_data.get('labFecfin',self.instance.labFecfin)
        self.instance.labContacnombre = self.validated_data.get('labContacnombre',self.instance.labContacnombre)
        self.instance.labContaccelular = self.validated_data.get('labContaccelular',self.instance.labContaccelular)        
        self.instance.labObservacion = self.validated_data.get('labObservacion',self.instance.labObservacion)        
        self.instance.perId = self.validated_data.get('perId',self.instance.perId)
        self.instance.save()
        return self.instance
        
    def delete(self):
        self.instance. estado = False
        self.instance.save()
        return self.instance

# REGISTRO DE USUARIO
class UsuarioRegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        exclude = ['last_login']
    def save(self):
        password = self.validated_data.get('password')
        is_superuser = self.validated_data.get('is_superuser')
        usuCorreo = self.validated_data.get('usuCorreo')
        usuNombre = self.validated_data.get('usuNombre')
        usuFono = self.validated_data.get('usuFono')
        usuCumple = self.validated_data.get('usuCumple')
        is_staff = self.validated_data.get('is_staff')
        
        nuevoUsuario = Usuario(is_superuser=is_superuser, usuCorreo=usuCorreo, usuNombre=usuNombre, usuFono=usuFono, usuCumple=usuCumple,is_staff=is_staff)
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=5)
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)
    class Meta:
        model = Usuario
        fields = ['email','password', 'tokens']
    # esta funcion no le podemos poner otro nombre, puesto que va relacionada con el is_valid() del serializador
    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        usuario = auth.authenticate(usuCorreo=email, password=password)
        if not usuario:
            raise AuthenticationFailed('Credenciales invalidas, intentelo de nuevo')
        return {
            'email': usuario.usuCorreo,
            'tokens': usuario.tokens()
        }