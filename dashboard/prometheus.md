# Ajouter repo prometheus-community
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Installer kube-prometheus-stack (Prometheus + Grafana)
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring --create-namespace

# Accéder à Grafana

kubectl get secret --namespace monitoring monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

[//]: # (------------)
# Resultat installation
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring --create-namespace
NAME: monitoring
LAST DEPLOYED: Sat Sep 27 21:28:47 2025
NAMESPACE: monitoring
STATUS: deployed
REVISION: 1
NOTES:
kube-prometheus-stack has been installed. Check its status by running:
kubectl --namespace monitoring get pods -l "release=monitoring"

Get Grafana 'admin' user password by running:

kubectl --namespace monitoring get secrets monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 -d ; echo

Access Grafana local instance:

export POD_NAME=$(kubectl --namespace monitoring get pod -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=monitoring" -oname)
kubectl --namespace monitoring port-forward $POD_NAME 3000

Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.

------------------

kubectl --namespace monitoring get secrets monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 -d ; echo
prom-operator
