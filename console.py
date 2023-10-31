import re

from rich.columns import Columns
from rich.console import Console
from rich.markdown import Markdown
from rich.padding import Padding
from rich.panel import Panel
from rich.text import Text

console = Console()


def print_markdown(text) -> None:
    """Prints a rich info message. Support Markdown syntax."""

    md = Padding(Markdown(text), 2)
    console.print(md)


def print_step(text) -> None:
    """Prints a rich info message."""

    panel = Panel(Text(text, justify="left"))
    console.print(panel)


def print_table(items) -> None:
    """Prints items in a table."""

    console.print(
        Columns([Panel(f"[yellow]{item}", expand=True) for item in items]))


def print_substep(text, style="") -> None:
    """Prints a rich colored info message without the panelling."""
    console.print(text, style=style)
