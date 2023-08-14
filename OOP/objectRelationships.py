# class Country:
#     def __init__(self, name=None, population=0):
#         self.name = name
#         self.population = population

#     def printDetails(self):
#         print("Country Name:", self.name)
#         print("Country Population", self.population)


# class Person:
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country

#     def printDetails(self):
#         print("Person Name:", self.name)
#         self.country.printDetails()


# c = Country("Wales", 1500)
# p = Person("Joe", c)
# p.printDetails()

# # deletes the object p
# del p
# print("")
# c.printDetails()


# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
    
#     def printDetails(self):
#         print("Model:", self.model)
#         print("Color:", self.color)


# class SedanEngine:
#     def __init__(self):
#         pass
    
#     def start(self):
#         print ("Car has started.")

#     def stop(self):
#         print("Car has stopped.")



# class Sedan(Car):
#     def __init__(self, model, color):
#         super().__init__(model, color)
#         self.engine = SedanEngine()

    
#     def setStart(self):
#         self.engine.start()
    
#     def setStop(self):
#         self.engine.stop()
    

# car1 = Sedan("Toyota","Grey")
# car1.setStart()
# car1.printDetails()
# car1.setStop()

# class Player:
#     def __init__(self, ID, name, teamName):
#         self.id = ID
#         self.name = name
#         self.teamname = teamName

# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.players = []

#     def addPlayer(self, newPlayer):
#         newPlayer =[]
#         self.newPlayer = newPlayer.append(self.players)

#     def getNumberOfPlayers(self):
#         return (len(self.newPlayer))
    

# class School:
#     def __init__(self, teams, name):
#         teams = []
#         self.teams = teams.append(Team)
#         self.name = name

#     def addTeam(self, newTeam):
#         newTeam = []
#         self.newTeam = newTeam.append(self.teams)
    
#     def getTotalPlayersInSchool(self):
#         return (len(self.newTeam))

# Player1 = Player("012", "Bola", "Tigers")
# Player2 = Player ("013", "Chika", "Tigers")
# Team1 = Team("Tigers", "2")
# Team1.addPlayer("James") 
# print(Team1.getNumberOfPlayers())

class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def getNumberOfPlayers(self):
        return len(self.players)

    def addPlayer(self, player):
        self.players.append(player)


class School:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        length = 0
        for n in self.teams:
            length = length + (n.getNumberOfPlayers())
        return length


p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

red_team = Team("Red Team")
red_team.addPlayer(p1)
red_team.addPlayer(p2)

blue_team = Team("Blue Team")
blue_team.addPlayer(p2)
blue_team.addPlayer(p3)

mySchool = School("My School")
mySchool.addTeam(red_team)
mySchool.addTeam(blue_team)

print("Total players in mySchool:", mySchool.getTotalPlayersInSchool())