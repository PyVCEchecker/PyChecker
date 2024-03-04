# AWS App Mesh Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

AWS App Mesh is a service mesh based on the [Envoy](https://www.envoyproxy.io/) proxy that makes it easy to monitor and control microservices. App Mesh standardizes how your microservices communicate, giving you end-to-end visibility and helping to ensure high-availability for your applications.

App Mesh gives you consistent visibility and network traffic controls for every microservice in an application.

App Mesh supports microservice applications that use service discovery naming for their components. To use App Mesh, you must have an existing application running on AWS Fargate, Amazon ECS, Amazon EKS, Kubernetes on AWS, or Amazon EC2.

For further information on **AWS App Mesh**, visit the [AWS App Mesh Documentation](https://docs.aws.amazon.com/app-mesh/index.html).

## Create the App and Stack

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
app = cdk.App()
stack = cdk.Stack(app, "stack")
```

## Creating the Mesh

A service mesh is a logical boundary for network traffic between the services that reside within it.

After you create your service mesh, you can create virtual services, virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.

The following example creates the `AppMesh` service mesh with the default egress filter of `DROP_ALL`. See [the AWS CloudFormation `EgressFilter` resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html) for more info on egress filters.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
mesh = appmesh.Mesh(self, "AppMesh",
    mesh_name="myAwsMesh"
)
```

The mesh can instead be created with the `ALLOW_ALL` egress filter by providing the `egressFilter` property.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
mesh = appmesh.Mesh(self, "AppMesh",
    mesh_name="myAwsMesh",
    egress_filter=appmesh.MeshFilterType.ALLOW_ALL
)
```

## Adding VirtualRouters

A *mesh* uses  *virtual routers* as logical units to route requests to *virtual nodes*.

Virtual routers handle traffic for one or more virtual services within your mesh.
After you create a virtual router, you can create and associate routes to your virtual router that direct incoming requests to different virtual nodes.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# mesh is of type appmesh.Mesh

router = mesh.add_virtual_router("router",
    listeners=[appmesh.VirtualRouterListener.http(8080)]
)
```

Note that creating the router using the `addVirtualRouter()` method places it in the same stack as the mesh
(which might be different from the current stack).
The router can also be created using the `VirtualRouter` constructor (passing in the mesh) instead of calling the `addVirtualRouter()` method.
This is particularly useful when splitting your resources between many stacks: for example, defining the mesh itself as part of an infrastructure stack, but defining the other resources, such as routers, in the application stack:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# infra_stack is of type Stack
# app_stack is of type Stack


mesh = appmesh.Mesh(infra_stack, "AppMesh",
    mesh_name="myAwsMesh",
    egress_filter=appmesh.MeshFilterType.ALLOW_ALL
)

# the VirtualRouter will belong to 'appStack',
# even though the Mesh belongs to 'infraStack'
router = appmesh.VirtualRouter(app_stack, "router",
    mesh=mesh,  # notice that mesh is a required property when creating a router with the 'new' statement
    listeners=[appmesh.VirtualRouterListener.http(8081)]
)
```

The same is true for other `add*()` methods in the App Mesh construct library.

The `VirtualRouterListener` class lets you define protocol-specific listeners.
The `http()`, `http2()`, `grpc()` and `tcp()` methods create listeners for the named protocols.
They accept a single parameter that defines the port to on which requests will be matched.
The port parameter defaults to 8080 if omitted.

## Adding a VirtualService

A *virtual service* is an abstraction of a real service that is provided by a virtual node directly, or indirectly by means of a virtual router. Dependent services call your virtual service by its `virtualServiceName`, and those requests are routed to the virtual node or virtual router specified as the provider for the virtual service.

We recommend that you use the service discovery name of the real service that you're targeting (such as `my-service.default.svc.cluster.local`).

When creating a virtual service:

* If you want the virtual service to spread traffic across multiple virtual nodes, specify a virtual router.
* If you want the virtual service to reach a virtual node directly, without a virtual router, specify a virtual node.

Adding a virtual router as the provider:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# router is of type appmesh.VirtualRouter


appmesh.VirtualService(self, "virtual-service",
    virtual_service_name="my-service.default.svc.cluster.local",  # optional
    virtual_service_provider=appmesh.VirtualServiceProvider.virtual_router(router)
)
```

Adding a virtual node as the provider:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# node is of type appmesh.VirtualNode


appmesh.VirtualService(self, "virtual-service",
    virtual_service_name="my-service.default.svc.cluster.local",  # optional
    virtual_service_provider=appmesh.VirtualServiceProvider.virtual_node(node)
)
```

## Adding a VirtualNode

A *virtual node* acts as a logical pointer to a particular task group, such as an Amazon ECS service or a Kubernetes deployment.

When you create a virtual node, accept inbound traffic by specifying a *listener*. Outbound traffic that your virtual node expects to send should be specified as a *back end*.

The response metadata for your new virtual node contains the Amazon Resource Name (ARN) that is associated with the virtual node. Set this value (either the full ARN or the truncated resource name) as the `APPMESH_VIRTUAL_NODE_NAME` environment variable for your task group's Envoy proxy container in your task definition or pod spec. For example, the value could be `mesh/default/virtualNode/simpleapp`. This is then mapped to the `node.id` and `node.cluster` Envoy parameters.

> **Note**
> If you require your Envoy stats or tracing to use a different name, you can override the `node.cluster` value that is set by `APPMESH_VIRTUAL_NODE_NAME` with the `APPMESH_VIRTUAL_NODE_CLUSTER` environment variable.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# mesh is of type appmesh.Mesh
vpc = ec2.Vpc(self, "vpc")
namespace = cloudmap.PrivateDnsNamespace(self, "test-namespace",
    vpc=vpc,
    name="domain.local"
)
service = namespace.create_service("Svc")
node = mesh.add_virtual_node("virtual-node",
    service_discovery=appmesh.ServiceDiscovery.cloud_map(service),
    listeners=[appmesh.VirtualNodeListener.http(
        port=8081,
        health_check=appmesh.HealthCheck.http(
            healthy_threshold=3,
            interval=cdk.Duration.seconds(5),  # minimum
            path="/health-check-path",
            timeout=cdk.Duration.seconds(2),  # minimum
            unhealthy_threshold=2
        )
    )],
    access_log=appmesh.AccessLog.from_file_path("/dev/stdout")
)
```

Create a `VirtualNode` with the constructor and add tags.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# mesh is of type Mesh
# service is of type Service


node = appmesh.VirtualNode(self, "node",
    mesh=mesh,
    service_discovery=appmesh.ServiceDiscovery.cloud_map(service),
    listeners=[appmesh.VirtualNodeListener.http(
        port=8080,
        health_check=appmesh.HealthCheck.http(
            healthy_threshold=3,
            interval=cdk.Duration.seconds(5),
            path="/ping",
            timeout=cdk.Duration.seconds(2),
            unhealthy_threshold=2
        ),
        timeout=HttpTimeout(
            idle=cdk.Duration.seconds(5)
        )
    )],
    backend_defaults=BackendDefaults(
        tls_client_policy=TlsClientPolicy(
            validation=TlsValidation(
                trust=appmesh.TlsValidationTrust.file("/keys/local_cert_chain.pem")
            )
        )
    ),
    access_log=appmesh.AccessLog.from_file_path("/dev/stdout")
)

cdk.Tags.of(node).add("Environment", "Dev")
```

Create a `VirtualNode` with the constructor and add backend virtual service.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# mesh is of type Mesh
# router is of type VirtualRouter
# service is of type Service


node = appmesh.VirtualNode(self, "node",
    mesh=mesh,
    service_discovery=appmesh.ServiceDiscovery.cloud_map(service),
    listeners=[appmesh.VirtualNodeListener.http(
        port=8080,
        health_check=appmesh.HealthCheck.http(
            healthy_threshold=3,
            interval=cdk.Duration.seconds(5),
            path="/ping",
            timeout=cdk.Duration.seconds(2),
            unhealthy_threshold=2
        ),
        timeout=HttpTimeout(
            idle=cdk.Duration.seconds(5)
        )
    )],
    access_log=appmesh.AccessLog.from_file_path("/dev/stdout")
)

virtual_service = appmesh.VirtualService(self, "service-1",
    virtual_service_provider=appmesh.VirtualServiceProvider.virtual_router(router),
    virtual_service_name="service1.domain.local"
)

node.add_backend(appmesh.Backend.virtual_service(virtual_service))
```

The `listeners` property can be left blank and added later with the `node.addListener()` method. The `serviceDiscovery` property must be specified when specifying a listener.

The `backends` property can be added with `node.addBackend()`. In the example, we define a virtual service and add it to the virtual node to allow egress traffic to other nodes.

The `backendDefaults` property is added to the node while creating the virtual node. These are the virtual node's default settings for all backends.

### Adding TLS to a listener

The `tls` property specifies TLS configuration when creating a listener for a virtual node or a virtual gateway.
Provide the TLS certificate to the proxy in one of the following ways:

* A certificate from AWS Certificate Manager (ACM).
* A customer-provided certificate (specify a `certificateChain` path file and a `privateKey` file path).
* A certificate provided by a Secrets Discovery Service (SDS) endpoint over local Unix Domain Socket (specify its `secretName`).

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# A Virtual Node with listener TLS from an ACM provided certificate
# cert is of type certificatemanager.Certificate
# mesh is of type appmesh.Mesh


node = appmesh.VirtualNode(self, "node",
    mesh=mesh,
    service_discovery=appmesh.ServiceDiscovery.dns("node"),
    listeners=[appmesh.VirtualNodeListener.grpc(
        port=80,
        tls={
            "mode": appmesh.TlsMode.STRICT,
            "certificate": appmesh.TlsCertificate.acm(cert)
        }
    )]
)

# A Virtual Gateway with listener TLS from a customer provided file certificate
gateway = appmesh.VirtualGateway(self, "gateway",
    mesh=mesh,
    listeners=[appmesh.VirtualGatewayListener.grpc(
        port=8080,
        tls={
            "mode": appmesh.TlsMode.STRICT,
            "certificate": appmesh.TlsCertificate.file("path/to/certChain", "path/to/privateKey")
        }
    )],
    virtual_gateway_name="gateway"
)

# A Virtual Gateway with listener TLS from a SDS provided certificate
gateway2 = appmesh.VirtualGateway(self, "gateway2",
    mesh=mesh,
    listeners=[appmesh.VirtualGatewayListener.http2(
        port=8080,
        tls={
            "mode": appmesh.TlsMode.STRICT,
            "certificate": appmesh.TlsCertificate.sds("secrete_certificate")
        }
    )],
    virtual_gateway_name="gateway2"
)
```

### Adding mutual TLS authentication

Mutual TLS authentication is an optional component of TLS that offers two-way peer authentication.
To enable mutual TLS authentication, add the `mutualTlsCertificate` property to TLS client policy and/or the `mutualTlsValidation` property to your TLS listener.

`tls.mutualTlsValidation` and `tlsClientPolicy.mutualTlsCertificate` can be sourced from either:

* A customer-provided certificate (specify a `certificateChain` path file and a `privateKey` file path).
* A certificate provided by a Secrets Discovery Service (SDS) endpoint over local Unix Domain Socket (specify its `secretName`).

> **Note**
> Currently, a certificate from AWS Certificate Manager (ACM) cannot be used for mutual TLS authentication.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# mesh is of type appmesh.Mesh


node1 = appmesh.VirtualNode(self, "node1",
    mesh=mesh,
    service_discovery=appmesh.ServiceDiscovery.dns("node"),
    listeners=[appmesh.VirtualNodeListener.grpc(
        port=80,
        tls={
            "mode": appmesh.TlsMode.STRICT,
            "certificate": appmesh.TlsCertificate.file("path/to/certChain", "path/to/privateKey"),
            # Validate a file client certificates to enable mutual TLS authentication when a client provides a certificate.
            "mutual_tls_validation": {
                "trust": appmesh.TlsValidationTrust.file("path-to-certificate")
            }
        }
    )]
)

certificate_authority_arn = "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012"
node2 = appmesh.VirtualNode(self, "node2",
    mesh=mesh,
    service_discovery=appmesh.ServiceDiscovery.dns("node2"),
    backend_defaults={
        "tls_client_policy": {
            "ports": [8080, 8081],
            "validation": {
                "subject_alternative_names": appmesh.SubjectAlternativeNames.matching_exactly("mesh-endpoint.apps.local"),
                "trust": appmesh.TlsValidationTrust.acm([
                    acmpca.CertificateAuthority.from_certificate_authority_arn(self, "certificate", certificate_authority_arn)
                ])
            },
            # Provide a SDS client certificate when a server requests it and enable mutual TLS authentication.
            "mutual_tls_certificate": appmesh.TlsCertificate.sds("secret_certificate")
        }
    }
)
```

### Adding outlier detection to a Virtual Node listener

The `outlierDetection` property adds outlier detection to a Virtual Node listener. The properties
`baseEjectionDuration`, `interval`, `maxEjectionPercent`, and `maxServerErrors` are required.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# mesh is of type appmesh.Mesh
# Cloud Map service discovery is currently required for host ejection by outlier detection
vpc = ec2.Vpc(self, "vpc")
namespace = cloudmap.PrivateDnsNamespace(self, "test-namespace",
    vpc=vpc,
    name="domain.local"
)
service = namespace.create_service("Svc")
node = mesh.add_virtual_node("virtual-node",
    service_discovery=appmesh.ServiceDiscovery.cloud_map(service),
    listeners=[appmesh.VirtualNodeListener.http(
        outlier_detection={
            "base_ejection_duration": cdk.Duration.seconds(10),
            "interval": cdk.Duration.seconds(30),
            "max_ejection_percent": 50,
            "max_server_errors": 5
        }
    )]
)
```

### Adding a connection pool to a listener

The `connectionPool` property can be added to a Virtual Node listener or Virtual Gateway listener to add a request connection pool. Each listener protocol type has its own connection pool properties.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# A Virtual Node with a gRPC listener with a connection pool set
# mesh is of type appmesh.Mesh

node = appmesh.VirtualNode(self, "node",
    mesh=mesh,
    # DNS service discovery can optionally specify the DNS response type as either LOAD_BALANCER or ENDPOINTS.
    # LOAD_BALANCER means that the DNS resolver returns a loadbalanced set of endpoints,
    # whereas ENDPOINTS means that the DNS resolver is returning all the endpoints.
    # By default, the response type is assumed to be LOAD_BALANCER
    service_discovery=appmesh.ServiceDiscovery.dns("node", appmesh.DnsResponseType.ENDPOINTS),
    listeners=[appmesh.VirtualNodeListener.http(
        port=80,
        connection_pool={
            "max_connections": 100,
            "max_pending_requests": 10
        }
    )]
)

# A Virtual Gateway with a gRPC listener with a connection pool set
gateway = appmesh.VirtualGateway(self, "gateway",
    mesh=mesh,
    listeners=[appmesh.VirtualGatewayListener.grpc(
        port=8080,
        connection_pool={
            "max_requests": 10
        }
    )],
    virtual_gateway_name="gateway"
)
```

## Adding a Route

A *route* matches requests with an associated virtual router and distributes traffic to its associated virtual nodes.
The route distributes matching requests to one or more target virtual nodes with relative weighting.

The `RouteSpec` class lets you define protocol-specific route specifications.
The `tcp()`, `http()`, `http2()`, and `grpc()` methods create a specification for the named protocols.

For HTTP-based routes, the match field can match on path (prefix, exact, or regex), HTTP method, scheme,
HTTP headers, and query parameters. By default, HTTP-based routes match all requests.

For gRPC-based routes, the match field can  match on service name, method name, and metadata.
When specifying the method name, the service name must also be specified.

For example, here's how to add an HTTP route that matches based on a prefix of the URL path:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# router is of type appmesh.VirtualRouter
# node is of type appmesh.VirtualNode


router.add_route("route-http",
    route_spec=appmesh.RouteSpec.http(
        weighted_targets=[{
            "virtual_node": node
        }
        ],
        match={
            # Path that is passed to this method must start with '/'.
            "path": appmesh.HttpRoutePathMatch.starts_with("/path-to-app")
        }
    )
)
```

Add an HTTP2 route that matches based on exact path, method, scheme, headers, and query parameters:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# router is of type appmesh.VirtualRouter
# node is of type appmesh.VirtualNode


router.add_route("route-http2",
    route_spec=appmesh.RouteSpec.http2(
        weighted_targets=[{
            "virtual_node": node
        }
        ],
        match={
            "path": appmesh.HttpRoutePathMatch.exactly("/exact"),
            "method": appmesh.HttpRouteMethod.POST,
            "protocol": appmesh.HttpRouteProtocol.HTTPS,
            "headers": [
                # All specified headers must match for the route to match.
                appmesh.HeaderMatch.value_is("Content-Type", "application/json"),
                appmesh.HeaderMatch.value_is_not("Content-Type", "application/json")
            ],
            "query_parameters": [
                # All specified query parameters must match for the route to match.
                appmesh.QueryParameterMatch.value_is("query-field", "value")
            ]
        }
    )
)
```

Add a single route with two targets and split traffic 50/50:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# router is of type appmesh.VirtualRouter
# node is of type appmesh.VirtualNode


router.add_route("route-http",
    route_spec=appmesh.RouteSpec.http(
        weighted_targets=[{
            "virtual_node": node,
            "weight": 50
        }, {
            "virtual_node": node,
            "weight": 50
        }
        ],
        match={
            "path": appmesh.HttpRoutePathMatch.starts_with("/path-to-app")
        }
    )
)
```

Add an http2 route with retries:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# router is of type appmesh.VirtualRouter
# node is of type appmesh.VirtualNode


router.add_route("route-http2-retry",
    route_spec=appmesh.RouteSpec.http2(
        weighted_targets=[{"virtual_node": node}],
        retry_policy={
            # Retry if the connection failed
            "tcp_retry_events": [appmesh.TcpRetryEvent.CONNECTION_ERROR],
            # Retry if HTTP responds with a gateway error (502, 503, 504)
            "http_retry_events": [appmesh.HttpRetryEvent.GATEWAY_ERROR],
            # Retry five times
            "retry_attempts": 5,
            # Use a 1 second timeout per retry
            "retry_timeout": cdk.Duration.seconds(1)
        }
    )
)
```

Add a gRPC route with retries:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# router is of type appmesh.VirtualRouter
# node is of type appmesh.VirtualNode


router.add_route("route-grpc-retry",
    route_spec=appmesh.RouteSpec.grpc(
        weighted_targets=[{"virtual_node": node}],
        match={"service_name": "servicename"},
        retry_policy={
            "tcp_retry_events": [appmesh.TcpRetryEvent.CONNECTION_ERROR],
            "http_retry_events": [appmesh.HttpRetryEvent.GATEWAY_ERROR],
            # Retry if gRPC responds that the request was cancelled, a resource
            # was exhausted, or if the service is unavailable
            "grpc_retry_events": [appmesh.GrpcRetryEvent.CANCELLED, appmesh.GrpcRetryEvent.RESOURCE_EXHAUSTED, appmesh.GrpcRetryEvent.UNAVAILABLE
            ],
            "retry_attempts": 5,
            "retry_timeout": cdk.Duration.seconds(1)
        }
    )
)
```

Add an gRPC route that matches based on method name and metadata:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# router is of type VirtualRouter
# node is of type VirtualNode


router.add_route("route-grpc-retry",
    route_spec=appmesh.RouteSpec.grpc(
        weighted_targets=[WeightedTarget(virtual_node=node)],
        match=GrpcRouteMatch(
            # When method name is specified, service name must be also specified.
            method_name="methodname",
            service_name="servicename",
            metadata=[
                # All specified metadata must match for the route to match.
                appmesh.HeaderMatch.value_starts_with("Content-Type", "application/"),
                appmesh.HeaderMatch.value_does_not_start_with("Content-Type", "text/")
            ]
        )
    )
)
```

Add a gRPC route with timeout:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# router is of type appmesh.VirtualRouter
# node is of type appmesh.VirtualNode


router.add_route("route-http",
    route_spec=appmesh.RouteSpec.grpc(
        weighted_targets=[{
            "virtual_node": node
        }
        ],
        match={
            "service_name": "my-service.default.svc.cluster.local"
        },
        timeout={
            "idle": cdk.Duration.seconds(2),
            "per_request": cdk.Duration.seconds(1)
        }
    )
)
```

## Adding a Virtual Gateway

A *virtual gateway* allows resources outside your mesh to communicate with resources inside your mesh.
The virtual gateway represents an Envoy proxy running in an Amazon ECS task, in a Kubernetes service, or on an Amazon EC2 instance.
Unlike a virtual node, which represents Envoy running with an application, a virtual gateway represents Envoy deployed by itself.

A virtual gateway is similar to a virtual node in that it has a listener that accepts traffic for a particular port and protocol (HTTP, HTTP2, gRPC).
Traffic received by the virtual gateway is directed to other services in your mesh
using rules defined in gateway routes which can be added to your virtual gateway.

Create a virtual gateway with the constructor:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# mesh is of type appmesh.Mesh

certificate_authority_arn = "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012"

gateway = appmesh.VirtualGateway(self, "gateway",
    mesh=mesh,
    listeners=[appmesh.VirtualGatewayListener.http(
        port=443,
        health_check=appmesh.HealthCheck.http(
            interval=cdk.Duration.seconds(10)
        )
    )],
    backend_defaults={
        "tls_client_policy": {
            "ports": [8080, 8081],
            "validation": {
                "trust": appmesh.TlsValidationTrust.acm([
                    acmpca.CertificateAuthority.from_certificate_authority_arn(self, "certificate", certificate_authority_arn)
                ])
            }
        }
    },
    access_log=appmesh.AccessLog.from_file_path("/dev/stdout"),
    virtual_gateway_name="virtualGateway"
)
```

Add a virtual gateway directly to the mesh:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# mesh is of type appmesh.Mesh


gateway = mesh.add_virtual_gateway("gateway",
    access_log=appmesh.AccessLog.from_file_path("/dev/stdout"),
    virtual_gateway_name="virtualGateway",
    listeners=[appmesh.VirtualGatewayListener.http(
        port=443,
        health_check=appmesh.HealthCheck.http(
            interval=cdk.Duration.seconds(10)
        )
    )]
)
```

The `listeners` field defaults to an HTTP Listener on port 8080 if omitted.
A gateway route can be added using the `gateway.addGatewayRoute()` method.

The `backendDefaults` property, provided when creating the virtual gateway, specifies the virtual gateway's default settings for all backends.

## Adding a Gateway Route

A *gateway route* is attached to a virtual gateway and routes matching traffic to an existing virtual service.

For HTTP-based gateway routes, the `match` field can be used to match on
path (prefix, exact, or regex), HTTP method, host name, HTTP headers, and query parameters.
By default, HTTP-based gateway routes match all requests.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# gateway is of type appmesh.VirtualGateway
# virtual_service is of type appmesh.VirtualService


gateway.add_gateway_route("gateway-route-http",
    route_spec=appmesh.GatewayRouteSpec.http(
        route_target=virtual_service,
        match={
            "path": appmesh.HttpGatewayRoutePathMatch.regex("regex")
        }
    )
)
```

For gRPC-based gateway routes, the `match` field can be used to match on service name, host name, and metadata.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# gateway is of type appmesh.VirtualGateway
# virtual_service is of type appmesh.VirtualService


gateway.add_gateway_route("gateway-route-grpc",
    route_spec=appmesh.GatewayRouteSpec.grpc(
        route_target=virtual_service,
        match={
            "hostname": appmesh.GatewayRouteHostnameMatch.ends_with(".example.com")
        }
    )
)
```

For HTTP based gateway routes, App Mesh automatically rewrites the matched prefix path in Gateway Route to “/”.
This automatic rewrite configuration can be overwritten in following ways:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# gateway is of type VirtualGateway
# virtual_service is of type VirtualService


gateway.add_gateway_route("gateway-route-http",
    route_spec=appmesh.GatewayRouteSpec.http(
        route_target=virtual_service,
        match=HttpGatewayRouteMatch(
            # This disables the default rewrite to '/', and retains original path.
            path=appmesh.HttpGatewayRoutePathMatch.starts_with("/path-to-app/", "")
        )
    )
)

gateway.add_gateway_route("gateway-route-http-1",
    route_spec=appmesh.GatewayRouteSpec.http(
        route_target=virtual_service,
        match=HttpGatewayRouteMatch(
            # If the request full path is '/path-to-app/xxxxx', this rewrites the path to '/rewrittenUri/xxxxx'.
            # Please note both `prefixPathMatch` and `rewriteTo` must start and end with the `/` character.
            path=appmesh.HttpGatewayRoutePathMatch.starts_with("/path-to-app/", "/rewrittenUri/")
        )
    )
)
```

If matching other path (exact or regex), only specific rewrite path can be specified.
Unlike `startsWith()` method above, no default rewrite is performed.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# gateway is of type VirtualGateway
# virtual_service is of type VirtualService


gateway.add_gateway_route("gateway-route-http-2",
    route_spec=appmesh.GatewayRouteSpec.http(
        route_target=virtual_service,
        match=HttpGatewayRouteMatch(
            # This rewrites the path from '/test' to '/rewrittenPath'.
            path=appmesh.HttpGatewayRoutePathMatch.exactly("/test", "/rewrittenPath")
        )
    )
)
```

For HTTP/gRPC based routes, App Mesh automatically rewrites
the original request received at the Virtual Gateway to the destination Virtual Service name.
This default host name rewrite can be configured by specifying the rewrite rule as one of the `match` property:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# gateway is of type appmesh.VirtualGateway
# virtual_service is of type appmesh.VirtualService


gateway.add_gateway_route("gateway-route-grpc",
    route_spec=appmesh.GatewayRouteSpec.grpc(
        route_target=virtual_service,
        match={
            "hostname": appmesh.GatewayRouteHostnameMatch.exactly("example.com"),
            # This disables the default rewrite to virtual service name and retain original request.
            "rewrite_request_hostname": False
        }
    )
)
```

## Importing Resources

Each App Mesh resource class comes with two static methods, `from<Resource>Arn` and `from<Resource>Attributes` (where `<Resource>` is replaced with the resource name, such as `VirtualNode`) for importing a reference to an existing App Mesh resource.
These imported resources can be used with other resources in your mesh as if they were defined directly in your CDK application.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
arn = "arn:aws:appmesh:us-east-1:123456789012:mesh/testMesh/virtualNode/testNode"
appmesh.VirtualNode.from_virtual_node_arn(self, "importedVirtualNode", arn)
```

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
virtual_node_name = "my-virtual-node"
appmesh.VirtualNode.from_virtual_node_attributes(self, "imported-virtual-node",
    mesh=appmesh.Mesh.from_mesh_name(self, "Mesh", "testMesh"),
    virtual_node_name=virtual_node_name
)
```

To import a mesh, again there are two static methods, `fromMeshArn` and `fromMeshName`.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
arn = "arn:aws:appmesh:us-east-1:123456789012:mesh/testMesh"
appmesh.Mesh.from_mesh_arn(self, "imported-mesh", arn)
```

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
appmesh.Mesh.from_mesh_name(self, "imported-mesh", "abc")
```

## IAM Grants

`VirtualNode` and `VirtualGateway` provide `grantStreamAggregatedResources` methods that grant identities that are running
Envoy access to stream generated config from App Mesh.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# mesh is of type appmesh.Mesh

gateway = appmesh.VirtualGateway(self, "testGateway", mesh=mesh)
envoy_user = iam.User(self, "envoyUser")

#
# This will grant `grantStreamAggregatedResources` ONLY for this gateway.
#
gateway.grant_stream_aggregated_resources(envoy_user)
```

## Adding Resources to shared meshes

A shared mesh allows resources created by different accounts to communicate with each other in the same mesh:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# This is the ARN for the mesh from different AWS IAM account ID.
# Ensure mesh is properly shared with your account. For more details, see: https://github.com/aws/aws-cdk/issues/15404
arn = "arn:aws:appmesh:us-east-1:123456789012:mesh/testMesh"
shared_mesh = appmesh.Mesh.from_mesh_arn(self, "imported-mesh", arn)

# This VirtualNode resource can communicate with the resources in the mesh from different AWS IAM account ID.
appmesh.VirtualNode(self, "test-node",
    mesh=shared_mesh
)
```
