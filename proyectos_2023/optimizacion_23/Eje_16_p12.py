import plotly.graph_objects as go 
import numpy as np 

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)

X, Y = np.meshgrid(x,y)

Z = (X-1)**2 * Y

fig = go.Figure(data= [go.Surface(z=Z)])
fig.update_layout(title = 'funcion', autosize = False, width = 500, height = 500, margin = dict(l=65, r = 50, b = 65, t = 90))
fig.show()