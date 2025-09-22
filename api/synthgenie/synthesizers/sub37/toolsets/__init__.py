"""Toolsets for the Moog Sub 37 synthesizer."""

from .amplifier_toolset import AMPLIFIER_KEYWORDS, amplifier_toolset
from .arpeggiator_toolset import ARPEGGIATOR_KEYWORDS, arpeggiator_toolset
from .effects_toolset import EFFECTS_KEYWORDS, effects_toolset
from .filter_toolset import FILTER_KEYWORDS, filter_toolset
from .glide_toolset import GLIDE_KEYWORDS, glide_toolset
from .modulation_toolset import MODULATION_KEYWORDS, modulation_toolset
from .oscillator_toolset import OSCILLATOR_KEYWORDS, oscillator_toolset

__all__ = [
    'amplifier_toolset',
    'arpeggiator_toolset',
    'effects_toolset',
    'filter_toolset',
    'glide_toolset',
    'modulation_toolset',
    'oscillator_toolset',
    'AMPLIFIER_KEYWORDS',
    'ARPEGGIATOR_KEYWORDS',
    'EFFECTS_KEYWORDS',
    'FILTER_KEYWORDS',
    'GLIDE_KEYWORDS',
    'MODULATION_KEYWORDS',
    'OSCILLATOR_KEYWORDS',
]
