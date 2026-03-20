class Question:
    """
    A class to represent a multiple-choice question.
    """

    def __init__(self, text, options, answer):
        self.text = text            # Question text
        self.options = options      # List of options (A, B, C, D)
        self.answer = answer        # Correct answer

    def is_correct(self, choice):
        """
        Check if the selected answer is correct
        """
        if choice is None:
            return False
        return choice.strip().lower() == self.answer.strip().lower()