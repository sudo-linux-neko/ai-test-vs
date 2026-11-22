// SPDX-License-Identifier: GPL-3.0-or-later
// Copyright (C) 2026 Vaibhav Agarwal

/**
 * Classical Music Composer - Frontend JavaScript
 * Handles audio generation, playback, and visualization
 */

let audioContext = null;
let analyser = null;
let animationId = null;

/**
 * Generate a piece via the API
 */
async function generatePiece(pieceId) {
    const loadingEl = document.getElementById(`loading-${pieceId}`);
    const statusEl = document.getElementById('player-status');
    const playerEl = document.getElementById('audio-player');
    
    if (loadingEl) loadingEl.classList.add('active');
    if (statusEl) statusEl.textContent = `Composing ${pieceId}...`;
    
    try {
        const response = await fetch(`/generate/${pieceId}`);
        const data = await response.json();
        
        if (data.success) {
            if (statusEl) {
                statusEl.textContent = `Playing: ${pieceId} (${data.duration} minutes)`;
            }
            
            // Play the generated audio
            if (data.wav && playerEl) {
                playerEl.src = data.wav;
                playerEl.play();
                initVisualizer(playerEl);
            } else if (data.midi && playerEl) {
                // Fallback to MIDI if WAV not available
                playerEl.src = data.midi;
            }
        } else {
            if (statusEl) statusEl.textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        if (statusEl) statusEl.textContent = `Error: ${error.message}`;
    } finally {
        if (loadingEl) loadingEl.classList.remove('active');
    }
}

/**
 * Initialize the audio visualizer
 */
function initVisualizer(audioElement) {
    if (!audioContext) {
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
        analyser = audioContext.createAnalyser();
        analyser.fftSize = 256;
    }
    
    const source = audioContext.createMediaElementSource(audioElement);
    source.connect(analyser);
    analyser.connect(audioContext.destination);
    
    const canvas = document.getElementById('visualizer');
    const ctx = canvas.getContext('2d');
    
    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);
    
    function draw() {
        animationId = requestAnimationFrame(draw);
        
        analyser.getByteFrequencyData(dataArray);
        
        ctx.fillStyle = '#1a0f0a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        const barWidth = (canvas.width / bufferLength) * 2.5;
        let x = 0;
        
        for (let i = 0; i < bufferLength; i++) {
            const barHeight = (dataArray[i] / 255) * canvas.height;
            
            // Gold gradient for bars
            const gradient = ctx.createLinearGradient(0, canvas.height, 0, canvas.height - barHeight);
            gradient.addColorStop(0, '#c9a227');
            gradient.addColorStop(1, '#e8c547');
            
            ctx.fillStyle = gradient;
            ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
            
            x += barWidth + 1;
        }
    }
    
    draw();
}

/**
 * Generate all pieces at once
 */
async function generateAll() {
    const statusEl = document.getElementById('player-status');
    if (statusEl) statusEl.textContent = 'Generating all compositions...';
    
    try {
        const response = await fetch('/generate_all');
        const data = await response.json();
        
        if (data.success) {
            if (statusEl) statusEl.textContent = 'All pieces generated!';
        }
    } catch (error) {
        if (statusEl) statusEl.textContent = `Error: ${error.message}`;
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const playerEl = document.getElementById('audio-player');
    if (playerEl) {
        playerEl.addEventListener('ended', () => {
            const statusEl = document.getElementById('player-status');
            if (statusEl) statusEl.textContent = 'Playback finished';
            if (animationId) cancelAnimationFrame(animationId);
        });
    }
});
