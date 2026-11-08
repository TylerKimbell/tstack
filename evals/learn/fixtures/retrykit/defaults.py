# INVENTED FIXTURE: RetryKit does not exist. Used only by the learn dry run.
# Holds defaults only. The request loop lives in the client module, which isn't included.

MAX_ATTEMPTS = 5
BACKOFF_MS = 100
RETRYABLE_STATUS = {429, 500, 502, 503, 504}
