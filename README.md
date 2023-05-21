Repo for creating and testing dockerized stateless applications

Config files included for deploying to kubernetes (See Actions => Workflows for automated deployments)

To run an app locally with automatic tear-down once the app exists/stops running:

`docker run --rm app`

To deploy to AKS manually:

- Create an AKS cluster
- Connect kubectl to the cluster
```
az account set --subscription <subscription id>

az aks get-credentials --name <cluster-name> --resource-group <resource-group-name>
```
- Run `kubectl apply -f /path/to/directory/deployment.yaml` and `kubectl apply -f /path/to/directory/service.yaml`
- Check Deployment: `kubectl get all` `kubectl describe services`
- Access deployment: open publicIP:PORT or port forward to access locally `kubectl port-forward service/nginx-service LOCALPORT:SERVICEPORT` then open localhost:LOCALPORT
- Tear down cluster: `az aks delete --name <cluster-name> --resource-group <resource-group-name>`