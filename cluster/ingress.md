### Installer NGINX Ingress Controller avec Helm

```shell 
helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx \
--namespace ingress-nginx --create-namespace \
--set controller.replicaCount=2 \
--set controller.metrics.enabled=true \
--set controller.service.type=LoadBalancer \
--set controller.service.annotations."metallb\.universe\.tf/address-pool"=default
``` 

```shell 
kubectl -n ingress-nginx get pods -o wide
```

helm upgrade ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx \
--set controller.extraArgs.tcp-services-configmap="ingress-nginx/tcp-services"



yaml
spec:
containers:
- name: controller
image: k8s.gcr.io/ingress-nginx/controller:v1.10.0
args:
- /nginx-ingress-controller
- --tcp-services-configmap=ingress-nginx/tcp-services
# autres arguments...