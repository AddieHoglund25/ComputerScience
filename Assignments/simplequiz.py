#simple quiz assignment - create a quiz that tallies your score at the end

answer_one = input ("What is the best color?\n>")

answer_two = input ("What is the best animal?\n>")

answer_three = input ("What is the best movie?\n>")

answer_four = input ("What is the worst color?\n>")

answer_five = input("What is the best food?\n>")


def tally_score():
    score = 0

    if answer_one.lower() == "blue":
        score = score + 1
  
    if answer_two.lower() == "dog":
        score = score + 1

    if answer_three.lower() == "dunkirk":
        score = score + 1
   
    if answer_four.lower() == "yellow":
        score = score + 1

    if answer_five.lower() == "pasta":
        score = score + 1

    print(score)

tally_score()