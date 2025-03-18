@login @simpath
Feature: New User Flow feature

Background: Login
    Given User opens login page
    When user enters user name and clicks on continue button
    And user enters password and clicks on login button
    Then user should able to see home page

  @1
Scenario: Tc001 New user flow home page validation

    When user clicks on filter button in homepage
    Then user should able to see different filter options
    When user clicks on sort button in homepage
    Then user should able to see different sort options


@Filtertest
Scenario: Tc002 Checking the functionality of Filter button
     When user clicks on filter button in homepage
     And clicks on NotStarted button
#     Then user should able to see Start button
#     When user clicks on filter button in homepage
     And clicks on Inprogress button
#     And user clicks on filter button in homepage
     And clicks on Completed button
     Then user should able to see Resume button

@SortTest
 Scenario: Tc003 Checking the functionality of Sort button
      When user clicks on sort button in homepage
      And clicks on Recently Started button
#      Then user should able to see Enter Path button
      Then user should able to see Resume button
      When user clicks on sort button in homepage
      When user clicks on A-Z button in homepage
      Then user should able to see Resume button
      When user clicks on sort button in homepage
      And clicks on Z-A button
      Then user should able to see Resume button



