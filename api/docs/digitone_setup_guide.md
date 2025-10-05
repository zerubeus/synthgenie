# Digitone Setup Guide for SynthGenie

## MIDI Configuration Requirements

For SynthGenie to control your Digitone via MIDI, you must configure the Digitone's MIDI settings correctly.

### Required Settings

1. **Access MIDI CONFIG Menu**
   - Press `[FUNC] + [SETTINGS]`
   - Navigate to **MIDI CONFIG** section

2. **Enable Auto Channel** (CRITICAL)
   - Set **Auto Channel: ON**
   - This automatically maps:
     - Track 1 → MIDI Channel 1
     - Track 2 → MIDI Channel 2
     - Track 3 → MIDI Channel 3
     - Track 4 → MIDI Channel 4
     - Track 5 → MIDI Channel 5
     - ... and so on up to Track 16 → MIDI Channel 16

3. **Other Recommended Settings**
   - **Receive CC**: ON (to receive Control Change messages)
   - **Receive NRPN**: ON (for future high-resolution parameter support)
   - **Param Output**: OFF (we're receiving MIDI, not sending parameter changes)
   - **Transport Receive**: Optional (for clock sync)

### Troubleshooting

#### Problem: MIDI messages sent but parameters don't change

**Symptoms:**
- UI shows "Sent 20 MIDI actions" with CC numbers
- Digitone display doesn't show parameter changes
- Sound doesn't match the requested design

**Solution:**
1. Verify **Auto Channel is ON** in MIDI CONFIG
2. Check that the track number in your prompt matches the track you're looking at
   - Example: "...on track 5" should target Track 5 on the Digitone
3. Ensure the correct machine is selected on that track
   - Example: FM Drum prompt requires FM Drum machine on that track
4. Check MIDI cable connection and MIDI device selection in UI

#### Problem: "Unknown format" shown in UI

**Cause:** Frontend display issue when MIDI CC field is null/undefined

**Impact:** Visual only - does not affect MIDI message sending

**Status:** Known issue, does not prevent functionality

### Verification Steps

After configuring MIDI settings:

1. **Test with a simple prompt:**
   ```
   Set filter cutoff to 100 using wavetone on track 1
   ```

2. **Watch the Digitone display:**
   - You should see the filter cutoff parameter change on Track 1
   - The knob position should update on screen

3. **Listen to the sound:**
   - Play a note on Track 1
   - The sound should be brighter (high filter cutoff)

### MIDI CC Reference

The Digitone accepts standard MIDI CC messages for most parameters. Here are some common ones:

#### Amp Envelope (works on all machines)
- Attack Time: CC 84
- Hold Time: CC 85
- Decay Time: CC 86
- Sustain Level: CC 87
- Release Time: CC 88

#### Filter (works on all machines)
- Frequency: CC 16
- Resonance: CC 17 (machine dependent)
- Type: CC 18 (machine dependent)

#### Machine-Specific Parameters
Each synthesis machine (FM Tone, FM Drum, Wavetone, Swarmer) uses CC 40-77 for machine-specific parameters across 4 SYN pages.

See the main MIDI specification in `digitone.md` for complete CC listings.

### Common Workflow

1. **Select a track and machine on Digitone:**
   - Navigate to desired track (1-16)
   - Choose machine (FM Tone, FM Drum, Wavetone, or Swarmer)

2. **Craft your prompt with track and machine:**
   ```
   Design a powerful techno kick drum on track 5 using FM drum
   ```

3. **Send prompt via SynthGenie UI:**
   - The agent will route to correct machine agent
   - MIDI CCs will be sent on channel 5
   - Parameters will update on Track 5

4. **Fine-tune manually:**
   - Adjust parameters on Digitone as needed
   - Use agent again with refinement prompts

### Reference

- **Digitone Manual**: Pages 74-77 (MIDI CONFIG section)
- **MIDI Specification**: Appendix C of Digitone manual
- **SynthGenie MIDI Audit**: `digitone_midi_audit.md`
