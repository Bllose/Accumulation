``` Python
from bokeh.plotting import figure, show
from bokeh.resources import INLINE
import bokeh.io
bokeh.io.output_notebook(INLINE)
x = [1,2,3,4,5]
y = [6,7,2,4,5]
p = figure(title='Simple line example', x_axis_label='x', y_axis_label = 'y')
p.line(x, y, legend_label='Temp.', line_width=2)
# plotting
中级接口(mid-level interface)
the main idea can be described by the statement:
**Starting from simple defualt figures(with sensible default tools, grids and axes), add markers and other
shapes whose visual attributes are tied to directly data.**
## Scatter Plots
Bokeh can draw many types of visual shapes(called glyphs), including lines, bars, patches, hex tiles and
Using various marker glyphs of Bokeh to create simple scatter plots.
ps: ```p.circle``` ```p.line```
用来创建 plot 对象
output_file/ output_notebook
输出为独立文件/ 输出到Notebook上
# show/save  
``` Python
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.resources import INLINE
output_notebook(INLINE)
# create a new plot with default tools, using figure
p = figure(plot_width=400, plot_height=400)
# add a circle renderer with x and y coordinates, size, color, and alpha
p.circle([1,2,3,4,5], [6, 7, 2, 4, 5], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)
``` Python
import networkx as nx
from bokeh.models import Circle, MultiLine
from bokeh.plotting import figure, from_networkx, show
G = nx.karate_club_graph()
SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = 'darkgrey', 'red'
edge_attrs = {}
# 遍历该网状结构数据，通过头结点、尾结点确定一条边，再通过头结点名称与尾结点名称是否一致，给边上色。
# 另外，权重属性在本案例中未使用，故忽略
for start_node, end_node, _ in G.edges(data=True):
    edge_color = SAME_CLUB_COLOR if G.nodes[start_node]["club"] == G.nodes[end_node]["club"] else DIFFERENT_CLUB_COLOR
    edge_attrs[(start_node, end_node)] = edge_color
# 将准备好的边界颜色参数添加到“边界参数”中， 与权重这个参数在一起。
{0: {1: {'weight': 4, 'edge_color': 'darkgrey'}, 2: {'weight': 5, 'edge_color': 'darkgrey'}, 3: {'weight': 3, 'edge_color': 'darkgrey'}, 4: {'weight': 3, 'edge_color': 'darkgrey'}, 5: {'weight': 3, 'edge_color': 'darkgrey'}, 6: ...
如上数据结果说明： 边 (0, 1) 权重为4， 颜色为灰色。 边(0, 2) 权重为5， 也为灰色，等等。
nx.set_edge_attributes(G, edge_attrs, "edge_color")
plot = figure(width=400, height=400, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2), x_axis_location=None,
              toolbar_location=None, title="Graph Interaction Demo", background_fill_color="#efefef",
              tooltips="index: @index, club: @club")
plot.grid.grid_line_color= None
graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))
graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="lightblue")
graph_renderer.edge_renderer.glyph = MultiLine(line_color="edge_color", line_alpha=0.8, line_width=1.5)
plot.renderers.append(graph_renderer)
show(plot)
# [networkX](https://networkx.org/)
**[github.com/networkx/networkx](https://github.com/networkx/networkx)**
NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
>>> import networkx as nx
>>> G = nx.Graph()
>>> G.add_edge("A", "B", weight=4)
>>> G.add_edge("B", "D", weight=2)
>>> G.add_edge("A", "C", weight=3)
>>> G.add_edge("C", "D", weight=4)
>>> nx.shortest_path(G, "A", "D", weight="weight")
['A', 'B', 'D']
