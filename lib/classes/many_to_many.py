class Game:
    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and len(title) > 0:
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        total_score = sum(result.score for result in player.results())
        players = [result.player for result in player.results()]
        num_players = len(players)

        return total_score / num_players

class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played() # True if it exists, False if it doesn't.

    def num_times_played(self, game):
        games = [result.game for result in self.results()] # Creates a list of every game played by player via their results, without making it a unique set.
        return games.count(game) # Uses built in count method to count each item in the list, which takes in that one game argument, so giving the count for that particular game.

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game