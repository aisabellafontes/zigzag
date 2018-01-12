# ZigZag Sequence Code

Created based on ZigZag Problems (Topcoder registry )

# Description
Basically, the zigzag code consists in a sequence of integer numbers
that the difference between each element with your previous element
is a negative or positive result.

If those results (negative or positive) equal the previous result,
so it's not a zigzag code.

    Like that:
    e.g : 1,7,4,9,2,5 is a zigzag code. Difference results: [+6,-3,+5,-7,-3] => [ +,-,+,-,+]
    e.g : 1,4,7,2,5 isn't a zigzag code.Difference results: [+3, +3, -5, +3] => [+,+,-,+]


# Requirements
    python3 setuptools pip

# Instalation

From PyPI: [NOT REGISTERED YET]

    pip install ZigZag

From source:

    python setup.py install

# Usage

    import zigzag

    sequence = [1,7,4,9,2,5]
    zig = zigzag.ZigZag(sequence)
    zig.is_zigzag()