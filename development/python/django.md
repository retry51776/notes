# Django
> Kind like ASP .Net MVC Framework, Django uses Model View Template(MVT); 
> 
> Build-in features:
- RouteControl
- Admin Panel
- User & Permission Mgr
- DB mgr & ORM Model
- ViewSet & Form that generated from Model
- Signal `Model Event & Request Event`

> not good at static file, through S3 or whitenoise

> Django ORM is weird
- why can't they uses operator like normal `entry__xField__operator`; `xRelationship__childField__operator`;
- `Entry.objects.all()[-1]` not support;
- `.order_by('-rating')` why not `.asc()` or `.desc()`


## Company
- Pinterest
- Instagram
- Dropbox
- Youtube

## Workflow
1. urls.py `route`
2. ViewSet `aka controller: What record, how to serialize, who can see Mixin; which form/template`
   1. Model `permission`
3. Template

## Folder Structure
- /manager.py `entry point`
- /setting.py
- /urls.py `URL Route Register; appname is default_base_name, will overwritten by basename; so {% url 'xxx' param1 %} can reference url`
- /admin.py `what shows up in Admin Panel`
----Folders------
- /migration `alembic`
- /forms `Django build-in forms`
- /views `Django build-in ui components, EX: table, list`
- /models `ORM & permission control`
- /serializers `For api`
- /management
  - /commands `kind like npm run xxx, call by python3 manager.py xxxx`

# Django Components
- Setting
- Http Request
  - Middleware
  - Deserialize & Serialize Request
- View
  - Serializer
  - View (decorator or class)
    - Pagination
- Model & DB Migrations
  - Model Meta options https://docs.djangoproject.com/en/4.1/ref/models/options/
    - permissions
  - orm weird syntax `__pk implies __id__exact; fieldName__lt=14`
  - `django.core.files.File`
  - lookups
- Form & Template
- Others
  - `django.core.mail`
  - security
    - hostname, CSRF, SSL
    - Default Django User, Sites, Groups
  - Signals

## Cmds
```py
# List all cmds
django-admin
python3 manager.py runserver_plus
# [makemigrations, migrate, runserver, collectstatic, xxx, createsuperuser, shell_plus]
```
## Model
> attach common logic to Model as methods `get_xyz()`

- `Model.objects.all()`
- `Model.save()`
- `Model.delete()`
- `Field.contribute_to_class()` Field adds descriptor,
- `Field.contribute_to_related_class` adds descriptor to nested Model
- `Field.view_perm_name` = rules_permissions.key; used by descriptor to enforce which rules_permissions
- Meta
```py
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
# FloatField, DateTimeField
model.CharField(null=True, choices=[('a', 'a'), ('b', 'b')])
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

# QuerySet reverse order
XXX.objects.all().order_by("-amount")
# Many to Many double __ .filter(xxx__yy="zz")
```
## View
> In typical MVC model, Controller in django includes (urls.py, ViewSet)

> Class Base View (CBV) `overwrite life cycle event to enforce permission & control; class will auto implement a lot simple ops, but do more complex ops requires read doc`
> > default route `list, create, retrieve, update, partial_update, destroy`
> Function Base View (FBV) `you got to hook up everything`

### ViewSet Key methods
- QuerySet._fetch_all() 
- get_queryset()
- get()
- post()
- list()
- create()
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

# add sub method into ViewSet EX:/user/123/set_password
@action(detail=True, method=["GET"], permission_classes=[])
def set_password(self, request)

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