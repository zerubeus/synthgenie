# Digitone MIDI Reference

Complete MIDI implementation extracted from Digitone User Manual OS 1.41

---

## Table of Contents

- [1. MIDI Track Parameters](#1-midi-track-parameters)
  - [1.1 Editing MIDI Track Parameters](#11-editing-midi-track-parameters)
  - [1.2 Trig Parameters Page](#12-trig-parameters-page)
  - [1.3 SYN1 Page (MIDI Source)](#13-syn1-page-midi-source)
  - [1.4 SYN2 Page (MIDI Source)](#14-syn2-page-midi-source)
  - [1.5 FLTR Page (CC Value)](#15-fltr-page-cc-value)
  - [1.6 AMP Page (CC Select)](#16-amp-page-cc-select)
  - [1.7 LFO Page](#17-lfo-page)
- [2. MIDI Configuration](#2-midi-configuration)
  - [2.1 Sync](#21-sync)
  - [2.2 Port Config](#22-port-config)
  - [2.3 Channels](#23-channels)
- [3. MIDI Implementation](#3-midi-implementation)
  - [3.1 Track Parameters](#31-track-parameters)
  - [3.2 Trig Parameters](#32-trig-parameters)
  - [3.3 FM Parameters](#33-fm-parameters)
  - [3.4 Filter Parameters](#34-filter-parameters)
  - [3.5 Amp Parameters](#35-amp-parameters)
  - [3.6 LFO Parameters](#36-lfo-parameters)
  - [3.7 MIDI Track Parameters](#37-midi-track-parameters)
  - [3.8 FX Parameters](#38-fx-parameters)
  - [3.9 Misc Parameters](#39-misc-parameters)
- [4. LFO Modulation Destinations](#4-lfo-modulation-destinations)

---

## 1. MIDI Track Parameters

The Digitone has four MIDI tracks used to control external MIDI-equipped gear. Each MIDI track can send note data, velocity, note length, control pitch bend and aftertouch, as well as eight freely assignable MIDI control change parameters (MIDI CCs).

A MIDI track can have any MIDI channel assigned to it, and several tracks can share the same channel. If several tracks are assigned to the same MIDI channel, the track with the lowest number has priority when receiving MIDI.

The MIDI tracks function almost the same way as the synth tracks. Parameter locks, LFO modulation, copy and paste commands are available. Each MIDI track also features micro timing, individual track length, and time signature settings. The main difference is that the MIDI tracks do not generate any sound and the sequencer data instead transmits through the MIDI OUT or USB ports.

Press the **[MIDI]** key and then press one of the **[T1–4]** keys to select which MIDI track to edit.

### 1.1 Editing MIDI Track Parameters

There are five PARAMETER pages for the MIDI tracks:

- **TRIG PARAMETERS** - Note trig settings
- **SYN1** - MIDI Source parameters (Channel, Bank, Program Change, Pitch Bend, etc.)
- **SYN2** - Additional MIDI Source parameters
- **FLTR** - CC Value settings (CC1-8 values)
- **AMP** - CC Select settings (which CC numbers to use)
- **LFO** - LFO modulation settings

Press the **[PARAMETER]** keys to access the MIDI tracks PARAMETER pages. Use the DATA ENTRY knobs A-H to change the parameters. Press and hold a **[PARAMETER]** key to see the values for all parameters on that page.

### 1.2 Trig Parameters Page

Here you find the parameters for the note trigs. These general settings affect note trigs placed in the sequencer.

Press **[TRIG PARAMETERS]** to access this parameter page.

#### 1.2.1 ROOT

- **Range:** C0–G10
- Root sets the default note value that the note trigs placed in GRID RECORDING mode have. If you change the root note and have additional notes added on the same trig, then the additional notes are offset and transposed accordingly.

#### 1.2.2 VEL

- **Range:** 1–127
- Trig Velocity controls the velocity of the notes the MIDI track sends out. A setting of 0 equals a NOTE OFF command.

#### 1.2.3 LEN

- **Range:** 0.125–128, INF
- Trig Length sets the duration of the notes. When a note has finished playing, a NOTE OFF command is sent. The INF setting equals infinite note length.

#### 1.2.4 PROB

- **Range:** 0%–100%
- TRIG PROBABILITY sets the probability that the trigs on the track play or not. The probability outcome is re-evaluated every time a trig is set to play. The default setting is 100%, meaning that all the trigs on the track play every time.

**Note:** This parameter changes temporarily to display and control COND (Trig Condition) when you add a conditional lock. If you have placed a conditional lock on a trig in the sequencer, the trig condition overrides the Trig Probability setting.

#### 1.2.6 LFO.T

- **Range:** ON, OFF
- LFO Trig controls if the LFO is triggered or not.

### 1.3 SYN1 Page (MIDI Source)

Here you can set the MIDI channel that the MIDI track should use to send data. Bank and program change values are also set here, together with a few standard CC parameters.

**Important:** The default value of the parameters on this page is OFF, meaning they are disabled and do not send out any data. Press and hold **[FUNC]** and then press the DATA ENTRY knobs to enable them. You can then use the DATA ENTRY knobs to set the parameter values as usual. Disable the parameters again by repeating the activation procedure.

Press **[SYN1]** once to access this parameter page.

#### 1.3.1 CHAN

- **Range:** OFF, 1–16
- Channel sets the MIDI channel the track sends MIDI data to. If you set this parameter to OFF, it turns the MIDI track off.
- **Note:** This parameter cannot be parameter locked.

#### 1.3.2 BANK

- **Range:** OFF, 1–128
- Bank sends a bank change message on CC 0 MSB.

#### 1.3.3 SBNK

- **Range:** OFF, 1–128
- Sub Bank sends a bank change message on CC 32 LSB.

#### 1.3.4 PROG

- **Range:** OFF, 1–128
- Program Change sends a Program Change message.

#### 1.3.5 PB

- **Range:** OFF, -128.00–128.00
- Pitch Bend controls the pitch bend data sent on the MIDI track.

#### 1.3.6 AT

- **Range:** OFF, 0–127
- Aftertouch controls the aftertouch data sent on the MIDI track.

#### 1.3.7 MW

- **Range:** OFF, 0–127
- Mod Wheel controls the modulation wheel data sent on the MIDI track.

#### 1.3.8 BC

- **Range:** OFF, 0–127
- Breath controller controls the breath control data sent on the MIDI track.

### 1.4 SYN2 Page (MIDI Source)

SYN2 page contains the same parameters as the SYN1 page. Press **[SYN2]** to access this parameter page.

### 1.5 FLTR Page (CC Value)

Here you can set the values of up to eight assignable CC commands.

**Important:** The default value of the parameters on this page is OFF, meaning they are disabled and do not send out any data. Press and hold **[FUNC]** and then press the DATA ENTRY knobs to enable them. You can then use the DATA ENTRY knobs to set the parameter values as usual. Disable the parameters again by repeating the enabling procedure.

Press **[FLTR]** to access this parameter page.

#### 1.5.1 VAL1-VAL8

- **Range:** OFF, 0–127
- CC 1–8 Value controls the values that the CC commands send. You specify the CC commands themselves on the AMP (CC SELECT) page. These parameters default value is OFF. Press **[FUNC]** + DATA ENTRY knobs to activate the parameters and then turn the DATA ENTRY knobs to set a value.

### 1.6 AMP Page (CC Select)

Here you select the eight CC commands whose values you set with the parameters on the FLTR PAGE (CC VALUE) page.

Press **[AMP]** to access this parameter page.

#### 1.6.1 SEL1-SEL8

- **Range:** 1–119
- CC 1–8 Select specifies the CC commands whose values are controlled by the parameters on the FLTR (CC VALUE) page. The selectable commands are the standard MIDI Control Change Messages.

### 1.7 LFO Page

The Low-Frequency Oscillator can be used to interact with the parameters found on the MIDI tracks' SYN1 and FLTR pages. Customize the low-frequency oscillator behavior, orientation, and depth on this page.

Press **[LFO]** to access this parameter page.

#### 1.7.1 SPD

- **Range:** -64.00–63.00
- Speed sets the speed of the LFO1. Try settings of 8, 16, or 32 to sync the LFO to straight beats. The knob is bipolar. The LFO cycle can be played backward by using negative values.

#### 1.7.2 MULT

- Multiplier multiplies the LFO1 SPD parameter by the set factor either by multiplying the current tempo (BPM settings) or by multiplying a fixed tempo of 120 BPM.

#### 1.7.3 FADE

- **Range:** -64–63
- Fade In/Out makes it possible to fade in/fade out the LFO1 modulation. The knob is bipolar. Positive values give a fade-out, negative values give a fade in. 0 gives no fade in/fade out.

#### 1.7.4 DEST

- Destination selects the modulation destination for the LFO1. Preview how the LFO modulation affects the sound by highlighting a destination. Press **[YES]** to confirm the selection.

#### 1.7.5 WAVE

- Waveform sets the LFO1 waveform. There are seven waveforms:
  - Triangle
  - Sine
  - Square
  - Sawtooth
  - Exponential
  - Ramp
  - Random

#### 1.7.6 SPH

- **Range:** 0–127
- Start Phase sets the point within the wave cycle where the LFO1 starts when it is triggered. 0 makes the LFO start at the beginning of a complete wave cycle, 64 makes it start at the center.

#### 1.7.7 MODE

- Trig Mode sets how the LFO1 acts when triggered by a note:
  - **FRE** - (default) Free-running mode. Makes the LFO run continuously, never restarting or stopping even if triggered by a note.
  - **TRG** - Makes the LFO restart when a note is triggered.
  - **HLD** - Makes the LFO run free in the background, but when a note is triggered, the LFO output level is latched and held still until the next note is triggered.
  - **ONE** - The LFO starts when a note is triggered, then runs to the end of the waveform and then stops. This makes the LFO function similar to an envelope.
  - **HLF** - The LFO starts when a note is triggered, then runs to the middle of the waveform and then stops.

#### 1.7.8 DEP

- **Range:** -64.00–63.00
- Depth sets the depth and polarity of the LFO1 modulation. Both negative (inverted) and positive modulation depth is possible. A center setting, 0.00, equals no modulation depth.

---

## 2. MIDI Configuration

In the SETTINGS menu you find various sub-menus dealing with MIDI functionality.

### 2.1 Sync

Controls how Digitone receives and sends MIDI clock and transport commands.

#### CLOCK RECEIVE

- Sets whether or not Digitone responds to MIDI clock sent from external devices.

#### CLOCK SEND

- Sets whether or not Digitone transmits MIDI clock.

#### TRANSPORT RECEIVE

- Sets whether or not Digitone responds to MIDI transport messages sent from external devices.

#### TRANSPORT SEND

- Sets whether or not Digitone transmits MIDI transport messages.

#### PROG CH RECEIVE

- Sets whether or not Digitone responds to incoming program change messages, which is useful when wanting to select patterns externally. The MIDI channel that listens to incoming program change messages is set in the MIDI CHANNELS menu.

#### PROG CH SEND

- Sets whether or not Digitone sends program change messages when patterns change. You set the MIDI channel that sends program change messages in the MIDI CHANNELS menu.

### 2.2 Port Config

MIDI port related settings.

#### TURBO SPEED

- Press **[YES]** to start the turbo speed negotiation. The device chooses the optimal speed automatically.
- **Note:** You must use a MIDI interface that supports the Turbo-MIDI protocol.

#### OUT PORT FUNC

- Selects what type of signal the MIDI OUT port sends:
  - **MIDI** - Port sends out MIDI data
  - **DIN 24** - Port sends DIN 24 sync pulses (no MIDI data transferred)
  - **DIN 48** - Port sends DIN 48 sync pulses (no MIDI data transferred)

#### THRU PORT FUNC

- Selects what type of signal the MIDI THRU port sends (same options as OUT PORT FUNC)

#### INPUT FROM

- Selects the input MIDI data port:
  - **DISABLED** - Receives no MIDI data
  - **MIDI** - Receives MIDI data from the MIDI IN port
  - **USB** - Receives MIDI data from the USB port
  - **MIDI+USB** - Receives MIDI data from both MIDI IN and USB ports

#### OUTPUT TO

- Selects the output MIDI data port:
  - **DISABLED** - Sends no MIDI data
  - **MIDI** - Sends MIDI data to the MIDI OUT port
  - **USB** - Sends MIDI data to the USB port
  - **MIDI+USB** - Sends MIDI data to both MIDI OUT and USB ports

**Important:** If MIDI+USB is selected in OUTPUT TO settings, MIDI data will limit the USB speed. When sending large chunks of data, make sure you only use the USB setting.

#### OUTPUT CH

- Selects whether the knobs send data on the AUTO channel or the track channel.

#### PARAM OUTPUT

- Selects what type of MIDI messages the DATA ENTRY knobs send:
  - **NRPN** - Sends NRPN MIDI messages
  - **CC** - Sends CC MIDI messages

#### ENCODER DEST

- Controls whether the DATA ENTRY and LEVEL/DATA knobs send MIDI data:
  - **INT** - Knobs only affect the Digitone and send no MIDI data
  - **INT + EXT** - Knobs affect the Digitone and also send MIDI data to external devices

#### TRIG KEY DEST

- Controls whether the [TRIG] keys send MIDI data:
  - **INT** - [TRIG] keys only affect the Digitone and send no MIDI data
  - **INT + EXT** - [TRIG] keys affect the Digitone and also send MIDI data to external devices
  - **EXT** - [TRIG] keys send MIDI data to external devices but do not affect the Digitone

#### MUTE DEST

- Controls whether activating/deactivating mutes send MIDI data:
  - **INT** - Mutes only affect the Digitone and no MIDI data is sent
  - **INT + EXT** - Mutes affect the Digitone and also send MIDI data to external devices
  - **EXT** - Mutes send MIDI data externally but do not affect the Digitone

#### RECEIVE NOTES

- Sets whether or not it is possible to use an external MIDI keyboard or controller to play the Digitone.

#### RECEIVE CC/NRPN

- Sets whether or not it is possible to use an external MIDI device to control Digitone parameters with CC/NRPN data.

### 2.3 Channels

MIDI channel configuration.

#### TRACK 1–4 CHANNEL

- Selects dedicated MIDI channel that controls the synth tracks. It also sets the MIDI channel for the MIDI messages the DATA ENTRY knobs on the chosen track send.
- **OFF** setting makes the track disregard any incoming MIDI messages.

#### MIDI 1–4 CHANNEL

- Selects dedicated MIDI channel that controls the MIDI tracks. It also sets the MIDI channel for the MIDI messages the DATA ENTRY knobs on the chosen track send.
- **OFF** setting makes the track disregard any incoming MIDI messages.

#### FX CHANNEL

- Selects dedicated MIDI channel that controls the FX parameters. It also sets the MIDI channel for the MIDI messages the DATA ENTRY knobs on the FX pages send.
- **OFF** setting makes the track disregard any incoming MIDI messages.

#### AUTO CHANNEL

- Selects the MIDI channel that gives access to the currently active track. If an external MIDI keyboard connected to Digitone sends MIDI data on this channel, the keyboard controls the currently selected track.

---

## 3. MIDI Implementation

Complete CC and NRPN specifications for the Digitone.

### 3.1 Track Parameters

| Parameter   | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| ----------- | ------ | ------ | -------- | -------- |
| Mute        | 94     | -      | 1        | 101      |
| Track level | 95     | -      | 1        | 100      |

### 3.2 Trig Parameters

| Parameter       | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| --------------- | ------ | ------ | -------- | -------- |
| Root            | 3      | -      | 3        | 0        |
| Velocity        | 4      | -      | 3        | 1        |
| Length          | 5      | -      | 3        | 2        |
| Filter Trig     | 13     | -      | 3        | 5        |
| LFO Trig        | 14     | -      | 3        | 6        |
| Portamento Time | 15     | -      | 3        | 7        |
| Portamento On   | 16     | -      | 3        | 8        |

### 3.3 FM Parameters

#### SYN1 Page

| Parameter       | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| --------------- | ------ | ------ | -------- | -------- |
| Algorithm       | 90     | -      | 1        | 72       |
| Ratio C         | 91     | -      | 1        | 73       |
| Ratio A         | 92     | -      | 1        | 74       |
| Ratio B         | 16     | 48     | 1        | 75       |
| Harmonics       | 17     | 49     | 1        | 76       |
| Detune          | 18     | 50     | 1        | 77       |
| Feedback        | 19     | 51     | 1        | 78       |
| Mix             | 20     | 52     | 1        | 79       |
| Ratio C Offset  | -      | -      | 1        | 95       |
| Ratio A Offset  | -      | -      | 1        | 96       |
| Ratio B1 Offset | -      | -      | 1        | 97       |
| Ratio B2 Offset | -      | -      | 1        | 98       |

#### SYN2 Page

| Parameter    | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| ------------ | ------ | ------ | -------- | -------- |
| A Env Attack | 75     | -      | 1        | 80       |
| A Env Decay  | 76     | -      | 1        | 81       |
| A Env End    | 77     | -      | 1        | 82       |
| A Level      | 78     | -      | 1        | 83       |
| B Env Attack | 79     | -      | 1        | 84       |
| B Env Decay  | 80     | -      | 1        | 85       |
| B Env End    | 81     | -      | 1        | 86       |
| B Level      | 82     | -      | 1        | 87       |
| A Delay      | 83     | -      | 1        | 88       |
| A Trig       | 84     | -      | 1        | 89       |
| A Env Reset  | 85     | -      | 1        | 90       |
| B Delay      | 86     | -      | 1        | 91       |
| B Trig       | 87     | -      | 1        | 92       |
| B Env Reset  | 88     | -      | 1        | 93       |
| Phase Reset  | 89     | -      | 1        | 94       |

### 3.4 Filter Parameters

| Parameter        | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| ---------------- | ------ | ------ | -------- | -------- |
| Filter Frequency | 23     | 55     | 1        | 20       |
| Resonance        | 24     | 56     | 1        | 21       |
| Filter Type      | 74     | -      | 1        | 22       |
| Attack Time      | 70     | -      | 1        | 16       |
| Decay Time       | 71     | -      | 1        | 17       |
| Sustain Level    | 72     | -      | 1        | 18       |
| Release Time     | 73     | -      | 1        | 19       |
| Env. Depth       | 25     | 57     | 1        | 23       |
| Env. Delay       | 43     | -      | 1        | 66       |
| Base             | 26     | 58     | 1        | 24       |
| Width            | 27     | 59     | 1        | 25       |

### 3.5 Amp Parameters

| Parameter     | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| ------------- | ------ | ------ | -------- | -------- |
| Attack Time   | 104    | -      | 1        | 32       |
| Decay Time    | 105    | -      | 1        | 33       |
| Sustain Level | 106    | -      | 1        | 34       |
| Release Time  | 107    | -      | 1        | 35       |
| Drive         | 9      | 41     | 1        | 36       |
| Pan           | 10     | 42     | 1        | 37       |
| Volume        | 7      | 39     | 1        | 38       |
| Chorus Send   | 12     | 44     | 1        | 41       |
| Delay Send    | 13     | 45     | 1        | 40       |
| Reverb Send   | 14     | 46     | 1        | 39       |
| Amp Env Reset | 102    | -      | 1        | 42       |

### 3.6 LFO Parameters

| Parameter        | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| ---------------- | ------ | ------ | -------- | -------- |
| Speed LFO1       | 28     | 60     | 1        | 48       |
| Multiplier LFO1  | 108    | -      | 1        | 49       |
| Fade In/Out LFO1 | 109    | -      | 1        | 50       |
| Destination LFO1 | 110    | -      | 1        | 51       |
| Waveform LFO1    | 111    | -      | 1        | 52       |
| Start Phase LFO1 | 112    | -      | 1        | 53       |
| Trig Mode LFO1   | 113    | -      | 1        | 54       |
| Depth LFO1       | 29     | 61     | 1        | 55       |
| Speed LFO2       | 30     | 62     | 1        | 57       |
| Multiplier LFO2  | 114    | -      | 1        | 58       |
| Fade In/Out LFO2 | 115    | -      | 1        | 59       |
| Destination LFO2 | 116    | -      | 1        | 60       |
| Waveform LFO2    | 117    | -      | 1        | 61       |
| Start Phase LFO2 | 118    | -      | 1        | 62       |
| Trig Mode LFO2   | 119    | -      | 1        | 63       |
| Depth LFO2       | 31     | 63     | 1        | 64       |

### 3.7 MIDI Track Parameters

#### CC Value

| Parameter | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| --------- | ------ | ------ | -------- | -------- |
| CC Val1   | 70     | -      | -        | -        |
| CC Val2   | 71     | -      | -        | -        |
| CC Val3   | 72     | -      | -        | -        |
| CC Val4   | 73     | -      | -        | -        |
| CC Val5   | 74     | -      | -        | -        |
| CC Val6   | 75     | -      | -        | -        |
| CC Val7   | 76     | -      | -        | -        |
| CC Val8   | 77     | -      | -        | -        |

### 3.8 FX Parameters

#### Chorus

| Parameter   | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| ----------- | ------ | ------ | -------- | -------- |
| Depth       | 3      | 35     | 2        | 0        |
| Speed       | 9      | 41     | 2        | 1        |
| High-pass   | 70     | -      | 2        | 2        |
| Width       | 71     | -      | 2        | 3        |
| Delay Send  | 12     | 44     | 2        | 4        |
| Reverb Send | 13     | 45     | 2        | 5        |
| Mix Volume  | 14     | -      | 2        | 6        |

#### Delay

| Parameter       | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| --------------- | ------ | ------ | -------- | -------- |
| Delay Time      | 15     | 47     | 2        | 10       |
| Pingpong        | 16     | 48     | 2        | 11       |
| Stereo Width    | 17     | 49     | 2        | 12       |
| Feedback        | 18     | 50     | 2        | 13       |
| Highpass Filter | 72     | -      | 2        | 14       |
| Lowpass Filter  | 73     | -      | 2        | 15       |
| Reverb Send     | 19     | 51     | 2        | 16       |
| Mix Volume      | 20     | -      | 2        | 17       |

#### Reverb

| Parameter       | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| --------------- | ------ | ------ | -------- | -------- |
| Predelay        | 21     | 53     | 2        | 20       |
| Decay Time      | 74     | -      | 2        | 21       |
| Shelving Freq   | 75     | -      | 2        | 22       |
| Shelving Gain   | 22     | 54     | 2        | 23       |
| Highpass Filter | 76     | -      | 2        | 24       |
| Lowpass Filter  | 77     | -      | 2        | 25       |
| Mix Volume      | 23     | -      | 2        | 26       |

#### Master

| Parameter        | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| ---------------- | ------ | ------ | -------- | -------- |
| Master Overdrive | 29     | 61     | 2        | 37       |
| Dual Mono        | 83     | -      | 2        | 105      |
| Input L Volume   | 24     | 56     | 2        | 30       |
| Input R Volume   | 25     | 57     | 2        | 32       |
| Pan L            | 78     | -      | 2        | 31       |
| Pan R            | 79     | -      | 2        | 33       |
| Chorus Send L    | 26     | 58     | 2        | 34       |
| Chorus Send R    | 30     | 62     | 2        | 102      |
| Delay Send L     | 27     | 59     | 2        | 35       |
| Delay Send R     | 31     | 63     | 2        | 103      |
| Reverb Send L    | 28     | 60     | 2        | 36       |
| Reverb Send R    | 82     | 32     | 2        | 104      |
| Chorus Send L/R  | 26     | 58     | 2        | 34       |
| Delay Send L/R   | 27     | 59     | 2        | 35       |
| Reverb Send L/R  | 28     | 60     | 2        | 36       |
| Pattern Volume   | 95     | -      | 2        | 38       |

### 3.9 Misc Parameters

| Parameter    | CC MSB | CC LSB | NRPN MSB | NRPN LSB |
| ------------ | ------ | ------ | -------- | -------- |
| Pattern Mute | -      | -      | 1        | 104      |
| Sustain      | 64     | -      | -        | -        |
| Sostenuto    | 66     | -      | -        | -        |

---

## 4. LFO Modulation Destinations

### Audio Tracks

#### SYN Parameters

- Algorithm
- Ratio C
- Ratio A
- Ratio B
- Harmonics
- Detune
- Feedback
- Mix
- A Attack
- A Decay
- A End
- A Level
- B Attack
- B Decay
- B End
- B Level
- A Delay
- B Delay
- Pitch All
- Pitch A and B2
- Ratio All
- AB Level
- AB Attack
- AB Decay
- AB End
- AB Delay
- Ratio C Offset
- Ratio A Offset
- Ratio B1 Offset
- Ratio B2 Offset

#### Filter Parameters

- Frequency
- Resonance
- Envelope Depth
- Attack Time
- Decay Time
- Sustain Level
- Release Time
- Base
- Width
- Env. Delay

#### Amplifier Parameters

- Attack Time
- Decay Time
- Sustain Level
- Release Time
- Drive
- Pan
- Volume
- Reverb Send
- Delay Send
- Chorus Send

### MIDI Tracks

#### SRC (Source) Parameters

- Pitch Bend
- Aftertouch
- Mod Wheel
- Breath Controller

#### CC Parameters

- CC1 Value
- CC2 Value
- CC3 Value
- CC4 Value
- CC5 Value
- CC6 Value
- CC7 Value
- CC8 Value

---

## Notes

- When using CC messages, parameters with both CC MSB and CC LSB support 14-bit resolution (0-16383).
- Parameters with only CC MSB support 7-bit resolution (0-127).
- NRPN messages provide an alternative to CC messages for parameter control.
- The PARAM OUTPUT setting in MIDI CONFIG determines whether CC or NRPN messages are sent.
- MIDI tracks can use any of the standard MIDI CC numbers (1-119) for their eight assignable CC parameters.

---

_Extracted from Digitone User Manual OS 1.41_
