# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

"""
Piece 2: Spring Concerto in E Major
Inspired by Vivaldi - The Four Seasons, "Spring": I. Allegro
Duration: ~7 minutes | Solo Violin + Strings | Allegro (~120 BPM)
"""

from .composer_engine import SequentialComposer
from .music_theory import *
from .patterns import *
import random

TEMPO_BPM = 120
TICKS_PER_BEAT = 480


def compose_vivaldi():
    """Compose a Baroque concerto in ritornello form."""
    composer = SequentialComposer(ticks_per_beat=TICKS_PER_BEAT)
    
    score_track = composer.create_track("Score/Tempo", 0)
    composer.set_tempo(score_track, TEMPO_BPM)
    composer.set_time_signature(score_track, 4, 4)
    
    solo_vln = composer.create_track("Solo Violin", INSTRUMENTS['violin'])
    vln1 = composer.create_track("Violin I", INSTRUMENTS['violin'])
    vln2 = composer.create_track("Violin II", INSTRUMENTS['violin'])
    viola = composer.create_track("Viola", INSTRUMENTS['viola'])
    cello = composer.create_track("Cello/Continuo", INSTRUMENTS['cello'])
    
    # Extended ritornello form for 5+ minute duration
    for cycle in range(4):  # 4 cycles for extended duration
        generate_ritornello_form(composer, solo_vln, vln1, vln2, viola, cello)
    
    # Final grand ritornello
    ritornello_a_final(composer, solo_vln, vln1, vln2, viola, cello, key_root=76)
    
    filename = '/home/neko/ai-test-vs/audio/vivaldi_spring_concerto.mid'
    composer.save(filename)
    
    duration_minutes = composer.track_positions[solo_vln] / TICKS_PER_BEAT / TEMPO_BPM
    print(f"Vivaldi-style piece composed: {filename}")
    print(f"Duration: {duration_minutes:.1f} minutes")
    return filename, duration_minutes


def generate_ritornello_form(composer, solo_vln, vln1, vln2, viola, cello):
    """Generate full ritornello form structure."""
    ritornello_a(composer, solo_vln, vln1, vln2, viola, cello, key_root=76)
    episode_birdsong(composer, solo_vln, vln1, vln2, viola, cello)
    ritornello_a_short(composer, solo_vln, vln1, vln2, viola, cello, key_root=76)
    episode_streams(composer, solo_vln, vln1, vln2, viola, cello)
    ritornella_a_variant(composer, solo_vln, vln1, vln2, viola, cello, key_root=76)
    episode_storm(composer, solo_vln, vln1, vln2, viola, cello)
    ritornello_a_short(composer, solo_vln, vln1, vln2, viola, cello, key_root=76)
    episode_pastoral(composer, solo_vln, vln1, vln2, viola, cello)
    ritornello_a_short(composer, solo_vln, vln1, vln2, viola, cello, key_root=83)
    episode_extended_solo(composer, solo_vln, vln1, vln2, viola, cello)


def ritornello_a(composer, solo_vln, vln1, vln2, viola, cello, key_root):
    """Main ritornello theme in E Major."""
    solo_melody = [
        (0, 0.25, 95), (4, 0.25, 90), (7, 0.25, 95), (11, 0.5, 100),
        (12, 0.25, 95), (11, 0.25, 90), (7, 0.25, 95), (4, 0.5, 90),
        (0, 0.25, 85), (4, 0.25, 90), (7, 0.25, 85), (11, 0.5, 95),
        (12, 0.25, 90), (11, 0.25, 85), (7, 0.25, 90), (4, 0.5, 95),
        (0, 0.5, 100), (0, 0.5, 95),
        (4, 0.25, 90), (7, 0.25, 95), (11, 0.25, 90), (12, 0.5, 100),
        (11, 0.25, 90), (7, 0.25, 95), (4, 0.25, 90), (0, 0.5, 95),
    ]
    
    for interval, dur, vel in solo_melody:
        composer.note(solo_vln, key_root + interval, dur, vel)
    
    for interval, dur, vel in solo_melody:
        composer.note(vln1, key_root + interval - 12, dur, vel - 20)
    
    for i in range(16):
        comp_interval = [0, 4, 7, 4, 0, 4, 7, 4, 0, 4, 7, 4, 0, 4, 7, 4][i]
        composer.note(vln2, key_root - 12 + comp_interval, 0.5, 60)
    
    for i in range(16):
        viola_note = [0, 0, 4, 4, 7, 7, 4, 4][i % 8]
        composer.note(viola, key_root - 24 + viola_note, 0.5, 55)
    
    for i in range(16):
        bass_note = [0, 0, 0, 0, 4, 4, 4, 4, 7, 7, 7, 7, 0, 0, 0, 0][i]
        composer.note(cello, key_root - 36 + bass_note, 0.5, 65)


def ritornello_a_short(composer, solo_vln, vln1, vln2, viola, cello, key_root):
    """Short version of ritornello theme."""
    solo_melody = [
        (0, 0.25, 95), (4, 0.25, 90), (7, 0.25, 95), (11, 0.5, 100),
        (12, 0.25, 95), (11, 0.25, 90), (7, 0.25, 95), (4, 0.5, 90),
        (0, 0.5, 100), (0, 0.5, 95),
        (4, 0.25, 90), (7, 0.25, 95), (11, 0.25, 90), (12, 0.5, 100),
    ]
    
    for interval, dur, vel in solo_melody:
        composer.note(solo_vln, key_root + interval, dur, vel)
    
    for interval, dur, vel in solo_melody:
        composer.note(vln1, key_root + interval - 12, dur, vel - 25)
    
    for i in range(8):
        comp_interval = [0, 4, 7, 4, 0, 4, 7, 4][i]
        composer.note(vln2, key_root - 12 + comp_interval, 0.5, 55)
    
    for i in range(8):
        viola_note = [0, 0, 4, 4, 7, 7, 4, 4][i]
        composer.note(viola, key_root - 24 + viola_note, 0.5, 50)
    
    for i in range(8):
        bass_note = [0, 0, 0, 0, 4, 4, 4, 4][i]
        composer.note(cello, key_root - 36 + bass_note, 0.5, 60)


def ritornella_a_variant(composer, solo_vln, vln1, vln2, viola, cello, key_root):
    """Variant of ritornello with different figuration."""
    solo_melody = [
        (0, 0.125, 95), (4, 0.125, 90), (7, 0.125, 95), (4, 0.125, 90),
        (7, 0.125, 95), (11, 0.125, 100), (7, 0.125, 95), (11, 0.125, 100),
        (12, 0.25, 95), (11, 0.25, 90), (7, 0.25, 95), (4, 0.5, 90),
        (0, 0.125, 85), (4, 0.125, 90), (7, 0.125, 85), (4, 0.125, 80),
        (7, 0.125, 85), (11, 0.125, 90), (7, 0.125, 85), (11, 0.125, 90),
        (12, 0.5, 100), (7, 0.5, 95), (4, 0.5, 90), (0, 1.0, 100),
    ]
    
    for interval, dur, vel in solo_melody:
        composer.note(solo_vln, key_root + interval, dur, vel)
    
    for interval, dur, vel in solo_melody:
        composer.note(vln1, key_root + interval - 12, dur, vel - 25)
    
    for i in range(12):
        composer.note(vln2, key_root - 12, 0.5, 55)
    for i in range(12):
        composer.note(viola, key_root - 24, 0.5, 50)
    for i in range(12):
        composer.note(cello, key_root - 36, 0.5, 60)


def ritornello_a_final(composer, solo_vln, vln1, vln2, viola, cello, key_root):
    """Final ritornello - grand statement."""
    ritornello_a(composer, solo_vln, vln1, vln2, viola, cello, key_root)
    
    solo_finale = [
        (12, 0.25, 100), (11, 0.25, 95), (7, 0.25, 100), (4, 0.25, 95),
        (7, 0.25, 100), (11, 0.25, 95), (12, 0.5, 105),
        (11, 0.25, 100), (7, 0.25, 95), (4, 0.25, 100), (0, 0.5, 105),
        (0, 1.0, 110), (0, 1.0, 115),
    ]
    
    for interval, dur, vel in solo_finale:
        composer.note(solo_vln, key_root + interval, dur, vel)
    
    for interval, dur, vel in solo_finale:
        composer.note(vln1, key_root + interval - 12, dur, vel - 15)
        composer.note(vln2, key_root + interval - 12, dur, vel - 25)
    
    for i in range(10):
        composer.note(viola, key_root - 24, 0.5, 65)
        composer.note(cello, key_root - 36, 0.5, 75)


def episode_birdsong(composer, solo_vln, vln1, vln2, viola, cello):
    """Birdsong episode."""
    for _ in range(4):
        birdsong_figure(composer, solo_vln, 88, 90)
        birdsong_figure(composer, solo_vln, 86, 85)
        composer.note(solo_vln, 88, 0.5, 90)
        birdsong_figure(composer, solo_vln, 91, 85)
    
    for i in range(16):
        composer.note(vln1, 76, 0.25, 45)
        composer.note(vln2, 76, 0.25, 40)
    
    for i in range(8):
        composer.note(viola, 64, 0.5, 40)
        composer.note(cello, 52, 0.5, 50)


def episode_streams(composer, solo_vln, vln1, vln2, viola, cello):
    """Flowing streams episode."""
    flowing_water_figure(composer, solo_vln, 76, 4.0, 80)
    flowing_water_figure(composer, solo_vln, 79, 4.0, 85)
    flowing_water_figure(composer, solo_vln, 83, 4.0, 80)
    flowing_water_figure(composer, solo_vln, 76, 4.0, 85)
    
    for i in range(32):
        composer.note(vln1, 76, 0.125, 50)
        composer.note(vln2, 72, 0.125, 45)
    
    for i in range(16):
        composer.note(viola, 64, 0.5, 45)
        composer.note(cello, 52, 0.5, 55)


def episode_storm(composer, solo_vln, vln1, vln2, viola, cello):
    """Thunderstorm episode."""
    thunder_effect(composer, cello, 52, 3.0, 90)
    thunder_effect(composer, viola, 60, 3.0, 85)
    
    for i in range(16):
        note = 76 + (i % 12)
        composer.note(solo_vln, note, 0.125, 95)
    
    for i in range(16):
        note = 88 - (i % 12)
        composer.note(solo_vln, note, 0.125, 90)
    
    for i in range(8):
        composer.note(vln1, 76, 0.25, 80)
        composer.note(vln2, 72, 0.25, 75)
    
    thunder_effect(composer, cello, 52, 2.0, 95)
    thunder_effect(composer, viola, 60, 2.0, 90)
    
    for i in range(20):
        note = 76 + random.randint(-5, 12)
        composer.note(solo_vln, note, 0.1, 85)


def episode_pastoral(composer, solo_vln, vln1, vln2, viola, cello):
    """Pastoral dance episode."""
    pastoral_drone(composer, cello, 76, 8.0, 55)
    pastoral_drone(composer, viola, 69, 8.0, 50)
    
    pastoral_melody = [
        (76, 0.5, 85), (79, 0.5, 90), (83, 0.5, 85), (79, 0.5, 90),
        (76, 0.5, 85), (79, 0.5, 90), (83, 1.0, 95),
        (83, 0.5, 90), (86, 0.5, 95), (83, 0.5, 90), (79, 0.5, 85),
        (76, 0.5, 90), (74, 0.5, 85), (76, 1.0, 95),
    ]
    
    for _ in range(3):
        for note, dur, vel in pastoral_melody:
            composer.note(solo_vln, note, dur, vel)
    
    for i in range(24):
        composer.note(vln1, 76, 0.5, 55)
        composer.note(vln2, 72, 0.5, 50)


def episode_extended_solo(composer, solo_vln, vln1, vln2, viola, cello):
    """Extended solo violin episode."""
    for i in range(8):
        composer.note(solo_vln, 76 + i, 0.125, 90)
    for i in range(8):
        composer.note(solo_vln, 84 - i, 0.125, 85)
    
    for _ in range(4):
        composer.note(solo_vln, 76, 0.25, 85)
        composer.note(solo_vln, 80, 0.25, 90)
        composer.note(solo_vln, 83, 0.25, 95)
        composer.note(solo_vln, 88, 0.25, 90)
        composer.note(solo_vln, 83, 0.25, 85)
        composer.note(solo_vln, 80, 0.25, 80)
    
    trill(composer, solo_vln, 88, 89, 1.0, 90)
    trill(composer, solo_vln, 86, 87, 1.0, 85)
    trill(composer, solo_vln, 83, 84, 1.0, 90)
    
    for i in range(16):
        composer.note(cello, 52, 0.5, 50)
        composer.note(viola, 60, 0.5, 45)
    for i in range(16):
        composer.note(vln1, 76, 0.5, 40)
        composer.note(vln2, 72, 0.5, 35)


if __name__ == '__main__':
    compose_vivaldi()
