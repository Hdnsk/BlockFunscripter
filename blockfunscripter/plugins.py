import importlib
import pkgutil
import inspect
from bfslib import AbstractGenerator
from bfslib.abstract import AbstractBlock

loaded_plugins = []
discovered_plugins = [
    name
    for finder, name, ispkg
    in pkgutil.iter_modules()
    if name.startswith('bfslib')
]


class Plugin():
    def __init__(self, name) -> None:
        self.name = name
        self.generators = self.discover_generators()
        self.blocks = self.discover_blocks()

    def discover_generators(self) -> list:
        generators = importlib.import_module(".generators", package=self.name)
        for name, obj in inspect.getmembers(generators):
            if inspect.isclass(obj):
                if AbstractGenerator in obj.__bases__:
                    yield {"name": name, "obj": obj}

    def discover_blocks(self) -> list:
        blocks = importlib.import_module(".blocks", package=self.name)
        for name, obj in inspect.getmembers(blocks):
            if inspect.isclass(obj):
                if AbstractBlock in obj.__bases__:
                    yield {"name": name, "obj": obj}


def plugin_loaded(name) -> bool:
    for p in loaded_plugins:
        if p.name == name:
            return True
    return False


def load_plugins() -> None:
    for name in discovered_plugins:
        if not plugin_loaded(name):
            loaded_plugins.append(Plugin(name))


load_plugins()
