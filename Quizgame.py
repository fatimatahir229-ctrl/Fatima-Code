import pandas as pd

class QuizGame:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)
        self.players = {}
        self.current_player = None

    def display_welcome(self):
        print("\nWELCOME TO THE GK QUIZ")
        print("\nRULES OF THE GAME:")
        print("1 The same person cannot join twice.")
        print("2 One wrong answer — game over for that player.")

    def get_player_name(self):
        while True:
            name = input("Enter your name: ").strip()
            if not name:
                print("Please enter a valid name.")
                continue
            if name in self.players:
                print(f"Sorry {name}, you have already played.")
                print("Please use a different name.")
                continue
            return name

    def run_quiz(self):
        self.display_welcome()

        while True:
            player_name = self.get_player_name()
            self.current_player = player_name
            self.players[player_name] = 0

            print(f"\nHey {player_name}, let's play!")

            score = self.ask_questions()

            if score > 0:
                print(f"\n🎉 Congratulations {player_name}, well played!")
                print(f"Your score is {score}/{len(self.df)}")
            else:
                print(f"\nSorry {player_name}, better luck next time!")

            play_again = input("\nWould another player like to play? (yes/no): ").strip().lower()
            if play_again not in ["y", "yes"]:
                break

        self.display_final_results()

    def ask_questions(self):
        score = 0
        for index, row in self.df.iterrows():
            question_no = row["Question No."]
            question = row["Question"]
            options = [row["Option A"], row["Option B"], row["Option C"], row["Option D"]]
            correct_answer = row["Correct Answer"]

            print(f"\nQ{question_no}: {question}")
            for opt in options:
                print(opt)

            while True:
                user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
                if user_answer in ["A", "B", "C", "D"]:
                    break
                print("Invalid input. Please enter A, B, C, or D.")

            if user_answer == correct_answer.upper():
                score += 1
                self.players[self.current_player] = score
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
                return score

        return score

    def display_final_results(self):
        print("\nFinal Results")

        if not self.players:
            print("No players participated.")
            return

        results_df = pd.DataFrame({
            "Player": list(self.players.keys()),
            "Score": list(self.players.values())
        })

        results_df["Total Questions"] = len(self.df)
        results_df["Percentage"] = (results_df["Score"] / len(self.df) * 100).round(1)

        print("\n", results_df.to_string(index=False))

        file_name = "Quiz_Results.xlsx"


        try:
            old_df = pd.read_excel(file_name)
            final_df = pd.concat([old_df, results_df], ignore_index=True)
        except FileNotFoundError:
            final_df = results_df


        final_df.to_excel(file_name, index=False)
        print(f"\n Results have been saved to '{file_name}'")

if __name__ == "__main__":
    game = QuizGame("General_Knowledge_Quiz.xlsx")
    game.run_quiz()
