import random
h='''
                         
 |    |   /\   |\  |  |        |\  /|   /\   |\  |
 |----|  /--\  | \ |  |   _ _  | \/ |  /--\  | \ |
 |    | /    \ |  \|  |_ _ _|  |    | /    \ |  \|
 '''
print(h)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''','''
---+---''']
word_list=['kedar','darshan','viraj']
choosen_word=random.choice(word_list)
lives=7
print(f'the solution is {choosen_word}')


display=[]
world_length=len(choosen_word)
for _ in range(world_length):
    display+='_'
end_of_game=False
while not end_of_game:
    guess=input('guess a letter').lower()

    if guess in display:
        print(f'you already choose these letter {guess}')

    for position in range(world_length):
        letter=choosen_word[position]

        if letter==guess:
            display[position]=letter
            print('you choose the letter corectly')

    if guess not in choosen_word:
        print(f'you guess it wrong you have to lose a life')
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose")

    print(display)

    if '_' not in display:
        end_of_game=True
        print("You won")
    
    
    print(stages[lives])



     
  
  