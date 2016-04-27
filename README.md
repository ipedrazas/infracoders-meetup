# infracoders-meetup

During this talk we will look at the Kuberentes Probes:

* LivenessProbe
* ReadynessProbe

Why and how should we use them.

There are 3 examples:

* Simple `readynessProbe` example with 1 pod and 2 containers: the idea is to highlight that the health check is per container, not per pod (important).
* Microservice B with a dependency to MongoDB and another microservice.
* Third example to illustrate how the `readynessProbe` can help to minimise errors.

