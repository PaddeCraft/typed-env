# Quick Start

```python
from typed_env import *

vars = [
    v("FOO", str),
    v("BAR", int, OPTIONAL),
]

load_env(vars)
```

This example requires only one environment variable, `FOO`, but should `BAR` be present, it would need to be an integer (=match an integer regex).