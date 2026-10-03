# retrybox

Call a function up to N times. The last exception is raised when every attempt fails.

```python
from retrybox import retry, try_retry, attempt_of

retry(lambda: load(), 3)
ok, value = try_retry(lambda: load(), 3)
value, n = attempt_of(lambda: load(), 3)
```

```bash
python -m unittest test_retrybox.py
```

MIT
