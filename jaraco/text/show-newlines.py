import autocommand
import inflect

from more_itertools import always_iterable

import jaraco.text


def report_newlines(filename):
    r"""
    Report the newlines in the indicated file.

    >>> report_newlines(__file__)
    newline is '\n'
    >>> tmp_path = getfixture('tmp_path')
    >>> filename = tmp_path / 'out.txt'
    >>> _ = filename.write_text('foo\nbar\r\n')
    >>> report_newlines(filename)
    newlines are ('\n', '\r\n')
    """
    newlines = jaraco.text.read_newlines(filename)
    count = len(tuple(always_iterable(newlines)))
    engine = inflect.engine()
    print(
        engine.plural_noun("newline", count),
        engine.plural_verb("is", count),
        repr(newlines),
    )


autocommand.autocommand(__name__)(report_newlines)
