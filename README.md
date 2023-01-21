# How to configure Ingress on Kind

- Configurar hosts:
```
C:\Windows\System32\drivers\etc
/etc/hosts
```

127.0.0.1 kubernetes.docker.internal

Ref:

https://dustinspecker.com/posts/test-ingress-in-kind/

https://docs.flagger.app/tutorials/nginx-progressive-delivery

https://devopstales.github.io/home/flagger-nginx-canary-deployments/

kind create cluster --config=kind.yaml

kubectl create ns ingress-nginx

helm upgrade -i ingress-nginx ingress-nginx/ingress-nginx \
--namespace ingress-nginx \
--set controller.metrics.enabled=true \
--set controller.podAnnotations."prometheus\.io/scrape"=true \
--set controller.podAnnotations."prometheus\.io/port"=10254

kubectl apply --filename https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml

helm upgrade -i flagger flagger/flagger \
--namespace ingress-nginx \
--set prometheus.install=true \
--set meshProvider=nginx

kubectl create ns test

kubectl apply -k https://github.com/fluxcd/flagger//kustomize/podinfo?ref=main

helm upgrade -i flagger-loadtester flagger/loadtester --namespace=test

k apply -f canary

kubectl -n test set image deployment/podinfo podinfod=ghcr.io/stefanprodan/podinfo:6.0.1