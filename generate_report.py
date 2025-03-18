import os
from datetime import datetime
import sys
import pytest
from behave.__main__ import main as behave_main
import os
import shutil
from behave.__main__ import main as behave_main


#Define the directory for reports
report_dir = os.path.join(os.getcwd(), "reports")

# Ensure the report directory exists
if not os.path.exists(report_dir):
    os.makedirs(report_dir)

# Generate a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Define the report file name with timestamp
report_file = os.path.join(report_dir, f"report_{timestamp}.html")
allure_report_dir = os.path.join(os.getcwd(), 'reports', 'allure')
# os.system("allure generate reports/allure -o reports/allure-report --clean")
# os.system("allure open reports/allure-report")

# Run behave with the html formatter
sys.argv = [
        'behave',
        '-f', 'behave_html_formatter:HTMLFormatter',
        '-o', report_file,
        '-f', 'allure_behave.formatter:AllureFormatter',
        '-o', allure_report_dir,
        '--no-capture',
    ]

behave_main()

  




