# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

"""
Classical Music Composer - Web Application
Flask app for generating and playing classical compositions.
"""

from flask import Flask, render_template, send_file, jsonify, request
import os
import subprocess
import json
from compositions import compose_mozart, compose_vivaldi, compose_beethoven

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, 'audio')
SOUNDFONT_PATH = '/usr/share/sounds/sf2/TimGM6mb.sf2'

# Ensure audio directory exists
os.makedirs(AUDIO_DIR, exist_ok=True)

# Piece metadata
PIECES = {
    'mozart': {
        'title': 'Classical Serenade in G Major',
        'inspiration': 'Mozart — Eine Kleine Nachtmusik, K. 525',
        'tempo': 'Allegro (132 BPM)',
        'key': 'G Major',
        'duration': '~12 minutes',
        'instruments': 'String Quartet (Violin I, Violin II, Viola, Cello)',
        'form': 'Sonata-Allegro',
        'description': 'A bright, energetic work in Classical style featuring the famous rocket theme and elegant Alberti bass patterns.',
        'era': 'classical',
        'era_name': 'Classical Period (1750-1820)',
        'room': 'vienna'
    },
    'vivaldi': {
        'title': 'Spring Concerto in E Major',
        'inspiration': 'Vivaldi — The Four Seasons, "Spring": I. Allegro',
        'tempo': 'Allegro (120 BPM)',
        'key': 'E Major',
        'duration': '~7 minutes',
        'instruments': 'Solo Violin + String Orchestra',
        'form': 'Ritornello (ABACADAEA)',
        'description': 'A programmatic Baroque concerto evoking birdsong, flowing streams, thunderstorms, and pastoral celebrations.',
        'era': 'baroque',
        'era_name': 'Baroque Period (1600-1750)',
        'room': 'venice'
    },
    'beethoven': {
        'title': 'Moonlight Sonata in C# Minor',
        'inspiration': 'Beethoven — Piano Sonata No. 14, "Moonlight": I. Adagio sostenuto',
        'tempo': 'Adagio sostenuto (54 BPM)',
        'key': 'C# Minor',
        'duration': '~7 minutes',
        'instruments': 'Solo Piano',
        'form': 'Ternary (ABA\')',
        'description': 'A hauntingly beautiful nocturne with constant triplet arpeggios and a floating melody of deep melancholy.',
        'era': 'romantic',
        'era_name': 'Late Classical / Early Romantic (1800-1830)',
        'room': 'studio'
    }
}


def generate_all_pieces():
    """Generate all three compositions as MIDI files."""
    results = {}
    
    print("Generating Mozart composition...")
    mozart_mid, mozart_dur = compose_mozart()
    results['mozart'] = {'midi': mozart_mid, 'duration': mozart_dur}
    
    print("Generating Vivaldi composition...")
    vivaldi_mid, vivaldi_dur = compose_vivaldi()
    results['vivaldi'] = {'midi': vivaldi_mid, 'duration': vivaldi_dur}
    
    print("Generating Beethoven composition...")
    beethoven_mid, beethoven_dur = compose_beethoven()
    results['beethoven'] = {'midi': beethoven_mid, 'duration': beethoven_dur}
    
    return results


def midi_to_wav(midi_path, wav_path):
    """Convert MIDI to WAV using FluidSynth."""
    try:
        cmd = [
            'fluidsynth',
            '-ni', SOUNDFONT_PATH,
            midi_path,
            '-F', wav_path,
            '-r', '44100'
        ]
        subprocess.run(cmd, capture_output=True, timeout=120)
        return os.path.exists(wav_path)
    except Exception as e:
        print(f"Conversion error: {e}")
        return False


@app.route('/')
def index():
    """Main page with all three pieces."""
    return render_template('index.html', pieces=PIECES)


@app.route('/piece/<piece_id>')
def piece(piece_id):
    """Individual piece page."""
    if piece_id not in PIECES:
        return "Piece not found", 404
    return render_template('piece.html', piece=PIECES[piece_id], piece_id=piece_id)


@app.route('/generate/<piece_id>')
def generate_piece(piece_id):
    """Generate a specific piece."""
    try:
        if piece_id == 'mozart':
            midi_path, duration = compose_mozart()
        elif piece_id == 'vivaldi':
            midi_path, duration = compose_vivaldi()
        elif piece_id == 'beethoven':
            midi_path, duration = compose_beethoven()
        else:
            return jsonify({'error': 'Unknown piece'}), 400
        
        # Convert to WAV
        wav_path = midi_path.replace('.mid', '.wav')
        success = midi_to_wav(midi_path, wav_path)
        
        return jsonify({
            'success': True,
            'midi': f'/audio/{os.path.basename(midi_path)}',
            'wav': f'/audio/{os.path.basename(wav_path)}' if success else None,
            'duration': round(duration, 1)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/generate_all')
def generate_all():
    """Generate all pieces."""
    try:
        results = generate_all_pieces()
        
        # Convert all to WAV
        for piece_id, data in results.items():
            wav_path = data['midi'].replace('.mid', '.wav')
            midi_to_wav(data['midi'], wav_path)
        
        return jsonify({'success': True, 'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/audio/<filename>')
def serve_audio(filename):
    """Serve audio files."""
    path = os.path.join(AUDIO_DIR, filename)
    if os.path.exists(path):
        return send_file(path)
    return "File not found", 404


@app.route('/api/pieces')
def api_pieces():
    """API endpoint for piece metadata."""
    return jsonify(PIECES)


if __name__ == '__main__':
    print("Generating all compositions...")
    generate_all_pieces()
    print("Starting web server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
