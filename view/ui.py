def get_string(question, max_length=None):#checking empty string
    while True:
        response = input(f'{question}:')
        if response:
            return response
        print("please enter game title. Empty not allowed")
