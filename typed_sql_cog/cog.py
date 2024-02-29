# dummy file for type hint


def out(sOut: str = "", dedent: bool = False, trimblanklines: bool = False) -> None:
    """
    Writes text to the output.
    sOut is the string to write to the output.
    If dedent is True, then common initial white space is removed from
    the lines in sOut before adding them to the output. If trimblanklines is
    True, then an initial and trailing blank line are removed from sOut before
    adding them to the output. Together, these option arguments make it easier
    to use multi-line strings, and they only are useful for multi-line strings:
    """


def outl(sOut: str = "", dedent: bool = False, trimblanklines: bool = False) -> None:
    """
    Same as cog.out, but adds a trailing newline.
    """


def msg(msg: str) -> None:
    """
    Prints msg to stdout with a "Message: " prefix.
    """


def error(msg: str) -> None:
    """
    Raises an exception with msg as the text. No traceback is included, so
    that non-Python programmers using your code generators won't be scared.
    """


inFile: str = ""
"""
An attribute, the path of the input file.
"""

outFile: str = ""
"""
An attribute, the path of the output file.
"""

firstLineNum: int = 0
"""
An attribute, the line number of the first line of Python code in the 
generator. This can be used to distinguish between two generators in the 
same input file, if needed.
"""

previous: str = ""
"""
An attribute, the text output of the previous run of this generator. This 
can be used for whatever purpose you like, including outputting again 
with cog.out().
"""
