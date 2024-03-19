# Twingate Resource Provider

The Twingate Resource Provider lets you manage [Twingate](https://www.twingate.com/) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @twingate/pulumi-twingate
```

or `yarn`:

```bash
yarn add @twingate/pulumi-twingate
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi-twingate
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/pulumi/pulumi-twingate/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumi.Twingate
```

## Configuration

The following configuration points are available for the `twingate` provider:

- `twingate:apiKey` (environment: `twingate_API_KEY`) - the API key for `twingate`
- `twingate:region` (environment: `twingate_REGION`) - the region in which to deploy resources

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/twingate/api-docs/).
