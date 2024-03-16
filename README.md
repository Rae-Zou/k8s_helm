# k8s_helm
## Deploy on Kubernetes with Docker Desktop
The Kubernetes server runs locally within your Docker instance, is not configurable, and is a single-node cluster. It runs within a Docker container on your local system, and is only for local testing.
https://docs.docker.com/desktop/kubernetes/
https://bus-ekapop.medium.com/setup-k8s-single-node-with-docker-desktop-and-helm-ab537c0ae01c 

## Create Helm Chart
https://docs.vmware.com/en/VMware-Tanzu-Application-Catalog/services/tutorials/GUID-create-first-helm-chart-index.html

## Verify the Helm chart’s configuration
```bash
helm lint .
```

## Verify the values are correctly substituted in the templates
```bash
helm template .
```

## Check for errors before actually installing
```bash
helm install --dry-run python-test ./mychart
```

## deploy the chart to the Kubernetes Cluster
```bash
helm install python-test ./mychart
```

## check the release list
````bash
helm list
````

## Uninstall the Helm release
```bash
helm uninstall python-test
```