# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

"""
Helper functions for Mozart-style composition.
"""

from .music_theory import *
from .patterns import *


def compose_theme1_gmajor(composer, violin1, violin2, viola, cello):
    """Theme 1 in G Major."""
    melody = [
        (62, 0.25, 90), (64, 0.25, 85), (66, 0.25, 85), (67, 0.5, 95),
        (67, 0.25, 80), (69, 0.25, 85), (71, 0.25, 85), (72, 0.5, 95),
        (72, 0.25, 80), (71, 0.25, 85), (69, 0.25, 85), (67, 0.5, 95),
        (66, 0.25, 80), (64, 0.25, 85), (62, 0.25, 85), (62, 0.5, 90),
        (62, 0.25, 85), (64, 0.25, 90), (66, 0.25, 85), (67, 0.75, 95),
        (69, 0.25, 85), (67, 0.25, 80), (66, 0.25, 85), (64, 0.5, 90),
        (66, 0.25, 85), (67, 0.25, 90), (69, 0.25, 85), (71, 0.5, 95),
        (72, 0.25, 85), (74, 0.25, 90), (74, 1.0, 100),
    ]
    for note, dur, vel in melody:
        composer.note(violin1, note, dur, vel)
    
    for note, dur, vel in [(59, 1.0, 65), (57, 1.0, 65), (59, 1.0, 65), (60, 1.0, 65),
                            (62, 1.0, 65), (60, 1.0, 65), (59, 1.0, 65), (62, 2.0, 70)]:
        composer.note(violin2, note, dur, vel)
    
    for note, dur, vel in [(50, 0.5, 55), (50, 0.5, 55), (48, 0.5, 55), (48, 0.5, 55),
                            (50, 0.5, 55), (50, 0.5, 55), (52, 0.5, 55), (52, 0.5, 55),
                            (54, 0.5, 55), (54, 0.5, 55), (55, 0.5, 55), (55, 0.5, 55),
                            (54, 0.5, 55), (54, 0.5, 55), (57, 1.0, 60), (57, 1.0, 60)]:
        composer.note(viola, note, dur, vel)
    
    for _ in range(2):
        for note, dur, vel in [(31, 0.25, 60), (38, 0.25, 55), (35, 0.25, 55), (38, 0.25, 55),
                                (31, 0.25, 60), (38, 0.25, 55), (35, 0.25, 55), (38, 0.25, 55),
                                (36, 0.25, 60), (43, 0.25, 55), (40, 0.25, 55), (43, 0.25, 55),
                                (38, 0.25, 60), (45, 0.25, 55), (42, 0.25, 55), (45, 0.25, 55)]:
            composer.note(cello, note, dur, vel)
    
    extend_theme1_5to8(composer, violin1, violin2, viola, cello)

"""
Helper functions for Mozart-style composition.
"""

from .music_theory import *
from .patterns import *


def compose_theme1_gmajor(composer, violin1, violin2, viola, cello):
    """Theme 1 in G Major - the famous rocket theme."""
    melody = [
        (62, 0.25, 90), (64, 0.25, 85), (66, 0.25, 85), (67, 0.5, 95),
        (67, 0.25, 80), (69, 0.25, 85), (71, 0.25, 85), (72, 0.5, 95),
        (72, 0.25, 80), (71, 0.25, 85), (69, 0.25, 85), (67, 0.5, 95),
        (66, 0.25, 80), (64, 0.25, 85), (62, 0.25, 85), (62, 0.5, 90),
        (62, 0.25, 85), (64, 0.25, 90), (66, 0.25, 85), (67, 0.75, 95),
        (69, 0.25, 85), (67, 0.25, 80), (66, 0.25, 85), (64, 0.5, 90),
        (66, 0.25, 85), (67, 0.25, 90), (69, 0.25, 85), (71, 0.5, 95),
        (72, 0.25, 85), (74, 0.25, 90), (74, 1.0, 100),
    ]
    
    for note, dur, vel in melody:
        composer.note(violin1, note, dur, vel)
    
    for note, dur, vel in [(59, 1.0, 65), (57, 1.0, 65), (59, 1.0, 65), (60, 1.0, 65),
                            (62, 1.0, 65), (60, 1.0, 65), (59, 1.0, 65), (62, 2.0, 70)]:
        composer.note(violin2, note, dur, vel)
    
    for note, dur, vel in [(50, 0.5, 55), (50, 0.5, 55), (48, 0.5, 55), (48, 0.5, 55),
                            (50, 0.5, 55), (50, 0.5, 55), (52, 0.5, 55), (52, 0.5, 55),
                            (54, 0.5, 55), (54, 0.5, 55), (55, 0.5, 55), (55, 0.5, 55),
                            (54, 0.5, 55), (54, 0.5, 55), (57, 1.0, 60), (57, 1.0, 60)]:
        composer.note(viola, note, dur, vel)
    
    for _ in range(2):
        for note, dur, vel in [(31, 0.25, 60), (38, 0.25, 55), (35, 0.25, 55), (38, 0.25, 55),
                                (31, 0.25, 60), (38, 0.25, 55), (35, 0.25, 55), (38, 0.25, 55),
                                (36, 0.25, 60), (43, 0.25, 55), (40, 0.25, 55), (43, 0.25, 55),
                                (38, 0.25, 60), (45, 0.25, 55), (42, 0.25, 55), (45, 0.25, 55)]:
            composer.note(cello, note, dur, vel)
    
    extend_theme1_5to8(composer, violin1, violin2, viola, cello)


def extend_theme1_5to8(composer, violin1, violin2, viola, cello):
    """Bars 5-8 of Theme 1."""
    melody = [
        (72, 0.25, 90), (71, 0.25, 85), (69, 0.25, 85), (67, 0.5, 95),
        (66, 0.25, 80), (67, 0.25, 85), (69, 0.25, 85), (71, 0.5, 90),
        (72, 0.25, 85), (74, 0.25, 90), (72, 0.25, 85), (71, 0.25, 85),
        (69, 0.5, 95), (67, 0.25, 80), (69, 0.25, 85),
        (71, 0.25, 90), (72, 0.25, 85), (74, 0.25, 90), (76, 0.5, 95),
        (74, 0.25, 85), (72, 0.25, 85), (71, 0.25, 90),
        (69, 0.5, 85), (67, 0.5, 90), (66, 0.5, 85), (64, 0.5, 90),
        (62, 0.5, 85), (64, 0.5, 90), (66, 0.5, 85), (67, 1.0, 100),
    ]
    
    for note, dur, vel in melody:

def compose_theme2_dmajor(composer, violin1, violin2, viola, cello):
    """Theme 2 in D Major - more lyrical."""
    melody = [
        (74, 0.5, 85), (73, 0.25, 75), (74, 0.25, 85),
        (76, 0.5, 90), (74, 0.25, 75), (76, 0.25, 85),
        (78, 0.75, 95), (76, 0.25, 80),
        (74, 0.5, 85), (73, 0.5, 80),
        (74, 0.25, 85), (76, 0.25, 80), (78, 0.25, 85), (79, 0.5, 90),
        (81, 0.25, 85), (79, 0.25, 80), (78, 0.25, 85), (76, 0.5, 90),
        (74, 0.5, 85), (76, 0.5, 80),
        (78, 0.25, 90), (79, 0.25, 85), (81, 0.25, 90), (83, 0.5, 95),
        (81, 0.25, 85), (79, 0.25, 85), (78, 0.25, 90), (76, 0.5, 90),
        (74, 0.5, 85), (76, 0.5, 80),
        (78, 0.25, 85), (76, 0.25, 90), (74, 0.25, 85), (73, 0.25, 80),
        (74, 1.0, 95), (76, 0.5, 85), (74, 0.5, 90), (73, 0.5, 85), (74, 1.0, 100),
    ]
    for note, dur, vel in melody:
        composer.note(violin1, note, dur, vel)
    
    for note, dur, vel in [(69, 1.0, 65), (67, 1.0, 65), (69, 1.0, 65), (71, 1.0, 65),
                            (73, 1.0, 65), (71, 1.0, 65), (69, 1.0, 65), (71, 1.0, 65),
                            (73, 1.0, 65), (71, 1.0, 65), (69, 1.0, 65), (67, 1.0, 65),
                            (69, 1.0, 65), (71, 1.0, 65), (69, 1.0, 65), (67, 1.0, 65)]:
        composer.note(violin2, note, dur, vel)
    
    for _ in range(8):
        composer.note(viola, 57, 0.5, 55)
    
    for note, dur, vel in [(38, 0.25, 60), (45, 0.25, 55), (42, 0.25, 55), (45, 0.25, 55)] * 4:
        composer.note(cello, note, dur, vel)


def compose_closing_dmajor(composer, violin1, violin2, viola, cello):
    """Closing section confirming D Major."""
    melody = [
        (74, 0.25, 90), (76, 0.25, 85), (78, 0.25, 90), (79, 0.5, 95),
        (78, 0.25, 85), (76, 0.25, 85), (74, 0.25, 90), (76, 0.5, 95),
        (78, 0.25, 90), (79, 0.25, 85), (81, 0.25, 90), (79, 0.5, 95),
        (78, 0.5, 85), (76, 0.5, 90), (74, 1.0, 100),
    ]
    for note, dur, vel in melody:
        composer.note(violin1, note, dur, vel)
    
    for _ in range(4):
        composer.note(violin2, 62, 0.5, 65)
        composer.note(viola, 50, 0.5, 55)
        composer.note(cello, 38, 0.5, 65)


def extend_theme1_5to8(composer, violin1, violin2, viola, cello):
    """Bars 5-8 of Theme 1."""
    melody = [
        (72, 0.25, 90), (71, 0.25, 85), (69, 0.25, 85), (67, 0.5, 95),
        (66, 0.25, 80), (67, 0.25, 85), (69, 0.25, 85), (71, 0.5, 90),
        (72, 0.25, 85), (74, 0.25, 90), (72, 0.25, 85), (71, 0.25, 85),
        (69, 0.5, 95), (67, 0.25, 80), (69, 0.25, 85),
        (71, 0.25, 90), (72, 0.25, 85), (74, 0.25, 90), (76, 0.5, 95),
        (74, 0.25, 85), (72, 0.25, 85), (71, 0.25, 90),
        (69, 0.5, 85), (67, 0.5, 90), (66, 0.5, 85), (64, 0.5, 90),
        (62, 0.5, 85), (64, 0.5, 90), (66, 0.5, 85), (67, 1.0, 100),
    ]
    for note, dur, vel in melody:
        composer.note(violin1, note, dur, vel)
    
    for _ in range(4):
        composer.note(violin2, 60, 0.5, 60)
        composer.note(violin2, 59, 0.5, 60)
    
    for n in [55, 57, 59, 60, 62, 60, 59, 55]:
        composer.note(viola, n, 0.5, 55)
    
    for note, dur, vel in [(31, 0.25, 60), (38, 0.25, 55), (35, 0.25, 55), (38, 0.25, 55),
                            (33, 0.25, 60), (40, 0.25, 55), (37, 0.25, 55), (40, 0.25, 55),
                            (35, 0.25, 60), (42, 0.25, 55), (39, 0.25, 55), (42, 0.25, 55),
                            (31, 0.5, 65), (31, 0.5, 65), (31, 1.0, 70)]:
        composer.note(cello, note, dur, vel)


def compose_transition(composer, violin1, violin2, viola, cello):
    """Transition modulating from G Major to D Major."""
    melody = [
        (74, 0.25, 90), (76, 0.25, 85), (78, 0.25, 90), (79, 0.5, 95),
        (78, 0.25, 85), (76, 0.25, 85), (74, 0.25, 90), (76, 0.5, 95),
        (74, 0.25, 85), (72, 0.25, 90), (74, 0.25, 85), (76, 0.25, 90),
        (78, 0.25, 85), (79, 0.25, 90), (81, 0.5, 100),
        (79, 0.5, 90), (78, 0.5, 85), (76, 0.5, 90),
    ]
    for note, dur, vel in melody:
        composer.note(violin1, note, dur, vel)
    
    for _ in range(4):
        composer.note(violin2, 62, 0.25, 70)
        composer.note(violin2, 64, 0.25, 65)
        composer.note(violin2, 66, 0.25, 65)
        composer.note(violin2, 67, 0.25, 70)
    
    for _ in range(4):
        composer.note(viola, 50, 0.5, 55)
        composer.note(viola, 52, 0.5, 55)
    
    for n in [31, 33, 35, 38, 40, 38, 35, 38]:
        composer.note(cello, n, 0.5, 65)

        composer.note(violin1, note, dur, vel)
    
    for _ in range(4):
        composer.note(violin2, 60, 0.5, 60)
        composer.note(violin2, 59, 0.5, 60)
    
    for n in [55, 57, 59, 60, 62, 60, 59, 55]:
        composer.note(viola, n, 0.5, 55)
    
    for note, dur, vel in [(31, 0.25, 60), (38, 0.25, 55), (35, 0.25, 55), (38, 0.25, 55),
                            (33, 0.25, 60), (40, 0.25, 55), (37, 0.25, 55), (40, 0.25, 55),
                            (35, 0.25, 60), (42, 0.25, 55), (39, 0.25, 55), (42, 0.25, 55),
                            (31, 0.5, 65), (31, 0.5, 65), (31, 1.0, 70)]:
        composer.note(cello, note, dur, vel)


def compose_transition(composer, violin1, violin2, viola, cello):
    """Transition modulating from G Major to D Major."""
    melody = [
        (74, 0.25, 90), (76, 0.25, 85), (78, 0.25, 90), (79, 0.5, 95),
        (78, 0.25, 85), (76, 0.25, 85), (74, 0.25, 90), (76, 0.5, 95),
        (74, 0.25, 85), (72, 0.25, 90), (74, 0.25, 85), (76, 0.25, 90),
        (78, 0.25, 85), (79, 0.25, 90), (81, 0.5, 100),
        (79, 0.5, 90), (78, 0.5, 85), (76, 0.5, 90),
    ]
    
    for note, dur, vel in melody:
        composer.note(violin1, note, dur, vel)
    
    for _ in range(4):
        composer.note(violin2, 62, 0.25, 70)
        composer.note(violin2, 64, 0.25, 65)
        composer.note(violin2, 66, 0.25, 65)
        composer.note(violin2, 67, 0.25, 70)
    
    for _ in range(4):
        composer.note(viola, 50, 0.5, 55)
        composer.note(viola, 52, 0.5, 55)
    
    for n in [31, 33, 35, 38, 40, 38, 35, 38]:
        composer.note(cello, n, 0.5, 65)
