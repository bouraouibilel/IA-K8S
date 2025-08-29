### Installation de Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
###  test de l'installation
helm version

###  Ajouter le dépôt KubeAI

helm repo add kubeai https://www.kubeai.org
helm repo update


###  Créer le namespace kubeai
kubectl create namespace kubeai

###  Désinstaller KubeAI s'il est déjà installé
helm delete kubeai kubeai/kubeai -n kubeai

###  Installer KubeAI dans le namespace kubeai
helm install kubeai kubeai/kubeai -n kubeai


###  Désinstaller KubeAI Models s'il est déjà installé
helm delete kubeai-models kubeai/models -n kubeai

###  Installer KubeAI Models dans le namespace kubeai
helm install kubeai-models kubeai/models -n kubeai --create-namespace -f kubeai-models.yaml

###  autres commandes utiles


helm upgrade --install open-webui open-webui/open-webui --version 0.6.22
helm upgrade --install kubeai kubeai/kubeai -n kubeai --version 0.21.0

helm get values kubeai -n kubeai
helm get values kubeai/kubeai -n kubeai

helm upgrade kubeai kubeai/kubeai -n kubeai -f pw.values.yaml

kubectl rollout restart deployment openwebui -n kubeai
kubectl scale deployment openwebui --replicas=0 -n kubeai

