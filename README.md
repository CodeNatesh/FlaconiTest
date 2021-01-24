# FlaconiTest

Steps to be followed to execute the Automation scripts

1. Add the chrome driver in the /usr/bin/ folder in mac or put the file in some location in windows
2. install the pytest-html package for the reporting
3. go to termainl and change the directory to project directory
4. Enter command in teminal "pytest  -m ui_test ui_tests/workflows/test_cases_flaconi.py --html=report.html"
5. Check the Reports.html file for the reports and logs