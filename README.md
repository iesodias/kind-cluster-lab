# How to configure Ingress on Kind

### Configurar hosts:

Add an entry to /etc/hosts with the IP address found that looks like:

```
C:\Windows\System32\drivers\etc #Windows

/etc/hosts  #Linux
```

```
127.0.0.1 kubernetes.docker.internal
```

Then create a kind cluster using this config file via:

```
kind create cluster --config=kind.yaml
```

Create a ingress namespace

```
kubectl create ns ingress-nginx
```

Helm Upgrade using this annotations:

```
helm upgrade -i ingress-nginx ingress-nginx/ingress-nginx \
--namespace ingress-nginx \
--set controller.metrics.enabled=true \
--set controller.podAnnotations."prometheus\.io/scrape"=true \
--set controller.podAnnotations."prometheus\.io/port"=10254
```

Deploy the nginx-ingress controller:

```
kubectl apply --filename https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml
```


Time zone ref

```
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
```

### Ref:
- https://dustinspecker.com/posts/test-ingress-in-kind/
- https://docs.flagger.app/tutorials/nginx-progressive-delivery
- https://devopstales.github.io/home/flagger-nginx-canary-deployments/