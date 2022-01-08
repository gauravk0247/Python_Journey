# Write a program to fill in a letter template given below with name and date.
letter = '''Congraluations Dear <|NAME|>
        You are Selected to IMONSAR Technology for Role of Full Stack Developer.
        thanks and regards Imonsar Technology Pvt Ltd

         <|Date|>'''
letter = letter.replace("<|NAME|>", "Gaurav")
letter = letter.replace("<|Date|>", "26 November 2021")
print(letter)
       