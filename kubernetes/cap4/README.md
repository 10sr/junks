cap4
====

sample-pod
----------

```console
kubectl create -f sample-pod.yaml
kubectl create -f sample-pod.yaml
kubectl get pods
kubectl delete -f sample-pod.yaml
kubectl apply -f sample-pod.yaml
kubectl get pods sample-pod -o jsonpath="{.spec.containers[].image}"
```
