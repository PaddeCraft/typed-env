# load_env()

The `load_env()`-function loads the environment from the `.env` file and the existing environment. If any duplicate variables exist, the ones from the `.env`-file are preferred.

```python
def load_env(vars: list[TypedVarDefinition] = [], /, filename :str = ".env", exit_on_error: bool = True) -> [Env, Optional[list[Error]]]
```

This returns
- An instance of `Env` if `exit_on_error=True`
- `[Env, []]` if `exit_on_error=False` and no errors are present
- `[None, list[Error]]` if  `exit_on_error=False` and errors are present