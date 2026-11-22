# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

"""
Classical Music Composition Engine
Generates original compositions in the style of Mozart, Vivaldi, and Beethoven.
"""

from .mozart_piece import compose_mozart
from .vivaldi_piece import compose_vivaldi
from .beethoven_piece import compose_beethoven

__all__ = ['compose_mozart', 'compose_vivaldi', 'compose_beethoven']
