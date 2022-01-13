# Q.2 The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'HisCore.txt' which is either blank or contains the previous Hi-score. You need to write a pgogram to upload the Hi-score wheather game() breats the Hi-Score.
def game():
    return 55

score = game()
with open ("hiscore.txt") as f:
    hiscore = f.read()
if hiscore == '':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
    
elif int(hiscore)<score:
    with open("hiscore.txt", "w") as f:
        f.write(str(score))