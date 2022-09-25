# Django REST framework (DRF)
> DRF parses HttpRequest header & body into Python Dict; Uses Serializer to convert into different formats;
> Authentication policies, Auto create OpenAPI endpoint from Model
> Attach API by `path('/api', include('rest_framework.urls'))`
> `drf_spectacular` auto generate openapi documentation

- Router
- View
  - ViewSet
    - serializer_class
    - permission_classes
    - authentication_classes
    - filter_backends
  - GenericViewSet
    - get_object()
    - get_queryset()
  - ModelViewSet
    - list()
    - retrieve()
    - create()
    - destroy()
- Parsers & Render & Pagination
- `DEFAULT_PERMISSION_CLASSES` triggers by
  - View.get_object() -> .check_object_permissions(request, obj)


## GenericViewSet
```py
def get_object()
def get_queryset()
```
## ModelViewSet
```py
# Default methods
def list(self, request):
def create(self, request):
def retrieve(self, request, pk=None):
def update(self, request, pk=None):
def partial_update(self, request, pk=None):
def destroy(self, request, pk=None):
def perform_create()
def perform_update()
def perform_destroy()
```

## Serializer
```py
# Google how to override to define fields, read_only_fields, attach event handler
from rest_framework.serializers import ModelSerializer
xyz = SerializerMethodField()
def get_xyz():
  return 1

xxx = xxxSerializer(date={}, initial_data={}, validated_data={})
xxx.is_valid()
xxx.errors
xxx.data
xxx.validated_data
xxx._writeable_fields
```

# Django Addons / Apps
## Permission
- django-guardian
- drf-access-policy
- django-rules `In memory`
> `predicate` is function enforce permission logic
> 
> `Meta.rules_permissions = { 'xyz', is_admin }`
```
```


### Django-cors-headers

### sentry
> Runtime Error Tracking; sentry.io is paid version
### Django GUID
### Cookiecutter


### djangorestframework-version-transforms
> 1. by header param `Accept: version=1`
> 2. by url path `r'?(?P<pk>[0-9]+)/$'`


# Testing
```bash
# must install to test django
pip install pytest-django
```
## Factory-Boy
unit test tool, similar to fixture