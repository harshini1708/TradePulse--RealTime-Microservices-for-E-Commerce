
# Distributed Real-Time Microservices System for E-Commerce

## Project Overview:
This project demonstrates a distributed real-time microservices architecture for an e-commerce platform. It consists of three core services: Product Service, Order Service, and User Service, each deployed as a containerized microservice using Docker and orchestrated with Kubernetes.

### Technologies:
- **Docker** for containerization of microservices.
- **Kubernetes** for service orchestration.
- **Microservices architecture** to ensure scalability and fault tolerance.

### Services:
1. **Product Service**: Manages product information.
2. **Order Service**: Manages customer orders.
3. **User Service**: Handles user accounts and authentication.

### How to Run:
1. **Build Docker images** for each microservice using the provided Dockerfiles.
2. **Deploy the services** on a Kubernetes cluster using the deployment files.
3. **Scale the system** by adjusting Kubernetes replica sets.

## Steps to Deploy:
1. Build Docker images for each service:
```
docker build -t product-service ./code/product_service
docker build -t order-service ./code/order_service
docker build -t user-service ./code/user_service
```

2. Deploy to Kubernetes:
```
kubectl apply -f kubernetes/
```

3. Scale services as needed:
```
kubectl scale --replicas=5 deployment/product-service
kubectl scale --replicas=5 deployment/order-service
kubectl scale --replicas=5 deployment/user-service
```
