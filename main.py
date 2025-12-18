# Leagues

# Libraries
import os
import json
import shutil
import datetime
import random
import time

# Variables

global savesFol
savesFol = "saves/"

flagDEV = True

# GAME VARIABLES

 # Team Overalls
ovr1 = 89
ovr2 = 86


# Sub functions

def space(): # Used to create the illusion of a changing display in the terminal
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def error(text):
    print("----------------------------\nError!", text, "\n----------------------------")

# New Game Creator

def newGame():
    space()
    print("##########################\n\n[New Game]\n\n##########################\n\n")
    print("Select a League:")
    print("[1] Premier League")
    print("\n[0] Return")

    while True:
        opt = input()
        if opt == "1" or opt == "2" or opt == "3" or opt == "4":
            break

    match opt:
        case "1":

            leagueTeams = ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich", "Leicester", "Liverpool", "Man City", "Man Utd", "Newcastle", "N'ham Forest", "Southampton", "Spurs", "West Ham", "Wolves"]
            space()
            print("Selected League: Premier League\n")
            print("Select a Team:\n")

            for x in range(len(leagueTeams)):
                print(leagueTeams[x])

            print("\n[0] Return")

            while True:
                opt2 = input()

                if opt2 == "0":
                    newGame()
                    break
                else:
                    try:
                        selTeam = leagueTeams[leagueTeams.index(opt2.capitalize())]
                        break
                    except ValueError:
                        error("Team not in league")

            while True:
                space()
                print("Save new game as:")
                saveName = input("Save: ")

                if saveName == "0": # Invalid save name check
                    error("Save name cannot be '0'")
                    break

                currentSFol = savesFol + saveName

                try:
                    os.mkdir(currentSFol)
                    break
                except FileExistsError:
                    error("Save game already exists.")
                    ow = input("Overwrite? [y/n]")
                    if ow == "y":
                        shutil.rmtree(currentSFol)
                        os.mkdir(currentSFol)
                        break

            save0 = currentSFol + "/save0.json"

            # Prepare JSON
            
            open(save0, "x")
            save0_w = open(save0, "w")
            save0_w.write("{}")
            save0_w.close()

            save0_j = json.load(open(save0, "r"))

            save0_j["team"] = selTeam
            save0_j["league"] = "Premier League"

            save0_w = open(save0, "w")

            json.dump(save0_j, save0_w)
            
            

        # End of new game
                    
def loadGame():
    space()
    print("##########################\n\n[Load Game]\n\n##########################\n\n")
    saveList = os.listdir(savesFol)

    print("Name      | Last saved")

    # Save file display
        
    for x in range(len(saveList)):
        filePath = savesFol + saveList[x]
        padding = 10 - len(saveList[x])

        saveInfo = saveList[x]
        
        for x in range(padding):
            saveInfo = saveInfo + " "
        saveInfo = saveInfo + "| " + str(datetime.datetime.fromtimestamp(os.path.getmtime(filePath))).split(".", 1)[0]
        print(saveInfo)

    print("\n[0] Return")
    
    while True:
        opt2 = input()

        if opt2 == "0":
            mainMenu()
            break
        else:
            try:
                curSave = saveList[saveList.index(opt2)]
                break
            except ValueError:
                error("Save does not exist")

def playMatch(teamH, teamA, ovrH, ovrA):
    # Read database values

    
    
    clock = 0
    homeG = 0
    awayG = 0
    ftGoals = 0

    injuryMins = random.randint(0,3)
    gameDuration = 90 + injuryMins
    print("Kick off")
    while clock <= gameDuration:
        time.sleep(0.8)
        clock = clock + 1
        space()
        print("Clock: " + str(clock))
        initRNG = random.randint(0,63)

        if homeG >= awayG + 2:
            initRNG = random.randint(0, 100)
        elif awayG >= homeG + 2:
            initRNG = random.randint(0, 100)

        if homeG == awayG:
            drawChance = initRNG = random.randint(0,20)
        if initRNG == 8 or initRNG == 7:
            ovrRNG = random.randint(0, 99)
            if ovrRNG > ovrH:
                pass
            else:
                homeG = homeG + 1
        elif initRNG == 9:
            ovrRNG = random.randint(0, 99)
            if ovrRNG > ovrA:
                pass
            else:
                awayG = awayG + 1

        print(teamH + " " + str(homeG) + " - " + str(awayG) + " " + teamA)

        if clock == 90:
            ftGoals = homeG + awayG
            if ftGoals > 7:
                ftGoals = 7
        gameDuration = 90 + injuryMins + ftGoals

    input("Full time!")
    
def openSettings():
    space()
    print("##########################\n\n[Settings]\n\n##########################\n\n")

    # Developer debugging
    if flagDEV == True:
        print("[1] Test function 1")
        print("[2] Test function 2")
        print("[3] Test function 3")
        print("[0] Exit")

        while True:
            opt = input()
            if opt == "1" or opt == "2" or opt == "3" or opt == "0":
                break

        match opt:
            case "1":
                playMatch("Arsenal", "Aston Villa", ovr1, ovr2)
                pass
            case "2":
                pass
            case "3":
                pass
            case "0":
                mainMenu()
                    
            



    
# Main Menu

def mainMenu():
    space()
    print("##########################\n\n[PyLeagues] by Noah Dainty\n\n##########################\n\n")

    print("[1] New Game")
    print("[2] Load Game")
    print("[3] Settings")
    print("[0] Exit")

    while True:
        opt = input()
        if opt == "1" or opt == "2" or opt == "3" or opt == "0":
            break

    match opt:
        case "1":
            newGame()
        case "2":
            loadGame()
        case "3":
            openSettings()
        case "0":
            exit()


# Running code

while True:
    mainMenu()
