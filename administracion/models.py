from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
# AbstractBaseUser, permite modificar todo las tabal de usuario
# AbstractUser, perimite solo modificar algunos campos de la tabla usuario
class ManejoUsuario(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, usuCorreo, usuNombre, usuFono, usuPass, **extra_fields):
        values = [usuCorreo, usuFono, usuNombre]
        # Genera un diccionario de datos {"nombre:"Eduardo",...}
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError("El valor de {} debe estar definido".format(field_name))
        #nomalaize, verifica que el correo haya sido correctamente ingresado @ y .
        usuCorreo = self.normalize_email(usuCorreo)
        user = self.model(
            usuCorreo = usuCorreo,
            usuNombre=usuNombre,
            usuFono=usuFono,
            **extra_fields
        )
        user.set_password(usuPass)
        user.save(using=self._db)
        return user

    def create_user(self, usuCorreo, usuNombre, usuFono, usuPass=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(usuCorreo, usuNombre, usuFono, usuPass, **extra_fields)
    
    def create_superuser(self,  usuCorreo, usuNombre, usuFono, usuPass, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El super usuario debe de ser staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El super usuario debe de ser superusuario')
        return self._create_user( usuCorreo, usuNombre, usuFono, usuPass, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    usuId = models.AutoField(db_column='usu_id', primary_key=True)
    usuCorreo = models.EmailField(db_column='usu_correo', unique=True, verbose_name='Correo')
    usuNombre = models.CharField(db_column='usu_nombre', max_length=50)
    usuFono = models.CharField(db_column='usu_fono', max_length=15)
    usuCumple = models.DateField(db_column='usu_cumple', blank=True, null=True)
    password = models.TextField(db_column='usu_pass', null=True)
    # CAMPOS OBLIGATORIAMENTE EN INGLES y si o si tienen que ir
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = ManejoUsuario()

    USERNAME_FIELD = 'usuCorreo'
    REQUIRED_FIELDS = ['usuNombre','usuFono']
    
    def tokens(self):
        tokens = RefreshToken.for_user(self)
        return {
            'acceso': str(tokens.access_token),
            'refresh': str(tokens)
        }
    class Meta:
        db_table = 't_usuario'

# Create your models here.
class PersonaModel(models.Model):
    # Definir todos los atributos de nuestra tabla
    # Si no definimos la PK, django automaticamente va a crear una columna llamada ID y obviamente va a ser un integer, auto_increment, not_null, primary_key
    perId = models.AutoField(db_column='per_id',primary_key=True, null=False, unique=True)
    perDni = models.CharField(db_column='per_dni', max_length=8)
    perNombres = models.CharField(db_column='per_nombres', max_length=50)
    perApellidos = models.CharField(db_column='per_apellidos', max_length=50)
    perFecnac = models.DateField(db_column='per_fecnac')
    perSexo = models.CharField(db_column='per_sexo', max_length=1)
    perCorreo = models.CharField(db_column='per_correo', max_length=20)
    perCelular = models.CharField(db_column='per_celular', max_length=15)
    perObservacion = models.CharField(db_column='per_observacion', max_length=100)        
    
    # Campos para auditoria
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 't_persona'

class LaboralModel(models.Model):
    # Si no definimos la PK, django automaticamente va a crear una columna llamada ID y obviamente va a ser un integer, auto_increment, not_null, primary_key
    labId = models.AutoField(db_column='lab_id',primary_key=True, null=False, unique=True)    
    labEmpresa = models.CharField(db_column='lab_empresa', max_length=50)
    labCargo = models.CharField(db_column='lab_cargo', max_length=50)
    labFecini = models.DateField(db_column='lab_fecini')
    labFecfin = models.DateField(db_column='lab_fecfin')
    labContacnombre = models.CharField(db_column='lab_contacnombre', max_length=50)
    labContaccelular = models.CharField(db_column='lab_contaccelular',max_length=15)    
    labObservacion = models.CharField(db_column='lab_observacion', max_length=100)        
    perId = models.ForeignKey(PersonaModel, on_delete=models.PROTECT, db_column='per_id', related_name='laboralesPersona')
    
    # Campos para auditoria
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 't_laboral'

class HobbieModel(models.Model):
    # Si no definimos la PK, django automaticamente va a crear una columna llamada ID y obviamente va a ser un integer, auto_increment, not_null, primary_key
    hobId = models.AutoField(db_column='hob_id',primary_key=True, null=False, unique=True)    
    hobDescripcion = models.CharField(db_column='hob_descripcion', max_length=50)    
    hobObservacion = models.CharField(db_column='hob_observacion', max_length=100)        
    perId = models.ForeignKey(PersonaModel, on_delete=models.PROTECT, db_column='per_id', related_name='hobbiesPersona')
    
    # Campos para auditoria
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 't_hobbie'

class HabilidadModel(models.Model):
    # Si no definimos la PK, django automaticamente va a crear una columna llamada ID y obviamente va a ser un integer, auto_increment, not_null, primary_key
    habId = models.AutoField(db_column='hab_id',primary_key=True, null=False, unique=True)    
    habDescripcion = models.CharField(db_column='hab_descripcion', max_length=50)    
    habObservacion = models.CharField(db_column='hab_observacion', max_length=100)        
    perId = models.ForeignKey(PersonaModel, on_delete=models.PROTECT, db_column='per_id', related_name='habilidadesPersona')
    
    # Campos para auditoria
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 't_habilidad'


class AcademicoModel(models.Model):
    # Si no definimos la PK, django automaticamente va a crear una columna llamada ID y obviamente va a ser un integer, auto_increment, not_null, primary_key
    acadId = models.AutoField(db_column='acad_id',primary_key=True, null=False, unique=True)    
    acadNivel = models.CharField(db_column='acad_nivel', max_length=50)
    acadCestudios = models.CharField(db_column='acad_cestudios', max_length=50)
    acadCarrera = models.CharField(db_column='acad_carrera', max_length=50)    
    acadObservacion = models.CharField(db_column='acad_observacion', max_length=100)        
    perId = models.ForeignKey(PersonaModel, on_delete=models.PROTECT, db_column='per_id', related_name='academicosPersona')
    
    # Campos para auditoria
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 't_academico'

class ConocimientoModel(models.Model):
    # Si no definimos la PK, django automaticamente va a crear una columna llamada ID y obviamente va a ser un integer, auto_increment, not_null, primary_key
    conociId = models.AutoField(db_column='conoci_id',primary_key=True, null=False, unique=True)    
    conociDescripcion = models.CharField(db_column='conoci_descripcion', max_length=50)    
    conociFecini = models.DateField(db_column='conoci_fecini')
    conociFecfin = models.DateField(db_column='conoci_fecfin')
    conociCestudios = models.CharField(db_column='conoci_cestudios', max_length=50)
    conociHoras = models.CharField(db_column='conoci_horas', max_length=50)    
    conociObservacion = models.CharField(db_column='conoci_observacion', max_length=100)        
    perId = models.ForeignKey(PersonaModel, on_delete=models.PROTECT, db_column='per_id', related_name='conocimientosPersona')
    
    # Campos para auditoria
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 't_conocimiento'


