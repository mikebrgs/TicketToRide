import json, sys, random

# Player class
class Player():
  def __init__(self, name):
    self.name = name
    self.carriages = 0
    self.ticketHand = list()
    self.carriageHand = list()
    self.points = 0

class CarriageCard():
  def __init__(self, colour):
    self.colour = colour

class TicketCard():
  def __init__(self, cityA, cityB, points):
    self.cities = [cityA, cityB]
    self.points = points

class Route():
  def __init__(self, cityA, cityB, colour, carriages):
    self.cities = [cityA, cityB]
    self.colour = colour
    self.carriages = carriages

# Game class
class TicketToRide():
  def __init__(self):
    # This should be a list of touples
    # (city A, city B, carriages, colour)
    self.board = list()
    # This should also be a list of strings/characters
    # (type)
    self.carriageDeck = list()
    # This is the same but the cards are visible
    self.carriageVisible = list()
    # Discarded cards
    self.carriageDiscarded = list()
    # This should also be a list of touples
    # (city A, city B, carriages)
    self.ticketDeck = list()
    # Discarded cards
    self.ticketDiscarded = list()
    # This should be a list of players
    # Players are an object
    self.players = list()
    ## Game settings
    self.pointSystem = dict()
    self.carriages = 0
    self.startCarriageCards = 0
    self.startTickets = 0

  def newPlayer(self, name):
    player = Player(name)
    self.players.append()

  def load(self, filename):
    try:
      config = json.load(open(filename))
    except:
      print("Error loading JSON file")
      return False
    try:
      for carriageType in config["carriageTypes"]:
        for i in range(0, carriageType["count"]):
          self.carriageDeck.append(CarriageCard(carriageType["colour"]))
      for ticket in config["tickets"]:
        self.ticketDeck.append(TicketCard(ticket["cityA"],
          ticket["cityB"],
          ticket["points"]))
      for point in config["pointSystem"]:
        self.pointSystem[point["carriages"]] = point["points"]
      for route in config["board"]:
        self.board.append(Route(route["cityA"],
          route["cityB"],
          route["colour"],
          route["carriages"]))
      self.carriages = config["playerSettings"]["carriages"]
      self.startCarriageCards = config["playerSettings"]["startCarriageCards"]
      self.startTickets = config["playerSettings"]["startTickets"]

    except:
      print("Problem with JSON format")
    return True

  # Set the game as ready to start
  def reset(self):
    # Shuffle the deck


  def play(self):
    pass

class GameAnalytics(object):
  def __init__(self, arg):


## Debug
def main():
  ttr = TicketToRide()
  ttr.load("/Users/mikebrgs/CurrentWork/playground/ttrAgent/configs/us.json")

if __name__ == "__main__":
  main()