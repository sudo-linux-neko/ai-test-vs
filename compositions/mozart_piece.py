# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

"""
Piece 1: Classical Serenade in G Major
Inspired by Mozart - Eine Kleine Nachtmusik, K. 525
Duration: ~12 minutes | String Quartet | Allegro (~132 BPM)
"""

from .composer_engine import SequentialComposer
from .music_theory import *
from .patterns import *

TEMPO_BPM = 132
TICKS_PER_BEAT = 480


def compose_mozart():
    """Compose a complete sonata-allegro movement in G Major."""
    composer = SequentialComposer(ticks_per_beat=TICKS_PER_BEAT)
    
    score_track = composer.create_track("Score/Tempo", 0)
    composer.set_tempo(score_track, TEMPO_BPM)
    composer.set_time_signature(score_track, 4, 4)
    
    v1 = composer.create_track("Violin I", INSTRUMENTS['violin'])
    v2 = composer.create_track("Violin II", INSTRUMENTS['violin'])
    va = composer.create_track("Viola", INSTRUMENTS['viola'])
    vc = composer.create_track("Cello", INSTRUMENTS['cello'])
    
    # Generate extended sonata-allegro form with multiple repetitions
    # to achieve 10+ minute duration
    for cycle in range(5):  # 5 cycles for extended duration
        generate_exposition(composer, v1, v2, va, vc, repeat=True)
        generate_development(composer, v1, v2, va, vc)
        generate_recapitulation(composer, v1, v2, va, vc)
        generate_coda(composer, v1, v2, va, vc)
    
    generate_extended_coda(composer, v1, v2, va, vc)
    
    filename = '/home/neko/ai-test-vs/audio/mozart_classical_serenade.mid'
    composer.save(filename)
    
    duration_minutes = composer.track_positions[v1] / TICKS_PER_BEAT / TEMPO_BPM
    print(f"Mozart-style piece composed: {filename}")
    print(f"Duration: {duration_minutes:.1f} minutes")
    return filename, duration_minutes


def generate_exposition(composer, v1, v2, va, vc, repeat=True):
    """Generate full exposition section."""
    for _ in range(2):
        mozart_theme1_phrase(composer, v1, v2, va, vc, key_root=67)
    
    mozart_transition(composer, v1, v2, va, vc)
    
    for _ in range(2):
        mozart_theme2_phrase(composer, v1, v2, va, vc, key_root=74)
    
    mozart_closing(composer, v1, v2, va, vc, key_root=74)
    
    if repeat:
        for _ in range(2):
            mozart_theme1_phrase(composer, v1, v2, va, vc, key_root=67)
        mozart_transition(composer, v1, v2, va, vc)
        for _ in range(2):
            mozart_theme2_phrase(composer, v1, v2, va, vc, key_root=74)
        mozart_closing(composer, v1, v2, va, vc, key_root=74)


def mozart_theme1_phrase(composer, v1, v2, va, vc, key_root):
    """Generate a 4-bar phrase of Theme 1 material."""
    melody_notes = [
        (0, 0.25, 90), (2, 0.25, 85), (4, 0.25, 85), (5, 0.5, 95),
        (5, 0.25, 80), (7, 0.25, 85), (9, 0.25, 85), (10, 0.5, 95),
        (10, 0.25, 80), (9, 0.25, 85), (7, 0.25, 85), (5, 0.5, 95),
        (4, 0.25, 80), (2, 0.25, 85), (0, 0.25, 85), (0, 0.5, 90),
        (0, 0.25, 85), (2, 0.25, 90), (4, 0.25, 85), (5, 0.75, 95),
        (7, 0.25, 85), (5, 0.25, 80), (4, 0.25, 85), (2, 0.5, 90),
        (4, 0.25, 85), (5, 0.25, 90), (7, 0.25, 85), (9, 0.5, 95),
        (10, 0.25, 85), (12, 0.25, 90), (12, 1.0, 100),
    ]
    
    for interval, dur, vel in melody_notes:
        composer.note(v1, key_root + interval, dur, vel)
    
    harmony_intervals = [0, 0, 3, 3, 5, 5, 3, 3, 0, 0, 3, 3, 5, 5, 3, 0]
    for i, interval in enumerate(harmony_intervals):
        vel = 70 if i % 4 == 0 else 60
        composer.note(v2, key_root - 12 + interval, 0.5, vel)
    
    for i in range(8):
        interval = [0, 0, 3, 3, 5, 5, 3, 0][i % 8]
        composer.note(va, key_root - 16 + interval, 0.5, 55)
    
    for i in range(8):
        for j, interval in enumerate([0, 5, 3, 5]):
            composer.note(vc, key_root - 24 + interval, 0.25, 60 if j == 0 else 55)


def mozart_theme2_phrase(composer, v1, v2, va, vc, key_root):
    """Generate a 4-bar phrase of Theme 2 material."""
    melody_notes = [
        (0, 0.5, 85), (-1, 0.25, 75), (0, 0.25, 85),
        (2, 0.5, 90), (0, 0.25, 75), (2, 0.25, 85),
        (4, 0.75, 95), (2, 0.25, 80),
        (0, 0.5, 85), (-1, 0.5, 80),
        (0, 0.25, 85), (2, 0.25, 80), (4, 0.25, 85), (5, 0.5, 90),
        (7, 0.25, 85), (5, 0.25, 80), (4, 0.25, 85), (2, 0.5, 90),
        (0, 0.5, 85), (2, 0.5, 80),
        (4, 0.25, 90), (5, 0.25, 85), (7, 0.25, 90), (9, 0.5, 95),
        (7, 0.25, 85), (5, 0.25, 85), (4, 0.25, 90), (2, 0.5, 90),
        (0, 0.5, 85), (2, 0.5, 80),
        (4, 0.25, 85), (2, 0.25, 90), (0, 0.25, 85), (-1, 0.25, 80),
        (0, 1.0, 95), (2, 0.5, 85), (0, 0.5, 90), (-1, 0.5, 85), (0, 1.0, 100),
    ]
    
    for interval, dur, vel in melody_notes:
        composer.note(v1, key_root + interval, dur, vel)
    
    for i in range(16):
        interval = [0, 4, 2, 4, 5, 4, 2, 0, 0, 4, 2, 4, 5, 4, 2, 0][i % 16]
        composer.note(v2, key_root - 12 + interval, 0.5, 60)
    
    for i in range(8):
        composer.note(va, key_root - 16, 0.5, 55)
    
    for i in range(8):
        for j, interval in enumerate([0, 5, 3, 5]):
            composer.note(vc, key_root - 24 + interval, 0.25, 60 if j == 0 else 55)


def mozart_transition(composer, v1, v2, va, vc):
    """Transition from G to D Major."""
    melody = [
        (12, 0.25, 90), (14, 0.25, 85), (16, 0.25, 90), (17, 0.5, 95),
        (16, 0.25, 85), (14, 0.25, 85), (12, 0.25, 90), (14, 0.5, 95),
        (12, 0.25, 85), (10, 0.25, 90), (12, 0.25, 85), (14, 0.25, 90),
        (16, 0.25, 85), (17, 0.25, 90), (19, 0.5, 100),
        (17, 0.5, 90), (16, 0.5, 85), (14, 0.5, 90),
    ]
    for interval, dur, vel in melody:
        composer.note(v1, 67 + interval, dur, vel)
    
    for _ in range(4):
        for n in [62, 64, 66, 67]:
            composer.note(v2, n, 0.25, 65)
    
    for _ in range(4):
        composer.note(va, 50, 0.5, 55)
        composer.note(va, 52, 0.5, 55)
    
    for n in [31, 33, 35, 38, 40, 38, 35, 38]:
        composer.note(vc, n, 0.5, 65)


def mozart_closing(composer, v1, v2, va, vc, key_root):
    """Closing section."""
    melody = [
        (0, 0.25, 90), (2, 0.25, 85), (4, 0.25, 90), (5, 0.5, 95),
        (4, 0.25, 85), (2, 0.25, 85), (0, 0.25, 90), (2, 0.5, 95),
        (4, 0.25, 90), (5, 0.25, 85), (7, 0.25, 90), (5, 0.5, 95),
        (4, 0.5, 85), (2, 0.5, 90), (0, 1.0, 100),
    ]
    for interval, dur, vel in melody:
        composer.note(v1, key_root + interval, dur, vel)
    
    for _ in range(4):
        composer.note(v2, key_root - 12, 0.5, 65)
        composer.note(va, key_root - 16, 0.5, 55)
        composer.note(vc, key_root - 24, 0.5, 65)


def generate_development(composer, v1, v2, va, vc):
    """Generate development section with modulation."""
    dev_keys = [64, 74, 60, 59, 57, 55, 62]
    
    for key in dev_keys:
        melody = [
            (0, 0.25, 85), (2, 0.25, 80), (4, 0.25, 85), (5, 0.5, 90),
            (4, 0.25, 80), (2, 0.25, 80), (0, 0.25, 85), (2, 0.5, 90),
            (4, 0.25, 85), (5, 0.25, 80), (7, 0.25, 85), (9, 0.5, 90),
            (7, 0.25, 80), (5, 0.25, 80), (4, 0.25, 85), (5, 0.5, 90),
        ]
        for interval, dur, vel in melody:
            composer.note(v1, key + interval, dur, vel)
        
        for i in range(8):
            composer.note(v2, key - 12 + (i % 5), 0.5, 55)
        for i in range(8):
            composer.note(va, key - 16 + (i % 3), 0.5, 50)
        for i in range(8):
            for j, interval in enumerate([0, 5, 3, 5]):
                composer.note(vc, key - 24 + interval, 0.25, 60 if j == 0 else 55)
    
    for _ in range(8):
        composer.note(v1, 62, 0.25, 75)
    for _ in range(8):
        composer.note(v2, 66, 0.25, 60)
    for _ in range(4):
        composer.note(va, 50, 0.5, 50)
    for _ in range(4):
        composer.note(vc, 38, 0.5, 55)


def generate_recapitulation(composer, v1, v2, va, vc):
    """Generate recapitulation - all in G Major."""
    for _ in range(2):
        mozart_theme1_phrase(composer, v1, v2, va, vc, key_root=67)
    
    transition_gmajor(composer, v1, v2, va, vc)
    
    for _ in range(2):
        mozart_theme2_phrase(composer, v1, v2, va, vc, key_root=79)
    
    mozart_closing(composer, v1, v2, va, vc, key_root=79)


def transition_gmajor(composer, v1, v2, va, vc):
    """Transition staying in G Major."""
    melody = [
        (12, 0.25, 90), (14, 0.25, 85), (16, 0.25, 90), (17, 0.5, 95),
        (16, 0.25, 85), (14, 0.25, 85), (12, 0.25, 90), (14, 0.5, 95),
        (12, 0.25, 85), (10, 0.25, 90), (12, 0.25, 85), (14, 0.25, 90),
        (12, 0.5, 95), (10, 0.5, 85), (9, 0.5, 90), (7, 0.5, 85),
    ]
    for interval, dur, vel in melody:
        composer.note(v1, 67 + interval, dur, vel)
    
    for _ in range(4):
        composer.note(v2, 62, 0.5, 65)
        composer.note(va, 50, 0.5, 55)
        composer.note(vc, 38, 0.5, 60)


def generate_coda(composer, v1, v2, va, vc):
    """Generate coda section."""
    for _ in range(3):
        melody = [
            (19, 0.25, 90), (21, 0.25, 85), (23, 0.25, 90), (24, 0.5, 100),
            (23, 0.25, 85), (21, 0.25, 90), (19, 0.25, 85), (18, 0.25, 80),
            (19, 1.0, 95),
            (21, 0.25, 90), (19, 0.25, 85), (18, 0.25, 90), (16, 0.25, 85),
            (14, 1.0, 95),
        ]
        for interval, dur, vel in melody:
            composer.note(v1, 67 + interval, dur, vel)
    
    final_chord(composer, v1, v2, va, vc, 67)


def generate_extended_coda(composer, v1, v2, va, vc):
    """Extended coda for duration."""
    for _ in range(4):
        melody = [
            (0, 0.25, 85), (4, 0.25, 90), (7, 0.25, 85), (12, 0.5, 95),
            (7, 0.25, 85), (4, 0.25, 90), (0, 0.25, 85), (4, 0.5, 90),
            (7, 0.25, 85), (12, 0.25, 90), (7, 0.25, 85), (4, 0.5, 90),
            (0, 0.5, 85), (4, 0.5, 90), (7, 1.0, 100),
        ]
        for interval, dur, vel in melody:
            composer.note(v1, 67 + interval, dur, vel)
        
        for _ in range(4):
            composer.note(v2, 55, 0.5, 60)
            composer.note(va, 55, 0.5, 55)
            composer.note(vc, 31, 0.5, 65)
    
    # Grand finale
    final_chord(composer, v1, v2, va, vc, 67)
    composer.note(v1, 79, 3.0, 110)
    composer.note(v2, 67, 3.0, 90)
    composer.note(va, 64, 3.0, 80)
    composer.note(vc, 31, 3.0, 95)


def final_chord(composer, v1, v2, va, vc, root):
    """Final tutti chord."""
    composer.note(v1, root + 12, 2.0, 100)
    composer.note(v2, root + 7, 2.0, 80)
    composer.note(va, root + 4, 2.0, 70)
    composer.note(vc, root, 2.0, 85)


if __name__ == '__main__':
    compose_mozart()
