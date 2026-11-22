# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

"""
Core Music Theory Module
Provides fundamental music theory utilities for composition.
"""

# Note name to MIDI number mapping
NOTE_TO_MIDI = {
    'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
    'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
}

# Scale degree intervals (semitones)
MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]
MINOR_SCALE_NATURAL = [0, 2, 3, 5, 7, 8, 10]
MINOR_SCALE_HARMONIC = [0, 2, 3, 5, 7, 8, 11]
MINOR_SCALE_MELODIC = [0, 2, 3, 5, 7, 9, 11]

# Chord qualities by scale degree (major key)
MAJOR_KEY_CHORDS = {
    1: 'major', 2: 'minor', 3: 'minor', 4: 'major', 5: 'major',
    6: 'minor', 7: 'diminished'
}

# Chord qualities by scale degree (minor key)
MINOR_KEY_CHORDS = {
    1: 'minor', 2: 'diminished', 3: 'major', 4: 'minor', 5: 'minor',
    6: 'major', 7: 'major'
}

# Circle of fifths for key relationships
CIRCLE_OF_FIFTHS_MAJOR = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']
CIRCLE_OF_FIFTHS_MINOR = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F', 'C', 'G', 'D']

# Standard chord progressions
AUTHENTIC_CADENCE = [5, 1]  # V-I
PLAGAL_CADENCE = [4, 1]     # IV-I
DECEPTIVE_CADENCE = [5, 6]  # V-vi
HALF_CADENCE = [1, 5]       # I-V


def note_to_midi(note_name, octave):
    """Convert note name and octave to MIDI number."""
    return NOTE_TO_MIDI[note_name] + (octave + 1) * 12


def midi_to_note(midi_num):
    """Convert MIDI number to note name and octave."""
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (midi_num // 12) - 1
    note = notes[midi_num % 12]
    return note, octave


def get_scale_notes(root, scale_type='major'):
    """Get all notes in a scale."""
    root_midi = NOTE_TO_MIDI[root]
    if scale_type == 'major':
        intervals = MAJOR_SCALE
    elif scale_type == 'minor_natural':
        intervals = MINOR_SCALE_NATURAL
    elif scale_type == 'minor_harmonic':
        intervals = MINOR_SCALE_HARMONIC
    elif scale_type == 'minor_melodic':
        intervals = MINOR_SCALE_MELODIC
    else:
        intervals = MAJOR_SCALE
    
    return [(root_midi + interval) % 12 for interval in intervals]


def get_chord_notes(root, quality='major', inversion=0):
    """Get the notes of a chord."""
    root_midi = NOTE_TO_MIDI[root]
    
    if quality == 'major':
        intervals = [0, 4, 7]
    elif quality == 'minor':
        intervals = [0, 3, 7]
    elif quality == 'diminished':
        intervals = [0, 3, 6]
    elif quality == 'augmented':
        intervals = [0, 4, 8]
    elif quality == 'dominant7':
        intervals = [0, 4, 7, 10]
    elif quality == 'major7':
        intervals = [0, 4, 7, 11]
    elif quality == 'minor7':
        intervals = [0, 3, 7, 10]
    elif quality == 'diminished7':
        intervals = [0, 3, 6, 9]
    else:
        intervals = [0, 4, 7]
    
    notes = [(root_midi + interval) % 12 for interval in intervals]
    
    # Apply inversion
    for _ in range(inversion):
        notes.append(notes.pop(0) + 12)
    
    return notes


def get_diatonic_chord(key_root, scale_degree, key_type='major'):
    """Get the diatonic chord at a scale degree."""
    scale_notes = get_scale_notes(key_root, key_type if key_type == 'major' else 'minor_natural')
    root = scale_notes[scale_degree - 1]
    
    if key_type == 'major':
        quality = MAJOR_KEY_CHORDS[scale_degree]
    else:
        quality = MINOR_KEY_CHORDS[scale_degree]
    
    # Convert root number back to note name
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    root_name = notes[root]
    
    return root_name, quality


def get_relative_minor(major_key):
    """Get the relative minor of a major key."""
    major_idx = CIRCLE_OF_FIFTHS_MAJOR.index(major_key) if major_key in CIRCLE_OF_FIFTHS_MAJOR else 0
    return CIRCLE_OF_FIFTHS_MINOR[major_idx]


def get_relative_major(minor_key):
    """Get the relative major of a minor key."""
    minor_idx = CIRCLE_OF_FIFTHS_MINOR.index(minor_key) if minor_key in CIRCLE_OF_FIFTHS_MINOR else 0
    return CIRCLE_OF_FIFTHS_MAJOR[minor_idx]


def get_dominant(key):
    """Get the dominant key."""
    key_idx = NOTE_TO_MIDI[key]
    dominant_idx = (key_idx + 7) % 12
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return notes[dominant_idx]


def get_subdominant(key):
    """Get the subdominant key."""
    key_idx = NOTE_TO_MIDI[key]
    subdom_idx = (key_idx + 5) % 12
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return notes[subdom_idx]


# Instrument MIDI program numbers
INSTRUMENTS = {
    'piano': 0,
    'bright_acoustic_piano': 1,
    'electric_piano': 4,
    'harpsichord': 6,
    'celesta': 8,
    'violin': 40,
    'viola': 41,
    'cello': 42,
    'contrabass': 43,
    'tremolo_strings': 44,
    'pizzicato_strings': 45,
    'orchestral_harp': 46,
    'string_ensemble_1': 48,
    'string_ensemble_2': 49,
    'synth_strings': 50,
    'choir_aahs': 52,
    'trumpet': 56,
    'trombone': 57,
    'french_horn': 60,
    'alto_sax': 65,
    'oboe': 68,
    'bassoon': 70,
    'clarinet': 71,
    'flute': 73,
    'recorder': 74,
    'pipe_organ': 19,
}

# Dynamics (MIDI velocity)
DYNAMICS = {
    'ppp': 20, 'pp': 35, 'p': 50, 'mp': 65,
    'mf': 75, 'f': 90, 'ff': 105, 'fff': 120
}
