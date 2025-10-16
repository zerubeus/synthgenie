# Digitone 2 - Complete MIDI Parameter Mapping

This document maps every machine parameter to its corresponding MIDI CC and NRPN values. Each machine shows its actual parameter names mapped to MIDI values - no more cross-referencing!

---

## TABLE OF CONTENTS

### SYN MACHINES

1. [FM TONE](#fm-tone-machine)
2. [FM DRUM](#fm-drum-machine)
3. [WAVETONE](#wavetone-machine)
4. [SWARMER](#swarmer-machine)
5. [MIDI Machine](#midi-machine)

### FILTER MACHINES

6. [Multi-Mode Filter](#multi-mode-filter)
7. [Lowpass 4](#lowpass-4-filter)
8. [Legacy LP/HP](#legacy-lphp-filter)
9. [Comb- Filter](#comb--filter)
10. [Comb+ Filter](#comb-filter)
11. [Equalizer](#equalizer-filter)

### UNIVERSAL PARAMETERS

- [Track Parameters](#track-parameters)
- [Trig Parameters](#trig-parameters)
- [AMP Envelope](#amp-parameters-all-machines)
- [FX Parameters](#fx-parameters-all-tracks)
- [LFO 1, 2, 3](#lfo-parameters)
- [Send FX](#send-fx-parameters)
- [Mixer & Compressor](#mixer-parameters)
- [Euclidean Sequencer](#euclidean-sequencer-parameters)

---

# SYN MACHINES

## FM TONE Machine

### SYN PAGE 1

| Parameter   | Knob | Description                                                         | CC MSB | NRPN MSB:LSB |
| ----------- | ---- | ------------------------------------------------------------------- | ------ | ------------ |
| **ALGO**    | A    | Algorithm selection (operator routing structure)                    | 40     | 1:73         |
| **RATIO C** | B    | Frequency ratio for operator C                                      | 41     | 1:74         |
| **RATIO A** | C    | Frequency ratio for operator A                                      | 42     | 1:75         |
| **RATIO B** | D    | Frequency ratio for operators B1 and B2 (0.25-16.0, revolving)      | 43     | 1:76         |
| **HARM**    | E    | Harmonics (bipolar: negative=Op C, positive=Op A & B1) (-26 to +26) | 44     | 1:77         |
| **DTUN**    | F    | Detune offset for operators A and B2                                | 45     | 1:78         |
| **FDBK**    | G    | Feedback amount (self-modulation of feedback operator)              | 46     | 1:79         |
| **MIX**     | H    | Mix between carrier outputs X and Y (-64 to +63)                    | 47     | 1:80         |

### SYN PAGE 2

| Parameter   | Knob | Description                                                 | CC MSB | NRPN MSB:LSB |
| ----------- | ---- | ----------------------------------------------------------- | ------ | ------------ |
| **ATK (A)** | A    | Attack time for operator A modulation envelope              | 48     | 1:81         |
| **DEC (A)** | B    | Decay time for operator A modulation envelope               | 49     | 1:82         |
| **END (A)** | C    | End level for operator A modulation envelope                | 50     | 1:83         |
| **LEV (A)** | D    | Modulation amount from operator A                           | 51     | 1:84         |
| **ATK (B)** | E    | Attack time for operator group B (B1 & B2) envelope         | 52     | 1:85         |
| **DEC (B)** | F    | Decay time for operator group B envelope                    | 53     | 1:86         |
| **END (B)** | G    | End level for operator group B envelope                     | 54     | 1:87         |
| **LEV (B)** | H    | Modulation amount from operator group B (macro for B1 & B2) | 55     | 1:88         |

### SYN PAGE 3

| Parameter    | Knob | Description                                         | CC MSB | NRPN MSB:LSB |
| ------------ | ---- | --------------------------------------------------- | ------ | ------------ |
| **ADEL**     | A    | Envelope delay before attack for operator A         | 56     | 1:89         |
| **ATRG**     | B    | Envelope trig mode for A (trigged=ADE / gated=ASDE) | 57     | 1:90         |
| **ARST**     | C    | Envelope reset behavior for operator A              | 58     | 1:91         |
| **PHRT**     | D    | Phase reset (OFF/ALL/C/A+B/A+B2)                    | 59     | 1:92         |
| **BDEL**     | E    | Envelope delay before attack for operator group B   | 60     | 1:93         |
| **BTRG**     | F    | Envelope trig mode for B (trigged=ADE / gated=ASDE) | 61     | 1:94         |
| **BRST**     | G    | Envelope reset behavior for operator group B        | 62     | 1:95         |
| **[Unused]** | H    | —                                                   | 63     | 1:96         |

### SYN PAGE 4

| Parameter           | Knob | Description                             | CC MSB | NRPN MSB:LSB |
| ------------------- | ---- | --------------------------------------- | ------ | ------------ |
| **Ratio Offset C**  | A    | Ratio offset for operator C             | 70     | 1:97         |
| **Ratio Offset A**  | B    | Ratio offset for operator A             | 71     | 1:98         |
| **Ratio Offset B1** | C    | Ratio offset for operator B1            | 72     | 1:99         |
| **Ratio Offset B2** | D    | Ratio offset for operator B2            | 73     | 1:100        |
| **Key Track A**     | E    | Modulation key tracking for operator A  | 74     | 1:101        |
| **Key Track B1**    | F    | Modulation key tracking for operator B1 | 75     | 1:102        |
| **Key Track B2**    | G    | Modulation key tracking for operator B2 | 76     | 1:103        |
| **[Unused]**        | H    | —                                       | 77     | 1:104        |

---

## FM DRUM Machine

### SYN PAGE 1

| Parameter | Knob | Description                       | CC MSB | NRPN MSB:LSB |
| --------- | ---- | --------------------------------- | ------ | ------------ |
| **TUNE**  | A    | Oscillator pitch                  | 40     | 1:73         |
| **STIM**  | B    | Sweep time (pitch sweep duration) | 41     | 1:74         |
| **SDEP**  | C    | Sweep depth                       | 42     | 1:75         |
| **ALGO**  | D    | Algorithm selection               | 43     | 1:76         |
| **OP.C**  | E    | Operator C waveform               | 44     | 1:77         |
| **OP.AB** | F    | Operator A & B waveform           | 45     | 1:78         |
| **FDBK**  | G    | Feedback amount                   | 46     | 1:79         |
| **FOLD**  | H    | Wavefold amount (body part only)  | 47     | 1:80         |

### SYN PAGE 2

| Parameter     | Knob | Description                        | CC MSB | NRPN MSB:LSB |
| ------------- | ---- | ---------------------------------- | ------ | ------------ |
| **DEC (A)**   | A    | Decay time for operator A envelope | 48     | 1:81         |
| **END (A)**   | B    | End level for operator A envelope  | 49     | 1:82         |
| **RATIO (A)** | C    | Frequency ratio for operator A     | 50     | 1:83         |
| **MOD (A)**   | D    | Modulation amount from operator A  | 51     | 1:84         |
| **DEC (B)**   | E    | Decay time for operator B envelope | 52     | 1:85         |
| **END (B)**   | F    | End level for operator B envelope  | 53     | 1:86         |
| **RATIO (B)** | G    | Frequency ratio for operator B     | 54     | 1:87         |
| **MOD (B)**   | H    | Modulation amount from operator B  | 55     | 1:88         |

### SYN PAGE 3

| Parameter    | Knob | Description                                   | CC MSB | NRPN MSB:LSB |
| ------------ | ---- | --------------------------------------------- | ------ | ------------ |
| **HOLD**     | A    | Body hold time before decay                   | 56     | 1:89         |
| **DEC**      | B    | Body decay time (last value = infinite)       | 57     | 1:90         |
| **PH.C**     | C    | Operator C phase reset (0-90=degrees, 91=OFF) | 58     | 1:91         |
| **LEV**      | D    | Body level                                    | 59     | 1:92         |
| **NRST**     | E    | Noise reset (fixed seed when ON)              | 60     | 1:93         |
| **NRM**      | F    | Noise ring mod (Op C as ring modulator)       | 61     | 1:94         |
| **[Unused]** | G    | —                                             | 62     | 1:95         |
| **[Unused]** | H    | —                                             | 63     | 1:96         |

### SYN PAGE 4

| Parameter | Knob | Description                                  | CC MSB | NRPN MSB:LSB |
| --------- | ---- | -------------------------------------------- | ------ | ------------ |
| **NHLD**  | A    | Noise hold time                              | 70     | 1:97         |
| **NDEC**  | B    | Noise decay time (last value = infinite)     | 71     | 1:98         |
| **TRAN**  | C    | Drum transient selection                     | 72     | 1:99         |
| **TLEV**  | D    | Transient level                              | 73     | 1:100        |
| **BASE**  | E    | Noise/transient filter base frequency        | 74     | 1:101        |
| **WDTH**  | F    | Noise/transient filter width                 | 75     | 1:102        |
| **GRAN**  | G    | Noise grain density (high=white, low=grainy) | 76     | 1:103        |
| **NLEV**  | H    | Noise level                                  | 77     | 1:104        |

---

## WAVETONE Machine

### SYN PAGE 1

| Parameter | Knob | Description                                      | CC MSB | NRPN MSB:LSB |
| --------- | ---- | ------------------------------------------------ | ------ | ------------ |
| **TUN1**  | A    | Oscillator 1 tune                                | 40     | 1:73         |
| **WAV1**  | B    | Oscillator 1 waveform (crossfades between waves) | 41     | 1:74         |
| **PD1**   | C    | Oscillator 1 phase distortion                    | 42     | 1:75         |
| **LEV1**  | D    | Oscillator 1 level                               | 43     | 1:76         |
| **TUN2**  | E    | Oscillator 2 tune                                | 44     | 1:77         |
| **WAV2**  | F    | Oscillator 2 waveform (crossfades between waves) | 45     | 1:78         |
| **PD2**   | G    | Oscillator 2 phase distortion                    | 46     | 1:79         |
| **LEV2**  | H    | Oscillator 2 level                               | 47     | 1:80         |

### SYN PAGE 2

| Parameter    | Knob | Description                                                   | CC MSB | NRPN MSB:LSB |
| ------------ | ---- | ------------------------------------------------------------- | ------ | ------------ |
| **OFS1**     | A    | Oscillator 1 linear offset (Hz, not cents)                    | 48     | 1:81         |
| **TBL1**     | B    | Oscillator 1 wavetable (PRIM/HARM)                            | 49     | 1:82         |
| **MOD**      | C    | Oscillator modulation (OFF/RING MOD/RING MOD FIXED/HARD SYNC) | 50     | 1:83         |
| **RSET**     | D    | Phase reset (OFF/ON/RAND)                                     | 51     | 1:84         |
| **OFS2**     | E    | Oscillator 2 linear offset (Hz, not cents)                    | 52     | 1:85         |
| **TBL2**     | F    | Oscillator 2 wavetable (PRIM/HARM)                            | 53     | 1:86         |
| **DRIF**     | G    | Oscillator drift (random pitch drift for osc 1 & 2)           | 54     | 1:87         |
| **[Unused]** | H    | —                                                             | 55     | 1:88         |

### SYN PAGE 3

| Parameter | Knob | Description                                        | CC MSB | NRPN MSB:LSB |
| --------- | ---- | -------------------------------------------------- | ------ | ------------ |
| **ATK**   | A    | Noise attack time                                  | 56     | 1:89         |
| **HOLD**  | B    | Noise hold time (0-126=fixed, NOTE=gate-dependent) | 57     | 1:90         |
| **DEC**   | C    | Noise decay time                                   | 58     | 1:91         |
| **NLEV**  | D    | Noise level                                        | 59     | 1:92         |
| **BASE**  | E    | Noise filter base frequency                        | 60     | 1:93         |
| **WDTH**  | F    | Noise filter width                                 | 61     | 1:94         |
| **TYPE**  | G    | Noise type (GRAIN/TUNED/S&H)                       | 62     | 1:95         |
| **CHAR**  | H    | Noise character (varies by TYPE)                   | 63     | 1:96         |

### SYN PAGE 4

| Parameter    | Knob | Description | CC MSB | NRPN MSB:LSB |
| ------------ | ---- | ----------- | ------ | ------------ |
| **[Unused]** | A    | —           | 70     | 1:97         |
| **[Unused]** | B    | —           | 71     | 1:98         |
| **[Unused]** | C    | —           | 72     | 1:99         |
| **[Unused]** | D    | —           | 73     | 1:100        |
| **[Unused]** | E    | —           | 74     | 1:101        |
| **[Unused]** | F    | —           | 75     | 1:102        |
| **[Unused]** | G    | —           | 76     | 1:103        |
| **[Unused]** | H    | —           | 77     | 1:104        |

---

## SWARMER Machine

### SYN PAGE 1

| Parameter | Knob | Description                                         | CC MSB | NRPN MSB:LSB |
| --------- | ---- | --------------------------------------------------- | ------ | ------------ |
| **TUNE**  | A    | Pitch offset (bipolar, 0=unchanged)                 | 40     | 1:73         |
| **SWRM**  | B    | Swarm waveform (for 6 detuned oscillators)          | 41     | 1:74         |
| **DET**   | C    | Detune amount for swarm oscillators                 | 42     | 1:75         |
| **MIX**   | D    | Swarm level vs main oscillator                      | 43     | 1:76         |
| **M.OCT** | E    | Main oscillator octave down (-1 or -2)              | 44     | 1:77         |
| **MAIN**  | F    | Main oscillator waveform                            | 45     | 1:78         |
| **ANIM**  | G    | Swarm animation (modulation amount via hidden LFOs) | 46     | 1:79         |
| **N.MOD** | H    | Noise modulation amount for swarm oscillators       | 47     | 1:80         |

### SYN PAGES 2-4

_SWARMER only uses SYN PAGE 1. Pages 2-4 are unused for this machine._

---

## MIDI Machine

The MIDI machine uses different page layouts compared to audio machines.

### TRIG PAGE

| Parameter | Description         | CC MSB | NRPN MSB:LSB |
| --------- | ------------------- | ------ | ------------ |
| **NOTE**  | Trig note pitch     | 3      | 3:0          |
| **VEL**   | Trig velocity       | 4      | 3:1          |
| **LEN**   | Trig length         | 5      | 3:2          |
| **PROB**  | Trig probability    | —      | —            |
| **LFO.T** | LFO trig            | —      | —            |
| **FILL**  | Fill trig condition | —      | —            |
| **COND**  | Trig condition      | —      | —            |

### SYN PAGE (MIDI Machine)

| Parameter | Description            | Range     |
| --------- | ---------------------- | --------- |
| **CHAN**  | MIDI channel           | OFF, 1-16 |
| **BANK**  | Bank change (CC 0 MSB) | —         |
| **SBNK**  | Sub bank (CC 32 LSB)   | —         |
| **PROG**  | Program change         | —         |
| **PB**    | Pitch bend             | —         |
| **AT**    | Aftertouch             | —         |
| **MW**    | Mod wheel              | —         |
| **BC**    | Breath controller      | —         |

### FLTR PAGE 1 & AMP PAGE 1 (MIDI Machine - CC Values)

| Parameter | Description | CC MSB | NRPN MSB:LSB |
| --------- | ----------- | ------ | ------------ |
| **VAL1**  | CC 1 value  | 70     | 1:16         |
| **VAL2**  | CC 2 value  | 71     | 1:17         |
| **VAL3**  | CC 3 value  | 72     | 1:18         |
| **VAL4**  | CC 4 value  | 73     | 1:19         |
| **VAL5**  | CC 5 value  | 74     | 1:20         |
| **VAL6**  | CC 6 value  | 75     | 1:21         |
| **VAL7**  | CC 7 value  | 76     | 1:22         |
| **VAL8**  | CC 8 value  | 77     | 1:23         |
| **VAL9**  | CC 9 value  | 78     | 1:60         |
| **VAL10** | CC 10 value | 79     | 1:61         |
| **VAL11** | CC 11 value | 80     | 1:62         |
| **VAL12** | CC 12 value | 81     | 1:63         |
| **VAL13** | CC 13 value | 82     | 1:64         |
| **VAL14** | CC 14 value | 83     | 1:65         |
| **VAL15** | CC 15 value | 84     | 1:66         |
| **VAL16** | CC 16 value | 85     | 1:67         |

_Note: FLTR PAGE 2 and AMP PAGE 2 contain SEL1-SEL16 parameters to select which MIDI CC commands the VAL parameters control. These can be learned via MIDI learn function._

---

## Universal Parameters (All Audio Machines)

### TRIG PARAMETERS

| Parameter             | Description             | CC MSB | NRPN MSB:LSB |
| --------------------- | ----------------------- | ------ | ------------ |
| **Note**              | Trig note               | 3      | 3:0          |
| **Velocity**          | Trig velocity           | 4      | 3:1          |
| **Length**            | Trig length             | 5      | 3:2          |
| **Filter Trig**       | Filter envelope trigger | 13     | —            |
| **LFO Trig**          | LFO trigger             | 14     | —            |
| **Portamento Time**   | Portamento time         | 9      | 3:6          |
| **Portamento On/Off** | Portamento toggle       | 65     | 3:7          |

### TRACK PARAMETERS

| Parameter       | Description  | CC MSB | NRPN MSB:LSB |
| --------------- | ------------ | ------ | ------------ |
| **Mute**        | Track mute   | 94     | 1:108        |
| **Track Level** | Track volume | 95     | 1:110        |

---

## FILTER MACHINES (All Types)

### Multi-Mode, Lowpass 4, Legacy LP/HP, Comb-, Comb+, Equalizer

| Parameter         | Description                                 | CC MSB | NRPN MSB:LSB |
| ----------------- | ------------------------------------------- | ------ | ------------ |
| **Frequency**     | Filter cutoff/center frequency              | 16     | 1:20         |
| **Data Entry F**  | Machine-dependent (Resonance/Gain/Feedback) | 17     | 1:21         |
| **Data Entry G**  | Machine-dependent (Type/Q/LPF)              | 18     | 1:22         |
| **Env. Depth**    | Envelope modulation depth (bipolar)         | 24     | 1:26         |
| **Attack Time**   | Filter envelope attack                      | 20     | 1:16         |
| **Decay Time**    | Filter envelope decay                       | 21     | 1:17         |
| **Sustain Level** | Filter envelope sustain                     | 22     | 1:18         |
| **Release Time**  | Filter envelope release                     | 23     | 1:19         |
| **Env. Delay**    | Envelope delay time                         | 19     | 1:23         |
| **Key Tracking**  | Filter key tracking                         | 26     | 1:69         |
| **Base**          | Base-width filter base frequency            | 27     | 1:24         |
| **Width**         | Base-width filter width                     | 28     | 1:25         |
| **Env. Reset**    | Envelope reset toggle                       | 25     | 1:68         |

_Note: Filter machine types share the same MIDI mapping structure, but parameter functions vary (e.g., Data Entry G is "Type" on Multi-Mode, "Q" on Equalizer, "LPF" on Comb filters)._

---

## AMP PARAMETERS (All Machines)

| Parameter         | Description           | CC MSB | NRPN MSB:LSB |
| ----------------- | --------------------- | ------ | ------------ |
| **Attack Time**   | Amp envelope attack   | 84     | 1:30         |
| **Hold Time**     | Amp envelope hold     | 85     | 1:31         |
| **Decay Time**    | Amp envelope decay    | 86     | 1:32         |
| **Sustain Level** | Amp envelope sustain  | 87     | 1:33         |
| **Release Time**  | Amp envelope release  | 88     | 1:34         |
| **Env. Reset**    | Envelope reset toggle | 92     | 1:41         |
| **Mode**          | Amp mode              | 91     | 1:40         |
| **Pan**           | Stereo panning        | 89     | 1:38         |
| **Volume**        | Track volume          | 90     | 1:39         |

---

## FX PARAMETERS (All Tracks)

| Parameter                 | Description                   | CC MSB | NRPN MSB:LSB |
| ------------------------- | ----------------------------- | ------ | ------------ |
| **Bit Reduction**         | Bit depth reduction           | 78     | 1:5          |
| **Overdrive**             | Overdrive amount              | 81     | 1:8          |
| **Sample Rate Reduction** | Sample rate reduction         | 79     | 1:6          |
| **SRR Routing**           | Sample rate reduction routing | 80     | 1:7          |
| **Overdrive Routing**     | Overdrive routing             | 82     | 1:9          |
| **Delay Send**            | Send to delay FX              | 30     | 1:36         |
| **Reverb Send**           | Send to reverb FX             | 31     | 1:37         |
| **Chorus Send**           | Send to chorus FX             | 29     | 1:35         |

---

## LFO PARAMETERS

### LFO 1

| Parameter            | Description              | CC MSB | NRPN MSB:LSB |
| -------------------- | ------------------------ | ------ | ------------ |
| **Speed**            | LFO speed                | 102    | 1:42         |
| **Multiplier**       | Speed multiplier         | 103    | 1:43         |
| **Fade In/Out**      | Fade time                | 104    | 1:44         |
| **Destination**      | Modulation destination   | 105    | 1:45         |
| **Waveform**         | LFO waveform             | 106    | 1:46         |
| **Start Phase/Slew** | Start phase or slew rate | 107    | 1:47         |
| **Trig Mode**        | Trigger mode             | 108    | 1:48         |
| **Depth**            | Modulation depth         | 109    | 1:49         |

### LFO 2

| Parameter            | Description              | CC MSB | NRPN MSB:LSB |
| -------------------- | ------------------------ | ------ | ------------ |
| **Speed**            | LFO speed                | 111    | 1:50         |
| **Multiplier**       | Speed multiplier         | 112    | 1:51         |
| **Fade In/Out**      | Fade time                | 113    | 1:52         |
| **Destination**      | Modulation destination   | 114    | 1:53         |
| **Waveform**         | LFO waveform             | 115    | 1:54         |
| **Start Phase/Slew** | Start phase or slew rate | 116    | 1:55         |
| **Trig Mode**        | Trigger mode             | 117    | 1:56         |
| **Depth**            | Modulation depth         | 118    | 1:57         |

### LFO 3

| Parameter            | Description              | CC MSB | NRPN MSB:LSB |
| -------------------- | ------------------------ | ------ | ------------ |
| **Speed**            | LFO speed                | —      | 1:58         |
| **Multiplier**       | Speed multiplier         | —      | 1:59         |
| **Fade In/Out**      | Fade time                | —      | 1:60         |
| **Destination**      | Modulation destination   | —      | 1:61         |
| **Waveform**         | LFO waveform             | —      | 1:62         |
| **Start Phase/Slew** | Start phase or slew rate | —      | 1:70         |
| **Trig Mode**        | Trigger mode             | —      | 1:71         |
| **Depth**            | Modulation depth         | —      | 1:72         |

_Note: LFO 3 only has NRPN control, no CC MSB._

---

## EUCLIDEAN SEQUENCER PARAMETERS

| Parameter                 | Description              | NRPN MSB:LSB |
| ------------------------- | ------------------------ | ------------ |
| **Pulse Generator 1**     | Euclidean pulses track 1 | 3:8          |
| **Pulse Generator 2**     | Euclidean pulses track 2 | 3:9          |
| **Euclidean Mode On/Off** | Enable euclidean mode    | 3:14         |
| **Rotation Generator 1**  | Rotation offset track 1  | 3:11         |
| **Rotation Generator 2**  | Rotation offset track 2  | 3:12         |
| **Track Rotation**        | Track rotation offset    | 3:13         |
| **Boolean Operator**      | Boolean logic operator   | 3:10         |

---

## SEND FX PARAMETERS

### DELAY

| Parameter           | Description      | CC MSB | NRPN MSB:LSB |
| ------------------- | ---------------- | ------ | ------------ |
| **Delay Time**      | Delay time       | 21     | 2:0          |
| **Pingpong**        | Pingpong mode    | 22     | 2:1          |
| **Stereo Width**    | Stereo width     | 23     | 2:2          |
| **Feedback**        | Delay feedback   | 24     | 2:3          |
| **Highpass Filter** | HP filter cutoff | 25     | 2:4          |
| **Lowpass Filter**  | LP filter cutoff | 26     | 2:5          |
| **Reverb Send**     | Send to reverb   | 27     | 2:6          |
| **Mix Volume**      | Delay mix level  | 28     | 2:7          |

### REVERB

| Parameter           | Description               | CC MSB | NRPN MSB:LSB |
| ------------------- | ------------------------- | ------ | ------------ |
| **Predelay**        | Predelay time             | 29     | 2:8          |
| **Decay Time**      | Reverb decay              | 30     | 2:9          |
| **Shelving Freq**   | Shelving filter frequency | 31     | 2:10         |
| **Shelving Gain**   | Shelving filter gain      | 89     | 2:11         |
| **Highpass Filter** | HP filter cutoff          | 90     | 2:12         |
| **Lowpass Filter**  | LP filter cutoff          | 91     | 2:13         |
| **Mix Volume**      | Reverb mix level          | 92     | 2:15         |

### CHORUS

| Parameter            | Description      | CC MSB | NRPN MSB:LSB |
| -------------------- | ---------------- | ------ | ------------ |
| **Depth**            | Chorus depth     | 16     | 2:41         |
| **Speed**            | Chorus speed     | 9      | 2:42         |
| **High Pass Filter** | HP filter cutoff | 70     | 2:43         |
| **Width**            | Stereo width     | 71     | 2:44         |
| **Delay Send**       | Send to delay    | 12     | 2:45         |
| **Reverb Send**      | Send to reverb   | 13     | 2:46         |
| **Mix Volume**       | Chorus mix level | 14     | 2:47         |

---

## MIXER PARAMETERS

### COMPRESSOR

| Parameter            | Description              | CC MSB | NRPN MSB:LSB |
| -------------------- | ------------------------ | ------ | ------------ |
| **Threshold**        | Compression threshold    | 111    | 2:16         |
| **Attack Time**      | Compressor attack        | 112    | 2:17         |
| **Release Time**     | Compressor release       | 113    | 2:18         |
| **Makeup Gain**      | Output gain compensation | 114    | 2:19         |
| **Pattern Volume**   | Overall pattern volume   | 119    | 2:24         |
| **Ratio**            | Compression ratio        | 115    | 2:20         |
| **Sidechain Source** | Sidechain input          | 116    | 2:21         |
| **Sidechain Filter** | Sidechain filter         | 117    | 2:22         |
| **Dry/Wet Mix**      | Parallel compression     | 118    | 2:23         |

### EXTERNAL INPUT MIXER

| Parameter               | Description       | CC MSB | NRPN MSB:LSB |
| ----------------------- | ----------------- | ------ | ------------ |
| **Dual Mono**           | Dual mono mode    | 82     | 2:40         |
| **Input L Level**       | Left input level  | 72     | 2:30         |
| **Input L Pan**         | Left input pan    | 74     | 2:32         |
| **Input R Level**       | Right input level | 73     | 2:31         |
| **Input R Pan**         | Right input pan   | 75     | 2:33         |
| **Input L Delay Send**  | Left delay send   | 78     | 2:36         |
| **Input R Delay Send**  | Right delay send  | 79     | 2:37         |
| **Input L Reverb Send** | Left reverb send  | 80     | 2:38         |
| **Input R Reverb Send** | Right reverb send | 81     | 2:39         |
| **Input L Chorus Send** | Left chorus send  | 76     | 2:34         |
| **Input R Chorus Send** | Right chorus send | 77     | 2:35         |

_Note: When in stereo mode (Dual Mono OFF), "L R" parameters control both channels as a stereo pair._

---

## MISC PARAMETERS

| Parameter            | Description             | CC MSB | NRPN MSB:LSB |
| -------------------- | ----------------------- | ------ | ------------ |
| **Pattern Mute**     | Mute entire pattern     | 110    | 1:109        |
| **Master Overdrive** | Master output overdrive | 17     | 2:50         |

---

## MIDI Implementation Notes

### NRPN Format

- **MSB (Most Significant Byte)**: High byte of NRPN address
- **LSB (Least Significant Byte)**: Low byte of NRPN address
- Format in tables shown as `MSB:LSB` (e.g., `1:73`)

### CC vs NRPN

- Most parameters have both CC and NRPN control
- LFO 3 parameters only have NRPN control (no CC)
- Some parameters only have NRPN control (marked with "—" in CC column)

### Parameter Ranges

- Most parameters: 0-127
- Bipolar parameters: -64 to +63 (MIDI value 0-127, center at 64)
- Special ranges noted in parameter descriptions

### MIDI Learn

For MIDI machine SEL parameters (CC select):

1. Press and hold [FUNC] + DATA ENTRY knob
2. "MIDI LEARN" popup appears
3. Send desired CC from external device
4. Parameter automatically configured

### Track Configuration

- Each track can send on MIDI channels 1-16
- Set channel in SYN page CHAN parameter
- AUTO CHANNEL available in SETTINGS > MIDI CONFIG

---

## Quick Workflow Tips

1. **Finding Parameters**: Use Ctrl+F to search for parameter names
2. **CC vs NRPN**: Use CC for basic control, NRPN for full 14-bit resolution
3. **Machine Switching**: SYN page knobs change function based on active machine
4. **MIDI Tracks**: Configure on SYN/FLTR/AMP pages, not standard audio machine pages
5. **Modulation**: LFO destinations vary by machine—check Appendix D in manual

---

_Document based on Digitone 2 User Manual OS 1.00A (October 2024)_
