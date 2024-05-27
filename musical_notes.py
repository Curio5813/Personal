from math import log2


def frequency_of_notes():
    """
    This function return a list of frequency of all musical notes that
    is produced by piano.
    :return:
    """
    la, q, l1 = 27.5, 2, []
    for i in range(-10, 88 + 1):
        lg = 1 + log2(2 ** ((i - 1) / 12))
        f = la * q ** (lg - 1)  # This formula above and in this row calculate the frequency
        l1.append(f)            # in the temperated music instruments.
    return l1


def musical_notes(l1):
    """
    This function print the musical note, its octave, and  your frequency.
    :param l1:
    :return:
    """
    note, answer1, answer2 = [], [], []
    for k in range(-21, 89):
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        la, q, cont = 27.5, 2, 12
        lg = 1 + log2(2 ** ((k - 1) / 12))
        f = la * q ** (lg - 1)
        octv = ((k - 4) // 12)  # This formula calculate the octave in piano's keyboard.
        if octv == 0:
            octv = 1
        else:
            octv += 1
        for i in range(0, len(l1)):  # Iterations in the list with frequencys.
            if i > 2 and l1[i] % f == 0:
                n = l1.index(l1[i]) - 3
                note.append(notes[n + cont] + str(octv + 1))
                break
            if i % 12 == 0:
                cont -= 12
    print(*note)
    notas = ['G#4', 'F#1', 'G#2', 'A#1', 'E5', 'A4', 'A#3', 'E1', 'A3', 'A2', 'D#5', 'G#5',
             'B2', 'A1', 'F2', 'D5', 'F4', 'C#3', 'D1', 'B3', 'F#2', 'C#5']
    print(len(notas))
    for k in range(0, len(notas)):
        for i in range(0, len(note)):
            if notas[k] == note[i]:
                answer1.append(notas[k])


musical_notes(frequency_of_notes())
