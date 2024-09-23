#!/usr/bin/env python3
"""
Pandoc filter to convert code blocks with class "mermaid" to graph
"""

import os
from sys import getfilesystemencoding, stderr
from subprocess import Popen, call, PIPE
from itertools import chain
from glob import iglob
from hashlib import sha1
from pandocfilters import toJSONFilter, RawBlock, RawInline, Para, Image
from utillc import *

import mermaid as md
from mermaid.graph import Graph as G

sequence = G('Sequence-diagram',"""
stateDiagram-v2
    [*] --> Still
    Still --> [*]
 
    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
""")
render = md.Mermaid(sequence)
render.to_svg("/tmp/mermaid.svg")


def mermaid(key, value, fmt, meta):                   # pylint:disable=I0011,W0613
    """Handle mermaid block."""
    return (key, value, fmt, meta)


def fff() :
    return [Image(['', [], []], [], [
        png(
            contents,
            latexsnippet(
                '\\gregorioscore', kvs, staffsize, initiallines
            )
        ),
        ""
    ])]


if __name__ == "__main__":
    #EKO()
    toJSONFilter(mermaid)


