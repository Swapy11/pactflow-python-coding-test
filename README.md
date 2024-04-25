# PactFlow Python Coding Test
# Steps done to complete the assignment

### Task 1

1. Added utility function "read_input_content_from_file_or_string" to pypacter-cli/src/pypacter_cli/util.py file. 
- This function returns the file content if filename is provided as argument otherwise returns the input itself.
2. Added detect_language function to src/pypacter/language_detector.py file
- In this function called GPT_4.invoke(prompt) to invoke the gpt4 model and provided the input prompt to identify the programming language.
- Used already initialised GPT_4 instance in models.py file.
3. Added unit test cases in tests/test_language_detector.py file.
  

### Task 2

Added /detect-language api endpoint to pypacter-api/src/pypacter_api/base.py file.
- This api extract the input from request_body
- Calls the detect_language function from core package to get the output.
- Convert and returns the output in json using JSONResponse object


### Task 3

1. Added call_detect_language_api function to pypacter-cli/src/pypacter_cli/__init__.py file to api endpoint to get the output
2. Added process_input function to pypacter-cli/src/pypacter_cli/__init__.py file as cli command to take input from user and process the input and returns the output to cli.
3. Added the requirements.txt file.
