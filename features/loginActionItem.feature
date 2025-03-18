@smoke1 @simpath @loginActionItem
Feature: Example feature

Scenario Outline: <Tc> Validating the login page with invalid usernames
    Given User opens login page
    When user enters "<username>" and clicks on continue button
    Then user should able to see username error message

     Examples:
      | Tc    | username  |
      | Tc001 | 123456    |
      | Tc002 | asdfg     |
      | Tc003 | @asdg!    |
      | Tc004 | 123@asdf  |

Scenario Outline: <Tc> Validating the login page with valid username and invalid password
    Given User opens login page
    When user enters user name and clicks on continue button
    And user enters "<password>" and clicks on login button
    Then user should able to see password error message

    Examples:
      | Tc    | password  |
      | Tc005 | 123456    |
      | Tc006 | asdfg     |
      | Tc007 | @asdg!    |
      | Tc008 | 123@asdf  |

  @9
Scenario: Tc009 Enparadigm Action Item page
    Given User opens login page
    When user enters user name and clicks on continue button
     And user enters password and clicks on login button
    Then user should able to see home page
    When user clicks on talenthub button and clicks on Action itom button
    Then user should able to see action page button
    When user clicks on filter button
    Then user should able to see all,pending,completed buttons
    When user clicks on sort button
    Then user should able to see latest first and oldest first buttons



