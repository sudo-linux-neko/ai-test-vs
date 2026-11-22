# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

"""
Period-authentic musical patterns for Classical, Baroque, and Romantic composition.
"""

from .music_theory import *
import random


def alberti_bass(composer, track_idx, chord_notes, duration_beats=1.0, velocity=60):
    """
    Generate Alberti bass pattern (low-high-middle-high).
    Classic Classical period accompaniment pattern.
    """
    if len(chord_notes) < 3:
        return 0
    
    root = chord_notes[0]
    third = chord_notes[1] if len(chord_notes) > 1 else root + 4
    fifth = chord_notes[2] if len(chord_notes) > 2 else root + 7
    
    pattern_notes = [root - 12, fifth - 12, third - 12, fifth - 12]
    beat_div = duration_beats / 4.0
    
    for n in pattern_notes:
        composer.note(track_idx, n, beat_div, velocity)
    
    return duration_beats


def baroque_motor_rhythm(composer, track_idx, note_val, duration_beats=1.0, velocity=80):
    """Generate Baroque motor rhythm (continuous sixteenth notes)."""
    num_notes = int(duration_beats * 4)
    if num_notes == 0:
        return 0
    dur = duration_beats / num_notes
    
    for _ in range(num_notes):
        composer.note(track_idx, note_val, dur, velocity)
    
    return duration_beats


def triplet_arpeggio(composer, track_idx, chord_notes, duration_beats=1.0, velocity=50):
    """Generate triplet arpeggio pattern (Moonlight Sonata style)."""
    if len(chord_notes) < 3:
        return 0
    
    pattern_notes = [chord_notes[0] - 12, chord_notes[1] - 12, chord_notes[2] - 12]
    beat_div = duration_beats / 3.0
    
    for n in pattern_notes:
        composer.note(track_idx, n, beat_div, velocity)
    
    return duration_beats


def scales_run(composer, track_idx, start_note, num_notes, direction='up', 
              beat_dur=0.25, velocity=80):
    """Generate a scale run (common in Baroque and Classical music)."""
    current = start_note
    total = 0
    
    for i in range(num_notes):
        composer.note(track_idx, current, beat_dur, velocity)
        total += beat_dur
        if direction == 'up':
            current += 1 if i % 2 == 0 else 2
        else:
            current -= 1 if i % 2 == 0 else 2
    
    return total


def mordent(composer, track_idx, main_note, beat_dur=0.25, velocity=80):
    """Generate a mordent ornament (main-note-lower-main)."""
    composer.note(track_idx, main_note, beat_dur / 3, velocity)
    composer.note(track_idx, main_note - 1, beat_dur / 3, velocity)
    composer.note(track_idx, main_note, beat_dur / 3, velocity)
    return beat_dur


def trill(composer, track_idx, main_note, upper_note, total_beats=0.5, velocity=80):
    """Generate a trill ornament."""
    num_notes = int(total_beats * 8)
    if num_notes == 0:
        return 0
    dur = total_beats / num_notes
    
    for i in range(num_notes):
        note = main_note if i % 2 == 0 else upper_note
        composer.note(track_idx, note, dur, velocity)
    
    return total_beats


def turn(composer, track_idx, main_note, beat_dur=0.25, velocity=80):
    """Generate a turn ornament (upper-main-lower-main)."""
    upper = main_note + 1
    lower = main_note - 1
    sub_beat = beat_dur / 4
    
    composer.note(track_idx, upper, sub_beat, velocity)
    composer.note(track_idx, main_note, sub_beat, velocity)
    composer.note(track_idx, lower, sub_beat, velocity)
    composer.note(track_idx, main_note, sub_beat, velocity)
    
    return beat_dur


def birdsong_figure(composer, track_idx, base_note, velocity=85):
    """Generate a bird-like melodic figure (for Vivaldi Spring)."""
    pattern = [base_note, base_note + 2, base_note + 4, base_note + 2, base_note]
    durs = [0.125, 0.125, 0.25, 0.125, 0.25]
    
    for note, dur in zip(pattern, durs):
        composer.note(track_idx, note, dur, velocity)
    
    return sum(durs)


def thunder_effect(composer, track_idx, base_note, duration_beats=2.0, velocity=90):
    """Generate thunder-like tremolo effect (for Vivaldi Spring storm)."""
    num_notes = int(duration_beats * 8)
    if num_notes == 0:
        return 0
    dur = duration_beats / num_notes
    
    for i in range(num_notes):
        note = base_note if i % 2 == 0 else base_note - 2
        v = velocity - random.randint(0, 15)
        composer.note(track_idx, note, dur, v)
    
    return duration_beats


def flowing_water_figure(composer, track_idx, base_note, duration_beats=2.0, velocity=70):
    """Generate flowing water arpeggio figure (for Vivaldi)."""
    pattern = [0, 4, 7, 4, 0, 4, 7, 12]
    num_cycles = int(duration_beats / 2)
    beat_per_note = 2.0 / len(pattern)
    
    for _ in range(num_cycles):
        for interval in pattern:
            composer.note(track_idx, base_note + interval, beat_per_note, velocity)
    
    return num_cycles * 2.0


def pastoral_drone(composer, track_idx, drone_note, duration_beats, velocity=60):
    """Generate a drone bass note (pastoral/bagpipe effect)."""
    composer.note(track_idx, drone_note - 12, duration_beats, velocity)
    return duration_beats

