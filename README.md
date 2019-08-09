# Example Note Taking App for Observability in Practice

This is a WIP repo that will be used to showcase how to use Logs, Traces, Metrics, and Synthetics to debug your production applications.

It (will be) the third iteration of the [Distributed Tracing workshop](https://github.com/burningion/distributed-tracing-with-apm-workshop).

Specifically, in this iteration we'll generate a note taking application, along with authentication, database calls, and distributed tracing.

The idea is, we'll have a (slightly) broken application out of the box, and we'll see how instrumentation via traces and metrics can help us fix applications in the real world.

## Getting Started

Just as the previous repo was built to run in `docker-compose` and Kubernetes, this project will follow the same path.

For now, just a:

```
$ DD_API_KEY=<YOUR_API_KEY> docker-compose up
```

Should get you started. But be warned, nothing is really hooked up just yet.
