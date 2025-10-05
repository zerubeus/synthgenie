## APPENDIX C: MIDI

APPENDIX C: MIDI

```
This appendix lists the CC and NRPN specifications for the Digitone II. Please note that due to the large
number of controllable parameters and that the machines share the same CC values, it is not possible to
control high-resolution parameters using CC. Instead, you should use NRPN messages for this purpose.
```

### C.1 TRACK PARAMETERS

##### TRACK

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Mute 94 1 108
Track level 95 1 110
```

### C.2 TRIG PARAMETERS

##### TRIG PARAMETERS

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Note 3 3 0
Velocity 4 3 1
Length 5 3 2
Filter Trig 13
LFO Trig 14
Portamento Time 9 3 6
Portamento On/Off 65 3 7
```

### C.3 SOURCE PARAMETERS

##### SYN PAGE 1

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Data entry knob A (machine dependent) 40 1 73
Data entry knob B (machine dependent) 41 1 74
Data entry knob C (machine dependent) 42 1 75
Data entry knob D (machine dependent) 43 1 76
Data entry knob E (machine dependent) 44 1 77
Data entry knob F (machine dependent) 45 1 78
Data entry knob G (machine dependent) 46 1 79
Data entry knob H (machine dependent) 47 1 80
```

##### SYN PAGE 2

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Data entry knob A (machine dependent) 48 1 81
Data entry knob B (machine dependent) 49 1 82
Data entry knob C (machine dependent) 50 1 83
Data entry knob D (machine dependent) 51 1 84
Data entry knob E (machine dependent) 52 1 85
Data entry knob F (machine dependent) 53 1 86
Data entry knob G (machine dependent) 54 1 87
Data entry knob H (machine dependent) 55 1 88
```

##### APPENDIX C: MIDI

##### SYN PAGE 3

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Data entry knob A (machine dependent) 56 1 89
Data entry knob B (machine dependent) 57 1 90
Data entry knob C (machine dependent) 58 1 91
Data entry knob D (machine dependent) 59 1 92
Data entry knob E (machine dependent) 60 1 93
Data entry knob F (machine dependent) 61 1 94
Data entry knob G (machine dependent) 62 1 95
Data entry knob H (machine dependent) 63 1 96
```

##### SYN PAGE 4

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Data entry knob A (machine dependent) 70 1 97
Data entry knob B (machine dependent) 71 1 98
Data entry knob C (machine dependent) 72 1 99
Data entry knob D (machine dependent) 73 1 100
Data entry knob E (machine dependent) 74 1 101
Data entry knob F (machine dependent) 75 1 102
Data entry knob G (machine dependent) 76 1 103
Data entry knob H (machine dependent) 77 1 104
```

### C.4 FILTER PARAMETERS

##### FILTER

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Frequency 16 1 20
Data entry knob F (machine dependent) 17 1 21
Data entry knob G (machine dependent) 18 1 22
Env. Depth 24 1 26
Attack Time 20 1 16
Decay Time 21 1 17
Sustain Level 22 1 18
Release Time 23 1 19
Env. Delay 19 1 23
Key Tracking 26 1 69
Base 27 1 24
Width 28 1 25
Env. Reset 25 1 68
```

### C.5 AMP PARAMETERS

##### AMP

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Attack Time 84 1 30
Hold Time 85 1 31
Decay Time 86 1 32
Sustain Level 86 1 33
Release Time 88 1 34
```

##### APPENDIX C: MIDI

##### AMP

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Env. Reset 92 1 41
Mode 91 1 40
Pan 89 1 38
Volume 90 1 39
```

### C.6 EUCLIDEAN SEQUENCER PARAMETERS

##### AMP

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Pulse Generator 1 3 8
Pulse Generator 2 3 9
Euclidean Mode On/Off 3 14
Rotation Generator 1 3 11
Rotation Generator 2 3 12
Track Rotation 3 13
Boolean Operator 3 10
```

### C.7 FX PARAMETERS

##### AMP

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Bit Reduction 78 1 5
Overdrive 81 1 8
Sample Rate Reduction 79 1 6
SRR Routing 80 1 7
Overdrive Routing 82 1 9
Delay Send 30 1 36
Reverb Send 31 1 37
Chorus Send 29 1 35
```

### C.8 MOD PARAMETERS.

##### LFO 1

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Speed 102 1 42
Multiplier 103 1 43
Fade In/Out 104 1 44
Destination 105 1 45
Waveform 106 1 46
Start Phase/Slew 107 1 47
Trig Mode 108 1 48
Depth 109 1 49
```

##### LFO 2

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Speed 111 1 50
Multiplier 112 1 51
Fade In/Out 113 1 52
```

##### APPENDIX C: MIDI

##### LFO 2

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Destination 114 1 53
Waveform 115 1 54
Start Phase/Slew 116 1 55
Trig Mode 117 1 56
Depth 118 1 57
```

##### LFO 3

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Speed 1 58
Multiplier 1 59
Fade In/Out 1 60
Destination 1 61
Waveform 1 62
Start Phase/Slew 1 70
Trig Mode 1 71
Depth 1 72
```

### C.9 SEND FX PARAMETERS

##### DELAY

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Delay Time 21 2 0
Pingpong 22 2 1
Stereo Width 23 2 2
Feedback 24 2 3
Highpass Filter 25 2 4
Lowpass Filter 26 2 5
Reverb Send 27 2 6
Mix Volume 28 2 7
```

##### REVERB

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Predelay 29 2 8
Decay Time 30 2 9
Shelving Freq 31 2 10
Shelving Gain 89 2 11
Highpass Filter 90 2 12
Lowpass Filter 91 2 13
Mix Volume 92 2 15
```

##### CHORUS

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Depth 16 2 41
Speed 9 2 42
High Pass Filter 70 2 43
Width 71 2 44
```

##### APPENDIX C: MIDI

##### CHORUS

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Delay Send 12 2 45
Reverb Send 13 2 46
Mix Volume 14 2 47
```

### C.10 MIXER PARAMETERS

##### COMPRESSOR

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Threshold 111 2 16
Attack Time 112 2 17
Release Time 113 2 18
Makeup Gain 114 2 19
Pattern Volume 119 2 24
Ratio 115 2 20
Sidechain Source 116 2 21
Sidechain Filter 117 2 22
Dry/Wet Mix 118 2 23
```

##### EXTERNAL IN MIXER

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Dual Mono 82 2 40
Input L Level 72 2 30
Input L Pan 74 2 32
Input R Level 73 2 31
Input R Pan 75 2 33
Input L Delay Send 78 2 36
Input R Delay Send 79 2 37
Input L Reverb Send 80 2 38
Input R Reverb Send 81 2 39
Input L Chorus Send 76 2 34
Input R Chorus Send 77 2 35
Input L R Level 72 2 30
Input L R Balance 74 2 32
Input L R Delay Send 78 2 36
Input L R Reverb Send 80 2 38
Input L R Chorus Send 76 2 34
```

### C.11 VAL PARAMETERS

```
These are the CC VAL parameters on the [FLTR] and [AMP] pages for MIDI tracks.
```

```
CC VAL
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
VAL1 70 1 16
VAL2 71 1 17
VAL3 72 1 18
VAL4 73 1 19
VAL5 74 1 20
```

##### APPENDIX C: MIDI

##### CC VAL

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
VAL6 75 1 21
VAL7 76 1 22
VAL8 77 1 23
VAL9 78 1 60
VAL10 79 1 61
VAL11 80 1 62
VAL12 81 1 63
VAL13 82 1 64
VAL14 83 1 65
VAL15 84 1 66
VAL16 85 1 67
```

### C.12 MISC PARAMETERS

##### MISC

```
Parameter CC MSB CC LSB NRPN MSB NRPN LSB
Pattern Mute 110 1 109
Master Overdrive 17 2 50
```

## APPENDIX D: MODULATION DESTINATIONS

APPENDIX D: MODULATION DESTINATIONS

```
The following are the modulation destinations for the Digitone II’s LFOs:
```

```
AUDIO TRACKS
```

```
META: None
```

```
LFO1: Speed (Only available for LFO2/3)
LFO1: Multiplier (Only available for LFO2/3)
LFO1: Fade In/Out (Only available for LFO2/3)
LFO1: Waveform (Only available for LFO2/3)
LFO1: Start Phase (Only available for LFO2/3)
LFO1: Trig Mode (Only available for LFO2/3)
LFO1: Depth (Only available for LFO2/3)
LFO2: Speed (Only available for LFO3)
LFO2: Multiplier (Only available for LFO3)
LFO2: Fade In/Out (Only available for LFO3)
LFO2: Waveform (Only available for LFO3)
LFO2: Start Phase (Only available for LFO3)
LFO2: Trig Mode (Only available for LFO3)
LFO2: Depth (Only available for LFO3)
```

```
SYN: Data entry knob A, page 1– 4
(machine dependent.)
SYN: Data entry knob B, page 1– 4
(machine dependent)
SYN: Data entry knob C, page 1– 4
(machine dependent)
SYN: Data entry knob D, page 1– 4
(machine dependent)
SYN: Data entry knob E, page 1– 4
(machine dependent)
SYN: Data entry knob F, page 1– 4
(machine dependent)
SYN: Data entry knob G, page 1– 4
(machine dependent)
SYN: Data entry knob H, page 1– 4
(machine dependent)
```

```
FILTER: Attack Time
FILTER: Decay Time
FILTER: Sustain Level
FILTER: Release Time
FILTER: Frequency
FILTER: Data entry knob F (machine dependent)
FILTER: Data entry knob G (machine dependent)
FILTER: Envelope Depth
FILTER: Env. Delay
FILTER: Key Tracking
```

```
FILTER: Base
FILTER: Width
FILTER: Env. Reset
```

```
AMP: Attack Time
AMP: Hold Time
AMP: Decay Time
AMP: Sustain Level
AMP: Release Time
AMP: Pan
AMP: Volume
```

```
FX: Delay Send
FX: Reverb Send
FX: Chorus Send
FX: Bit Reduction
FX: SRR
FX: SRR Routing
FX: Overdrive
```

##### MIDI TRACKS

```
META: None
```

```
LFO1: Speed (Only available for LFO2)
LFO1: Multiplier (Only available for LFO2)
LFO1: Fade In/Out (Only available for LFO2)
LFO1: Waveform (Only available for LFO2)
LFO1: Start Phase (Only available for LFO2)
LFO1: Trig Mode (Only available for LFO2)
LFO1: Depth (Only available for LFO2)
```

```
SYN: Pitch Bend
SYN: Aftertouch
SYN: Mod Wheel
SYN: Breath Controller
```

```
CC: CC1–16 Values
```

## APPENDIX E: KEYBOARD SCALES

APPENDIX E: KEYBOARD SCALES

The following are the selectable scales for the KEYBOARD mode. For more information, please see: “8.5.1
KEYBOARD MODE” on page 24,

##### • CHROMATIC

##### • IONIAN (MAJOR)

##### • DORIAN

##### • PHRYGIAN

##### • LYDIAN

##### • MIXOLYDIAN

##### • AEOLIAN (MINOR)

##### • LOCRIAN

##### • PENTATONIC MINOR

##### • PENTATONIC MAJOR

##### • MELODIC MINOR

##### • HARMONIC MINOR

##### • WHOLE TONE

##### • BLUES

##### • COMBO MINOR

##### • PERSIAN

##### • I WATO

##### • IN-SEN

##### • HIRAJOSHI

##### • PELOG

##### • PHRYGIAN DOMINANT

##### • WHOLE-HALF DIMINISHED

##### • HALF-WHOLE DIMINISHED

##### • SPANISH

##### • MAJOR LOCRIAN

##### • SUPER LOCRIAN

- DORIAN b 2
- LYDIAN AUGMENTED
- LYDIAN DOMINANT
- DOUBLE HARMONIC MAJOR
- LYDIAN #2 #6
- ULTRAPHRYGIAN
- HUNGARIAN MINOR
- ORIENTAL
- IONIAN #2 #5
- LOCRIAN bb 3 bb 7

## INDEX

INDEX

```
+DRIVE 16 , 29
```

### A

##### ARPEGGIATOR 39

##### AUDIO ROUTING

```
Global 77
```

### B

##### BACKUP 20

##### BREATH CONTROLLER 39

### C

##### CHAINS 41

##### CHORD MODE 25

##### CHORUS 67

##### CHROMATIC MODE 24

##### CLASS COMPLIANT 20

##### COMPRESSOR 67

##### CONDITIONAL LOCKS 51

##### CONNECTORS 14

##### CONTROL ALL 19

```
Configuration 35
COPY, PASTE AND CLEAR 52
CREDITS AND CONTACT INFORMATION 88
```

### D

##### DATA STRUCTURE 16

```
Patterns 16
Presets 16
Project 16
DELAY 65
```

### E

##### EARLY STARTUP MENU 81

##### EUCLIDEAN SEQUENCER 46

### F

##### FACTORY RESET 81

##### FILL MODE 52

##### FILTER 59

##### FLTR MACHINES 101

##### FM SYNTHESIS

```
Algorithms 107
Carrier 106
FM ratios 107
Harmonics 109
Modulator 106
Operator envelopes 108
Operators 106
SYN1 Page 1 parameters overview 111
FX AND MIXER PARAMETERS 65
Chorus 67
Compressor 67
Delay 65
External mixer 70
```

```
FX mixer 70
Internal mixer 69
Reverb 66
```

### G

##### GRID RECORDING MODE 43

### H

##### HARD SYNC 97

### K

##### KEYBOARD SCALE 26

##### KEYBOARD SCALES 119

##### KEY COMBINATIONS 84

##### KITS 29

### L

##### LED BACKLIGHT 78

##### LED INTENSITY 78

##### LFO 63 , 64

### M

##### MACHINES 16 , 89

```
Assigning to track 89
METRONOME 23
MICRO TIMING 48
MIDI CC & NRPN 112
MIDI CONFIG 74
MIDI LEARN 101
MIDI TRACKS 17
Parameters 99
MIXER 69 , 70
MUTE MODE 27
```

### N

##### NAMING SCREEN 19

##### NOTE EDIT 43

##### NOTE EDIT MENU 43

### O

##### OS UPGRADE 80

### P

##### PAGE SETUP

```
Length per pattern mode 49
Length per track mode 49
PANEL LAYOUT 12
PARAMETER LOCKS 50
PATTERNS
Grid recording mode 43
Live recording mode 44
Parameter locks 50
Pattern control 41
Selecting a pattern 41
Trig modes 27
```

##### INDEX

```
Trig Types 42
```

PATTERNS, KITS AND PRESETS 29
Editing a preset 35
Playing a preset 34
PERFORM KIT MODE 55
PORTAMENTO 37

On/Off 59
PRESET LOCKS 50

PRESETS 29
Audio track parameters 57
Editing a preset 35
Playing a preset 34
Saving a preset 35

PRESET SELECTING 22
PROJECT MANAGER 72

PROJECTS 72
Load 72
Project Manager 72
Save 72
Write protection 72

PURGE (REMOVE UNUSED)
All 72
Kits 34

### Q

##### QUANTIZATION 48

##### QUICK SCROLLING 19

##### QUICK START 22

### R

##### RETRIGS 48 , 58

##### REVERB 66

##### RING MODULATION 97

### S

##### SAFETY AND MAINTENANCE 3

##### SCALES 119

##### SCREEN SAVER 18

##### SEQUENCER 41

```
Conditional locks 51
Editing a pattern 42
Parameter locks 50
Pattern control 41
Retrig Menu 48
Scale Menu 48
Selecting a pattern 41
Trig menu 46
Trig parameters page 48
```

SEQUENCER RECORDING MODES
Grid recording mode 43
Live recording mode 44

SETTINGS 72
MIDI config 73 , 74
Project 72
System 78 , 80

SETUP EXAMPLES 82

```
Controlling a synthesizer using the MIDI tracks 82
Digitone II with a monophonic bass machine 82
SONG MODE 53
SOUND ARCHITECTURE 15
SWING 23
SYN MACHINES 89
SYSEX DUMP 76
```

### T

##### TECHNICAL INFORMATION 87

##### TEMPO 23

##### TEMPORARY SAVE AND RELOAD 52

##### TRACK PARAMETERS 57

```
Amp 59
Filter 59
LFO 62
Syn 59
Trig 57 , 58
TRANSPOSE
Pattern transpose 53
Track transpose 53
TRIG MODE 27
TRIGS 42
Lock trigs 42
Note trigs 42
Parameter locks 50
```

### U

##### UNISON 47

### V

##### VOICE MENU 47

```
Locked voices 47
Unison 47
Voice stealing 44 , 47
```
