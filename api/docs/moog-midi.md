# Moog Subsequent 37 MIDI Operations

## MIDI Channel

By default, the Subsequent 37 is set to receive and send MIDI on Channel 1, but it can be configured to send and receive on MIDI Channel (1 - 16).

## MIDI Control Change (CC) Messages

The tables below list all MIDI CC messages for the Subsequent 37.

### LFO Clock Divider Values

MIDI CC values for LFO 1 Clock Divider (CC #3) and LFO 2 Clock Divider (CC #8):

| Time Value | Division | Value Range |
|------------|----------|-------------|
| 4 Whole Notes | 4 WHOLE | 0-6 |
| 3 Whole Notes | 3 WHOLE | 7-12 |
| 2 Whole Notes | 2 WHOLE | 13-18 |
| Whole Note + Half Note | WH + 1/2 | 19-24 |
| Whole Note | WH | 25-30 |
| Dotted 1/2 Note | 1/2 DOT | 31-36 |
| Whole Note Triplet | WH T | 37-42 |
| 1/2 Note | 1/2 | 43-48 |
| Dotted 1/4 Note | 1/4 DOT | 49-54 |
| 1/2 Note Triplet | 1/2 T | 55-60 |
| 1/4 Note | 1/4 | 61-67 |
| Dotted 1/8 Note | 1/8 DOT | 68-73 |
| 1/4 Note Triplet | 1/4 T | 74-79 |
| 1/8 Note | 1/8 | 80-85 |
| Dotted 1/16 Note | 1/16 DOT | 86-91 |
| 1/8 Note Triplet | 1/8 T | 92-97 |
| 1/16 Note | 1/16 | 98-103 |
| 1/16 Note Triplet | 1/16 T | 104-109 |
| 1/32 Note | 1/32 | 110-115 |
| 1/32 Note Triplet | 1/32 T | 116-121 |
| 1/64 Note Triplet | 1/64 T | 122-127 |

### MIDI Control Change (CC) Messages

| Parameter | CC# | Value Range/Description |
|-----------|-----|------------------------|
| Bank Select | 0 | Always transmits 0, should always send 0 when sending this CC |
| Mod Wheel | 1 [MSB], 33 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Reserved - MIDI Breath Ctrl | 2 [MSB], 34 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| LFO 1 Rate | 3 [MSB], 35 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Mod 1 Pitch Amt | 4 [MSB], 36 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Glide Time | 5 [MSB], 37 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Reserved - Data Entry | 6 [MSB], 38 [LSB] | - |
| Master Volume | 7 [MSB], 39 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| LFO 2 Rate | 8 [MSB], 40 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| OSC 1 Wave | 9 [MSB], 41 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Reserved - MIDI Pan | 10 [MSB], 42 [LSB] | - |
| Mod 1 Filter Amt | 11 [MSB], 43 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| OSC 2 Freq | 12 [MSB], 44 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| OSC 2 Beat Freq | 13 [MSB], 45 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| OSC 2 Wave | 14 [MSB], 46 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Mod 2 Pitch Amt | 15 [MSB], 47 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Mod 2 Filter Amt | 16 [MSB], 48 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Mod 2 PGM Dest Amt | 17 [MSB], 49 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Filter Multidrive | 18 [MSB], 50 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Filter Cutoff | 19 [MSB], 51 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Mod 1 PGM Dest Amt | 20 [MSB], 52 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Filter Resonance | 21 [MSB], 53 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Filter KB Amt | 22 [MSB], 54 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Filter EG Attack Time | 23 [MSB], 55 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Filter EG Decay Time | 24 [MSB], 56 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Filter EG Sustain Time | 25 [MSB], 57 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Filter EG Release Time | 26 [MSB], 58 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Filter EG Amt | 27 [MSB], 59 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Amp EG Attack Time | 28 [MSB], 60 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Amp EG Decay Time | 29 [MSB], 61 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Amp EG Sustain Time | 30 [MSB], 62 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Amp EG Release Time | 31 [MSB], 63 [LSB] | 0-127 [MSB], 0-16383[MSB,LSB] |
| Bank Select [LSB] | 32 | 0 = Preset Banks 1-8, 1 = Preset Banks 9-16 |
| Hold Pedal/Sustain | 64 | 0 = OFF / 64 = ON |
| Glide | 65 | 0 = OFF / 64 = ON |
| Arpeggiator Latch | 69 | 0 = OFF / 64 = ON |
| Mod 1 OSC 1/2 Sel | 70 | 0 = OSC1 + OSC2, 43 = OSC1, 85 = OSC2 |
| Mod 1 Source | 71 | 0 = Triangle LFO, 21 = Square LFO, 43 = Saw LFO, 64 = Ramp LFO, 85 = S&H LFO, 107 = F.EG/PGM |
| Mod 2 Source | 72 | 0 = Triangle LFO, 21 = Square LFO, 43 = Saw LFO, 64 = Ramp LFO, 85 = S&H LFO, 107 = F.EG/PGM |
| Arp On/Off | 73 | 0 = OFF / 64 = ON |
| OSC 1 Octave | 74 | 0 = 16', 32 = 8', 64 = 4', 96 = 2' |
| OSC 2 Octave | 75 | 0 = 16', 32 = 8', 64 = 4', 96 = 2' |
| LFO 1 Range | 76 | 0 = Low Range, 43 = Med Range, 85 = Hi Range |
| OSC 2 Hard Sync On/Off | 77 | 0 = OFF / 64 = ON |
| LFO 2 Range | 78 | 0 = Low Range, 43 = Med Range, 85 = Hi Range |
| Filter EG KB Amt | 79 | 0-127 |
| Amp EG KB Amt | 80 | 0-127 |
| OSC KB Reset On/Off | 81 | 0 = OFF / 64 = ON |
| Filter EG Reset | 82 | 0 = OFF / 64 = ON |
| Amp EG Reset | 83 | 0 = OFF / 64 = ON |
| Reserved Portamento Control | 84 | - |
| Glide Type | 85 | 0 = LCR, 43 = LCT, 85 = EXP |
| Filter EG Vel Amt | 86 | 0-127 |
| Amp EG Vel Amt | 87 | 0-127 |
| Mod 2 OSC 1/2 Sel | 88 | 0 = OSC1 + OSC2, 43 = OSC1, 85 = OSC2 |
| KB Octave | 89 | 0 = -2 Oct, 26 = -1 Oct, 51 = +0 Oct, 77 = +1 Oct, 102 = +2 Oct |
| Mod 1 Dest | 91 | 0 = LFO2 Rate, 18 = VCA Level, 37 = OSC1 Wave, 55 = OSC1 + OSC2 Wave, 73 = OSC2 Wave, 91 = Noise Level, 110 = EG Time/PGM |
| Mod 2 Dest | 92 | 0 = LFO1 Rate, 18 = VCA Level, 37 = OSC1 Wave, 55 = OSC1 + OSC2 Wave, 73 = OSC2 Wave, 91 = Noise Level, 110 = EG Time/PGM |
| LFO 1 KB Reset | 93 | 0 = OFF / 64 = ON |
| Glide Legato | 94 | 0 = OFF / 64 = ON |
| LFO 2 KB Reset | 95 | 0 = OFF / 64 = ON |
| Reserved Data Increment | 96 | - |
| Reserved Data Decrement | 97 | - |
| Reserved NRPN LSB | 98 | - |
| Reserved NRPN MSB | 99 | - |
| Reserved RPN LSB | 100 | - |
| Reserved RPN MSB | 101 | - |
| Glide Dest OSC 1/2/Both | 102 | 0 = OSC1 + OSC2, 43 = OSC1, 85 = OSC2 |
| Filter EG Delay | 103 | 0-127 |
| Amp EG Delay | 104 | 0-127 |
| Filter EG Hold | 105 | 0-127 |
| Amp EG Hold | 106 | 0-127 |
| Pitch Bend Up Amount | 107 | 0-24 Semitones |
| Pitch Bend Down Amount | 108 | 0-24 Semitones |
| Filter Slopes (Poles) | 109 | 0 = -6dB, 32 = -12dB, 64 = -18dB, 96 = -24dB |
| OSC Duo Mode On/Off | 110 | 0 = OFF / 64 = ON |
| KB Ctrl Lo/Hi | 111 | 0 = Neither, 32 = Lo, 64 = Hi |
| Filter EG Multi Trig | 112 | 0 = OFF / 64 = ON |
| Amp EG Multi Trig | 113 | 0 = OFF / 64 = ON |
| OSC 1 Level | 114 | 0-127 |
| OSC 1 Sub Level | 115 | 0-127 |
| OSC 2 Level | 116 | 0-127 |
| Noise Level | 117 | 0-127 |
| Feedback/Ext Level | 118 | 0-127 |
| KB Transpose | 119 | Receive Only: -12 to +13 Semitones |
| Local Control On/Off | 122 | 0 = OFF / 127 = ON |
| All Notes Off | 123 | - |

## NRPN Chart

Non Registered Parameter Numbers allow for a much higher number of unique control messages (16,000+).
Since the Subsequent 37 has over 150 parameters saved with each sound, it is not possible to assign a
standard MIDI CC to every parameter. For complete MIDI output from every panel knob and button, you will
need to set the KNB NRPN/CC parameter to NRPN mode.

**Note:** Not every audio production software allows easy editing of NRPN messages, so you may prefer CC
output for ease of use.

| Parameter | Value Range | NRPN | NRPN MSB (CC 99) | NRPN LSB (CC 98) |
|-----------|-------------|------|------------------|------------------|
| Mod Wheel | 16384 | 402 | 3 | 18 |
| Arp Rate | 16384 | 403 | 3 | 19 |
| Arp Sync | 2 | 404 | 3 | 20 |
| Arp Range | 7 | 405 | 3 | 21 |
| Arp Back Forth | 2 | 406 | 3 | 22 |
| Arp BF Mode | 2 | 407 | 3 | 23 |
| Arp Invert | 2 | 408 | 3 | 24 |
| Arp Pattern | 6 | 409 | 3 | 25 |
| Arp Run | 2 | 410 | 3 | 26 |
| Arp Latch | 2 | 411 | 3 | 27 |
| Arp Gate Len | 16384 | 412 | 3 | 28 |
| Arp Clk Div | 21 | 413 | 3 | 29 |
| (Reserved) | - | 414 | 3 | 30 |
| (Reserved) | - | 415 | 3 | 31 |
| Arp Step 1 Reset | 2 | 416 | 3 | 32 |
| Glide Time | 16384 | 417 | 3 | 33 |
| Glide OSC | 3 | 418 | 3 | 34 |
| Glide Type | 3 | 419 | 3 | 35 |
| Glide Gate | 2 | 420 | 3 | 36 |
| Glide Legato | 2 | 421 | 3 | 37 |
| Glide On | 2 | 422 | 3 | 38 |
| LFO 1 Rate | 16384 | 423 | 3 | 39 |
| LFO 1 Range | 3 | 424 | 3 | 40 |
| LFO 1 Sync | 2 | 425 | 3 | 41 |
| LFO 1 KB Reset | 2 | 426 | 3 | 42 |
| LFO 1 Clk Div | 21 | 427 | 3 | 43 |
| LFO 1 Clk Src | 2 | 428 | 3 | 44 |
| (Reserved) | - | 429 | 3 | 45 |
| LFO 1 KB Track | 16384 | 430 | 3 | 46 |
| (Reserved) | - | 431 | 3 | 47 |
| (Reserved) | - | 432 | 3 | 48 |
| (Reserved) | - | 433 | 3 | 49 |
| Mod 1 MWHL Amt | 16384 | 434 | 3 | 50 |
| (Reserved) | - | 435 | 3 | 51 |
| Mod 1 Velocity Amt | 16384 | 436 | 3 | 52 |
| Mod 1 Pressure Amt | 16384 | 437 | 3 | 53 |
| Mod 1 CTL4 Amt | 16384 | 438 | 3 | 54 |
| (Reserved) | - | 439 | 3 | 55 |
| Mod 1 Source | 6 | 440 | 3 | 56 |
| Mod 1 PGM Src | 8 | 441 | 3 | 57 |
| Mod 1 Dest | 7 | 442 | 3 | 58 |
| Mod 1 PGM Dest | 89 | 443 | 3 | 59 |
| Mod 1 PGM Amt | 16384 | 444 | 3 | 60 |
| Mod 1 Pitch Amt | 16384 | 445 | 3 | 61 |
| Mod 1 Filter Amt | 16384 | 446 | 3 | 62 |
| Mod 1 Pitch Dest | 3 | 447 | 3 | 63 |
| LFO 2 Rate | 16384 | 448 | 3 | 64 |
| LFO 2 Range | 3 | 449 | 3 | 65 |
| LFO 2 Sync | 2 | 450 | 3 | 66 |
| LFO 2 KB Reset | 2 | 451 | 3 | 67 |
| LFO 2 Clk Div | 21 | 452 | 3 | 68 |
| LFO 2 Clk Src | 2 | 453 | 3 | 69 |
| (Reserved) | - | 454 | 3 | 70 |
| LFO 2 KB Track | 16384 | 455 | 3 | 71 |
| (Reserved) | - | 456 | 3 | 72 |
| (Reserved) | - | 457 | 3 | 73 |
| (Reserved) | - | 458 | 3 | 74 |
| (Reserved) | - | 459 | 3 | 75 |
| Mod 2 MWHL Amt | 16384 | 460 | 3 | 76 |
| Mod 2 Velocity Amt | 16384 | 461 | 3 | 77 |
| Mod 2 Pressure Amt | 16384 | 462 | 3 | 78 |
| Mod 2 CTL4 Amt | 16384 | 463 | 3 | 79 |
| (Reserved) | - | 464 | 3 | 80 |
| Mod 2 Source | 6 | 465 | 3 | 81 |
| Mod 2 PGM Src | 8 | 466 | 3 | 82 |
| Mod 2 Dest | 7 | 467 | 3 | 83 |
| Mod 2 PGM Dest | 89 | 468 | 3 | 84 |
| Mod 2 PGM Amt | 16384 | 469 | 3 | 85 |
| Mod 2 Pitch Amt | 16384 | 470 | 3 | 86 |
| Mod 2 Filter Amt | 16384 | 471 | 3 | 87 |
| Mod 2 Pitch Dest | 3 | 472 | 3 | 88 |
| (Reserved) | - | 473 | 3 | 89 |
| (Reserved) | - | 474 | 3 | 90 |
| (Reserved) | - | 475 | 3 | 91 |
| (Reserved) | - | 476 | 3 | 92 |
| (Reserved) | - | 477 | 3 | 93 |
| (Reserved) | - | 478 | 3 | 94 |
| OSC 1 Octave | 4 | 479 | 3 | 95 |
| OSC 1 Wave | 16384 | 480 | 3 | 96 |
| OSC 2 Hard Sync | 2 | 481 | 3 | 97 |
| OSC KB Reset | 2 | 482 | 3 | 98 |
| OSC 2 Octave | 4 | 483 | 3 | 99 |
| OSC 2 Wave | 16384 | 484 | 3 | 100 |
| OSC 2 KB Ctrl | 3 | 485 | 3 | 101 |
| OSC 2 Duo Mode | 16384 | 486 | 3 | 102 |
| OSC 2 Frequency | 3 | 487 | 3 | 103 |
| OSC 2 Beat | 2 | 488 | 3 | 104 |
| OSC 1 Level | 2 | 489 | 3 | 105 |
| OSC 1 On | 21 | 490 | 3 | 106 |
| Sub OSC On | 2 | 491 | 3 | 107 |
| Sub OSC Level | 16384 | 492 | 3 | 108 |
| OSC 2 Level | 16384 | 493 | 3 | 109 |
| OSC 2 On | 2 | 494 | 3 | 110 |
| Noise On | 2 | 495 | 3 | 111 |
| Noise Level | 16384 | 496 | 3 | 112 |
| FB Ext Level | 16384 | 497 | 3 | 113 |
| FB Ext On | 2 | 498 | 3 | 114 |
| Filter Cutoff | 16384 | 499 | 3 | 115 |
| Filter Resonance | 500 | 500 | 3 | 116 |
| Filter Drive | 16384 | 501 | 3 | 117 |
| Filter Slope | 4 | 502 | 3 | 118 |
| Filter EG Amt | 16384 | 503 | 3 | 119 |
| Filter KB Amt | 16384 | 504 | 3 | 120 |
| F EG Attack | 16384 | 505 | 3 | 121 |
| F EG Decay | 16384 | 506 | 3 | 122 |
| F EG Sustain | 16384 | 507 | 3 | 123 |
| F EG Release | 16384 | 508 | 3 | 124 |
| F EG Delay | 16384 | 509 | 3 | 125 |
| F EG Hold | 16384 | 510 | 3 | 126 |
| F EG Vel Amt | 16384 | 511 | 3 | 127 |
| F EG KB Track | 16384 | 512 | 4 | 0 |
| F EG Multi Trig | 2 | 513 | 4 | 1 |
| F EG Reset | 2 | 514 | 4 | 2 |
| F EG Sync | 2 | 515 | 4 | 3 |
| F EG Loop | 2 | 516 | 4 | 4 |
| F EG Latch | 2 | 517 | 4 | 5 |
| F EG Clk Div | 2 | 518 | 4 | 6 |
| (Reserved) | - | 519 | 4 | 7 |
| F EG Attk Exp | 2 | 520 | 4 | 8 |
| (Reserved) | - | 521 | 4 | 9 |
| (Reserved) | - | 522 | 4 | 10 |
| (Reserved) | - | 523 | 4 | 11 |
| (Reserved) | - | 524 | 4 | 12 |
