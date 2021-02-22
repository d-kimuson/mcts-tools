import executing
import pprint
from .coloring import SolarizedDark as SolarizedDark
from typing import Any

PYTHON2: Any

def bindStaticVariable(name: Any, value: Any): ...
def colorize(s: Any): ...
def supportTerminalColorsInWindows() -> None: ...
def stderrPrint(*args: Any) -> None: ...
def isLiteral(s: Any): ...
def colorizedStderrPrint(s: Any) -> None: ...

DEFAULT_PREFIX: str
DEFAULT_LINE_WRAP_WIDTH: int
DEFAULT_CONTEXT_DELIMITER: str
DEFAULT_OUTPUT_FUNCTION = colorizedStderrPrint
DEFAULT_ARG_TO_STRING_FUNCTION = pprint.pformat

class NoSourceAvailableError(OSError):
    infoMessage: str = ...

def callOrValue(obj: Any): ...

class Source(executing.Source):
    def get_text_with_indentation(self, node: Any): ...

def prefixLinesAfterFirst(prefix: Any, s: Any): ...
def indented_lines(prefix: Any, string: Any): ...
def format_pair(prefix: Any, arg: Any, value: Any): ...
def argumentToString(obj: Any): ...

class IceCreamDebugger:
    lineWrapWidth: Any = ...
    contextDelimiter: Any = ...
    enabled: bool = ...
    prefix: Any = ...
    includeContext: Any = ...
    outputFunction: Any = ...
    argToStringFunction: Any = ...
    def __init__(self, prefix: Any = ..., outputFunction: Any = ..., argToStringFunction: Any = ..., includeContext: bool = ...) -> None: ...
    def __call__(self, *args: Any): ...
    def format(self, *args: Any): ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def configureOutput(self, prefix: Any = ..., outputFunction: Any = ..., argToStringFunction: Any = ..., includeContext: Any = ...) -> None: ...

ic: Any
