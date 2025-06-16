import time 

def introduction():
	print("WELCOME TO QUIZ CHALLENGE ")
	PRINT("LET ME KNOW YOUR IQ")
	time.sleep(1)#it is used to stop the program for 1second and it is the in predefined module time
	
quiz_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Andhrapradesh", "B) Telangana", "C) Newdelhi", "D) Chattisgarh"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
        "answer": "B"
    }
]
def running_quiz():
	score=0
	question_num=1
	for question in quiz_questions:	
		print("\nQuestions",question_number,":",question["questions"])
	for option in question["options"]:
		print(option)
	 user_answer = input("Choose answer (A, B, C, D): ").strip().upper()
	if user_answer == question["answer"]:
            print("Correct!")
            score += 1	
	 else:
            print("Wrong! The correct option is", question["answer"])
 print("*****\n Quiz Over! \n*****")
	 if score == len(quiz_questions):
        print("Great job! You got a perfect score!")
    elif score >= 2:
        print("Nice work! Keep practicing.")
    else:
        print("Try again! Better luck next time")
        