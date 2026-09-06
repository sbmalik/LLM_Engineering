## check torch version
```bash
uv run python
import torch as t 
t.__version__ 
```

## check accelerators
```bash
uv run python
import torch as t
# cuda (NVIDIA)
t.cuda.is_available()
# mps (Macbook)
t.backends.mps.is_available()
```