"""
class:

Player:
 - name
 - total_runs
 - fours
 - sixes
 - is_out
Team
 - player
 - total_runs
 - current_player
 - non_striker
 - wickets
 - extras
 - get_scoreboard()
 - swap_strike()

ScoreBoard
 - team
 - overs
 - current_over
 - current_team_index
 - swap_teams()
 - input_balls()
 - play_match()
 - determine_winner()

 Match() - API Interface
  - start()

Match
"""

class Player:
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.fours = 0
        self.sixes = 0
        self.is_out = 0
        self.balls_faced = 0

    def add_runs(self, run):
        self.runs += run
        self.balls_faced += 1

        if run == 4:
            self.fours += 1

        if run == 6:
            self.sixes += 1

    def out(self):
        self.is_out = True

    def __str__(self):
        return f"{self.name} - {self.runs} ({self.balls_faced} balls), 4s: {self.fours}, 6s: {self.sixes}"


class Team:
    def __init__(self, team_name, players):
        self.name = team_name
        self.players = [Player(player) for player in players]
        self.extras = 0
        self.total_runs = 0
        self.wickets = 0
        self.current_batsman = 0
        self.non_striker = 1

    def add_runs(self, run, is_extra=False):
        self.total_runs += run
        if is_extra:
            self.extras += 1

        self.players[self.current_batsman].add_runs(run)

    def wicket(self):
        self.wickets += 1
        self.players[self.current_batsman].out()

        self.current_batsman = max(self.current_batsman, self.non_striker) + 1

    def swap_strike(self):
        self.current_batsman, self.non_striker = self.non_striker, self.current_batsman

    def get_scorecard(self):
        scorecard = f"Scorecard for {self.name}:\n"
        for player in self.players:
            star = '*' if not player.is_out and player == self.players[self.current_batsman] else ''
            scorecard += f"{player.name}{star} {player.runs} {player.fours} {player.sixes} {player.balls_faced}\n"
        scorecard += f"Total: {self.total_runs}/{self.wickets}, Extras: {self.extras}\n"
        return scorecard


class Scoreboard:
    def __init__(self, team1, team2, overs):
        self.teams = [team1, team2]
        self.overs = overs
        self.current_over = 0
        self.current_team_index = 0

    def input_ball(self, runs):
        current_team = self.teams[self.current_team_index]

        if runs in ("W", "w"):
            current_team.wicket()

        elif runs in ("Wd", "Nb"):
            current_team.add_runs(1, is_extra=True)

        else:
            current_team.add_runs(runs)

            if runs in (1, 3):
                current_team.swap_strike()

    def print_score(self):
        current_team = self.teams[self.current_team_index]

        print(current_team.get_scorecard())

    def play_match(self, balls):
        for ball in balls:
            if ball in ("W", "w", "Wd", "Nb"):
                    self.input_ball(ball)
            else:
                ball = int(ball)
                self.input_ball(ball)

            if ball != "Wd" or ball != "Nb":
                self.current_over += 1

                if self.current_over % 6 == 0:
                    self.teams[self.current_team_index].swap_strike()
                    self.print_score()

    def switch_team(self):
        # Switch to the other team
        self.current_team_index = 1 - self.current_team_index

    def determine_winner(self):
        for team in self.teams:
            print(team.get_scorecard())

        if self.teams[0].total_runs > self.teams[1].total_runs:
            print(f"{self.teams[0].name} won the match by {self.teams[0].total_runs - self.teams[1].total_runs} runs.")
        elif self.teams[1].total_runs > self.teams[0].total_runs:
            print(f"{self.teams[1].name} won the match by {self.teams[1].total_runs - self.teams[0].total_runs} runs.")
        else:
            print(f"The match is a tie.")

    def print_final_score(self):
        self.determine_winner()


class Match:
    def __init__(self, team1_name, team1_players, team2_name, team2_players, overs):
        self.team1 = Team(team1_name, team1_players)
        self.team2 = Team(team2_name, team2_players)

        self.scoreboard = Scoreboard(self.team1, self.team2, overs)

    def start(self, team1_balls, team2_balls):
        self.scoreboard.play_match(team1_balls)
        self.scoreboard.switch_team()
        self.scoreboard.play_match(team2_balls)

        self.scoreboard.print_final_score()


match = Match("Team 1", ["P1", "P2", "P3", "P4", "P5"], "Team 2", ["P6", "P7", "P8", "P9", "P10"], 2)
match.start(["1", "1", "1", "1", "1", "2", "W", "4", "4", "Wd", "W", "1", "6"], ["4", "6", "W", "W", "1", "1", "6", "1", "W", "W"])
