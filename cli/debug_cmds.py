from prompt_toolkit import print_formatted_text as print
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

def color(args):
    color = args[0]
    print (
            FormattedText([("class:color_me", "Some sample text for you to see the color")]),
            style=Style.from_dict({'color_me': color})
        )
    


def debug(msg, style=None):
    if style:
        print(msg, style=style)
    else:
        print(msg)