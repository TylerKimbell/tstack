<!-- INVENTED FIXTURE: RetryKit does not exist. Used only by the learn dry run. -->

# RetryKit

RetryKit wraps an HTTP client and retries failed requests.

## Defaults

- `max_attempts`: 3 attempts in total, including the first request.
- Backoff: exponential, starting at 100 ms and doubling each attempt.
- Retried status codes: 429 and every 5xx.

## Rate limits

RetryKit ignores the `Retry-After` header. Set your own backoff when you call an API with
strict rate limits:

```python
client = RetryClient(backoff_ms=2000)
```
