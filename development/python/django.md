# Django
> Kind like ASP .Net MVC Framework; Comes w RouteControl, @admin vs user; DB mgr & ORM; ViewSet that can load from Model; Form can auto generate by model; api support; can addon multi tenant; Event attach to Model(signal)
## Structure
- /manager.py `entry point`
- /setting.py
- /urls.py `URL Route Register; appname is default_base_name, will overwritten by basename`
- /admin.py `Admin controller`
----
- /migration `alembic`
- /forms `Django build-in forms`
- /views `Django build-in ui components, EX: table, list`
- /models `ORM & permission control`
- /serializers `For api`
- /management
  - /commands `kind like npm run xxx, call by python3 manager.py xxxx`

## Cmds
```py
python3 manager.py runserver_plus
# [makemigrations, migrate, runserver, xxx]
```
## Model
```py
# Google how to override to define fields, read_only_fields, attach event handler
from rest_framework.serializers import ModelSerializer


# attach event to Model
# https://docs.djangoproject.com/en/4.0/ref/signals/
from django.db.models.signals import pre_init, post_delete, post_save
from django.dispatch import receiver
@receiver(pre_init, sender=xxxModel)

# similar formik dirty
instance.data_change('xyz')
```

## Controller
```py
# app.route('/xxx', xxx_funct)
path('/xxx', view)
# app.register('/xxx', xxx_app, prefix='xxx')
path('xxx', include('xxx.urls'))

# django-tenants uses second_level_domain & postgres schema to implement permission control
with schema_context('public'):
    pass

from django.contrib.auth.models import Group, Permission
```
## View
```py
# Add Django Form into Admin page
@admin.register(xxxModel)

# Add custom model to Django 
admin.site.register(django.db.models)

# model.FileField(validators=[])

# ViewSet defined what Model, which records, which properties shows on form & default values  
```

## Django Apps | Addons | Plugin
### Django REST framework
> Authentication policies, 

### Django-cors-headers

### sentry
> Runtime Error Tracking; sentry.io is paid version
### Django GUID
### Cookiecutter
