#  Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) 
# and a start position (integer). The function will return the song composed by going though the musical notes 
# beginning with the start position and following the moves given as parameter.

def make_song(musical_notes, moves_list, start_position):
    song = []
    current_position = start_position
    song.append(musical_notes[current_position])
    
    for move in moves_list:
        current_position += move
        if 0 <= current_position < len(musical_notes):
            song.append(musical_notes[current_position])
        if current_position > len(musical_notes):
            song.append(musical_notes[current_position % len(musical_notes)])
    
    return song

musical_notes = ["do", "re", "mi", "fa", "sol"]
moves_list = [1, -3, 4, 2]
start_position = 2

print(f"Cantecul creat este: {make_song(musical_notes, moves_list, start_position)}")
