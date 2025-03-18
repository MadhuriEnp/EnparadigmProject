@pathpage
Feature: simulation path page validation

#Background: Login
#    Given User opens login page
#    When user enters user name and clicks on continue button
#    And user enters password and clicks on login button
#    Then user should able to see home page

  @LearnerProfile
  Scenario: Verify the functionality of creating user for that user completing the learner course
    Given User opens admin login page
    When user clicks on sign in with google button and enters valid user credentials
    Then user should able to see catalyx admin homepage
    When user clicks on cohort management and create user
    And user selects cohort and company for creating learner user
    And user enters valid details for the learning profile
#    Then user should able to see success popup of user creation
    When user clicks on Post Rollout
    And user clicks on Usermanagement
    And user verifies the details of user name and email
    Then user clicks on MagicLink and clicks on copy magic Link
    Then user should able to see home page of learner profile
    When user clicks on talenthub button and verifies the values in different pages like performance, Action Item, Progress, Social,Resources, Achievements
    And user clicks on learningPath and selcts the course and started the course
    When user clicks on talenthub button and verifies the values in different pages like performance, Action Item, Progress, Social,Resources, Achievements





#@Test1234
#  Scenario: tc000 Testing
#  Given User opens login page
#    When user enters user name and clicks on continue button
#    And user enters password and clicks on login button
#  Then user goes to another url

Scenario: Tc001 Validating the path page navigation
     Given User opens login page
    When user enters user name and clicks on continue button
    And user enters password and clicks on login button
    Then user should able to see home page
     When user clicks on sim1 resume button
     Then user should able to see the sim1 heading
     When user clicks on resume button in simulation1 page
     Then user should able to see the A Missed Promotion
#     When user clicks on sim2 resume button
#     Then user should able to see the sim2 heading


