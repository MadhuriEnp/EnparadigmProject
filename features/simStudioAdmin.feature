@simStudioxAdmin @simpath
Feature: simstudio Admin Login feature

Background: Login functionality with valid credentials
Given user is in simstudio admin login page
When user clicks on sign in with google button and enters valid credentials
Then user should able to see simstudio dashboard page

  @simStudioAIModule
Scenario: Tc001 Ethos AI module positive flow

When user clicks on search button and enters details
And user clicks on selected AI coach play button
Then user should able to see selected aicoach heading page
When user clicks on next button and play's the simulation1,simulation2 and verifies all button in scenarios page
Then user should able to see completed round1 heading


@EmptyScenario1Respone
Scenario: Tc002 Ethos AI module without entering scenario1 response negative flow

When user clicks on search button and enters details
And user clicks on selected AI coach play button
Then user should able to see selected aicoach heading page
When user clicks on next button and play's the simulation1,simulation2 and does not enters the scenario1 reposnse
Then user should able to see submit button is still disabled


  @EmptyScenario2Respone
Scenario: Tc003 Ethos AI module without entering scenario2 response negative flow

When user clicks on search button and enters details
And user clicks on selected AI coach play button
Then user should able to see selected aicoach heading page
When user clicks on next button and play's the simulation1,simulation2 and does not enters the scenario2 response
Then user should able to see submit button is still disabled


    @randomInputScenario1Response @oct1
Scenario Outline: <Tc> Verify the Ethos AI module score for scenario1 response with random input
When user clicks on search button and enters details
And user clicks on selected AI coach play button
Then user should able to see selected aicoach heading page
When user clicks on next button and play's the simulation1,simulation2 and enters random "<response1>" in scenario1 response
Then user should able to validate the score
  Examples:
  | Tc    | response1 |
  | Tc004 | Thank you |
  | Tc005 | 123456    |
  | Tc006 | @#$%^&*(  |
  | Tc007 | 12@#$qasfh |
  | Tc008 | asdfghk    |


      @randomInputScenario2Response @oct1
Scenario Outline: <Tc> Verify the Ethos AI module score for scenario2 response with random input
When user clicks on search button and enters details
And user clicks on selected AI coach play button
Then user should able to see selected aicoach heading page
When user clicks on next button and play's the simulation1,simulation2 and enters random "<response2>" in scenario2 response
Then user should able to validate the score
  Examples:
  |Tc     | response2 |
  | Tc009 | Thank you |
  | Tc010 | 123456    |
  | Tc011 | @#$%^&*(  |
  | Tc012 | 12@#$qasfh |
  | Tc013 | asdfghk    |

#  @GettingUsername
#Scenario: Tc014 Getting username and verifying
#When user clicks on search button and enters details
#And user clicks on selected AI coach play button
#    And user fetches the username

  @VerifyingGameTypeTextFieldVerifications
  Scenario: Tc015 Verify the text field verifications in the game type while create the module
  When user clicks on create module
  Then user should able to see create module page
  When user fill the module details in the step one and clicks on save and next
  Then user should able to see module setup step two
  When user fill the module details in the step two and click on save and next
  Then user should able to see module content
  When user clicks on content and gametype
  Then user should able to verify all the fields and elements


    @VerifyingGameTypeVideoFieldVerifications
    Scenario: Tc016 Verify the text field verifications in the video game type while create the module
    When user clicks on create module
    Then user should able to see create module page
    When user fill the module details in the step one and clicks on save and next
    Then user should able to see module setup step two
    When user fill the module details in the step two and click on save and next
    Then user should able to see module content
    When user clicks on content and gametype
    Then user should able to verify all the fields and elements in the video


  @CreatingTextGameTypeModule
    Scenario:  Tc017 Creating the module with text game type
      When user clicks on create module
      Then user should able to see create module page
      When user fill the module details in the step one and clicks on save and next
      Then user should able to see module setup step two
      When user fill the module details in the step two and click on save and next
      Then user should able to see module content
      When user fill the details in step three clicks on pubhish it for testing
      Then user should able to see fourth step report
      When fill details in step four and clicks on save button
      Then user should able to see the text data saved successfully
      When user clicks on modules and searchs for the just created module and published it
      Then user should able to see published succesfully


  @CreatingVideoGameTypeModule
    Scenario:  Tc018 Creating the module with Video game type
      When user clicks on create module
      Then user should able to see create module page
      When user fill the module details in the step one and clicks on save and next
      Then user should able to see module setup step two
      When user fill the module details in the step two and click on save and next
      Then user should able to see module content
      When user fill the details for video game type in step three clicks on pubhish it for testing
      Then user should able to see fourth step report
      When fill details in step four and clicks on save button
      Then user should able to see the text data saved successfully
      When user clicks on modules and searchs for the just created module and published it
      Then user should able to see published succesfully



  @CreatingModuleAndPlayingIt
  Scenario: Tc019 Creating the module and trying to play it
    When user clicks on create module
    Then user should able to see create module page
    When user fill the module details in the step one and clicks on save and next
    Then user should able to see module setup step two
    When user fill the module details in the step two and click on save and next
    Then user should able to see module content
    When user fill the details in step three clicks on pubhish it for testing
    Then user should able to see fourth step report
    When fill details in step four and clicks on save button
    Then user should able to see the text data saved successfully
    When user clicks on modules and searchs for the just created module and published it
    Then user should able to see published succesfully
     Given User opens admin login page
     When user clicks on sign in with google button and enters valid user credentials in the already signedin account
     Then user should able to see catalyx admin homepage
    When user clicks on path management, create path and clicks on static and selects Path
    Then user should able to see edit path details page
    When user fills all the path details and click on save and next button
    Then user should able to see edit module details page
    When user fills all the module details and click on save and next button
    Then user should able to see add feedback questions page
    When user selects feedback questions and clicks on publish button
    Then user should able to see manage path sage and verifies the path
    When user clicks on cohort management1
    And user enters the cohort details and selects the learning path
    Then user should able to see of cohortsuccesspopup1
    When user clicks on cohort management and create user
#    When user clicks on create user
    And user selects cohort and company for creating learner user in gametype
    And user enters valid details for the learning profile
    When user clicks on Post Rollout
    And user clicks on Usermanagement
    And user verifies the details of user name and email
    Then user clicks on MagicLink and clicks on copy magic Link1
    Then user should able to see home page of learner profile1
    When user clicks on start and starts plays the game



  @NegativeModuleStep1Empty
    Scenario Outline:  <Tc> Creating the module with empty <Descp> and verifying the error message
      When user clicks on create module
      Then user should able to see create module page
      When user fill the module details in the step one with empty details like "<ModName>", "<ModHeading>", "<Description>", "<NeededTime>", "<gameType>" and "<colorPalette>" and clicks on save and next
      Then user should able to see respective error message for creating module
    Examples:
    | Tc     | ModName | ModHeading | Description | NeededTime    | gameType    | colorPalette | Descp                 |
    | Tc020  | ""      | Heading    | description | selNeedTime   | selgameType | selcolPal    | Module Name           |
    | Tc021  | Module1 | ""         | description | selNeedTime   | selgameType | selcolPal    | Module Heading        |
    | Tc022  | Module1 | Heading    | ""          | selNeedTime   | selgameType | selcolPal    | Module Description    |
    | Tc023  | Module1 | Heading    | description | empNeedTime   | selgameType | selcolPal    | Module Game type      |
    | Tc024  | Module1 | Heading    | description | selNeedTime   | empgameType | selcolPal    | Time Needed for Module|
    | Tc025  | Module1 | Heading    | description | selNeedTime   | selgameType | empcolPal    | Colour Palette        |

    @NegativeModuleStep2Empty
    Scenario: Tc026 Creating the module step 2 with empty parameters and verifying the error message
    When user clicks on create module
    Then user should able to see create module page
    When user fill the module details in the step one and clicks on save and next
    Then user should able to see module setup step two
      When user clicks on save and next button in creating module
      Then user should able to see respective error message for creating module

  @NegativeModuleStep3EmptySce1
    Scenario: Tc027 Creating the module step 3 with empty parameters and verifying the error message
    When user clicks on create module
    Then user should able to see create module page
    When user fill the module details in the step one and clicks on save and next
    Then user should able to see module setup step two
    When user fill the module details in the step two and click on save and next
    Then user should able to see module content
    When user clicks on publish module for testing button in creating module
    Then user should able to see respective error message in step3

@NegativeModuleStep2ContentTypeEmpty
    Scenario Outline:  <Tc> Creating the module with empty <Descp> and verifying the error message
    When user clicks on create module
    Then user should able to see create module page
    When user fill the module details in the step one and clicks on save and next
    Then user should able to see module setup step two
    When user fill the module details in the step two and click on save and next
    Then user should able to see module content
    When user enters the empty values like "<RefeName>", "<Heading>", "<Context>" and "<ImageUrl>"
    Then user should able to see respective error message for creating module

    Examples:
    | Tc     | RefeName | Heading | Context | ImageUrl    | Descp                 |
    | Tc028  | ""      | Headinggg    | Contexttt | selImage  |  Reference           |
    | Tc029  | Refereencee1 | ""         | Contexttt | selImage   |  Heading      |
    | Tc030  | Refereencee1 | Headinggg    | ""          | selImage   | Context    |
    | Tc031  | Refereencee1 | Headinggg    | Contexttt | empImage  | Image Url     |






  







