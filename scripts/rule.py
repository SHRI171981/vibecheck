def validate_text(context):
    output = {
        "feedback": "",
        "sentiment": "",
        "score": 0,
        "context" : context
    }
    MIN_LENGTH = 10
    MAX_LENGTH = 50
    cuss_words = ['asshole','cunt','fucker','fuck','mf','bitch','motherfucker']
    context = context.lower()
    context = context.strip()
    context = context.split() 
    num_words = len(context)
    if num_words < MIN_LENGTH:
        output["feedback"] = f"length is too small: {num_words}"
        return False, output
    if num_words > MAX_LENGTH:
        output["feedback"] = f"Length is too large: {num_words}"
        return False , output
    for word in cuss_words:
        if word in context:
            output["feedback"] = F"This should not be there: {word}"
            return False , output
    return True , output
        
# sen = "     i dont wanna die tonight but the moon looks like the bitch im looking         "
sen = "a s c"
# print(sen)
if __name__ == "__main__":
    validate_text(sen)
    report = validate_text(sen)
    print(report)

# print("Hello World")