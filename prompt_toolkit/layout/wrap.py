from enum import Enum


class WrapStyle(Enum):
    """
    Determines how content will wrap when `wrap_lines` is `True`.

    The options are as follows:

        * CHAR: wrap on the character. This is effectively the default behavior
              if `wrap_lines` is `True`
        * WORD: wrap on a whitespace break.
        * ELLIPSIS: not so much a wrap, as a replacement of the last three
              characters of a line with three dots.
    """

    CHAR = "CHAR"
    WORD = "WORD"
    ELLIPSIS = "ELLIPSIS"
