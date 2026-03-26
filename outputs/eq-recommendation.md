# Eq Recommendation

This is a mono, 24kHz FLAC recording, which means it’s limited in high-frequency detail (above 12kHz). However, for podcast narration, the voice is clear and usable. Here is how you can polish this to sound broadcast-ready.

### EQ Strategy (The "Broadcast" Presets)
To get that rich, radio-ready sound, apply the following adjustments in your EQ plugin:

*   **High-Pass Filter (Low-Cut):** Cut everything below **80Hz-100Hz**.
    *   *Why:* This eliminates the low-end rumble from the phone's handling and microphone pre-amp noise.
*   **Low-End/Proximity Effect (200Hz - 400Hz):** Perform a slight cut (2-3dB) in the **250Hz** region.
    *   *Why:* This is the "mud" range. Your voice has a bit of boxiness here due to the proximity effect of the phone mic; cutting it makes the voice sound less congested.
*   **Nasal Resonances (800Hz - 1.2kHz):** A light, surgical cut if it sounds too "honky" or nasal.
    *   *Why:* This helps smooth out the natural shape of the vocal cavity.
*   **Presence and Intelligibility (3kHz - 5kHz):** A gentle boost (2dB).
    *   *Why:* This helps the voice "cut through" the mix. It aids in consonant clarity, making your narration sound more professional.
*   **Air Frequencies (Above 10kHz):** A gentle high-shelf boost.
    *   *Why:* Because this is a 24kHz recording, there is not much information above 12kHz. A soft boost at the very top can help "brighten" the recording, though it won't add true detail.

### Recommended Processing
To achieve the professional, "held" quality required for podcasting, I recommend this signal chain:

1.  **De-Esser:** This is crucial. Even if sibilance isn't currently piercing, broadcast compression will raise the noise floor and likely amplify your "s" and "t" sounds. Use a De-Esser before compression to tame any harsh frequencies.
2.  **Compression (The "Glue"):** Apply a standard compressor with a ratio of **3:1 or 4:1**. Set your threshold so you are seeing about 3-6dB of gain reduction during louder parts.
    *   *Why:* Compression keeps the voice level consistent. It makes the quieter parts audible and keeps the loud outbursts from clipping, which is the hallmark of a "broadcast" sound.
3.  **Noise Reduction:** Since this was recorded on a mobile device, there is a low-level background hiss. Use a dedicated noise reduction plugin (like iZotope RX Voice De-noise or even a simple gate) to pull the floor down slightly when you aren't speaking.
4.  **Limiter:** Add a final Limiter on your master output with a ceiling of **-1.0 dB**. This ensures your podcast doesn't peak or distort.

**Final Tip:** Since you are recording on a mobile device, consistency in your distance to the microphone is key. Stay about 6-8 inches away. If you find your voice sounds "hollow," ensure you aren't in a room with too much echo, as the phone mic is very sensitive to reflections.
