import streamlit as st
from sys import path
import backend.connection as ct
import pandas as pd

#df = pd.DataFrame(backend.connection.list_products())

for p in path:
  print(p)