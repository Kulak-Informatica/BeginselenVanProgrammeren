''' 
This is my solution to the seccond question on the exam of 2017. 
The prompt had some weird requirements:
- the name of the person shouldn't be stored in plain text (probably to take away some of the boring work on an exam.)
- making a list of leaders who had someone show up to the event (I guess this question was not properly copied by the student who gave it to us, but I decided to roll with it. AKA to lazy to change it! ) 

If you have any remarks (I'm not perfect) or questions, you can always create an issue on github, or contact me personally(Robbe Decapmaker).

we need:
- Active players
- Tournement leaders
- Boardmember
- tournaments

with this information, we should (for each individual) also store:
- current club
- date of birth
- living place
- date of first attendence 

For the active players, we keep a list of matches which contains this info:
- name of the oponent
- result(lost,draw,win)

Tournament leaders 
- tournaments

tournament
- list of players
- leaderboard


The following functionality should also be possible:
- give a list of oponents of a given player
- list the tournament leaders who have led a tournament with players attending
- give the succesrate of a given player (won + 0.5*draw)
'''



class tournament():
    def __init__(self, name):
        self._name = name
        self._playerlist = []
    
    # get the players who have attended the tounament
    def get_players(self):
        return self._playerlist

    #adding a player to the playerlist, this should be done with the object active player, not the name of a player.
    def add_player(self,player):
        self._playerlist.append(player)

    def add_ranking(self):
        pass
        # Not sure how to implement this one, should we just get a list, or do we have to calculat it our selves?
        # The question promt is not clear about this. furthermore in this state of the porgram, we don't have enough info to do it our selves.
        # Feel free to create a github issue!
    
# A standard member class to inheret from.
# Also the class for a board member (no special requirements)
class member():
    def __init__(self, club, birthday, adress, firstday):
        self._club = club
        self._birthday = birthday
        self._adress = adress
        self._firstday = firstday

# The class for active players
class active_player(member):

    def __init__(self,club,birthday,adress,firstday):
        super().__init__(club,birthday,adress,firstday)
        self._matchresults = dict()
    
    # Adding a match to the players results list. oponent_name is the name of the oponent, result is the result of the game
    def add_match(self,oponent_name,result):
        self._matchresults[oponent_name] = result
    
    # This returns a set of oponents, this makes sure we do not have double entry's
    def get_oponents(self):
        oponents = set()
        for oponent in self._matchresults.keys():
            oponents.add(oponent)
        return oponents

    # This calculates the succesrate of a player.
    def get_succes(self):
        succes = 0
        for value in self._matchresults.values():
            if value == 'won':
                succes += 1
            if value == 'draw':
                succes += 0.5
        return succes

# the class for  tournament leaders
class tournament_leader(member):
    def __init__(self, club , birthday, adress, firstday):
        super().__init__(club,birthday,adress,firstday)
        self._tournaments = []

    # Adding a tournament which has been led by this individual, tournaments are objects, not names!
    def add_tournament(self, tournament):
        self._tournaments.append(tournament)
    
    # This is to know if a leader has had players in the tournament
    def get_tournaments(self):
        for tournament in self._tournaments:
            if len(tournament.get_players()) != 0:
                return True
        return False

# this is an example run:
def testrun():
    
    #creating 2 tournaments
    tournament1 = tournament("tournament1")
    tournament2 = tournament("tournament2")

    #creating 2 players
    Jane = active_player("club1", "01/01/69", "street", "01/01/96")
    John = active_player("club1", "01/01/69", "street", "01/01/96")

    #creating 2 leaders
    Smith = tournament_leader("club1", "01/01/69", "street", "01/01/96")
    Doe = tournament_leader("club1", "01/01/69", "street", "01/01/96")

    #assigning leaders to a tournament
    Smith.add_tournament(tournament1)
    Doe.add_tournament(tournament2)

    #adding players to a tournament
    tournament1.add_player(Jane)
    tournament1.add_player(John)

    #creating a match between players
    John.add_match(Jane,'lost')
    Jane.add_match(John,'won')
    
    #printing the succesrate of players
    print("Jane: " + str(Jane.get_succes()))
    print("John: " + str(John.get_succes()))

    #getting the list of oponents for a player (this has a weird output because we do not store the name of a player in plain text, but rather as a variable name. I know this is a stupid choice, but I'm far to lazy to change it! Also the prompt didn't ask for it.)
    print("Oponents to Jane: " + str(Jane.get_oponents()))
    
    #the tournament leaders who have had people show up at the event (Again: to lazy to make a proper output.)
    for leader in [Smith, Doe]:
        if leader.get_tournaments():
            print(leader)

testrun()