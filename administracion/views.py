from .models import PersonaModel,AcademicoModel,ConocimientoModel,HabilidadModel,HobbieModel,LaboralModel,Usuario
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status   
from .serializers import PersonaSerializer,AcademicoSerializer,ConocimientoSerializer,HabilidadSerializer,HobbieSerializer,LaboralSerializer, UsuarioRegistroSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class PersonasView(ListCreateAPIView):
    queryset = PersonaModel.objects.all() #SELECT * FROM PERSONA
    serializer_class=PersonaSerializer
    #PERMISOS RESTRINGIDO CON TOKEN DE ACCESO
    permission_classes = (IsAuthenticated,)
    def get(self,request):
    #Cuando el queryset devuelve una lista se tiene que colocar el many=True, por defecto esta en False
        respuesta=self.get_serializer(self.get_queryset(),many=True)
        return Response({
            'ok': True,
            'content': respuesta.data,
            'message': None
        })
    
    def post (self, request):
        # print(request.data)
        respuesta=self.get_serializer(data=request.data)
        # print(respuesta.is_valid(raise_exception=True))
        if respuesta.is_valid(raise_exception=True):
            #con el save se hace el guardado a la BD
            respuesta.save()
            return Response({
                'ok':True,
                'content': respuesta.data,
                'message':'Se agrego el registro de manera exitosa'

            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                'ok':False,
                'content': None,
                'message':'Hubo un error al crear el registro de persona'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class PersonaView(RetrieveUpdateDestroyAPIView):
    serializer_class=PersonaSerializer
    queryset=PersonaModel.objects.all()
    def get(self,request, personaId):
        print(self.get_queryset().filter(perId=personaId))
        #El get devuelve todas las coincidencias de un modelo 
        #mediante un filtro que va como parametro indicando el atributo (la columna de la BD) y sy valor
        print(self.get_queryset().get(perId=personaId))
        print(self.get_queryset().filter(perId=personaId))
        respuesta=self.get_serializer(self.get_queryset().get(perId=personaId))
        #Una vez que muestra informacion ya ha sido serializada, simplemente
        #para obtener su ifnormacion en tipo de fdiccionario llamado a su atributi data
        #la cual almacena lo necesitado
        return Response({
            'Ok':True,
            'content': respuesta.data,
            'message': None
        })
    def put(self, request, personaId):
        respuesta = self.serializer_class(self.get_queryset().get(perId=personaId), data=request.data)
        if respuesta.is_valid(raise_exception=True):
            #resultado es un nuevo objeto actuaizado
            resultado = respuesta.update()
            return Response({
                'ok': True,
                'content': self.serializer_class(resultado).data,
                'message':''
            })
    def delete(self, request, personaId):
        respuesta = self.get_serializer(self.get_queryset().get(perId=personaId))
        resultado = respuesta.delete()
        return Response({
            'ok':True,
            'content': self.get_serializer(resultado).data,
            'message': 'Se inhabilito con éxito el registro persona'
            }, status=status.HTTP_200_OK)    

class AcademicosView(ListCreateAPIView):
    queryset = AcademicoModel.objects.all() #SELECT * FROM ACADEMICO
    serializer_class=AcademicoSerializer
    def get(self,request):
    #Cuando el queryset devuelve una lista se tiene que colocar el many=True, por defecto esta en False
        respuesta=self.get_serializer(self.get_queryset(),many=True)
        return Response({
            'ok': True,
            'content': respuesta.data,
            'message': None
        })
    
    def post (self, request):
        # print(request.data)
        respuesta=self.get_serializer(data=request.data)
        # print(respuesta.is_valid(raise_exception=True))
        if respuesta.is_valid(raise_exception=True):
            #con el save se hace el guardado a la BD
            respuesta.save()
            return Response({
                'ok':True,
                'content': respuesta.data,
                'message':'Se agrego el registro de manera exitosa'

            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                'ok':False,
                'content': None,
                'message':'Hubo un error al crear el registro academico'
            }, status=status.HTTP_400_BAD_REQUEST)

class AcademicoView(RetrieveUpdateDestroyAPIView):
    serializer_class=AcademicoSerializer
    queryset=AcademicoModel.objects.all()
    def get(self,request, academicoId):
        print(self.get_queryset().filter(acadId=academicoId))
        #El get devuelve todas las coincidencias de un modelo 
        #mediante un filtro que va como parametro indicando el atributo (la columna de la BD) y sy valor
        print(self.get_queryset().get(acadId=academicoId))
        print(self.get_queryset().filter(acadId=academicoId))
        respuesta=self.get_serializer(self.get_queryset().get(acadId=academicoId))
        #Una vez que muestra informacion ya ha sido serializada, simplemente
        #para obtener su ifnormacion en tipo de fdiccionario llamado a su atributi data
        #la cual almacena lo necesitado
        return Response({
            'Ok':True,
            'content': respuesta.data,
            'message': None
        })
    def put(self, request, laboralId):
        respuesta = self.serializer_class(self.get_queryset().get(labId=laboralId), data=request.data)
        if respuesta.is_valid(raise_exception=True):
            #resultado es un nuevo objeto actuaizado
            resultado = respuesta.update()
            return Response({
                'ok': True,
                'content': self.serializer_class(resultado).data,
                'message':''
            })
    def delete(self, request, academicoId):
        respuesta = self.get_serializer(self.get_queryset().get(acadId=academicoId))
        resultado = respuesta.delete()
        return Response({
            'ok':True,
            'content': self.get_serializer(resultado).data,
            'message': 'Se inhabilito con éxito el registro academico'
            }, status=status.HTTP_200_OK)  

class ConocimientosView(ListCreateAPIView):
    queryset = ConocimientoModel.objects.all() #SELECT * FROM CONOCIMIENTO
    serializer_class = ConocimientoSerializer
    def get(self,request):
    #Cuando el queryset devuelve una lista se tiene que colocar el many=True, por defecto esta en False
        respuesta=self.get_serializer(self.get_queryset(),many=True)
        return Response({
            'ok': True,
            'content': respuesta.data,
            'message': None
        })
    
    def post (self, request):
        # print(request.data)
        respuesta=self.get_serializer(data=request.data)
        # print(respuesta.is_valid(raise_exception=True))
        if respuesta.is_valid(raise_exception=True):
            #con el save se hace el guardado a la BD
            respuesta.save()
            return Response({
                'ok':True,
                'content': respuesta.data,
                'message':'Se agrego el registro de manera exitosa'

            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                'ok':False,
                'content': None,
                'message':'Hubo un error al crear el registro de conocimiento'
            }, status=status.HTTP_400_BAD_REQUEST)

class ConocimientoView(RetrieveUpdateDestroyAPIView):
    serializer_class = ConocimientoSerializer
    queryset = ConocimientoModel.objects.all()
    def get(self,request, conocimientoId):
        print(self.get_queryset().filter(conociId=conocimientoId))
        #El get devuelve todas las coincidencias de un modelo 
        #mediante un filtro que va como parametro indicando el atributo (la columna de la BD) y sy valor
        print(self.get_queryset().get(conociId=conocimientoId))
        print(self.get_queryset().filter(conociId=conocimientoId))
        respuesta=self.get_serializer(self.get_queryset().get(conociId=conocimientoId))
        #Una vez que muestra informacion ya ha sido serializada, simplemente
        #para obtener su ifnormacion en tipo de fdiccionario llamado a su atributi data
        #la cual almacena lo necesitado
        return Response({
            'Ok':True,
            'content': respuesta.data,
            'message': None
        })
    def put(self, request, conocimientoId):
        respuesta = self.serializer_class(self.get_queryset().get(conociId=conocimientoId), data=request.data)
        if respuesta.is_valid(raise_exception=True):
            #resultado es un nuevo objeto actuaizado
            resultado = respuesta.update()
            return Response({
                'ok': True,
                'content': self.serializer_class(resultado).data,
                'message':''
            })
    def delete(self, request, conocimientoId):
        respuesta = self.get_serializer(self.get_queryset().get(conociId=conocimientoId))
        resultado = respuesta.delete()
        return Response({
            'ok':True,
            'content': self.get_serializer(resultado).data,
            'message': 'Se inhabilito con éxito el registro conocimiento'
            }, status=status.HTTP_200_OK)

class HabilidadesView(ListCreateAPIView):
    queryset = HabilidadModel.objects.all() #SELECT * FROM HABILIDAD
    serializer_class = HabilidadSerializer
    def get(self,request):
    #Cuando el queryset devuelve una lista se tiene que colocar el many=True, por defecto esta en False
        respuesta=self.get_serializer(self.get_queryset(),many=True)
        return Response({
            'ok': True,
            'content': respuesta.data,
            'message': None
        })
    
    def post (self, request):
        # print(request.data)
        respuesta=self.get_serializer(data=request.data)
        # print(respuesta.is_valid(raise_exception=True))
        if respuesta.is_valid(raise_exception=True):
            #con el save se hace el guardado a la BD
            respuesta.save()
            return Response({
                'ok':True,
                'content': respuesta.data,
                'message':'Se agrego el registro de manera exitosa'

            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                'ok':False,
                'content': None,
                'message':'Hubo un error al crear el registro de habilidad'
            }, status=status.HTTP_400_BAD_REQUEST)

class HabilidadView(RetrieveUpdateDestroyAPIView):
    serializer_class = HabilidadSerializer
    queryset = HabilidadModel.objects.all()
    def get(self,request, habilidadId):
        print(self.get_queryset().filter(habId=habilidadId))
        #El get devuelve todas las coincidencias de un modelo 
        #mediante un filtro que va como parametro indicando el atributo (la columna de la BD) y sy valor
        print(self.get_queryset().get(habiId=habilidadId))
        print(self.get_queryset().filter(habiId=habilidadId))
        respuesta=self.get_serializer(self.get_queryset().get(habId=habilidadId))
        #Una vez que muestra informacion ya ha sido serializada, simplemente
        #para obtener su ifnormacion en tipo de fdiccionario llamado a su atributi data
        #la cual almacena lo necesitado
        return Response({
            'Ok':True,
            'content': respuesta.data,
            'message': None
        })
    def put(self, request, habilidadId):
        respuesta = self.serializer_class(self.get_queryset().get(habId=habilidadId), data=request.data)
        if respuesta.is_valid(raise_exception=True):
            #resultado es un nuevo objeto actuaizado
            resultado = respuesta.update()
            return Response({
                'ok': True,
                'content': self.serializer_class(resultado).data,
                'message':''
            })
    def delete(self, request, habilidadId):
        respuesta = self.get_serializer(self.get_queryset().get(habId=habilidadId))
        resultado = respuesta.delete()
        return Response({
            'ok':True,
            'content': self.get_serializer(resultado).data,
            'message': 'Se inhabilito con éxito el registro habilidad'
            }, status=status.HTTP_200_OK)

class HobbiesView(ListCreateAPIView):
    queryset = HobbieModel.objects.all() #SELECT * FROM HOBBIE
    serializer_class = HobbieSerializer
    def get(self,request):
    #Cuando el queryset devuelve una lista se tiene que colocar el many=True, por defecto esta en False
        respuesta=self.get_serializer(self.get_queryset(),many=True)
        return Response({
            'ok': True,
            'content': respuesta.data,
            'message': None
        })
    
    def post (self, request):
        # print(request.data)
        respuesta=self.get_serializer(data=request.data)
        # print(respuesta.is_valid(raise_exception=True))
        if respuesta.is_valid(raise_exception=True):
            #con el save se hace el guardado a la BD
            respuesta.save()
            return Response({
                'ok':True,
                'content': respuesta.data,
                'message':'Se agrego el registro de manera exitosa'

            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                'ok':False,
                'content': None,
                'message':'Hubo un error al crear el registro de hobbie'
            }, status=status.HTTP_400_BAD_REQUEST)

class HobbieView(RetrieveUpdateDestroyAPIView):
    serializer_class = HobbieSerializer
    queryset = HobbieModel.objects.all()
    def get(self,request, hobbieId):
        print(self.get_queryset().filter(hobId=hobbieId))
        #El get devuelve todas las coincidencias de un modelo 
        #mediante un filtro que va como parametro indicando el atributo (la columna de la BD) y sy valor
        print(self.get_queryset().get(hobId=hobbieId))
        print(self.get_queryset().filter(hobId=hobbieId))
        respuesta=self.get_serializer(self.get_queryset().get(hobId=hobbieId))
        #Una vez que muestra informacion ya ha sido serializada, simplemente
        #para obtener su ifnormacion en tipo de fdiccionario llamado a su atributi data
        #la cual almacena lo necesitado
        return Response({
            'Ok':True,
            'content': respuesta.data,
            'message': None
        })
    def put(self, request, hobbieId):
        respuesta = self.serializer_class(self.get_queryset().get(hobId=habilidadId), data=request.data)
        if respuesta.is_valid(raise_exception=True):
            #resultado es un nuevo objeto actuaizado
            resultado = respuesta.update()
            return Response({
                'ok': True,
                'content': self.serializer_class(resultado).data,
                'message':''
            })
    def delete(self, request, hobbieId):
        respuesta = self.get_serializer(self.get_queryset().get(hobId=hobbieId))
        resultado = respuesta.delete()
        return Response({
            'ok':True,
            'content': self.get_serializer(resultado).data,
            'message': 'Se inhabilito con éxito el registro hobbie'
            }, status=status.HTTP_200_OK)

class LaboralesView(ListCreateAPIView):
    queryset = LaboralModel.objects.all() #SELECT * FROM LABORAL
    serializer_class=LaboralSerializer
    def get(self,request):
    #Cuando el queryset devuelve una lista se tiene que colocar el many=True, por defecto esta en False
        respuesta=self.get_serializer(self.get_queryset(),many=True)
        return Response({
            'ok': True,
            'content': respuesta.data,
            'message': None
        })
    
    def post (self, request):
        # print(request.data)
        respuesta=self.get_serializer(data=request.data)
        # print(respuesta.is_valid(raise_exception=True))
        if respuesta.is_valid(raise_exception=True):
            #con el save se hace el guardado a la BD
            respuesta.save()
            return Response({
                'ok':True,
                'content': respuesta.data,
                'message':'Se agrego el registro de manera exitosa'

            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                'ok':False,
                'content': None,
                'message':'Hubo un error al crear el registro laboral'
            }, status=status.HTTP_400_BAD_REQUEST)

class LaboralView(RetrieveUpdateDestroyAPIView):
    serializer_class=LaboralSerializer
    queryset=LaboralModel.objects.all()
    def get(self,request, laboralId):
        print(self.get_queryset().filter(labId=laboralId))
        #El get devuelve todas las coincidencias de un modelo 
        #mediante un filtro que va como parametro indicando el atributo (la columna de la BD) y sy valor
        print(self.get_queryset().get(labId=laboralId))
        print(self.get_queryset().filter(labId=laboralId))
        respuesta=self.get_serializer(self.get_queryset().get(labId=laboralId))
        #Una vez que muestra informacion ya ha sido serializada, simplemente
        #para obtener su ifnormacion en tipo de fdiccionario llamado a su atributi data
        #la cual almacena lo necesitado
        return Response({
            'Ok':True,
            'content': respuesta.data,
            'message': None
        })
    def put(self, request, laboralId):
        respuesta = self.serializer_class(self.get_queryset().get(labId=laboralId), data=request.data)
        if respuesta.is_valid(raise_exception=True):
            #resultado es un nuevo objeto actuaizado
            resultado = respuesta.update()
            return Response({
                'ok': True,
                'content': self.serializer_class(resultado).data,
                'message':''
            })
    def delete(self, request, laboralId):
        respuesta = self.get_serializer(self.get_queryset().get(labId=laboralId))
        resultado = respuesta.delete()
        return Response({
            'ok':True,
            'content': self.get_serializer(resultado).data,
            'message': 'Se inhabilito con éxito el registro laboral'
            }, status=status.HTTP_200_OK)

#vistas de USUARIO
class RegistroView(CreateAPIView):
    queryset = Usuario.objects.all() #SELECT * FROM usuario
    serializer_class = UsuarioRegistroSerializer
    def get(self,request):
    #Cuando el queryset devuelve una lista se tiene que colocar el many=True, por defecto esta en False
        respuesta=self.get_serializer(self.get_queryset(),many=True)
        return Response({
            'ok': True,
            'content': respuesta.data,
            'message': None
        })

    def post(self, request):
        # VALIDAR SI YA HAY UN USUARIO CON ESE EMAIL
        correo = request.data.get('usuCorreo')
        # el filter devuelve una LISTA de todas las coincidencias y el get si no hay indicara un error
        usuarios = self.get_queryset().filter(usuCorreo=correo).first()
        if usuarios:
            return Response({
                'ok': False,
                'message':'El usuario con correo {} ya existe'.format(correo,)
            },status = status.HTTP_400_BAD_REQUEST)
        else:
            respuesta = self.get_serializer(data=request.data)
            if respuesta.is_valid(raise_exception=True):
                resultado = respuesta.save()
                return Response({
                    'ok': True,
                    'content': self.get_serializer(resultado).data,
                    'message':'Usuario creado exitosamente'
                }, status=201)
            else:
                return Response({
                    'ok': False,
                    'message': 'Data Incorrecta'
                }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializador = self.get_serializer(data=request.data)
        serializador.is_valid(raise_exception=True)
        return Response({
            'ok':True,
            'content':serializador.data
        })














