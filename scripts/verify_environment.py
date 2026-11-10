
import sys
import numpy
import pandas
import scipy
import pyarrow
import requests
import yaml
import matplotlib
import plotly
import pytest

print("=" * 50)
print("NEUROWEAVE ENVIRONMENT VERIFICATION")
print("=" * 50)

print("Python:", sys.version)
print("Python executable:", sys.executable)

print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("SciPy:", scipy.__version__)
print("PyArrow:", pyarrow.__version__)

print("\nAll essential libraries imported successfully!")
print("NeuroWeave environment is ready!")
