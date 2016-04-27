# infracoders-meetup

During this talk we will look at the [Kuberentes Probes](http://kubernetes.io/docs/user-guide/pod-states/#container-probes):

* LivenessProbe: I'm healthy. **Keep** sending traffic!
* ReadinessProbe: I'm ready. **Start** sending traffic!

Why and how should we use them.

There are 3 examples:

* Simple `readinessProbe` example with 1 pod and 2 containers: the idea is to highlight that the health check is per container, not per pod (important).
* [Microservice B](api-mongo) with a dependency to [MongoDB](mongo) and [another microservice](simple-api).
* [Third example](slow-mongo) to illustrate how the `readinessProbe` can help to minimise errors.



A Probe is a diagnostic performed periodically by the kubelet on a container. Specifically the diagnostic is one of three Handlers:

* ExecAction: executes a specified command inside the container expecting on success that the command exits with status code 0.
* TCPSocketAction: performs a tcp check against **the container’s IP** address on a specified port expecting on success that the port is open.
* HTTPGetAction: performs an HTTP Get against **the container’s IP** address on a specified port and path expecting on success that the response has a status code greater than or equal to 200 and less than 400.
