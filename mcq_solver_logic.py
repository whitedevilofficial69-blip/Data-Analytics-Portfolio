import re

def solve_mcq(question, context_text, options):
    print(f"Question: {question}")
    
    # Simple logic: Check which option appears in the context text
    best_guess = None
    for option in options:
        # Using regex to find exact word matches
        if re.search(r'\b' + re.escape(option) + r'\b', context_text, re.IGNORECASE):
            best_guess = option
            break
            
    if best_guess:
        return f"Predicted Answer: {best_guess}"
    else:
        return "Answer not found in context."

# Test the app
context = "Python is a high-level programming language created by Guido van Rossum."
q = "Who created Python?"
opts = ["Elon Musk", "Guido van Rossum", "Bill Gates", "Steve Jobs"]

print(solve_mcq(q, context, opts))
