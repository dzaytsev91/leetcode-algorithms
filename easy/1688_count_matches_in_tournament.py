class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        if n < 2:
            return total_matches

        teams = n
        while True:

            teams, matches = self.play(teams)
            total_matches += matches

            if teams == 1:
                return int(total_matches)

    def play(self, teams: int):
        if teams % 2 == 0:
            return teams / 2, teams / 2
        return ((teams - 1) / 2) + 1, (teams - 1) / 2
