########################################
# Name: Christian Chambers
# Collaborators (if any): 
# GenAI Transcript (if any): 
# Estimated time spent (hr): 7
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    gw = WordleGWindow()
    
    ENGLISH_WORDS_5 = []
    
    for word in range(len(ENGLISH_WORDS)):
        if len(ENGLISH_WORDS[word])==5:
            ENGLISH_WORDS_5.append(ENGLISH_WORDS[word])
    
    
    
    WORD = ENGLISH_WORDS_5[random.randrange(len(ENGLISH_WORDS_5))]
    
    col = 0
    row = 0
    N_ROWS = 6
    gw.show_message(WORD)
    def word_to_row(word:str,row,):
        for Letter in len(word):
            gw.set_square_letter(row,Letter,word[Letter].upper())
            col +=1
    def word_from_row():
        row = gw.get_current_row()
        GUESS=''
        for col in range(5):
            GUESS += gw.get_square_letter(row,col)
        GUESS= GUESS.lower()
        return GUESS
            
            


        
    def check_letters():
        row = gw.get_current_row()
        remain = WORD
        GUESS=word_from_row()
        for letter in range(len(GUESS)):
            if GUESS[letter]==WORD[letter]:
                gw.set_square_color(row,letter,CORRECT_COLOR)
                gw.set_key_color(GUESS[letter],CORRECT_COLOR)
                remain = remain[:letter]+'_'+remain[letter+1:]
        for letter in range(len(GUESS)):
            if GUESS[letter] in remain and gw.get_square_color(row, letter)!=CORRECT_COLOR:
                gw.set_square_color(row,letter,PRESENT_COLOR)
                if gw.get_key_color(GUESS[letter])!=CORRECT_COLOR:
                    gw.set_key_color(GUESS[letter],PRESENT_COLOR)
                remain=remain.replace(GUESS[letter],'_',1)
            elif gw.get_square_color(row, letter)!=CORRECT_COLOR and gw.get_square_color(row, letter)!=PRESENT_COLOR:
                gw.set_square_color(row, letter,MISSING_COLOR)
                if gw.get_key_color(GUESS[letter])!=CORRECT_COLOR and gw.get_key_color(GUESS[letter])!=PRESENT_COLOR:
                    gw.set_key_color(GUESS[letter],MISSING_COLOR)

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        if word_from_row() == WORD:
            check_letters()
            gw.show_message('you win')
            gw.set_current_row(N_ROWS)
        elif word_from_row() in ENGLISH_WORDS_5:
            check_letters()
            row = gw.get_current_row()
            gw.set_current_row(row+1)
            if row+1 == N_ROWS:
                gw.show_message('The Word Was '+WORD)
        else:
            gw.show_message("Not a word in the english languidge")
    
    
    
    gw.add_enter_listener(enter_action)













# Startup boilerplate
if __name__ == "__main__":
    wordle()
