string_midi = {'E':40, 'A':45, 'D':50, 'G':55, 'B':59, 'e':64 }
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
def midi_to_note(midi):
    octave = midi // 12 - 1
    note = notes[midi % 12]
    return '{}{}'.format(note, octave)


def string_to_note(val):
    if len(val) < 2:
        return None
    # Validate string name
    string = val[:1]
    if string_midi.get(string) == None:
        return None
    # Convert to midi note
    fret = int(val[1:])
    midi = string_midi[string] + fret
    return midi_to_note(midi)


