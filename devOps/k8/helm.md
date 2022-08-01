# Helm
> Helm is package manager for k8s
> 
> Helm < 2.0 Client / Sever (Tiller) since 3.0 No more Tiller
> 
> The biggest feature helm is uninstall & rollback
> 
> (Go template language)[https://pkg.go.dev/text/template]
> 
> (YAML)[https://helm.sh/docs/chart_template_guide/yaml_techniques/]
## Helm CMDs
```bash
brew install helm
brew install kustomize
brew install chart-testing
# Helm's unitest tool
helm plugin install https://github.com/lrills/helm-unittest

# By default Helm don't have public repo(unlike npm or pip)
helm repo add stable https://charts.helm.sh/stable
helm repo add traefik https://helm.tra
efik.io/traefik
helm repo update

# You got to check source chart yourself
helm show chart traefik/traefik
helm dependency list xxx

# Install chart with different values has 2 ways(value.yml or --set xxx=123)
1. create chart folder
2. helm pull & check code
3. create xxx-config.yml
4. helm install --values=xxx-config.yaml xxx xxx

# pull chart zip
helm pull traefik/traefik
helm install --values=xxx.yaml chart_name --namespace [kube-system]
helm install traefik traefik/traefik --set dashboard.enabled=true,serviceType=LoadBalancer,rbac.enabled=true,dashboard.domain=traefik.local
helm uninstall xxx

# Repo Operations
helm template Release1 helm-charts
helm search xxx
helm search repo xxx
helm search hub xxx

# Chart Operations
# View chart
helm template --debug <chart_name>
helm install --dry-run measly-whippet ./mychart
helm install --dry-run --disable-openapi-validation measly-whippet ./mychart
helm test <RELEASE_NAME>
helm create xx
helm package xxx

```
## Helm Structure
> example https://github.com/traefik/traefik-helm-chart/blob/master/traefik/
```
/helm-charts
  /charts
  /templates (what k8 objects creates)
    /_helpers.tpl (define common properties)
    /NOTES.txt (docstring)
    /tests (helm test xxx)
  .values.yaml (k8 values)
  .Chart.yaml (chart meta info)

/templates/_helpers.tpl
{{- define "xxx.label" }}
{{- end }}

//templates/xxx_deployment
{{- template "xxx.label"}}
```

## Helm workflow control & reference
> This remind me php programming
> 
```bash
// - remove line space
test:
  {{- .Release.Name }}

{{- toYaml .Values.xxx | nindent 8 }}
{{ include "helm-cahrts.labels" . | nindent 4 }}
{{ .Values.service.name | default "10m" | qoute }}

  toppings: |-
    {{- range $.Values.pizzaToppings }}
    - {{ . | title | quote }}
    {{- end }}    
  {{- end }}

{{- with .Values.xx.xxx.xxxx }}
    grand_chile: yy
    root_xx: {{ $.Values.xx }}
{{- end}}

{{ range $index, $service := (lookup "v1" "Service" "mynamespace" "").items }}
    {{/* do something with each service */}}
{{ end }}

operators (eq, ne, lt, gt, and, or and so on)

data:
  {{- $files := .Files }}
  {{- range tuple "config1.toml" "config2.toml" "config3.toml" }}
  {{ . }}: |-
        {{ $files.Get . }}
  {{- end }}
```
