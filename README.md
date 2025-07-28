# Automation Test Project & Date Formatting Tool

This project contains two main tasks:

Task 1: Web form automation using Playwright (including simulated reCAPTCHA interaction) and installation of windows application

Task 2: Flexible date formatting utility using Python

## Project Structure
```bash
.
├── helper/
├── installer/
│   ├── Carbonite-personal-client.exe
├── tests/
│   ├── __init__.py
│   ├── test_signUp_page_installer.py   # Task 1
│   └── test_install_application.py     # Task 1
├── task2/
│   └── date_formatter.py               # Task 2
├── pageObjects/
│   ├── __init__.py
│   └── SignupPage.py                   # Page Object Model (Task 1)
├── utils/
│   ├── fixture.py
├── requirements.txt
├── pytest.ini
├── TestCase.xlsx
└── README.md
```

## Setup Instructions

### Step 1: Create Virtual Environment
Make sure you have Python 3.8+ installed.

```bash
python -m venv venv
venv\Scripts\activate   # Linux: source venv/bin/activate
```

### Step 2: Install Requirements
```bash
pip install -r requirements.txt
```

## Task 1: Web Form Automation Using Playwright-pytest & Windows Installer Test
- Description
    - Automates a signup form at Carbonite Trial page.
    - Uses Playwright to fill out the form.
    - Simulates CAPTCHA token injection to bypass UI-only validation.
    - Installer automation uses Pywinauto to open .exe and click buttons.

### 1. Run Task 1 Test Cases
```bash
pytest tests/test_signUp_page_installer.py
pytest tests/test_install_application.py
```

### 2. Test Case List (Task 1)
- Added the file TestCase.xlsx in the project with all the valid scenario's
- Open signup form page and check title contains "Carbonite"
- Accept cookie banner
- Fill:
    - Email
    - Confirm Email
    - Password
    - Confirm Password
    - Country dropdown
    - Inject dummy reCAPTCHA token and click the checkbox (simulated)
    - Submit the form

### 3. Limitations
#### 3.1 reCAPTCHA
- Cannot be automated legally/technically.
- Workaround: Injecting dummy token assumes front-end validation only.
- Won't work with server-side CAPTCHA verification.
- Hence Not working right now

#### 3.2 Windows Installer Automation
- Fails without admin rights due to CreateProcess elevation.
- If GUI windows don’t load or run silently in the background, Pywinauto can’t hook into them.
- Need admin permissions and a visible GUI process to automate reliably.

##  Task 2: Flexible Date Formatter
- Description
    - Accepts user input date in any common format
    - Accepts a target format like %m/%d/%Y
    - Converts date accordingly
    - Handles invalid inputs & formats

### 1. Run Task 2
```bash
python task2/date_formatter.py
```

### 2. Edge Cases Handled
- Empty input
- Incorrect/ambiguous date formats
- Leap year and non-leap year edge cases
- Locale-specific formats (if required)
- Invalid output format directives

## Requirement.txt example
```bash
playwright==1.43.0
pywinauto==0.6.8
dateutil==2.8.2
python-dateutil==2.8.2
pytest==7.4.2
```

## Author
Himanshu Rathee

July 2025