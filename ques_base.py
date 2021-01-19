class question_base:
    statement = None
    difficulty = None

    def problem_statement(self):
        return self.statement

    def problem_difficulty(self):
        return self.difficulty

    def difficulty_score(self):
        return self.difficulty ** 1.5
