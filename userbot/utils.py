
import sys
import logging
import importlib
from telethon import events
from pathlib import Path
import inspect
import re

def load_plugins(plugin_name):
    path = Path(f"HyperAlphaX/plugins/{plugin_name}.py")
    name = "HyperAlphaX.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["HyperAlphaX.plugins." + plugin_name] = load
    print("HyperAlphaX has Imported " + plugin_name)
