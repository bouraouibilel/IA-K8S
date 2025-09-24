k create namespace qdrant

helm install qdrant qdrant/qdrant -n qdrant -f qdrant-values-ha.yaml

