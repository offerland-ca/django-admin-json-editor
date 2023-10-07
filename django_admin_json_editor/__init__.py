from .admin import JSONEditorWidget

try:
    from .version import __version__
except ImportError:
    __version__ = "main"
