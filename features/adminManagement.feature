@catalyxAdmin @simpath @adminManagement
Feature: Admin Management feature

Background: Validating enparadigm admin login page
    Given User navigates to admin login page
    When user clicks on signin with google button and enters valid user credentials
    Then user should able to see the catalyx admin homepage
#
##    1
#    @CreatingAdmin
#Scenario: Tc001 Creating the admin
#    When user clicks on admin management
#    And user clicks on create admin
#    Then user should able to see the create admin
#    When user enters all the user details and clicks on create user button
#    Then User should able to see the successfull message of creating user
#
##        2,3,4
        @EmptyValuesCreatingAdmin
    Scenario Outline: <Tc> Creating the admin with providing empty data and verifying the error messages
    When user clicks on admin management
    And user clicks on create admin
    Then user should able to see the create admin
    When user enters the user details like "<name>", "<username>", "<password>"  empty one at a time
    Then user able to see the respective error messages
    Examples:
    | Tc    | name    | username          | password |
    | Tc002 |   ""    | madhuri@gmail.com | madhuri  |
    | Tc003 | Madhuri |        ""         | madhuri  |
    | Tc004 | Madhuri | madhuri@gmail.com |   ""     |
#
##            5
     @WithoutRoleCreatingAdmin
    Scenario: Tc005 Creating the admin without role and verifying the error messages
    When user clicks on admin management
    And user clicks on create admin
    Then user should able to see the create admin
    When user enters the user details without selecting role
    Then user able to see the respective error messages
#
##         6,7,8,9
    @InvalidUsername
    Scenario Outline: <Tc> Creating the admin with invalid username verifying the error messages
     When user clicks on admin management
    And user clicks on create admin
    Then user should able to see the create admin
    When user enters the creating user details with "<invalidUsername>" invalid username
    Then user able to see the respective error messages
     Examples:
       | Tc    | invalidUsername  |
       | Tc006 | 123456           |
       | Tc007 | asdfg@           |
       | Tc008 | @asdg!           |
       | Tc009 | user             |
#
##        10
#@CreatingClientAdmin
#Scenario: Tc010 Creating the client admin
#    When user clicks on admin management
#    And user clicks on create admin
#    Then user should able to see the create admin
#    When user enters all the client admin user details and clicks on create button
#    Then User should able to see the successfull message of creating user

##11
##    @updateAdmin
##Scenario: Updating the admin(Not totally implemented)
##    When user clicks on admin management
##    And user clicks on update admin
##    Then user should able to see the update admin page
##    When user enters all the update admin user details and clicks on update admin button
##    Then User should able to see the successfull message of updating admin user
#
#
#
#
#
#
#
