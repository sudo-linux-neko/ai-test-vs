# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

"""
Composer Engine
Core engine for generating MIDI compositions with period-authentic patterns.
"""

import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
from .music_theory import *
import random


class SequentialComposer:
    """Composes music sequentially, tracking time position."""
    
    def __init__(self, ticks_per_beat=480):
        self.ticks_per_beat = ticks_per_beat
        self.midi = MidiFile(ticks_per_beat=ticks_per_beat)
        self.tracks = []
        self.track_positions = []
        
    def create_track(self, name, instrument=0):
        """Create a new track with sequential writing capability."""
        track = MidiTrack()
        track.append(MetaMessage('track_name', name=name, time=0))
        track.append(Message('program_change', program=instrument, time=0))
        self.tracks.append(track)
        self.track_positions.append(0)
        return len(self.tracks) - 1
    
    def set_tempo(self, track_idx, bpm):
        """Set tempo for a track."""
        tempo = mido.bpm2tempo(bpm)
        self.tracks[track_idx].append(MetaMessage('set_tempo', tempo=tempo, time=0))
    
    def set_time_signature(self, track_idx, num=4, den=4):
        """Set time signature."""
        self.tracks[track_idx].append(MetaMessage('time_signature',
                                                    numerator=num, denominator=den, time=0))
    
    def note(self, track_idx, midi_note, duration_beats, velocity=80):
        """Add a note at current position, advancing time."""
        dur_ticks = int(duration_beats * self.ticks_per_beat)
        self.tracks[track_idx].append(Message('note_on', note=midi_note,
                                               velocity=velocity, time=0))
        self.tracks[track_idx].append(Message('note_off', note=midi_note,
                                               velocity=0, time=dur_ticks))
        self.track_positions[track_idx] += dur_ticks
        return duration_beats
    
    def rest(self, track_idx, duration_beats):
        """Add a rest (silence)."""
        dur_ticks = int(duration_beats * self.ticks_per_beat)
        self.tracks[track_idx].append(Message('note_on', note=0,
                                               velocity=0, time=dur_ticks))
        self.tracks[track_idx].append(Message('note_off', note=0, velocity=0, time=0))
        self.track_positions[track_idx] += dur_ticks
        return duration_beats
    
    def chord(self, track_idx, midi_notes, duration_beats, velocity=80):
        """Add a chord at current position."""
        dur_ticks = int(duration_beats * self.ticks_per_beat)
        for i, note in enumerate(midi_notes):
            t = 0 if i > 0 else 0
            self.tracks[track_idx].append(Message('note_on', note=note,
                                                   velocity=velocity, time=t))
        for i, note in enumerate(midi_notes):
            t = dur_ticks if i == 0 else 0
            self.tracks[track_idx].append(Message('note_off', note=note,
                                                   velocity=0, time=t))
        self.track_positions[track_idx] += dur_ticks
        return duration_beats
    
    def save(self, filename):
        """Save all tracks to MIDI file."""
        for track in self.tracks:
            self.midi.tracks.append(track)
        self.midi.save(filename)
        return filename
    
    def get_duration_beats(self, track_idx):
        """Get total duration in beats for a track."""
        return self.track_positions[track_idx] / self.ticks_per_beat
