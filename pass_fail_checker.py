# Get user input
score = int(input("Enter your test score (0-100): "))

# Validate input
if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100")
else:
    # Check if passing or failing
    if score >= 75:
        print("Result: Safe ")
    else:
        print("Result: Mag impake kana kay baka mapalayas ka ")
