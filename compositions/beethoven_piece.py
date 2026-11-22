# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

"""
Piece 3: Moonlight Sonata in C# Minor
Inspired by Beethoven - Piano Sonata No. 14, "Moonlight": I. Adagio sostenuto
Duration: ~7 minutes | Solo Piano | Adagio sostenuto (~54 BPM)
"""

from .composer_engine import SequentialComposer
from .music_theory import *
from .patterns import *

TEMPO_BPM = 54
TICKS_PER_BEAT = 480


def compose_beethoven():
    """Compose a ternary form piece in C# minor."""
    composer = SequentialComposer(ticks_per_beat=TICKS_PER_BEAT)
    
    score_track = composer.create_track("Score/Tempo", 0)
    composer.set_tempo(score_track, TEMPO_BPM)
    composer.set_time_signature(score_track, 4, 4)
    
    piano_rh = composer.create_track("Piano Right Hand", INSTRUMENTS['piano'])
    piano_lh = composer.create_track("Piano Left Hand", INSTRUMENTS['piano'])
    
    # Ternary form: A - B - A' - Coda
    generate_section_a(composer, piano_rh, piano_lh)
    generate_section_b(composer, piano_rh, piano_lh)
    generate_section_a_prime(composer, piano_rh, piano_lh)
    generate_coda(composer, piano_rh, piano_lh)
    
    filename = '/home/neko/ai-test-vs/audio/beethoven_moonlight_sonata.mid'
    composer.save(filename)
    
    duration_minutes = composer.track_positions[piano_rh] / TICKS_PER_BEAT / TEMPO_BPM
    print(f"Beethoven-style piece composed: {filename}")
    print(f"Duration: {duration_minutes:.1f} minutes")
    return filename, duration_minutes


def generate_section_a(composer, rh, lh):
    """Section A: The famous triplet arpeggios with haunting melody."""
    # 8 repetitions of the main pattern for duration
    for _ in range(8):
        moonlight_pattern(composer, rh, lh, 61, 4.0)   # C# minor
        moonlight_pattern(composer, rh, lh, 64, 4.0)   # E major
        moonlight_pattern(composer, rh, lh, 68, 4.0)   # G# minor
        moonlight_pattern(composer, rh, lh, 61, 4.0)   # C# minor
        moonlight_pattern(composer, rh, lh, 59, 4.0)   # B major
        moonlight_pattern(composer, rh, lh, 61, 4.0)   # C# minor


def moonlight_pattern(composer, rh, lh, root, duration_beats):
    """Generate one bar of moonlight pattern."""
    # Left hand: triplet arpeggios
    chord_tones = [root - 12, root - 8, root - 5]  # Root, 3rd, 5th below
    
    num_triplets = int(duration_beats / 1.0)  # One pattern per beat
    for _ in range(num_triplets):
        triplet_arpeggio(composer, lh, chord_tones, 1.0, 45)
    
    # Right hand: haunting melody floating above
    melody_intervals = [12, 16, 19, 16, 12, 7, 4, 7]  # Octave + chord tones
    melody_durs = [0.5, 0.5, 1.0, 0.5, 0.5, 1.0, 0.5, 0.5]
    
    for interval, dur in zip(melody_intervals, melody_durs):
        vel = 55 if interval == 19 else 50  # Slight emphasis on high note
        composer.note(rh, root + interval, dur, vel)


def generate_section_b(composer, rh, lh):
    """Section B: More intense, with louder dynamics and fuller texture."""
    for _ in range(6):
        # More dramatic version of the pattern
        moonlight_pattern_intense(composer, rh, lh, 61, 4.0)   # C# minor
        moonlight_pattern_intense(composer, rh, lh, 66, 4.0)   # F# minor
        moonlight_pattern_intense(composer, rh, lh, 69, 4.0)   # A major
        moonlight_pattern_intense(composer, rh, lh, 61, 4.0)   # C# minor


def moonlight_pattern_intense(composer, rh, lh, root, duration_beats):
    """More intense moonlight pattern with fuller chords."""
    # Left hand: fuller arpeggios
    chord_tones = [root - 12, root - 8, root - 5, root - 1]
    
    num_triplets = int(duration_beats / 1.0)
    for _ in range(num_triplets):
        for i, tone in enumerate(chord_tones):
            composer.note(lh, tone, 1.0 / len(chord_tones), 50 + i * 3)
    
    # Right hand: more ornamented melody
    melody_intervals = [12, 16, 19, 24, 19, 16, 12, 7, 4, 7, 12, 16]
    melody_durs = [0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25]
    
    for interval, dur in zip(melody_intervals, melody_durs):
        vel = 60 if interval >= 19 else 55
        composer.note(rh, root + interval, dur, vel)


def generate_section_a_prime(composer, rh, lh):
    """Section A': Return of opening material, even more sparse."""
    for _ in range(6):
        moonlight_pattern(composer, rh, lh, 61, 4.0)
        moonlight_pattern(composer, rh, lh, 64, 4.0)
        moonlight_pattern(composer, rh, lh, 68, 4.0)
        moonlight_pattern(composer, rh, lh, 61, 4.0)
    
    # Gradually thinning texture
    for _ in range(4):
        sparse_pattern(composer, rh, lh, 61, 4.0)


def sparse_pattern(composer, rh, lh, root, duration_beats):
    """Very sparse pattern near the end."""
    # Left hand: just single notes
    composer.note(lh, root - 12, 1.0, 40)
    composer.note(lh, root - 8, 1.0, 35)
    composer.note(lh, root - 5, 1.0, 40)
    composer.note(lh, root - 12, 1.0, 35)
    
    # Right hand: single sustained notes
    composer.note(rh, root + 12, 2.0, 45)
    composer.note(rh, root + 7, 2.0, 40)


def generate_coda(composer, rh, lh):
    """Coda: Final fading gestures."""
    # Final C# minor chords fading away
    for _ in range(4):
        sparse_pattern(composer, rh, lh, 61, 4.0)
    
    # Final notes - fading to nothing
    composer.note(lh, 37, 4.0, 35)  # Low C#
    composer.note(rh, 73, 4.0, 40)  # High C#
    
    composer.note(lh, 40, 4.0, 30)  # E
    composer.note(rh, 76, 4.0, 35)  # E
    
    composer.note(lh, 43, 6.0, 25)  # G# - final note, very soft
    composer.note(rh, 73, 6.0, 30)  # C# - resolution


if __name__ == '__main__':
    compose_beethoven()
