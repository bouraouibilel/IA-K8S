## MetalLB (Services LoadBalancer on‑prem)

### Installer MetalLB

```shell
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.12/config/manifests/metallb-native.yaml
```

### Pool d’adresses & annonce L2

[Voir le fichier metallb-ipaddresspool.yaml](./metallb-ipaddresspool.yaml)

