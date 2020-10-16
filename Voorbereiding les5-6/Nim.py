# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:35:08 2020

@author: Thibaut
"""

import random

def main():
    a_piles = int(input("Maximaal aantal stapeltjes voor de randomizer (minimaal 2): \n> "))
    while a_piles < 2: a_piles = int(input("Maximaal aantal stapeltjes voor de randomizer (minimaal 2): \n> ")) 
    a_lucifers = int(input("Maximaal aantal lucifers per stapeltje voor de randomizer (minimaal 1): \n> ")) 
    while a_piles < 1: a_lucifers = int(input("Maximaal aantal lucifers per stapeltje voor de randomizer (minimaal 1): \n> ")) 
    
    board = generate(a_piles, a_lucifers)
    
    
    winner = ""
    if input("Wil je tegen de computer spelen? (j/n): \n> ") == "j":
        pl1 = random.choice(["Speler1", "Computer"])
        print("\nJij mag beginnen!") if pl1=="Speler1" else print("\nDe computer mag beginnen!")
        vC(board, pl1)
        
    else:
        pl1 = random.choice(["Speler1", "Speler2"])
        print("\nSpeler 1 mag beginnen!") if pl1=="Speler1" else print("\nSpeler 2 mag beginnen!")
        v1(board, pl1)
        
        
        
def exitGame(pl, gameMode):
    if pl == "Speler1" and gameMode == "vC":
        print("\nComputer wint")
    elif pl == "Speler1":
        print("\nSpeler2 wint")
    else:
        print("\nSpeler1 wint")
        

        
def generate(a_piles, a_lucifers):
    piles = random.randint(2, a_piles)
    board = dict()
    for i in range(piles):
        name = "Stapel " + str(i+1)
        board[name] = random.randint(1, a_lucifers)
        
    #return {"Stapel 1": 3, "Stapel 2": 4, "Stapel 3": 5}
    return board
    


def v1(board, pl):
    printBoard(board)
    if checkBoard(board):
        board = movePl(board)
        pl = changePlayer(pl, "v1")
        v1(board, pl)
   
    else:
        exitGame(pl1, "v1")


def vC(board, pl):
    printBoard(board)
    if checkBoard(board):
        if pl == "Speler1":
            board = movePl(board)
        else:
            board = moveCo(board)
            
        pl = changePlayer(pl, "vC")
        vC(board, pl)
    else:
        exitGame(pl, "vC")
    

def changePlayer(pl, gameMode):
    if pl == "Speler1" and gameMode == "vC":
        pl = "Computer"
    elif pl == "Speler1":
        pl = "Speler2"
    else:
        pl = "Speler1"
    
    return pl

    
    
def movePl(board):
    calcBoard(board)
    
    #hulpmiddel
    print(calcBoard(board))
    
    pile = int(input("Geef het nummer van de stapel van je zet: "))
    while pile > len(board) or 0 == board["Stapel "+str(pile)]:
        pile = int(input(f"We spelen met maar {len(board)} stapels, probeer opnieuw: "))
    luc = int(input(f"Geef het van het aantal lucifers dat je wilt weghalen van stapel {pile}: "))
    while luc > board["Stapel "+str(pile)] or luc == 0:
        luc = int(input(f"Stapel {pile} heeft maar {board['Stapel '+str(pile)]} lucifers, probeer opnieuw: "))
        
    pile = "Stapel "+str(pile)
    board[pile] = board[pile] - luc
    
    return board
    

def moveCo(board):
    nextMove = calcBoard(board)
    if nextMove == []:
        choice = random.choice(list(board.keys()))
        while board[choice] == 0:
            choice = random.choice(list(board.keys()))
        nextMove = [choice, random.randint(1, board[choice])]
        
    boodschap = "De computer deed "
    if nextMove[1] == board[nextMove[0]]:
        boodschap += "alle lucifers van " + nextMove[0] + " weg!"
    elif nextMove[1] > 1:
        boodschap += str(nextMove[1]) + " lucifers van " + nextMove[0] + " weg!"
    else:
        boodschap += str(nextMove[1]) + " lucifer van " + nextMove[0] + " weg!"
        
    board[nextMove[0]] -= nextMove[1]
    print(boodschap)
    
    
    return board
    
    
     
def printBoard(board):
    print("\n"+"="*30)
    for k, v in board.items():
        print(f"{k}: {v*'| '}")
    print(""+"="*30)   
        

def checkBoard(board):
    som = 0
    for k, v in board.items():
        som += v
    if som > 0:
        return True
    
    return False
        
        
        
def calcBoard(board):
    nim = 0
    for k, v in board.items():
        nim = nim ^ v

    zetLijst = []
    for k, v in board.items():
        X = v ^ nim
        if X < v:
            zetLijst = [k, abs(X-v)]
    
    return zetLijst



main()