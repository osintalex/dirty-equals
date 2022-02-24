import logging
from pathlib import Path

from pygments.styles.xcode import XcodeStyle
from pygments_ansi_color import color_tokens
from pymdownx.highlight import HtmlFormatter

try:
    import pytest
except ImportError:
    pytest = None

logger = logging.getLogger('mkdocs.test_examples')


def on_pre_build(config):
    test_examples()
    build_ansi_styles()


def test_examples():
    """
    Plug called by mkdocs-simple-hooks to run the examples tests.
    """
    if not pytest:
        logger.info('pytest not installed, skipping examples tests')
    else:
        logger.info('running examples tests...')
        return_code = pytest.main(['-q', '-p', 'no:sugar', 'tests/test_docs.py'])
        if return_code != 0:
            logger.warning('examples tests failed')


def build_ansi_styles():
    styles_file = Path(__file__).parent / 'css/ansi.css'
    if styles_file.exists():
        return

    colours = {
        'Black': '#000000',
        'Red': '#EF2929',
        'Green': '#8AE234',
        'Yellow': '#FCE94F',
        'Blue': '#3465A4',
        'Magenta': '#c509c5',
        'Cyan': '#34E2E2',
        'White': '#ffffff',
    }

    class MyStyle(XcodeStyle):
        styles = dict(XcodeStyle.styles)
        styles.update(color_tokens(colours, colours))

    formatter = HtmlFormatter(style=MyStyle)
    styles_file.parent.mkdir(exist_ok=True)
    styles_file.write_text(formatter.get_style_defs())
    logger.info('generated ansi styles file=%s', styles_file)
