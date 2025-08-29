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
