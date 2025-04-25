import re
def tokenizer(text):
    punctuation_pattern=r"[।|!?,.:\'\";()]"
    date_pattern=r"\b\d{2}-\d{2}-\d{4}\b"
    url_pattern=r"https?://[^\s]+"
    username_pattern=r"@\w+\b"
    email_pattern=r"[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    number_pattern=r"\b(\d+\.\d+|\d+/\d+/\d+|\d{1,3}(,\d{2,3})+)\b"
    # combined_pattern=f"{punctuation_pattern}|{date_pattern}|{url_pattern}|{username_pattern}|{email_pattern}|{number_pattern}"

    combined_pattern = f"({url_pattern})|({email_pattern})|({date_pattern})|({username_pattern})|({number_pattern})|({punctuation_pattern})"

    results=re.findall(combined_pattern,text)

    return results


text="यह @username, email@example.com, और एक तारीख 01-01-2021 के साथ एक नमूना पाठ है। संख्याएँ जैसे 33.15, 3,22,243, 313/77।"

result=tokenizer(text)
print(result)