# [Spring Cloud](https://spring.io/projects/spring-cloud)  
## Features
- Distributed/versioned configuration
- Service registraion and discovery
- Routing
- Service-to-service calls
- Load balancing
- Circuit Breakers
- Global locks
- Leadership election and cluster state
- Distributed messaging
## Spring Cloud provides tools
- configuration management
- service discovery
- circuit breakers
- intelligent routing
- microproxy
- control bus
- one-time tokens
- leadership election
- distributed sessions
- cluster state
## Main Projects  
### Spring Cloud Config  
> Spring Cloud tools: configuration management  
Spring Cloud Config provides server and client-side support for externalized configuration in a distributed system. With the Config Server you have a central place to manage external properties for applications across all environments. The concepts on both client and server map identically to the Spring ```Environment``` and ```PropertySource``` abstractions, so they fit very well with Spring applications, but can be used with any application running in any language. As an application moves through the deployment pipeline from dev to test and into production you can manage the configuration between those environments and be certain that applications have everything they need to run when they migrate. The default implementation of the server storage backend uses git so it easily supports labelled versions of configuration environments, as well as being accessible to a wide range of tooling for managing the content. It is easy to add alternative implementations and plug them in with Spring configuration.  
> **abstraction** _noun_ the situation in which a subject is very general and not based on real situations.  
### Spring Cloud Gateway  
This project provides a library for building an API Gateway on top of Spring WebFlux. Spring Cloud Gateway aims to provide a simple, yet effective way to route to APIs and provide [cross cutting concerns](https://en.wikipedia.org/wiki/Cross-cutting_concern) to them such as: security, monitoring/metrics, and resiliency.  
> **resilience** _formal_ resiliency _noun_ the ability of a substance to return to its usual shape after being bent, stretched, or pressed.
#### Features
- Built on Spring Framework 5, Project Reactor and Spring Boot 2.0
- Able to match routes on any request attribute.
- Predicates and filters are specific to routes.
- **Circuit Breaker integration.**
- **Spring Cloud DiscoveryClient integration**
- Easy to write Predicates and Filters
- Request Rate Limiting 
- Path Rewriting  
### Spring Cloud Circuit Breaker  
Spring Cloud Circuit breaker provides an abstraction across different circuit breaker implementations. 
It provides a consistent API to use in your applications allowing you the developer to choose the circuit breaker implementation that best fits your needs for your app.
#### Supported Implementations  
- Netfix Hystrix
- Resilience4J
- Sentinel
- Spring Retry
