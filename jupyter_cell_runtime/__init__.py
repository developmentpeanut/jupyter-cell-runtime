def load_ipython_extension(ipython):
    from .extension import load_ipython_extension as _load
    _load(ipython)

def unload_ipython_extension(ipython):
    from .extension import unload_ipython_extension as _unload
    _unload(ipython)
