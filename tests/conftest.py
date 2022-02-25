from devtools import pformat

from dirty_equals import Contains


def pytest_assertrepr_compare(config, op, left, right):
    if isinstance(right, Contains):
        word = 'not' if op == '==' else 'unexpectedly'
        if len(right.contained_values) == 1:
            descr = f'Container: {right.contained_values[0]!r} {word} found in'
        else:
            descr = f'Container: {right.contained_values!r} all {word} found in'
        return [
            f'[dirty-equals] "{op}" failed',
            descr,
            *pformat(left).split('\n'),
        ]
