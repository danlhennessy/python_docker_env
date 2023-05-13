Streamlit webapp designed to show average deadlift 1rm for powerlifters by age.
Focussing on 90kg weight class.

The app has been redesigned to suit a container

Includes a Dockerfile to build app into an image, plus kubernetes deployment config to create 3 replicas along with a load balancer.

Local Docker Setup:

- Build image `docker build -t st-deadlift .`
- Run in docker container `docker run -p 8501:8501 st-deadlift` (Maps container port 8501 to localhost port 8501)
- Connect to app at http://localhost:8501

Kubernetes Setup:
- Tag docker image `docker tag st-deadlift:version YOUR-USER-NAME/repository:version`
- Push image to Docker Hub `docker push YOUR-USER-NAME/repository:version`
- Edit kubernetes deployment.yaml with link to Docker Hub image
- Apply deployment config `kubectl apply -f deployment.yaml`
- Apply service config `kubectl apply -f service.yaml`
- Check deployment `kubectl get pods -o wide` `kubectl describe deployment st-deadlift`
- Connect to app at http://localhost:8501

Helm:
- Add a chart repository: `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
- `helm repo update`
- 