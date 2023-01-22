# How to configure Ingress on Kind

### Configurar hosts:
```
C:\Windows\System32\drivers\etc
/etc/hosts
```

```
127.0.0.1 kubernetes.docker.internal
```


```
kind create cluster --config=kind.yaml
```


```
kubectl create ns ingress-nginx
```


```
helm upgrade -i ingress-nginx ingress-nginx/ingress-nginx \
--namespace ingress-nginx \
--set controller.metrics.enabled=true \
--set controller.podAnnotations."prometheus\.io/scrape"=true \
--set controller.podAnnotations."prometheus\.io/port"=10254
```

```
kubectl apply --filename https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml
```


Time zone
```
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
```

### Ref:
- https://dustinspecker.com/posts/test-ingress-in-kind/
- https://docs.flagger.app/tutorials/nginx-progressive-delivery
- https://devopstales.github.io/home/flagger-nginx-canary-deployments/