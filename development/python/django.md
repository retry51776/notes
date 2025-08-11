# Django

> Like ASP.NET MVC, Django follows a Model‑View‑Template (MVT) pattern.  
> It provides many built‑in features:

- URL routing
- Admin panel
- User and permission management
- Database ORM
- ViewSets and forms generated from models
- Signals for model and request events

> Static file handling is not ideal; consider using S3 or WhiteNoise.

## ORM Quirks

- Queries use double‑underscore lookups, e.g., `entry__field__gt=5`.
- Slicing like `Entry.objects.all()[-1]` is unsupported.
- Ordering uses strings: `.order_by('-rating')`; there are no `.asc()`/`.desc()` helpers.

## Companies Using Django

- Pinterest
- Instagram
- Dropbox
- YouTube

## Typical Workflow

1. **urls.py** – define routes.
2. **ViewSet** (controller) – decides which records to expose, how to serialize them, and who can see what.
   - Models define permissions.
3. Templates render the UI.

## Project Structure

```
/manage.py          # Entry point
/settings.py        # Configuration
/urls.py            # URL registration; app name defaults to `base_name` but can be overridden with `basename`.
/admin.py           # Admin panel definitions
/migrations/        # Database migrations (similar to Alembic)
/forms/             # Django form classes
/views/             # View functions / class‑based views
/models/            # ORM models and permission logic
/serializers/       # DRF serializers for APIs
/management/
    commands/       # Custom management commands (`python manage.py mycommand`)
```

## Core Components

### Settings, Requests & Middleware

- `Middleware` processes requests/responses.
- Deserialization/serialization of request data.

### Views

- **Serializers** – convert model instances to JSON and vice‑versa.
- **View classes / functions**
  - Pagination
  - Permissions

### Models & Migrations

- Model meta options: <https://docs.djangoproject.com/en/4.1/ref/models/options/>
  - `permissions`
- ORM lookups use the `__` syntax (`field__lt=14`).
- File handling with `django.core.files.File`.
- Signals for model events.

### Forms & Templates

- Template tags resemble PHP tags.
- Inheritance and inclusion mechanisms.

### Miscellaneous Utilities

- Email: `django.core.mail`
- Security features (CSRF, SSL, host validation)
- Built‑in user, site, and group models.

## Management Commands (`manage.py`)

```python
# List all commands
django-admin
python3 manage.py runserver_plus   # Development server with extra features

# Common commands:
# makemigrations, showmigrations, migrate,
# runserver, collectstatic, createsuperuser, shell_plus, etc.
```

## Models

> Attach common logic as methods (`def get_xyz(self): ...`).  
> Polymorphic models allow a single table to represent multiple Python classes.

- `Model.objects` is the manager; you can subclass it for custom querysets.
- Common queryset methods:
  - `.all()`, `.filter(...)`, `.exclude(...)`
  - `.update_or_create(defaults={})`
  - `.get_or_create() → (instance, created)`
  - `.annotate(total=Sum('field'))`

### Example Model Snippet

```python
from django.db import models
from django.db.models.signals import pre_init, post_delete, post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100, null=True, choices=[('a', 'A'), ('b', 'B')])
    file = models.FileField(validators=[])

    class Meta:
        permissions = [
            ("can_publish", "Can publish items"),
        ]

# Signals
@receiver(pre_init, sender=MyModel)
def mymodel_pre_init(sender, **kwargs):
    ...

post_save.connect(my_handler, sender=MyModel)

def my_handler(sender, instance, created, **kwargs):
    if created:
        instance.xyz = False
```

### Relationships

```python
# ForeignKey example
user = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,   # Options: CASCADE, SET_DEFAULT, PROTECT, RESTRICT
    blank=True,
    null=True,
)

# Reverse relation
entries = user.my_model_set.all()
entries.add(new_obj)
entries.create(...)
entries.remove(old_obj)
entries.clear()
entries.set([obj1.id, obj2.id])
```

### Query Ordering

```python
MyModel.objects.all().order_by("-amount")
```

## Views (Class‑Based & Function‑Based)

> In MVC terms, the controller consists of `urls.py` and view classes/functions.

### ViewSet Key Methods

- `_fetch_all()`
- `get_queryset()`
- HTTP verbs: `get()`, `post()`, etc.
- CRUD actions: `list()`, `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()`

```python
# URL routing examples
path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}))
path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve',
                                            'put': 'update',
                                            'delete': 'destroy'}))

# Adding custom actions
@action(detail=True, methods=["GET"], permission_classes=[])
def set_password(self, request):
    ...
```

### Template Basics

```django
{% extends "base.html" %}
{% include "navbar.html" %}

{% block content %}
  <h1>{{ title }}</h1>
{% endblock %}
```

#### Mixin Lifecycle (simplified)

`setup() → dispatch() → http_method_not_allowed() → options()`

#### FormView Workflow

1. `get_context_data()`
2. `get_form_class()`
3. `get_form_kwargs()`
4. `get_success_url()`
5. `form_valid()`
6. `form_invalid()`
7. `post()`

```python
# Register a model with the admin site
@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
```

## Signals

> Typically attached to models, but can also listen for request‑level events.

## Permissions

- Documentation: <https://docs.djangoproject.com/en/4.0/topics/auth/default/>
- Each model automatically gets four CRUD permissions.
- Permissions can be grouped into **Groups**.
- Three user categories: superuser, staff, regular active users.

### Enforcing Permissions

- Mixin: `PermissionRequiredMixin` with `permission_required = 'app.change_model'`
- Decorator: `@login_required`
- Manual checks inside view logic
- Middleware for global enforcement

