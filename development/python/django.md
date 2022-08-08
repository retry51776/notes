# Django
> Kind like ASP .Net MVC Framework, Django uses Model View Template(MVT); Comes w RouteControl, @admin vs user; DB mgr & ORM; ViewSet & Form that generated from Model; Model Event & Request Event(signal); Build-in Admin Panel;

> not good at static file, through S3 or whitenoise

## Company
- Pinterest
- Instagram
- Dropbox
- Youtube
## Workflow
1. urls.py `route`
2. ViewSet `aka controller: What record, how to serialize, who can see Mixin; which form/template`
3. Model `permission`

## Structure
- /manager.py `entry point`
- /setting.py
- /urls.py `URL Route Register; appname is default_base_name, will overwritten by basename; so {% url 'xxx' %} can reference url`
- /admin.py `what shows up in Admin Panel`
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
# [makemigrations, migrate, runserver, collectstatic, xxx, createsuperuser]
```
## Model
```py
# Google how to override to define fields, read_only_fields, attach event handler
from rest_framework.serializers import ModelSerializer


# attach event to Model; Kind like redux
# https://docs.djangoproject.com/en/4.0/ref/signals/
from django.db.models.signals import pre_init, post_delete, post_save
from django.dispatch import receiver
# hook up by decorator
@receiver(pre_init, sender=xxxModel)

# hook up manually
post_save.connect(handler_func, sender=xxModel)

def handler_func(sender, instance, created, **kwargs):
  if created:
    instance.xyz = False

# similar formik dirty
instance.data_change('xyz')
model.FileField(validators=[])

# https://docs.djangoproject.com/en/4.0/ref/models/relations/
entries = b.xxx_set.all()
.add()
.create()
.remove()
.clear()
.set(id=123)

# Model Relation
user = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,# CASCADE, SET_DEFAULT,
    blank=True,
    null=True,
)
# PROTECT / RESTRICT prevent parent delete
# SET_NULL is set parent foreign key null
# CASCADE delete with parent
```

## View
> In typical MVC model, Controller in django includes (urls.py, ViewSet)

> Class Base View (CBV) `overwrite life cycle event to enforce permission & control; class will auto implement a lot simple ops, but do more complex ops requires read doc`
> Function Base View (FBV) `you got to hook up everything`
```py
# app.route('/xxx', xxx_funct)
path('/xxx', view)
# app.register('/xxx', xxx_app, prefix='xxx')
path('xxx', include('xxx.urls'))

# django-tenants uses second_level_domain & postgres schema to implement permission control
with schema_context('public'):
    pass

from django.contrib.auth.models import Group, Permission
# Within ViewSet
if (xxx) {
  redirect('/login')
}

# Must meet at least one permission
@admin.action(
  permissions=['change', 'create'],
  description='Mark selected stories as published',
)

from django.view import View
class xx(View):
  def get(self, request):
    return render(request, xyzView, { 'xxx': 99 })
  def post():
    pass
```

## Template
> I consider /templates /forms these are V in MVC;
> even /templates have a little Controller capability
```py
{% extends 'xxx.html' %}
{% include 'xxx.html' %}
{% block 'xxx.html' %}
  <h1>{{ xyz }}</h1>
{% endblock %}
```
> FormModel
> Template Tag `aka php tag inside html`
> Template Inheriting
> Template Including
> Template Block

### Mixin workflow
`setup() -> dispatch() -> http_method_not_allowed() -> options()`

### FormView workflow
1. `get_context_data()` 
2. `get_form_class()`
3. `get_form_kwargs()`
4. `get_success_url()`
5. `form_valid()`
6. `form_invalid()` 
7. `post()`
```py

# Add Django Form into Admin Panel
@admin.register(xxxModel)

# Add custom model to Django 
admin.site.register(django.db.models)

# ViewSet defined what Model, Serializer, which records, which properties shows on form & default values

# APIView is rest_framework.views template
csrfmiddlewaretoken: $('input[name=csrfmiddletoken]').val()
```

## Signal
> Usually attach to Model, but also can attach to Request

## Permission
> https://docs.djangoproject.com/en/4.0/topics/auth/default/
each Model generated 4 CRUD permissions

Permission can group into Group

3 types auth_users: [super_user, staff_user, active_user]

permission enforcement:
- inherit PermissionRequiredMixin `permission_required = 'xxx.change_xxx'`
- by decorator `@login_required`
- redirect within ViewController
- by middleware
## Django Apps | Addons | Plugin
### Django REST framework (DRF)
> Authentication policies, Auto create OpenAPI endpoint from Model
> Attach API by `path('/api', include('rest_framework.urls'))`

### Django-cors-headers

### sentry
> Runtime Error Tracking; sentry.io is paid version
### Django GUID
### Cookiecutter
