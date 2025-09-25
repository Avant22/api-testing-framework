# 🔄 Regression Strategy

## Approach
- Automated regression runs on every push/PR via GitHub Actions.
- Includes functional, schema, performance, and mocked API tests.

## Scope
- All API endpoints in scope for testing.
- Schema validations for backward compatibility.
- Benchmark results to catch performance regressions.

## Frequency
- On every PR (CI pipeline).
- Full regression suite nightly (via scheduled GitHub Action).
