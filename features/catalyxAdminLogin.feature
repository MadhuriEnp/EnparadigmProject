@catalyxAdmin @simpath
Feature: Admin Login feature

#Background: Validating enparadigm admin login page
#    Given User opens admin login page
#    When user clicks on sign in with google button and enters valid user credentials
#    Then user should able to see catalyx admin homepage


 Scenario Outline: <Tc> Validating the admin login page with invalid usernames
     Given User opens admin login page
     When user enters the invalid "<username>" and clicks on continue button
     Then user should be in the signin page

      Examples:
       | Tc    | username  |
       | Tc001 | 123456    |
       | Tc002 | asdfg     |
       | Tc003 | @asdg!    |
       | Tc004 | 123@asdf  |

 Scenario Outline: <Tc> Validating the login page with valid username and invalid password
     Given User opens admin login page
     When user enters valid username and invalid "<password>" and clicks on login button
     Then user should be in the signin page

     Examples:
       | Tc    | password  |
       | Tc005 | 123456    |
       | Tc006 | asdfg     |
       | Tc007 | @asdg!    |
       | Tc008 | 123@asdf  |

 Scenario: Tc009 Validating enparadigm admin login page
     Given User opens admin login page
     When user clicks on sign in with google button and enters valid user credentials
     Then user should able to see catalyx admin homepage

 Scenario: Tc010 creating the company
    Given User opens admin login page
    When user clicks on sign in with google button and enters valid user credentials
    Then user should able to see catalyx admin homepage
    When user enters company details and clicks on crete company
    Then user should able to see successpopup

   @EmptyParametersCompany
   Scenario Outline: <Tc> Verify the functionality of creating company with empty parameters
     Given User opens admin login page
    When user clicks on sign in with google button and enters valid user credentials
    Then user should able to see catalyx admin homepage
    When user enters the empty details for "<compName>" , "<domainName>" and "<selIndus>" for the creating the company
     Then user should able to see respective error messsages for creating company
     Examples:
     | Tc    | compName | domainName | selIndus |
     | Tc011 | ""       | xyz.com    | role     |
     | Tc012 | Madhurii |  ""        | role     |
     | Tc013 | Madhurii | xyz.com    | emptry   |



 Scenario: Tc014 Creating the deal
    Given User opens admin login page
    When user clicks on sign in with google button and enters valid user credentials
    Then user should able to see catalyx admin homepage
     When user clicks on create deal
     And user needs to enter all the details in that particular page
     Then user should able to see success popup


     @EmptyParametersCreatingDeal
   Scenario Outline: <Tc> Verify the functionality of creating deal with empty parameters
      Given User opens admin login page
    When user clicks on sign in with google button and enters valid user credentials
    Then user should able to see catalyx admin homepage
     When user clicks on create deal
    When user enters the empty details for "<dealName>", "<selComp>", "<selSalesOwner>", "<selDeliOwner>" for the creating the deal
     Then user should able to see respective error messsages for creating deal
     Examples:
     | Tc    | dealName  | selComp | selSalesOwner |  selDeliOwner |
     | Tc015 | ""        | selectComp   | selectSales     |  selectDelOwn |
     | Tc016 | Madhuriii |  emptyComp        | selectSales    | selectDelOwn |
     | Tc017 | Madhuriii | selectComp    | emptrySales   | selectDelOwn      |
     | Tc018 | Madhuriii |   selectComp  | selectSales   |  emprtyDelOwn     |

       @CreatingCohort
 Scenario: Tc019 Creating the cohort
     Given User opens admin login page
    When user clicks on sign in with google button and enters valid user credentials
    Then user should able to see catalyx admin homepage
     When user clicks on cohort management
     And user clicks on create catalyx cohort and enters valida details
     Then user should able to see of cohortsuccesspopup

         @CreatingCohortEmptyParameters
   Scenario Outline: <Tc> Verify the functionality of creating cohort with empty parameters
 Given User opens admin login page
    When user clicks on sign in with google button and enters valid user credentials
    Then user should able to see catalyx admin homepage
     When user clicks on cohort management
     And user clicks on create catalyx cohort and enters empty details for "<cohortName>", "<company>", "<deal>", "<hrname>", "<hremail>", "<startDate>", "<deadline>", "<deliveryOwner>", "<learningPath>"
     Then user should able to see respective error message for creating cohort
     Examples:
     | Tc    | cohortName | company    | deal        | hrname | hremail         | startDate    | deadline    | deliveryOwner | learningPath |
     | Tc020 | ""         | selectComp | selectDeal  | sammy  | sammy@gmail.com | selStartDate | selDeadline | selDelOwner   | selLearnPath |
     | Tc021 | Test       | emptyComp  | selectDeal  | sammy  | sammy@gmail.com | selStartDate | selDeadline | selDelOwner   | selLearnPath |
     | Tc022 | Test       | selectComp | emptyDeal   | sammy  | sammy@gmail.com | selStartDate | selDeadline | selDelOwner   | selLearnPath |
     | Tc023 | Test       | selectComp | selectDeal  | ""     | sammy@gmail.com | selStartDate | selDeadline | selDelOwner   | selLearnPath |
     | Tc024 | Test       | selectComp | selectDeal  | sammy  | ""              | selStartDate | selDeadline | selDelOwner   | selLearnPath |
     | Tc025 | Test       | selectComp | selectDeal  | sammy  | sammy@gmail.com | empStartDate | selDeadline | selDelOwner   | selLearnPath |
     | Tc026 | Test       | selectComp | selectDeal  | sammy  | sammy@gmail.com | selStartDate | empDeadline | selDelOwner   | selLearnPath |
     | Tc027 | Test       | selectComp | selectDeal  | sammy  | sammy@gmail.com | selStartDate | selDeadline | empDelOwner   | selLearnPath |
     | Tc028 | Test       | selectComp | selectDeal  | sammy  | sammy@gmail.com | selStartDate | selDeadline | selDelOwner   | empLearnPath |
     | Tc029 | TestMadhu  | selectComp | selectDeal  | sammy  | sammy@gmail.com | selStartDate | selDeadline | selDelOwner   | selLearnPath |

  @CreatingCohortInvalidHREmail
    Scenario Outline: <Tc> Verify the functionality of creating cohort with invalid hr email
      Given User opens admin login page
      When user clicks on sign in with google button and enters valid user credentials
      Then user should able to see catalyx admin homepage
      When user clicks on cohort management
      And user clicks on create catalyx cohort and enters the invalid hr email "<InvalidEmail>"
      Then user should able to see respective error message for creating cohort
    Examples:
    | Tc    | InvalidEmail |
#    | Tc030 | 12345        |
#    | Tc031 | saadgf       |
#    | Tc032 | jfhdj@gmail  |
    | Tc033 | dfhj.com     |

@CreateUser
 Scenario: Tc034 Creating the user
      Given User opens admin login page
      When user clicks on sign in with google button and enters valid user credentials
      Then user should able to see catalyx admin homepage
      When user clicks on cohort management and create user
      And user selects cohort and company
      And user enters valid details
      Then user should able to see success popup of user creation

  @CreatingUserEmptyParameters
    Scenario Outline: <Tc> Verify the functionality of creating user with empty parameters and invalid username
      Given User opens admin login page
      When user clicks on sign in with google button and enters valid user credentials
      Then user should able to see catalyx admin homepage
      When user clicks on cohort management and create user
      And user selects cohort and company
      And user enters valid details with empty parameters for "<name>" and "<username>"
      Then user should able to see respective error message for creating user
    Examples:
    | Tc    | name | username         |
    | Tc035 | ""   | tester@gmail.com |
    | Tc036 | test | ""               |
    | Tc037 | test | 12222222222      |
    | Tc038 | test | adsfgghg         |
    | Tc039 | test | test@gmal        |
    | Tc040 | test | test.com         |

    @withoutCompanyCohortCreatingUser
      Scenario: Tc041 Creating the user without company and cohort
      Given User opens admin login page
      When user clicks on sign in with google button and enters valid user credentials
      Then user should able to see catalyx admin homepage
      When user clicks on cohort management and create user
      And user enters valid details
      Then user should able to see respective error message for creating user


      @copyingMagicLink
 Scenario: Tc042 Copying the magic Link
     Given User opens admin login page
    When user clicks on sign in with google button and enters valid user credentials
    Then user should able to see catalyx admin homepage
     When user clicks on Post Rollout
     And user clicks on Usermanagement
#              And user selects cohort and company
     Then user clicks on MagicLink and clicks on copy magic Link


