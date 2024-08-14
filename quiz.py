# quiz.py

import time
from questions import questions

def start_quiz():
    score = 0
    start_time = time.time()
    answered_questions = []
    total_questions = len(questions)
    
    while len(answered_questions) < total_questions:
        for acronym, meaning in questions.items():
            if acronym in answered_questions:
                continue
            
            print(f"What does {acronym} stand for?")
            answer = input("Your answer: ").strip()
            
            if answer.lower() == meaning.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {meaning}")
            
            answered_questions.append(acronym)
            
            # Show current score and elapsed time
            elapsed_time = time.time() - start_time
            print(f"Score: {score}/{len(answered_questions)}")
            print(f"Time elapsed: {int(elapsed_time)} seconds\n")
            
            # Ask if the user wants to go back to any previous question
            if len(answered_questions) < total_questions:
                go_back = input("Do you want to go back to any question? (yes/no): ").strip().lower()
                if go_back == "yes":
                    answered_questions.remove(acronym)
                    continue
            
    print(f"\nQuiz completed! Your final score is {score}/{total_questions}")
    total_time = time.time() - start_time
    print(f"Total time taken: {int(total_time)} seconds")

if __name__ == "__main__":
    start_quiz()
