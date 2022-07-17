# Helm
> Helm is package manager for k8, also templating Engines
> 
> Helm < 2.0 Client / Sever (Tiller) since 3.0 No more Tiller

## Helm CMDs
```bash
# By default Helm don't have public repo(unlike npm or pip)
helm repo add stable https://charts.helm.sh/stable
helm repo add traefik https://helm.tra
efik.io/traefik
helm repo update

# You got to check source chart yourself
helm show chart traefik/traefik
helm dependency list xxx

# Install chart with different values has 2 ways(value.yml or --set xxx=123)
helm install --values=xxx.yaml chart_name --namespace [kube-system]
helm install traefik traefik/traefik --set dashboard.enabled=true,serviceType=LoadBalancer,rbac.enabled=true,dashboard.domain=traefik.local
helm uninstall xxx

# Repo Operations
helm template Release1 helm-charts
helm search xxx
helm search repo xxx
helm search hub xxx

# Chart Operations
helm create xxx
helm package xxx

```
## Helm Structure
```
/helm-charts
  /charts
  /templates (what k8 objects creates)
  .values.yaml (k8 values)
  .Chart.yaml (chart meta info)
{{ include "helm-cahrts.labels" . | nindent 4 }}
{{ .Values.service.name | qoute }}

// - remove line space
test:
  {{- .Release.Name }}

{{- toYaml .Values.xxx | nindent 8 }}

```