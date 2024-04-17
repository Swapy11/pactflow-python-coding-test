from src.pypacter import detect_language


def test_detect_language_valid_code():
    snippet = 'List<String> things = new ArrayList<>();'
    language = detect_language(snippet)
    assert language == "Java"

def test_detect_language_invalid_code():
    snippet = 'console.log("Hello world");'
    language = detect_language(snippet)
    assert language == "JavaScript"

def test_detect_language_empty_code():
    snippet = ''
    language = detect_language(snippet)
    assert language == "Unknown"

def test_detect_language_exception():
    with pytest.raises(Exception):
        snippet = 'invalid_code'
        detect_language(snippet)

# Add more test cases as needed

if __name__ == "__main__":
    pytest.main()