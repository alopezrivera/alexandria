import os
import sys
from datetime import datetime
from contextlib import contextmanager

from alexandria.data_structs.string import capletter
from alexandria.shell.color import colors, shell_supports_color
from alexandria.data_structs.string import join_set_distance


@contextmanager
def suppress_stdout():
    """
    Suppress console output.
    """
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


def str_color(string, color, color_bg="", highlight=""):
    """
    Generate a colored string using the available foreground and background
    colors and highlights, or ANSI codes directly.

    Automatically detects whether your shell supports ANSI color codes:
    in the case they're not, no ANSI codes will be added to your string.

    **
    Note:

    Incorrect ANSI codes will be rendered as text. Furthermore, not
    all ANSI codes may be supported by your shell of choice. In such
    cases the ANSI codes will be rendered as text as well.
    **

    ### Available colors:
    - 'black'     |   'brightBlack'
    - 'red'       |   'brightRed'
    - 'green'     |   'brightGreen'
    - 'yellow'    |   'brightYellow'
    - 'blue'      |   'brightBlue'
    - 'magenta'   |   'brightMagenta'
    - 'cyan'      |   'brightCyan'
    - 'white'     |   'brightWhite'

    ### Available highlights:
    - bold
    - faint
    - italic
    - underline
    - crossed
    - framed
    - encircled
    - overlined

    :param string: String to print.
    :param color: Color.
    :param color_bg: Background color.
    :param highlight: Highlight.
    """
    if shell_supports_color():
        color_key       = "fg" + capletter(color, 0)
        color_bg_key    = "bg" + capletter(color_bg, 0)

        color           = colors.__dict__[color_key]    if color_key    in colors.__dict__.keys() else color
        color_bg        = colors.__dict__[color_bg_key] if color_bg_key in colors.__dict__.keys() else color_bg
        highlight       = colors.__dict__[highlight]    if highlight    in colors.__dict__.keys() else highlight

        bound = lambda s: colors.reset + s + colors.reset
        c_str = bound(color + color_bg + highlight + string)

        return c_str
    else:
        return string


def print_color(string, color, color_bg="", highlight="", **kwargs):
    """
    Print in color using the available foreground and background colors
    and highlights, or ANSI codes directly.

    Automatically detects whether your shell supports ANSI color codes:
    in the case they're not, the standard _print_ function is used.

    Supports keyword arguments for the standard _print_ function.

    **
    Note:

    Incorrect ANSI codes will be rendered as text. Furthermore, not
    all ANSI codes may be supported by your chosen shell. In such
    cases the ANSI codes will be rendered as text as well.
    **

    ### Available colors:
    - 'black'     |   'brightBlack'
    - 'red'       |   'brightRed'
    - 'green'     |   'brightGreen'
    - 'yellow'    |   'brightYellow'
    - 'blue'      |   'brightBlue'
    - 'magenta'   |   'brightMagenta'
    - 'cyan'      |   'brightCyan'
    - 'white'     |   'brightWhite'

    ### Available highlights:
    - bold
    - faint
    - italic
    - underline
    - crossed
    - framed
    - encircled
    - overlined

    :param string: String to print.
    :param color: Color.
    :param color_bg: Background color.
    :param highlight: Highlight.
    :param kwargs: Keyword arguments for the standard _print_ function.
    """
    if shell_supports_color():
        c_str = str_color(string, color, color_bg, highlight)
        print(c_str, **kwargs)
    else:
        print(string, **kwargs)


def str_log(kind, msg,
            kind_color='black',
            kind_bg_color='white',
            msg_color='cyan',
            msg_bg_color="",
            t_color="",
            t_bg_color=""):
    """
    Create rich logging string.

    TIME :: KIND :: MSG

    Colors rendered via the _str_color_ method. Refer to the Alexandria _str_color_
    and _colors_ class documentation for color input information.

    :param kind: Message kind. Akin to Python logging library's INFO, WARNING, CRITICAL.
                 As Alexandria does not pretend to replace logging, _kind_ is an arbitrary
                 convenient marker unaffected by _loglevel_ or any other output control
                 parameters.
    :param msg: Log message.
    :param kind_color: Kind text color.
    :param kind_bg_color: Kind background color.
    :param msg_color: Message text color.
    :param msg_bg_color: Message background color.
    :param t_color: Time text color.
    :param t_bg_color: Time background color.
    """
    # Print current time
    t = datetime.now().strftime("%H:%M:%S")
    str_t    = str_color(t,    t_color,    t_bg_color)
    # Print log kind
    str_kind = str_color(kind, kind_color, kind_bg_color)
    # Print log
    str_msg  = str_color(msg,  msg_color,  msg_bg_color)

    r = join_set_distance(str_t + " ::", str_kind, 15)
    r = join_set_distance(r, "::", 47)
    r = join_set_distance(r, str_msg, len(r))
    return r


def log(kind, msg,
        kind_color='black',
        kind_bg_color='white',
        msg_color='cyan',
        msg_bg_color="",
        t_color="",
        t_bg_color="",
        **kwargs):
    """
    Rich logging function.

    TIME :: KIND :: MSG

    Colors rendered via the _str_color_ method. Refer to the Alexandria _str_color_
    and _colors_ class documentation for color input information.

    :param kind: Message kind. Akin to Python logging library's INFO, WARNING, CRITICAL.
                 As Alexandria does not pretend to replace logging, _kind_ is an arbitrary
                 convenient marker unaffected by _loglevel_ or any other output control
                 parameters.
    :param msg: Log message.
    :param kind_color: Kind text color.
    :param kind_bg_color: Kind background color.
    :param msg_color: Message text color.
    :param msg_bg_color: Message background color.
    :param t_color: Time text color.
    :param t_bg_color: Time background color.
    :param kwargs: Keyword arguments for the standard _print_ function.
    """
    s = str_log(kind, msg,
                kind_color, kind_bg_color,
                msg_color, msg_bg_color,
                t_color, t_bg_color)
    print(s, **kwargs)


def print_numbered_list(lst, length=10):
    """
    Print numbered list.

    :param lst: List.
    :param length: Length of each of the strings containing a numeral and list entry.
    """
    for i in range(len(lst)):
        n = f"{i+1}"+"."
        s = join_set_distance(n, str(lst[i]), length)
        print(s)


def print_result(var, val, u, d=5, n=10):
    """
    Pretty print a calculated result.

    :param var: Variable
    :param val: Value
    :param u: Units
    :param d: Decimal digits
    :param n: Resulting string length
    :return:
    """
    s = join_set_distance(f'{var} {val:.{d}f}', u, n)
    print(s)


if __name__ == "__main__":
    log("INFO", "HELL NO" + str_color("MAAFUCKA", "red"))
    log("WARNING", "HELL NO" + str_color("MAAFUCKA", "red"))
    log("CRITICAL", "HELL NO" + str_color("MAAFUCKA", "red"))
