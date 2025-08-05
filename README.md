# Luhn Validator
A simple python library and CLI to validate numbers using the Luhn algorithm (used in credit card numbers, IMEIs, etc.).

### Usage
You can install the package in editable mode (for development)
* Navigate to your luhn-validator/ folder
* (Optional but recomended) Set up a virtual environment:
>python -m venv venv

>.\venv\Scripts\actiivate # on Windows

>source /venv/bin/activate # on Linux
* Run to Install:
>pip install -e .
* After installing, run:
>luhn-validator 1234567812345670
* You can also use it as a library:
>from luhn.luhn import is_luhn

### License
MIT License -- free to use, modify, and distribute.

### Author
Agriana
GitHub: @Agri99
