# Enparadigm Project

## Project Overview

Enparadigm is a leading learning and development company that specializes in experiential, technology-driven training solutions. It focuses on enhancing leadership, business acumen, sales effectiveness, and decision-making skills through simulations and gamified learning. Known for its customized programs, Enparadigm caters to various industries, empowering teams from senior management to frontline employees. With a mission to bridge the gap between theory and practice, it delivers impactful, result-oriented training aligned with organizational goals.


## Key Features

1. Experiential Learning: Their programs focus on "learning by doing" using simulations, case studies, and real-world scenarios to enhance retention and application.
2. Customized Solutions: They design tailored training modules based on the specific needs of organizations and their teams, ensuring relevance and alignment with business goals.
3. Technology Integration: They use state-of-the-art tools and digital platforms to facilitate immersive and interactive learning experiences.
## Getting Started with Installation

This guide will help you set up the Enparadigm project on your local system for development and testing.

### Prerequisites

Before starting, ensure you have:

- **Python (3.8 or Higher)**: Required for running the software.
- **Java (11 or Higher)**: Essential for setting up Jenkins.
- **Node.js and npm**: Needed for Playwright testing.
- **Jenkins**: Used for automating tests and managing deployments.

> **Note**: Install `allure`, `behave`, `pytest`, and `playwright` as these tools will be required for testing and report generation.
pip install playwright
playwright install
pip install behave
pip install pytest pytest-playwright
pip install behave-html-formatter
pip install allure-behave

### Step-by-Step Installation Guide

1. **Clone the Repository**
   Clone the project to your system:
  
2. **Set Up a Virtual Environment**
   A virtual environment helps manage dependencies:
   ```bash
   python3 -m venv env
   # For Windows, use:
   For creating venv file : python -m venv venv
   For Activating the scripts : venv\Scripts\activate
   ```

3. **Install Required Packages**
   Install all necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Playwright Setup**
   For end-to-end testing, install Playwright along with required browsers:
   ```bash
   playwright install
   ```

## Configuration Details

To ensure proper functionality, certain configurations are required.



### Jenkins Configuration

Jenkins is an open-source automation server used to automate various stages of software development, such as Continuous Integration (CI) and Continuous Delivery (CD). Here’s a setup guide for using Jenkins with Enparadigm:

#### Key Benefits of Jenkins

- **Automation**: Reduces manual effort and errors by automating repetitive tasks.
- **Continuous Integration**: Ensures code quality by automatically building and testing changes.
- **Continuous Delivery**: Streamlines the release process with automated deployment.
- **Flexibility and Extensibility**: Integrates with various tools and supports many plugins.

#### Setting Up Jenkins

1. **Java Development Kit (JDK)**: Ensure JDK 8 or later is installed.
2. **System Administrator Privileges**: Required for installation and configuration.

#### Installation Methods

- **WAR File**: Download from the [Jenkins site](https://www.jenkins.io/doc/book/installing/war-file/) and run with `java -jar jenkins.war`.
- **System Service**: Download the installer and follow on-screen instructions.

#### Initial Setup

1. **Unlock Jenkins**: Locate the initial password in the Jenkins home directory.
2. **Install Suggested Plugins**: Install default or required plugins.
3. **Admin Account**: Set up an admin account for secure management.

#### Configuration Steps

1. **Global Configuration**: Accessed via Manage Jenkins > Configure System.
2. **Email Notifications**: Configure for build status alerts.
3. **Manage Plugins**: Install plugins needed for SCM, build, test, and deployment.

#### Creating and Running Jobs

1. **New Job**: Go to New Item, choose the job type (e.g., Freestyle, Pipeline).
2. **Source Code Management**: Connect to Git or other version control systems.
3. **Build Steps**: Add steps, like executing scripts or commands.
4. **Post-Build Actions**: Configure actions, such as publishing reports.

#### Example: Python Playwright Job

1. **Login**: Log in to Jenkins.
2. **Create Item**: Select "New Item" and define a name and type (e.g., Freestyle).
3. **Configure Source Code**: Select Git if applicable.
4. **Add Build Steps**: For Python projects, add commands in "Execute Windows Batch Command."
5. **Post-Build Actions**: Add actions like "Publish HTML Reports" for test results.

> **Note**: Ensure necessary plugins are installed for SCM, reporting, and notifications.

## Running the Project

With everything set up, use these commands to perform tests and view reports.

### Running Tests

1. **Unit Tests**: Located in `tests/unit`, run with:
   ```bash
   pytest tests/unit
   ```

2. **Behavior-Driven Tests**: BDD tests are in `tests/bdd` and can be run with:
   ```bash
   behave tests/bdd
   ```

3. **End-to-End Tests**: Managed by Playwright; run them with:
   ```bash
   playwright test
   ```

### Viewing Reports with Allure

Allure generates detailed reports from test results. To view them:
*Before generating the report we have to install the allure
pip install behave-html-formatter
pip install allure-behave
1. Run the following to create a report:
   behave -f allure_behave.formatter:AllureFormatter -o allure-results -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html
   ```
2. Open the report with:
   allure open reports/allure-report
   ```

## Directory Structure

Understanding the main directories will help you navigate the project:

```
.
├── src                     # Main application code for Enparadigm
├── tests
│   ├── unit                # Unit tests
│   ├── bdd                 # Behavior-driven development tests
│   └── e2e                 # End-to-End tests
├── reports                 # Allure-generated test reports
└── docs                    # Documentation for the project
```

## Contribution Guidelines

We encourage contributions to the project! Follow these guidelines to keep the code clean and organized:

- **Code Style**: Follow PEP 8 standards.
- **Branching Strategy**: Use `feature/` for new features, `bugfix/` for bug fixes, and `hotfix/` for urgent issues.
- **Documentation**: Ensure new code is well-documented.
- **Testing**: Write tests for any new code and check that all tests pass before submitting a pull request.
- **Pull Requests**: Clearly describe the purpose of your pull request, referencing any related issues.

## Troubleshooting Common Issues

1. **Dependency Issues**: Make sure all packages in `requirements.txt` are correctly installed.
2. **Database Connection**: Verify that `DATABASE_URL` is correct and accessible.
3. **Playwright Issues**: If browsers aren’t found, re-run `playwright install`.

## Contact and Support

If you have questions or need help, please reach out:

- **Email**: support@enparadigm.com
- **Website**: [Enparadigm](https://simulation-test.catalyx.live/catalyx/adminlogin.php)
