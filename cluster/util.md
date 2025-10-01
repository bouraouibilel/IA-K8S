kubectl get pods -n anythingllm | grep -v Running | awk '{print $1}' | xargs kubectl delete pod -n anythingllm

kubectl get pods --all-namespaces | grep -v Running | awk '{print $2}' | xargs kubectl delete pod --all-namespaces

kubectl get pods --all-namespaces | grep -v Running | awk 'NR>1 {print $1" "$2}' | xargs -n2 sh -c 'kubectl delete pod -n $0 $1'


