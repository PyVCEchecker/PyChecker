'''
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
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.aws_acmpca
import aws_cdk.aws_certificatemanager
import aws_cdk.aws_iam
import aws_cdk.aws_servicediscovery
import aws_cdk.core
import constructs


class AccessLog(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.AccessLog",
):
    '''Configuration for Envoy Access logs for mesh endpoints.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromFilePath") # type: ignore[misc]
    @builtins.classmethod
    def from_file_path(cls, file_path: builtins.str) -> "AccessLog":
        '''Path to a file to write access logs to.

        :param file_path: -

        :default: - no file based access logging
        '''
        return typing.cast("AccessLog", jsii.sinvoke(cls, "fromFilePath", [file_path]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "AccessLogConfig":
        '''Called when the AccessLog type is initialized.

        Can be used to enforce
        mutual exclusivity with future properties

        :param scope: -
        '''
        ...


class _AccessLogProxy(AccessLog):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "AccessLogConfig":
        '''Called when the AccessLog type is initialized.

        Can be used to enforce
        mutual exclusivity with future properties

        :param scope: -
        '''
        return typing.cast("AccessLogConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, AccessLog).__jsii_proxy_class__ = lambda : _AccessLogProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.AccessLogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "virtual_gateway_access_log": "virtualGatewayAccessLog",
        "virtual_node_access_log": "virtualNodeAccessLog",
    },
)
class AccessLogConfig:
    def __init__(
        self,
        *,
        virtual_gateway_access_log: typing.Optional["CfnVirtualGateway.VirtualGatewayAccessLogProperty"] = None,
        virtual_node_access_log: typing.Optional["CfnVirtualNode.AccessLogProperty"] = None,
    ) -> None:
        '''All Properties for Envoy Access logs for mesh endpoints.

        :param virtual_gateway_access_log: VirtualGateway CFN configuration for Access Logging. Default: - no access logging
        :param virtual_node_access_log: VirtualNode CFN configuration for Access Logging. Default: - no access logging
        '''
        if isinstance(virtual_gateway_access_log, dict):
            virtual_gateway_access_log = CfnVirtualGateway.VirtualGatewayAccessLogProperty(**virtual_gateway_access_log)
        if isinstance(virtual_node_access_log, dict):
            virtual_node_access_log = CfnVirtualNode.AccessLogProperty(**virtual_node_access_log)
        self._values: typing.Dict[str, typing.Any] = {}
        if virtual_gateway_access_log is not None:
            self._values["virtual_gateway_access_log"] = virtual_gateway_access_log
        if virtual_node_access_log is not None:
            self._values["virtual_node_access_log"] = virtual_node_access_log

    @builtins.property
    def virtual_gateway_access_log(
        self,
    ) -> typing.Optional["CfnVirtualGateway.VirtualGatewayAccessLogProperty"]:
        '''VirtualGateway CFN configuration for Access Logging.

        :default: - no access logging
        '''
        result = self._values.get("virtual_gateway_access_log")
        return typing.cast(typing.Optional["CfnVirtualGateway.VirtualGatewayAccessLogProperty"], result)

    @builtins.property
    def virtual_node_access_log(
        self,
    ) -> typing.Optional["CfnVirtualNode.AccessLogProperty"]:
        '''VirtualNode CFN configuration for Access Logging.

        :default: - no access logging
        '''
        result = self._values.get("virtual_node_access_log")
        return typing.cast(typing.Optional["CfnVirtualNode.AccessLogProperty"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Backend(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.Backend",
):
    '''Contains static factory methods to create backends.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="virtualService") # type: ignore[misc]
    @builtins.classmethod
    def virtual_service(
        cls,
        virtual_service: "IVirtualService",
        *,
        tls_client_policy: typing.Optional["TlsClientPolicy"] = None,
    ) -> "Backend":
        '''Construct a Virtual Service backend.

        :param virtual_service: -
        :param tls_client_policy: TLS properties for Client policy for the backend. Default: - none
        '''
        props = VirtualServiceBackendOptions(tls_client_policy=tls_client_policy)

        return typing.cast("Backend", jsii.sinvoke(cls, "virtualService", [virtual_service, props]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, _scope: aws_cdk.core.Construct) -> "BackendConfig":
        '''Return backend config.

        :param _scope: -
        '''
        ...


class _BackendProxy(Backend):
    @jsii.member(jsii_name="bind")
    def bind(self, _scope: aws_cdk.core.Construct) -> "BackendConfig":
        '''Return backend config.

        :param _scope: -
        '''
        return typing.cast("BackendConfig", jsii.invoke(self, "bind", [_scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Backend).__jsii_proxy_class__ = lambda : _BackendProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.BackendConfig",
    jsii_struct_bases=[],
    name_mapping={"virtual_service_backend": "virtualServiceBackend"},
)
class BackendConfig:
    def __init__(
        self,
        *,
        virtual_service_backend: "CfnVirtualNode.BackendProperty",
    ) -> None:
        '''Properties for a backend.

        :param virtual_service_backend: Config for a Virtual Service backend.
        '''
        if isinstance(virtual_service_backend, dict):
            virtual_service_backend = CfnVirtualNode.BackendProperty(**virtual_service_backend)
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service_backend": virtual_service_backend,
        }

    @builtins.property
    def virtual_service_backend(self) -> "CfnVirtualNode.BackendProperty":
        '''Config for a Virtual Service backend.'''
        result = self._values.get("virtual_service_backend")
        assert result is not None, "Required property 'virtual_service_backend' is missing"
        return typing.cast("CfnVirtualNode.BackendProperty", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.BackendDefaults",
    jsii_struct_bases=[],
    name_mapping={"tls_client_policy": "tlsClientPolicy"},
)
class BackendDefaults:
    def __init__(
        self,
        *,
        tls_client_policy: typing.Optional["TlsClientPolicy"] = None,
    ) -> None:
        '''Represents the properties needed to define backend defaults.

        :param tls_client_policy: TLS properties for Client policy for backend defaults. Default: - none
        '''
        if isinstance(tls_client_policy, dict):
            tls_client_policy = TlsClientPolicy(**tls_client_policy)
        self._values: typing.Dict[str, typing.Any] = {}
        if tls_client_policy is not None:
            self._values["tls_client_policy"] = tls_client_policy

    @builtins.property
    def tls_client_policy(self) -> typing.Optional["TlsClientPolicy"]:
        '''TLS properties for Client policy for backend defaults.

        :default: - none
        '''
        result = self._values.get("tls_client_policy")
        return typing.cast(typing.Optional["TlsClientPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackendDefaults(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnGatewayRoute(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute",
):
    '''A CloudFormation ``AWS::AppMesh::GatewayRoute``.

    :cloudformationResource: AWS::AppMesh::GatewayRoute
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        mesh_name: builtins.str,
        spec: typing.Union["CfnGatewayRoute.GatewayRouteSpecProperty", aws_cdk.core.IResolvable],
        virtual_gateway_name: builtins.str,
        gateway_route_name: typing.Optional[builtins.str] = None,
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::AppMesh::GatewayRoute``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param mesh_name: ``AWS::AppMesh::GatewayRoute.MeshName``.
        :param spec: ``AWS::AppMesh::GatewayRoute.Spec``.
        :param virtual_gateway_name: ``AWS::AppMesh::GatewayRoute.VirtualGatewayName``.
        :param gateway_route_name: ``AWS::AppMesh::GatewayRoute.GatewayRouteName``.
        :param mesh_owner: ``AWS::AppMesh::GatewayRoute.MeshOwner``.
        :param tags: ``AWS::AppMesh::GatewayRoute.Tags``.
        '''
        props = CfnGatewayRouteProps(
            mesh_name=mesh_name,
            spec=spec,
            virtual_gateway_name=virtual_gateway_name,
            gateway_route_name=gateway_route_name,
            mesh_owner=mesh_owner,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrGatewayRouteName")
    def attr_gateway_route_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: GatewayRouteName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayRouteName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshName")
    def attr_mesh_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshOwner")
    def attr_mesh_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceOwner")
    def attr_resource_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUid")
    def attr_uid(self) -> builtins.str:
        '''
        :cloudformationAttribute: Uid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVirtualGatewayName")
    def attr_virtual_gateway_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: VirtualGatewayName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualGatewayName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppMesh::GatewayRoute.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::GatewayRoute.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshname
        '''
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        jsii.set(self, "meshName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="spec")
    def spec(
        self,
    ) -> typing.Union["CfnGatewayRoute.GatewayRouteSpecProperty", aws_cdk.core.IResolvable]:
        '''``AWS::AppMesh::GatewayRoute.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-spec
        '''
        return typing.cast(typing.Union["CfnGatewayRoute.GatewayRouteSpecProperty", aws_cdk.core.IResolvable], jsii.get(self, "spec"))

    @spec.setter
    def spec(
        self,
        value: typing.Union["CfnGatewayRoute.GatewayRouteSpecProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "spec", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGatewayName")
    def virtual_gateway_name(self) -> builtins.str:
        '''``AWS::AppMesh::GatewayRoute.VirtualGatewayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-virtualgatewayname
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualGatewayName"))

    @virtual_gateway_name.setter
    def virtual_gateway_name(self, value: builtins.str) -> None:
        jsii.set(self, "virtualGatewayName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayRouteName")
    def gateway_route_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::GatewayRoute.GatewayRouteName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-gatewayroutename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayRouteName"))

    @gateway_route_name.setter
    def gateway_route_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "gatewayRouteName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::GatewayRoute.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshowner
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "meshOwner", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GatewayRouteHostnameMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"exact": "exact", "suffix": "suffix"},
    )
    class GatewayRouteHostnameMatchProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[builtins.str] = None,
            suffix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param exact: ``CfnGatewayRoute.GatewayRouteHostnameMatchProperty.Exact``.
            :param suffix: ``CfnGatewayRoute.GatewayRouteHostnameMatchProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact
            if suffix is not None:
                self._values["suffix"] = suffix

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.GatewayRouteHostnameMatchProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def suffix(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.GatewayRouteHostnameMatchProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-suffix
            '''
            result = self._values.get("suffix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayRouteHostnameMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GatewayRouteHostnameRewriteProperty",
        jsii_struct_bases=[],
        name_mapping={"default_target_hostname": "defaultTargetHostname"},
    )
    class GatewayRouteHostnameRewriteProperty:
        def __init__(
            self,
            *,
            default_target_hostname: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param default_target_hostname: ``CfnGatewayRoute.GatewayRouteHostnameRewriteProperty.DefaultTargetHostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_target_hostname is not None:
                self._values["default_target_hostname"] = default_target_hostname

        @builtins.property
        def default_target_hostname(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.GatewayRouteHostnameRewriteProperty.DefaultTargetHostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html#cfn-appmesh-gatewayroute-gatewayroutehostnamerewrite-defaulttargethostname
            '''
            result = self._values.get("default_target_hostname")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayRouteHostnameRewriteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GatewayRouteMetadataMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exact": "exact",
            "prefix": "prefix",
            "range": "range",
            "regex": "regex",
            "suffix": "suffix",
        },
    )
    class GatewayRouteMetadataMatchProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            range: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteRangeMatchProperty"]] = None,
            regex: typing.Optional[builtins.str] = None,
            suffix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param exact: ``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Exact``.
            :param prefix: ``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Prefix``.
            :param range: ``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Range``.
            :param regex: ``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Regex``.
            :param suffix: ``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact
            if prefix is not None:
                self._values["prefix"] = prefix
            if range is not None:
                self._values["range"] = range
            if regex is not None:
                self._values["regex"] = regex
            if suffix is not None:
                self._values["suffix"] = suffix

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteRangeMatchProperty"]]:
            '''``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Range``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-range
            '''
            result = self._values.get("range")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteRangeMatchProperty"]], result)

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Regex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def suffix(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.GatewayRouteMetadataMatchProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-suffix
            '''
            result = self._values.get("suffix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayRouteMetadataMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GatewayRouteRangeMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class GatewayRouteRangeMatchProperty:
        def __init__(self, *, end: jsii.Number, start: jsii.Number) -> None:
            '''
            :param end: ``CfnGatewayRoute.GatewayRouteRangeMatchProperty.End``.
            :param start: ``CfnGatewayRoute.GatewayRouteRangeMatchProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "end": end,
                "start": start,
            }

        @builtins.property
        def end(self) -> jsii.Number:
            '''``CfnGatewayRoute.GatewayRouteRangeMatchProperty.End``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html#cfn-appmesh-gatewayroute-gatewayrouterangematch-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def start(self) -> jsii.Number:
            '''``CfnGatewayRoute.GatewayRouteRangeMatchProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html#cfn-appmesh-gatewayroute-gatewayrouterangematch-start
            '''
            result = self._values.get("start")
            assert result is not None, "Required property 'start' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayRouteRangeMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GatewayRouteSpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "grpc_route": "grpcRoute",
            "http2_route": "http2Route",
            "http_route": "httpRoute",
        },
    )
    class GatewayRouteSpecProperty:
        def __init__(
            self,
            *,
            grpc_route: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteProperty"]] = None,
            http2_route: typing.Optional[typing.Union["CfnGatewayRoute.HttpGatewayRouteProperty", aws_cdk.core.IResolvable]] = None,
            http_route: typing.Optional[typing.Union["CfnGatewayRoute.HttpGatewayRouteProperty", aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param grpc_route: ``CfnGatewayRoute.GatewayRouteSpecProperty.GrpcRoute``.
            :param http2_route: ``CfnGatewayRoute.GatewayRouteSpecProperty.Http2Route``.
            :param http_route: ``CfnGatewayRoute.GatewayRouteSpecProperty.HttpRoute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if grpc_route is not None:
                self._values["grpc_route"] = grpc_route
            if http2_route is not None:
                self._values["http2_route"] = http2_route
            if http_route is not None:
                self._values["http_route"] = http_route

        @builtins.property
        def grpc_route(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteProperty"]]:
            '''``CfnGatewayRoute.GatewayRouteSpecProperty.GrpcRoute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-grpcroute
            '''
            result = self._values.get("grpc_route")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteProperty"]], result)

        @builtins.property
        def http2_route(
            self,
        ) -> typing.Optional[typing.Union["CfnGatewayRoute.HttpGatewayRouteProperty", aws_cdk.core.IResolvable]]:
            '''``CfnGatewayRoute.GatewayRouteSpecProperty.Http2Route``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-http2route
            '''
            result = self._values.get("http2_route")
            return typing.cast(typing.Optional[typing.Union["CfnGatewayRoute.HttpGatewayRouteProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def http_route(
            self,
        ) -> typing.Optional[typing.Union["CfnGatewayRoute.HttpGatewayRouteProperty", aws_cdk.core.IResolvable]]:
            '''``CfnGatewayRoute.GatewayRouteSpecProperty.HttpRoute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-httproute
            '''
            result = self._values.get("http_route")
            return typing.cast(typing.Optional[typing.Union["CfnGatewayRoute.HttpGatewayRouteProperty", aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayRouteSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GatewayRouteTargetProperty",
        jsii_struct_bases=[],
        name_mapping={"virtual_service": "virtualService"},
    )
    class GatewayRouteTargetProperty:
        def __init__(
            self,
            *,
            virtual_service: typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteVirtualServiceProperty"],
        ) -> None:
            '''
            :param virtual_service: ``CfnGatewayRoute.GatewayRouteTargetProperty.VirtualService``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "virtual_service": virtual_service,
            }

        @builtins.property
        def virtual_service(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteVirtualServiceProperty"]:
            '''``CfnGatewayRoute.GatewayRouteTargetProperty.VirtualService``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html#cfn-appmesh-gatewayroute-gatewayroutetarget-virtualservice
            '''
            result = self._values.get("virtual_service")
            assert result is not None, "Required property 'virtual_service' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteVirtualServiceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayRouteTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GatewayRouteVirtualServiceProperty",
        jsii_struct_bases=[],
        name_mapping={"virtual_service_name": "virtualServiceName"},
    )
    class GatewayRouteVirtualServiceProperty:
        def __init__(self, *, virtual_service_name: builtins.str) -> None:
            '''
            :param virtual_service_name: ``CfnGatewayRoute.GatewayRouteVirtualServiceProperty.VirtualServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "virtual_service_name": virtual_service_name,
            }

        @builtins.property
        def virtual_service_name(self) -> builtins.str:
            '''``CfnGatewayRoute.GatewayRouteVirtualServiceProperty.VirtualServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html#cfn-appmesh-gatewayroute-gatewayroutevirtualservice-virtualservicename
            '''
            result = self._values.get("virtual_service_name")
            assert result is not None, "Required property 'virtual_service_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayRouteVirtualServiceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GrpcGatewayRouteActionProperty",
        jsii_struct_bases=[],
        name_mapping={"target": "target", "rewrite": "rewrite"},
    )
    class GrpcGatewayRouteActionProperty:
        def __init__(
            self,
            *,
            target: typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteTargetProperty"],
            rewrite: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteRewriteProperty"]] = None,
        ) -> None:
            '''
            :param target: ``CfnGatewayRoute.GrpcGatewayRouteActionProperty.Target``.
            :param rewrite: ``CfnGatewayRoute.GrpcGatewayRouteActionProperty.Rewrite``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "target": target,
            }
            if rewrite is not None:
                self._values["rewrite"] = rewrite

        @builtins.property
        def target(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteTargetProperty"]:
            '''``CfnGatewayRoute.GrpcGatewayRouteActionProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteTargetProperty"], result)

        @builtins.property
        def rewrite(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteRewriteProperty"]]:
            '''``CfnGatewayRoute.GrpcGatewayRouteActionProperty.Rewrite``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-rewrite
            '''
            result = self._values.get("rewrite")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteRewriteProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcGatewayRouteActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GrpcGatewayRouteMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hostname": "hostname",
            "metadata": "metadata",
            "service_name": "serviceName",
        },
    )
    class GrpcGatewayRouteMatchProperty:
        def __init__(
            self,
            *,
            hostname: typing.Optional[typing.Union["CfnGatewayRoute.GatewayRouteHostnameMatchProperty", aws_cdk.core.IResolvable]] = None,
            metadata: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteMetadataProperty"]]]] = None,
            service_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param hostname: ``CfnGatewayRoute.GrpcGatewayRouteMatchProperty.Hostname``.
            :param metadata: ``CfnGatewayRoute.GrpcGatewayRouteMatchProperty.Metadata``.
            :param service_name: ``CfnGatewayRoute.GrpcGatewayRouteMatchProperty.ServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if hostname is not None:
                self._values["hostname"] = hostname
            if metadata is not None:
                self._values["metadata"] = metadata
            if service_name is not None:
                self._values["service_name"] = service_name

        @builtins.property
        def hostname(
            self,
        ) -> typing.Optional[typing.Union["CfnGatewayRoute.GatewayRouteHostnameMatchProperty", aws_cdk.core.IResolvable]]:
            '''``CfnGatewayRoute.GrpcGatewayRouteMatchProperty.Hostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-hostname
            '''
            result = self._values.get("hostname")
            return typing.cast(typing.Optional[typing.Union["CfnGatewayRoute.GatewayRouteHostnameMatchProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def metadata(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteMetadataProperty"]]]]:
            '''``CfnGatewayRoute.GrpcGatewayRouteMatchProperty.Metadata``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-metadata
            '''
            result = self._values.get("metadata")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteMetadataProperty"]]]], result)

        @builtins.property
        def service_name(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.GrpcGatewayRouteMatchProperty.ServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-servicename
            '''
            result = self._values.get("service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcGatewayRouteMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GrpcGatewayRouteMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "invert": "invert", "match": "match"},
    )
    class GrpcGatewayRouteMetadataProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            invert: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            match: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteMetadataMatchProperty"]] = None,
        ) -> None:
            '''
            :param name: ``CfnGatewayRoute.GrpcGatewayRouteMetadataProperty.Name``.
            :param invert: ``CfnGatewayRoute.GrpcGatewayRouteMetadataProperty.Invert``.
            :param match: ``CfnGatewayRoute.GrpcGatewayRouteMetadataProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if invert is not None:
                self._values["invert"] = invert
            if match is not None:
                self._values["match"] = match

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnGatewayRoute.GrpcGatewayRouteMetadataProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invert(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnGatewayRoute.GrpcGatewayRouteMetadataProperty.Invert``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-invert
            '''
            result = self._values.get("invert")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def match(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteMetadataMatchProperty"]]:
            '''``CfnGatewayRoute.GrpcGatewayRouteMetadataProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-match
            '''
            result = self._values.get("match")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteMetadataMatchProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcGatewayRouteMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GrpcGatewayRouteProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "match": "match"},
    )
    class GrpcGatewayRouteProperty:
        def __init__(
            self,
            *,
            action: typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteActionProperty"],
            match: typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteMatchProperty"],
        ) -> None:
            '''
            :param action: ``CfnGatewayRoute.GrpcGatewayRouteProperty.Action``.
            :param match: ``CfnGatewayRoute.GrpcGatewayRouteProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
                "match": match,
            }

        @builtins.property
        def action(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteActionProperty"]:
            '''``CfnGatewayRoute.GrpcGatewayRouteProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteActionProperty"], result)

        @builtins.property
        def match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteMatchProperty"]:
            '''``CfnGatewayRoute.GrpcGatewayRouteProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-match
            '''
            result = self._values.get("match")
            assert result is not None, "Required property 'match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GrpcGatewayRouteMatchProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcGatewayRouteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.GrpcGatewayRouteRewriteProperty",
        jsii_struct_bases=[],
        name_mapping={"hostname": "hostname"},
    )
    class GrpcGatewayRouteRewriteProperty:
        def __init__(
            self,
            *,
            hostname: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteHostnameRewriteProperty"]] = None,
        ) -> None:
            '''
            :param hostname: ``CfnGatewayRoute.GrpcGatewayRouteRewriteProperty.Hostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if hostname is not None:
                self._values["hostname"] = hostname

        @builtins.property
        def hostname(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteHostnameRewriteProperty"]]:
            '''``CfnGatewayRoute.GrpcGatewayRouteRewriteProperty.Hostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html#cfn-appmesh-gatewayroute-grpcgatewayrouterewrite-hostname
            '''
            result = self._values.get("hostname")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteHostnameRewriteProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcGatewayRouteRewriteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpGatewayRouteActionProperty",
        jsii_struct_bases=[],
        name_mapping={"target": "target", "rewrite": "rewrite"},
    )
    class HttpGatewayRouteActionProperty:
        def __init__(
            self,
            *,
            target: typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteTargetProperty"],
            rewrite: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteRewriteProperty"]] = None,
        ) -> None:
            '''
            :param target: ``CfnGatewayRoute.HttpGatewayRouteActionProperty.Target``.
            :param rewrite: ``CfnGatewayRoute.HttpGatewayRouteActionProperty.Rewrite``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "target": target,
            }
            if rewrite is not None:
                self._values["rewrite"] = rewrite

        @builtins.property
        def target(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteTargetProperty"]:
            '''``CfnGatewayRoute.HttpGatewayRouteActionProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteTargetProperty"], result)

        @builtins.property
        def rewrite(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteRewriteProperty"]]:
            '''``CfnGatewayRoute.HttpGatewayRouteActionProperty.Rewrite``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-rewrite
            '''
            result = self._values.get("rewrite")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteRewriteProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpGatewayRouteActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exact": "exact",
            "prefix": "prefix",
            "range": "range",
            "regex": "regex",
            "suffix": "suffix",
        },
    )
    class HttpGatewayRouteHeaderMatchProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            range: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteRangeMatchProperty"]] = None,
            regex: typing.Optional[builtins.str] = None,
            suffix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param exact: ``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Exact``.
            :param prefix: ``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Prefix``.
            :param range: ``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Range``.
            :param regex: ``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Regex``.
            :param suffix: ``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact
            if prefix is not None:
                self._values["prefix"] = prefix
            if range is not None:
                self._values["range"] = range
            if regex is not None:
                self._values["regex"] = regex
            if suffix is not None:
                self._values["suffix"] = suffix

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteRangeMatchProperty"]]:
            '''``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Range``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-range
            '''
            result = self._values.get("range")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteRangeMatchProperty"]], result)

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Regex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def suffix(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-suffix
            '''
            result = self._values.get("suffix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpGatewayRouteHeaderMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpGatewayRouteHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "invert": "invert", "match": "match"},
    )
    class HttpGatewayRouteHeaderProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            invert: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            match: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty"]] = None,
        ) -> None:
            '''
            :param name: ``CfnGatewayRoute.HttpGatewayRouteHeaderProperty.Name``.
            :param invert: ``CfnGatewayRoute.HttpGatewayRouteHeaderProperty.Invert``.
            :param match: ``CfnGatewayRoute.HttpGatewayRouteHeaderProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if invert is not None:
                self._values["invert"] = invert
            if match is not None:
                self._values["match"] = match

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnGatewayRoute.HttpGatewayRouteHeaderProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invert(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnGatewayRoute.HttpGatewayRouteHeaderProperty.Invert``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-invert
            '''
            result = self._values.get("invert")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def match(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty"]]:
            '''``CfnGatewayRoute.HttpGatewayRouteHeaderProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-match
            '''
            result = self._values.get("match")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteHeaderMatchProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpGatewayRouteHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpGatewayRouteMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "headers": "headers",
            "hostname": "hostname",
            "method": "method",
            "path": "path",
            "prefix": "prefix",
            "query_parameters": "queryParameters",
        },
    )
    class HttpGatewayRouteMatchProperty:
        def __init__(
            self,
            *,
            headers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteHeaderProperty"]]]] = None,
            hostname: typing.Optional[typing.Union["CfnGatewayRoute.GatewayRouteHostnameMatchProperty", aws_cdk.core.IResolvable]] = None,
            method: typing.Optional[builtins.str] = None,
            path: typing.Optional[typing.Union["CfnGatewayRoute.HttpPathMatchProperty", aws_cdk.core.IResolvable]] = None,
            prefix: typing.Optional[builtins.str] = None,
            query_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.QueryParameterProperty"]]]] = None,
        ) -> None:
            '''
            :param headers: ``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Headers``.
            :param hostname: ``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Hostname``.
            :param method: ``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Method``.
            :param path: ``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Path``.
            :param prefix: ``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Prefix``.
            :param query_parameters: ``CfnGatewayRoute.HttpGatewayRouteMatchProperty.QueryParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if headers is not None:
                self._values["headers"] = headers
            if hostname is not None:
                self._values["hostname"] = hostname
            if method is not None:
                self._values["method"] = method
            if path is not None:
                self._values["path"] = path
            if prefix is not None:
                self._values["prefix"] = prefix
            if query_parameters is not None:
                self._values["query_parameters"] = query_parameters

        @builtins.property
        def headers(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteHeaderProperty"]]]]:
            '''``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Headers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-headers
            '''
            result = self._values.get("headers")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteHeaderProperty"]]]], result)

        @builtins.property
        def hostname(
            self,
        ) -> typing.Optional[typing.Union["CfnGatewayRoute.GatewayRouteHostnameMatchProperty", aws_cdk.core.IResolvable]]:
            '''``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Hostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-hostname
            '''
            result = self._values.get("hostname")
            return typing.cast(typing.Optional[typing.Union["CfnGatewayRoute.GatewayRouteHostnameMatchProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def method(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Method``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def path(
            self,
        ) -> typing.Optional[typing.Union["CfnGatewayRoute.HttpPathMatchProperty", aws_cdk.core.IResolvable]]:
            '''``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[typing.Union["CfnGatewayRoute.HttpPathMatchProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpGatewayRouteMatchProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.QueryParameterProperty"]]]]:
            '''``CfnGatewayRoute.HttpGatewayRouteMatchProperty.QueryParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-queryparameters
            '''
            result = self._values.get("query_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.QueryParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpGatewayRouteMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty",
        jsii_struct_bases=[],
        name_mapping={"exact": "exact"},
    )
    class HttpGatewayRoutePathRewriteProperty:
        def __init__(self, *, exact: typing.Optional[builtins.str] = None) -> None:
            '''
            :param exact: ``CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html#cfn-appmesh-gatewayroute-httpgatewayroutepathrewrite-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpGatewayRoutePathRewriteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty",
        jsii_struct_bases=[],
        name_mapping={"default_prefix": "defaultPrefix", "value": "value"},
    )
    class HttpGatewayRoutePrefixRewriteProperty:
        def __init__(
            self,
            *,
            default_prefix: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param default_prefix: ``CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty.DefaultPrefix``.
            :param value: ``CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_prefix is not None:
                self._values["default_prefix"] = default_prefix
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def default_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty.DefaultPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-defaultprefix
            '''
            result = self._values.get("default_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpGatewayRoutePrefixRewriteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpGatewayRouteProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "match": "match"},
    )
    class HttpGatewayRouteProperty:
        def __init__(
            self,
            *,
            action: typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteActionProperty"],
            match: typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteMatchProperty"],
        ) -> None:
            '''
            :param action: ``CfnGatewayRoute.HttpGatewayRouteProperty.Action``.
            :param match: ``CfnGatewayRoute.HttpGatewayRouteProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
                "match": match,
            }

        @builtins.property
        def action(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteActionProperty"]:
            '''``CfnGatewayRoute.HttpGatewayRouteProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteActionProperty"], result)

        @builtins.property
        def match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteMatchProperty"]:
            '''``CfnGatewayRoute.HttpGatewayRouteProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-match
            '''
            result = self._values.get("match")
            assert result is not None, "Required property 'match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRouteMatchProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpGatewayRouteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpGatewayRouteRewriteProperty",
        jsii_struct_bases=[],
        name_mapping={"hostname": "hostname", "path": "path", "prefix": "prefix"},
    )
    class HttpGatewayRouteRewriteProperty:
        def __init__(
            self,
            *,
            hostname: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteHostnameRewriteProperty"]] = None,
            path: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty"]] = None,
            prefix: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty"]] = None,
        ) -> None:
            '''
            :param hostname: ``CfnGatewayRoute.HttpGatewayRouteRewriteProperty.Hostname``.
            :param path: ``CfnGatewayRoute.HttpGatewayRouteRewriteProperty.Path``.
            :param prefix: ``CfnGatewayRoute.HttpGatewayRouteRewriteProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if hostname is not None:
                self._values["hostname"] = hostname
            if path is not None:
                self._values["path"] = path
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def hostname(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteHostnameRewriteProperty"]]:
            '''``CfnGatewayRoute.HttpGatewayRouteRewriteProperty.Hostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-hostname
            '''
            result = self._values.get("hostname")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.GatewayRouteHostnameRewriteProperty"]], result)

        @builtins.property
        def path(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty"]]:
            '''``CfnGatewayRoute.HttpGatewayRouteRewriteProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty"]], result)

        @builtins.property
        def prefix(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty"]]:
            '''``CfnGatewayRoute.HttpGatewayRouteRewriteProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpGatewayRouteRewriteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpPathMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"exact": "exact", "regex": "regex"},
    )
    class HttpPathMatchProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[builtins.str] = None,
            regex: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param exact: ``CfnGatewayRoute.HttpPathMatchProperty.Exact``.
            :param regex: ``CfnGatewayRoute.HttpPathMatchProperty.Regex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact
            if regex is not None:
                self._values["regex"] = regex

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpPathMatchProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html#cfn-appmesh-gatewayroute-httppathmatch-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpPathMatchProperty.Regex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html#cfn-appmesh-gatewayroute-httppathmatch-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpPathMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.HttpQueryParameterMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"exact": "exact"},
    )
    class HttpQueryParameterMatchProperty:
        def __init__(self, *, exact: typing.Optional[builtins.str] = None) -> None:
            '''
            :param exact: ``CfnGatewayRoute.HttpQueryParameterMatchProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnGatewayRoute.HttpQueryParameterMatchProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html#cfn-appmesh-gatewayroute-httpqueryparametermatch-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpQueryParameterMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRoute.QueryParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "match": "match"},
    )
    class QueryParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            match: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpQueryParameterMatchProperty"]] = None,
        ) -> None:
            '''
            :param name: ``CfnGatewayRoute.QueryParameterProperty.Name``.
            :param match: ``CfnGatewayRoute.QueryParameterProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if match is not None:
                self._values["match"] = match

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnGatewayRoute.QueryParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html#cfn-appmesh-gatewayroute-queryparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def match(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpQueryParameterMatchProperty"]]:
            '''``CfnGatewayRoute.QueryParameterProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html#cfn-appmesh-gatewayroute-queryparameter-match
            '''
            result = self._values.get("match")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGatewayRoute.HttpQueryParameterMatchProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.CfnGatewayRouteProps",
    jsii_struct_bases=[],
    name_mapping={
        "mesh_name": "meshName",
        "spec": "spec",
        "virtual_gateway_name": "virtualGatewayName",
        "gateway_route_name": "gatewayRouteName",
        "mesh_owner": "meshOwner",
        "tags": "tags",
    },
)
class CfnGatewayRouteProps:
    def __init__(
        self,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[CfnGatewayRoute.GatewayRouteSpecProperty, aws_cdk.core.IResolvable],
        virtual_gateway_name: builtins.str,
        gateway_route_name: typing.Optional[builtins.str] = None,
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppMesh::GatewayRoute``.

        :param mesh_name: ``AWS::AppMesh::GatewayRoute.MeshName``.
        :param spec: ``AWS::AppMesh::GatewayRoute.Spec``.
        :param virtual_gateway_name: ``AWS::AppMesh::GatewayRoute.VirtualGatewayName``.
        :param gateway_route_name: ``AWS::AppMesh::GatewayRoute.GatewayRouteName``.
        :param mesh_owner: ``AWS::AppMesh::GatewayRoute.MeshOwner``.
        :param tags: ``AWS::AppMesh::GatewayRoute.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh_name": mesh_name,
            "spec": spec,
            "virtual_gateway_name": virtual_gateway_name,
        }
        if gateway_route_name is not None:
            self._values["gateway_route_name"] = gateway_route_name
        if mesh_owner is not None:
            self._values["mesh_owner"] = mesh_owner
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::GatewayRoute.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshname
        '''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Union[CfnGatewayRoute.GatewayRouteSpecProperty, aws_cdk.core.IResolvable]:
        '''``AWS::AppMesh::GatewayRoute.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast(typing.Union[CfnGatewayRoute.GatewayRouteSpecProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def virtual_gateway_name(self) -> builtins.str:
        '''``AWS::AppMesh::GatewayRoute.VirtualGatewayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-virtualgatewayname
        '''
        result = self._values.get("virtual_gateway_name")
        assert result is not None, "Required property 'virtual_gateway_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gateway_route_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::GatewayRoute.GatewayRouteName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-gatewayroutename
        '''
        result = self._values.get("gateway_route_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::GatewayRoute.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshowner
        '''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppMesh::GatewayRoute.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGatewayRouteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMesh(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.CfnMesh",
):
    '''A CloudFormation ``AWS::AppMesh::Mesh``.

    :cloudformationResource: AWS::AppMesh::Mesh
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        mesh_name: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMesh.MeshSpecProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::AppMesh::Mesh``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param mesh_name: ``AWS::AppMesh::Mesh.MeshName``.
        :param spec: ``AWS::AppMesh::Mesh.Spec``.
        :param tags: ``AWS::AppMesh::Mesh.Tags``.
        '''
        props = CfnMeshProps(mesh_name=mesh_name, spec=spec, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshName")
    def attr_mesh_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshOwner")
    def attr_mesh_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceOwner")
    def attr_resource_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUid")
    def attr_uid(self) -> builtins.str:
        '''
        :cloudformationAttribute: Uid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppMesh::Mesh.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::Mesh.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-meshname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "meshName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="spec")
    def spec(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMesh.MeshSpecProperty"]]:
        '''``AWS::AppMesh::Mesh.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-spec
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMesh.MeshSpecProperty"]], jsii.get(self, "spec"))

    @spec.setter
    def spec(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMesh.MeshSpecProperty"]],
    ) -> None:
        jsii.set(self, "spec", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnMesh.EgressFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class EgressFilterProperty:
        def __init__(self, *, type: builtins.str) -> None:
            '''
            :param type: ``CfnMesh.EgressFilterProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnMesh.EgressFilterProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html#cfn-appmesh-mesh-egressfilter-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EgressFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnMesh.MeshSpecProperty",
        jsii_struct_bases=[],
        name_mapping={"egress_filter": "egressFilter"},
    )
    class MeshSpecProperty:
        def __init__(
            self,
            *,
            egress_filter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMesh.EgressFilterProperty"]] = None,
        ) -> None:
            '''
            :param egress_filter: ``CfnMesh.MeshSpecProperty.EgressFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if egress_filter is not None:
                self._values["egress_filter"] = egress_filter

        @builtins.property
        def egress_filter(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMesh.EgressFilterProperty"]]:
            '''``CfnMesh.MeshSpecProperty.EgressFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html#cfn-appmesh-mesh-meshspec-egressfilter
            '''
            result = self._values.get("egress_filter")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMesh.EgressFilterProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MeshSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.CfnMeshProps",
    jsii_struct_bases=[],
    name_mapping={"mesh_name": "meshName", "spec": "spec", "tags": "tags"},
)
class CfnMeshProps:
    def __init__(
        self,
        *,
        mesh_name: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMesh.MeshSpecProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppMesh::Mesh``.

        :param mesh_name: ``AWS::AppMesh::Mesh.MeshName``.
        :param spec: ``AWS::AppMesh::Mesh.Spec``.
        :param tags: ``AWS::AppMesh::Mesh.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if mesh_name is not None:
            self._values["mesh_name"] = mesh_name
        if spec is not None:
            self._values["spec"] = spec
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def mesh_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::Mesh.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-meshname
        '''
        result = self._values.get("mesh_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMesh.MeshSpecProperty]]:
        '''``AWS::AppMesh::Mesh.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMesh.MeshSpecProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppMesh::Mesh.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMeshProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRoute(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.CfnRoute",
):
    '''A CloudFormation ``AWS::AppMesh::Route``.

    :cloudformationResource: AWS::AppMesh::Route
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, "CfnRoute.RouteSpecProperty"],
        virtual_router_name: builtins.str,
        mesh_owner: typing.Optional[builtins.str] = None,
        route_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::AppMesh::Route``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param mesh_name: ``AWS::AppMesh::Route.MeshName``.
        :param spec: ``AWS::AppMesh::Route.Spec``.
        :param virtual_router_name: ``AWS::AppMesh::Route.VirtualRouterName``.
        :param mesh_owner: ``AWS::AppMesh::Route.MeshOwner``.
        :param route_name: ``AWS::AppMesh::Route.RouteName``.
        :param tags: ``AWS::AppMesh::Route.Tags``.
        '''
        props = CfnRouteProps(
            mesh_name=mesh_name,
            spec=spec,
            virtual_router_name=virtual_router_name,
            mesh_owner=mesh_owner,
            route_name=route_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshName")
    def attr_mesh_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshOwner")
    def attr_mesh_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceOwner")
    def attr_resource_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRouteName")
    def attr_route_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: RouteName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRouteName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUid")
    def attr_uid(self) -> builtins.str:
        '''
        :cloudformationAttribute: Uid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVirtualRouterName")
    def attr_virtual_router_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: VirtualRouterName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualRouterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppMesh::Route.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::Route.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshname
        '''
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        jsii.set(self, "meshName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="spec")
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRoute.RouteSpecProperty"]:
        '''``AWS::AppMesh::Route.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-spec
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRoute.RouteSpecProperty"], jsii.get(self, "spec"))

    @spec.setter
    def spec(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnRoute.RouteSpecProperty"],
    ) -> None:
        jsii.set(self, "spec", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouterName")
    def virtual_router_name(self) -> builtins.str:
        '''``AWS::AppMesh::Route.VirtualRouterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-virtualroutername
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualRouterName"))

    @virtual_router_name.setter
    def virtual_router_name(self, value: builtins.str) -> None:
        jsii.set(self, "virtualRouterName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::Route.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshowner
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "meshOwner", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routeName")
    def route_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::Route.RouteName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-routename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeName"))

    @route_name.setter
    def route_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "routeName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.DurationProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class DurationProperty:
        def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
            '''
            :param unit: ``CfnRoute.DurationProperty.Unit``.
            :param value: ``CfnRoute.DurationProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''``CfnRoute.DurationProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html#cfn-appmesh-route-duration-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''``CfnRoute.DurationProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html#cfn-appmesh-route-duration-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.GrpcRetryPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_retries": "maxRetries",
            "per_retry_timeout": "perRetryTimeout",
            "grpc_retry_events": "grpcRetryEvents",
            "http_retry_events": "httpRetryEvents",
            "tcp_retry_events": "tcpRetryEvents",
        },
    )
    class GrpcRetryPolicyProperty:
        def __init__(
            self,
            *,
            max_retries: jsii.Number,
            per_retry_timeout: typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"],
            grpc_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
            http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
            tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param max_retries: ``CfnRoute.GrpcRetryPolicyProperty.MaxRetries``.
            :param per_retry_timeout: ``CfnRoute.GrpcRetryPolicyProperty.PerRetryTimeout``.
            :param grpc_retry_events: ``CfnRoute.GrpcRetryPolicyProperty.GrpcRetryEvents``.
            :param http_retry_events: ``CfnRoute.GrpcRetryPolicyProperty.HttpRetryEvents``.
            :param tcp_retry_events: ``CfnRoute.GrpcRetryPolicyProperty.TcpRetryEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_retries": max_retries,
                "per_retry_timeout": per_retry_timeout,
            }
            if grpc_retry_events is not None:
                self._values["grpc_retry_events"] = grpc_retry_events
            if http_retry_events is not None:
                self._values["http_retry_events"] = http_retry_events
            if tcp_retry_events is not None:
                self._values["tcp_retry_events"] = tcp_retry_events

        @builtins.property
        def max_retries(self) -> jsii.Number:
            '''``CfnRoute.GrpcRetryPolicyProperty.MaxRetries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-maxretries
            '''
            result = self._values.get("max_retries")
            assert result is not None, "Required property 'max_retries' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def per_retry_timeout(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]:
            '''``CfnRoute.GrpcRetryPolicyProperty.PerRetryTimeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-perretrytimeout
            '''
            result = self._values.get("per_retry_timeout")
            assert result is not None, "Required property 'per_retry_timeout' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"], result)

        @builtins.property
        def grpc_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRoute.GrpcRetryPolicyProperty.GrpcRetryEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-grpcretryevents
            '''
            result = self._values.get("grpc_retry_events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def http_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRoute.GrpcRetryPolicyProperty.HttpRetryEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-httpretryevents
            '''
            result = self._values.get("http_retry_events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tcp_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRoute.GrpcRetryPolicyProperty.TcpRetryEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-tcpretryevents
            '''
            result = self._values.get("tcp_retry_events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcRetryPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.GrpcRouteActionProperty",
        jsii_struct_bases=[],
        name_mapping={"weighted_targets": "weightedTargets"},
    )
    class GrpcRouteActionProperty:
        def __init__(
            self,
            *,
            weighted_targets: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.WeightedTargetProperty"]]],
        ) -> None:
            '''
            :param weighted_targets: ``CfnRoute.GrpcRouteActionProperty.WeightedTargets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "weighted_targets": weighted_targets,
            }

        @builtins.property
        def weighted_targets(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.WeightedTargetProperty"]]]:
            '''``CfnRoute.GrpcRouteActionProperty.WeightedTargets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html#cfn-appmesh-route-grpcrouteaction-weightedtargets
            '''
            result = self._values.get("weighted_targets")
            assert result is not None, "Required property 'weighted_targets' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.WeightedTargetProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcRouteActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.GrpcRouteMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metadata": "metadata",
            "method_name": "methodName",
            "service_name": "serviceName",
        },
    )
    class GrpcRouteMatchProperty:
        def __init__(
            self,
            *,
            metadata: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteMetadataProperty"]]]] = None,
            method_name: typing.Optional[builtins.str] = None,
            service_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param metadata: ``CfnRoute.GrpcRouteMatchProperty.Metadata``.
            :param method_name: ``CfnRoute.GrpcRouteMatchProperty.MethodName``.
            :param service_name: ``CfnRoute.GrpcRouteMatchProperty.ServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if metadata is not None:
                self._values["metadata"] = metadata
            if method_name is not None:
                self._values["method_name"] = method_name
            if service_name is not None:
                self._values["service_name"] = service_name

        @builtins.property
        def metadata(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteMetadataProperty"]]]]:
            '''``CfnRoute.GrpcRouteMatchProperty.Metadata``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-metadata
            '''
            result = self._values.get("metadata")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteMetadataProperty"]]]], result)

        @builtins.property
        def method_name(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.GrpcRouteMatchProperty.MethodName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-methodname
            '''
            result = self._values.get("method_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_name(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.GrpcRouteMatchProperty.ServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-servicename
            '''
            result = self._values.get("service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcRouteMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.GrpcRouteMetadataMatchMethodProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exact": "exact",
            "prefix": "prefix",
            "range": "range",
            "regex": "regex",
            "suffix": "suffix",
        },
    )
    class GrpcRouteMetadataMatchMethodProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            range: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.MatchRangeProperty"]] = None,
            regex: typing.Optional[builtins.str] = None,
            suffix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param exact: ``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Exact``.
            :param prefix: ``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Prefix``.
            :param range: ``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Range``.
            :param regex: ``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Regex``.
            :param suffix: ``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact
            if prefix is not None:
                self._values["prefix"] = prefix
            if range is not None:
                self._values["range"] = range
            if regex is not None:
                self._values["regex"] = regex
            if suffix is not None:
                self._values["suffix"] = suffix

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.MatchRangeProperty"]]:
            '''``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Range``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-range
            '''
            result = self._values.get("range")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.MatchRangeProperty"]], result)

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Regex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def suffix(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.GrpcRouteMetadataMatchMethodProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-suffix
            '''
            result = self._values.get("suffix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcRouteMetadataMatchMethodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.GrpcRouteMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "invert": "invert", "match": "match"},
    )
    class GrpcRouteMetadataProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            invert: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            match: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteMetadataMatchMethodProperty"]] = None,
        ) -> None:
            '''
            :param name: ``CfnRoute.GrpcRouteMetadataProperty.Name``.
            :param invert: ``CfnRoute.GrpcRouteMetadataProperty.Invert``.
            :param match: ``CfnRoute.GrpcRouteMetadataProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if invert is not None:
                self._values["invert"] = invert
            if match is not None:
                self._values["match"] = match

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnRoute.GrpcRouteMetadataProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invert(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnRoute.GrpcRouteMetadataProperty.Invert``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-invert
            '''
            result = self._values.get("invert")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def match(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteMetadataMatchMethodProperty"]]:
            '''``CfnRoute.GrpcRouteMetadataProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-match
            '''
            result = self._values.get("match")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteMetadataMatchMethodProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcRouteMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.GrpcRouteProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "match": "match",
            "retry_policy": "retryPolicy",
            "timeout": "timeout",
        },
    )
    class GrpcRouteProperty:
        def __init__(
            self,
            *,
            action: typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteActionProperty"],
            match: typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteMatchProperty"],
            retry_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRetryPolicyProperty"]] = None,
            timeout: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcTimeoutProperty"]] = None,
        ) -> None:
            '''
            :param action: ``CfnRoute.GrpcRouteProperty.Action``.
            :param match: ``CfnRoute.GrpcRouteProperty.Match``.
            :param retry_policy: ``CfnRoute.GrpcRouteProperty.RetryPolicy``.
            :param timeout: ``CfnRoute.GrpcRouteProperty.Timeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
                "match": match,
            }
            if retry_policy is not None:
                self._values["retry_policy"] = retry_policy
            if timeout is not None:
                self._values["timeout"] = timeout

        @builtins.property
        def action(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteActionProperty"]:
            '''``CfnRoute.GrpcRouteProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteActionProperty"], result)

        @builtins.property
        def match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteMatchProperty"]:
            '''``CfnRoute.GrpcRouteProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-match
            '''
            result = self._values.get("match")
            assert result is not None, "Required property 'match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteMatchProperty"], result)

        @builtins.property
        def retry_policy(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRetryPolicyProperty"]]:
            '''``CfnRoute.GrpcRouteProperty.RetryPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-retrypolicy
            '''
            result = self._values.get("retry_policy")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRetryPolicyProperty"]], result)

        @builtins.property
        def timeout(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcTimeoutProperty"]]:
            '''``CfnRoute.GrpcRouteProperty.Timeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcTimeoutProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcRouteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.GrpcTimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"idle": "idle", "per_request": "perRequest"},
    )
    class GrpcTimeoutProperty:
        def __init__(
            self,
            *,
            idle: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]] = None,
            per_request: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]] = None,
        ) -> None:
            '''
            :param idle: ``CfnRoute.GrpcTimeoutProperty.Idle``.
            :param per_request: ``CfnRoute.GrpcTimeoutProperty.PerRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if idle is not None:
                self._values["idle"] = idle
            if per_request is not None:
                self._values["per_request"] = per_request

        @builtins.property
        def idle(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]]:
            '''``CfnRoute.GrpcTimeoutProperty.Idle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-idle
            '''
            result = self._values.get("idle")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]], result)

        @builtins.property
        def per_request(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]]:
            '''``CfnRoute.GrpcTimeoutProperty.PerRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-perrequest
            '''
            result = self._values.get("per_request")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcTimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.HeaderMatchMethodProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exact": "exact",
            "prefix": "prefix",
            "range": "range",
            "regex": "regex",
            "suffix": "suffix",
        },
    )
    class HeaderMatchMethodProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            range: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.MatchRangeProperty"]] = None,
            regex: typing.Optional[builtins.str] = None,
            suffix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param exact: ``CfnRoute.HeaderMatchMethodProperty.Exact``.
            :param prefix: ``CfnRoute.HeaderMatchMethodProperty.Prefix``.
            :param range: ``CfnRoute.HeaderMatchMethodProperty.Range``.
            :param regex: ``CfnRoute.HeaderMatchMethodProperty.Regex``.
            :param suffix: ``CfnRoute.HeaderMatchMethodProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact
            if prefix is not None:
                self._values["prefix"] = prefix
            if range is not None:
                self._values["range"] = range
            if regex is not None:
                self._values["regex"] = regex
            if suffix is not None:
                self._values["suffix"] = suffix

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HeaderMatchMethodProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HeaderMatchMethodProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.MatchRangeProperty"]]:
            '''``CfnRoute.HeaderMatchMethodProperty.Range``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-range
            '''
            result = self._values.get("range")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.MatchRangeProperty"]], result)

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HeaderMatchMethodProperty.Regex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def suffix(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HeaderMatchMethodProperty.Suffix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-suffix
            '''
            result = self._values.get("suffix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HeaderMatchMethodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.HttpPathMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"exact": "exact", "regex": "regex"},
    )
    class HttpPathMatchProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[builtins.str] = None,
            regex: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param exact: ``CfnRoute.HttpPathMatchProperty.Exact``.
            :param regex: ``CfnRoute.HttpPathMatchProperty.Regex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact
            if regex is not None:
                self._values["regex"] = regex

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HttpPathMatchProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html#cfn-appmesh-route-httppathmatch-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HttpPathMatchProperty.Regex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html#cfn-appmesh-route-httppathmatch-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpPathMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.HttpQueryParameterMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"exact": "exact"},
    )
    class HttpQueryParameterMatchProperty:
        def __init__(self, *, exact: typing.Optional[builtins.str] = None) -> None:
            '''
            :param exact: ``CfnRoute.HttpQueryParameterMatchProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HttpQueryParameterMatchProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html#cfn-appmesh-route-httpqueryparametermatch-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpQueryParameterMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.HttpRetryPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_retries": "maxRetries",
            "per_retry_timeout": "perRetryTimeout",
            "http_retry_events": "httpRetryEvents",
            "tcp_retry_events": "tcpRetryEvents",
        },
    )
    class HttpRetryPolicyProperty:
        def __init__(
            self,
            *,
            max_retries: jsii.Number,
            per_retry_timeout: typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"],
            http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
            tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param max_retries: ``CfnRoute.HttpRetryPolicyProperty.MaxRetries``.
            :param per_retry_timeout: ``CfnRoute.HttpRetryPolicyProperty.PerRetryTimeout``.
            :param http_retry_events: ``CfnRoute.HttpRetryPolicyProperty.HttpRetryEvents``.
            :param tcp_retry_events: ``CfnRoute.HttpRetryPolicyProperty.TcpRetryEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_retries": max_retries,
                "per_retry_timeout": per_retry_timeout,
            }
            if http_retry_events is not None:
                self._values["http_retry_events"] = http_retry_events
            if tcp_retry_events is not None:
                self._values["tcp_retry_events"] = tcp_retry_events

        @builtins.property
        def max_retries(self) -> jsii.Number:
            '''``CfnRoute.HttpRetryPolicyProperty.MaxRetries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-maxretries
            '''
            result = self._values.get("max_retries")
            assert result is not None, "Required property 'max_retries' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def per_retry_timeout(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]:
            '''``CfnRoute.HttpRetryPolicyProperty.PerRetryTimeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-perretrytimeout
            '''
            result = self._values.get("per_retry_timeout")
            assert result is not None, "Required property 'per_retry_timeout' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"], result)

        @builtins.property
        def http_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRoute.HttpRetryPolicyProperty.HttpRetryEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-httpretryevents
            '''
            result = self._values.get("http_retry_events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tcp_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRoute.HttpRetryPolicyProperty.TcpRetryEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-tcpretryevents
            '''
            result = self._values.get("tcp_retry_events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpRetryPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.HttpRouteActionProperty",
        jsii_struct_bases=[],
        name_mapping={"weighted_targets": "weightedTargets"},
    )
    class HttpRouteActionProperty:
        def __init__(
            self,
            *,
            weighted_targets: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.WeightedTargetProperty"]]],
        ) -> None:
            '''
            :param weighted_targets: ``CfnRoute.HttpRouteActionProperty.WeightedTargets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "weighted_targets": weighted_targets,
            }

        @builtins.property
        def weighted_targets(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.WeightedTargetProperty"]]]:
            '''``CfnRoute.HttpRouteActionProperty.WeightedTargets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html#cfn-appmesh-route-httprouteaction-weightedtargets
            '''
            result = self._values.get("weighted_targets")
            assert result is not None, "Required property 'weighted_targets' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.WeightedTargetProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpRouteActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.HttpRouteHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "invert": "invert", "match": "match"},
    )
    class HttpRouteHeaderProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            invert: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            match: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HeaderMatchMethodProperty"]] = None,
        ) -> None:
            '''
            :param name: ``CfnRoute.HttpRouteHeaderProperty.Name``.
            :param invert: ``CfnRoute.HttpRouteHeaderProperty.Invert``.
            :param match: ``CfnRoute.HttpRouteHeaderProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if invert is not None:
                self._values["invert"] = invert
            if match is not None:
                self._values["match"] = match

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnRoute.HttpRouteHeaderProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invert(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnRoute.HttpRouteHeaderProperty.Invert``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-invert
            '''
            result = self._values.get("invert")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def match(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HeaderMatchMethodProperty"]]:
            '''``CfnRoute.HttpRouteHeaderProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-match
            '''
            result = self._values.get("match")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HeaderMatchMethodProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpRouteHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.HttpRouteMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "headers": "headers",
            "method": "method",
            "path": "path",
            "prefix": "prefix",
            "query_parameters": "queryParameters",
            "scheme": "scheme",
        },
    )
    class HttpRouteMatchProperty:
        def __init__(
            self,
            *,
            headers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnRoute.HttpRouteHeaderProperty", aws_cdk.core.IResolvable]]]] = None,
            method: typing.Optional[builtins.str] = None,
            path: typing.Optional[typing.Union["CfnRoute.HttpPathMatchProperty", aws_cdk.core.IResolvable]] = None,
            prefix: typing.Optional[builtins.str] = None,
            query_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnRoute.QueryParameterProperty", aws_cdk.core.IResolvable]]]] = None,
            scheme: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param headers: ``CfnRoute.HttpRouteMatchProperty.Headers``.
            :param method: ``CfnRoute.HttpRouteMatchProperty.Method``.
            :param path: ``CfnRoute.HttpRouteMatchProperty.Path``.
            :param prefix: ``CfnRoute.HttpRouteMatchProperty.Prefix``.
            :param query_parameters: ``CfnRoute.HttpRouteMatchProperty.QueryParameters``.
            :param scheme: ``CfnRoute.HttpRouteMatchProperty.Scheme``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if headers is not None:
                self._values["headers"] = headers
            if method is not None:
                self._values["method"] = method
            if path is not None:
                self._values["path"] = path
            if prefix is not None:
                self._values["prefix"] = prefix
            if query_parameters is not None:
                self._values["query_parameters"] = query_parameters
            if scheme is not None:
                self._values["scheme"] = scheme

        @builtins.property
        def headers(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnRoute.HttpRouteHeaderProperty", aws_cdk.core.IResolvable]]]]:
            '''``CfnRoute.HttpRouteMatchProperty.Headers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-headers
            '''
            result = self._values.get("headers")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnRoute.HttpRouteHeaderProperty", aws_cdk.core.IResolvable]]]], result)

        @builtins.property
        def method(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HttpRouteMatchProperty.Method``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def path(
            self,
        ) -> typing.Optional[typing.Union["CfnRoute.HttpPathMatchProperty", aws_cdk.core.IResolvable]]:
            '''``CfnRoute.HttpRouteMatchProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[typing.Union["CfnRoute.HttpPathMatchProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HttpRouteMatchProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnRoute.QueryParameterProperty", aws_cdk.core.IResolvable]]]]:
            '''``CfnRoute.HttpRouteMatchProperty.QueryParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-queryparameters
            '''
            result = self._values.get("query_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnRoute.QueryParameterProperty", aws_cdk.core.IResolvable]]]], result)

        @builtins.property
        def scheme(self) -> typing.Optional[builtins.str]:
            '''``CfnRoute.HttpRouteMatchProperty.Scheme``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-scheme
            '''
            result = self._values.get("scheme")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpRouteMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.HttpRouteProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "match": "match",
            "retry_policy": "retryPolicy",
            "timeout": "timeout",
        },
    )
    class HttpRouteProperty:
        def __init__(
            self,
            *,
            action: typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpRouteActionProperty"],
            match: typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpRouteMatchProperty"],
            retry_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpRetryPolicyProperty"]] = None,
            timeout: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpTimeoutProperty"]] = None,
        ) -> None:
            '''
            :param action: ``CfnRoute.HttpRouteProperty.Action``.
            :param match: ``CfnRoute.HttpRouteProperty.Match``.
            :param retry_policy: ``CfnRoute.HttpRouteProperty.RetryPolicy``.
            :param timeout: ``CfnRoute.HttpRouteProperty.Timeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
                "match": match,
            }
            if retry_policy is not None:
                self._values["retry_policy"] = retry_policy
            if timeout is not None:
                self._values["timeout"] = timeout

        @builtins.property
        def action(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpRouteActionProperty"]:
            '''``CfnRoute.HttpRouteProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpRouteActionProperty"], result)

        @builtins.property
        def match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpRouteMatchProperty"]:
            '''``CfnRoute.HttpRouteProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-match
            '''
            result = self._values.get("match")
            assert result is not None, "Required property 'match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpRouteMatchProperty"], result)

        @builtins.property
        def retry_policy(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpRetryPolicyProperty"]]:
            '''``CfnRoute.HttpRouteProperty.RetryPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-retrypolicy
            '''
            result = self._values.get("retry_policy")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpRetryPolicyProperty"]], result)

        @builtins.property
        def timeout(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpTimeoutProperty"]]:
            '''``CfnRoute.HttpRouteProperty.Timeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpTimeoutProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpRouteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.HttpTimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"idle": "idle", "per_request": "perRequest"},
    )
    class HttpTimeoutProperty:
        def __init__(
            self,
            *,
            idle: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]] = None,
            per_request: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]] = None,
        ) -> None:
            '''
            :param idle: ``CfnRoute.HttpTimeoutProperty.Idle``.
            :param per_request: ``CfnRoute.HttpTimeoutProperty.PerRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if idle is not None:
                self._values["idle"] = idle
            if per_request is not None:
                self._values["per_request"] = per_request

        @builtins.property
        def idle(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]]:
            '''``CfnRoute.HttpTimeoutProperty.Idle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-idle
            '''
            result = self._values.get("idle")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]], result)

        @builtins.property
        def per_request(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]]:
            '''``CfnRoute.HttpTimeoutProperty.PerRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-perrequest
            '''
            result = self._values.get("per_request")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpTimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.MatchRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class MatchRangeProperty:
        def __init__(self, *, end: jsii.Number, start: jsii.Number) -> None:
            '''
            :param end: ``CfnRoute.MatchRangeProperty.End``.
            :param start: ``CfnRoute.MatchRangeProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "end": end,
                "start": start,
            }

        @builtins.property
        def end(self) -> jsii.Number:
            '''``CfnRoute.MatchRangeProperty.End``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html#cfn-appmesh-route-matchrange-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def start(self) -> jsii.Number:
            '''``CfnRoute.MatchRangeProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html#cfn-appmesh-route-matchrange-start
            '''
            result = self._values.get("start")
            assert result is not None, "Required property 'start' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MatchRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.QueryParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "match": "match"},
    )
    class QueryParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            match: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpQueryParameterMatchProperty"]] = None,
        ) -> None:
            '''
            :param name: ``CfnRoute.QueryParameterProperty.Name``.
            :param match: ``CfnRoute.QueryParameterProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if match is not None:
                self._values["match"] = match

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnRoute.QueryParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html#cfn-appmesh-route-queryparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def match(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpQueryParameterMatchProperty"]]:
            '''``CfnRoute.QueryParameterProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html#cfn-appmesh-route-queryparameter-match
            '''
            result = self._values.get("match")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.HttpQueryParameterMatchProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.RouteSpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "grpc_route": "grpcRoute",
            "http2_route": "http2Route",
            "http_route": "httpRoute",
            "priority": "priority",
            "tcp_route": "tcpRoute",
        },
    )
    class RouteSpecProperty:
        def __init__(
            self,
            *,
            grpc_route: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteProperty"]] = None,
            http2_route: typing.Optional[typing.Union["CfnRoute.HttpRouteProperty", aws_cdk.core.IResolvable]] = None,
            http_route: typing.Optional[typing.Union["CfnRoute.HttpRouteProperty", aws_cdk.core.IResolvable]] = None,
            priority: typing.Optional[jsii.Number] = None,
            tcp_route: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.TcpRouteProperty"]] = None,
        ) -> None:
            '''
            :param grpc_route: ``CfnRoute.RouteSpecProperty.GrpcRoute``.
            :param http2_route: ``CfnRoute.RouteSpecProperty.Http2Route``.
            :param http_route: ``CfnRoute.RouteSpecProperty.HttpRoute``.
            :param priority: ``CfnRoute.RouteSpecProperty.Priority``.
            :param tcp_route: ``CfnRoute.RouteSpecProperty.TcpRoute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if grpc_route is not None:
                self._values["grpc_route"] = grpc_route
            if http2_route is not None:
                self._values["http2_route"] = http2_route
            if http_route is not None:
                self._values["http_route"] = http_route
            if priority is not None:
                self._values["priority"] = priority
            if tcp_route is not None:
                self._values["tcp_route"] = tcp_route

        @builtins.property
        def grpc_route(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteProperty"]]:
            '''``CfnRoute.RouteSpecProperty.GrpcRoute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-grpcroute
            '''
            result = self._values.get("grpc_route")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.GrpcRouteProperty"]], result)

        @builtins.property
        def http2_route(
            self,
        ) -> typing.Optional[typing.Union["CfnRoute.HttpRouteProperty", aws_cdk.core.IResolvable]]:
            '''``CfnRoute.RouteSpecProperty.Http2Route``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-http2route
            '''
            result = self._values.get("http2_route")
            return typing.cast(typing.Optional[typing.Union["CfnRoute.HttpRouteProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def http_route(
            self,
        ) -> typing.Optional[typing.Union["CfnRoute.HttpRouteProperty", aws_cdk.core.IResolvable]]:
            '''``CfnRoute.RouteSpecProperty.HttpRoute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-httproute
            '''
            result = self._values.get("http_route")
            return typing.cast(typing.Optional[typing.Union["CfnRoute.HttpRouteProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            '''``CfnRoute.RouteSpecProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-priority
            '''
            result = self._values.get("priority")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def tcp_route(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.TcpRouteProperty"]]:
            '''``CfnRoute.RouteSpecProperty.TcpRoute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-tcproute
            '''
            result = self._values.get("tcp_route")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.TcpRouteProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouteSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.TcpRouteActionProperty",
        jsii_struct_bases=[],
        name_mapping={"weighted_targets": "weightedTargets"},
    )
    class TcpRouteActionProperty:
        def __init__(
            self,
            *,
            weighted_targets: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.WeightedTargetProperty"]]],
        ) -> None:
            '''
            :param weighted_targets: ``CfnRoute.TcpRouteActionProperty.WeightedTargets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "weighted_targets": weighted_targets,
            }

        @builtins.property
        def weighted_targets(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.WeightedTargetProperty"]]]:
            '''``CfnRoute.TcpRouteActionProperty.WeightedTargets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html#cfn-appmesh-route-tcprouteaction-weightedtargets
            '''
            result = self._values.get("weighted_targets")
            assert result is not None, "Required property 'weighted_targets' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.WeightedTargetProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TcpRouteActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.TcpRouteProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "timeout": "timeout"},
    )
    class TcpRouteProperty:
        def __init__(
            self,
            *,
            action: typing.Union[aws_cdk.core.IResolvable, "CfnRoute.TcpRouteActionProperty"],
            timeout: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.TcpTimeoutProperty"]] = None,
        ) -> None:
            '''
            :param action: ``CfnRoute.TcpRouteProperty.Action``.
            :param timeout: ``CfnRoute.TcpRouteProperty.Timeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
            }
            if timeout is not None:
                self._values["timeout"] = timeout

        @builtins.property
        def action(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRoute.TcpRouteActionProperty"]:
            '''``CfnRoute.TcpRouteProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRoute.TcpRouteActionProperty"], result)

        @builtins.property
        def timeout(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.TcpTimeoutProperty"]]:
            '''``CfnRoute.TcpRouteProperty.Timeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.TcpTimeoutProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TcpRouteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.TcpTimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"idle": "idle"},
    )
    class TcpTimeoutProperty:
        def __init__(
            self,
            *,
            idle: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]] = None,
        ) -> None:
            '''
            :param idle: ``CfnRoute.TcpTimeoutProperty.Idle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if idle is not None:
                self._values["idle"] = idle

        @builtins.property
        def idle(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]]:
            '''``CfnRoute.TcpTimeoutProperty.Idle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html#cfn-appmesh-route-tcptimeout-idle
            '''
            result = self._values.get("idle")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRoute.DurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TcpTimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnRoute.WeightedTargetProperty",
        jsii_struct_bases=[],
        name_mapping={"virtual_node": "virtualNode", "weight": "weight"},
    )
    class WeightedTargetProperty:
        def __init__(self, *, virtual_node: builtins.str, weight: jsii.Number) -> None:
            '''
            :param virtual_node: ``CfnRoute.WeightedTargetProperty.VirtualNode``.
            :param weight: ``CfnRoute.WeightedTargetProperty.Weight``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "virtual_node": virtual_node,
                "weight": weight,
            }

        @builtins.property
        def virtual_node(self) -> builtins.str:
            '''``CfnRoute.WeightedTargetProperty.VirtualNode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html#cfn-appmesh-route-weightedtarget-virtualnode
            '''
            result = self._values.get("virtual_node")
            assert result is not None, "Required property 'virtual_node' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def weight(self) -> jsii.Number:
            '''``CfnRoute.WeightedTargetProperty.Weight``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html#cfn-appmesh-route-weightedtarget-weight
            '''
            result = self._values.get("weight")
            assert result is not None, "Required property 'weight' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WeightedTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.CfnRouteProps",
    jsii_struct_bases=[],
    name_mapping={
        "mesh_name": "meshName",
        "spec": "spec",
        "virtual_router_name": "virtualRouterName",
        "mesh_owner": "meshOwner",
        "route_name": "routeName",
        "tags": "tags",
    },
)
class CfnRouteProps:
    def __init__(
        self,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, CfnRoute.RouteSpecProperty],
        virtual_router_name: builtins.str,
        mesh_owner: typing.Optional[builtins.str] = None,
        route_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppMesh::Route``.

        :param mesh_name: ``AWS::AppMesh::Route.MeshName``.
        :param spec: ``AWS::AppMesh::Route.Spec``.
        :param virtual_router_name: ``AWS::AppMesh::Route.VirtualRouterName``.
        :param mesh_owner: ``AWS::AppMesh::Route.MeshOwner``.
        :param route_name: ``AWS::AppMesh::Route.RouteName``.
        :param tags: ``AWS::AppMesh::Route.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh_name": mesh_name,
            "spec": spec,
            "virtual_router_name": virtual_router_name,
        }
        if mesh_owner is not None:
            self._values["mesh_owner"] = mesh_owner
        if route_name is not None:
            self._values["route_name"] = route_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::Route.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshname
        '''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnRoute.RouteSpecProperty]:
        '''``AWS::AppMesh::Route.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnRoute.RouteSpecProperty], result)

    @builtins.property
    def virtual_router_name(self) -> builtins.str:
        '''``AWS::AppMesh::Route.VirtualRouterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-virtualroutername
        '''
        result = self._values.get("virtual_router_name")
        assert result is not None, "Required property 'virtual_router_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::Route.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshowner
        '''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::Route.RouteName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-routename
        '''
        result = self._values.get("route_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppMesh::Route.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnVirtualGateway(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway",
):
    '''A CloudFormation ``AWS::AppMesh::VirtualGateway``.

    :cloudformationResource: AWS::AppMesh::VirtualGateway
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewaySpecProperty"],
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        virtual_gateway_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::AppMesh::VirtualGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param mesh_name: ``AWS::AppMesh::VirtualGateway.MeshName``.
        :param spec: ``AWS::AppMesh::VirtualGateway.Spec``.
        :param mesh_owner: ``AWS::AppMesh::VirtualGateway.MeshOwner``.
        :param tags: ``AWS::AppMesh::VirtualGateway.Tags``.
        :param virtual_gateway_name: ``AWS::AppMesh::VirtualGateway.VirtualGatewayName``.
        '''
        props = CfnVirtualGatewayProps(
            mesh_name=mesh_name,
            spec=spec,
            mesh_owner=mesh_owner,
            tags=tags,
            virtual_gateway_name=virtual_gateway_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshName")
    def attr_mesh_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshOwner")
    def attr_mesh_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceOwner")
    def attr_resource_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUid")
    def attr_uid(self) -> builtins.str:
        '''
        :cloudformationAttribute: Uid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVirtualGatewayName")
    def attr_virtual_gateway_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: VirtualGatewayName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualGatewayName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppMesh::VirtualGateway.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualGateway.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshname
        '''
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        jsii.set(self, "meshName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="spec")
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewaySpecProperty"]:
        '''``AWS::AppMesh::VirtualGateway.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-spec
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewaySpecProperty"], jsii.get(self, "spec"))

    @spec.setter
    def spec(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewaySpecProperty"],
    ) -> None:
        jsii.set(self, "spec", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualGateway.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshowner
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "meshOwner", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGatewayName")
    def virtual_gateway_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualGateway.VirtualGatewayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-virtualgatewayname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualGatewayName"))

    @virtual_gateway_name.setter
    def virtual_gateway_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "virtualGatewayName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.SubjectAlternativeNameMatchersProperty",
        jsii_struct_bases=[],
        name_mapping={"exact": "exact"},
    )
    class SubjectAlternativeNameMatchersProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param exact: ``CfnVirtualGateway.SubjectAlternativeNameMatchersProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenamematchers.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact

        @builtins.property
        def exact(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnVirtualGateway.SubjectAlternativeNameMatchersProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenamematchers.html#cfn-appmesh-virtualgateway-subjectalternativenamematchers-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectAlternativeNameMatchersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.SubjectAlternativeNamesProperty",
        jsii_struct_bases=[],
        name_mapping={"match": "match"},
    )
    class SubjectAlternativeNamesProperty:
        def __init__(
            self,
            *,
            match: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.SubjectAlternativeNameMatchersProperty"],
        ) -> None:
            '''
            :param match: ``CfnVirtualGateway.SubjectAlternativeNamesProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "match": match,
            }

        @builtins.property
        def match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.SubjectAlternativeNameMatchersProperty"]:
            '''``CfnVirtualGateway.SubjectAlternativeNamesProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html#cfn-appmesh-virtualgateway-subjectalternativenames-match
            '''
            result = self._values.get("match")
            assert result is not None, "Required property 'match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.SubjectAlternativeNameMatchersProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectAlternativeNamesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayAccessLogProperty",
        jsii_struct_bases=[],
        name_mapping={"file": "file"},
    )
    class VirtualGatewayAccessLogProperty:
        def __init__(
            self,
            *,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayFileAccessLogProperty"]] = None,
        ) -> None:
            '''
            :param file: ``CfnVirtualGateway.VirtualGatewayAccessLogProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if file is not None:
                self._values["file"] = file

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayFileAccessLogProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayAccessLogProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayaccesslog-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayFileAccessLogProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayAccessLogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayBackendDefaultsProperty",
        jsii_struct_bases=[],
        name_mapping={"client_policy": "clientPolicy"},
    )
    class VirtualGatewayBackendDefaultsProperty:
        def __init__(
            self,
            *,
            client_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayClientPolicyProperty"]] = None,
        ) -> None:
            '''
            :param client_policy: ``CfnVirtualGateway.VirtualGatewayBackendDefaultsProperty.ClientPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if client_policy is not None:
                self._values["client_policy"] = client_policy

        @builtins.property
        def client_policy(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayClientPolicyProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayBackendDefaultsProperty.ClientPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html#cfn-appmesh-virtualgateway-virtualgatewaybackenddefaults-clientpolicy
            '''
            result = self._values.get("client_policy")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayClientPolicyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayBackendDefaultsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayClientPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"tls": "tls"},
    )
    class VirtualGatewayClientPolicyProperty:
        def __init__(
            self,
            *,
            tls: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty"]] = None,
        ) -> None:
            '''
            :param tls: ``CfnVirtualGateway.VirtualGatewayClientPolicyProperty.TLS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if tls is not None:
                self._values["tls"] = tls

        @builtins.property
        def tls(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayClientPolicyProperty.TLS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicy-tls
            '''
            result = self._values.get("tls")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayClientPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "validation": "validation",
            "certificate": "certificate",
            "enforce": "enforce",
            "ports": "ports",
        },
    )
    class VirtualGatewayClientPolicyTlsProperty:
        def __init__(
            self,
            *,
            validation: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextProperty"],
            certificate: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayClientTlsCertificateProperty"]] = None,
            enforce: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            ports: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[jsii.Number]]] = None,
        ) -> None:
            '''
            :param validation: ``CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty.Validation``.
            :param certificate: ``CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty.Certificate``.
            :param enforce: ``CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty.Enforce``.
            :param ports: ``CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty.Ports``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "validation": validation,
            }
            if certificate is not None:
                self._values["certificate"] = certificate
            if enforce is not None:
                self._values["enforce"] = enforce
            if ports is not None:
                self._values["ports"] = ports

        @builtins.property
        def validation(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextProperty"]:
            '''``CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty.Validation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-validation
            '''
            result = self._values.get("validation")
            assert result is not None, "Required property 'validation' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextProperty"], result)

        @builtins.property
        def certificate(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayClientTlsCertificateProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty.Certificate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-certificate
            '''
            result = self._values.get("certificate")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayClientTlsCertificateProperty"]], result)

        @builtins.property
        def enforce(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty.Enforce``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-enforce
            '''
            result = self._values.get("enforce")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def ports(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]]:
            '''``CfnVirtualGateway.VirtualGatewayClientPolicyTlsProperty.Ports``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-ports
            '''
            result = self._values.get("ports")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayClientPolicyTlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayClientTlsCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={"file": "file", "sds": "sds"},
    )
    class VirtualGatewayClientTlsCertificateProperty:
        def __init__(
            self,
            *,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty"]] = None,
            sds: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsSdsCertificateProperty"]] = None,
        ) -> None:
            '''
            :param file: ``CfnVirtualGateway.VirtualGatewayClientTlsCertificateProperty.File``.
            :param sds: ``CfnVirtualGateway.VirtualGatewayClientTlsCertificateProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if file is not None:
                self._values["file"] = file
            if sds is not None:
                self._values["sds"] = sds

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayClientTlsCertificateProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty"]], result)

        @builtins.property
        def sds(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsSdsCertificateProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayClientTlsCertificateProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-sds
            '''
            result = self._values.get("sds")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsSdsCertificateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayClientTlsCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayConnectionPoolProperty",
        jsii_struct_bases=[],
        name_mapping={"grpc": "grpc", "http": "http", "http2": "http2"},
    )
    class VirtualGatewayConnectionPoolProperty:
        def __init__(
            self,
            *,
            grpc: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayGrpcConnectionPoolProperty"]] = None,
            http: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayHttpConnectionPoolProperty"]] = None,
            http2: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayHttp2ConnectionPoolProperty"]] = None,
        ) -> None:
            '''
            :param grpc: ``CfnVirtualGateway.VirtualGatewayConnectionPoolProperty.GRPC``.
            :param http: ``CfnVirtualGateway.VirtualGatewayConnectionPoolProperty.HTTP``.
            :param http2: ``CfnVirtualGateway.VirtualGatewayConnectionPoolProperty.HTTP2``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if grpc is not None:
                self._values["grpc"] = grpc
            if http is not None:
                self._values["http"] = http
            if http2 is not None:
                self._values["http2"] = http2

        @builtins.property
        def grpc(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayGrpcConnectionPoolProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayConnectionPoolProperty.GRPC``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-grpc
            '''
            result = self._values.get("grpc")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayGrpcConnectionPoolProperty"]], result)

        @builtins.property
        def http(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayHttpConnectionPoolProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayConnectionPoolProperty.HTTP``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http
            '''
            result = self._values.get("http")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayHttpConnectionPoolProperty"]], result)

        @builtins.property
        def http2(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayHttp2ConnectionPoolProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayConnectionPoolProperty.HTTP2``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http2
            '''
            result = self._values.get("http2")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayHttp2ConnectionPoolProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayConnectionPoolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayFileAccessLogProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path"},
    )
    class VirtualGatewayFileAccessLogProperty:
        def __init__(self, *, path: builtins.str) -> None:
            '''
            :param path: ``CfnVirtualGateway.VirtualGatewayFileAccessLogProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "path": path,
            }

        @builtins.property
        def path(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayFileAccessLogProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayfileaccesslog-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayFileAccessLogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayGrpcConnectionPoolProperty",
        jsii_struct_bases=[],
        name_mapping={"max_requests": "maxRequests"},
    )
    class VirtualGatewayGrpcConnectionPoolProperty:
        def __init__(self, *, max_requests: jsii.Number) -> None:
            '''
            :param max_requests: ``CfnVirtualGateway.VirtualGatewayGrpcConnectionPoolProperty.MaxRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_requests": max_requests,
            }

        @builtins.property
        def max_requests(self) -> jsii.Number:
            '''``CfnVirtualGateway.VirtualGatewayGrpcConnectionPoolProperty.MaxRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool-maxrequests
            '''
            result = self._values.get("max_requests")
            assert result is not None, "Required property 'max_requests' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayGrpcConnectionPoolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "healthy_threshold": "healthyThreshold",
            "interval_millis": "intervalMillis",
            "protocol": "protocol",
            "timeout_millis": "timeoutMillis",
            "unhealthy_threshold": "unhealthyThreshold",
            "path": "path",
            "port": "port",
        },
    )
    class VirtualGatewayHealthCheckPolicyProperty:
        def __init__(
            self,
            *,
            healthy_threshold: jsii.Number,
            interval_millis: jsii.Number,
            protocol: builtins.str,
            timeout_millis: jsii.Number,
            unhealthy_threshold: jsii.Number,
            path: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param healthy_threshold: ``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.HealthyThreshold``.
            :param interval_millis: ``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.IntervalMillis``.
            :param protocol: ``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.Protocol``.
            :param timeout_millis: ``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.TimeoutMillis``.
            :param unhealthy_threshold: ``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.UnhealthyThreshold``.
            :param path: ``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.Path``.
            :param port: ``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "healthy_threshold": healthy_threshold,
                "interval_millis": interval_millis,
                "protocol": protocol,
                "timeout_millis": timeout_millis,
                "unhealthy_threshold": unhealthy_threshold,
            }
            if path is not None:
                self._values["path"] = path
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def healthy_threshold(self) -> jsii.Number:
            '''``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.HealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-healthythreshold
            '''
            result = self._values.get("healthy_threshold")
            assert result is not None, "Required property 'healthy_threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def interval_millis(self) -> jsii.Number:
            '''``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.IntervalMillis``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-intervalmillis
            '''
            result = self._values.get("interval_millis")
            assert result is not None, "Required property 'interval_millis' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timeout_millis(self) -> jsii.Number:
            '''``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.TimeoutMillis``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-timeoutmillis
            '''
            result = self._values.get("timeout_millis")
            assert result is not None, "Required property 'timeout_millis' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def unhealthy_threshold(self) -> jsii.Number:
            '''``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.UnhealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-unhealthythreshold
            '''
            result = self._values.get("unhealthy_threshold")
            assert result is not None, "Required property 'unhealthy_threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''``CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayHealthCheckPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayHttp2ConnectionPoolProperty",
        jsii_struct_bases=[],
        name_mapping={"max_requests": "maxRequests"},
    )
    class VirtualGatewayHttp2ConnectionPoolProperty:
        def __init__(self, *, max_requests: jsii.Number) -> None:
            '''
            :param max_requests: ``CfnVirtualGateway.VirtualGatewayHttp2ConnectionPoolProperty.MaxRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttp2connectionpool.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_requests": max_requests,
            }

        @builtins.property
        def max_requests(self) -> jsii.Number:
            '''``CfnVirtualGateway.VirtualGatewayHttp2ConnectionPoolProperty.MaxRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttp2connectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttp2connectionpool-maxrequests
            '''
            result = self._values.get("max_requests")
            assert result is not None, "Required property 'max_requests' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayHttp2ConnectionPoolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayHttpConnectionPoolProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_connections": "maxConnections",
            "max_pending_requests": "maxPendingRequests",
        },
    )
    class VirtualGatewayHttpConnectionPoolProperty:
        def __init__(
            self,
            *,
            max_connections: jsii.Number,
            max_pending_requests: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param max_connections: ``CfnVirtualGateway.VirtualGatewayHttpConnectionPoolProperty.MaxConnections``.
            :param max_pending_requests: ``CfnVirtualGateway.VirtualGatewayHttpConnectionPoolProperty.MaxPendingRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_connections": max_connections,
            }
            if max_pending_requests is not None:
                self._values["max_pending_requests"] = max_pending_requests

        @builtins.property
        def max_connections(self) -> jsii.Number:
            '''``CfnVirtualGateway.VirtualGatewayHttpConnectionPoolProperty.MaxConnections``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxconnections
            '''
            result = self._values.get("max_connections")
            assert result is not None, "Required property 'max_connections' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_pending_requests(self) -> typing.Optional[jsii.Number]:
            '''``CfnVirtualGateway.VirtualGatewayHttpConnectionPoolProperty.MaxPendingRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxpendingrequests
            '''
            result = self._values.get("max_pending_requests")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayHttpConnectionPoolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayListenerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "port_mapping": "portMapping",
            "connection_pool": "connectionPool",
            "health_check": "healthCheck",
            "tls": "tls",
        },
    )
    class VirtualGatewayListenerProperty:
        def __init__(
            self,
            *,
            port_mapping: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayPortMappingProperty"],
            connection_pool: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayConnectionPoolProperty"]] = None,
            health_check: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty"]] = None,
            tls: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsProperty"]] = None,
        ) -> None:
            '''
            :param port_mapping: ``CfnVirtualGateway.VirtualGatewayListenerProperty.PortMapping``.
            :param connection_pool: ``CfnVirtualGateway.VirtualGatewayListenerProperty.ConnectionPool``.
            :param health_check: ``CfnVirtualGateway.VirtualGatewayListenerProperty.HealthCheck``.
            :param tls: ``CfnVirtualGateway.VirtualGatewayListenerProperty.TLS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "port_mapping": port_mapping,
            }
            if connection_pool is not None:
                self._values["connection_pool"] = connection_pool
            if health_check is not None:
                self._values["health_check"] = health_check
            if tls is not None:
                self._values["tls"] = tls

        @builtins.property
        def port_mapping(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayPortMappingProperty"]:
            '''``CfnVirtualGateway.VirtualGatewayListenerProperty.PortMapping``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-portmapping
            '''
            result = self._values.get("port_mapping")
            assert result is not None, "Required property 'port_mapping' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayPortMappingProperty"], result)

        @builtins.property
        def connection_pool(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayConnectionPoolProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerProperty.ConnectionPool``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-connectionpool
            '''
            result = self._values.get("connection_pool")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayConnectionPoolProperty"]], result)

        @builtins.property
        def health_check(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerProperty.HealthCheck``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-healthcheck
            '''
            result = self._values.get("health_check")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty"]], result)

        @builtins.property
        def tls(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerProperty.TLS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-tls
            '''
            result = self._values.get("tls")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayListenerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayListenerTlsAcmCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_arn": "certificateArn"},
    )
    class VirtualGatewayListenerTlsAcmCertificateProperty:
        def __init__(self, *, certificate_arn: builtins.str) -> None:
            '''
            :param certificate_arn: ``CfnVirtualGateway.VirtualGatewayListenerTlsAcmCertificateProperty.CertificateArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate_arn": certificate_arn,
            }

        @builtins.property
        def certificate_arn(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsAcmCertificateProperty.CertificateArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate-certificatearn
            '''
            result = self._values.get("certificate_arn")
            assert result is not None, "Required property 'certificate_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayListenerTlsAcmCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
    )
    class VirtualGatewayListenerTlsCertificateProperty:
        def __init__(
            self,
            *,
            acm: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsAcmCertificateProperty"]] = None,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty"]] = None,
            sds: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsSdsCertificateProperty"]] = None,
        ) -> None:
            '''
            :param acm: ``CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty.ACM``.
            :param file: ``CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty.File``.
            :param sds: ``CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if acm is not None:
                self._values["acm"] = acm
            if file is not None:
                self._values["file"] = file
            if sds is not None:
                self._values["sds"] = sds

        @builtins.property
        def acm(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsAcmCertificateProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty.ACM``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-acm
            '''
            result = self._values.get("acm")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsAcmCertificateProperty"]], result)

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty"]], result)

        @builtins.property
        def sds(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsSdsCertificateProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-sds
            '''
            result = self._values.get("sds")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsSdsCertificateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayListenerTlsCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_chain": "certificateChain",
            "private_key": "privateKey",
        },
    )
    class VirtualGatewayListenerTlsFileCertificateProperty:
        def __init__(
            self,
            *,
            certificate_chain: builtins.str,
            private_key: builtins.str,
        ) -> None:
            '''
            :param certificate_chain: ``CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty.CertificateChain``.
            :param private_key: ``CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty.PrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate_chain": certificate_chain,
                "private_key": private_key,
            }

        @builtins.property
        def certificate_chain(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty.CertificateChain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-certificatechain
            '''
            result = self._values.get("certificate_chain")
            assert result is not None, "Required property 'certificate_chain' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def private_key(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsFileCertificateProperty.PrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-privatekey
            '''
            result = self._values.get("private_key")
            assert result is not None, "Required property 'private_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayListenerTlsFileCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayListenerTlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate": "certificate",
            "mode": "mode",
            "validation": "validation",
        },
    )
    class VirtualGatewayListenerTlsProperty:
        def __init__(
            self,
            *,
            certificate: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty"],
            mode: builtins.str,
            validation: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextProperty"]] = None,
        ) -> None:
            '''
            :param certificate: ``CfnVirtualGateway.VirtualGatewayListenerTlsProperty.Certificate``.
            :param mode: ``CfnVirtualGateway.VirtualGatewayListenerTlsProperty.Mode``.
            :param validation: ``CfnVirtualGateway.VirtualGatewayListenerTlsProperty.Validation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate": certificate,
                "mode": mode,
            }
            if validation is not None:
                self._values["validation"] = validation

        @builtins.property
        def certificate(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty"]:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsProperty.Certificate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-certificate
            '''
            result = self._values.get("certificate")
            assert result is not None, "Required property 'certificate' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsCertificateProperty"], result)

        @builtins.property
        def mode(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def validation(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsProperty.Validation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-validation
            '''
            result = self._values.get("validation")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayListenerTlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayListenerTlsSdsCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_name": "secretName"},
    )
    class VirtualGatewayListenerTlsSdsCertificateProperty:
        def __init__(self, *, secret_name: builtins.str) -> None:
            '''
            :param secret_name: ``CfnVirtualGateway.VirtualGatewayListenerTlsSdsCertificateProperty.SecretName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "secret_name": secret_name,
            }

        @builtins.property
        def secret_name(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsSdsCertificateProperty.SecretName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate-secretname
            '''
            result = self._values.get("secret_name")
            assert result is not None, "Required property 'secret_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayListenerTlsSdsCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trust": "trust",
            "subject_alternative_names": "subjectAlternativeNames",
        },
    )
    class VirtualGatewayListenerTlsValidationContextProperty:
        def __init__(
            self,
            *,
            trust: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextTrustProperty"],
            subject_alternative_names: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.SubjectAlternativeNamesProperty"]] = None,
        ) -> None:
            '''
            :param trust: ``CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextProperty.Trust``.
            :param subject_alternative_names: ``CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "trust": trust,
            }
            if subject_alternative_names is not None:
                self._values["subject_alternative_names"] = subject_alternative_names

        @builtins.property
        def trust(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextTrustProperty"]:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextProperty.Trust``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-trust
            '''
            result = self._values.get("trust")
            assert result is not None, "Required property 'trust' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextTrustProperty"], result)

        @builtins.property
        def subject_alternative_names(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.SubjectAlternativeNamesProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-subjectalternativenames
            '''
            result = self._values.get("subject_alternative_names")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.SubjectAlternativeNamesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayListenerTlsValidationContextProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"file": "file", "sds": "sds"},
    )
    class VirtualGatewayListenerTlsValidationContextTrustProperty:
        def __init__(
            self,
            *,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextFileTrustProperty"]] = None,
            sds: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextSdsTrustProperty"]] = None,
        ) -> None:
            '''
            :param file: ``CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextTrustProperty.File``.
            :param sds: ``CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextTrustProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if file is not None:
                self._values["file"] = file
            if sds is not None:
                self._values["sds"] = sds

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextFileTrustProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextTrustProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextFileTrustProperty"]], result)

        @builtins.property
        def sds(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextSdsTrustProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayListenerTlsValidationContextTrustProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-sds
            '''
            result = self._values.get("sds")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextSdsTrustProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayListenerTlsValidationContextTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayLoggingProperty",
        jsii_struct_bases=[],
        name_mapping={"access_log": "accessLog"},
    )
    class VirtualGatewayLoggingProperty:
        def __init__(
            self,
            *,
            access_log: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayAccessLogProperty"]] = None,
        ) -> None:
            '''
            :param access_log: ``CfnVirtualGateway.VirtualGatewayLoggingProperty.AccessLog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if access_log is not None:
                self._values["access_log"] = access_log

        @builtins.property
        def access_log(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayAccessLogProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayLoggingProperty.AccessLog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html#cfn-appmesh-virtualgateway-virtualgatewaylogging-accesslog
            '''
            result = self._values.get("access_log")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayAccessLogProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayLoggingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayPortMappingProperty",
        jsii_struct_bases=[],
        name_mapping={"port": "port", "protocol": "protocol"},
    )
    class VirtualGatewayPortMappingProperty:
        def __init__(self, *, port: jsii.Number, protocol: builtins.str) -> None:
            '''
            :param port: ``CfnVirtualGateway.VirtualGatewayPortMappingProperty.Port``.
            :param protocol: ``CfnVirtualGateway.VirtualGatewayPortMappingProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "port": port,
                "protocol": protocol,
            }

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnVirtualGateway.VirtualGatewayPortMappingProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html#cfn-appmesh-virtualgateway-virtualgatewayportmapping-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayPortMappingProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html#cfn-appmesh-virtualgateway-virtualgatewayportmapping-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayPortMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewaySpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "listeners": "listeners",
            "backend_defaults": "backendDefaults",
            "logging": "logging",
        },
    )
    class VirtualGatewaySpecProperty:
        def __init__(
            self,
            *,
            listeners: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnVirtualGateway.VirtualGatewayListenerProperty", aws_cdk.core.IResolvable]]],
            backend_defaults: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayBackendDefaultsProperty"]] = None,
            logging: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayLoggingProperty"]] = None,
        ) -> None:
            '''
            :param listeners: ``CfnVirtualGateway.VirtualGatewaySpecProperty.Listeners``.
            :param backend_defaults: ``CfnVirtualGateway.VirtualGatewaySpecProperty.BackendDefaults``.
            :param logging: ``CfnVirtualGateway.VirtualGatewaySpecProperty.Logging``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "listeners": listeners,
            }
            if backend_defaults is not None:
                self._values["backend_defaults"] = backend_defaults
            if logging is not None:
                self._values["logging"] = logging

        @builtins.property
        def listeners(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnVirtualGateway.VirtualGatewayListenerProperty", aws_cdk.core.IResolvable]]]:
            '''``CfnVirtualGateway.VirtualGatewaySpecProperty.Listeners``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-listeners
            '''
            result = self._values.get("listeners")
            assert result is not None, "Required property 'listeners' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnVirtualGateway.VirtualGatewayListenerProperty", aws_cdk.core.IResolvable]]], result)

        @builtins.property
        def backend_defaults(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayBackendDefaultsProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewaySpecProperty.BackendDefaults``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-backenddefaults
            '''
            result = self._values.get("backend_defaults")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayBackendDefaultsProperty"]], result)

        @builtins.property
        def logging(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayLoggingProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewaySpecProperty.Logging``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-logging
            '''
            result = self._values.get("logging")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayLoggingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewaySpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayTlsValidationContextAcmTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_authority_arns": "certificateAuthorityArns"},
    )
    class VirtualGatewayTlsValidationContextAcmTrustProperty:
        def __init__(
            self,
            *,
            certificate_authority_arns: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param certificate_authority_arns: ``CfnVirtualGateway.VirtualGatewayTlsValidationContextAcmTrustProperty.CertificateAuthorityArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate_authority_arns": certificate_authority_arns,
            }

        @builtins.property
        def certificate_authority_arns(self) -> typing.List[builtins.str]:
            '''``CfnVirtualGateway.VirtualGatewayTlsValidationContextAcmTrustProperty.CertificateAuthorityArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-certificateauthorityarns
            '''
            result = self._values.get("certificate_authority_arns")
            assert result is not None, "Required property 'certificate_authority_arns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayTlsValidationContextAcmTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayTlsValidationContextFileTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_chain": "certificateChain"},
    )
    class VirtualGatewayTlsValidationContextFileTrustProperty:
        def __init__(self, *, certificate_chain: builtins.str) -> None:
            '''
            :param certificate_chain: ``CfnVirtualGateway.VirtualGatewayTlsValidationContextFileTrustProperty.CertificateChain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate_chain": certificate_chain,
            }

        @builtins.property
        def certificate_chain(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayTlsValidationContextFileTrustProperty.CertificateChain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust-certificatechain
            '''
            result = self._values.get("certificate_chain")
            assert result is not None, "Required property 'certificate_chain' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayTlsValidationContextFileTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayTlsValidationContextProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trust": "trust",
            "subject_alternative_names": "subjectAlternativeNames",
        },
    )
    class VirtualGatewayTlsValidationContextProperty:
        def __init__(
            self,
            *,
            trust: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty"],
            subject_alternative_names: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.SubjectAlternativeNamesProperty"]] = None,
        ) -> None:
            '''
            :param trust: ``CfnVirtualGateway.VirtualGatewayTlsValidationContextProperty.Trust``.
            :param subject_alternative_names: ``CfnVirtualGateway.VirtualGatewayTlsValidationContextProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "trust": trust,
            }
            if subject_alternative_names is not None:
                self._values["subject_alternative_names"] = subject_alternative_names

        @builtins.property
        def trust(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty"]:
            '''``CfnVirtualGateway.VirtualGatewayTlsValidationContextProperty.Trust``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-trust
            '''
            result = self._values.get("trust")
            assert result is not None, "Required property 'trust' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty"], result)

        @builtins.property
        def subject_alternative_names(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.SubjectAlternativeNamesProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayTlsValidationContextProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-subjectalternativenames
            '''
            result = self._values.get("subject_alternative_names")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.SubjectAlternativeNamesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayTlsValidationContextProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayTlsValidationContextSdsTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_name": "secretName"},
    )
    class VirtualGatewayTlsValidationContextSdsTrustProperty:
        def __init__(self, *, secret_name: builtins.str) -> None:
            '''
            :param secret_name: ``CfnVirtualGateway.VirtualGatewayTlsValidationContextSdsTrustProperty.SecretName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "secret_name": secret_name,
            }

        @builtins.property
        def secret_name(self) -> builtins.str:
            '''``CfnVirtualGateway.VirtualGatewayTlsValidationContextSdsTrustProperty.SecretName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-secretname
            '''
            result = self._values.get("secret_name")
            assert result is not None, "Required property 'secret_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayTlsValidationContextSdsTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
    )
    class VirtualGatewayTlsValidationContextTrustProperty:
        def __init__(
            self,
            *,
            acm: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextAcmTrustProperty"]] = None,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextFileTrustProperty"]] = None,
            sds: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextSdsTrustProperty"]] = None,
        ) -> None:
            '''
            :param acm: ``CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty.ACM``.
            :param file: ``CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty.File``.
            :param sds: ``CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if acm is not None:
                self._values["acm"] = acm
            if file is not None:
                self._values["file"] = file
            if sds is not None:
                self._values["sds"] = sds

        @builtins.property
        def acm(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextAcmTrustProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty.ACM``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-acm
            '''
            result = self._values.get("acm")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextAcmTrustProperty"]], result)

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextFileTrustProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextFileTrustProperty"]], result)

        @builtins.property
        def sds(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextSdsTrustProperty"]]:
            '''``CfnVirtualGateway.VirtualGatewayTlsValidationContextTrustProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-sds
            '''
            result = self._values.get("sds")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualGateway.VirtualGatewayTlsValidationContextSdsTrustProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualGatewayTlsValidationContextTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.CfnVirtualGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "mesh_name": "meshName",
        "spec": "spec",
        "mesh_owner": "meshOwner",
        "tags": "tags",
        "virtual_gateway_name": "virtualGatewayName",
    },
)
class CfnVirtualGatewayProps:
    def __init__(
        self,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, CfnVirtualGateway.VirtualGatewaySpecProperty],
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        virtual_gateway_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppMesh::VirtualGateway``.

        :param mesh_name: ``AWS::AppMesh::VirtualGateway.MeshName``.
        :param spec: ``AWS::AppMesh::VirtualGateway.Spec``.
        :param mesh_owner: ``AWS::AppMesh::VirtualGateway.MeshOwner``.
        :param tags: ``AWS::AppMesh::VirtualGateway.Tags``.
        :param virtual_gateway_name: ``AWS::AppMesh::VirtualGateway.VirtualGatewayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if mesh_owner is not None:
            self._values["mesh_owner"] = mesh_owner
        if tags is not None:
            self._values["tags"] = tags
        if virtual_gateway_name is not None:
            self._values["virtual_gateway_name"] = virtual_gateway_name

    @builtins.property
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualGateway.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshname
        '''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnVirtualGateway.VirtualGatewaySpecProperty]:
        '''``AWS::AppMesh::VirtualGateway.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnVirtualGateway.VirtualGatewaySpecProperty], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualGateway.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshowner
        '''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppMesh::VirtualGateway.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def virtual_gateway_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualGateway.VirtualGatewayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-virtualgatewayname
        '''
        result = self._values.get("virtual_gateway_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnVirtualNode(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode",
):
    '''A CloudFormation ``AWS::AppMesh::VirtualNode``.

    :cloudformationResource: AWS::AppMesh::VirtualNode
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeSpecProperty"],
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        virtual_node_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::AppMesh::VirtualNode``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param mesh_name: ``AWS::AppMesh::VirtualNode.MeshName``.
        :param spec: ``AWS::AppMesh::VirtualNode.Spec``.
        :param mesh_owner: ``AWS::AppMesh::VirtualNode.MeshOwner``.
        :param tags: ``AWS::AppMesh::VirtualNode.Tags``.
        :param virtual_node_name: ``AWS::AppMesh::VirtualNode.VirtualNodeName``.
        '''
        props = CfnVirtualNodeProps(
            mesh_name=mesh_name,
            spec=spec,
            mesh_owner=mesh_owner,
            tags=tags,
            virtual_node_name=virtual_node_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshName")
    def attr_mesh_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshOwner")
    def attr_mesh_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceOwner")
    def attr_resource_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUid")
    def attr_uid(self) -> builtins.str:
        '''
        :cloudformationAttribute: Uid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVirtualNodeName")
    def attr_virtual_node_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: VirtualNodeName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualNodeName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppMesh::VirtualNode.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualNode.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshname
        '''
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        jsii.set(self, "meshName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="spec")
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeSpecProperty"]:
        '''``AWS::AppMesh::VirtualNode.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-spec
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeSpecProperty"], jsii.get(self, "spec"))

    @spec.setter
    def spec(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeSpecProperty"],
    ) -> None:
        jsii.set(self, "spec", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualNode.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshowner
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "meshOwner", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualNodeName")
    def virtual_node_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualNode.VirtualNodeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-virtualnodename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNodeName"))

    @virtual_node_name.setter
    def virtual_node_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "virtualNodeName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.AccessLogProperty",
        jsii_struct_bases=[],
        name_mapping={"file": "file"},
    )
    class AccessLogProperty:
        def __init__(
            self,
            *,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.FileAccessLogProperty"]] = None,
        ) -> None:
            '''
            :param file: ``CfnVirtualNode.AccessLogProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if file is not None:
                self._values["file"] = file

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.FileAccessLogProperty"]]:
            '''``CfnVirtualNode.AccessLogProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html#cfn-appmesh-virtualnode-accesslog-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.FileAccessLogProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessLogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.AwsCloudMapInstanceAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class AwsCloudMapInstanceAttributeProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: ``CfnVirtualNode.AwsCloudMapInstanceAttributeProperty.Key``.
            :param value: ``CfnVirtualNode.AwsCloudMapInstanceAttributeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnVirtualNode.AwsCloudMapInstanceAttributeProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnVirtualNode.AwsCloudMapInstanceAttributeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsCloudMapInstanceAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "namespace_name": "namespaceName",
            "service_name": "serviceName",
            "attributes": "attributes",
        },
    )
    class AwsCloudMapServiceDiscoveryProperty:
        def __init__(
            self,
            *,
            namespace_name: builtins.str,
            service_name: builtins.str,
            attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.AwsCloudMapInstanceAttributeProperty"]]]] = None,
        ) -> None:
            '''
            :param namespace_name: ``CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty.NamespaceName``.
            :param service_name: ``CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty.ServiceName``.
            :param attributes: ``CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "namespace_name": namespace_name,
                "service_name": service_name,
            }
            if attributes is not None:
                self._values["attributes"] = attributes

        @builtins.property
        def namespace_name(self) -> builtins.str:
            '''``CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty.NamespaceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-namespacename
            '''
            result = self._values.get("namespace_name")
            assert result is not None, "Required property 'namespace_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_name(self) -> builtins.str:
            '''``CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty.ServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-servicename
            '''
            result = self._values.get("service_name")
            assert result is not None, "Required property 'service_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.AwsCloudMapInstanceAttributeProperty"]]]]:
            '''``CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.AwsCloudMapInstanceAttributeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsCloudMapServiceDiscoveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.BackendDefaultsProperty",
        jsii_struct_bases=[],
        name_mapping={"client_policy": "clientPolicy"},
    )
    class BackendDefaultsProperty:
        def __init__(
            self,
            *,
            client_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientPolicyProperty"]] = None,
        ) -> None:
            '''
            :param client_policy: ``CfnVirtualNode.BackendDefaultsProperty.ClientPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if client_policy is not None:
                self._values["client_policy"] = client_policy

        @builtins.property
        def client_policy(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientPolicyProperty"]]:
            '''``CfnVirtualNode.BackendDefaultsProperty.ClientPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html#cfn-appmesh-virtualnode-backenddefaults-clientpolicy
            '''
            result = self._values.get("client_policy")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientPolicyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackendDefaultsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.BackendProperty",
        jsii_struct_bases=[],
        name_mapping={"virtual_service": "virtualService"},
    )
    class BackendProperty:
        def __init__(
            self,
            *,
            virtual_service: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualServiceBackendProperty"]] = None,
        ) -> None:
            '''
            :param virtual_service: ``CfnVirtualNode.BackendProperty.VirtualService``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if virtual_service is not None:
                self._values["virtual_service"] = virtual_service

        @builtins.property
        def virtual_service(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualServiceBackendProperty"]]:
            '''``CfnVirtualNode.BackendProperty.VirtualService``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html#cfn-appmesh-virtualnode-backend-virtualservice
            '''
            result = self._values.get("virtual_service")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualServiceBackendProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackendProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ClientPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"tls": "tls"},
    )
    class ClientPolicyProperty:
        def __init__(
            self,
            *,
            tls: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientPolicyTlsProperty"]] = None,
        ) -> None:
            '''
            :param tls: ``CfnVirtualNode.ClientPolicyProperty.TLS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if tls is not None:
                self._values["tls"] = tls

        @builtins.property
        def tls(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientPolicyTlsProperty"]]:
            '''``CfnVirtualNode.ClientPolicyProperty.TLS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html#cfn-appmesh-virtualnode-clientpolicy-tls
            '''
            result = self._values.get("tls")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientPolicyTlsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ClientPolicyTlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "validation": "validation",
            "certificate": "certificate",
            "enforce": "enforce",
            "ports": "ports",
        },
    )
    class ClientPolicyTlsProperty:
        def __init__(
            self,
            *,
            validation: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextProperty"],
            certificate: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientTlsCertificateProperty"]] = None,
            enforce: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            ports: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[jsii.Number]]] = None,
        ) -> None:
            '''
            :param validation: ``CfnVirtualNode.ClientPolicyTlsProperty.Validation``.
            :param certificate: ``CfnVirtualNode.ClientPolicyTlsProperty.Certificate``.
            :param enforce: ``CfnVirtualNode.ClientPolicyTlsProperty.Enforce``.
            :param ports: ``CfnVirtualNode.ClientPolicyTlsProperty.Ports``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "validation": validation,
            }
            if certificate is not None:
                self._values["certificate"] = certificate
            if enforce is not None:
                self._values["enforce"] = enforce
            if ports is not None:
                self._values["ports"] = ports

        @builtins.property
        def validation(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextProperty"]:
            '''``CfnVirtualNode.ClientPolicyTlsProperty.Validation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-validation
            '''
            result = self._values.get("validation")
            assert result is not None, "Required property 'validation' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextProperty"], result)

        @builtins.property
        def certificate(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientTlsCertificateProperty"]]:
            '''``CfnVirtualNode.ClientPolicyTlsProperty.Certificate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-certificate
            '''
            result = self._values.get("certificate")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientTlsCertificateProperty"]], result)

        @builtins.property
        def enforce(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnVirtualNode.ClientPolicyTlsProperty.Enforce``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-enforce
            '''
            result = self._values.get("enforce")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def ports(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]]:
            '''``CfnVirtualNode.ClientPolicyTlsProperty.Ports``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-ports
            '''
            result = self._values.get("ports")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientPolicyTlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ClientTlsCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={"file": "file", "sds": "sds"},
    )
    class ClientTlsCertificateProperty:
        def __init__(
            self,
            *,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsFileCertificateProperty"]] = None,
            sds: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsSdsCertificateProperty"]] = None,
        ) -> None:
            '''
            :param file: ``CfnVirtualNode.ClientTlsCertificateProperty.File``.
            :param sds: ``CfnVirtualNode.ClientTlsCertificateProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if file is not None:
                self._values["file"] = file
            if sds is not None:
                self._values["sds"] = sds

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsFileCertificateProperty"]]:
            '''``CfnVirtualNode.ClientTlsCertificateProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsFileCertificateProperty"]], result)

        @builtins.property
        def sds(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsSdsCertificateProperty"]]:
            '''``CfnVirtualNode.ClientTlsCertificateProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-sds
            '''
            result = self._values.get("sds")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsSdsCertificateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientTlsCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.DnsServiceDiscoveryProperty",
        jsii_struct_bases=[],
        name_mapping={"hostname": "hostname", "response_type": "responseType"},
    )
    class DnsServiceDiscoveryProperty:
        def __init__(
            self,
            *,
            hostname: builtins.str,
            response_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param hostname: ``CfnVirtualNode.DnsServiceDiscoveryProperty.Hostname``.
            :param response_type: ``CfnVirtualNode.DnsServiceDiscoveryProperty.ResponseType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "hostname": hostname,
            }
            if response_type is not None:
                self._values["response_type"] = response_type

        @builtins.property
        def hostname(self) -> builtins.str:
            '''``CfnVirtualNode.DnsServiceDiscoveryProperty.Hostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html#cfn-appmesh-virtualnode-dnsservicediscovery-hostname
            '''
            result = self._values.get("hostname")
            assert result is not None, "Required property 'hostname' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def response_type(self) -> typing.Optional[builtins.str]:
            '''``CfnVirtualNode.DnsServiceDiscoveryProperty.ResponseType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html#cfn-appmesh-virtualnode-dnsservicediscovery-responsetype
            '''
            result = self._values.get("response_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DnsServiceDiscoveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.DurationProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class DurationProperty:
        def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
            '''
            :param unit: ``CfnVirtualNode.DurationProperty.Unit``.
            :param value: ``CfnVirtualNode.DurationProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''``CfnVirtualNode.DurationProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html#cfn-appmesh-virtualnode-duration-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''``CfnVirtualNode.DurationProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html#cfn-appmesh-virtualnode-duration-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.FileAccessLogProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path"},
    )
    class FileAccessLogProperty:
        def __init__(self, *, path: builtins.str) -> None:
            '''
            :param path: ``CfnVirtualNode.FileAccessLogProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "path": path,
            }

        @builtins.property
        def path(self) -> builtins.str:
            '''``CfnVirtualNode.FileAccessLogProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html#cfn-appmesh-virtualnode-fileaccesslog-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileAccessLogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.GrpcTimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"idle": "idle", "per_request": "perRequest"},
    )
    class GrpcTimeoutProperty:
        def __init__(
            self,
            *,
            idle: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]] = None,
            per_request: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]] = None,
        ) -> None:
            '''
            :param idle: ``CfnVirtualNode.GrpcTimeoutProperty.Idle``.
            :param per_request: ``CfnVirtualNode.GrpcTimeoutProperty.PerRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if idle is not None:
                self._values["idle"] = idle
            if per_request is not None:
                self._values["per_request"] = per_request

        @builtins.property
        def idle(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]]:
            '''``CfnVirtualNode.GrpcTimeoutProperty.Idle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-idle
            '''
            result = self._values.get("idle")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]], result)

        @builtins.property
        def per_request(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]]:
            '''``CfnVirtualNode.GrpcTimeoutProperty.PerRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-perrequest
            '''
            result = self._values.get("per_request")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrpcTimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.HealthCheckProperty",
        jsii_struct_bases=[],
        name_mapping={
            "healthy_threshold": "healthyThreshold",
            "interval_millis": "intervalMillis",
            "protocol": "protocol",
            "timeout_millis": "timeoutMillis",
            "unhealthy_threshold": "unhealthyThreshold",
            "path": "path",
            "port": "port",
        },
    )
    class HealthCheckProperty:
        def __init__(
            self,
            *,
            healthy_threshold: jsii.Number,
            interval_millis: jsii.Number,
            protocol: builtins.str,
            timeout_millis: jsii.Number,
            unhealthy_threshold: jsii.Number,
            path: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param healthy_threshold: ``CfnVirtualNode.HealthCheckProperty.HealthyThreshold``.
            :param interval_millis: ``CfnVirtualNode.HealthCheckProperty.IntervalMillis``.
            :param protocol: ``CfnVirtualNode.HealthCheckProperty.Protocol``.
            :param timeout_millis: ``CfnVirtualNode.HealthCheckProperty.TimeoutMillis``.
            :param unhealthy_threshold: ``CfnVirtualNode.HealthCheckProperty.UnhealthyThreshold``.
            :param path: ``CfnVirtualNode.HealthCheckProperty.Path``.
            :param port: ``CfnVirtualNode.HealthCheckProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "healthy_threshold": healthy_threshold,
                "interval_millis": interval_millis,
                "protocol": protocol,
                "timeout_millis": timeout_millis,
                "unhealthy_threshold": unhealthy_threshold,
            }
            if path is not None:
                self._values["path"] = path
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def healthy_threshold(self) -> jsii.Number:
            '''``CfnVirtualNode.HealthCheckProperty.HealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-healthythreshold
            '''
            result = self._values.get("healthy_threshold")
            assert result is not None, "Required property 'healthy_threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def interval_millis(self) -> jsii.Number:
            '''``CfnVirtualNode.HealthCheckProperty.IntervalMillis``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-intervalmillis
            '''
            result = self._values.get("interval_millis")
            assert result is not None, "Required property 'interval_millis' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''``CfnVirtualNode.HealthCheckProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timeout_millis(self) -> jsii.Number:
            '''``CfnVirtualNode.HealthCheckProperty.TimeoutMillis``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-timeoutmillis
            '''
            result = self._values.get("timeout_millis")
            assert result is not None, "Required property 'timeout_millis' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def unhealthy_threshold(self) -> jsii.Number:
            '''``CfnVirtualNode.HealthCheckProperty.UnhealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-unhealthythreshold
            '''
            result = self._values.get("unhealthy_threshold")
            assert result is not None, "Required property 'unhealthy_threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''``CfnVirtualNode.HealthCheckProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''``CfnVirtualNode.HealthCheckProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.HttpTimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"idle": "idle", "per_request": "perRequest"},
    )
    class HttpTimeoutProperty:
        def __init__(
            self,
            *,
            idle: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]] = None,
            per_request: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]] = None,
        ) -> None:
            '''
            :param idle: ``CfnVirtualNode.HttpTimeoutProperty.Idle``.
            :param per_request: ``CfnVirtualNode.HttpTimeoutProperty.PerRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if idle is not None:
                self._values["idle"] = idle
            if per_request is not None:
                self._values["per_request"] = per_request

        @builtins.property
        def idle(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]]:
            '''``CfnVirtualNode.HttpTimeoutProperty.Idle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-idle
            '''
            result = self._values.get("idle")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]], result)

        @builtins.property
        def per_request(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]]:
            '''``CfnVirtualNode.HttpTimeoutProperty.PerRequest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-perrequest
            '''
            result = self._values.get("per_request")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpTimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ListenerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "port_mapping": "portMapping",
            "connection_pool": "connectionPool",
            "health_check": "healthCheck",
            "outlier_detection": "outlierDetection",
            "timeout": "timeout",
            "tls": "tls",
        },
    )
    class ListenerProperty:
        def __init__(
            self,
            *,
            port_mapping: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.PortMappingProperty"],
            connection_pool: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeConnectionPoolProperty"]] = None,
            health_check: typing.Optional[typing.Union["CfnVirtualNode.HealthCheckProperty", aws_cdk.core.IResolvable]] = None,
            outlier_detection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.OutlierDetectionProperty"]] = None,
            timeout: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTimeoutProperty"]] = None,
            tls: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsProperty"]] = None,
        ) -> None:
            '''
            :param port_mapping: ``CfnVirtualNode.ListenerProperty.PortMapping``.
            :param connection_pool: ``CfnVirtualNode.ListenerProperty.ConnectionPool``.
            :param health_check: ``CfnVirtualNode.ListenerProperty.HealthCheck``.
            :param outlier_detection: ``CfnVirtualNode.ListenerProperty.OutlierDetection``.
            :param timeout: ``CfnVirtualNode.ListenerProperty.Timeout``.
            :param tls: ``CfnVirtualNode.ListenerProperty.TLS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "port_mapping": port_mapping,
            }
            if connection_pool is not None:
                self._values["connection_pool"] = connection_pool
            if health_check is not None:
                self._values["health_check"] = health_check
            if outlier_detection is not None:
                self._values["outlier_detection"] = outlier_detection
            if timeout is not None:
                self._values["timeout"] = timeout
            if tls is not None:
                self._values["tls"] = tls

        @builtins.property
        def port_mapping(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.PortMappingProperty"]:
            '''``CfnVirtualNode.ListenerProperty.PortMapping``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-portmapping
            '''
            result = self._values.get("port_mapping")
            assert result is not None, "Required property 'port_mapping' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.PortMappingProperty"], result)

        @builtins.property
        def connection_pool(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeConnectionPoolProperty"]]:
            '''``CfnVirtualNode.ListenerProperty.ConnectionPool``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-connectionpool
            '''
            result = self._values.get("connection_pool")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeConnectionPoolProperty"]], result)

        @builtins.property
        def health_check(
            self,
        ) -> typing.Optional[typing.Union["CfnVirtualNode.HealthCheckProperty", aws_cdk.core.IResolvable]]:
            '''``CfnVirtualNode.ListenerProperty.HealthCheck``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-healthcheck
            '''
            result = self._values.get("health_check")
            return typing.cast(typing.Optional[typing.Union["CfnVirtualNode.HealthCheckProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def outlier_detection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.OutlierDetectionProperty"]]:
            '''``CfnVirtualNode.ListenerProperty.OutlierDetection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-outlierdetection
            '''
            result = self._values.get("outlier_detection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.OutlierDetectionProperty"]], result)

        @builtins.property
        def timeout(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTimeoutProperty"]]:
            '''``CfnVirtualNode.ListenerProperty.Timeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTimeoutProperty"]], result)

        @builtins.property
        def tls(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsProperty"]]:
            '''``CfnVirtualNode.ListenerProperty.TLS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-tls
            '''
            result = self._values.get("tls")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListenerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ListenerTimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"grpc": "grpc", "http": "http", "http2": "http2", "tcp": "tcp"},
    )
    class ListenerTimeoutProperty:
        def __init__(
            self,
            *,
            grpc: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.GrpcTimeoutProperty"]] = None,
            http: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.HttpTimeoutProperty"]] = None,
            http2: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.HttpTimeoutProperty"]] = None,
            tcp: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TcpTimeoutProperty"]] = None,
        ) -> None:
            '''
            :param grpc: ``CfnVirtualNode.ListenerTimeoutProperty.GRPC``.
            :param http: ``CfnVirtualNode.ListenerTimeoutProperty.HTTP``.
            :param http2: ``CfnVirtualNode.ListenerTimeoutProperty.HTTP2``.
            :param tcp: ``CfnVirtualNode.ListenerTimeoutProperty.TCP``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if grpc is not None:
                self._values["grpc"] = grpc
            if http is not None:
                self._values["http"] = http
            if http2 is not None:
                self._values["http2"] = http2
            if tcp is not None:
                self._values["tcp"] = tcp

        @builtins.property
        def grpc(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.GrpcTimeoutProperty"]]:
            '''``CfnVirtualNode.ListenerTimeoutProperty.GRPC``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-grpc
            '''
            result = self._values.get("grpc")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.GrpcTimeoutProperty"]], result)

        @builtins.property
        def http(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.HttpTimeoutProperty"]]:
            '''``CfnVirtualNode.ListenerTimeoutProperty.HTTP``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http
            '''
            result = self._values.get("http")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.HttpTimeoutProperty"]], result)

        @builtins.property
        def http2(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.HttpTimeoutProperty"]]:
            '''``CfnVirtualNode.ListenerTimeoutProperty.HTTP2``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http2
            '''
            result = self._values.get("http2")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.HttpTimeoutProperty"]], result)

        @builtins.property
        def tcp(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TcpTimeoutProperty"]]:
            '''``CfnVirtualNode.ListenerTimeoutProperty.TCP``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-tcp
            '''
            result = self._values.get("tcp")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TcpTimeoutProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListenerTimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ListenerTlsAcmCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_arn": "certificateArn"},
    )
    class ListenerTlsAcmCertificateProperty:
        def __init__(self, *, certificate_arn: builtins.str) -> None:
            '''
            :param certificate_arn: ``CfnVirtualNode.ListenerTlsAcmCertificateProperty.CertificateArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate_arn": certificate_arn,
            }

        @builtins.property
        def certificate_arn(self) -> builtins.str:
            '''``CfnVirtualNode.ListenerTlsAcmCertificateProperty.CertificateArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html#cfn-appmesh-virtualnode-listenertlsacmcertificate-certificatearn
            '''
            result = self._values.get("certificate_arn")
            assert result is not None, "Required property 'certificate_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListenerTlsAcmCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ListenerTlsCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
    )
    class ListenerTlsCertificateProperty:
        def __init__(
            self,
            *,
            acm: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsAcmCertificateProperty"]] = None,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsFileCertificateProperty"]] = None,
            sds: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsSdsCertificateProperty"]] = None,
        ) -> None:
            '''
            :param acm: ``CfnVirtualNode.ListenerTlsCertificateProperty.ACM``.
            :param file: ``CfnVirtualNode.ListenerTlsCertificateProperty.File``.
            :param sds: ``CfnVirtualNode.ListenerTlsCertificateProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if acm is not None:
                self._values["acm"] = acm
            if file is not None:
                self._values["file"] = file
            if sds is not None:
                self._values["sds"] = sds

        @builtins.property
        def acm(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsAcmCertificateProperty"]]:
            '''``CfnVirtualNode.ListenerTlsCertificateProperty.ACM``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-acm
            '''
            result = self._values.get("acm")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsAcmCertificateProperty"]], result)

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsFileCertificateProperty"]]:
            '''``CfnVirtualNode.ListenerTlsCertificateProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsFileCertificateProperty"]], result)

        @builtins.property
        def sds(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsSdsCertificateProperty"]]:
            '''``CfnVirtualNode.ListenerTlsCertificateProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-sds
            '''
            result = self._values.get("sds")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsSdsCertificateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListenerTlsCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ListenerTlsFileCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_chain": "certificateChain",
            "private_key": "privateKey",
        },
    )
    class ListenerTlsFileCertificateProperty:
        def __init__(
            self,
            *,
            certificate_chain: builtins.str,
            private_key: builtins.str,
        ) -> None:
            '''
            :param certificate_chain: ``CfnVirtualNode.ListenerTlsFileCertificateProperty.CertificateChain``.
            :param private_key: ``CfnVirtualNode.ListenerTlsFileCertificateProperty.PrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate_chain": certificate_chain,
                "private_key": private_key,
            }

        @builtins.property
        def certificate_chain(self) -> builtins.str:
            '''``CfnVirtualNode.ListenerTlsFileCertificateProperty.CertificateChain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html#cfn-appmesh-virtualnode-listenertlsfilecertificate-certificatechain
            '''
            result = self._values.get("certificate_chain")
            assert result is not None, "Required property 'certificate_chain' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def private_key(self) -> builtins.str:
            '''``CfnVirtualNode.ListenerTlsFileCertificateProperty.PrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html#cfn-appmesh-virtualnode-listenertlsfilecertificate-privatekey
            '''
            result = self._values.get("private_key")
            assert result is not None, "Required property 'private_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListenerTlsFileCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ListenerTlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate": "certificate",
            "mode": "mode",
            "validation": "validation",
        },
    )
    class ListenerTlsProperty:
        def __init__(
            self,
            *,
            certificate: typing.Union["CfnVirtualNode.ListenerTlsCertificateProperty", aws_cdk.core.IResolvable],
            mode: builtins.str,
            validation: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsValidationContextProperty"]] = None,
        ) -> None:
            '''
            :param certificate: ``CfnVirtualNode.ListenerTlsProperty.Certificate``.
            :param mode: ``CfnVirtualNode.ListenerTlsProperty.Mode``.
            :param validation: ``CfnVirtualNode.ListenerTlsProperty.Validation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate": certificate,
                "mode": mode,
            }
            if validation is not None:
                self._values["validation"] = validation

        @builtins.property
        def certificate(
            self,
        ) -> typing.Union["CfnVirtualNode.ListenerTlsCertificateProperty", aws_cdk.core.IResolvable]:
            '''``CfnVirtualNode.ListenerTlsProperty.Certificate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-certificate
            '''
            result = self._values.get("certificate")
            assert result is not None, "Required property 'certificate' is missing"
            return typing.cast(typing.Union["CfnVirtualNode.ListenerTlsCertificateProperty", aws_cdk.core.IResolvable], result)

        @builtins.property
        def mode(self) -> builtins.str:
            '''``CfnVirtualNode.ListenerTlsProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def validation(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsValidationContextProperty"]]:
            '''``CfnVirtualNode.ListenerTlsProperty.Validation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-validation
            '''
            result = self._values.get("validation")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsValidationContextProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListenerTlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ListenerTlsSdsCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_name": "secretName"},
    )
    class ListenerTlsSdsCertificateProperty:
        def __init__(self, *, secret_name: builtins.str) -> None:
            '''
            :param secret_name: ``CfnVirtualNode.ListenerTlsSdsCertificateProperty.SecretName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlssdscertificate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "secret_name": secret_name,
            }

        @builtins.property
        def secret_name(self) -> builtins.str:
            '''``CfnVirtualNode.ListenerTlsSdsCertificateProperty.SecretName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlssdscertificate.html#cfn-appmesh-virtualnode-listenertlssdscertificate-secretname
            '''
            result = self._values.get("secret_name")
            assert result is not None, "Required property 'secret_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListenerTlsSdsCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ListenerTlsValidationContextProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trust": "trust",
            "subject_alternative_names": "subjectAlternativeNames",
        },
    )
    class ListenerTlsValidationContextProperty:
        def __init__(
            self,
            *,
            trust: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsValidationContextTrustProperty"],
            subject_alternative_names: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.SubjectAlternativeNamesProperty"]] = None,
        ) -> None:
            '''
            :param trust: ``CfnVirtualNode.ListenerTlsValidationContextProperty.Trust``.
            :param subject_alternative_names: ``CfnVirtualNode.ListenerTlsValidationContextProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "trust": trust,
            }
            if subject_alternative_names is not None:
                self._values["subject_alternative_names"] = subject_alternative_names

        @builtins.property
        def trust(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsValidationContextTrustProperty"]:
            '''``CfnVirtualNode.ListenerTlsValidationContextProperty.Trust``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-trust
            '''
            result = self._values.get("trust")
            assert result is not None, "Required property 'trust' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ListenerTlsValidationContextTrustProperty"], result)

        @builtins.property
        def subject_alternative_names(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.SubjectAlternativeNamesProperty"]]:
            '''``CfnVirtualNode.ListenerTlsValidationContextProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-subjectalternativenames
            '''
            result = self._values.get("subject_alternative_names")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.SubjectAlternativeNamesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListenerTlsValidationContextProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ListenerTlsValidationContextTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"file": "file", "sds": "sds"},
    )
    class ListenerTlsValidationContextTrustProperty:
        def __init__(
            self,
            *,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextFileTrustProperty"]] = None,
            sds: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextSdsTrustProperty"]] = None,
        ) -> None:
            '''
            :param file: ``CfnVirtualNode.ListenerTlsValidationContextTrustProperty.File``.
            :param sds: ``CfnVirtualNode.ListenerTlsValidationContextTrustProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if file is not None:
                self._values["file"] = file
            if sds is not None:
                self._values["sds"] = sds

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextFileTrustProperty"]]:
            '''``CfnVirtualNode.ListenerTlsValidationContextTrustProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextFileTrustProperty"]], result)

        @builtins.property
        def sds(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextSdsTrustProperty"]]:
            '''``CfnVirtualNode.ListenerTlsValidationContextTrustProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-sds
            '''
            result = self._values.get("sds")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextSdsTrustProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListenerTlsValidationContextTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.LoggingProperty",
        jsii_struct_bases=[],
        name_mapping={"access_log": "accessLog"},
    )
    class LoggingProperty:
        def __init__(
            self,
            *,
            access_log: typing.Optional[typing.Union["CfnVirtualNode.AccessLogProperty", aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param access_log: ``CfnVirtualNode.LoggingProperty.AccessLog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if access_log is not None:
                self._values["access_log"] = access_log

        @builtins.property
        def access_log(
            self,
        ) -> typing.Optional[typing.Union["CfnVirtualNode.AccessLogProperty", aws_cdk.core.IResolvable]]:
            '''``CfnVirtualNode.LoggingProperty.AccessLog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html#cfn-appmesh-virtualnode-logging-accesslog
            '''
            result = self._values.get("access_log")
            return typing.cast(typing.Optional[typing.Union["CfnVirtualNode.AccessLogProperty", aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.OutlierDetectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_ejection_duration": "baseEjectionDuration",
            "interval": "interval",
            "max_ejection_percent": "maxEjectionPercent",
            "max_server_errors": "maxServerErrors",
        },
    )
    class OutlierDetectionProperty:
        def __init__(
            self,
            *,
            base_ejection_duration: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"],
            interval: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"],
            max_ejection_percent: jsii.Number,
            max_server_errors: jsii.Number,
        ) -> None:
            '''
            :param base_ejection_duration: ``CfnVirtualNode.OutlierDetectionProperty.BaseEjectionDuration``.
            :param interval: ``CfnVirtualNode.OutlierDetectionProperty.Interval``.
            :param max_ejection_percent: ``CfnVirtualNode.OutlierDetectionProperty.MaxEjectionPercent``.
            :param max_server_errors: ``CfnVirtualNode.OutlierDetectionProperty.MaxServerErrors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "base_ejection_duration": base_ejection_duration,
                "interval": interval,
                "max_ejection_percent": max_ejection_percent,
                "max_server_errors": max_server_errors,
            }

        @builtins.property
        def base_ejection_duration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]:
            '''``CfnVirtualNode.OutlierDetectionProperty.BaseEjectionDuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-baseejectionduration
            '''
            result = self._values.get("base_ejection_duration")
            assert result is not None, "Required property 'base_ejection_duration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"], result)

        @builtins.property
        def interval(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]:
            '''``CfnVirtualNode.OutlierDetectionProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-interval
            '''
            result = self._values.get("interval")
            assert result is not None, "Required property 'interval' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"], result)

        @builtins.property
        def max_ejection_percent(self) -> jsii.Number:
            '''``CfnVirtualNode.OutlierDetectionProperty.MaxEjectionPercent``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-maxejectionpercent
            '''
            result = self._values.get("max_ejection_percent")
            assert result is not None, "Required property 'max_ejection_percent' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_server_errors(self) -> jsii.Number:
            '''``CfnVirtualNode.OutlierDetectionProperty.MaxServerErrors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-maxservererrors
            '''
            result = self._values.get("max_server_errors")
            assert result is not None, "Required property 'max_server_errors' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutlierDetectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.PortMappingProperty",
        jsii_struct_bases=[],
        name_mapping={"port": "port", "protocol": "protocol"},
    )
    class PortMappingProperty:
        def __init__(self, *, port: jsii.Number, protocol: builtins.str) -> None:
            '''
            :param port: ``CfnVirtualNode.PortMappingProperty.Port``.
            :param protocol: ``CfnVirtualNode.PortMappingProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "port": port,
                "protocol": protocol,
            }

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnVirtualNode.PortMappingProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html#cfn-appmesh-virtualnode-portmapping-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''``CfnVirtualNode.PortMappingProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html#cfn-appmesh-virtualnode-portmapping-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.ServiceDiscoveryProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_cloud_map": "awsCloudMap", "dns": "dns"},
    )
    class ServiceDiscoveryProperty:
        def __init__(
            self,
            *,
            aws_cloud_map: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty"]] = None,
            dns: typing.Optional[typing.Union["CfnVirtualNode.DnsServiceDiscoveryProperty", aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param aws_cloud_map: ``CfnVirtualNode.ServiceDiscoveryProperty.AWSCloudMap``.
            :param dns: ``CfnVirtualNode.ServiceDiscoveryProperty.DNS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if aws_cloud_map is not None:
                self._values["aws_cloud_map"] = aws_cloud_map
            if dns is not None:
                self._values["dns"] = dns

        @builtins.property
        def aws_cloud_map(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty"]]:
            '''``CfnVirtualNode.ServiceDiscoveryProperty.AWSCloudMap``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-awscloudmap
            '''
            result = self._values.get("aws_cloud_map")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty"]], result)

        @builtins.property
        def dns(
            self,
        ) -> typing.Optional[typing.Union["CfnVirtualNode.DnsServiceDiscoveryProperty", aws_cdk.core.IResolvable]]:
            '''``CfnVirtualNode.ServiceDiscoveryProperty.DNS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-dns
            '''
            result = self._values.get("dns")
            return typing.cast(typing.Optional[typing.Union["CfnVirtualNode.DnsServiceDiscoveryProperty", aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceDiscoveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.SubjectAlternativeNameMatchersProperty",
        jsii_struct_bases=[],
        name_mapping={"exact": "exact"},
    )
    class SubjectAlternativeNameMatchersProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param exact: ``CfnVirtualNode.SubjectAlternativeNameMatchersProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact

        @builtins.property
        def exact(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnVirtualNode.SubjectAlternativeNameMatchersProperty.Exact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html#cfn-appmesh-virtualnode-subjectalternativenamematchers-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectAlternativeNameMatchersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.SubjectAlternativeNamesProperty",
        jsii_struct_bases=[],
        name_mapping={"match": "match"},
    )
    class SubjectAlternativeNamesProperty:
        def __init__(
            self,
            *,
            match: typing.Union["CfnVirtualNode.SubjectAlternativeNameMatchersProperty", aws_cdk.core.IResolvable],
        ) -> None:
            '''
            :param match: ``CfnVirtualNode.SubjectAlternativeNamesProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "match": match,
            }

        @builtins.property
        def match(
            self,
        ) -> typing.Union["CfnVirtualNode.SubjectAlternativeNameMatchersProperty", aws_cdk.core.IResolvable]:
            '''``CfnVirtualNode.SubjectAlternativeNamesProperty.Match``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html#cfn-appmesh-virtualnode-subjectalternativenames-match
            '''
            result = self._values.get("match")
            assert result is not None, "Required property 'match' is missing"
            return typing.cast(typing.Union["CfnVirtualNode.SubjectAlternativeNameMatchersProperty", aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectAlternativeNamesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.TcpTimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"idle": "idle"},
    )
    class TcpTimeoutProperty:
        def __init__(
            self,
            *,
            idle: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]] = None,
        ) -> None:
            '''
            :param idle: ``CfnVirtualNode.TcpTimeoutProperty.Idle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if idle is not None:
                self._values["idle"] = idle

        @builtins.property
        def idle(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]]:
            '''``CfnVirtualNode.TcpTimeoutProperty.Idle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html#cfn-appmesh-virtualnode-tcptimeout-idle
            '''
            result = self._values.get("idle")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.DurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TcpTimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.TlsValidationContextAcmTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_authority_arns": "certificateAuthorityArns"},
    )
    class TlsValidationContextAcmTrustProperty:
        def __init__(
            self,
            *,
            certificate_authority_arns: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param certificate_authority_arns: ``CfnVirtualNode.TlsValidationContextAcmTrustProperty.CertificateAuthorityArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate_authority_arns": certificate_authority_arns,
            }

        @builtins.property
        def certificate_authority_arns(self) -> typing.List[builtins.str]:
            '''``CfnVirtualNode.TlsValidationContextAcmTrustProperty.CertificateAuthorityArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextacmtrust-certificateauthorityarns
            '''
            result = self._values.get("certificate_authority_arns")
            assert result is not None, "Required property 'certificate_authority_arns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TlsValidationContextAcmTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.TlsValidationContextFileTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_chain": "certificateChain"},
    )
    class TlsValidationContextFileTrustProperty:
        def __init__(self, *, certificate_chain: builtins.str) -> None:
            '''
            :param certificate_chain: ``CfnVirtualNode.TlsValidationContextFileTrustProperty.CertificateChain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "certificate_chain": certificate_chain,
            }

        @builtins.property
        def certificate_chain(self) -> builtins.str:
            '''``CfnVirtualNode.TlsValidationContextFileTrustProperty.CertificateChain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextfiletrust-certificatechain
            '''
            result = self._values.get("certificate_chain")
            assert result is not None, "Required property 'certificate_chain' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TlsValidationContextFileTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.TlsValidationContextProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trust": "trust",
            "subject_alternative_names": "subjectAlternativeNames",
        },
    )
    class TlsValidationContextProperty:
        def __init__(
            self,
            *,
            trust: typing.Union["CfnVirtualNode.TlsValidationContextTrustProperty", aws_cdk.core.IResolvable],
            subject_alternative_names: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.SubjectAlternativeNamesProperty"]] = None,
        ) -> None:
            '''
            :param trust: ``CfnVirtualNode.TlsValidationContextProperty.Trust``.
            :param subject_alternative_names: ``CfnVirtualNode.TlsValidationContextProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "trust": trust,
            }
            if subject_alternative_names is not None:
                self._values["subject_alternative_names"] = subject_alternative_names

        @builtins.property
        def trust(
            self,
        ) -> typing.Union["CfnVirtualNode.TlsValidationContextTrustProperty", aws_cdk.core.IResolvable]:
            '''``CfnVirtualNode.TlsValidationContextProperty.Trust``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-trust
            '''
            result = self._values.get("trust")
            assert result is not None, "Required property 'trust' is missing"
            return typing.cast(typing.Union["CfnVirtualNode.TlsValidationContextTrustProperty", aws_cdk.core.IResolvable], result)

        @builtins.property
        def subject_alternative_names(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.SubjectAlternativeNamesProperty"]]:
            '''``CfnVirtualNode.TlsValidationContextProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-subjectalternativenames
            '''
            result = self._values.get("subject_alternative_names")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.SubjectAlternativeNamesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TlsValidationContextProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.TlsValidationContextSdsTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_name": "secretName"},
    )
    class TlsValidationContextSdsTrustProperty:
        def __init__(self, *, secret_name: builtins.str) -> None:
            '''
            :param secret_name: ``CfnVirtualNode.TlsValidationContextSdsTrustProperty.SecretName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "secret_name": secret_name,
            }

        @builtins.property
        def secret_name(self) -> builtins.str:
            '''``CfnVirtualNode.TlsValidationContextSdsTrustProperty.SecretName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextsdstrust-secretname
            '''
            result = self._values.get("secret_name")
            assert result is not None, "Required property 'secret_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TlsValidationContextSdsTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.TlsValidationContextTrustProperty",
        jsii_struct_bases=[],
        name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
    )
    class TlsValidationContextTrustProperty:
        def __init__(
            self,
            *,
            acm: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextAcmTrustProperty"]] = None,
            file: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextFileTrustProperty"]] = None,
            sds: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextSdsTrustProperty"]] = None,
        ) -> None:
            '''
            :param acm: ``CfnVirtualNode.TlsValidationContextTrustProperty.ACM``.
            :param file: ``CfnVirtualNode.TlsValidationContextTrustProperty.File``.
            :param sds: ``CfnVirtualNode.TlsValidationContextTrustProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if acm is not None:
                self._values["acm"] = acm
            if file is not None:
                self._values["file"] = file
            if sds is not None:
                self._values["sds"] = sds

        @builtins.property
        def acm(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextAcmTrustProperty"]]:
            '''``CfnVirtualNode.TlsValidationContextTrustProperty.ACM``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-acm
            '''
            result = self._values.get("acm")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextAcmTrustProperty"]], result)

        @builtins.property
        def file(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextFileTrustProperty"]]:
            '''``CfnVirtualNode.TlsValidationContextTrustProperty.File``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-file
            '''
            result = self._values.get("file")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextFileTrustProperty"]], result)

        @builtins.property
        def sds(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextSdsTrustProperty"]]:
            '''``CfnVirtualNode.TlsValidationContextTrustProperty.SDS``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-sds
            '''
            result = self._values.get("sds")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.TlsValidationContextSdsTrustProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TlsValidationContextTrustProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.VirtualNodeConnectionPoolProperty",
        jsii_struct_bases=[],
        name_mapping={"grpc": "grpc", "http": "http", "http2": "http2", "tcp": "tcp"},
    )
    class VirtualNodeConnectionPoolProperty:
        def __init__(
            self,
            *,
            grpc: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeGrpcConnectionPoolProperty"]] = None,
            http: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeHttpConnectionPoolProperty"]] = None,
            http2: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeHttp2ConnectionPoolProperty"]] = None,
            tcp: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeTcpConnectionPoolProperty"]] = None,
        ) -> None:
            '''
            :param grpc: ``CfnVirtualNode.VirtualNodeConnectionPoolProperty.GRPC``.
            :param http: ``CfnVirtualNode.VirtualNodeConnectionPoolProperty.HTTP``.
            :param http2: ``CfnVirtualNode.VirtualNodeConnectionPoolProperty.HTTP2``.
            :param tcp: ``CfnVirtualNode.VirtualNodeConnectionPoolProperty.TCP``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if grpc is not None:
                self._values["grpc"] = grpc
            if http is not None:
                self._values["http"] = http
            if http2 is not None:
                self._values["http2"] = http2
            if tcp is not None:
                self._values["tcp"] = tcp

        @builtins.property
        def grpc(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeGrpcConnectionPoolProperty"]]:
            '''``CfnVirtualNode.VirtualNodeConnectionPoolProperty.GRPC``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-grpc
            '''
            result = self._values.get("grpc")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeGrpcConnectionPoolProperty"]], result)

        @builtins.property
        def http(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeHttpConnectionPoolProperty"]]:
            '''``CfnVirtualNode.VirtualNodeConnectionPoolProperty.HTTP``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http
            '''
            result = self._values.get("http")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeHttpConnectionPoolProperty"]], result)

        @builtins.property
        def http2(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeHttp2ConnectionPoolProperty"]]:
            '''``CfnVirtualNode.VirtualNodeConnectionPoolProperty.HTTP2``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http2
            '''
            result = self._values.get("http2")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeHttp2ConnectionPoolProperty"]], result)

        @builtins.property
        def tcp(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeTcpConnectionPoolProperty"]]:
            '''``CfnVirtualNode.VirtualNodeConnectionPoolProperty.TCP``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-tcp
            '''
            result = self._values.get("tcp")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.VirtualNodeTcpConnectionPoolProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualNodeConnectionPoolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.VirtualNodeGrpcConnectionPoolProperty",
        jsii_struct_bases=[],
        name_mapping={"max_requests": "maxRequests"},
    )
    class VirtualNodeGrpcConnectionPoolProperty:
        def __init__(self, *, max_requests: jsii.Number) -> None:
            '''
            :param max_requests: ``CfnVirtualNode.VirtualNodeGrpcConnectionPoolProperty.MaxRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_requests": max_requests,
            }

        @builtins.property
        def max_requests(self) -> jsii.Number:
            '''``CfnVirtualNode.VirtualNodeGrpcConnectionPoolProperty.MaxRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html#cfn-appmesh-virtualnode-virtualnodegrpcconnectionpool-maxrequests
            '''
            result = self._values.get("max_requests")
            assert result is not None, "Required property 'max_requests' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualNodeGrpcConnectionPoolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.VirtualNodeHttp2ConnectionPoolProperty",
        jsii_struct_bases=[],
        name_mapping={"max_requests": "maxRequests"},
    )
    class VirtualNodeHttp2ConnectionPoolProperty:
        def __init__(self, *, max_requests: jsii.Number) -> None:
            '''
            :param max_requests: ``CfnVirtualNode.VirtualNodeHttp2ConnectionPoolProperty.MaxRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttp2connectionpool.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_requests": max_requests,
            }

        @builtins.property
        def max_requests(self) -> jsii.Number:
            '''``CfnVirtualNode.VirtualNodeHttp2ConnectionPoolProperty.MaxRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttp2connectionpool.html#cfn-appmesh-virtualnode-virtualnodehttp2connectionpool-maxrequests
            '''
            result = self._values.get("max_requests")
            assert result is not None, "Required property 'max_requests' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualNodeHttp2ConnectionPoolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.VirtualNodeHttpConnectionPoolProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_connections": "maxConnections",
            "max_pending_requests": "maxPendingRequests",
        },
    )
    class VirtualNodeHttpConnectionPoolProperty:
        def __init__(
            self,
            *,
            max_connections: jsii.Number,
            max_pending_requests: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param max_connections: ``CfnVirtualNode.VirtualNodeHttpConnectionPoolProperty.MaxConnections``.
            :param max_pending_requests: ``CfnVirtualNode.VirtualNodeHttpConnectionPoolProperty.MaxPendingRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_connections": max_connections,
            }
            if max_pending_requests is not None:
                self._values["max_pending_requests"] = max_pending_requests

        @builtins.property
        def max_connections(self) -> jsii.Number:
            '''``CfnVirtualNode.VirtualNodeHttpConnectionPoolProperty.MaxConnections``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodehttpconnectionpool-maxconnections
            '''
            result = self._values.get("max_connections")
            assert result is not None, "Required property 'max_connections' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_pending_requests(self) -> typing.Optional[jsii.Number]:
            '''``CfnVirtualNode.VirtualNodeHttpConnectionPoolProperty.MaxPendingRequests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodehttpconnectionpool-maxpendingrequests
            '''
            result = self._values.get("max_pending_requests")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualNodeHttpConnectionPoolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.VirtualNodeSpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "backend_defaults": "backendDefaults",
            "backends": "backends",
            "listeners": "listeners",
            "logging": "logging",
            "service_discovery": "serviceDiscovery",
        },
    )
    class VirtualNodeSpecProperty:
        def __init__(
            self,
            *,
            backend_defaults: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.BackendDefaultsProperty"]] = None,
            backends: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnVirtualNode.BackendProperty", aws_cdk.core.IResolvable]]]] = None,
            listeners: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnVirtualNode.ListenerProperty", aws_cdk.core.IResolvable]]]] = None,
            logging: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.LoggingProperty"]] = None,
            service_discovery: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ServiceDiscoveryProperty"]] = None,
        ) -> None:
            '''
            :param backend_defaults: ``CfnVirtualNode.VirtualNodeSpecProperty.BackendDefaults``.
            :param backends: ``CfnVirtualNode.VirtualNodeSpecProperty.Backends``.
            :param listeners: ``CfnVirtualNode.VirtualNodeSpecProperty.Listeners``.
            :param logging: ``CfnVirtualNode.VirtualNodeSpecProperty.Logging``.
            :param service_discovery: ``CfnVirtualNode.VirtualNodeSpecProperty.ServiceDiscovery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if backend_defaults is not None:
                self._values["backend_defaults"] = backend_defaults
            if backends is not None:
                self._values["backends"] = backends
            if listeners is not None:
                self._values["listeners"] = listeners
            if logging is not None:
                self._values["logging"] = logging
            if service_discovery is not None:
                self._values["service_discovery"] = service_discovery

        @builtins.property
        def backend_defaults(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.BackendDefaultsProperty"]]:
            '''``CfnVirtualNode.VirtualNodeSpecProperty.BackendDefaults``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backenddefaults
            '''
            result = self._values.get("backend_defaults")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.BackendDefaultsProperty"]], result)

        @builtins.property
        def backends(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnVirtualNode.BackendProperty", aws_cdk.core.IResolvable]]]]:
            '''``CfnVirtualNode.VirtualNodeSpecProperty.Backends``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backends
            '''
            result = self._values.get("backends")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnVirtualNode.BackendProperty", aws_cdk.core.IResolvable]]]], result)

        @builtins.property
        def listeners(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnVirtualNode.ListenerProperty", aws_cdk.core.IResolvable]]]]:
            '''``CfnVirtualNode.VirtualNodeSpecProperty.Listeners``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-listeners
            '''
            result = self._values.get("listeners")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnVirtualNode.ListenerProperty", aws_cdk.core.IResolvable]]]], result)

        @builtins.property
        def logging(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.LoggingProperty"]]:
            '''``CfnVirtualNode.VirtualNodeSpecProperty.Logging``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-logging
            '''
            result = self._values.get("logging")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.LoggingProperty"]], result)

        @builtins.property
        def service_discovery(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ServiceDiscoveryProperty"]]:
            '''``CfnVirtualNode.VirtualNodeSpecProperty.ServiceDiscovery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-servicediscovery
            '''
            result = self._values.get("service_discovery")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ServiceDiscoveryProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualNodeSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.VirtualNodeTcpConnectionPoolProperty",
        jsii_struct_bases=[],
        name_mapping={"max_connections": "maxConnections"},
    )
    class VirtualNodeTcpConnectionPoolProperty:
        def __init__(self, *, max_connections: jsii.Number) -> None:
            '''
            :param max_connections: ``CfnVirtualNode.VirtualNodeTcpConnectionPoolProperty.MaxConnections``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodetcpconnectionpool.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_connections": max_connections,
            }

        @builtins.property
        def max_connections(self) -> jsii.Number:
            '''``CfnVirtualNode.VirtualNodeTcpConnectionPoolProperty.MaxConnections``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodetcpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodetcpconnectionpool-maxconnections
            '''
            result = self._values.get("max_connections")
            assert result is not None, "Required property 'max_connections' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualNodeTcpConnectionPoolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNode.VirtualServiceBackendProperty",
        jsii_struct_bases=[],
        name_mapping={
            "virtual_service_name": "virtualServiceName",
            "client_policy": "clientPolicy",
        },
    )
    class VirtualServiceBackendProperty:
        def __init__(
            self,
            *,
            virtual_service_name: builtins.str,
            client_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientPolicyProperty"]] = None,
        ) -> None:
            '''
            :param virtual_service_name: ``CfnVirtualNode.VirtualServiceBackendProperty.VirtualServiceName``.
            :param client_policy: ``CfnVirtualNode.VirtualServiceBackendProperty.ClientPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "virtual_service_name": virtual_service_name,
            }
            if client_policy is not None:
                self._values["client_policy"] = client_policy

        @builtins.property
        def virtual_service_name(self) -> builtins.str:
            '''``CfnVirtualNode.VirtualServiceBackendProperty.VirtualServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html#cfn-appmesh-virtualnode-virtualservicebackend-virtualservicename
            '''
            result = self._values.get("virtual_service_name")
            assert result is not None, "Required property 'virtual_service_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_policy(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientPolicyProperty"]]:
            '''``CfnVirtualNode.VirtualServiceBackendProperty.ClientPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html#cfn-appmesh-virtualnode-virtualservicebackend-clientpolicy
            '''
            result = self._values.get("client_policy")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualNode.ClientPolicyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualServiceBackendProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.CfnVirtualNodeProps",
    jsii_struct_bases=[],
    name_mapping={
        "mesh_name": "meshName",
        "spec": "spec",
        "mesh_owner": "meshOwner",
        "tags": "tags",
        "virtual_node_name": "virtualNodeName",
    },
)
class CfnVirtualNodeProps:
    def __init__(
        self,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, CfnVirtualNode.VirtualNodeSpecProperty],
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        virtual_node_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppMesh::VirtualNode``.

        :param mesh_name: ``AWS::AppMesh::VirtualNode.MeshName``.
        :param spec: ``AWS::AppMesh::VirtualNode.Spec``.
        :param mesh_owner: ``AWS::AppMesh::VirtualNode.MeshOwner``.
        :param tags: ``AWS::AppMesh::VirtualNode.Tags``.
        :param virtual_node_name: ``AWS::AppMesh::VirtualNode.VirtualNodeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if mesh_owner is not None:
            self._values["mesh_owner"] = mesh_owner
        if tags is not None:
            self._values["tags"] = tags
        if virtual_node_name is not None:
            self._values["virtual_node_name"] = virtual_node_name

    @builtins.property
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualNode.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshname
        '''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnVirtualNode.VirtualNodeSpecProperty]:
        '''``AWS::AppMesh::VirtualNode.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnVirtualNode.VirtualNodeSpecProperty], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualNode.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshowner
        '''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppMesh::VirtualNode.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def virtual_node_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualNode.VirtualNodeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-virtualnodename
        '''
        result = self._values.get("virtual_node_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualNodeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnVirtualRouter(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.CfnVirtualRouter",
):
    '''A CloudFormation ``AWS::AppMesh::VirtualRouter``.

    :cloudformationResource: AWS::AppMesh::VirtualRouter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualRouter.VirtualRouterSpecProperty"],
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        virtual_router_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::AppMesh::VirtualRouter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param mesh_name: ``AWS::AppMesh::VirtualRouter.MeshName``.
        :param spec: ``AWS::AppMesh::VirtualRouter.Spec``.
        :param mesh_owner: ``AWS::AppMesh::VirtualRouter.MeshOwner``.
        :param tags: ``AWS::AppMesh::VirtualRouter.Tags``.
        :param virtual_router_name: ``AWS::AppMesh::VirtualRouter.VirtualRouterName``.
        '''
        props = CfnVirtualRouterProps(
            mesh_name=mesh_name,
            spec=spec,
            mesh_owner=mesh_owner,
            tags=tags,
            virtual_router_name=virtual_router_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshName")
    def attr_mesh_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshOwner")
    def attr_mesh_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceOwner")
    def attr_resource_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUid")
    def attr_uid(self) -> builtins.str:
        '''
        :cloudformationAttribute: Uid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVirtualRouterName")
    def attr_virtual_router_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: VirtualRouterName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualRouterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppMesh::VirtualRouter.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualRouter.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshname
        '''
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        jsii.set(self, "meshName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="spec")
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualRouter.VirtualRouterSpecProperty"]:
        '''``AWS::AppMesh::VirtualRouter.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-spec
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualRouter.VirtualRouterSpecProperty"], jsii.get(self, "spec"))

    @spec.setter
    def spec(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualRouter.VirtualRouterSpecProperty"],
    ) -> None:
        jsii.set(self, "spec", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualRouter.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshowner
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "meshOwner", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouterName")
    def virtual_router_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualRouter.VirtualRouterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-virtualroutername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualRouterName"))

    @virtual_router_name.setter
    def virtual_router_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "virtualRouterName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualRouter.PortMappingProperty",
        jsii_struct_bases=[],
        name_mapping={"port": "port", "protocol": "protocol"},
    )
    class PortMappingProperty:
        def __init__(self, *, port: jsii.Number, protocol: builtins.str) -> None:
            '''
            :param port: ``CfnVirtualRouter.PortMappingProperty.Port``.
            :param protocol: ``CfnVirtualRouter.PortMappingProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "port": port,
                "protocol": protocol,
            }

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnVirtualRouter.PortMappingProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html#cfn-appmesh-virtualrouter-portmapping-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''``CfnVirtualRouter.PortMappingProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html#cfn-appmesh-virtualrouter-portmapping-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualRouter.VirtualRouterListenerProperty",
        jsii_struct_bases=[],
        name_mapping={"port_mapping": "portMapping"},
    )
    class VirtualRouterListenerProperty:
        def __init__(
            self,
            *,
            port_mapping: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualRouter.PortMappingProperty"],
        ) -> None:
            '''
            :param port_mapping: ``CfnVirtualRouter.VirtualRouterListenerProperty.PortMapping``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "port_mapping": port_mapping,
            }

        @builtins.property
        def port_mapping(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualRouter.PortMappingProperty"]:
            '''``CfnVirtualRouter.VirtualRouterListenerProperty.PortMapping``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html#cfn-appmesh-virtualrouter-virtualrouterlistener-portmapping
            '''
            result = self._values.get("port_mapping")
            assert result is not None, "Required property 'port_mapping' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualRouter.PortMappingProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualRouterListenerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualRouter.VirtualRouterSpecProperty",
        jsii_struct_bases=[],
        name_mapping={"listeners": "listeners"},
    )
    class VirtualRouterSpecProperty:
        def __init__(
            self,
            *,
            listeners: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnVirtualRouter.VirtualRouterListenerProperty", aws_cdk.core.IResolvable]]],
        ) -> None:
            '''
            :param listeners: ``CfnVirtualRouter.VirtualRouterSpecProperty.Listeners``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "listeners": listeners,
            }

        @builtins.property
        def listeners(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnVirtualRouter.VirtualRouterListenerProperty", aws_cdk.core.IResolvable]]]:
            '''``CfnVirtualRouter.VirtualRouterSpecProperty.Listeners``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html#cfn-appmesh-virtualrouter-virtualrouterspec-listeners
            '''
            result = self._values.get("listeners")
            assert result is not None, "Required property 'listeners' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnVirtualRouter.VirtualRouterListenerProperty", aws_cdk.core.IResolvable]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualRouterSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.CfnVirtualRouterProps",
    jsii_struct_bases=[],
    name_mapping={
        "mesh_name": "meshName",
        "spec": "spec",
        "mesh_owner": "meshOwner",
        "tags": "tags",
        "virtual_router_name": "virtualRouterName",
    },
)
class CfnVirtualRouterProps:
    def __init__(
        self,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, CfnVirtualRouter.VirtualRouterSpecProperty],
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        virtual_router_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppMesh::VirtualRouter``.

        :param mesh_name: ``AWS::AppMesh::VirtualRouter.MeshName``.
        :param spec: ``AWS::AppMesh::VirtualRouter.Spec``.
        :param mesh_owner: ``AWS::AppMesh::VirtualRouter.MeshOwner``.
        :param tags: ``AWS::AppMesh::VirtualRouter.Tags``.
        :param virtual_router_name: ``AWS::AppMesh::VirtualRouter.VirtualRouterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if mesh_owner is not None:
            self._values["mesh_owner"] = mesh_owner
        if tags is not None:
            self._values["tags"] = tags
        if virtual_router_name is not None:
            self._values["virtual_router_name"] = virtual_router_name

    @builtins.property
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualRouter.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshname
        '''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnVirtualRouter.VirtualRouterSpecProperty]:
        '''``AWS::AppMesh::VirtualRouter.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnVirtualRouter.VirtualRouterSpecProperty], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualRouter.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshowner
        '''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppMesh::VirtualRouter.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def virtual_router_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualRouter.VirtualRouterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-virtualroutername
        '''
        result = self._values.get("virtual_router_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualRouterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnVirtualService(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.CfnVirtualService",
):
    '''A CloudFormation ``AWS::AppMesh::VirtualService``.

    :cloudformationResource: AWS::AppMesh::VirtualService
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualServiceSpecProperty"],
        virtual_service_name: builtins.str,
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::AppMesh::VirtualService``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param mesh_name: ``AWS::AppMesh::VirtualService.MeshName``.
        :param spec: ``AWS::AppMesh::VirtualService.Spec``.
        :param virtual_service_name: ``AWS::AppMesh::VirtualService.VirtualServiceName``.
        :param mesh_owner: ``AWS::AppMesh::VirtualService.MeshOwner``.
        :param tags: ``AWS::AppMesh::VirtualService.Tags``.
        '''
        props = CfnVirtualServiceProps(
            mesh_name=mesh_name,
            spec=spec,
            virtual_service_name=virtual_service_name,
            mesh_owner=mesh_owner,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshName")
    def attr_mesh_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMeshOwner")
    def attr_mesh_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: MeshOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMeshOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceOwner")
    def attr_resource_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUid")
    def attr_uid(self) -> builtins.str:
        '''
        :cloudformationAttribute: Uid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVirtualServiceName")
    def attr_virtual_service_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: VirtualServiceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualServiceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppMesh::VirtualService.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualService.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshname
        '''
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        jsii.set(self, "meshName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="spec")
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualServiceSpecProperty"]:
        '''``AWS::AppMesh::VirtualService.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-spec
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualServiceSpecProperty"], jsii.get(self, "spec"))

    @spec.setter
    def spec(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualServiceSpecProperty"],
    ) -> None:
        jsii.set(self, "spec", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualServiceName")
    def virtual_service_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualService.VirtualServiceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-virtualservicename
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualServiceName"))

    @virtual_service_name.setter
    def virtual_service_name(self, value: builtins.str) -> None:
        jsii.set(self, "virtualServiceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualService.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshowner
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "meshOwner", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualService.VirtualNodeServiceProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"virtual_node_name": "virtualNodeName"},
    )
    class VirtualNodeServiceProviderProperty:
        def __init__(self, *, virtual_node_name: builtins.str) -> None:
            '''
            :param virtual_node_name: ``CfnVirtualService.VirtualNodeServiceProviderProperty.VirtualNodeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "virtual_node_name": virtual_node_name,
            }

        @builtins.property
        def virtual_node_name(self) -> builtins.str:
            '''``CfnVirtualService.VirtualNodeServiceProviderProperty.VirtualNodeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html#cfn-appmesh-virtualservice-virtualnodeserviceprovider-virtualnodename
            '''
            result = self._values.get("virtual_node_name")
            assert result is not None, "Required property 'virtual_node_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualNodeServiceProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualService.VirtualRouterServiceProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"virtual_router_name": "virtualRouterName"},
    )
    class VirtualRouterServiceProviderProperty:
        def __init__(self, *, virtual_router_name: builtins.str) -> None:
            '''
            :param virtual_router_name: ``CfnVirtualService.VirtualRouterServiceProviderProperty.VirtualRouterName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "virtual_router_name": virtual_router_name,
            }

        @builtins.property
        def virtual_router_name(self) -> builtins.str:
            '''``CfnVirtualService.VirtualRouterServiceProviderProperty.VirtualRouterName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html#cfn-appmesh-virtualservice-virtualrouterserviceprovider-virtualroutername
            '''
            result = self._values.get("virtual_router_name")
            assert result is not None, "Required property 'virtual_router_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualRouterServiceProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualService.VirtualServiceProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "virtual_node": "virtualNode",
            "virtual_router": "virtualRouter",
        },
    )
    class VirtualServiceProviderProperty:
        def __init__(
            self,
            *,
            virtual_node: typing.Optional[typing.Union["CfnVirtualService.VirtualNodeServiceProviderProperty", aws_cdk.core.IResolvable]] = None,
            virtual_router: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualRouterServiceProviderProperty"]] = None,
        ) -> None:
            '''
            :param virtual_node: ``CfnVirtualService.VirtualServiceProviderProperty.VirtualNode``.
            :param virtual_router: ``CfnVirtualService.VirtualServiceProviderProperty.VirtualRouter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if virtual_node is not None:
                self._values["virtual_node"] = virtual_node
            if virtual_router is not None:
                self._values["virtual_router"] = virtual_router

        @builtins.property
        def virtual_node(
            self,
        ) -> typing.Optional[typing.Union["CfnVirtualService.VirtualNodeServiceProviderProperty", aws_cdk.core.IResolvable]]:
            '''``CfnVirtualService.VirtualServiceProviderProperty.VirtualNode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualnode
            '''
            result = self._values.get("virtual_node")
            return typing.cast(typing.Optional[typing.Union["CfnVirtualService.VirtualNodeServiceProviderProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def virtual_router(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualRouterServiceProviderProperty"]]:
            '''``CfnVirtualService.VirtualServiceProviderProperty.VirtualRouter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualrouter
            '''
            result = self._values.get("virtual_router")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualRouterServiceProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualServiceProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appmesh.CfnVirtualService.VirtualServiceSpecProperty",
        jsii_struct_bases=[],
        name_mapping={"provider": "provider"},
    )
    class VirtualServiceSpecProperty:
        def __init__(
            self,
            *,
            provider: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualServiceProviderProperty"]] = None,
        ) -> None:
            '''
            :param provider: ``CfnVirtualService.VirtualServiceSpecProperty.Provider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if provider is not None:
                self._values["provider"] = provider

        @builtins.property
        def provider(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualServiceProviderProperty"]]:
            '''``CfnVirtualService.VirtualServiceSpecProperty.Provider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html#cfn-appmesh-virtualservice-virtualservicespec-provider
            '''
            result = self._values.get("provider")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnVirtualService.VirtualServiceProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VirtualServiceSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.CfnVirtualServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "mesh_name": "meshName",
        "spec": "spec",
        "virtual_service_name": "virtualServiceName",
        "mesh_owner": "meshOwner",
        "tags": "tags",
    },
)
class CfnVirtualServiceProps:
    def __init__(
        self,
        *,
        mesh_name: builtins.str,
        spec: typing.Union[aws_cdk.core.IResolvable, CfnVirtualService.VirtualServiceSpecProperty],
        virtual_service_name: builtins.str,
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppMesh::VirtualService``.

        :param mesh_name: ``AWS::AppMesh::VirtualService.MeshName``.
        :param spec: ``AWS::AppMesh::VirtualService.Spec``.
        :param virtual_service_name: ``AWS::AppMesh::VirtualService.VirtualServiceName``.
        :param mesh_owner: ``AWS::AppMesh::VirtualService.MeshOwner``.
        :param tags: ``AWS::AppMesh::VirtualService.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh_name": mesh_name,
            "spec": spec,
            "virtual_service_name": virtual_service_name,
        }
        if mesh_owner is not None:
            self._values["mesh_owner"] = mesh_owner
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def mesh_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualService.MeshName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshname
        '''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnVirtualService.VirtualServiceSpecProperty]:
        '''``AWS::AppMesh::VirtualService.Spec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnVirtualService.VirtualServiceSpecProperty], result)

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''``AWS::AppMesh::VirtualService.VirtualServiceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-virtualservicename
        '''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppMesh::VirtualService.MeshOwner``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshowner
        '''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppMesh::VirtualService.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appmesh.DnsResponseType")
class DnsResponseType(enum.Enum):
    '''Enum of DNS service discovery response type.'''

    LOAD_BALANCER = "LOAD_BALANCER"
    '''DNS resolver returns a loadbalanced set of endpoints and the traffic would be sent to the given endpoints.

    It would not drain existing connections to other endpoints that are not part of this list.
    '''
    ENDPOINTS = "ENDPOINTS"
    '''DNS resolver is returning all the endpoints.

    This also means that if an endpoint is missing, it would drain the current connections to the missing endpoint.
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GatewayRouteAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_route_name": "gatewayRouteName",
        "virtual_gateway": "virtualGateway",
    },
)
class GatewayRouteAttributes:
    def __init__(
        self,
        *,
        gateway_route_name: builtins.str,
        virtual_gateway: "IVirtualGateway",
    ) -> None:
        '''Interface with properties necessary to import a reusable GatewayRoute.

        :param gateway_route_name: The name of the GatewayRoute.
        :param virtual_gateway: The VirtualGateway this GatewayRoute is associated with.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "gateway_route_name": gateway_route_name,
            "virtual_gateway": virtual_gateway,
        }

    @builtins.property
    def gateway_route_name(self) -> builtins.str:
        '''The name of the GatewayRoute.'''
        result = self._values.get("gateway_route_name")
        assert result is not None, "Required property 'gateway_route_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_gateway(self) -> "IVirtualGateway":
        '''The VirtualGateway this GatewayRoute is associated with.'''
        result = self._values.get("virtual_gateway")
        assert result is not None, "Required property 'virtual_gateway' is missing"
        return typing.cast("IVirtualGateway", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayRouteAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GatewayRouteBaseProps",
    jsii_struct_bases=[],
    name_mapping={"route_spec": "routeSpec", "gateway_route_name": "gatewayRouteName"},
)
class GatewayRouteBaseProps:
    def __init__(
        self,
        *,
        route_spec: "GatewayRouteSpec",
        gateway_route_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Basic configuration properties for a GatewayRoute.

        :param route_spec: What protocol the route uses.
        :param gateway_route_name: The name of the GatewayRoute. Default: - an automatically generated name
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "route_spec": route_spec,
        }
        if gateway_route_name is not None:
            self._values["gateway_route_name"] = gateway_route_name

    @builtins.property
    def route_spec(self) -> "GatewayRouteSpec":
        '''What protocol the route uses.'''
        result = self._values.get("route_spec")
        assert result is not None, "Required property 'route_spec' is missing"
        return typing.cast("GatewayRouteSpec", result)

    @builtins.property
    def gateway_route_name(self) -> typing.Optional[builtins.str]:
        '''The name of the GatewayRoute.

        :default: - an automatically generated name
        '''
        result = self._values.get("gateway_route_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayRouteBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GatewayRouteHostnameMatch(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.GatewayRouteHostnameMatch",
):
    '''Used to generate host name matching methods.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="endsWith") # type: ignore[misc]
    @builtins.classmethod
    def ends_with(cls, suffix: builtins.str) -> "GatewayRouteHostnameMatch":
        '''The value of the host name with the given name must end with the specified characters.

        :param suffix: The specified ending characters of the host name to match on.
        '''
        return typing.cast("GatewayRouteHostnameMatch", jsii.sinvoke(cls, "endsWith", [suffix]))

    @jsii.member(jsii_name="exactly") # type: ignore[misc]
    @builtins.classmethod
    def exactly(cls, name: builtins.str) -> "GatewayRouteHostnameMatch":
        '''The value of the host name must match the specified value exactly.

        :param name: The exact host name to match on.
        '''
        return typing.cast("GatewayRouteHostnameMatch", jsii.sinvoke(cls, "exactly", [name]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "GatewayRouteHostnameMatchConfig":
        '''Returns the gateway route host name match configuration.

        :param scope: -
        '''
        ...


class _GatewayRouteHostnameMatchProxy(GatewayRouteHostnameMatch):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "GatewayRouteHostnameMatchConfig":
        '''Returns the gateway route host name match configuration.

        :param scope: -
        '''
        return typing.cast("GatewayRouteHostnameMatchConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, GatewayRouteHostnameMatch).__jsii_proxy_class__ = lambda : _GatewayRouteHostnameMatchProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GatewayRouteHostnameMatchConfig",
    jsii_struct_bases=[],
    name_mapping={"hostname_match": "hostnameMatch"},
)
class GatewayRouteHostnameMatchConfig:
    def __init__(
        self,
        *,
        hostname_match: CfnGatewayRoute.GatewayRouteHostnameMatchProperty,
    ) -> None:
        '''Configuration for gateway route host name match.

        :param hostname_match: GatewayRoute CFN configuration for host name match.
        '''
        if isinstance(hostname_match, dict):
            hostname_match = CfnGatewayRoute.GatewayRouteHostnameMatchProperty(**hostname_match)
        self._values: typing.Dict[str, typing.Any] = {
            "hostname_match": hostname_match,
        }

    @builtins.property
    def hostname_match(self) -> CfnGatewayRoute.GatewayRouteHostnameMatchProperty:
        '''GatewayRoute CFN configuration for host name match.'''
        result = self._values.get("hostname_match")
        assert result is not None, "Required property 'hostname_match' is missing"
        return typing.cast(CfnGatewayRoute.GatewayRouteHostnameMatchProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayRouteHostnameMatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GatewayRouteProps",
    jsii_struct_bases=[GatewayRouteBaseProps],
    name_mapping={
        "route_spec": "routeSpec",
        "gateway_route_name": "gatewayRouteName",
        "virtual_gateway": "virtualGateway",
    },
)
class GatewayRouteProps(GatewayRouteBaseProps):
    def __init__(
        self,
        *,
        route_spec: "GatewayRouteSpec",
        gateway_route_name: typing.Optional[builtins.str] = None,
        virtual_gateway: "IVirtualGateway",
    ) -> None:
        '''Properties to define a new GatewayRoute.

        :param route_spec: What protocol the route uses.
        :param gateway_route_name: The name of the GatewayRoute. Default: - an automatically generated name
        :param virtual_gateway: The VirtualGateway this GatewayRoute is associated with.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "route_spec": route_spec,
            "virtual_gateway": virtual_gateway,
        }
        if gateway_route_name is not None:
            self._values["gateway_route_name"] = gateway_route_name

    @builtins.property
    def route_spec(self) -> "GatewayRouteSpec":
        '''What protocol the route uses.'''
        result = self._values.get("route_spec")
        assert result is not None, "Required property 'route_spec' is missing"
        return typing.cast("GatewayRouteSpec", result)

    @builtins.property
    def gateway_route_name(self) -> typing.Optional[builtins.str]:
        '''The name of the GatewayRoute.

        :default: - an automatically generated name
        '''
        result = self._values.get("gateway_route_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_gateway(self) -> "IVirtualGateway":
        '''The VirtualGateway this GatewayRoute is associated with.'''
        result = self._values.get("virtual_gateway")
        assert result is not None, "Required property 'virtual_gateway' is missing"
        return typing.cast("IVirtualGateway", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayRouteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GatewayRouteSpec(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.GatewayRouteSpec",
):
    '''Used to generate specs with different protocols for a GatewayRoute.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="grpc") # type: ignore[misc]
    @builtins.classmethod
    def grpc(
        cls,
        *,
        match: "GrpcGatewayRouteMatch",
        route_target: "IVirtualService",
    ) -> "GatewayRouteSpec":
        '''Creates an gRPC Based GatewayRoute.

        :param match: The criterion for determining a request match for this GatewayRoute.
        :param route_target: The VirtualService this GatewayRoute directs traffic to.
        '''
        options = GrpcGatewayRouteSpecOptions(match=match, route_target=route_target)

        return typing.cast("GatewayRouteSpec", jsii.sinvoke(cls, "grpc", [options]))

    @jsii.member(jsii_name="http") # type: ignore[misc]
    @builtins.classmethod
    def http(
        cls,
        *,
        route_target: "IVirtualService",
        match: typing.Optional["HttpGatewayRouteMatch"] = None,
    ) -> "GatewayRouteSpec":
        '''Creates an HTTP Based GatewayRoute.

        :param route_target: The VirtualService this GatewayRoute directs traffic to.
        :param match: The criterion for determining a request match for this GatewayRoute. When path match is defined, this may optionally determine the path rewrite configuration. Default: - matches any path and automatically rewrites the path to '/'
        '''
        options = HttpGatewayRouteSpecOptions(route_target=route_target, match=match)

        return typing.cast("GatewayRouteSpec", jsii.sinvoke(cls, "http", [options]))

    @jsii.member(jsii_name="http2") # type: ignore[misc]
    @builtins.classmethod
    def http2(
        cls,
        *,
        route_target: "IVirtualService",
        match: typing.Optional["HttpGatewayRouteMatch"] = None,
    ) -> "GatewayRouteSpec":
        '''Creates an HTTP2 Based GatewayRoute.

        :param route_target: The VirtualService this GatewayRoute directs traffic to.
        :param match: The criterion for determining a request match for this GatewayRoute. When path match is defined, this may optionally determine the path rewrite configuration. Default: - matches any path and automatically rewrites the path to '/'
        '''
        options = HttpGatewayRouteSpecOptions(route_target=route_target, match=match)

        return typing.cast("GatewayRouteSpec", jsii.sinvoke(cls, "http2", [options]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "GatewayRouteSpecConfig":
        '''Called when the GatewayRouteSpec type is initialized.

        Can be used to enforce
        mutual exclusivity with future properties

        :param scope: -
        '''
        ...


class _GatewayRouteSpecProxy(GatewayRouteSpec):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "GatewayRouteSpecConfig":
        '''Called when the GatewayRouteSpec type is initialized.

        Can be used to enforce
        mutual exclusivity with future properties

        :param scope: -
        '''
        return typing.cast("GatewayRouteSpecConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, GatewayRouteSpec).__jsii_proxy_class__ = lambda : _GatewayRouteSpecProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GatewayRouteSpecConfig",
    jsii_struct_bases=[],
    name_mapping={
        "grpc_spec_config": "grpcSpecConfig",
        "http2_spec_config": "http2SpecConfig",
        "http_spec_config": "httpSpecConfig",
    },
)
class GatewayRouteSpecConfig:
    def __init__(
        self,
        *,
        grpc_spec_config: typing.Optional[CfnGatewayRoute.GrpcGatewayRouteProperty] = None,
        http2_spec_config: typing.Optional[CfnGatewayRoute.HttpGatewayRouteProperty] = None,
        http_spec_config: typing.Optional[CfnGatewayRoute.HttpGatewayRouteProperty] = None,
    ) -> None:
        '''All Properties for GatewayRoute Specs.

        :param grpc_spec_config: The spec for a grpc gateway route. Default: - no grpc spec
        :param http2_spec_config: The spec for an http2 gateway route. Default: - no http2 spec
        :param http_spec_config: The spec for an http gateway route. Default: - no http spec
        '''
        if isinstance(grpc_spec_config, dict):
            grpc_spec_config = CfnGatewayRoute.GrpcGatewayRouteProperty(**grpc_spec_config)
        if isinstance(http2_spec_config, dict):
            http2_spec_config = CfnGatewayRoute.HttpGatewayRouteProperty(**http2_spec_config)
        if isinstance(http_spec_config, dict):
            http_spec_config = CfnGatewayRoute.HttpGatewayRouteProperty(**http_spec_config)
        self._values: typing.Dict[str, typing.Any] = {}
        if grpc_spec_config is not None:
            self._values["grpc_spec_config"] = grpc_spec_config
        if http2_spec_config is not None:
            self._values["http2_spec_config"] = http2_spec_config
        if http_spec_config is not None:
            self._values["http_spec_config"] = http_spec_config

    @builtins.property
    def grpc_spec_config(
        self,
    ) -> typing.Optional[CfnGatewayRoute.GrpcGatewayRouteProperty]:
        '''The spec for a grpc gateway route.

        :default: - no grpc spec
        '''
        result = self._values.get("grpc_spec_config")
        return typing.cast(typing.Optional[CfnGatewayRoute.GrpcGatewayRouteProperty], result)

    @builtins.property
    def http2_spec_config(
        self,
    ) -> typing.Optional[CfnGatewayRoute.HttpGatewayRouteProperty]:
        '''The spec for an http2 gateway route.

        :default: - no http2 spec
        '''
        result = self._values.get("http2_spec_config")
        return typing.cast(typing.Optional[CfnGatewayRoute.HttpGatewayRouteProperty], result)

    @builtins.property
    def http_spec_config(
        self,
    ) -> typing.Optional[CfnGatewayRoute.HttpGatewayRouteProperty]:
        '''The spec for an http gateway route.

        :default: - no http spec
        '''
        result = self._values.get("http_spec_config")
        return typing.cast(typing.Optional[CfnGatewayRoute.HttpGatewayRouteProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayRouteSpecConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"max_requests": "maxRequests"},
)
class GrpcConnectionPool:
    def __init__(self, *, max_requests: jsii.Number) -> None:
        '''Connection pool properties for gRPC listeners.

        :param max_requests: The maximum requests in the pool. Default: - none
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_requests": max_requests,
        }

    @builtins.property
    def max_requests(self) -> jsii.Number:
        '''The maximum requests in the pool.

        :default: - none
        '''
        result = self._values.get("max_requests")
        assert result is not None, "Required property 'max_requests' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcGatewayListenerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "port": "port",
        "tls": "tls",
    },
)
class GrpcGatewayListenerOptions:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional[GrpcConnectionPool] = None,
        health_check: typing.Optional["HealthCheck"] = None,
        port: typing.Optional[jsii.Number] = None,
        tls: typing.Optional["ListenerTlsOptions"] = None,
    ) -> None:
        '''Represents the properties needed to define GRPC Listeners for a VirtualGateway.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param port: Port to listen for connections on. Default: - 8080
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        if isinstance(connection_pool, dict):
            connection_pool = GrpcConnectionPool(**connection_pool)
        if isinstance(tls, dict):
            tls = ListenerTlsOptions(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(self) -> typing.Optional[GrpcConnectionPool]:
        '''Connection pool for http listeners.

        :default: - None
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional[GrpcConnectionPool], result)

    @builtins.property
    def health_check(self) -> typing.Optional["HealthCheck"]:
        '''The health check information for the listener.

        :default: - no healthcheck
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["HealthCheck"], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to listen for connections on.

        :default: - 8080
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls(self) -> typing.Optional["ListenerTlsOptions"]:
        '''Represents the configuration for enabling TLS on a listener.

        :default: - none
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["ListenerTlsOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcGatewayListenerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcGatewayRouteMatch",
    jsii_struct_bases=[],
    name_mapping={
        "hostname": "hostname",
        "metadata": "metadata",
        "rewrite_request_hostname": "rewriteRequestHostname",
        "service_name": "serviceName",
    },
)
class GrpcGatewayRouteMatch:
    def __init__(
        self,
        *,
        hostname: typing.Optional[GatewayRouteHostnameMatch] = None,
        metadata: typing.Optional[typing.Sequence["HeaderMatch"]] = None,
        rewrite_request_hostname: typing.Optional[builtins.bool] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The criterion for determining a request match for this GatewayRoute.

        :param hostname: Create host name based gRPC gateway route match. Default: - no matching on host name
        :param metadata: Create metadata based gRPC gateway route match. All specified metadata must match for the route to match. Default: - no matching on metadata
        :param rewrite_request_hostname: When ``true``, rewrites the original request received at the Virtual Gateway to the destination Virtual Service name. When ``false``, retains the original hostname from the request. Default: true
        :param service_name: Create service name based gRPC gateway route match. Default: - no matching on service name
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if metadata is not None:
            self._values["metadata"] = metadata
        if rewrite_request_hostname is not None:
            self._values["rewrite_request_hostname"] = rewrite_request_hostname
        if service_name is not None:
            self._values["service_name"] = service_name

    @builtins.property
    def hostname(self) -> typing.Optional[GatewayRouteHostnameMatch]:
        '''Create host name based gRPC gateway route match.

        :default: - no matching on host name
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[GatewayRouteHostnameMatch], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.List["HeaderMatch"]]:
        '''Create metadata based gRPC gateway route match.

        All specified metadata must match for the route to match.

        :default: - no matching on metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.List["HeaderMatch"]], result)

    @builtins.property
    def rewrite_request_hostname(self) -> typing.Optional[builtins.bool]:
        '''When ``true``, rewrites the original request received at the Virtual Gateway to the destination Virtual Service name.

        When ``false``, retains the original hostname from the request.

        :default: true
        '''
        result = self._values.get("rewrite_request_hostname")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Create service name based gRPC gateway route match.

        :default: - no matching on service name
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcGatewayRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcGatewayRouteSpecOptions",
    jsii_struct_bases=[],
    name_mapping={"match": "match", "route_target": "routeTarget"},
)
class GrpcGatewayRouteSpecOptions:
    def __init__(
        self,
        *,
        match: GrpcGatewayRouteMatch,
        route_target: "IVirtualService",
    ) -> None:
        '''Properties specific for a gRPC GatewayRoute.

        :param match: The criterion for determining a request match for this GatewayRoute.
        :param route_target: The VirtualService this GatewayRoute directs traffic to.
        '''
        if isinstance(match, dict):
            match = GrpcGatewayRouteMatch(**match)
        self._values: typing.Dict[str, typing.Any] = {
            "match": match,
            "route_target": route_target,
        }

    @builtins.property
    def match(self) -> GrpcGatewayRouteMatch:
        '''The criterion for determining a request match for this GatewayRoute.'''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast(GrpcGatewayRouteMatch, result)

    @builtins.property
    def route_target(self) -> "IVirtualService":
        '''The VirtualService this GatewayRoute directs traffic to.'''
        result = self._values.get("route_target")
        assert result is not None, "Required property 'route_target' is missing"
        return typing.cast("IVirtualService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcGatewayRouteSpecOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcHealthCheckOptions",
    jsii_struct_bases=[],
    name_mapping={
        "healthy_threshold": "healthyThreshold",
        "interval": "interval",
        "timeout": "timeout",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class GrpcHealthCheckOptions:
    def __init__(
        self,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[aws_cdk.core.Duration] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties used to define GRPC Based healthchecks.

        :param healthy_threshold: The number of consecutive successful health checks that must occur before declaring listener healthy. Default: 2
        :param interval: The time period between each health check execution. Default: Duration.seconds(5)
        :param timeout: The amount of time to wait when receiving a response from the health check. Default: Duration.seconds(2)
        :param unhealthy_threshold: The number of consecutive failed health checks that must occur before declaring a listener unhealthy. Default: - 2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if interval is not None:
            self._values["interval"] = interval
        if timeout is not None:
            self._values["timeout"] = timeout
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive successful health checks that must occur before declaring listener healthy.

        :default: 2
        '''
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The time period between each health check execution.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The amount of time to wait when receiving a response from the health check.

        :default: Duration.seconds(2)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive failed health checks that must occur before declaring a listener unhealthy.

        :default: - 2
        '''
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcHealthCheckOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appmesh.GrpcRetryEvent")
class GrpcRetryEvent(enum.Enum):
    '''gRPC events.'''

    CANCELLED = "CANCELLED"
    '''Request was cancelled.

    :see: https://grpc.github.io/grpc/core/md_doc_statuscodes.html
    '''
    DEADLINE_EXCEEDED = "DEADLINE_EXCEEDED"
    '''The deadline was exceeded.

    :see: https://grpc.github.io/grpc/core/md_doc_statuscodes.html
    '''
    INTERNAL_ERROR = "INTERNAL_ERROR"
    '''Internal error.

    :see: https://grpc.github.io/grpc/core/md_doc_statuscodes.html
    '''
    RESOURCE_EXHAUSTED = "RESOURCE_EXHAUSTED"
    '''A resource was exhausted.

    :see: https://grpc.github.io/grpc/core/md_doc_statuscodes.html
    '''
    UNAVAILABLE = "UNAVAILABLE"
    '''The service is unavailable.

    :see: https://grpc.github.io/grpc/core/md_doc_statuscodes.html
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcRouteMatch",
    jsii_struct_bases=[],
    name_mapping={
        "metadata": "metadata",
        "method_name": "methodName",
        "service_name": "serviceName",
    },
)
class GrpcRouteMatch:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Sequence["HeaderMatch"]] = None,
        method_name: typing.Optional[builtins.str] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The criterion for determining a request match for this Route.

        At least one match type must be selected.

        :param metadata: Create metadata based gRPC route match. All specified metadata must match for the route to match. Default: - do not match on metadata
        :param method_name: The method name to match from the request. If the method name is specified, service name must be also provided. Default: - do not match on method name
        :param service_name: Create service name based gRPC route match. Default: - do not match on service name
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if method_name is not None:
            self._values["method_name"] = method_name
        if service_name is not None:
            self._values["service_name"] = service_name

    @builtins.property
    def metadata(self) -> typing.Optional[typing.List["HeaderMatch"]]:
        '''Create metadata based gRPC route match.

        All specified metadata must match for the route to match.

        :default: - do not match on metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.List["HeaderMatch"]], result)

    @builtins.property
    def method_name(self) -> typing.Optional[builtins.str]:
        '''The method name to match from the request.

        If the method name is specified, service name must be also provided.

        :default: - do not match on method name
        '''
        result = self._values.get("method_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Create service name based gRPC route match.

        :default: - do not match on service name
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcTimeout",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class GrpcTimeout:
    def __init__(
        self,
        *,
        idle: typing.Optional[aws_cdk.core.Duration] = None,
        per_request: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        '''Represents timeouts for GRPC protocols.

        :param idle: Represents an idle timeout. The amount of time that a connection may be idle. Default: - none
        :param per_request: Represents per request timeout. Default: - 15 s
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''Represents an idle timeout.

        The amount of time that a connection may be idle.

        :default: - none
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def per_request(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''Represents per request timeout.

        :default: - 15 s
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcVirtualNodeListenerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "outlier_detection": "outlierDetection",
        "port": "port",
        "timeout": "timeout",
        "tls": "tls",
    },
)
class GrpcVirtualNodeListenerOptions:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional[GrpcConnectionPool] = None,
        health_check: typing.Optional["HealthCheck"] = None,
        outlier_detection: typing.Optional["OutlierDetection"] = None,
        port: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[GrpcTimeout] = None,
        tls: typing.Optional["ListenerTlsOptions"] = None,
    ) -> None:
        '''Represent the GRPC Node Listener prorperty.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param outlier_detection: Represents the configuration for enabling outlier detection. Default: - none
        :param port: Port to listen for connections on. Default: - 8080
        :param timeout: Timeout for GRPC protocol. Default: - None
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        if isinstance(connection_pool, dict):
            connection_pool = GrpcConnectionPool(**connection_pool)
        if isinstance(outlier_detection, dict):
            outlier_detection = OutlierDetection(**outlier_detection)
        if isinstance(timeout, dict):
            timeout = GrpcTimeout(**timeout)
        if isinstance(tls, dict):
            tls = ListenerTlsOptions(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port is not None:
            self._values["port"] = port
        if timeout is not None:
            self._values["timeout"] = timeout
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(self) -> typing.Optional[GrpcConnectionPool]:
        '''Connection pool for http listeners.

        :default: - None
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional[GrpcConnectionPool], result)

    @builtins.property
    def health_check(self) -> typing.Optional["HealthCheck"]:
        '''The health check information for the listener.

        :default: - no healthcheck
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["HealthCheck"], result)

    @builtins.property
    def outlier_detection(self) -> typing.Optional["OutlierDetection"]:
        '''Represents the configuration for enabling outlier detection.

        :default: - none
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["OutlierDetection"], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to listen for connections on.

        :default: - 8080
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout(self) -> typing.Optional[GrpcTimeout]:
        '''Timeout for GRPC protocol.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[GrpcTimeout], result)

    @builtins.property
    def tls(self) -> typing.Optional["ListenerTlsOptions"]:
        '''Represents the configuration for enabling TLS on a listener.

        :default: - none
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["ListenerTlsOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcVirtualNodeListenerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HeaderMatch(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.HeaderMatch",
):
    '''Used to generate header matching methods.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="valueDoesNotEndWith") # type: ignore[misc]
    @builtins.classmethod
    def value_does_not_end_with(
        cls,
        header_name: builtins.str,
        suffix: builtins.str,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must not end with the specified characters.

        :param header_name: the name of the header to match against.
        :param suffix: The suffix to test against.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valueDoesNotEndWith", [header_name, suffix]))

    @jsii.member(jsii_name="valueDoesNotMatchRegex") # type: ignore[misc]
    @builtins.classmethod
    def value_does_not_match_regex(
        cls,
        header_name: builtins.str,
        regex: builtins.str,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must not include the specified characters.

        :param header_name: the name of the header to match against.
        :param regex: The regex to test against.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valueDoesNotMatchRegex", [header_name, regex]))

    @jsii.member(jsii_name="valueDoesNotStartWith") # type: ignore[misc]
    @builtins.classmethod
    def value_does_not_start_with(
        cls,
        header_name: builtins.str,
        prefix: builtins.str,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must not start with the specified characters.

        :param header_name: the name of the header to match against.
        :param prefix: The prefix to test against.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valueDoesNotStartWith", [header_name, prefix]))

    @jsii.member(jsii_name="valueEndsWith") # type: ignore[misc]
    @builtins.classmethod
    def value_ends_with(
        cls,
        header_name: builtins.str,
        suffix: builtins.str,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must end with the specified characters.

        :param header_name: the name of the header to match against.
        :param suffix: The suffix to test against.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valueEndsWith", [header_name, suffix]))

    @jsii.member(jsii_name="valueIs") # type: ignore[misc]
    @builtins.classmethod
    def value_is(
        cls,
        header_name: builtins.str,
        header_value: builtins.str,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must match the specified value exactly.

        :param header_name: the name of the header to match against.
        :param header_value: The exact value to test against.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valueIs", [header_name, header_value]))

    @jsii.member(jsii_name="valueIsNot") # type: ignore[misc]
    @builtins.classmethod
    def value_is_not(
        cls,
        header_name: builtins.str,
        header_value: builtins.str,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must not match the specified value exactly.

        :param header_name: the name of the header to match against.
        :param header_value: The exact value to test against.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valueIsNot", [header_name, header_value]))

    @jsii.member(jsii_name="valueMatchesRegex") # type: ignore[misc]
    @builtins.classmethod
    def value_matches_regex(
        cls,
        header_name: builtins.str,
        regex: builtins.str,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must include the specified characters.

        :param header_name: the name of the header to match against.
        :param regex: The regex to test against.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valueMatchesRegex", [header_name, regex]))

    @jsii.member(jsii_name="valuesIsInRange") # type: ignore[misc]
    @builtins.classmethod
    def values_is_in_range(
        cls,
        header_name: builtins.str,
        start: jsii.Number,
        end: jsii.Number,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must be in a range of values.

        :param header_name: the name of the header to match against.
        :param start: Match on values starting at and including this value.
        :param end: Match on values up to but not including this value.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valuesIsInRange", [header_name, start, end]))

    @jsii.member(jsii_name="valuesIsNotInRange") # type: ignore[misc]
    @builtins.classmethod
    def values_is_not_in_range(
        cls,
        header_name: builtins.str,
        start: jsii.Number,
        end: jsii.Number,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must not be in a range of values.

        :param header_name: the name of the header to match against.
        :param start: Match on values starting at and including this value.
        :param end: Match on values up to but not including this value.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valuesIsNotInRange", [header_name, start, end]))

    @jsii.member(jsii_name="valueStartsWith") # type: ignore[misc]
    @builtins.classmethod
    def value_starts_with(
        cls,
        header_name: builtins.str,
        prefix: builtins.str,
    ) -> "HeaderMatch":
        '''The value of the header with the given name in the request must start with the specified characters.

        :param header_name: the name of the header to match against.
        :param prefix: The prefix to test against.
        '''
        return typing.cast("HeaderMatch", jsii.sinvoke(cls, "valueStartsWith", [header_name, prefix]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "HeaderMatchConfig":
        '''Returns the header match configuration.

        :param scope: -
        '''
        ...


class _HeaderMatchProxy(HeaderMatch):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "HeaderMatchConfig":
        '''Returns the header match configuration.

        :param scope: -
        '''
        return typing.cast("HeaderMatchConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, HeaderMatch).__jsii_proxy_class__ = lambda : _HeaderMatchProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HeaderMatchConfig",
    jsii_struct_bases=[],
    name_mapping={"header_match": "headerMatch"},
)
class HeaderMatchConfig:
    def __init__(self, *, header_match: CfnRoute.HttpRouteHeaderProperty) -> None:
        '''Configuration for ``HeaderMatch``.

        :param header_match: Route CFN configuration for the route header match.
        '''
        if isinstance(header_match, dict):
            header_match = CfnRoute.HttpRouteHeaderProperty(**header_match)
        self._values: typing.Dict[str, typing.Any] = {
            "header_match": header_match,
        }

    @builtins.property
    def header_match(self) -> CfnRoute.HttpRouteHeaderProperty:
        '''Route CFN configuration for the route header match.'''
        result = self._values.get("header_match")
        assert result is not None, "Required property 'header_match' is missing"
        return typing.cast(CfnRoute.HttpRouteHeaderProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HeaderMatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HealthCheck(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.HealthCheck",
):
    '''Contains static factory methods for creating health checks for different protocols.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="grpc") # type: ignore[misc]
    @builtins.classmethod
    def grpc(
        cls,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[aws_cdk.core.Duration] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> "HealthCheck":
        '''Construct a GRPC health check.

        :param healthy_threshold: The number of consecutive successful health checks that must occur before declaring listener healthy. Default: 2
        :param interval: The time period between each health check execution. Default: Duration.seconds(5)
        :param timeout: The amount of time to wait when receiving a response from the health check. Default: Duration.seconds(2)
        :param unhealthy_threshold: The number of consecutive failed health checks that must occur before declaring a listener unhealthy. Default: - 2
        '''
        options = GrpcHealthCheckOptions(
            healthy_threshold=healthy_threshold,
            interval=interval,
            timeout=timeout,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast("HealthCheck", jsii.sinvoke(cls, "grpc", [options]))

    @jsii.member(jsii_name="http") # type: ignore[misc]
    @builtins.classmethod
    def http(
        cls,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[aws_cdk.core.Duration] = None,
        path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> "HealthCheck":
        '''Construct a HTTP health check.

        :param healthy_threshold: The number of consecutive successful health checks that must occur before declaring listener healthy. Default: 2
        :param interval: The time period between each health check execution. Default: Duration.seconds(5)
        :param path: The destination path for the health check request. Default: /
        :param timeout: The amount of time to wait when receiving a response from the health check. Default: Duration.seconds(2)
        :param unhealthy_threshold: The number of consecutive failed health checks that must occur before declaring a listener unhealthy. Default: - 2
        '''
        options = HttpHealthCheckOptions(
            healthy_threshold=healthy_threshold,
            interval=interval,
            path=path,
            timeout=timeout,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast("HealthCheck", jsii.sinvoke(cls, "http", [options]))

    @jsii.member(jsii_name="http2") # type: ignore[misc]
    @builtins.classmethod
    def http2(
        cls,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[aws_cdk.core.Duration] = None,
        path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> "HealthCheck":
        '''Construct a HTTP2 health check.

        :param healthy_threshold: The number of consecutive successful health checks that must occur before declaring listener healthy. Default: 2
        :param interval: The time period between each health check execution. Default: Duration.seconds(5)
        :param path: The destination path for the health check request. Default: /
        :param timeout: The amount of time to wait when receiving a response from the health check. Default: Duration.seconds(2)
        :param unhealthy_threshold: The number of consecutive failed health checks that must occur before declaring a listener unhealthy. Default: - 2
        '''
        options = HttpHealthCheckOptions(
            healthy_threshold=healthy_threshold,
            interval=interval,
            path=path,
            timeout=timeout,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast("HealthCheck", jsii.sinvoke(cls, "http2", [options]))

    @jsii.member(jsii_name="tcp") # type: ignore[misc]
    @builtins.classmethod
    def tcp(
        cls,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[aws_cdk.core.Duration] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> "HealthCheck":
        '''Construct a TCP health check.

        :param healthy_threshold: The number of consecutive successful health checks that must occur before declaring listener healthy. Default: 2
        :param interval: The time period between each health check execution. Default: Duration.seconds(5)
        :param timeout: The amount of time to wait when receiving a response from the health check. Default: Duration.seconds(2)
        :param unhealthy_threshold: The number of consecutive failed health checks that must occur before declaring a listener unhealthy. Default: - 2
        '''
        options = TcpHealthCheckOptions(
            healthy_threshold=healthy_threshold,
            interval=interval,
            timeout=timeout,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast("HealthCheck", jsii.sinvoke(cls, "tcp", [options]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(
        self,
        scope: aws_cdk.core.Construct,
        *,
        default_port: typing.Optional[jsii.Number] = None,
    ) -> "HealthCheckConfig":
        '''Called when the AccessLog type is initialized.

        Can be used to enforce
        mutual exclusivity with future properties

        :param scope: -
        :param default_port: Port for Health Check interface. Default: - no default port is provided
        '''
        ...


class _HealthCheckProxy(HealthCheck):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: aws_cdk.core.Construct,
        *,
        default_port: typing.Optional[jsii.Number] = None,
    ) -> "HealthCheckConfig":
        '''Called when the AccessLog type is initialized.

        Can be used to enforce
        mutual exclusivity with future properties

        :param scope: -
        :param default_port: Port for Health Check interface. Default: - no default port is provided
        '''
        options = HealthCheckBindOptions(default_port=default_port)

        return typing.cast("HealthCheckConfig", jsii.invoke(self, "bind", [scope, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, HealthCheck).__jsii_proxy_class__ = lambda : _HealthCheckProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HealthCheckBindOptions",
    jsii_struct_bases=[],
    name_mapping={"default_port": "defaultPort"},
)
class HealthCheckBindOptions:
    def __init__(self, *, default_port: typing.Optional[jsii.Number] = None) -> None:
        '''Options used for creating the Health Check object.

        :param default_port: Port for Health Check interface. Default: - no default port is provided
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if default_port is not None:
            self._values["default_port"] = default_port

    @builtins.property
    def default_port(self) -> typing.Optional[jsii.Number]:
        '''Port for Health Check interface.

        :default: - no default port is provided
        '''
        result = self._values.get("default_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthCheckBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HealthCheckConfig",
    jsii_struct_bases=[],
    name_mapping={
        "virtual_gateway_health_check": "virtualGatewayHealthCheck",
        "virtual_node_health_check": "virtualNodeHealthCheck",
    },
)
class HealthCheckConfig:
    def __init__(
        self,
        *,
        virtual_gateway_health_check: typing.Optional[CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty] = None,
        virtual_node_health_check: typing.Optional[CfnVirtualNode.HealthCheckProperty] = None,
    ) -> None:
        '''All Properties for Health Checks for mesh endpoints.

        :param virtual_gateway_health_check: VirtualGateway CFN configuration for Health Checks. Default: - no health checks
        :param virtual_node_health_check: VirtualNode CFN configuration for Health Checks. Default: - no health checks
        '''
        if isinstance(virtual_gateway_health_check, dict):
            virtual_gateway_health_check = CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty(**virtual_gateway_health_check)
        if isinstance(virtual_node_health_check, dict):
            virtual_node_health_check = CfnVirtualNode.HealthCheckProperty(**virtual_node_health_check)
        self._values: typing.Dict[str, typing.Any] = {}
        if virtual_gateway_health_check is not None:
            self._values["virtual_gateway_health_check"] = virtual_gateway_health_check
        if virtual_node_health_check is not None:
            self._values["virtual_node_health_check"] = virtual_node_health_check

    @builtins.property
    def virtual_gateway_health_check(
        self,
    ) -> typing.Optional[CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty]:
        '''VirtualGateway CFN configuration for Health Checks.

        :default: - no health checks
        '''
        result = self._values.get("virtual_gateway_health_check")
        return typing.cast(typing.Optional[CfnVirtualGateway.VirtualGatewayHealthCheckPolicyProperty], result)

    @builtins.property
    def virtual_node_health_check(
        self,
    ) -> typing.Optional[CfnVirtualNode.HealthCheckProperty]:
        '''VirtualNode CFN configuration for Health Checks.

        :default: - no health checks
        '''
        result = self._values.get("virtual_node_health_check")
        return typing.cast(typing.Optional[CfnVirtualNode.HealthCheckProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthCheckConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.Http2ConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"max_requests": "maxRequests"},
)
class Http2ConnectionPool:
    def __init__(self, *, max_requests: jsii.Number) -> None:
        '''Connection pool properties for HTTP2 listeners.

        :param max_requests: The maximum requests in the pool. Default: - none
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_requests": max_requests,
        }

    @builtins.property
    def max_requests(self) -> jsii.Number:
        '''The maximum requests in the pool.

        :default: - none
        '''
        result = self._values.get("max_requests")
        assert result is not None, "Required property 'max_requests' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Http2ConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.Http2GatewayListenerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "port": "port",
        "tls": "tls",
    },
)
class Http2GatewayListenerOptions:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional[Http2ConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        port: typing.Optional[jsii.Number] = None,
        tls: typing.Optional["ListenerTlsOptions"] = None,
    ) -> None:
        '''Represents the properties needed to define HTTP2 Listeners for a VirtualGateway.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param port: Port to listen for connections on. Default: - 8080
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        if isinstance(connection_pool, dict):
            connection_pool = Http2ConnectionPool(**connection_pool)
        if isinstance(tls, dict):
            tls = ListenerTlsOptions(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(self) -> typing.Optional[Http2ConnectionPool]:
        '''Connection pool for http listeners.

        :default: - None
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional[Http2ConnectionPool], result)

    @builtins.property
    def health_check(self) -> typing.Optional[HealthCheck]:
        '''The health check information for the listener.

        :default: - no healthcheck
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[HealthCheck], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to listen for connections on.

        :default: - 8080
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls(self) -> typing.Optional["ListenerTlsOptions"]:
        '''Represents the configuration for enabling TLS on a listener.

        :default: - none
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["ListenerTlsOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Http2GatewayListenerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.Http2VirtualNodeListenerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "outlier_detection": "outlierDetection",
        "port": "port",
        "timeout": "timeout",
        "tls": "tls",
    },
)
class Http2VirtualNodeListenerOptions:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional[Http2ConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        outlier_detection: typing.Optional["OutlierDetection"] = None,
        port: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional["HttpTimeout"] = None,
        tls: typing.Optional["ListenerTlsOptions"] = None,
    ) -> None:
        '''Represent the HTTP2 Node Listener prorperty.

        :param connection_pool: Connection pool for http2 listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param outlier_detection: Represents the configuration for enabling outlier detection. Default: - none
        :param port: Port to listen for connections on. Default: - 8080
        :param timeout: Timeout for HTTP protocol. Default: - None
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        if isinstance(connection_pool, dict):
            connection_pool = Http2ConnectionPool(**connection_pool)
        if isinstance(outlier_detection, dict):
            outlier_detection = OutlierDetection(**outlier_detection)
        if isinstance(timeout, dict):
            timeout = HttpTimeout(**timeout)
        if isinstance(tls, dict):
            tls = ListenerTlsOptions(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port is not None:
            self._values["port"] = port
        if timeout is not None:
            self._values["timeout"] = timeout
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(self) -> typing.Optional[Http2ConnectionPool]:
        '''Connection pool for http2 listeners.

        :default: - None
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional[Http2ConnectionPool], result)

    @builtins.property
    def health_check(self) -> typing.Optional[HealthCheck]:
        '''The health check information for the listener.

        :default: - no healthcheck
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[HealthCheck], result)

    @builtins.property
    def outlier_detection(self) -> typing.Optional["OutlierDetection"]:
        '''Represents the configuration for enabling outlier detection.

        :default: - none
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["OutlierDetection"], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to listen for connections on.

        :default: - 8080
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout(self) -> typing.Optional["HttpTimeout"]:
        '''Timeout for HTTP protocol.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["HttpTimeout"], result)

    @builtins.property
    def tls(self) -> typing.Optional["ListenerTlsOptions"]:
        '''Represents the configuration for enabling TLS on a listener.

        :default: - none
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["ListenerTlsOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Http2VirtualNodeListenerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpConnectionPool",
    jsii_struct_bases=[],
    name_mapping={
        "max_connections": "maxConnections",
        "max_pending_requests": "maxPendingRequests",
    },
)
class HttpConnectionPool:
    def __init__(
        self,
        *,
        max_connections: jsii.Number,
        max_pending_requests: jsii.Number,
    ) -> None:
        '''Connection pool properties for HTTP listeners.

        :param max_connections: The maximum connections in the pool. Default: - none
        :param max_pending_requests: The maximum pending requests in the pool. Default: - none
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_connections": max_connections,
            "max_pending_requests": max_pending_requests,
        }

    @builtins.property
    def max_connections(self) -> jsii.Number:
        '''The maximum connections in the pool.

        :default: - none
        '''
        result = self._values.get("max_connections")
        assert result is not None, "Required property 'max_connections' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_pending_requests(self) -> jsii.Number:
        '''The maximum pending requests in the pool.

        :default: - none
        '''
        result = self._values.get("max_pending_requests")
        assert result is not None, "Required property 'max_pending_requests' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpGatewayListenerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "port": "port",
        "tls": "tls",
    },
)
class HttpGatewayListenerOptions:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional[HttpConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        port: typing.Optional[jsii.Number] = None,
        tls: typing.Optional["ListenerTlsOptions"] = None,
    ) -> None:
        '''Represents the properties needed to define HTTP Listeners for a VirtualGateway.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param port: Port to listen for connections on. Default: - 8080
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        if isinstance(connection_pool, dict):
            connection_pool = HttpConnectionPool(**connection_pool)
        if isinstance(tls, dict):
            tls = ListenerTlsOptions(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(self) -> typing.Optional[HttpConnectionPool]:
        '''Connection pool for http listeners.

        :default: - None
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional[HttpConnectionPool], result)

    @builtins.property
    def health_check(self) -> typing.Optional[HealthCheck]:
        '''The health check information for the listener.

        :default: - no healthcheck
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[HealthCheck], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to listen for connections on.

        :default: - 8080
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls(self) -> typing.Optional["ListenerTlsOptions"]:
        '''Represents the configuration for enabling TLS on a listener.

        :default: - none
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["ListenerTlsOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpGatewayListenerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpGatewayRouteMatch",
    jsii_struct_bases=[],
    name_mapping={
        "headers": "headers",
        "hostname": "hostname",
        "method": "method",
        "path": "path",
        "query_parameters": "queryParameters",
        "rewrite_request_hostname": "rewriteRequestHostname",
    },
)
class HttpGatewayRouteMatch:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Sequence[HeaderMatch]] = None,
        hostname: typing.Optional[GatewayRouteHostnameMatch] = None,
        method: typing.Optional["HttpRouteMethod"] = None,
        path: typing.Optional["HttpGatewayRoutePathMatch"] = None,
        query_parameters: typing.Optional[typing.Sequence["QueryParameterMatch"]] = None,
        rewrite_request_hostname: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''The criterion for determining a request match for this GatewayRoute.

        :param headers: Specifies the client request headers to match on. All specified headers must match for the gateway route to match. Default: - do not match on headers
        :param hostname: The gateway route host name to be matched on. Default: - do not match on host name
        :param method: The method to match on. Default: - do not match on method
        :param path: Specify how to match requests based on the 'path' part of their URL. Default: - matches requests with any path
        :param query_parameters: The query parameters to match on. All specified query parameters must match for the route to match. Default: - do not match on query parameters
        :param rewrite_request_hostname: When ``true``, rewrites the original request received at the Virtual Gateway to the destination Virtual Service name. When ``false``, retains the original hostname from the request. Default: true
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if headers is not None:
            self._values["headers"] = headers
        if hostname is not None:
            self._values["hostname"] = hostname
        if method is not None:
            self._values["method"] = method
        if path is not None:
            self._values["path"] = path
        if query_parameters is not None:
            self._values["query_parameters"] = query_parameters
        if rewrite_request_hostname is not None:
            self._values["rewrite_request_hostname"] = rewrite_request_hostname

    @builtins.property
    def headers(self) -> typing.Optional[typing.List[HeaderMatch]]:
        '''Specifies the client request headers to match on.

        All specified headers
        must match for the gateway route to match.

        :default: - do not match on headers
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.List[HeaderMatch]], result)

    @builtins.property
    def hostname(self) -> typing.Optional[GatewayRouteHostnameMatch]:
        '''The gateway route host name to be matched on.

        :default: - do not match on host name
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[GatewayRouteHostnameMatch], result)

    @builtins.property
    def method(self) -> typing.Optional["HttpRouteMethod"]:
        '''The method to match on.

        :default: - do not match on method
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["HttpRouteMethod"], result)

    @builtins.property
    def path(self) -> typing.Optional["HttpGatewayRoutePathMatch"]:
        '''Specify how to match requests based on the 'path' part of their URL.

        :default: - matches requests with any path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional["HttpGatewayRoutePathMatch"], result)

    @builtins.property
    def query_parameters(self) -> typing.Optional[typing.List["QueryParameterMatch"]]:
        '''The query parameters to match on.

        All specified query parameters must match for the route to match.

        :default: - do not match on query parameters
        '''
        result = self._values.get("query_parameters")
        return typing.cast(typing.Optional[typing.List["QueryParameterMatch"]], result)

    @builtins.property
    def rewrite_request_hostname(self) -> typing.Optional[builtins.bool]:
        '''When ``true``, rewrites the original request received at the Virtual Gateway to the destination Virtual Service name.

        When ``false``, retains the original hostname from the request.

        :default: true
        '''
        result = self._values.get("rewrite_request_hostname")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpGatewayRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HttpGatewayRoutePathMatch(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.HttpGatewayRoutePathMatch",
):
    '''Defines HTTP gateway route matching based on the URL path of the request.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="exactly") # type: ignore[misc]
    @builtins.classmethod
    def exactly(
        cls,
        path: builtins.str,
        rewrite_to: typing.Optional[builtins.str] = None,
    ) -> "HttpGatewayRoutePathMatch":
        '''The value of the path must match the specified value exactly.

        The provided ``path`` must start with the '/' character.

        :param path: the exact path to match on.
        :param rewrite_to: the value to substitute for the matched part of the path of the gateway request URL As a default, retains original request's URL path.
        '''
        return typing.cast("HttpGatewayRoutePathMatch", jsii.sinvoke(cls, "exactly", [path, rewrite_to]))

    @jsii.member(jsii_name="regex") # type: ignore[misc]
    @builtins.classmethod
    def regex(
        cls,
        regex: builtins.str,
        rewrite_to: typing.Optional[builtins.str] = None,
    ) -> "HttpGatewayRoutePathMatch":
        '''The value of the path must match the specified regex.

        :param regex: the regex used to match the path.
        :param rewrite_to: the value to substitute for the matched part of the path of the gateway request URL As a default, retains original request's URL path.
        '''
        return typing.cast("HttpGatewayRoutePathMatch", jsii.sinvoke(cls, "regex", [regex, rewrite_to]))

    @jsii.member(jsii_name="startsWith") # type: ignore[misc]
    @builtins.classmethod
    def starts_with(
        cls,
        prefix: builtins.str,
        rewrite_to: typing.Optional[builtins.str] = None,
    ) -> "HttpGatewayRoutePathMatch":
        '''The value of the path must match the specified prefix.

        :param prefix: the value to use to match the beginning of the path part of the URL of the request. It must start with the '/' character. When ``rewriteTo`` is provided, it must also end with the '/' character. If provided as "/", matches all requests. For example, if your virtual service name is "my-service.local" and you want the route to match requests to "my-service.local/metrics", your prefix should be "/metrics".
        :param rewrite_to: Specify either disabling automatic rewrite or rewriting to specified prefix path. To disable automatic rewrite, provide ``''``. As a default, request's URL path is automatically rewritten to '/'.
        '''
        return typing.cast("HttpGatewayRoutePathMatch", jsii.sinvoke(cls, "startsWith", [prefix, rewrite_to]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "HttpGatewayRoutePathMatchConfig":
        '''Returns the gateway route path match configuration.

        :param scope: -
        '''
        ...


class _HttpGatewayRoutePathMatchProxy(HttpGatewayRoutePathMatch):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "HttpGatewayRoutePathMatchConfig":
        '''Returns the gateway route path match configuration.

        :param scope: -
        '''
        return typing.cast("HttpGatewayRoutePathMatchConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, HttpGatewayRoutePathMatch).__jsii_proxy_class__ = lambda : _HttpGatewayRoutePathMatchProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpGatewayRoutePathMatchConfig",
    jsii_struct_bases=[],
    name_mapping={
        "prefix_path_match": "prefixPathMatch",
        "prefix_path_rewrite": "prefixPathRewrite",
        "whole_path_match": "wholePathMatch",
        "whole_path_rewrite": "wholePathRewrite",
    },
)
class HttpGatewayRoutePathMatchConfig:
    def __init__(
        self,
        *,
        prefix_path_match: typing.Optional[builtins.str] = None,
        prefix_path_rewrite: typing.Optional[CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty] = None,
        whole_path_match: typing.Optional[CfnGatewayRoute.HttpPathMatchProperty] = None,
        whole_path_rewrite: typing.Optional[CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty] = None,
    ) -> None:
        '''The type returned from the ``bind()`` method in {@link HttpGatewayRoutePathMatch}.

        :param prefix_path_match: Gateway route configuration for matching on the prefix of the URL path of the request. Default: - no matching will be performed on the prefix of the URL path
        :param prefix_path_rewrite: Gateway route configuration for rewriting the prefix of the URL path of the request. Default: - rewrites the request's URL path to '/'
        :param whole_path_match: Gateway route configuration for matching on the complete URL path of the request. Default: - no matching will be performed on the complete URL path
        :param whole_path_rewrite: Gateway route configuration for rewriting the complete URL path of the request.. Default: - no rewrite will be performed on the request's complete URL path
        '''
        if isinstance(prefix_path_rewrite, dict):
            prefix_path_rewrite = CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty(**prefix_path_rewrite)
        if isinstance(whole_path_match, dict):
            whole_path_match = CfnGatewayRoute.HttpPathMatchProperty(**whole_path_match)
        if isinstance(whole_path_rewrite, dict):
            whole_path_rewrite = CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty(**whole_path_rewrite)
        self._values: typing.Dict[str, typing.Any] = {}
        if prefix_path_match is not None:
            self._values["prefix_path_match"] = prefix_path_match
        if prefix_path_rewrite is not None:
            self._values["prefix_path_rewrite"] = prefix_path_rewrite
        if whole_path_match is not None:
            self._values["whole_path_match"] = whole_path_match
        if whole_path_rewrite is not None:
            self._values["whole_path_rewrite"] = whole_path_rewrite

    @builtins.property
    def prefix_path_match(self) -> typing.Optional[builtins.str]:
        '''Gateway route configuration for matching on the prefix of the URL path of the request.

        :default: - no matching will be performed on the prefix of the URL path
        '''
        result = self._values.get("prefix_path_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_path_rewrite(
        self,
    ) -> typing.Optional[CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty]:
        '''Gateway route configuration for rewriting the prefix of the URL path of the request.

        :default: - rewrites the request's URL path to '/'
        '''
        result = self._values.get("prefix_path_rewrite")
        return typing.cast(typing.Optional[CfnGatewayRoute.HttpGatewayRoutePrefixRewriteProperty], result)

    @builtins.property
    def whole_path_match(
        self,
    ) -> typing.Optional[CfnGatewayRoute.HttpPathMatchProperty]:
        '''Gateway route configuration for matching on the complete URL path of the request.

        :default: - no matching will be performed on the complete URL path
        '''
        result = self._values.get("whole_path_match")
        return typing.cast(typing.Optional[CfnGatewayRoute.HttpPathMatchProperty], result)

    @builtins.property
    def whole_path_rewrite(
        self,
    ) -> typing.Optional[CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty]:
        '''Gateway route configuration for rewriting the complete URL path of the request..

        :default: - no rewrite will be performed on the request's complete URL path
        '''
        result = self._values.get("whole_path_rewrite")
        return typing.cast(typing.Optional[CfnGatewayRoute.HttpGatewayRoutePathRewriteProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpGatewayRoutePathMatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpGatewayRouteSpecOptions",
    jsii_struct_bases=[],
    name_mapping={"route_target": "routeTarget", "match": "match"},
)
class HttpGatewayRouteSpecOptions:
    def __init__(
        self,
        *,
        route_target: "IVirtualService",
        match: typing.Optional[HttpGatewayRouteMatch] = None,
    ) -> None:
        '''Properties specific for HTTP Based GatewayRoutes.

        :param route_target: The VirtualService this GatewayRoute directs traffic to.
        :param match: The criterion for determining a request match for this GatewayRoute. When path match is defined, this may optionally determine the path rewrite configuration. Default: - matches any path and automatically rewrites the path to '/'
        '''
        if isinstance(match, dict):
            match = HttpGatewayRouteMatch(**match)
        self._values: typing.Dict[str, typing.Any] = {
            "route_target": route_target,
        }
        if match is not None:
            self._values["match"] = match

    @builtins.property
    def route_target(self) -> "IVirtualService":
        '''The VirtualService this GatewayRoute directs traffic to.'''
        result = self._values.get("route_target")
        assert result is not None, "Required property 'route_target' is missing"
        return typing.cast("IVirtualService", result)

    @builtins.property
    def match(self) -> typing.Optional[HttpGatewayRouteMatch]:
        '''The criterion for determining a request match for this GatewayRoute.

        When path match is defined, this may optionally determine the path rewrite configuration.

        :default: - matches any path and automatically rewrites the path to '/'
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional[HttpGatewayRouteMatch], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpGatewayRouteSpecOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpHealthCheckOptions",
    jsii_struct_bases=[],
    name_mapping={
        "healthy_threshold": "healthyThreshold",
        "interval": "interval",
        "path": "path",
        "timeout": "timeout",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class HttpHealthCheckOptions:
    def __init__(
        self,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[aws_cdk.core.Duration] = None,
        path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties used to define HTTP Based healthchecks.

        :param healthy_threshold: The number of consecutive successful health checks that must occur before declaring listener healthy. Default: 2
        :param interval: The time period between each health check execution. Default: Duration.seconds(5)
        :param path: The destination path for the health check request. Default: /
        :param timeout: The amount of time to wait when receiving a response from the health check. Default: Duration.seconds(2)
        :param unhealthy_threshold: The number of consecutive failed health checks that must occur before declaring a listener unhealthy. Default: - 2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if interval is not None:
            self._values["interval"] = interval
        if path is not None:
            self._values["path"] = path
        if timeout is not None:
            self._values["timeout"] = timeout
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive successful health checks that must occur before declaring listener healthy.

        :default: 2
        '''
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The time period between each health check execution.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The destination path for the health check request.

        :default: /
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The amount of time to wait when receiving a response from the health check.

        :default: Duration.seconds(2)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive failed health checks that must occur before declaring a listener unhealthy.

        :default: - 2
        '''
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpHealthCheckOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appmesh.HttpRetryEvent")
class HttpRetryEvent(enum.Enum):
    '''HTTP events on which to retry.'''

    SERVER_ERROR = "SERVER_ERROR"
    '''HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511.'''
    GATEWAY_ERROR = "GATEWAY_ERROR"
    '''HTTP status codes 502, 503, and 504.'''
    CLIENT_ERROR = "CLIENT_ERROR"
    '''HTTP status code 409.'''
    STREAM_ERROR = "STREAM_ERROR"
    '''Retry on refused stream.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "retry_attempts": "retryAttempts",
        "retry_timeout": "retryTimeout",
        "http_retry_events": "httpRetryEvents",
        "tcp_retry_events": "tcpRetryEvents",
    },
)
class HttpRetryPolicy:
    def __init__(
        self,
        *,
        retry_attempts: jsii.Number,
        retry_timeout: aws_cdk.core.Duration,
        http_retry_events: typing.Optional[typing.Sequence[HttpRetryEvent]] = None,
        tcp_retry_events: typing.Optional[typing.Sequence["TcpRetryEvent"]] = None,
    ) -> None:
        '''HTTP retry policy.

        :param retry_attempts: The maximum number of retry attempts.
        :param retry_timeout: The timeout for each retry attempt.
        :param http_retry_events: Specify HTTP events on which to retry. You must specify at least one value for at least one types of retry events. Default: - no retries for http events
        :param tcp_retry_events: TCP events on which to retry. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable. You must specify at least one value for at least one types of retry events. Default: - no retries for tcp events
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "retry_attempts": retry_attempts,
            "retry_timeout": retry_timeout,
        }
        if http_retry_events is not None:
            self._values["http_retry_events"] = http_retry_events
        if tcp_retry_events is not None:
            self._values["tcp_retry_events"] = tcp_retry_events

    @builtins.property
    def retry_attempts(self) -> jsii.Number:
        '''The maximum number of retry attempts.'''
        result = self._values.get("retry_attempts")
        assert result is not None, "Required property 'retry_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def retry_timeout(self) -> aws_cdk.core.Duration:
        '''The timeout for each retry attempt.'''
        result = self._values.get("retry_timeout")
        assert result is not None, "Required property 'retry_timeout' is missing"
        return typing.cast(aws_cdk.core.Duration, result)

    @builtins.property
    def http_retry_events(self) -> typing.Optional[typing.List[HttpRetryEvent]]:
        '''Specify HTTP events on which to retry.

        You must specify at least one value
        for at least one types of retry events.

        :default: - no retries for http events
        '''
        result = self._values.get("http_retry_events")
        return typing.cast(typing.Optional[typing.List[HttpRetryEvent]], result)

    @builtins.property
    def tcp_retry_events(self) -> typing.Optional[typing.List["TcpRetryEvent"]]:
        '''TCP events on which to retry.

        The event occurs before any processing of a
        request has started and is encountered when the upstream is temporarily or
        permanently unavailable. You must specify at least one value for at least
        one types of retry events.

        :default: - no retries for tcp events
        '''
        result = self._values.get("tcp_retry_events")
        return typing.cast(typing.Optional[typing.List["TcpRetryEvent"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpRouteMatch",
    jsii_struct_bases=[],
    name_mapping={
        "headers": "headers",
        "method": "method",
        "path": "path",
        "protocol": "protocol",
        "query_parameters": "queryParameters",
    },
)
class HttpRouteMatch:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Sequence[HeaderMatch]] = None,
        method: typing.Optional["HttpRouteMethod"] = None,
        path: typing.Optional["HttpRoutePathMatch"] = None,
        protocol: typing.Optional["HttpRouteProtocol"] = None,
        query_parameters: typing.Optional[typing.Sequence["QueryParameterMatch"]] = None,
    ) -> None:
        '''The criterion for determining a request match for this Route.

        :param headers: Specifies the client request headers to match on. All specified headers must match for the route to match. Default: - do not match on headers
        :param method: The HTTP client request method to match on. Default: - do not match on request method
        :param path: Specifies how is the request matched based on the path part of its URL. Default: - matches requests with all paths
        :param protocol: The client request protocol to match on. Applicable only for HTTP2 routes. Default: - do not match on HTTP2 request protocol
        :param query_parameters: The query parameters to match on. All specified query parameters must match for the route to match. Default: - do not match on query parameters
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if headers is not None:
            self._values["headers"] = headers
        if method is not None:
            self._values["method"] = method
        if path is not None:
            self._values["path"] = path
        if protocol is not None:
            self._values["protocol"] = protocol
        if query_parameters is not None:
            self._values["query_parameters"] = query_parameters

    @builtins.property
    def headers(self) -> typing.Optional[typing.List[HeaderMatch]]:
        '''Specifies the client request headers to match on.

        All specified headers
        must match for the route to match.

        :default: - do not match on headers
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.List[HeaderMatch]], result)

    @builtins.property
    def method(self) -> typing.Optional["HttpRouteMethod"]:
        '''The HTTP client request method to match on.

        :default: - do not match on request method
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["HttpRouteMethod"], result)

    @builtins.property
    def path(self) -> typing.Optional["HttpRoutePathMatch"]:
        '''Specifies how is the request matched based on the path part of its URL.

        :default: - matches requests with all paths
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional["HttpRoutePathMatch"], result)

    @builtins.property
    def protocol(self) -> typing.Optional["HttpRouteProtocol"]:
        '''The client request protocol to match on.

        Applicable only for HTTP2 routes.

        :default: - do not match on HTTP2 request protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional["HttpRouteProtocol"], result)

    @builtins.property
    def query_parameters(self) -> typing.Optional[typing.List["QueryParameterMatch"]]:
        '''The query parameters to match on.

        All specified query parameters must match for the route to match.

        :default: - do not match on query parameters
        '''
        result = self._values.get("query_parameters")
        return typing.cast(typing.Optional[typing.List["QueryParameterMatch"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appmesh.HttpRouteMethod")
class HttpRouteMethod(enum.Enum):
    '''Supported values for matching routes based on the HTTP request method.'''

    GET = "GET"
    '''GET request.'''
    HEAD = "HEAD"
    '''HEAD request.'''
    POST = "POST"
    '''POST request.'''
    PUT = "PUT"
    '''PUT request.'''
    DELETE = "DELETE"
    '''DELETE request.'''
    CONNECT = "CONNECT"
    '''CONNECT request.'''
    OPTIONS = "OPTIONS"
    '''OPTIONS request.'''
    TRACE = "TRACE"
    '''TRACE request.'''
    PATCH = "PATCH"
    '''PATCH request.'''


class HttpRoutePathMatch(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.HttpRoutePathMatch",
):
    '''Defines HTTP route matching based on the URL path of the request.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="exactly") # type: ignore[misc]
    @builtins.classmethod
    def exactly(cls, path: builtins.str) -> "HttpRoutePathMatch":
        '''The value of the path must match the specified value exactly.

        The provided ``path`` must start with the '/' character.

        :param path: the exact path to match on.
        '''
        return typing.cast("HttpRoutePathMatch", jsii.sinvoke(cls, "exactly", [path]))

    @jsii.member(jsii_name="regex") # type: ignore[misc]
    @builtins.classmethod
    def regex(cls, regex: builtins.str) -> "HttpRoutePathMatch":
        '''The value of the path must match the specified regex.

        :param regex: the regex used to match the path.
        '''
        return typing.cast("HttpRoutePathMatch", jsii.sinvoke(cls, "regex", [regex]))

    @jsii.member(jsii_name="startsWith") # type: ignore[misc]
    @builtins.classmethod
    def starts_with(cls, prefix: builtins.str) -> "HttpRoutePathMatch":
        '''The value of the path must match the specified prefix.

        :param prefix: the value to use to match the beginning of the path part of the URL of the request. It must start with the '/' character. If provided as "/", matches all requests. For example, if your virtual service name is "my-service.local" and you want the route to match requests to "my-service.local/metrics", your prefix should be "/metrics".
        '''
        return typing.cast("HttpRoutePathMatch", jsii.sinvoke(cls, "startsWith", [prefix]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "HttpRoutePathMatchConfig":
        '''Returns the route path match configuration.

        :param scope: -
        '''
        ...


class _HttpRoutePathMatchProxy(HttpRoutePathMatch):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "HttpRoutePathMatchConfig":
        '''Returns the route path match configuration.

        :param scope: -
        '''
        return typing.cast("HttpRoutePathMatchConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, HttpRoutePathMatch).__jsii_proxy_class__ = lambda : _HttpRoutePathMatchProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpRoutePathMatchConfig",
    jsii_struct_bases=[],
    name_mapping={
        "prefix_path_match": "prefixPathMatch",
        "whole_path_match": "wholePathMatch",
    },
)
class HttpRoutePathMatchConfig:
    def __init__(
        self,
        *,
        prefix_path_match: typing.Optional[builtins.str] = None,
        whole_path_match: typing.Optional[CfnRoute.HttpPathMatchProperty] = None,
    ) -> None:
        '''The type returned from the ``bind()`` method in {@link HttpRoutePathMatch}.

        :param prefix_path_match: Route configuration for matching on the prefix of the URL path of the request. Default: - no matching will be performed on the prefix of the URL path
        :param whole_path_match: Route configuration for matching on the complete URL path of the request. Default: - no matching will be performed on the complete URL path
        '''
        if isinstance(whole_path_match, dict):
            whole_path_match = CfnRoute.HttpPathMatchProperty(**whole_path_match)
        self._values: typing.Dict[str, typing.Any] = {}
        if prefix_path_match is not None:
            self._values["prefix_path_match"] = prefix_path_match
        if whole_path_match is not None:
            self._values["whole_path_match"] = whole_path_match

    @builtins.property
    def prefix_path_match(self) -> typing.Optional[builtins.str]:
        '''Route configuration for matching on the prefix of the URL path of the request.

        :default: - no matching will be performed on the prefix of the URL path
        '''
        result = self._values.get("prefix_path_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def whole_path_match(self) -> typing.Optional[CfnRoute.HttpPathMatchProperty]:
        '''Route configuration for matching on the complete URL path of the request.

        :default: - no matching will be performed on the complete URL path
        '''
        result = self._values.get("whole_path_match")
        return typing.cast(typing.Optional[CfnRoute.HttpPathMatchProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpRoutePathMatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appmesh.HttpRouteProtocol")
class HttpRouteProtocol(enum.Enum):
    '''Supported :scheme options for HTTP2.'''

    HTTP = "HTTP"
    '''Match HTTP requests.'''
    HTTPS = "HTTPS"
    '''Match HTTPS requests.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpTimeout",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class HttpTimeout:
    def __init__(
        self,
        *,
        idle: typing.Optional[aws_cdk.core.Duration] = None,
        per_request: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        '''Represents timeouts for HTTP protocols.

        :param idle: Represents an idle timeout. The amount of time that a connection may be idle. Default: - none
        :param per_request: Represents per request timeout. Default: - 15 s
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''Represents an idle timeout.

        The amount of time that a connection may be idle.

        :default: - none
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def per_request(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''Represents per request timeout.

        :default: - 15 s
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpVirtualNodeListenerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "outlier_detection": "outlierDetection",
        "port": "port",
        "timeout": "timeout",
        "tls": "tls",
    },
)
class HttpVirtualNodeListenerOptions:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional[HttpConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        outlier_detection: typing.Optional["OutlierDetection"] = None,
        port: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[HttpTimeout] = None,
        tls: typing.Optional["ListenerTlsOptions"] = None,
    ) -> None:
        '''Represent the HTTP Node Listener prorperty.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param outlier_detection: Represents the configuration for enabling outlier detection. Default: - none
        :param port: Port to listen for connections on. Default: - 8080
        :param timeout: Timeout for HTTP protocol. Default: - None
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        if isinstance(connection_pool, dict):
            connection_pool = HttpConnectionPool(**connection_pool)
        if isinstance(outlier_detection, dict):
            outlier_detection = OutlierDetection(**outlier_detection)
        if isinstance(timeout, dict):
            timeout = HttpTimeout(**timeout)
        if isinstance(tls, dict):
            tls = ListenerTlsOptions(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port is not None:
            self._values["port"] = port
        if timeout is not None:
            self._values["timeout"] = timeout
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(self) -> typing.Optional[HttpConnectionPool]:
        '''Connection pool for http listeners.

        :default: - None
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional[HttpConnectionPool], result)

    @builtins.property
    def health_check(self) -> typing.Optional[HealthCheck]:
        '''The health check information for the listener.

        :default: - no healthcheck
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[HealthCheck], result)

    @builtins.property
    def outlier_detection(self) -> typing.Optional["OutlierDetection"]:
        '''Represents the configuration for enabling outlier detection.

        :default: - none
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["OutlierDetection"], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to listen for connections on.

        :default: - 8080
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout(self) -> typing.Optional[HttpTimeout]:
        '''Timeout for HTTP protocol.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[HttpTimeout], result)

    @builtins.property
    def tls(self) -> typing.Optional["ListenerTlsOptions"]:
        '''Represents the configuration for enabling TLS on a listener.

        :default: - none
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["ListenerTlsOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpVirtualNodeListenerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-appmesh.IGatewayRoute")
class IGatewayRoute(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''Interface for which all GatewayRoute based classes MUST implement.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayRouteArn")
    def gateway_route_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the GatewayRoute.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayRouteName")
    def gateway_route_name(self) -> builtins.str:
        '''The name of the GatewayRoute.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGateway")
    def virtual_gateway(self) -> "IVirtualGateway":
        '''The VirtualGateway the GatewayRoute belongs to.'''
        ...


class _IGatewayRouteProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''Interface for which all GatewayRoute based classes MUST implement.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appmesh.IGatewayRoute"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayRouteArn")
    def gateway_route_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the GatewayRoute.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "gatewayRouteArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayRouteName")
    def gateway_route_name(self) -> builtins.str:
        '''The name of the GatewayRoute.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "gatewayRouteName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGateway")
    def virtual_gateway(self) -> "IVirtualGateway":
        '''The VirtualGateway the GatewayRoute belongs to.'''
        return typing.cast("IVirtualGateway", jsii.get(self, "virtualGateway"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGatewayRoute).__jsii_proxy_class__ = lambda : _IGatewayRouteProxy


@jsii.interface(jsii_type="@aws-cdk/aws-appmesh.IMesh")
class IMesh(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''Interface which all Mesh based classes MUST implement.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshArn")
    def mesh_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AppMesh mesh.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        '''The name of the AppMesh mesh.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addVirtualGateway")
    def add_virtual_gateway(
        self,
        id: builtins.str,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        listeners: typing.Optional[typing.Sequence["VirtualGatewayListener"]] = None,
        virtual_gateway_name: typing.Optional[builtins.str] = None,
    ) -> "VirtualGateway":
        '''Creates a new VirtualGateway in this Mesh.

        Note that the Gateway is created in the same Stack that this Mesh belongs to,
        which might be different than the current stack.

        :param id: -
        :param access_log: Access Logging Configuration for the VirtualGateway. Default: - no access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param listeners: Listeners for the VirtualGateway. Only one is supported. Default: - Single HTTP listener on port 8080
        :param virtual_gateway_name: Name of the VirtualGateway. Default: - A name is automatically determined
        '''
        ...

    @jsii.member(jsii_name="addVirtualNode")
    def add_virtual_node(
        self,
        id: builtins.str,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        backends: typing.Optional[typing.Sequence[Backend]] = None,
        listeners: typing.Optional[typing.Sequence["VirtualNodeListener"]] = None,
        service_discovery: typing.Optional["ServiceDiscovery"] = None,
        virtual_node_name: typing.Optional[builtins.str] = None,
    ) -> "VirtualNode":
        '''Creates a new VirtualNode in this Mesh.

        Note that the Node is created in the same Stack that this Mesh belongs to,
        which might be different than the current stack.

        :param id: -
        :param access_log: Access Logging Configuration for the virtual node. Default: - No access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param backends: Virtual Services that this is node expected to send outbound traffic to. Default: - No backends
        :param listeners: Initial listener for the virtual node. Default: - No listeners
        :param service_discovery: Defines how upstream clients will discover this VirtualNode. Default: - No Service Discovery
        :param virtual_node_name: The name of the VirtualNode. Default: - A name is automatically determined
        '''
        ...

    @jsii.member(jsii_name="addVirtualRouter")
    def add_virtual_router(
        self,
        id: builtins.str,
        *,
        listeners: typing.Optional[typing.Sequence["VirtualRouterListener"]] = None,
        virtual_router_name: typing.Optional[builtins.str] = None,
    ) -> "VirtualRouter":
        '''Creates a new VirtualRouter in this Mesh.

        Note that the Router is created in the same Stack that this Mesh belongs to,
        which might be different than the current stack.

        :param id: -
        :param listeners: Listener specification for the VirtualRouter. Default: - A listener on HTTP port 8080
        :param virtual_router_name: The name of the VirtualRouter. Default: - A name is automatically determined
        '''
        ...


class _IMeshProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''Interface which all Mesh based classes MUST implement.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appmesh.IMesh"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshArn")
    def mesh_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AppMesh mesh.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "meshArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        '''The name of the AppMesh mesh.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @jsii.member(jsii_name="addVirtualGateway")
    def add_virtual_gateway(
        self,
        id: builtins.str,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        listeners: typing.Optional[typing.Sequence["VirtualGatewayListener"]] = None,
        virtual_gateway_name: typing.Optional[builtins.str] = None,
    ) -> "VirtualGateway":
        '''Creates a new VirtualGateway in this Mesh.

        Note that the Gateway is created in the same Stack that this Mesh belongs to,
        which might be different than the current stack.

        :param id: -
        :param access_log: Access Logging Configuration for the VirtualGateway. Default: - no access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param listeners: Listeners for the VirtualGateway. Only one is supported. Default: - Single HTTP listener on port 8080
        :param virtual_gateway_name: Name of the VirtualGateway. Default: - A name is automatically determined
        '''
        props = VirtualGatewayBaseProps(
            access_log=access_log,
            backend_defaults=backend_defaults,
            listeners=listeners,
            virtual_gateway_name=virtual_gateway_name,
        )

        return typing.cast("VirtualGateway", jsii.invoke(self, "addVirtualGateway", [id, props]))

    @jsii.member(jsii_name="addVirtualNode")
    def add_virtual_node(
        self,
        id: builtins.str,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        backends: typing.Optional[typing.Sequence[Backend]] = None,
        listeners: typing.Optional[typing.Sequence["VirtualNodeListener"]] = None,
        service_discovery: typing.Optional["ServiceDiscovery"] = None,
        virtual_node_name: typing.Optional[builtins.str] = None,
    ) -> "VirtualNode":
        '''Creates a new VirtualNode in this Mesh.

        Note that the Node is created in the same Stack that this Mesh belongs to,
        which might be different than the current stack.

        :param id: -
        :param access_log: Access Logging Configuration for the virtual node. Default: - No access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param backends: Virtual Services that this is node expected to send outbound traffic to. Default: - No backends
        :param listeners: Initial listener for the virtual node. Default: - No listeners
        :param service_discovery: Defines how upstream clients will discover this VirtualNode. Default: - No Service Discovery
        :param virtual_node_name: The name of the VirtualNode. Default: - A name is automatically determined
        '''
        props = VirtualNodeBaseProps(
            access_log=access_log,
            backend_defaults=backend_defaults,
            backends=backends,
            listeners=listeners,
            service_discovery=service_discovery,
            virtual_node_name=virtual_node_name,
        )

        return typing.cast("VirtualNode", jsii.invoke(self, "addVirtualNode", [id, props]))

    @jsii.member(jsii_name="addVirtualRouter")
    def add_virtual_router(
        self,
        id: builtins.str,
        *,
        listeners: typing.Optional[typing.Sequence["VirtualRouterListener"]] = None,
        virtual_router_name: typing.Optional[builtins.str] = None,
    ) -> "VirtualRouter":
        '''Creates a new VirtualRouter in this Mesh.

        Note that the Router is created in the same Stack that this Mesh belongs to,
        which might be different than the current stack.

        :param id: -
        :param listeners: Listener specification for the VirtualRouter. Default: - A listener on HTTP port 8080
        :param virtual_router_name: The name of the VirtualRouter. Default: - A name is automatically determined
        '''
        props = VirtualRouterBaseProps(
            listeners=listeners, virtual_router_name=virtual_router_name
        )

        return typing.cast("VirtualRouter", jsii.invoke(self, "addVirtualRouter", [id, props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMesh).__jsii_proxy_class__ = lambda : _IMeshProxy


@jsii.interface(jsii_type="@aws-cdk/aws-appmesh.IRoute")
class IRoute(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''Interface for which all Route based classes MUST implement.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routeArn")
    def route_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the route.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routeName")
    def route_name(self) -> builtins.str:
        '''The name of the route.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouter")
    def virtual_router(self) -> "IVirtualRouter":
        '''The VirtualRouter the Route belongs to.'''
        ...


class _IRouteProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''Interface for which all Route based classes MUST implement.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appmesh.IRoute"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routeArn")
    def route_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the route.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "routeArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routeName")
    def route_name(self) -> builtins.str:
        '''The name of the route.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "routeName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouter")
    def virtual_router(self) -> "IVirtualRouter":
        '''The VirtualRouter the Route belongs to.'''
        return typing.cast("IVirtualRouter", jsii.get(self, "virtualRouter"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRoute).__jsii_proxy_class__ = lambda : _IRouteProxy


@jsii.interface(jsii_type="@aws-cdk/aws-appmesh.IVirtualGateway")
class IVirtualGateway(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''Interface which all Virtual Gateway based classes must implement.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualGateway belongs to.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGatewayArn")
    def virtual_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the VirtualGateway.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGatewayName")
    def virtual_gateway_name(self) -> builtins.str:
        '''Name of the VirtualGateway.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addGatewayRoute")
    def add_gateway_route(
        self,
        id: builtins.str,
        *,
        route_spec: GatewayRouteSpec,
        gateway_route_name: typing.Optional[builtins.str] = None,
    ) -> "GatewayRoute":
        '''Utility method to add a new GatewayRoute to the VirtualGateway.

        :param id: -
        :param route_spec: What protocol the route uses.
        :param gateway_route_name: The name of the GatewayRoute. Default: - an automatically generated name
        '''
        ...

    @jsii.member(jsii_name="grantStreamAggregatedResources")
    def grant_stream_aggregated_resources(
        self,
        identity: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grants the given entity ``appmesh:StreamAggregatedResources``.

        :param identity: -
        '''
        ...


class _IVirtualGatewayProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''Interface which all Virtual Gateway based classes must implement.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appmesh.IVirtualGateway"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualGateway belongs to.'''
        return typing.cast(IMesh, jsii.get(self, "mesh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGatewayArn")
    def virtual_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the VirtualGateway.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualGatewayArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGatewayName")
    def virtual_gateway_name(self) -> builtins.str:
        '''Name of the VirtualGateway.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualGatewayName"))

    @jsii.member(jsii_name="addGatewayRoute")
    def add_gateway_route(
        self,
        id: builtins.str,
        *,
        route_spec: GatewayRouteSpec,
        gateway_route_name: typing.Optional[builtins.str] = None,
    ) -> "GatewayRoute":
        '''Utility method to add a new GatewayRoute to the VirtualGateway.

        :param id: -
        :param route_spec: What protocol the route uses.
        :param gateway_route_name: The name of the GatewayRoute. Default: - an automatically generated name
        '''
        route = GatewayRouteBaseProps(
            route_spec=route_spec, gateway_route_name=gateway_route_name
        )

        return typing.cast("GatewayRoute", jsii.invoke(self, "addGatewayRoute", [id, route]))

    @jsii.member(jsii_name="grantStreamAggregatedResources")
    def grant_stream_aggregated_resources(
        self,
        identity: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grants the given entity ``appmesh:StreamAggregatedResources``.

        :param identity: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantStreamAggregatedResources", [identity]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualGateway).__jsii_proxy_class__ = lambda : _IVirtualGatewayProxy


@jsii.interface(jsii_type="@aws-cdk/aws-appmesh.IVirtualNode")
class IVirtualNode(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''Interface which all VirtualNode based classes must implement.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualNode belongs to.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualNodeArn")
    def virtual_node_arn(self) -> builtins.str:
        '''The Amazon Resource Name belonging to the VirtualNode.

        Set this value as the APPMESH_VIRTUAL_NODE_NAME environment variable for
        your task group's Envoy proxy container in your task definition or pod
        spec.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualNodeName")
    def virtual_node_name(self) -> builtins.str:
        '''The name of the VirtualNode.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grantStreamAggregatedResources")
    def grant_stream_aggregated_resources(
        self,
        identity: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grants the given entity ``appmesh:StreamAggregatedResources``.

        :param identity: -
        '''
        ...


class _IVirtualNodeProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''Interface which all VirtualNode based classes must implement.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appmesh.IVirtualNode"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualNode belongs to.'''
        return typing.cast(IMesh, jsii.get(self, "mesh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualNodeArn")
    def virtual_node_arn(self) -> builtins.str:
        '''The Amazon Resource Name belonging to the VirtualNode.

        Set this value as the APPMESH_VIRTUAL_NODE_NAME environment variable for
        your task group's Envoy proxy container in your task definition or pod
        spec.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualNodeArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualNodeName")
    def virtual_node_name(self) -> builtins.str:
        '''The name of the VirtualNode.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualNodeName"))

    @jsii.member(jsii_name="grantStreamAggregatedResources")
    def grant_stream_aggregated_resources(
        self,
        identity: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grants the given entity ``appmesh:StreamAggregatedResources``.

        :param identity: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantStreamAggregatedResources", [identity]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualNode).__jsii_proxy_class__ = lambda : _IVirtualNodeProxy


@jsii.interface(jsii_type="@aws-cdk/aws-appmesh.IVirtualRouter")
class IVirtualRouter(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''Interface which all VirtualRouter based classes MUST implement.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualRouter belongs to.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouterArn")
    def virtual_router_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the VirtualRouter.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouterName")
    def virtual_router_name(self) -> builtins.str:
        '''The name of the VirtualRouter.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addRoute")
    def add_route(
        self,
        id: builtins.str,
        *,
        route_spec: "RouteSpec",
        route_name: typing.Optional[builtins.str] = None,
    ) -> "Route":
        '''Add a single route to the router.

        :param id: -
        :param route_spec: Protocol specific spec.
        :param route_name: The name of the route. Default: - An automatically generated name
        '''
        ...


class _IVirtualRouterProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''Interface which all VirtualRouter based classes MUST implement.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appmesh.IVirtualRouter"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualRouter belongs to.'''
        return typing.cast(IMesh, jsii.get(self, "mesh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouterArn")
    def virtual_router_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the VirtualRouter.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualRouterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouterName")
    def virtual_router_name(self) -> builtins.str:
        '''The name of the VirtualRouter.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualRouterName"))

    @jsii.member(jsii_name="addRoute")
    def add_route(
        self,
        id: builtins.str,
        *,
        route_spec: "RouteSpec",
        route_name: typing.Optional[builtins.str] = None,
    ) -> "Route":
        '''Add a single route to the router.

        :param id: -
        :param route_spec: Protocol specific spec.
        :param route_name: The name of the route. Default: - An automatically generated name
        '''
        props = RouteBaseProps(route_spec=route_spec, route_name=route_name)

        return typing.cast("Route", jsii.invoke(self, "addRoute", [id, props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualRouter).__jsii_proxy_class__ = lambda : _IVirtualRouterProxy


@jsii.interface(jsii_type="@aws-cdk/aws-appmesh.IVirtualService")
class IVirtualService(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''Represents the interface which all VirtualService based classes MUST implement.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualService belongs to.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualServiceArn")
    def virtual_service_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the virtual service.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualServiceName")
    def virtual_service_name(self) -> builtins.str:
        '''The name of the VirtualService.

        :attribute: true
        '''
        ...


class _IVirtualServiceProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''Represents the interface which all VirtualService based classes MUST implement.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appmesh.IVirtualService"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualService belongs to.'''
        return typing.cast(IMesh, jsii.get(self, "mesh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualServiceArn")
    def virtual_service_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the virtual service.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualServiceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualServiceName")
    def virtual_service_name(self) -> builtins.str:
        '''The name of the VirtualService.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "virtualServiceName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualService).__jsii_proxy_class__ = lambda : _IVirtualServiceProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.ListenerTlsOptions",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "mode": "mode",
        "mutual_tls_validation": "mutualTlsValidation",
    },
)
class ListenerTlsOptions:
    def __init__(
        self,
        *,
        certificate: "TlsCertificate",
        mode: "TlsMode",
        mutual_tls_validation: typing.Optional["MutualTlsValidation"] = None,
    ) -> None:
        '''Represents TLS properties for listener.

        :param certificate: Represents TLS certificate.
        :param mode: The TLS mode.
        :param mutual_tls_validation: Represents a listener's TLS validation context. The client certificate will only be validated if the client provides it, enabling mutual TLS. Default: - client TLS certificate is not required
        '''
        if isinstance(mutual_tls_validation, dict):
            mutual_tls_validation = MutualTlsValidation(**mutual_tls_validation)
        self._values: typing.Dict[str, typing.Any] = {
            "certificate": certificate,
            "mode": mode,
        }
        if mutual_tls_validation is not None:
            self._values["mutual_tls_validation"] = mutual_tls_validation

    @builtins.property
    def certificate(self) -> "TlsCertificate":
        '''Represents TLS certificate.'''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast("TlsCertificate", result)

    @builtins.property
    def mode(self) -> "TlsMode":
        '''The TLS mode.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast("TlsMode", result)

    @builtins.property
    def mutual_tls_validation(self) -> typing.Optional["MutualTlsValidation"]:
        '''Represents a listener's TLS validation context.

        The client certificate will only be validated if the client provides it, enabling mutual TLS.

        :default: - client TLS certificate is not required
        '''
        result = self._values.get("mutual_tls_validation")
        return typing.cast(typing.Optional["MutualTlsValidation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListenerTlsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IMesh)
class Mesh(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.Mesh",
):
    '''Define a new AppMesh mesh.

    :see: https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        egress_filter: typing.Optional["MeshFilterType"] = None,
        mesh_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param egress_filter: Egress filter to be applied to the Mesh. Default: DROP_ALL
        :param mesh_name: The name of the Mesh being defined. Default: - A name is automatically generated
        '''
        props = MeshProps(egress_filter=egress_filter, mesh_name=mesh_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromMeshArn") # type: ignore[misc]
    @builtins.classmethod
    def from_mesh_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        mesh_arn: builtins.str,
    ) -> IMesh:
        '''Import an existing mesh by arn.

        :param scope: -
        :param id: -
        :param mesh_arn: -
        '''
        return typing.cast(IMesh, jsii.sinvoke(cls, "fromMeshArn", [scope, id, mesh_arn]))

    @jsii.member(jsii_name="fromMeshName") # type: ignore[misc]
    @builtins.classmethod
    def from_mesh_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        mesh_name: builtins.str,
    ) -> IMesh:
        '''Import an existing mesh by name.

        :param scope: -
        :param id: -
        :param mesh_name: -
        '''
        return typing.cast(IMesh, jsii.sinvoke(cls, "fromMeshName", [scope, id, mesh_name]))

    @jsii.member(jsii_name="addVirtualGateway")
    def add_virtual_gateway(
        self,
        id: builtins.str,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        listeners: typing.Optional[typing.Sequence["VirtualGatewayListener"]] = None,
        virtual_gateway_name: typing.Optional[builtins.str] = None,
    ) -> "VirtualGateway":
        '''Adds a VirtualGateway to the Mesh.

        :param id: -
        :param access_log: Access Logging Configuration for the VirtualGateway. Default: - no access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param listeners: Listeners for the VirtualGateway. Only one is supported. Default: - Single HTTP listener on port 8080
        :param virtual_gateway_name: Name of the VirtualGateway. Default: - A name is automatically determined
        '''
        props = VirtualGatewayBaseProps(
            access_log=access_log,
            backend_defaults=backend_defaults,
            listeners=listeners,
            virtual_gateway_name=virtual_gateway_name,
        )

        return typing.cast("VirtualGateway", jsii.invoke(self, "addVirtualGateway", [id, props]))

    @jsii.member(jsii_name="addVirtualNode")
    def add_virtual_node(
        self,
        id: builtins.str,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        backends: typing.Optional[typing.Sequence[Backend]] = None,
        listeners: typing.Optional[typing.Sequence["VirtualNodeListener"]] = None,
        service_discovery: typing.Optional["ServiceDiscovery"] = None,
        virtual_node_name: typing.Optional[builtins.str] = None,
    ) -> "VirtualNode":
        '''Adds a VirtualNode to the Mesh.

        :param id: -
        :param access_log: Access Logging Configuration for the virtual node. Default: - No access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param backends: Virtual Services that this is node expected to send outbound traffic to. Default: - No backends
        :param listeners: Initial listener for the virtual node. Default: - No listeners
        :param service_discovery: Defines how upstream clients will discover this VirtualNode. Default: - No Service Discovery
        :param virtual_node_name: The name of the VirtualNode. Default: - A name is automatically determined
        '''
        props = VirtualNodeBaseProps(
            access_log=access_log,
            backend_defaults=backend_defaults,
            backends=backends,
            listeners=listeners,
            service_discovery=service_discovery,
            virtual_node_name=virtual_node_name,
        )

        return typing.cast("VirtualNode", jsii.invoke(self, "addVirtualNode", [id, props]))

    @jsii.member(jsii_name="addVirtualRouter")
    def add_virtual_router(
        self,
        id: builtins.str,
        *,
        listeners: typing.Optional[typing.Sequence["VirtualRouterListener"]] = None,
        virtual_router_name: typing.Optional[builtins.str] = None,
    ) -> "VirtualRouter":
        '''Adds a VirtualRouter to the Mesh with the given id and props.

        :param id: -
        :param listeners: Listener specification for the VirtualRouter. Default: - A listener on HTTP port 8080
        :param virtual_router_name: The name of the VirtualRouter. Default: - A name is automatically determined
        '''
        props = VirtualRouterBaseProps(
            listeners=listeners, virtual_router_name=virtual_router_name
        )

        return typing.cast("VirtualRouter", jsii.invoke(self, "addVirtualRouter", [id, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshArn")
    def mesh_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AppMesh mesh.'''
        return typing.cast(builtins.str, jsii.get(self, "meshArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        '''The name of the AppMesh mesh.'''
        return typing.cast(builtins.str, jsii.get(self, "meshName"))


@jsii.enum(jsii_type="@aws-cdk/aws-appmesh.MeshFilterType")
class MeshFilterType(enum.Enum):
    '''A utility enum defined for the egressFilter type property, the default of DROP_ALL, allows traffic only to other resources inside the mesh, or API calls to amazon resources.

    :default: DROP_ALL
    '''

    ALLOW_ALL = "ALLOW_ALL"
    '''Allows all outbound traffic.'''
    DROP_ALL = "DROP_ALL"
    '''Allows traffic only to other resources inside the mesh, or API calls to amazon resources.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.MeshProps",
    jsii_struct_bases=[],
    name_mapping={"egress_filter": "egressFilter", "mesh_name": "meshName"},
)
class MeshProps:
    def __init__(
        self,
        *,
        egress_filter: typing.Optional[MeshFilterType] = None,
        mesh_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The set of properties used when creating a Mesh.

        :param egress_filter: Egress filter to be applied to the Mesh. Default: DROP_ALL
        :param mesh_name: The name of the Mesh being defined. Default: - A name is automatically generated
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if egress_filter is not None:
            self._values["egress_filter"] = egress_filter
        if mesh_name is not None:
            self._values["mesh_name"] = mesh_name

    @builtins.property
    def egress_filter(self) -> typing.Optional[MeshFilterType]:
        '''Egress filter to be applied to the Mesh.

        :default: DROP_ALL
        '''
        result = self._values.get("egress_filter")
        return typing.cast(typing.Optional[MeshFilterType], result)

    @builtins.property
    def mesh_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Mesh being defined.

        :default: - A name is automatically generated
        '''
        result = self._values.get("mesh_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MeshProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.MutualTlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class MutualTlsValidation:
    def __init__(
        self,
        *,
        trust: "MutualTlsValidationTrust",
        subject_alternative_names: typing.Optional["SubjectAlternativeNames"] = None,
    ) -> None:
        '''Represents the properties needed to define TLS Validation context that is supported for mutual TLS authentication.

        :param trust: Reference to where to retrieve the trust chain.
        :param subject_alternative_names: Represents the subject alternative names (SANs) secured by the certificate. SANs must be in the FQDN or URI format. Default: - If you don't specify SANs on the terminating mesh endpoint, the Envoy proxy for that node doesn't verify the SAN on a peer client certificate. If you don't specify SANs on the originating mesh endpoint, the SAN on the certificate provided by the terminating endpoint must match the mesh endpoint service discovery configuration.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "trust": trust,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def trust(self) -> "MutualTlsValidationTrust":
        '''Reference to where to retrieve the trust chain.'''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("MutualTlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional["SubjectAlternativeNames"]:
        '''Represents the subject alternative names (SANs) secured by the certificate.

        SANs must be in the FQDN or URI format.

        :default:

        - If you don't specify SANs on the terminating mesh endpoint,
        the Envoy proxy for that node doesn't verify the SAN on a peer client certificate.
        If you don't specify SANs on the originating mesh endpoint,
        the SAN on the certificate provided by the terminating endpoint must match the mesh endpoint service discovery configuration.
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["SubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutualTlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.OutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_duration": "baseEjectionDuration",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "max_server_errors": "maxServerErrors",
    },
)
class OutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_duration: aws_cdk.core.Duration,
        interval: aws_cdk.core.Duration,
        max_ejection_percent: jsii.Number,
        max_server_errors: jsii.Number,
    ) -> None:
        '''Represents the outlier detection for a listener.

        :param base_ejection_duration: The base amount of time for which a host is ejected.
        :param interval: The time interval between ejection sweep analysis.
        :param max_ejection_percent: Maximum percentage of hosts in load balancing pool for upstream service that can be ejected. Will eject at least one host regardless of the value.
        :param max_server_errors: Number of consecutive 5xx errors required for ejection.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "base_ejection_duration": base_ejection_duration,
            "interval": interval,
            "max_ejection_percent": max_ejection_percent,
            "max_server_errors": max_server_errors,
        }

    @builtins.property
    def base_ejection_duration(self) -> aws_cdk.core.Duration:
        '''The base amount of time for which a host is ejected.'''
        result = self._values.get("base_ejection_duration")
        assert result is not None, "Required property 'base_ejection_duration' is missing"
        return typing.cast(aws_cdk.core.Duration, result)

    @builtins.property
    def interval(self) -> aws_cdk.core.Duration:
        '''The time interval between ejection sweep analysis.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(aws_cdk.core.Duration, result)

    @builtins.property
    def max_ejection_percent(self) -> jsii.Number:
        '''Maximum percentage of hosts in load balancing pool for upstream service that can be ejected.

        Will eject at
        least one host regardless of the value.
        '''
        result = self._values.get("max_ejection_percent")
        assert result is not None, "Required property 'max_ejection_percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_server_errors(self) -> jsii.Number:
        '''Number of consecutive 5xx errors required for ejection.'''
        result = self._values.get("max_server_errors")
        assert result is not None, "Required property 'max_server_errors' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appmesh.Protocol")
class Protocol(enum.Enum):
    '''(deprecated) Enum of supported AppMesh protocols.

    :deprecated: not for use outside package

    :stability: deprecated
    '''

    HTTP = "HTTP"
    '''
    :stability: deprecated
    '''
    TCP = "TCP"
    '''
    :stability: deprecated
    '''
    HTTP2 = "HTTP2"
    '''
    :stability: deprecated
    '''
    GRPC = "GRPC"
    '''
    :stability: deprecated
    '''


class QueryParameterMatch(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.QueryParameterMatch",
):
    '''Used to generate query parameter matching methods.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="valueIs") # type: ignore[misc]
    @builtins.classmethod
    def value_is(
        cls,
        query_parameter_name: builtins.str,
        query_parameter_value: builtins.str,
    ) -> "QueryParameterMatch":
        '''The value of the query parameter with the given name in the request must match the specified value exactly.

        :param query_parameter_name: the name of the query parameter to match against.
        :param query_parameter_value: The exact value to test against.
        '''
        return typing.cast("QueryParameterMatch", jsii.sinvoke(cls, "valueIs", [query_parameter_name, query_parameter_value]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "QueryParameterMatchConfig":
        '''Returns the query parameter match configuration.

        :param scope: -
        '''
        ...


class _QueryParameterMatchProxy(QueryParameterMatch):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "QueryParameterMatchConfig":
        '''Returns the query parameter match configuration.

        :param scope: -
        '''
        return typing.cast("QueryParameterMatchConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, QueryParameterMatch).__jsii_proxy_class__ = lambda : _QueryParameterMatchProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.QueryParameterMatchConfig",
    jsii_struct_bases=[],
    name_mapping={"query_parameter_match": "queryParameterMatch"},
)
class QueryParameterMatchConfig:
    def __init__(
        self,
        *,
        query_parameter_match: CfnRoute.QueryParameterProperty,
    ) -> None:
        '''Configuration for ``QueryParameterMatch``.

        :param query_parameter_match: Route CFN configuration for route query parameter match.
        '''
        if isinstance(query_parameter_match, dict):
            query_parameter_match = CfnRoute.QueryParameterProperty(**query_parameter_match)
        self._values: typing.Dict[str, typing.Any] = {
            "query_parameter_match": query_parameter_match,
        }

    @builtins.property
    def query_parameter_match(self) -> CfnRoute.QueryParameterProperty:
        '''Route CFN configuration for route query parameter match.'''
        result = self._values.get("query_parameter_match")
        assert result is not None, "Required property 'query_parameter_match' is missing"
        return typing.cast(CfnRoute.QueryParameterProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueryParameterMatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRoute)
class Route(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.Route",
):
    '''Route represents a new or existing route attached to a VirtualRouter and Mesh.

    :see: https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        mesh: IMesh,
        virtual_router: IVirtualRouter,
        route_spec: "RouteSpec",
        route_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param mesh: The service mesh to define the route in.
        :param virtual_router: The VirtualRouter the Route belongs to.
        :param route_spec: Protocol specific spec.
        :param route_name: The name of the route. Default: - An automatically generated name
        '''
        props = RouteProps(
            mesh=mesh,
            virtual_router=virtual_router,
            route_spec=route_spec,
            route_name=route_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromRouteArn") # type: ignore[misc]
    @builtins.classmethod
    def from_route_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        route_arn: builtins.str,
    ) -> IRoute:
        '''Import an existing Route given an ARN.

        :param scope: -
        :param id: -
        :param route_arn: -
        '''
        return typing.cast(IRoute, jsii.sinvoke(cls, "fromRouteArn", [scope, id, route_arn]))

    @jsii.member(jsii_name="fromRouteAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_route_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        route_name: builtins.str,
        virtual_router: IVirtualRouter,
    ) -> IRoute:
        '''Import an existing Route given attributes.

        :param scope: -
        :param id: -
        :param route_name: The name of the Route.
        :param virtual_router: The VirtualRouter the Route belongs to.
        '''
        attrs = RouteAttributes(route_name=route_name, virtual_router=virtual_router)

        return typing.cast(IRoute, jsii.sinvoke(cls, "fromRouteAttributes", [scope, id, attrs]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routeArn")
    def route_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the route.'''
        return typing.cast(builtins.str, jsii.get(self, "routeArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routeName")
    def route_name(self) -> builtins.str:
        '''The name of the Route.'''
        return typing.cast(builtins.str, jsii.get(self, "routeName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouter")
    def virtual_router(self) -> IVirtualRouter:
        '''The VirtualRouter the Route belongs to.'''
        return typing.cast(IVirtualRouter, jsii.get(self, "virtualRouter"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.RouteAttributes",
    jsii_struct_bases=[],
    name_mapping={"route_name": "routeName", "virtual_router": "virtualRouter"},
)
class RouteAttributes:
    def __init__(
        self,
        *,
        route_name: builtins.str,
        virtual_router: IVirtualRouter,
    ) -> None:
        '''Interface with properties ncecessary to import a reusable Route.

        :param route_name: The name of the Route.
        :param virtual_router: The VirtualRouter the Route belongs to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "route_name": route_name,
            "virtual_router": virtual_router,
        }

    @builtins.property
    def route_name(self) -> builtins.str:
        '''The name of the Route.'''
        result = self._values.get("route_name")
        assert result is not None, "Required property 'route_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_router(self) -> IVirtualRouter:
        '''The VirtualRouter the Route belongs to.'''
        result = self._values.get("virtual_router")
        assert result is not None, "Required property 'virtual_router' is missing"
        return typing.cast(IVirtualRouter, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.RouteBaseProps",
    jsii_struct_bases=[],
    name_mapping={"route_spec": "routeSpec", "route_name": "routeName"},
)
class RouteBaseProps:
    def __init__(
        self,
        *,
        route_spec: "RouteSpec",
        route_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Base interface properties for all Routes.

        :param route_spec: Protocol specific spec.
        :param route_name: The name of the route. Default: - An automatically generated name
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "route_spec": route_spec,
        }
        if route_name is not None:
            self._values["route_name"] = route_name

    @builtins.property
    def route_spec(self) -> "RouteSpec":
        '''Protocol specific spec.'''
        result = self._values.get("route_spec")
        assert result is not None, "Required property 'route_spec' is missing"
        return typing.cast("RouteSpec", result)

    @builtins.property
    def route_name(self) -> typing.Optional[builtins.str]:
        '''The name of the route.

        :default: - An automatically generated name
        '''
        result = self._values.get("route_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.RouteProps",
    jsii_struct_bases=[RouteBaseProps],
    name_mapping={
        "route_spec": "routeSpec",
        "route_name": "routeName",
        "mesh": "mesh",
        "virtual_router": "virtualRouter",
    },
)
class RouteProps(RouteBaseProps):
    def __init__(
        self,
        *,
        route_spec: "RouteSpec",
        route_name: typing.Optional[builtins.str] = None,
        mesh: IMesh,
        virtual_router: IVirtualRouter,
    ) -> None:
        '''Properties to define new Routes.

        :param route_spec: Protocol specific spec.
        :param route_name: The name of the route. Default: - An automatically generated name
        :param mesh: The service mesh to define the route in.
        :param virtual_router: The VirtualRouter the Route belongs to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "route_spec": route_spec,
            "mesh": mesh,
            "virtual_router": virtual_router,
        }
        if route_name is not None:
            self._values["route_name"] = route_name

    @builtins.property
    def route_spec(self) -> "RouteSpec":
        '''Protocol specific spec.'''
        result = self._values.get("route_spec")
        assert result is not None, "Required property 'route_spec' is missing"
        return typing.cast("RouteSpec", result)

    @builtins.property
    def route_name(self) -> typing.Optional[builtins.str]:
        '''The name of the route.

        :default: - An automatically generated name
        '''
        result = self._values.get("route_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh(self) -> IMesh:
        '''The service mesh to define the route in.'''
        result = self._values.get("mesh")
        assert result is not None, "Required property 'mesh' is missing"
        return typing.cast(IMesh, result)

    @builtins.property
    def virtual_router(self) -> IVirtualRouter:
        '''The VirtualRouter the Route belongs to.'''
        result = self._values.get("virtual_router")
        assert result is not None, "Required property 'virtual_router' is missing"
        return typing.cast(IVirtualRouter, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RouteSpec(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.RouteSpec",
):
    '''Used to generate specs with different protocols for a RouteSpec.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="grpc") # type: ignore[misc]
    @builtins.classmethod
    def grpc(
        cls,
        *,
        match: GrpcRouteMatch,
        weighted_targets: typing.Sequence["WeightedTarget"],
        retry_policy: typing.Optional["GrpcRetryPolicy"] = None,
        timeout: typing.Optional[GrpcTimeout] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> "RouteSpec":
        '''Creates a GRPC Based RouteSpec.

        :param match: The criterion for determining a request match for this Route.
        :param weighted_targets: List of targets that traffic is routed to when a request matches the route.
        :param retry_policy: The retry policy. Default: - no retry policy
        :param timeout: An object that represents a grpc timeout. Default: - None
        :param priority: The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority. Default: - no particular priority
        '''
        options = GrpcRouteSpecOptions(
            match=match,
            weighted_targets=weighted_targets,
            retry_policy=retry_policy,
            timeout=timeout,
            priority=priority,
        )

        return typing.cast("RouteSpec", jsii.sinvoke(cls, "grpc", [options]))

    @jsii.member(jsii_name="http") # type: ignore[misc]
    @builtins.classmethod
    def http(
        cls,
        *,
        weighted_targets: typing.Sequence["WeightedTarget"],
        match: typing.Optional[HttpRouteMatch] = None,
        retry_policy: typing.Optional[HttpRetryPolicy] = None,
        timeout: typing.Optional[HttpTimeout] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> "RouteSpec":
        '''Creates an HTTP Based RouteSpec.

        :param weighted_targets: List of targets that traffic is routed to when a request matches the route.
        :param match: The criterion for determining a request match for this Route. Default: - matches on '/'
        :param retry_policy: The retry policy. Default: - no retry policy
        :param timeout: An object that represents a http timeout. Default: - None
        :param priority: The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority. Default: - no particular priority
        '''
        options = HttpRouteSpecOptions(
            weighted_targets=weighted_targets,
            match=match,
            retry_policy=retry_policy,
            timeout=timeout,
            priority=priority,
        )

        return typing.cast("RouteSpec", jsii.sinvoke(cls, "http", [options]))

    @jsii.member(jsii_name="http2") # type: ignore[misc]
    @builtins.classmethod
    def http2(
        cls,
        *,
        weighted_targets: typing.Sequence["WeightedTarget"],
        match: typing.Optional[HttpRouteMatch] = None,
        retry_policy: typing.Optional[HttpRetryPolicy] = None,
        timeout: typing.Optional[HttpTimeout] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> "RouteSpec":
        '''Creates an HTTP2 Based RouteSpec.

        :param weighted_targets: List of targets that traffic is routed to when a request matches the route.
        :param match: The criterion for determining a request match for this Route. Default: - matches on '/'
        :param retry_policy: The retry policy. Default: - no retry policy
        :param timeout: An object that represents a http timeout. Default: - None
        :param priority: The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority. Default: - no particular priority
        '''
        options = HttpRouteSpecOptions(
            weighted_targets=weighted_targets,
            match=match,
            retry_policy=retry_policy,
            timeout=timeout,
            priority=priority,
        )

        return typing.cast("RouteSpec", jsii.sinvoke(cls, "http2", [options]))

    @jsii.member(jsii_name="tcp") # type: ignore[misc]
    @builtins.classmethod
    def tcp(
        cls,
        *,
        weighted_targets: typing.Sequence["WeightedTarget"],
        timeout: typing.Optional["TcpTimeout"] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> "RouteSpec":
        '''Creates a TCP Based RouteSpec.

        :param weighted_targets: List of targets that traffic is routed to when a request matches the route.
        :param timeout: An object that represents a tcp timeout. Default: - None
        :param priority: The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority. Default: - no particular priority
        '''
        options = TcpRouteSpecOptions(
            weighted_targets=weighted_targets, timeout=timeout, priority=priority
        )

        return typing.cast("RouteSpec", jsii.sinvoke(cls, "tcp", [options]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "RouteSpecConfig":
        '''Called when the RouteSpec type is initialized.

        Can be used to enforce
        mutual exclusivity with future properties

        :param scope: -
        '''
        ...


class _RouteSpecProxy(RouteSpec):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "RouteSpecConfig":
        '''Called when the RouteSpec type is initialized.

        Can be used to enforce
        mutual exclusivity with future properties

        :param scope: -
        '''
        return typing.cast("RouteSpecConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, RouteSpec).__jsii_proxy_class__ = lambda : _RouteSpecProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.RouteSpecConfig",
    jsii_struct_bases=[],
    name_mapping={
        "grpc_route_spec": "grpcRouteSpec",
        "http2_route_spec": "http2RouteSpec",
        "http_route_spec": "httpRouteSpec",
        "priority": "priority",
        "tcp_route_spec": "tcpRouteSpec",
    },
)
class RouteSpecConfig:
    def __init__(
        self,
        *,
        grpc_route_spec: typing.Optional[CfnRoute.GrpcRouteProperty] = None,
        http2_route_spec: typing.Optional[CfnRoute.HttpRouteProperty] = None,
        http_route_spec: typing.Optional[CfnRoute.HttpRouteProperty] = None,
        priority: typing.Optional[jsii.Number] = None,
        tcp_route_spec: typing.Optional[CfnRoute.TcpRouteProperty] = None,
    ) -> None:
        '''All Properties for Route Specs.

        :param grpc_route_spec: The spec for a grpc route. Default: - no grpc spec
        :param http2_route_spec: The spec for an http2 route. Default: - no http2 spec
        :param http_route_spec: The spec for an http route. Default: - no http spec
        :param priority: The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority. Default: - no particular priority
        :param tcp_route_spec: The spec for a tcp route. Default: - no tcp spec
        '''
        if isinstance(grpc_route_spec, dict):
            grpc_route_spec = CfnRoute.GrpcRouteProperty(**grpc_route_spec)
        if isinstance(http2_route_spec, dict):
            http2_route_spec = CfnRoute.HttpRouteProperty(**http2_route_spec)
        if isinstance(http_route_spec, dict):
            http_route_spec = CfnRoute.HttpRouteProperty(**http_route_spec)
        if isinstance(tcp_route_spec, dict):
            tcp_route_spec = CfnRoute.TcpRouteProperty(**tcp_route_spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if grpc_route_spec is not None:
            self._values["grpc_route_spec"] = grpc_route_spec
        if http2_route_spec is not None:
            self._values["http2_route_spec"] = http2_route_spec
        if http_route_spec is not None:
            self._values["http_route_spec"] = http_route_spec
        if priority is not None:
            self._values["priority"] = priority
        if tcp_route_spec is not None:
            self._values["tcp_route_spec"] = tcp_route_spec

    @builtins.property
    def grpc_route_spec(self) -> typing.Optional[CfnRoute.GrpcRouteProperty]:
        '''The spec for a grpc route.

        :default: - no grpc spec
        '''
        result = self._values.get("grpc_route_spec")
        return typing.cast(typing.Optional[CfnRoute.GrpcRouteProperty], result)

    @builtins.property
    def http2_route_spec(self) -> typing.Optional[CfnRoute.HttpRouteProperty]:
        '''The spec for an http2 route.

        :default: - no http2 spec
        '''
        result = self._values.get("http2_route_spec")
        return typing.cast(typing.Optional[CfnRoute.HttpRouteProperty], result)

    @builtins.property
    def http_route_spec(self) -> typing.Optional[CfnRoute.HttpRouteProperty]:
        '''The spec for an http route.

        :default: - no http spec
        '''
        result = self._values.get("http_route_spec")
        return typing.cast(typing.Optional[CfnRoute.HttpRouteProperty], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority for the route.

        Routes are matched based on the specified
        value, where 0 is the highest priority.

        :default: - no particular priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tcp_route_spec(self) -> typing.Optional[CfnRoute.TcpRouteProperty]:
        '''The spec for a tcp route.

        :default: - no tcp spec
        '''
        result = self._values.get("tcp_route_spec")
        return typing.cast(typing.Optional[CfnRoute.TcpRouteProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteSpecConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.RouteSpecOptionsBase",
    jsii_struct_bases=[],
    name_mapping={"priority": "priority"},
)
class RouteSpecOptionsBase:
    def __init__(self, *, priority: typing.Optional[jsii.Number] = None) -> None:
        '''Base options for all route specs.

        :param priority: The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority. Default: - no particular priority
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if priority is not None:
            self._values["priority"] = priority

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority for the route.

        Routes are matched based on the specified
        value, where 0 is the highest priority.

        :default: - no particular priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteSpecOptionsBase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceDiscovery(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.ServiceDiscovery",
):
    '''Provides the Service Discovery method a VirtualNode uses.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="cloudMap") # type: ignore[misc]
    @builtins.classmethod
    def cloud_map(
        cls,
        service: aws_cdk.aws_servicediscovery.IService,
        instance_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> "ServiceDiscovery":
        '''Returns Cloud Map based service discovery.

        :param service: The AWS Cloud Map Service to use for service discovery.
        :param instance_attributes: A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.
        '''
        return typing.cast("ServiceDiscovery", jsii.sinvoke(cls, "cloudMap", [service, instance_attributes]))

    @jsii.member(jsii_name="dns") # type: ignore[misc]
    @builtins.classmethod
    def dns(
        cls,
        hostname: builtins.str,
        response_type: typing.Optional[DnsResponseType] = None,
    ) -> "ServiceDiscovery":
        '''Returns DNS based service discovery.

        :param hostname: -
        :param response_type: Specifies the DNS response type for the virtual node. The default is ``DnsResponseType.LOAD_BALANCER``.
        '''
        return typing.cast("ServiceDiscovery", jsii.sinvoke(cls, "dns", [hostname, response_type]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "ServiceDiscoveryConfig":
        '''Binds the current object when adding Service Discovery to a VirtualNode.

        :param scope: -
        '''
        ...


class _ServiceDiscoveryProxy(ServiceDiscovery):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "ServiceDiscoveryConfig":
        '''Binds the current object when adding Service Discovery to a VirtualNode.

        :param scope: -
        '''
        return typing.cast("ServiceDiscoveryConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ServiceDiscovery).__jsii_proxy_class__ = lambda : _ServiceDiscoveryProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.ServiceDiscoveryConfig",
    jsii_struct_bases=[],
    name_mapping={"cloudmap": "cloudmap", "dns": "dns"},
)
class ServiceDiscoveryConfig:
    def __init__(
        self,
        *,
        cloudmap: typing.Optional[CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty] = None,
        dns: typing.Optional[CfnVirtualNode.DnsServiceDiscoveryProperty] = None,
    ) -> None:
        '''Properties for VirtualNode Service Discovery.

        :param cloudmap: Cloud Map based Service Discovery. Default: - no Cloud Map based service discovery
        :param dns: DNS based Service Discovery. Default: - no DNS based service discovery
        '''
        if isinstance(cloudmap, dict):
            cloudmap = CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty(**cloudmap)
        if isinstance(dns, dict):
            dns = CfnVirtualNode.DnsServiceDiscoveryProperty(**dns)
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudmap is not None:
            self._values["cloudmap"] = cloudmap
        if dns is not None:
            self._values["dns"] = dns

    @builtins.property
    def cloudmap(
        self,
    ) -> typing.Optional[CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty]:
        '''Cloud Map based Service Discovery.

        :default: - no Cloud Map based service discovery
        '''
        result = self._values.get("cloudmap")
        return typing.cast(typing.Optional[CfnVirtualNode.AwsCloudMapServiceDiscoveryProperty], result)

    @builtins.property
    def dns(self) -> typing.Optional[CfnVirtualNode.DnsServiceDiscoveryProperty]:
        '''DNS based Service Discovery.

        :default: - no DNS based service discovery
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[CfnVirtualNode.DnsServiceDiscoveryProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceDiscoveryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubjectAlternativeNames(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.SubjectAlternativeNames",
):
    '''Used to generate Subject Alternative Names Matchers.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="matchingExactly") # type: ignore[misc]
    @builtins.classmethod
    def matching_exactly(cls, *names: builtins.str) -> "SubjectAlternativeNames":
        '''The values of the SAN must match the specified values exactly.

        :param names: The exact values to test against.
        '''
        return typing.cast("SubjectAlternativeNames", jsii.sinvoke(cls, "matchingExactly", [*names]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(
        self,
        scope: aws_cdk.core.Construct,
    ) -> "SubjectAlternativeNamesMatcherConfig":
        '''Returns Subject Alternative Names Matcher based on method type.

        :param scope: -
        '''
        ...


class _SubjectAlternativeNamesProxy(SubjectAlternativeNames):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: aws_cdk.core.Construct,
    ) -> "SubjectAlternativeNamesMatcherConfig":
        '''Returns Subject Alternative Names Matcher based on method type.

        :param scope: -
        '''
        return typing.cast("SubjectAlternativeNamesMatcherConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, SubjectAlternativeNames).__jsii_proxy_class__ = lambda : _SubjectAlternativeNamesProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.SubjectAlternativeNamesMatcherConfig",
    jsii_struct_bases=[],
    name_mapping={"subject_alternative_names_match": "subjectAlternativeNamesMatch"},
)
class SubjectAlternativeNamesMatcherConfig:
    def __init__(
        self,
        *,
        subject_alternative_names_match: CfnVirtualNode.SubjectAlternativeNameMatchersProperty,
    ) -> None:
        '''All Properties for Subject Alternative Names Matcher for both Client Policy and Listener.

        :param subject_alternative_names_match: VirtualNode CFN configuration for subject alternative names secured by the certificate.
        '''
        if isinstance(subject_alternative_names_match, dict):
            subject_alternative_names_match = CfnVirtualNode.SubjectAlternativeNameMatchersProperty(**subject_alternative_names_match)
        self._values: typing.Dict[str, typing.Any] = {
            "subject_alternative_names_match": subject_alternative_names_match,
        }

    @builtins.property
    def subject_alternative_names_match(
        self,
    ) -> CfnVirtualNode.SubjectAlternativeNameMatchersProperty:
        '''VirtualNode CFN configuration for subject alternative names secured by the certificate.'''
        result = self._values.get("subject_alternative_names_match")
        assert result is not None, "Required property 'subject_alternative_names_match' is missing"
        return typing.cast(CfnVirtualNode.SubjectAlternativeNameMatchersProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubjectAlternativeNamesMatcherConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.TcpConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"max_connections": "maxConnections"},
)
class TcpConnectionPool:
    def __init__(self, *, max_connections: jsii.Number) -> None:
        '''Connection pool properties for TCP listeners.

        :param max_connections: The maximum connections in the pool. Default: - none
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_connections": max_connections,
        }

    @builtins.property
    def max_connections(self) -> jsii.Number:
        '''The maximum connections in the pool.

        :default: - none
        '''
        result = self._values.get("max_connections")
        assert result is not None, "Required property 'max_connections' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TcpConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.TcpHealthCheckOptions",
    jsii_struct_bases=[],
    name_mapping={
        "healthy_threshold": "healthyThreshold",
        "interval": "interval",
        "timeout": "timeout",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class TcpHealthCheckOptions:
    def __init__(
        self,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[aws_cdk.core.Duration] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties used to define TCP Based healthchecks.

        :param healthy_threshold: The number of consecutive successful health checks that must occur before declaring listener healthy. Default: 2
        :param interval: The time period between each health check execution. Default: Duration.seconds(5)
        :param timeout: The amount of time to wait when receiving a response from the health check. Default: Duration.seconds(2)
        :param unhealthy_threshold: The number of consecutive failed health checks that must occur before declaring a listener unhealthy. Default: - 2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if interval is not None:
            self._values["interval"] = interval
        if timeout is not None:
            self._values["timeout"] = timeout
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive successful health checks that must occur before declaring listener healthy.

        :default: 2
        '''
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The time period between each health check execution.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The amount of time to wait when receiving a response from the health check.

        :default: Duration.seconds(2)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive failed health checks that must occur before declaring a listener unhealthy.

        :default: - 2
        '''
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TcpHealthCheckOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appmesh.TcpRetryEvent")
class TcpRetryEvent(enum.Enum):
    '''TCP events on which you may retry.'''

    CONNECTION_ERROR = "CONNECTION_ERROR"
    '''A connection error.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.TcpRouteSpecOptions",
    jsii_struct_bases=[RouteSpecOptionsBase],
    name_mapping={
        "priority": "priority",
        "weighted_targets": "weightedTargets",
        "timeout": "timeout",
    },
)
class TcpRouteSpecOptions(RouteSpecOptionsBase):
    def __init__(
        self,
        *,
        priority: typing.Optional[jsii.Number] = None,
        weighted_targets: typing.Sequence["WeightedTarget"],
        timeout: typing.Optional["TcpTimeout"] = None,
    ) -> None:
        '''Properties specific for a TCP Based Routes.

        :param priority: The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority. Default: - no particular priority
        :param weighted_targets: List of targets that traffic is routed to when a request matches the route.
        :param timeout: An object that represents a tcp timeout. Default: - None
        '''
        if isinstance(timeout, dict):
            timeout = TcpTimeout(**timeout)
        self._values: typing.Dict[str, typing.Any] = {
            "weighted_targets": weighted_targets,
        }
        if priority is not None:
            self._values["priority"] = priority
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority for the route.

        Routes are matched based on the specified
        value, where 0 is the highest priority.

        :default: - no particular priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weighted_targets(self) -> typing.List["WeightedTarget"]:
        '''List of targets that traffic is routed to when a request matches the route.'''
        result = self._values.get("weighted_targets")
        assert result is not None, "Required property 'weighted_targets' is missing"
        return typing.cast(typing.List["WeightedTarget"], result)

    @builtins.property
    def timeout(self) -> typing.Optional["TcpTimeout"]:
        '''An object that represents a tcp timeout.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["TcpTimeout"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TcpRouteSpecOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.TcpTimeout",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle"},
)
class TcpTimeout:
    def __init__(self, *, idle: typing.Optional[aws_cdk.core.Duration] = None) -> None:
        '''Represents timeouts for TCP protocols.

        :param idle: Represents an idle timeout. The amount of time that a connection may be idle. Default: - none
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle

    @builtins.property
    def idle(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''Represents an idle timeout.

        The amount of time that a connection may be idle.

        :default: - none
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TcpTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.TcpVirtualNodeListenerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "outlier_detection": "outlierDetection",
        "port": "port",
        "timeout": "timeout",
        "tls": "tls",
    },
)
class TcpVirtualNodeListenerOptions:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional[TcpConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        outlier_detection: typing.Optional[OutlierDetection] = None,
        port: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[TcpTimeout] = None,
        tls: typing.Optional[ListenerTlsOptions] = None,
    ) -> None:
        '''Represent the TCP Node Listener prorperty.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param outlier_detection: Represents the configuration for enabling outlier detection. Default: - none
        :param port: Port to listen for connections on. Default: - 8080
        :param timeout: Timeout for TCP protocol. Default: - None
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        if isinstance(connection_pool, dict):
            connection_pool = TcpConnectionPool(**connection_pool)
        if isinstance(outlier_detection, dict):
            outlier_detection = OutlierDetection(**outlier_detection)
        if isinstance(timeout, dict):
            timeout = TcpTimeout(**timeout)
        if isinstance(tls, dict):
            tls = ListenerTlsOptions(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port is not None:
            self._values["port"] = port
        if timeout is not None:
            self._values["timeout"] = timeout
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(self) -> typing.Optional[TcpConnectionPool]:
        '''Connection pool for http listeners.

        :default: - None
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional[TcpConnectionPool], result)

    @builtins.property
    def health_check(self) -> typing.Optional[HealthCheck]:
        '''The health check information for the listener.

        :default: - no healthcheck
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[HealthCheck], result)

    @builtins.property
    def outlier_detection(self) -> typing.Optional[OutlierDetection]:
        '''Represents the configuration for enabling outlier detection.

        :default: - none
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional[OutlierDetection], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to listen for connections on.

        :default: - 8080
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout(self) -> typing.Optional[TcpTimeout]:
        '''Timeout for TCP protocol.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[TcpTimeout], result)

    @builtins.property
    def tls(self) -> typing.Optional[ListenerTlsOptions]:
        '''Represents the configuration for enabling TLS on a listener.

        :default: - none
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[ListenerTlsOptions], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TcpVirtualNodeListenerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TlsCertificate(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.TlsCertificate",
):
    '''Represents a TLS certificate.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="acm") # type: ignore[misc]
    @builtins.classmethod
    def acm(
        cls,
        certificate: aws_cdk.aws_certificatemanager.ICertificate,
    ) -> "TlsCertificate":
        '''Returns an ACM TLS Certificate.

        :param certificate: -
        '''
        return typing.cast("TlsCertificate", jsii.sinvoke(cls, "acm", [certificate]))

    @jsii.member(jsii_name="file") # type: ignore[misc]
    @builtins.classmethod
    def file(
        cls,
        certificate_chain_path: builtins.str,
        private_key_path: builtins.str,
    ) -> "MutualTlsCertificate":
        '''Returns an File TLS Certificate.

        :param certificate_chain_path: -
        :param private_key_path: -
        '''
        return typing.cast("MutualTlsCertificate", jsii.sinvoke(cls, "file", [certificate_chain_path, private_key_path]))

    @jsii.member(jsii_name="sds") # type: ignore[misc]
    @builtins.classmethod
    def sds(cls, secret_name: builtins.str) -> "MutualTlsCertificate":
        '''Returns an SDS TLS Certificate.

        :param secret_name: -
        '''
        return typing.cast("MutualTlsCertificate", jsii.sinvoke(cls, "sds", [secret_name]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, _scope: aws_cdk.core.Construct) -> "TlsCertificateConfig":
        '''Returns TLS certificate based provider.

        :param _scope: -
        '''
        ...


class _TlsCertificateProxy(TlsCertificate):
    @jsii.member(jsii_name="bind")
    def bind(self, _scope: aws_cdk.core.Construct) -> "TlsCertificateConfig":
        '''Returns TLS certificate based provider.

        :param _scope: -
        '''
        return typing.cast("TlsCertificateConfig", jsii.invoke(self, "bind", [_scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, TlsCertificate).__jsii_proxy_class__ = lambda : _TlsCertificateProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.TlsCertificateConfig",
    jsii_struct_bases=[],
    name_mapping={"tls_certificate": "tlsCertificate"},
)
class TlsCertificateConfig:
    def __init__(
        self,
        *,
        tls_certificate: CfnVirtualNode.ListenerTlsCertificateProperty,
    ) -> None:
        '''A wrapper for the tls config returned by {@link TlsCertificate.bind}.

        :param tls_certificate: The CFN shape for a TLS certificate.
        '''
        if isinstance(tls_certificate, dict):
            tls_certificate = CfnVirtualNode.ListenerTlsCertificateProperty(**tls_certificate)
        self._values: typing.Dict[str, typing.Any] = {
            "tls_certificate": tls_certificate,
        }

    @builtins.property
    def tls_certificate(self) -> CfnVirtualNode.ListenerTlsCertificateProperty:
        '''The CFN shape for a TLS certificate.'''
        result = self._values.get("tls_certificate")
        assert result is not None, "Required property 'tls_certificate' is missing"
        return typing.cast(CfnVirtualNode.ListenerTlsCertificateProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TlsCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.TlsClientPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "validation": "validation",
        "enforce": "enforce",
        "mutual_tls_certificate": "mutualTlsCertificate",
        "ports": "ports",
    },
)
class TlsClientPolicy:
    def __init__(
        self,
        *,
        validation: "TlsValidation",
        enforce: typing.Optional[builtins.bool] = None,
        mutual_tls_certificate: typing.Optional["MutualTlsCertificate"] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''Represents the properties needed to define client policy.

        :param validation: Represents the object for TLS validation context.
        :param enforce: Whether the policy is enforced. Default: true
        :param mutual_tls_certificate: Represents a client TLS certificate. The certificate will be sent only if the server requests it, enabling mutual TLS. Default: - client TLS certificate is not provided
        :param ports: TLS is enforced on the ports specified here. If no ports are specified, TLS will be enforced on all the ports. Default: - all ports
        '''
        if isinstance(validation, dict):
            validation = TlsValidation(**validation)
        self._values: typing.Dict[str, typing.Any] = {
            "validation": validation,
        }
        if enforce is not None:
            self._values["enforce"] = enforce
        if mutual_tls_certificate is not None:
            self._values["mutual_tls_certificate"] = mutual_tls_certificate
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def validation(self) -> "TlsValidation":
        '''Represents the object for TLS validation context.'''
        result = self._values.get("validation")
        assert result is not None, "Required property 'validation' is missing"
        return typing.cast("TlsValidation", result)

    @builtins.property
    def enforce(self) -> typing.Optional[builtins.bool]:
        '''Whether the policy is enforced.

        :default: true
        '''
        result = self._values.get("enforce")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mutual_tls_certificate(self) -> typing.Optional["MutualTlsCertificate"]:
        '''Represents a client TLS certificate.

        The certificate will be sent only if the server requests it, enabling mutual TLS.

        :default: - client TLS certificate is not provided
        '''
        result = self._values.get("mutual_tls_certificate")
        return typing.cast(typing.Optional["MutualTlsCertificate"], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''TLS is enforced on the ports specified here.

        If no ports are specified, TLS will be enforced on all the ports.

        :default: - all ports
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TlsClientPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appmesh.TlsMode")
class TlsMode(enum.Enum):
    '''Enum of supported TLS modes.'''

    STRICT = "STRICT"
    '''Only accept encrypted traffic.'''
    PERMISSIVE = "PERMISSIVE"
    '''Accept encrypted and plaintext traffic.'''
    DISABLED = "DISABLED"
    '''TLS is disabled, only accept plaintext traffic.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.TlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class TlsValidation:
    def __init__(
        self,
        *,
        trust: "TlsValidationTrust",
        subject_alternative_names: typing.Optional[SubjectAlternativeNames] = None,
    ) -> None:
        '''Represents the properties needed to define TLS Validation context.

        :param trust: Reference to where to retrieve the trust chain.
        :param subject_alternative_names: Represents the subject alternative names (SANs) secured by the certificate. SANs must be in the FQDN or URI format. Default: - If you don't specify SANs on the terminating mesh endpoint, the Envoy proxy for that node doesn't verify the SAN on a peer client certificate. If you don't specify SANs on the originating mesh endpoint, the SAN on the certificate provided by the terminating endpoint must match the mesh endpoint service discovery configuration.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "trust": trust,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def trust(self) -> "TlsValidationTrust":
        '''Reference to where to retrieve the trust chain.'''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("TlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[SubjectAlternativeNames]:
        '''Represents the subject alternative names (SANs) secured by the certificate.

        SANs must be in the FQDN or URI format.

        :default:

        - If you don't specify SANs on the terminating mesh endpoint,
        the Envoy proxy for that node doesn't verify the SAN on a peer client certificate.
        If you don't specify SANs on the originating mesh endpoint,
        the SAN on the certificate provided by the terminating endpoint must match the mesh endpoint service discovery configuration.
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional[SubjectAlternativeNames], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TlsValidationTrust(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.TlsValidationTrust",
):
    '''Defines the TLS Validation Context Trust.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="acm") # type: ignore[misc]
    @builtins.classmethod
    def acm(
        cls,
        certificate_authorities: typing.Sequence[aws_cdk.aws_acmpca.ICertificateAuthority],
    ) -> "TlsValidationTrust":
        '''TLS Validation Context Trust for ACM Private Certificate Authority (CA).

        :param certificate_authorities: -
        '''
        return typing.cast("TlsValidationTrust", jsii.sinvoke(cls, "acm", [certificate_authorities]))

    @jsii.member(jsii_name="file") # type: ignore[misc]
    @builtins.classmethod
    def file(cls, certificate_chain: builtins.str) -> "MutualTlsValidationTrust":
        '''Tells envoy where to fetch the validation context from.

        :param certificate_chain: -
        '''
        return typing.cast("MutualTlsValidationTrust", jsii.sinvoke(cls, "file", [certificate_chain]))

    @jsii.member(jsii_name="sds") # type: ignore[misc]
    @builtins.classmethod
    def sds(cls, secret_name: builtins.str) -> "MutualTlsValidationTrust":
        '''TLS Validation Context Trust for Envoy' service discovery service.

        :param secret_name: -
        '''
        return typing.cast("MutualTlsValidationTrust", jsii.sinvoke(cls, "sds", [secret_name]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "TlsValidationTrustConfig":
        '''Returns Trust context based on trust type.

        :param scope: -
        '''
        ...


class _TlsValidationTrustProxy(TlsValidationTrust):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "TlsValidationTrustConfig":
        '''Returns Trust context based on trust type.

        :param scope: -
        '''
        return typing.cast("TlsValidationTrustConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, TlsValidationTrust).__jsii_proxy_class__ = lambda : _TlsValidationTrustProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.TlsValidationTrustConfig",
    jsii_struct_bases=[],
    name_mapping={"tls_validation_trust": "tlsValidationTrust"},
)
class TlsValidationTrustConfig:
    def __init__(
        self,
        *,
        tls_validation_trust: CfnVirtualNode.TlsValidationContextTrustProperty,
    ) -> None:
        '''All Properties for TLS Validation Trusts for both Client Policy and Listener.

        :param tls_validation_trust: VirtualNode CFN configuration for client policy's TLS Validation Trust.
        '''
        if isinstance(tls_validation_trust, dict):
            tls_validation_trust = CfnVirtualNode.TlsValidationContextTrustProperty(**tls_validation_trust)
        self._values: typing.Dict[str, typing.Any] = {
            "tls_validation_trust": tls_validation_trust,
        }

    @builtins.property
    def tls_validation_trust(self) -> CfnVirtualNode.TlsValidationContextTrustProperty:
        '''VirtualNode CFN configuration for client policy's TLS Validation Trust.'''
        result = self._values.get("tls_validation_trust")
        assert result is not None, "Required property 'tls_validation_trust' is missing"
        return typing.cast(CfnVirtualNode.TlsValidationContextTrustProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TlsValidationTrustConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IVirtualGateway)
class VirtualGateway(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.VirtualGateway",
):
    '''VirtualGateway represents a newly defined App Mesh Virtual Gateway.

    A virtual gateway allows resources that are outside of your mesh to communicate to resources that
    are inside of your mesh.

    :see: https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        mesh: IMesh,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        listeners: typing.Optional[typing.Sequence["VirtualGatewayListener"]] = None,
        virtual_gateway_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param mesh: The Mesh which the VirtualGateway belongs to.
        :param access_log: Access Logging Configuration for the VirtualGateway. Default: - no access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param listeners: Listeners for the VirtualGateway. Only one is supported. Default: - Single HTTP listener on port 8080
        :param virtual_gateway_name: Name of the VirtualGateway. Default: - A name is automatically determined
        '''
        props = VirtualGatewayProps(
            mesh=mesh,
            access_log=access_log,
            backend_defaults=backend_defaults,
            listeners=listeners,
            virtual_gateway_name=virtual_gateway_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromVirtualGatewayArn") # type: ignore[misc]
    @builtins.classmethod
    def from_virtual_gateway_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        virtual_gateway_arn: builtins.str,
    ) -> IVirtualGateway:
        '''Import an existing VirtualGateway given an ARN.

        :param scope: -
        :param id: -
        :param virtual_gateway_arn: -
        '''
        return typing.cast(IVirtualGateway, jsii.sinvoke(cls, "fromVirtualGatewayArn", [scope, id, virtual_gateway_arn]))

    @jsii.member(jsii_name="fromVirtualGatewayAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_virtual_gateway_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        mesh: IMesh,
        virtual_gateway_name: builtins.str,
    ) -> IVirtualGateway:
        '''Import an existing VirtualGateway given its attributes.

        :param scope: -
        :param id: -
        :param mesh: The Mesh that the VirtualGateway belongs to.
        :param virtual_gateway_name: The name of the VirtualGateway.
        '''
        attrs = VirtualGatewayAttributes(
            mesh=mesh, virtual_gateway_name=virtual_gateway_name
        )

        return typing.cast(IVirtualGateway, jsii.sinvoke(cls, "fromVirtualGatewayAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addGatewayRoute")
    def add_gateway_route(
        self,
        id: builtins.str,
        *,
        route_spec: GatewayRouteSpec,
        gateway_route_name: typing.Optional[builtins.str] = None,
    ) -> "GatewayRoute":
        '''Utility method to add a new GatewayRoute to the VirtualGateway.

        :param id: -
        :param route_spec: What protocol the route uses.
        :param gateway_route_name: The name of the GatewayRoute. Default: - an automatically generated name
        '''
        props = GatewayRouteBaseProps(
            route_spec=route_spec, gateway_route_name=gateway_route_name
        )

        return typing.cast("GatewayRoute", jsii.invoke(self, "addGatewayRoute", [id, props]))

    @jsii.member(jsii_name="grantStreamAggregatedResources")
    def grant_stream_aggregated_resources(
        self,
        identity: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grants the given entity ``appmesh:StreamAggregatedResources``.

        :param identity: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantStreamAggregatedResources", [identity]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listeners")
    def _listeners(self) -> typing.List["VirtualGatewayListenerConfig"]:
        return typing.cast(typing.List["VirtualGatewayListenerConfig"], jsii.get(self, "listeners"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh that the VirtualGateway belongs to.'''
        return typing.cast(IMesh, jsii.get(self, "mesh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGatewayArn")
    def virtual_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the VirtualGateway.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualGatewayArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGatewayName")
    def virtual_gateway_name(self) -> builtins.str:
        '''The name of the VirtualGateway.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualGatewayName"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualGatewayAttributes",
    jsii_struct_bases=[],
    name_mapping={"mesh": "mesh", "virtual_gateway_name": "virtualGatewayName"},
)
class VirtualGatewayAttributes:
    def __init__(self, *, mesh: IMesh, virtual_gateway_name: builtins.str) -> None:
        '''Unterface with properties necessary to import a reusable VirtualGateway.

        :param mesh: The Mesh that the VirtualGateway belongs to.
        :param virtual_gateway_name: The name of the VirtualGateway.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh": mesh,
            "virtual_gateway_name": virtual_gateway_name,
        }

    @builtins.property
    def mesh(self) -> IMesh:
        '''The Mesh that the VirtualGateway belongs to.'''
        result = self._values.get("mesh")
        assert result is not None, "Required property 'mesh' is missing"
        return typing.cast(IMesh, result)

    @builtins.property
    def virtual_gateway_name(self) -> builtins.str:
        '''The name of the VirtualGateway.'''
        result = self._values.get("virtual_gateway_name")
        assert result is not None, "Required property 'virtual_gateway_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualGatewayAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualGatewayBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_log": "accessLog",
        "backend_defaults": "backendDefaults",
        "listeners": "listeners",
        "virtual_gateway_name": "virtualGatewayName",
    },
)
class VirtualGatewayBaseProps:
    def __init__(
        self,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        listeners: typing.Optional[typing.Sequence["VirtualGatewayListener"]] = None,
        virtual_gateway_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Basic configuration properties for a VirtualGateway.

        :param access_log: Access Logging Configuration for the VirtualGateway. Default: - no access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param listeners: Listeners for the VirtualGateway. Only one is supported. Default: - Single HTTP listener on port 8080
        :param virtual_gateway_name: Name of the VirtualGateway. Default: - A name is automatically determined
        '''
        if isinstance(backend_defaults, dict):
            backend_defaults = BackendDefaults(**backend_defaults)
        self._values: typing.Dict[str, typing.Any] = {}
        if access_log is not None:
            self._values["access_log"] = access_log
        if backend_defaults is not None:
            self._values["backend_defaults"] = backend_defaults
        if listeners is not None:
            self._values["listeners"] = listeners
        if virtual_gateway_name is not None:
            self._values["virtual_gateway_name"] = virtual_gateway_name

    @builtins.property
    def access_log(self) -> typing.Optional[AccessLog]:
        '''Access Logging Configuration for the VirtualGateway.

        :default: - no access logging
        '''
        result = self._values.get("access_log")
        return typing.cast(typing.Optional[AccessLog], result)

    @builtins.property
    def backend_defaults(self) -> typing.Optional[BackendDefaults]:
        '''Default Configuration Virtual Node uses to communicate with Virtual Service.

        :default: - No Config
        '''
        result = self._values.get("backend_defaults")
        return typing.cast(typing.Optional[BackendDefaults], result)

    @builtins.property
    def listeners(self) -> typing.Optional[typing.List["VirtualGatewayListener"]]:
        '''Listeners for the VirtualGateway.

        Only one is supported.

        :default: - Single HTTP listener on port 8080
        '''
        result = self._values.get("listeners")
        return typing.cast(typing.Optional[typing.List["VirtualGatewayListener"]], result)

    @builtins.property
    def virtual_gateway_name(self) -> typing.Optional[builtins.str]:
        '''Name of the VirtualGateway.

        :default: - A name is automatically determined
        '''
        result = self._values.get("virtual_gateway_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualGatewayBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualGatewayListener(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.VirtualGatewayListener",
):
    '''Represents the properties needed to define listeners for a VirtualGateway.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="grpc") # type: ignore[misc]
    @builtins.classmethod
    def grpc(
        cls,
        *,
        connection_pool: typing.Optional[GrpcConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        port: typing.Optional[jsii.Number] = None,
        tls: typing.Optional[ListenerTlsOptions] = None,
    ) -> "VirtualGatewayListener":
        '''Returns a GRPC Listener for a VirtualGateway.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param port: Port to listen for connections on. Default: - 8080
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        options = GrpcGatewayListenerOptions(
            connection_pool=connection_pool,
            health_check=health_check,
            port=port,
            tls=tls,
        )

        return typing.cast("VirtualGatewayListener", jsii.sinvoke(cls, "grpc", [options]))

    @jsii.member(jsii_name="http") # type: ignore[misc]
    @builtins.classmethod
    def http(
        cls,
        *,
        connection_pool: typing.Optional[HttpConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        port: typing.Optional[jsii.Number] = None,
        tls: typing.Optional[ListenerTlsOptions] = None,
    ) -> "VirtualGatewayListener":
        '''Returns an HTTP Listener for a VirtualGateway.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param port: Port to listen for connections on. Default: - 8080
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        options = HttpGatewayListenerOptions(
            connection_pool=connection_pool,
            health_check=health_check,
            port=port,
            tls=tls,
        )

        return typing.cast("VirtualGatewayListener", jsii.sinvoke(cls, "http", [options]))

    @jsii.member(jsii_name="http2") # type: ignore[misc]
    @builtins.classmethod
    def http2(
        cls,
        *,
        connection_pool: typing.Optional[Http2ConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        port: typing.Optional[jsii.Number] = None,
        tls: typing.Optional[ListenerTlsOptions] = None,
    ) -> "VirtualGatewayListener":
        '''Returns an HTTP2 Listener for a VirtualGateway.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param port: Port to listen for connections on. Default: - 8080
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        options = Http2GatewayListenerOptions(
            connection_pool=connection_pool,
            health_check=health_check,
            port=port,
            tls=tls,
        )

        return typing.cast("VirtualGatewayListener", jsii.sinvoke(cls, "http2", [options]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "VirtualGatewayListenerConfig":
        '''Called when the GatewayListener type is initialized.

        Can be used to enforce
        mutual exclusivity

        :param scope: -
        '''
        ...


class _VirtualGatewayListenerProxy(VirtualGatewayListener):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "VirtualGatewayListenerConfig":
        '''Called when the GatewayListener type is initialized.

        Can be used to enforce
        mutual exclusivity

        :param scope: -
        '''
        return typing.cast("VirtualGatewayListenerConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, VirtualGatewayListener).__jsii_proxy_class__ = lambda : _VirtualGatewayListenerProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualGatewayListenerConfig",
    jsii_struct_bases=[],
    name_mapping={"listener": "listener"},
)
class VirtualGatewayListenerConfig:
    def __init__(
        self,
        *,
        listener: CfnVirtualGateway.VirtualGatewayListenerProperty,
    ) -> None:
        '''Properties for a VirtualGateway listener.

        :param listener: Single listener config for a VirtualGateway.
        '''
        if isinstance(listener, dict):
            listener = CfnVirtualGateway.VirtualGatewayListenerProperty(**listener)
        self._values: typing.Dict[str, typing.Any] = {
            "listener": listener,
        }

    @builtins.property
    def listener(self) -> CfnVirtualGateway.VirtualGatewayListenerProperty:
        '''Single listener config for a VirtualGateway.'''
        result = self._values.get("listener")
        assert result is not None, "Required property 'listener' is missing"
        return typing.cast(CfnVirtualGateway.VirtualGatewayListenerProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualGatewayListenerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualGatewayProps",
    jsii_struct_bases=[VirtualGatewayBaseProps],
    name_mapping={
        "access_log": "accessLog",
        "backend_defaults": "backendDefaults",
        "listeners": "listeners",
        "virtual_gateway_name": "virtualGatewayName",
        "mesh": "mesh",
    },
)
class VirtualGatewayProps(VirtualGatewayBaseProps):
    def __init__(
        self,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        listeners: typing.Optional[typing.Sequence[VirtualGatewayListener]] = None,
        virtual_gateway_name: typing.Optional[builtins.str] = None,
        mesh: IMesh,
    ) -> None:
        '''Properties used when creating a new VirtualGateway.

        :param access_log: Access Logging Configuration for the VirtualGateway. Default: - no access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param listeners: Listeners for the VirtualGateway. Only one is supported. Default: - Single HTTP listener on port 8080
        :param virtual_gateway_name: Name of the VirtualGateway. Default: - A name is automatically determined
        :param mesh: The Mesh which the VirtualGateway belongs to.
        '''
        if isinstance(backend_defaults, dict):
            backend_defaults = BackendDefaults(**backend_defaults)
        self._values: typing.Dict[str, typing.Any] = {
            "mesh": mesh,
        }
        if access_log is not None:
            self._values["access_log"] = access_log
        if backend_defaults is not None:
            self._values["backend_defaults"] = backend_defaults
        if listeners is not None:
            self._values["listeners"] = listeners
        if virtual_gateway_name is not None:
            self._values["virtual_gateway_name"] = virtual_gateway_name

    @builtins.property
    def access_log(self) -> typing.Optional[AccessLog]:
        '''Access Logging Configuration for the VirtualGateway.

        :default: - no access logging
        '''
        result = self._values.get("access_log")
        return typing.cast(typing.Optional[AccessLog], result)

    @builtins.property
    def backend_defaults(self) -> typing.Optional[BackendDefaults]:
        '''Default Configuration Virtual Node uses to communicate with Virtual Service.

        :default: - No Config
        '''
        result = self._values.get("backend_defaults")
        return typing.cast(typing.Optional[BackendDefaults], result)

    @builtins.property
    def listeners(self) -> typing.Optional[typing.List[VirtualGatewayListener]]:
        '''Listeners for the VirtualGateway.

        Only one is supported.

        :default: - Single HTTP listener on port 8080
        '''
        result = self._values.get("listeners")
        return typing.cast(typing.Optional[typing.List[VirtualGatewayListener]], result)

    @builtins.property
    def virtual_gateway_name(self) -> typing.Optional[builtins.str]:
        '''Name of the VirtualGateway.

        :default: - A name is automatically determined
        '''
        result = self._values.get("virtual_gateway_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualGateway belongs to.'''
        result = self._values.get("mesh")
        assert result is not None, "Required property 'mesh' is missing"
        return typing.cast(IMesh, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IVirtualNode)
class VirtualNode(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.VirtualNode",
):
    '''VirtualNode represents a newly defined AppMesh VirtualNode.

    Any inbound traffic that your virtual node expects should be specified as a
    listener. Any outbound traffic that your virtual node expects to reach
    should be specified as a backend.

    :see: https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        mesh: IMesh,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        backends: typing.Optional[typing.Sequence[Backend]] = None,
        listeners: typing.Optional[typing.Sequence["VirtualNodeListener"]] = None,
        service_discovery: typing.Optional[ServiceDiscovery] = None,
        virtual_node_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param mesh: The Mesh which the VirtualNode belongs to.
        :param access_log: Access Logging Configuration for the virtual node. Default: - No access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param backends: Virtual Services that this is node expected to send outbound traffic to. Default: - No backends
        :param listeners: Initial listener for the virtual node. Default: - No listeners
        :param service_discovery: Defines how upstream clients will discover this VirtualNode. Default: - No Service Discovery
        :param virtual_node_name: The name of the VirtualNode. Default: - A name is automatically determined
        '''
        props = VirtualNodeProps(
            mesh=mesh,
            access_log=access_log,
            backend_defaults=backend_defaults,
            backends=backends,
            listeners=listeners,
            service_discovery=service_discovery,
            virtual_node_name=virtual_node_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromVirtualNodeArn") # type: ignore[misc]
    @builtins.classmethod
    def from_virtual_node_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        virtual_node_arn: builtins.str,
    ) -> IVirtualNode:
        '''Import an existing VirtualNode given an ARN.

        :param scope: -
        :param id: -
        :param virtual_node_arn: -
        '''
        return typing.cast(IVirtualNode, jsii.sinvoke(cls, "fromVirtualNodeArn", [scope, id, virtual_node_arn]))

    @jsii.member(jsii_name="fromVirtualNodeAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_virtual_node_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        mesh: IMesh,
        virtual_node_name: builtins.str,
    ) -> IVirtualNode:
        '''Import an existing VirtualNode given its name.

        :param scope: -
        :param id: -
        :param mesh: The Mesh that the VirtualNode belongs to.
        :param virtual_node_name: The name of the VirtualNode.
        '''
        attrs = VirtualNodeAttributes(mesh=mesh, virtual_node_name=virtual_node_name)

        return typing.cast(IVirtualNode, jsii.sinvoke(cls, "fromVirtualNodeAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addBackend")
    def add_backend(self, backend: Backend) -> None:
        '''Add a Virtual Services that this node is expected to send outbound traffic to.

        :param backend: -
        '''
        return typing.cast(None, jsii.invoke(self, "addBackend", [backend]))

    @jsii.member(jsii_name="addListener")
    def add_listener(self, listener: "VirtualNodeListener") -> None:
        '''Utility method to add an inbound listener for this VirtualNode.

        Note: At this time, Virtual Nodes support at most one listener. Adding
        more than one will result in a failure to deploy the CloudFormation stack.
        However, the App Mesh team has plans to add support for multiple listeners
        on Virtual Nodes and Virtual Routers.

        :param listener: -

        :see: https://github.com/aws/aws-app-mesh-roadmap/issues/120
        '''
        return typing.cast(None, jsii.invoke(self, "addListener", [listener]))

    @jsii.member(jsii_name="grantStreamAggregatedResources")
    def grant_stream_aggregated_resources(
        self,
        identity: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grants the given entity ``appmesh:StreamAggregatedResources``.

        :param identity: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantStreamAggregatedResources", [identity]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualNode belongs to.'''
        return typing.cast(IMesh, jsii.get(self, "mesh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualNodeArn")
    def virtual_node_arn(self) -> builtins.str:
        '''The Amazon Resource Name belonging to the VirtualNode.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualNodeArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualNodeName")
    def virtual_node_name(self) -> builtins.str:
        '''The name of the VirtualNode.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualNodeName"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualNodeAttributes",
    jsii_struct_bases=[],
    name_mapping={"mesh": "mesh", "virtual_node_name": "virtualNodeName"},
)
class VirtualNodeAttributes:
    def __init__(self, *, mesh: IMesh, virtual_node_name: builtins.str) -> None:
        '''Interface with properties necessary to import a reusable VirtualNode.

        :param mesh: The Mesh that the VirtualNode belongs to.
        :param virtual_node_name: The name of the VirtualNode.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh": mesh,
            "virtual_node_name": virtual_node_name,
        }

    @builtins.property
    def mesh(self) -> IMesh:
        '''The Mesh that the VirtualNode belongs to.'''
        result = self._values.get("mesh")
        assert result is not None, "Required property 'mesh' is missing"
        return typing.cast(IMesh, result)

    @builtins.property
    def virtual_node_name(self) -> builtins.str:
        '''The name of the VirtualNode.'''
        result = self._values.get("virtual_node_name")
        assert result is not None, "Required property 'virtual_node_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNodeAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualNodeBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_log": "accessLog",
        "backend_defaults": "backendDefaults",
        "backends": "backends",
        "listeners": "listeners",
        "service_discovery": "serviceDiscovery",
        "virtual_node_name": "virtualNodeName",
    },
)
class VirtualNodeBaseProps:
    def __init__(
        self,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        backends: typing.Optional[typing.Sequence[Backend]] = None,
        listeners: typing.Optional[typing.Sequence["VirtualNodeListener"]] = None,
        service_discovery: typing.Optional[ServiceDiscovery] = None,
        virtual_node_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Basic configuration properties for a VirtualNode.

        :param access_log: Access Logging Configuration for the virtual node. Default: - No access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param backends: Virtual Services that this is node expected to send outbound traffic to. Default: - No backends
        :param listeners: Initial listener for the virtual node. Default: - No listeners
        :param service_discovery: Defines how upstream clients will discover this VirtualNode. Default: - No Service Discovery
        :param virtual_node_name: The name of the VirtualNode. Default: - A name is automatically determined
        '''
        if isinstance(backend_defaults, dict):
            backend_defaults = BackendDefaults(**backend_defaults)
        self._values: typing.Dict[str, typing.Any] = {}
        if access_log is not None:
            self._values["access_log"] = access_log
        if backend_defaults is not None:
            self._values["backend_defaults"] = backend_defaults
        if backends is not None:
            self._values["backends"] = backends
        if listeners is not None:
            self._values["listeners"] = listeners
        if service_discovery is not None:
            self._values["service_discovery"] = service_discovery
        if virtual_node_name is not None:
            self._values["virtual_node_name"] = virtual_node_name

    @builtins.property
    def access_log(self) -> typing.Optional[AccessLog]:
        '''Access Logging Configuration for the virtual node.

        :default: - No access logging
        '''
        result = self._values.get("access_log")
        return typing.cast(typing.Optional[AccessLog], result)

    @builtins.property
    def backend_defaults(self) -> typing.Optional[BackendDefaults]:
        '''Default Configuration Virtual Node uses to communicate with Virtual Service.

        :default: - No Config
        '''
        result = self._values.get("backend_defaults")
        return typing.cast(typing.Optional[BackendDefaults], result)

    @builtins.property
    def backends(self) -> typing.Optional[typing.List[Backend]]:
        '''Virtual Services that this is node expected to send outbound traffic to.

        :default: - No backends
        '''
        result = self._values.get("backends")
        return typing.cast(typing.Optional[typing.List[Backend]], result)

    @builtins.property
    def listeners(self) -> typing.Optional[typing.List["VirtualNodeListener"]]:
        '''Initial listener for the virtual node.

        :default: - No listeners
        '''
        result = self._values.get("listeners")
        return typing.cast(typing.Optional[typing.List["VirtualNodeListener"]], result)

    @builtins.property
    def service_discovery(self) -> typing.Optional[ServiceDiscovery]:
        '''Defines how upstream clients will discover this VirtualNode.

        :default: - No Service Discovery
        '''
        result = self._values.get("service_discovery")
        return typing.cast(typing.Optional[ServiceDiscovery], result)

    @builtins.property
    def virtual_node_name(self) -> typing.Optional[builtins.str]:
        '''The name of the VirtualNode.

        :default: - A name is automatically determined
        '''
        result = self._values.get("virtual_node_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNodeBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNodeListener(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.VirtualNodeListener",
):
    '''Defines listener for a VirtualNode.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="grpc") # type: ignore[misc]
    @builtins.classmethod
    def grpc(
        cls,
        *,
        connection_pool: typing.Optional[GrpcConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        outlier_detection: typing.Optional[OutlierDetection] = None,
        port: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[GrpcTimeout] = None,
        tls: typing.Optional[ListenerTlsOptions] = None,
    ) -> "VirtualNodeListener":
        '''Returns an GRPC Listener for a VirtualNode.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param outlier_detection: Represents the configuration for enabling outlier detection. Default: - none
        :param port: Port to listen for connections on. Default: - 8080
        :param timeout: Timeout for GRPC protocol. Default: - None
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        props = GrpcVirtualNodeListenerOptions(
            connection_pool=connection_pool,
            health_check=health_check,
            outlier_detection=outlier_detection,
            port=port,
            timeout=timeout,
            tls=tls,
        )

        return typing.cast("VirtualNodeListener", jsii.sinvoke(cls, "grpc", [props]))

    @jsii.member(jsii_name="http") # type: ignore[misc]
    @builtins.classmethod
    def http(
        cls,
        *,
        connection_pool: typing.Optional[HttpConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        outlier_detection: typing.Optional[OutlierDetection] = None,
        port: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[HttpTimeout] = None,
        tls: typing.Optional[ListenerTlsOptions] = None,
    ) -> "VirtualNodeListener":
        '''Returns an HTTP Listener for a VirtualNode.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param outlier_detection: Represents the configuration for enabling outlier detection. Default: - none
        :param port: Port to listen for connections on. Default: - 8080
        :param timeout: Timeout for HTTP protocol. Default: - None
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        props = HttpVirtualNodeListenerOptions(
            connection_pool=connection_pool,
            health_check=health_check,
            outlier_detection=outlier_detection,
            port=port,
            timeout=timeout,
            tls=tls,
        )

        return typing.cast("VirtualNodeListener", jsii.sinvoke(cls, "http", [props]))

    @jsii.member(jsii_name="http2") # type: ignore[misc]
    @builtins.classmethod
    def http2(
        cls,
        *,
        connection_pool: typing.Optional[Http2ConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        outlier_detection: typing.Optional[OutlierDetection] = None,
        port: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[HttpTimeout] = None,
        tls: typing.Optional[ListenerTlsOptions] = None,
    ) -> "VirtualNodeListener":
        '''Returns an HTTP2 Listener for a VirtualNode.

        :param connection_pool: Connection pool for http2 listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param outlier_detection: Represents the configuration for enabling outlier detection. Default: - none
        :param port: Port to listen for connections on. Default: - 8080
        :param timeout: Timeout for HTTP protocol. Default: - None
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        props = Http2VirtualNodeListenerOptions(
            connection_pool=connection_pool,
            health_check=health_check,
            outlier_detection=outlier_detection,
            port=port,
            timeout=timeout,
            tls=tls,
        )

        return typing.cast("VirtualNodeListener", jsii.sinvoke(cls, "http2", [props]))

    @jsii.member(jsii_name="tcp") # type: ignore[misc]
    @builtins.classmethod
    def tcp(
        cls,
        *,
        connection_pool: typing.Optional[TcpConnectionPool] = None,
        health_check: typing.Optional[HealthCheck] = None,
        outlier_detection: typing.Optional[OutlierDetection] = None,
        port: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[TcpTimeout] = None,
        tls: typing.Optional[ListenerTlsOptions] = None,
    ) -> "VirtualNodeListener":
        '''Returns an TCP Listener for a VirtualNode.

        :param connection_pool: Connection pool for http listeners. Default: - None
        :param health_check: The health check information for the listener. Default: - no healthcheck
        :param outlier_detection: Represents the configuration for enabling outlier detection. Default: - none
        :param port: Port to listen for connections on. Default: - 8080
        :param timeout: Timeout for TCP protocol. Default: - None
        :param tls: Represents the configuration for enabling TLS on a listener. Default: - none
        '''
        props = TcpVirtualNodeListenerOptions(
            connection_pool=connection_pool,
            health_check=health_check,
            outlier_detection=outlier_detection,
            port=port,
            timeout=timeout,
            tls=tls,
        )

        return typing.cast("VirtualNodeListener", jsii.sinvoke(cls, "tcp", [props]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "VirtualNodeListenerConfig":
        '''Binds the current object when adding Listener to a VirtualNode.

        :param scope: -
        '''
        ...


class _VirtualNodeListenerProxy(VirtualNodeListener):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "VirtualNodeListenerConfig":
        '''Binds the current object when adding Listener to a VirtualNode.

        :param scope: -
        '''
        return typing.cast("VirtualNodeListenerConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, VirtualNodeListener).__jsii_proxy_class__ = lambda : _VirtualNodeListenerProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualNodeListenerConfig",
    jsii_struct_bases=[],
    name_mapping={"listener": "listener"},
)
class VirtualNodeListenerConfig:
    def __init__(self, *, listener: CfnVirtualNode.ListenerProperty) -> None:
        '''Properties for a VirtualNode listener.

        :param listener: Single listener config for a VirtualNode.
        '''
        if isinstance(listener, dict):
            listener = CfnVirtualNode.ListenerProperty(**listener)
        self._values: typing.Dict[str, typing.Any] = {
            "listener": listener,
        }

    @builtins.property
    def listener(self) -> CfnVirtualNode.ListenerProperty:
        '''Single listener config for a VirtualNode.'''
        result = self._values.get("listener")
        assert result is not None, "Required property 'listener' is missing"
        return typing.cast(CfnVirtualNode.ListenerProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNodeListenerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualNodeProps",
    jsii_struct_bases=[VirtualNodeBaseProps],
    name_mapping={
        "access_log": "accessLog",
        "backend_defaults": "backendDefaults",
        "backends": "backends",
        "listeners": "listeners",
        "service_discovery": "serviceDiscovery",
        "virtual_node_name": "virtualNodeName",
        "mesh": "mesh",
    },
)
class VirtualNodeProps(VirtualNodeBaseProps):
    def __init__(
        self,
        *,
        access_log: typing.Optional[AccessLog] = None,
        backend_defaults: typing.Optional[BackendDefaults] = None,
        backends: typing.Optional[typing.Sequence[Backend]] = None,
        listeners: typing.Optional[typing.Sequence[VirtualNodeListener]] = None,
        service_discovery: typing.Optional[ServiceDiscovery] = None,
        virtual_node_name: typing.Optional[builtins.str] = None,
        mesh: IMesh,
    ) -> None:
        '''The properties used when creating a new VirtualNode.

        :param access_log: Access Logging Configuration for the virtual node. Default: - No access logging
        :param backend_defaults: Default Configuration Virtual Node uses to communicate with Virtual Service. Default: - No Config
        :param backends: Virtual Services that this is node expected to send outbound traffic to. Default: - No backends
        :param listeners: Initial listener for the virtual node. Default: - No listeners
        :param service_discovery: Defines how upstream clients will discover this VirtualNode. Default: - No Service Discovery
        :param virtual_node_name: The name of the VirtualNode. Default: - A name is automatically determined
        :param mesh: The Mesh which the VirtualNode belongs to.
        '''
        if isinstance(backend_defaults, dict):
            backend_defaults = BackendDefaults(**backend_defaults)
        self._values: typing.Dict[str, typing.Any] = {
            "mesh": mesh,
        }
        if access_log is not None:
            self._values["access_log"] = access_log
        if backend_defaults is not None:
            self._values["backend_defaults"] = backend_defaults
        if backends is not None:
            self._values["backends"] = backends
        if listeners is not None:
            self._values["listeners"] = listeners
        if service_discovery is not None:
            self._values["service_discovery"] = service_discovery
        if virtual_node_name is not None:
            self._values["virtual_node_name"] = virtual_node_name

    @builtins.property
    def access_log(self) -> typing.Optional[AccessLog]:
        '''Access Logging Configuration for the virtual node.

        :default: - No access logging
        '''
        result = self._values.get("access_log")
        return typing.cast(typing.Optional[AccessLog], result)

    @builtins.property
    def backend_defaults(self) -> typing.Optional[BackendDefaults]:
        '''Default Configuration Virtual Node uses to communicate with Virtual Service.

        :default: - No Config
        '''
        result = self._values.get("backend_defaults")
        return typing.cast(typing.Optional[BackendDefaults], result)

    @builtins.property
    def backends(self) -> typing.Optional[typing.List[Backend]]:
        '''Virtual Services that this is node expected to send outbound traffic to.

        :default: - No backends
        '''
        result = self._values.get("backends")
        return typing.cast(typing.Optional[typing.List[Backend]], result)

    @builtins.property
    def listeners(self) -> typing.Optional[typing.List[VirtualNodeListener]]:
        '''Initial listener for the virtual node.

        :default: - No listeners
        '''
        result = self._values.get("listeners")
        return typing.cast(typing.Optional[typing.List[VirtualNodeListener]], result)

    @builtins.property
    def service_discovery(self) -> typing.Optional[ServiceDiscovery]:
        '''Defines how upstream clients will discover this VirtualNode.

        :default: - No Service Discovery
        '''
        result = self._values.get("service_discovery")
        return typing.cast(typing.Optional[ServiceDiscovery], result)

    @builtins.property
    def virtual_node_name(self) -> typing.Optional[builtins.str]:
        '''The name of the VirtualNode.

        :default: - A name is automatically determined
        '''
        result = self._values.get("virtual_node_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualNode belongs to.'''
        result = self._values.get("mesh")
        assert result is not None, "Required property 'mesh' is missing"
        return typing.cast(IMesh, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNodeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IVirtualRouter)
class VirtualRouter(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.VirtualRouter",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        mesh: IMesh,
        listeners: typing.Optional[typing.Sequence["VirtualRouterListener"]] = None,
        virtual_router_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param mesh: The Mesh which the VirtualRouter belongs to.
        :param listeners: Listener specification for the VirtualRouter. Default: - A listener on HTTP port 8080
        :param virtual_router_name: The name of the VirtualRouter. Default: - A name is automatically determined
        '''
        props = VirtualRouterProps(
            mesh=mesh, listeners=listeners, virtual_router_name=virtual_router_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromVirtualRouterArn") # type: ignore[misc]
    @builtins.classmethod
    def from_virtual_router_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        virtual_router_arn: builtins.str,
    ) -> IVirtualRouter:
        '''Import an existing VirtualRouter given an ARN.

        :param scope: -
        :param id: -
        :param virtual_router_arn: -
        '''
        return typing.cast(IVirtualRouter, jsii.sinvoke(cls, "fromVirtualRouterArn", [scope, id, virtual_router_arn]))

    @jsii.member(jsii_name="fromVirtualRouterAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_virtual_router_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        mesh: IMesh,
        virtual_router_name: builtins.str,
    ) -> IVirtualRouter:
        '''Import an existing VirtualRouter given attributes.

        :param scope: -
        :param id: -
        :param mesh: The Mesh which the VirtualRouter belongs to.
        :param virtual_router_name: The name of the VirtualRouter.
        '''
        attrs = VirtualRouterAttributes(
            mesh=mesh, virtual_router_name=virtual_router_name
        )

        return typing.cast(IVirtualRouter, jsii.sinvoke(cls, "fromVirtualRouterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addRoute")
    def add_route(
        self,
        id: builtins.str,
        *,
        route_spec: RouteSpec,
        route_name: typing.Optional[builtins.str] = None,
    ) -> Route:
        '''Add a single route to the router.

        :param id: -
        :param route_spec: Protocol specific spec.
        :param route_name: The name of the route. Default: - An automatically generated name
        '''
        props = RouteBaseProps(route_spec=route_spec, route_name=route_name)

        return typing.cast(Route, jsii.invoke(self, "addRoute", [id, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualRouter belongs to.'''
        return typing.cast(IMesh, jsii.get(self, "mesh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouterArn")
    def virtual_router_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the VirtualRouter.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualRouterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualRouterName")
    def virtual_router_name(self) -> builtins.str:
        '''The name of the VirtualRouter.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualRouterName"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualRouterAttributes",
    jsii_struct_bases=[],
    name_mapping={"mesh": "mesh", "virtual_router_name": "virtualRouterName"},
)
class VirtualRouterAttributes:
    def __init__(self, *, mesh: IMesh, virtual_router_name: builtins.str) -> None:
        '''Interface with properties ncecessary to import a reusable VirtualRouter.

        :param mesh: The Mesh which the VirtualRouter belongs to.
        :param virtual_router_name: The name of the VirtualRouter.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh": mesh,
            "virtual_router_name": virtual_router_name,
        }

    @builtins.property
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualRouter belongs to.'''
        result = self._values.get("mesh")
        assert result is not None, "Required property 'mesh' is missing"
        return typing.cast(IMesh, result)

    @builtins.property
    def virtual_router_name(self) -> builtins.str:
        '''The name of the VirtualRouter.'''
        result = self._values.get("virtual_router_name")
        assert result is not None, "Required property 'virtual_router_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualRouterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualRouterBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "listeners": "listeners",
        "virtual_router_name": "virtualRouterName",
    },
)
class VirtualRouterBaseProps:
    def __init__(
        self,
        *,
        listeners: typing.Optional[typing.Sequence["VirtualRouterListener"]] = None,
        virtual_router_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Interface with base properties all routers willl inherit.

        :param listeners: Listener specification for the VirtualRouter. Default: - A listener on HTTP port 8080
        :param virtual_router_name: The name of the VirtualRouter. Default: - A name is automatically determined
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if listeners is not None:
            self._values["listeners"] = listeners
        if virtual_router_name is not None:
            self._values["virtual_router_name"] = virtual_router_name

    @builtins.property
    def listeners(self) -> typing.Optional[typing.List["VirtualRouterListener"]]:
        '''Listener specification for the VirtualRouter.

        :default: - A listener on HTTP port 8080
        '''
        result = self._values.get("listeners")
        return typing.cast(typing.Optional[typing.List["VirtualRouterListener"]], result)

    @builtins.property
    def virtual_router_name(self) -> typing.Optional[builtins.str]:
        '''The name of the VirtualRouter.

        :default: - A name is automatically determined
        '''
        result = self._values.get("virtual_router_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualRouterBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualRouterListener(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.VirtualRouterListener",
):
    '''Represents the properties needed to define listeners for a VirtualRouter.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="grpc") # type: ignore[misc]
    @builtins.classmethod
    def grpc(cls, port: typing.Optional[jsii.Number] = None) -> "VirtualRouterListener":
        '''Returns a GRPC Listener for a VirtualRouter.

        :param port: the optional port of the listener, 8080 by default.
        '''
        return typing.cast("VirtualRouterListener", jsii.sinvoke(cls, "grpc", [port]))

    @jsii.member(jsii_name="http") # type: ignore[misc]
    @builtins.classmethod
    def http(cls, port: typing.Optional[jsii.Number] = None) -> "VirtualRouterListener":
        '''Returns an HTTP Listener for a VirtualRouter.

        :param port: the optional port of the listener, 8080 by default.
        '''
        return typing.cast("VirtualRouterListener", jsii.sinvoke(cls, "http", [port]))

    @jsii.member(jsii_name="http2") # type: ignore[misc]
    @builtins.classmethod
    def http2(
        cls,
        port: typing.Optional[jsii.Number] = None,
    ) -> "VirtualRouterListener":
        '''Returns an HTTP2 Listener for a VirtualRouter.

        :param port: the optional port of the listener, 8080 by default.
        '''
        return typing.cast("VirtualRouterListener", jsii.sinvoke(cls, "http2", [port]))

    @jsii.member(jsii_name="tcp") # type: ignore[misc]
    @builtins.classmethod
    def tcp(cls, port: typing.Optional[jsii.Number] = None) -> "VirtualRouterListener":
        '''Returns a TCP Listener for a VirtualRouter.

        :param port: the optional port of the listener, 8080 by default.
        '''
        return typing.cast("VirtualRouterListener", jsii.sinvoke(cls, "tcp", [port]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: aws_cdk.core.Construct) -> "VirtualRouterListenerConfig":
        '''Called when the VirtualRouterListener type is initialized.

        Can be used to enforce
        mutual exclusivity

        :param scope: -
        '''
        ...


class _VirtualRouterListenerProxy(VirtualRouterListener):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct) -> "VirtualRouterListenerConfig":
        '''Called when the VirtualRouterListener type is initialized.

        Can be used to enforce
        mutual exclusivity

        :param scope: -
        '''
        return typing.cast("VirtualRouterListenerConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, VirtualRouterListener).__jsii_proxy_class__ = lambda : _VirtualRouterListenerProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualRouterListenerConfig",
    jsii_struct_bases=[],
    name_mapping={"listener": "listener"},
)
class VirtualRouterListenerConfig:
    def __init__(
        self,
        *,
        listener: CfnVirtualRouter.VirtualRouterListenerProperty,
    ) -> None:
        '''Properties for a VirtualRouter listener.

        :param listener: Single listener config for a VirtualRouter.
        '''
        if isinstance(listener, dict):
            listener = CfnVirtualRouter.VirtualRouterListenerProperty(**listener)
        self._values: typing.Dict[str, typing.Any] = {
            "listener": listener,
        }

    @builtins.property
    def listener(self) -> CfnVirtualRouter.VirtualRouterListenerProperty:
        '''Single listener config for a VirtualRouter.'''
        result = self._values.get("listener")
        assert result is not None, "Required property 'listener' is missing"
        return typing.cast(CfnVirtualRouter.VirtualRouterListenerProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualRouterListenerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualRouterProps",
    jsii_struct_bases=[VirtualRouterBaseProps],
    name_mapping={
        "listeners": "listeners",
        "virtual_router_name": "virtualRouterName",
        "mesh": "mesh",
    },
)
class VirtualRouterProps(VirtualRouterBaseProps):
    def __init__(
        self,
        *,
        listeners: typing.Optional[typing.Sequence[VirtualRouterListener]] = None,
        virtual_router_name: typing.Optional[builtins.str] = None,
        mesh: IMesh,
    ) -> None:
        '''The properties used when creating a new VirtualRouter.

        :param listeners: Listener specification for the VirtualRouter. Default: - A listener on HTTP port 8080
        :param virtual_router_name: The name of the VirtualRouter. Default: - A name is automatically determined
        :param mesh: The Mesh which the VirtualRouter belongs to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh": mesh,
        }
        if listeners is not None:
            self._values["listeners"] = listeners
        if virtual_router_name is not None:
            self._values["virtual_router_name"] = virtual_router_name

    @builtins.property
    def listeners(self) -> typing.Optional[typing.List[VirtualRouterListener]]:
        '''Listener specification for the VirtualRouter.

        :default: - A listener on HTTP port 8080
        '''
        result = self._values.get("listeners")
        return typing.cast(typing.Optional[typing.List[VirtualRouterListener]], result)

    @builtins.property
    def virtual_router_name(self) -> typing.Optional[builtins.str]:
        '''The name of the VirtualRouter.

        :default: - A name is automatically determined
        '''
        result = self._values.get("virtual_router_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualRouter belongs to.'''
        result = self._values.get("mesh")
        assert result is not None, "Required property 'mesh' is missing"
        return typing.cast(IMesh, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualRouterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IVirtualService)
class VirtualService(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.VirtualService",
):
    '''VirtualService represents a service inside an AppMesh.

    It routes traffic either to a Virtual Node or to a Virtual Router.

    :see: https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        virtual_service_provider: "VirtualServiceProvider",
        virtual_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param virtual_service_provider: The VirtualNode or VirtualRouter which the VirtualService uses as its provider.
        :param virtual_service_name: The name of the VirtualService. It is recommended this follows the fully-qualified domain name format, such as "my-service.default.svc.cluster.local". Default: - A name is automatically generated
        '''
        props = VirtualServiceProps(
            virtual_service_provider=virtual_service_provider,
            virtual_service_name=virtual_service_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromVirtualServiceArn") # type: ignore[misc]
    @builtins.classmethod
    def from_virtual_service_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        virtual_service_arn: builtins.str,
    ) -> IVirtualService:
        '''Import an existing VirtualService given an ARN.

        :param scope: -
        :param id: -
        :param virtual_service_arn: -
        '''
        return typing.cast(IVirtualService, jsii.sinvoke(cls, "fromVirtualServiceArn", [scope, id, virtual_service_arn]))

    @jsii.member(jsii_name="fromVirtualServiceAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_virtual_service_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        mesh: IMesh,
        virtual_service_name: builtins.str,
    ) -> IVirtualService:
        '''Import an existing VirtualService given its attributes.

        :param scope: -
        :param id: -
        :param mesh: The Mesh which the VirtualService belongs to.
        :param virtual_service_name: The name of the VirtualService, it is recommended this follows the fully-qualified domain name format.
        '''
        attrs = VirtualServiceAttributes(
            mesh=mesh, virtual_service_name=virtual_service_name
        )

        return typing.cast(IVirtualService, jsii.sinvoke(cls, "fromVirtualServiceAttributes", [scope, id, attrs]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mesh")
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualService belongs to.'''
        return typing.cast(IMesh, jsii.get(self, "mesh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualServiceArn")
    def virtual_service_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the virtual service.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualServiceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualServiceName")
    def virtual_service_name(self) -> builtins.str:
        '''The name of the VirtualService, it is recommended this follows the fully-qualified domain name format.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualServiceName"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualServiceAttributes",
    jsii_struct_bases=[],
    name_mapping={"mesh": "mesh", "virtual_service_name": "virtualServiceName"},
)
class VirtualServiceAttributes:
    def __init__(self, *, mesh: IMesh, virtual_service_name: builtins.str) -> None:
        '''Interface with properties ncecessary to import a reusable VirtualService.

        :param mesh: The Mesh which the VirtualService belongs to.
        :param virtual_service_name: The name of the VirtualService, it is recommended this follows the fully-qualified domain name format.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mesh": mesh,
            "virtual_service_name": virtual_service_name,
        }

    @builtins.property
    def mesh(self) -> IMesh:
        '''The Mesh which the VirtualService belongs to.'''
        result = self._values.get("mesh")
        assert result is not None, "Required property 'mesh' is missing"
        return typing.cast(IMesh, result)

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''The name of the VirtualService, it is recommended this follows the fully-qualified domain name format.'''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualServiceBackendOptions",
    jsii_struct_bases=[],
    name_mapping={"tls_client_policy": "tlsClientPolicy"},
)
class VirtualServiceBackendOptions:
    def __init__(
        self,
        *,
        tls_client_policy: typing.Optional[TlsClientPolicy] = None,
    ) -> None:
        '''Represents the properties needed to define a Virtual Service backend.

        :param tls_client_policy: TLS properties for Client policy for the backend. Default: - none
        '''
        if isinstance(tls_client_policy, dict):
            tls_client_policy = TlsClientPolicy(**tls_client_policy)
        self._values: typing.Dict[str, typing.Any] = {}
        if tls_client_policy is not None:
            self._values["tls_client_policy"] = tls_client_policy

    @builtins.property
    def tls_client_policy(self) -> typing.Optional[TlsClientPolicy]:
        '''TLS properties for  Client policy for the backend.

        :default: - none
        '''
        result = self._values.get("tls_client_policy")
        return typing.cast(typing.Optional[TlsClientPolicy], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceBackendOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "virtual_service_provider": "virtualServiceProvider",
        "virtual_service_name": "virtualServiceName",
    },
)
class VirtualServiceProps:
    def __init__(
        self,
        *,
        virtual_service_provider: "VirtualServiceProvider",
        virtual_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The properties applied to the VirtualService being defined.

        :param virtual_service_provider: The VirtualNode or VirtualRouter which the VirtualService uses as its provider.
        :param virtual_service_name: The name of the VirtualService. It is recommended this follows the fully-qualified domain name format, such as "my-service.default.svc.cluster.local". Default: - A name is automatically generated
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service_provider": virtual_service_provider,
        }
        if virtual_service_name is not None:
            self._values["virtual_service_name"] = virtual_service_name

    @builtins.property
    def virtual_service_provider(self) -> "VirtualServiceProvider":
        '''The VirtualNode or VirtualRouter which the VirtualService uses as its provider.'''
        result = self._values.get("virtual_service_provider")
        assert result is not None, "Required property 'virtual_service_provider' is missing"
        return typing.cast("VirtualServiceProvider", result)

    @builtins.property
    def virtual_service_name(self) -> typing.Optional[builtins.str]:
        '''The name of the VirtualService.

        It is recommended this follows the fully-qualified domain name format,
        such as "my-service.default.svc.cluster.local".

        :default: - A name is automatically generated

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            service.domain.local
        '''
        result = self._values.get("virtual_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualServiceProvider(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.VirtualServiceProvider",
):
    '''Represents the properties needed to define the provider for a VirtualService.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="none") # type: ignore[misc]
    @builtins.classmethod
    def none(cls, mesh: IMesh) -> "VirtualServiceProvider":
        '''Returns an Empty Provider for a VirtualService.

        This provides no routing capabilities
        and should only be used as a placeholder

        :param mesh: -
        '''
        return typing.cast("VirtualServiceProvider", jsii.sinvoke(cls, "none", [mesh]))

    @jsii.member(jsii_name="virtualNode") # type: ignore[misc]
    @builtins.classmethod
    def virtual_node(cls, virtual_node: IVirtualNode) -> "VirtualServiceProvider":
        '''Returns a VirtualNode based Provider for a VirtualService.

        :param virtual_node: -
        '''
        return typing.cast("VirtualServiceProvider", jsii.sinvoke(cls, "virtualNode", [virtual_node]))

    @jsii.member(jsii_name="virtualRouter") # type: ignore[misc]
    @builtins.classmethod
    def virtual_router(cls, virtual_router: IVirtualRouter) -> "VirtualServiceProvider":
        '''Returns a VirtualRouter based Provider for a VirtualService.

        :param virtual_router: -
        '''
        return typing.cast("VirtualServiceProvider", jsii.sinvoke(cls, "virtualRouter", [virtual_router]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, _construct: constructs.Construct) -> "VirtualServiceProviderConfig":
        '''Enforces mutual exclusivity for VirtualService provider types.

        :param _construct: -
        '''
        ...


class _VirtualServiceProviderProxy(VirtualServiceProvider):
    @jsii.member(jsii_name="bind")
    def bind(self, _construct: constructs.Construct) -> "VirtualServiceProviderConfig":
        '''Enforces mutual exclusivity for VirtualService provider types.

        :param _construct: -
        '''
        return typing.cast("VirtualServiceProviderConfig", jsii.invoke(self, "bind", [_construct]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, VirtualServiceProvider).__jsii_proxy_class__ = lambda : _VirtualServiceProviderProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.VirtualServiceProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "mesh": "mesh",
        "virtual_node_provider": "virtualNodeProvider",
        "virtual_router_provider": "virtualRouterProvider",
    },
)
class VirtualServiceProviderConfig:
    def __init__(
        self,
        *,
        mesh: IMesh,
        virtual_node_provider: typing.Optional[CfnVirtualService.VirtualNodeServiceProviderProperty] = None,
        virtual_router_provider: typing.Optional[CfnVirtualService.VirtualRouterServiceProviderProperty] = None,
    ) -> None:
        '''Properties for a VirtualService provider.

        :param mesh: Mesh the Provider is using. Default: - none
        :param virtual_node_provider: Virtual Node based provider. Default: - none
        :param virtual_router_provider: Virtual Router based provider. Default: - none
        '''
        if isinstance(virtual_node_provider, dict):
            virtual_node_provider = CfnVirtualService.VirtualNodeServiceProviderProperty(**virtual_node_provider)
        if isinstance(virtual_router_provider, dict):
            virtual_router_provider = CfnVirtualService.VirtualRouterServiceProviderProperty(**virtual_router_provider)
        self._values: typing.Dict[str, typing.Any] = {
            "mesh": mesh,
        }
        if virtual_node_provider is not None:
            self._values["virtual_node_provider"] = virtual_node_provider
        if virtual_router_provider is not None:
            self._values["virtual_router_provider"] = virtual_router_provider

    @builtins.property
    def mesh(self) -> IMesh:
        '''Mesh the Provider is using.

        :default: - none
        '''
        result = self._values.get("mesh")
        assert result is not None, "Required property 'mesh' is missing"
        return typing.cast(IMesh, result)

    @builtins.property
    def virtual_node_provider(
        self,
    ) -> typing.Optional[CfnVirtualService.VirtualNodeServiceProviderProperty]:
        '''Virtual Node based provider.

        :default: - none
        '''
        result = self._values.get("virtual_node_provider")
        return typing.cast(typing.Optional[CfnVirtualService.VirtualNodeServiceProviderProperty], result)

    @builtins.property
    def virtual_router_provider(
        self,
    ) -> typing.Optional[CfnVirtualService.VirtualRouterServiceProviderProperty]:
        '''Virtual Router based provider.

        :default: - none
        '''
        result = self._values.get("virtual_router_provider")
        return typing.cast(typing.Optional[CfnVirtualService.VirtualRouterServiceProviderProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.WeightedTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_node": "virtualNode", "weight": "weight"},
)
class WeightedTarget:
    def __init__(
        self,
        *,
        virtual_node: IVirtualNode,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for the Weighted Targets in the route.

        :param virtual_node: The VirtualNode the route points to.
        :param weight: The weight for the target. Default: 1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_node": virtual_node,
        }
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def virtual_node(self) -> IVirtualNode:
        '''The VirtualNode the route points to.'''
        result = self._values.get("virtual_node")
        assert result is not None, "Required property 'virtual_node' is missing"
        return typing.cast(IVirtualNode, result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''The weight for the target.

        :default: 1
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WeightedTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IGatewayRoute)
class GatewayRoute(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appmesh.GatewayRoute",
):
    '''GatewayRoute represents a new or existing gateway route attached to a VirtualGateway and Mesh.

    :see: https://docs.aws.amazon.com/app-mesh/latest/userguide/gateway-routes.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        virtual_gateway: IVirtualGateway,
        route_spec: GatewayRouteSpec,
        gateway_route_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param virtual_gateway: The VirtualGateway this GatewayRoute is associated with.
        :param route_spec: What protocol the route uses.
        :param gateway_route_name: The name of the GatewayRoute. Default: - an automatically generated name
        '''
        props = GatewayRouteProps(
            virtual_gateway=virtual_gateway,
            route_spec=route_spec,
            gateway_route_name=gateway_route_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromGatewayRouteArn") # type: ignore[misc]
    @builtins.classmethod
    def from_gateway_route_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        gateway_route_arn: builtins.str,
    ) -> IGatewayRoute:
        '''Import an existing GatewayRoute given an ARN.

        :param scope: -
        :param id: -
        :param gateway_route_arn: -
        '''
        return typing.cast(IGatewayRoute, jsii.sinvoke(cls, "fromGatewayRouteArn", [scope, id, gateway_route_arn]))

    @jsii.member(jsii_name="fromGatewayRouteAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_gateway_route_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        gateway_route_name: builtins.str,
        virtual_gateway: IVirtualGateway,
    ) -> IGatewayRoute:
        '''Import an existing GatewayRoute given attributes.

        :param scope: -
        :param id: -
        :param gateway_route_name: The name of the GatewayRoute.
        :param virtual_gateway: The VirtualGateway this GatewayRoute is associated with.
        '''
        attrs = GatewayRouteAttributes(
            gateway_route_name=gateway_route_name, virtual_gateway=virtual_gateway
        )

        return typing.cast(IGatewayRoute, jsii.sinvoke(cls, "fromGatewayRouteAttributes", [scope, id, attrs]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayRouteArn")
    def gateway_route_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the GatewayRoute.'''
        return typing.cast(builtins.str, jsii.get(self, "gatewayRouteArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayRouteName")
    def gateway_route_name(self) -> builtins.str:
        '''The name of the GatewayRoute.'''
        return typing.cast(builtins.str, jsii.get(self, "gatewayRouteName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualGateway")
    def virtual_gateway(self) -> IVirtualGateway:
        '''The VirtualGateway this GatewayRoute is a part of.'''
        return typing.cast(IVirtualGateway, jsii.get(self, "virtualGateway"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcRetryPolicy",
    jsii_struct_bases=[HttpRetryPolicy],
    name_mapping={
        "retry_attempts": "retryAttempts",
        "retry_timeout": "retryTimeout",
        "http_retry_events": "httpRetryEvents",
        "tcp_retry_events": "tcpRetryEvents",
        "grpc_retry_events": "grpcRetryEvents",
    },
)
class GrpcRetryPolicy(HttpRetryPolicy):
    def __init__(
        self,
        *,
        retry_attempts: jsii.Number,
        retry_timeout: aws_cdk.core.Duration,
        http_retry_events: typing.Optional[typing.Sequence[HttpRetryEvent]] = None,
        tcp_retry_events: typing.Optional[typing.Sequence[TcpRetryEvent]] = None,
        grpc_retry_events: typing.Optional[typing.Sequence[GrpcRetryEvent]] = None,
    ) -> None:
        '''gRPC retry policy.

        :param retry_attempts: The maximum number of retry attempts.
        :param retry_timeout: The timeout for each retry attempt.
        :param http_retry_events: Specify HTTP events on which to retry. You must specify at least one value for at least one types of retry events. Default: - no retries for http events
        :param tcp_retry_events: TCP events on which to retry. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable. You must specify at least one value for at least one types of retry events. Default: - no retries for tcp events
        :param grpc_retry_events: gRPC events on which to retry. You must specify at least one value for at least one types of retry events. Default: - no retries for gRPC events
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "retry_attempts": retry_attempts,
            "retry_timeout": retry_timeout,
        }
        if http_retry_events is not None:
            self._values["http_retry_events"] = http_retry_events
        if tcp_retry_events is not None:
            self._values["tcp_retry_events"] = tcp_retry_events
        if grpc_retry_events is not None:
            self._values["grpc_retry_events"] = grpc_retry_events

    @builtins.property
    def retry_attempts(self) -> jsii.Number:
        '''The maximum number of retry attempts.'''
        result = self._values.get("retry_attempts")
        assert result is not None, "Required property 'retry_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def retry_timeout(self) -> aws_cdk.core.Duration:
        '''The timeout for each retry attempt.'''
        result = self._values.get("retry_timeout")
        assert result is not None, "Required property 'retry_timeout' is missing"
        return typing.cast(aws_cdk.core.Duration, result)

    @builtins.property
    def http_retry_events(self) -> typing.Optional[typing.List[HttpRetryEvent]]:
        '''Specify HTTP events on which to retry.

        You must specify at least one value
        for at least one types of retry events.

        :default: - no retries for http events
        '''
        result = self._values.get("http_retry_events")
        return typing.cast(typing.Optional[typing.List[HttpRetryEvent]], result)

    @builtins.property
    def tcp_retry_events(self) -> typing.Optional[typing.List[TcpRetryEvent]]:
        '''TCP events on which to retry.

        The event occurs before any processing of a
        request has started and is encountered when the upstream is temporarily or
        permanently unavailable. You must specify at least one value for at least
        one types of retry events.

        :default: - no retries for tcp events
        '''
        result = self._values.get("tcp_retry_events")
        return typing.cast(typing.Optional[typing.List[TcpRetryEvent]], result)

    @builtins.property
    def grpc_retry_events(self) -> typing.Optional[typing.List[GrpcRetryEvent]]:
        '''gRPC events on which to retry.

        You must specify at least one value
        for at least one types of retry events.

        :default: - no retries for gRPC events
        '''
        result = self._values.get("grpc_retry_events")
        return typing.cast(typing.Optional[typing.List[GrpcRetryEvent]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.GrpcRouteSpecOptions",
    jsii_struct_bases=[RouteSpecOptionsBase],
    name_mapping={
        "priority": "priority",
        "match": "match",
        "weighted_targets": "weightedTargets",
        "retry_policy": "retryPolicy",
        "timeout": "timeout",
    },
)
class GrpcRouteSpecOptions(RouteSpecOptionsBase):
    def __init__(
        self,
        *,
        priority: typing.Optional[jsii.Number] = None,
        match: GrpcRouteMatch,
        weighted_targets: typing.Sequence[WeightedTarget],
        retry_policy: typing.Optional[GrpcRetryPolicy] = None,
        timeout: typing.Optional[GrpcTimeout] = None,
    ) -> None:
        '''Properties specific for a GRPC Based Routes.

        :param priority: The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority. Default: - no particular priority
        :param match: The criterion for determining a request match for this Route.
        :param weighted_targets: List of targets that traffic is routed to when a request matches the route.
        :param retry_policy: The retry policy. Default: - no retry policy
        :param timeout: An object that represents a grpc timeout. Default: - None
        '''
        if isinstance(match, dict):
            match = GrpcRouteMatch(**match)
        if isinstance(retry_policy, dict):
            retry_policy = GrpcRetryPolicy(**retry_policy)
        if isinstance(timeout, dict):
            timeout = GrpcTimeout(**timeout)
        self._values: typing.Dict[str, typing.Any] = {
            "match": match,
            "weighted_targets": weighted_targets,
        }
        if priority is not None:
            self._values["priority"] = priority
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority for the route.

        Routes are matched based on the specified
        value, where 0 is the highest priority.

        :default: - no particular priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def match(self) -> GrpcRouteMatch:
        '''The criterion for determining a request match for this Route.'''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast(GrpcRouteMatch, result)

    @builtins.property
    def weighted_targets(self) -> typing.List[WeightedTarget]:
        '''List of targets that traffic is routed to when a request matches the route.'''
        result = self._values.get("weighted_targets")
        assert result is not None, "Required property 'weighted_targets' is missing"
        return typing.cast(typing.List[WeightedTarget], result)

    @builtins.property
    def retry_policy(self) -> typing.Optional[GrpcRetryPolicy]:
        '''The retry policy.

        :default: - no retry policy
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional[GrpcRetryPolicy], result)

    @builtins.property
    def timeout(self) -> typing.Optional[GrpcTimeout]:
        '''An object that represents a grpc timeout.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[GrpcTimeout], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrpcRouteSpecOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appmesh.HttpRouteSpecOptions",
    jsii_struct_bases=[RouteSpecOptionsBase],
    name_mapping={
        "priority": "priority",
        "weighted_targets": "weightedTargets",
        "match": "match",
        "retry_policy": "retryPolicy",
        "timeout": "timeout",
    },
)
class HttpRouteSpecOptions(RouteSpecOptionsBase):
    def __init__(
        self,
        *,
        priority: typing.Optional[jsii.Number] = None,
        weighted_targets: typing.Sequence[WeightedTarget],
        match: typing.Optional[HttpRouteMatch] = None,
        retry_policy: typing.Optional[HttpRetryPolicy] = None,
        timeout: typing.Optional[HttpTimeout] = None,
    ) -> None:
        '''Properties specific for HTTP Based Routes.

        :param priority: The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority. Default: - no particular priority
        :param weighted_targets: List of targets that traffic is routed to when a request matches the route.
        :param match: The criterion for determining a request match for this Route. Default: - matches on '/'
        :param retry_policy: The retry policy. Default: - no retry policy
        :param timeout: An object that represents a http timeout. Default: - None
        '''
        if isinstance(match, dict):
            match = HttpRouteMatch(**match)
        if isinstance(retry_policy, dict):
            retry_policy = HttpRetryPolicy(**retry_policy)
        if isinstance(timeout, dict):
            timeout = HttpTimeout(**timeout)
        self._values: typing.Dict[str, typing.Any] = {
            "weighted_targets": weighted_targets,
        }
        if priority is not None:
            self._values["priority"] = priority
        if match is not None:
            self._values["match"] = match
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority for the route.

        Routes are matched based on the specified
        value, where 0 is the highest priority.

        :default: - no particular priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weighted_targets(self) -> typing.List[WeightedTarget]:
        '''List of targets that traffic is routed to when a request matches the route.'''
        result = self._values.get("weighted_targets")
        assert result is not None, "Required property 'weighted_targets' is missing"
        return typing.cast(typing.List[WeightedTarget], result)

    @builtins.property
    def match(self) -> typing.Optional[HttpRouteMatch]:
        '''The criterion for determining a request match for this Route.

        :default: - matches on '/'
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional[HttpRouteMatch], result)

    @builtins.property
    def retry_policy(self) -> typing.Optional[HttpRetryPolicy]:
        '''The retry policy.

        :default: - no retry policy
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional[HttpRetryPolicy], result)

    @builtins.property
    def timeout(self) -> typing.Optional[HttpTimeout]:
        '''An object that represents a http timeout.

        :default: - None
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[HttpTimeout], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpRouteSpecOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MutualTlsCertificate(
    TlsCertificate,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.MutualTlsCertificate",
):
    '''Represents a TLS certificate that is supported for mutual TLS authentication.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="differentiator")
    def _differentiator(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "differentiator"))


class _MutualTlsCertificateProxy(
    MutualTlsCertificate, jsii.proxy_for(TlsCertificate) # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, MutualTlsCertificate).__jsii_proxy_class__ = lambda : _MutualTlsCertificateProxy


class MutualTlsValidationTrust(
    TlsValidationTrust,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appmesh.MutualTlsValidationTrust",
):
    '''Represents a TLS Validation Context Trust that is supported for mutual TLS authentication.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="differentiator")
    def _differentiator(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "differentiator"))


class _MutualTlsValidationTrustProxy(
    MutualTlsValidationTrust, jsii.proxy_for(TlsValidationTrust) # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, MutualTlsValidationTrust).__jsii_proxy_class__ = lambda : _MutualTlsValidationTrustProxy


__all__ = [
    "AccessLog",
    "AccessLogConfig",
    "Backend",
    "BackendConfig",
    "BackendDefaults",
    "CfnGatewayRoute",
    "CfnGatewayRouteProps",
    "CfnMesh",
    "CfnMeshProps",
    "CfnRoute",
    "CfnRouteProps",
    "CfnVirtualGateway",
    "CfnVirtualGatewayProps",
    "CfnVirtualNode",
    "CfnVirtualNodeProps",
    "CfnVirtualRouter",
    "CfnVirtualRouterProps",
    "CfnVirtualService",
    "CfnVirtualServiceProps",
    "DnsResponseType",
    "GatewayRoute",
    "GatewayRouteAttributes",
    "GatewayRouteBaseProps",
    "GatewayRouteHostnameMatch",
    "GatewayRouteHostnameMatchConfig",
    "GatewayRouteProps",
    "GatewayRouteSpec",
    "GatewayRouteSpecConfig",
    "GrpcConnectionPool",
    "GrpcGatewayListenerOptions",
    "GrpcGatewayRouteMatch",
    "GrpcGatewayRouteSpecOptions",
    "GrpcHealthCheckOptions",
    "GrpcRetryEvent",
    "GrpcRetryPolicy",
    "GrpcRouteMatch",
    "GrpcRouteSpecOptions",
    "GrpcTimeout",
    "GrpcVirtualNodeListenerOptions",
    "HeaderMatch",
    "HeaderMatchConfig",
    "HealthCheck",
    "HealthCheckBindOptions",
    "HealthCheckConfig",
    "Http2ConnectionPool",
    "Http2GatewayListenerOptions",
    "Http2VirtualNodeListenerOptions",
    "HttpConnectionPool",
    "HttpGatewayListenerOptions",
    "HttpGatewayRouteMatch",
    "HttpGatewayRoutePathMatch",
    "HttpGatewayRoutePathMatchConfig",
    "HttpGatewayRouteSpecOptions",
    "HttpHealthCheckOptions",
    "HttpRetryEvent",
    "HttpRetryPolicy",
    "HttpRouteMatch",
    "HttpRouteMethod",
    "HttpRoutePathMatch",
    "HttpRoutePathMatchConfig",
    "HttpRouteProtocol",
    "HttpRouteSpecOptions",
    "HttpTimeout",
    "HttpVirtualNodeListenerOptions",
    "IGatewayRoute",
    "IMesh",
    "IRoute",
    "IVirtualGateway",
    "IVirtualNode",
    "IVirtualRouter",
    "IVirtualService",
    "ListenerTlsOptions",
    "Mesh",
    "MeshFilterType",
    "MeshProps",
    "MutualTlsCertificate",
    "MutualTlsValidation",
    "MutualTlsValidationTrust",
    "OutlierDetection",
    "Protocol",
    "QueryParameterMatch",
    "QueryParameterMatchConfig",
    "Route",
    "RouteAttributes",
    "RouteBaseProps",
    "RouteProps",
    "RouteSpec",
    "RouteSpecConfig",
    "RouteSpecOptionsBase",
    "ServiceDiscovery",
    "ServiceDiscoveryConfig",
    "SubjectAlternativeNames",
    "SubjectAlternativeNamesMatcherConfig",
    "TcpConnectionPool",
    "TcpHealthCheckOptions",
    "TcpRetryEvent",
    "TcpRouteSpecOptions",
    "TcpTimeout",
    "TcpVirtualNodeListenerOptions",
    "TlsCertificate",
    "TlsCertificateConfig",
    "TlsClientPolicy",
    "TlsMode",
    "TlsValidation",
    "TlsValidationTrust",
    "TlsValidationTrustConfig",
    "VirtualGateway",
    "VirtualGatewayAttributes",
    "VirtualGatewayBaseProps",
    "VirtualGatewayListener",
    "VirtualGatewayListenerConfig",
    "VirtualGatewayProps",
    "VirtualNode",
    "VirtualNodeAttributes",
    "VirtualNodeBaseProps",
    "VirtualNodeListener",
    "VirtualNodeListenerConfig",
    "VirtualNodeProps",
    "VirtualRouter",
    "VirtualRouterAttributes",
    "VirtualRouterBaseProps",
    "VirtualRouterListener",
    "VirtualRouterListenerConfig",
    "VirtualRouterProps",
    "VirtualService",
    "VirtualServiceAttributes",
    "VirtualServiceBackendOptions",
    "VirtualServiceProps",
    "VirtualServiceProvider",
    "VirtualServiceProviderConfig",
    "WeightedTarget",
]

publication.publish()
