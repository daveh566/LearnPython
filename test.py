from question import question
question_prompts = [
    "What color are oranges\n (a)Red\n (b)Green\n (c)Yellow\n\n",
    "What color are strawberries\n (a)Red\n (b)Blue\n (c)Mango\n\n",
    "What color are bananas\n (a)Blue\n (b)Yellow\n (c)Yellow\n\n",
    "What color is the blackboard\n (a)Black\n (b)Yellow\n (c)Blue\n\n"
]
questions = [
    question(question_prompts[0], "c"),
    question(question_prompts[1], "a"),
    question(question_prompts[2], "b"),
    question(question_prompts[3], "a")

]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You scored " +str(score)+ "/" + str(len(questions)))
run_test(questions)
