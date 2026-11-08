<!-- INVENTED FIXTURE: RetryKit does not exist. Used only by the learn dry run. -->

# Changelog

## 2.1.0 (2026-03-02)

- `Retry-After` is now honored on 429 responses.

## 2.0.0 (2025-11-18)

- Breaking: the default `max_attempts` is now 5.
- Breaking: 501 and 505 are no longer retried, since repeating the request can't help.

## 1.4.0 (2025-02-10)

- Added the `backoff_ms` option.
