from math import log2


def frequencyOfNotes():
    """
    This function return a list of frequency of all musical notes that
    is produced by piano.
    :return:
    """
    la, q, l1 = 27.5, 2, []
    for i in range(1, 88 + 1):
        lg = 1 + log2(2 ** ((i - 1) / 12))
        f = la * q ** (lg - 1)
        l1.append(f)
    return l1


def musicalNotes(l1):
    """
    This function print the musical note, its octave, and  your frequency.
    :param l1:
    :return:
    """
    k = int(input("Digit a key beteween 1 to 88 to as it has in piano: "))
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    la, q, cont = 27.5, 2, 12
    lg = 1 + log2(2 ** ((k - 1) / 12))
    f = la * q ** (lg - 1)
    octv = ((k - 4) // 12)
    if octv == 0:
        octv = 1
    else:
        octv += 1
    for i in range(0, len(l1)):
        if i <= 2 and l1[2] >= f:
            print(f"This key is the note '{notes[8 + k]}' in the piano. "
                  f"All the classical pianos start with note '{notes[9]}' "
                  f"and ends with note '{notes[0]}'.)")
            break
        if i > 2 and l1[i] % f == 0:
            n = l1.index(l1[i]) - 3
            print(f"This key is the note '{notes[n + cont]}' are in the {octv}º oitava "
                  f"and your frequency is {l1[i]:.2f} Hz.")
            break
        if i % 12 == 0:
            cont -= 12


musicalNotes(frequencyOfNotes())
