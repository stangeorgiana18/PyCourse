from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

# interact autogenetates a user interface control for a function argument
def func(x):
    return x

interact(func, x = 10)

# in Jupyter 

