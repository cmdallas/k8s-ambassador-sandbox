# K8s/Ambassador Sandbox

```shell
minikube start -p k8sambassador --extra-config=apiserver.enable-swagger-ui=true --alsologtostderr
minikub -p k8sambassador dashboard
kubectl create secret docker-registry registry-credentials --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
kubectl apply -f https://getambassador.io/yaml/ambassador/ambassador-rbac.yaml
kubectl apply -f kubernetes/ambassador-service.yaml
kubectl apply -f kubernetes/api-deployment-with-ambassador.yaml
minikube -p workshop service list
curl "http://<ambassador_ip>:<port>/?l=elixir&n=5"
```
