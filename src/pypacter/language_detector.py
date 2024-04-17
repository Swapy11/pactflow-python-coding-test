from models import GPT_4

def detect_language(sample_code:str):
    """
    Detects the programming language of a given sample_code.

    Args:
        sample_code (str): The code snippet to analyze.

    Returns:
        str: The name of the detected programming language.
    """
    prompt = [
        ("system", "You are a helpful assistant that detects programming languages."),
        ("human", sample_code),
        ]

    # Detect the programming language
    detected_language = GPT_4.invoke(prompt)

    # Extract output
    language = detected_language.content.strip()


def main():
    """
    driver code to test detect_language function 
    """
    snippet1 = 'List<String> things = new ArrayList<>();'
    snippet2 = 'console.log("Hello world");'

    language1 = detect_programming_language(snippet1)
    language2 = detect_programming_language(snippet2)

    print(f"Snippet 1 is written in {language1}")
    print(f"Snippet 2 is written in {language2}")


if __name__ == "__main__":
    main()
