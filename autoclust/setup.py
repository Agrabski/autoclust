from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="autoclust",
    version="1.3",
    rust_extensions=[RustExtension("autoclust.autoclust", binding=Binding.PyO3)],
    packages=["autoclust"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
import importlib
import autoclust
importlib.reload(autoclust)