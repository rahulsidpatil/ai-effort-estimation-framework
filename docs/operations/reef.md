# REEF Operations

## Delivery baseline

REEF is delivered as an OCI container image. Step 0 establishes a portable local runtime,
continuous integration, and release-driven publication; it does not deploy the application to
a shared hosting environment.

Pull requests and changes to `master` run formatting, linting, typing, tests, public-contract
validation, an image build, and a live-container smoke test. Publishing a GitHub release builds
the image for Linux AMD64 and ARM64, publishes semantic-version and commit tags to GitHub
Container Registry, embeds SBOM and provenance metadata, and creates a GitHub artifact
attestation. Stable releases also update `latest`; prereleases do not.

Workflow dependencies are pinned to immutable commit identifiers. Workflow permissions are
read-only by default and elevated only in the release job for package publication and
attestation. Dependabot proposes updates to Python, container, and workflow dependencies.

## Local container workflow

From `reef/`, build and start the service:

```sh
docker compose up --build
```

Open <http://localhost:8000>. The API documentation is at
<http://localhost:8000/api/docs>. The presentation-only UX tour is at
<http://localhost:8000/product-experience>. Stop the service with:

```sh
docker compose down
```

The named `reef-data` volume retains the SQLite database. To remove local data deliberately,
run `docker compose down --volumes`. This is destructive and cannot be undone unless the volume
was backed up.

## Configuration

| Variable | Default in image | Purpose |
| --- | --- | --- |
| `REEF_ENVIRONMENT` | `container` | Runtime environment label shown by the Step 0 UI. |
| `REEF_VERSION` | Image version | Application version reported by the UI and health endpoint. |
| `REEF_LOG_LEVEL` | `INFO` | Python logging level. |
| `REEF_DATA_DIR` | `/data` | Directory used for persistent application data. |
| `REEF_DATABASE_PATH` | `$REEF_DATA_DIR/reef.db` | Optional explicit SQLite database path. |
| `REEF_PORT` | `8000` in Compose | Host port exposed by the local Compose workflow. |

The image runs as UID/GID `10001`, has no shell login, and writes application state only under
`/data`. Logs are structured JSON and intentionally exclude request bodies, query strings,
credentials, prompts, and estimation content.

## Health and recovery

- `GET /healthz` reports whether the application process can serve requests.
- `GET /readyz` verifies that the configured SQLite database exists and can answer a query.
- Container orchestration should remove an instance from service when readiness returns `503`.

SQLite is the reference adapter for local, controlled, single-instance evaluation. Do not run
multiple replicas against the same SQLite file. Back up the mounted `/data` volume before an
upgrade that introduces a documented database migration. External databases, high availability,
authentication, public hosting, and disaster recovery remain outside the Step 0 boundary.

## Release verification

For release `<version>`, pull the published image and verify its GitHub attestation:

```sh
docker pull ghcr.io/rahulsidpatil/ai-effort-estimation-framework/reef:<version>
gh attestation verify \
  oci://ghcr.io/rahulsidpatil/ai-effort-estimation-framework/reef:<version> \
  --repo rahulsidpatil/ai-effort-estimation-framework
```
