from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.layout import Layout


about_title = ":octopus: About me :octopus:"

about_content = """\
[i] 
    A bit of everything 
    Almost just nothing
    But always enough
[/]
I like learning, coding, experimenting, researching, modelling. 
I feel very comfortable with Python, JavaScript and my favourite C++ and C.
I am interested in artificial intelligence, machine learning and process modelling. 
I also like doing electronics and coding on microprocessors.

I am for the sharing of knowledge, resources and ideas.

Note: [i]Don't expect to find only production ready code in my repo, mainly the opposite.[/]
"""
PADDING = 2
ABOUT_SIZE = 13+PADDING

about_panel = Panel.fit(
    about_content, box=box.SQUARE, border_style="blue", title=about_title, width=100
)

tree_title = "Repositories"

tree = Tree("[link=https://github.com/bortch]..", guide_style="bold cyan")
ai_ml_tree = tree.add("AI & Machine Learning", guide_style="green")
ai_ml_tree.add("[link=https://github.com/bortch/bs_lib]Own library of usefull functions")
ai_ml_tree.add("[link=https://github.com/bortch/quickdraw]Quick attempt @ the Quick Draw Challenge")
ai_ml_tree.add("[link=https://github.com/bortch/second_hand_UK_car_challenge]Quick attempt @ the Used UK cars challenge")
ai_ml_tree.add("[link=https://github.com/bortch/Learning_Machine_Learning]Notes from my AI & ML Courses")
electronics_tree = tree.add("Electronics & Embedded")
electronics_tree.add("[link=https://bortch.github.io/Upcycled-STIB-Validator/]Upcycled STIB-MIVB Validator")

TREE_SIZE = 8+PADDING

tree_panel = Panel.fit(
    tree, box=box.SQUARE, border_style="blue", title=tree_title, width=100
)

layout = Layout()
upper = Layout(size = ABOUT_SIZE)
lower = Layout(size = TREE_SIZE)
layout.split_column(
    upper,
    lower
)
upper.update(about_panel)
lower.update(tree_panel)

console = Console(record=True, width=100, height=ABOUT_SIZE+TREE_SIZE)

console.print(layout)

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
