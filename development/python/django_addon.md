# Django REST framework (DRF)

> DRF parses the `HttpRequest` header and body into a Python dict. It uses serializers to convert data into different formats.
>
> Features include authentication policies, automatic OpenAPI endpoint generation from models, and easy API attachment via  
> `path('/api', include('rest_framework.urls'))`.
>
> `drf_spectacular` can automatically generate OpenAPI documentation.

## Core Concepts

- **Router**
- **View**
  - **ViewSet**
    - `serializer_class`
    - `permission_classes`
    - `authentication_classes`
    - `filter_backends`
  - **GenericViewSet**
    - `get_object()`
    - `get_queryset()`
  - **ModelViewSet**
    - `list()`
    - `retrieve()`
    - `create()`
    - `destroy()`
- **Parsers, Renderers & Pagination**
- `DEFAULT_PERMISSION_CLASSES` are triggered by  
  `View.get_object()` → `.check_object_permissions(request, obj)`

## GenericViewSet

```python
def get_object(self):
    ...

def get_queryset(self):
    ...
```

## ModelViewSet (default methods)

```python
# List objects
def list(self, request):
    ...

# Create a new object
def create(self, request):
    ...

# Retrieve a single object
def retrieve(self, request, pk=None):
    ...

# Update an existing object
def update(self, request, pk=None):
    ...

# Partially update an object
def partial_update(self, request, pk=None):
    ...

# Delete an object
def destroy(self, request, pk=None):
    ...

# Hooks that can be overridden
def perform_create(self, serializer):
    ...

def perform_update(self, serializer):
    ...

def perform_destroy(self, instance):
    ...
```

## Serializer

```python
# To override fields, read‑only fields, or attach event handlers,
# consult the DRF documentation.
from rest_framework.serializers import ModelSerializer, SerializerMethodField

class MyModelSerializer(ModelSerializer):
    xyz = SerializerMethodField()

    def get_xyz(self, obj):
        return 1

# Usage example
serializer = MyModelSerializer(data={}, initial_data={}, validated_data={})
if serializer.is_valid():
    # Access serialized data
    print(serializer.data)
else:
    print(serializer.errors)

# Internal attributes
print(serializer._writable_fields)   # Note: this is a protected attribute.
```

## Django Add‑ons / Apps

### Permission Packages

- **django-guardian**
- **drf-access-policy**
- **django-rules** (in‑memory)
  > A *predicate* is a function that enforces permission logic.  
  > Example: `Meta.rules_permissions = { 'xyz', is_admin }`

### Other Useful Packages

- **django-cors-headers**
- **sentry-sdk** – runtime error tracking (paid version on Sentry.io)
- **django-guid**
- **cookiecutter-django**

### Versioning Strategies (`djangorestframework-version-transforms`)

1. By header parameter: `Accept: version=1`
2. By URL path, e.g., `r'(?P<pk>[0-9]+)/$'`

## Testing

```bash
# Install the Django test utilities
pip install pytest-django
```

### Factory‑Boy

A factory library for creating test objects, similar to fixtures.

