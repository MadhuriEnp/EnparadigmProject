@simStudioxAdmin @simpath @AIDiagnostic
Feature: simstudio Admin Login feature

Background: Login functionality with valid credentials
Given user is in simstudio admin login page
When user clicks on sign in with google button and enters valid credentials
Then user should able to see simstudio dashboard page


  @simStudioTextAIDiagnosticSimStudioUser
Scenario: Tc001 Verify the complete flow of AI Diagnostic Text Gametype creating and play it
     When user clicks on scenario bank and clicks on create scenario
    And user fills all the details in the text scenario for the creation
    When user clicks on create module
    Then user should able to see create module page
    When user fill the module details in the step one and clicks on save and next in the AI Diagnostic Gametype
    And user fills the atom setup details in atom set up step1b
    Then user should able to see module content
    When user fill the details in step three clicks on pubhish it for testing for creating AI Diagnostic Gametype
    When user clicks on modules and searchs for the just created module and published it in AIDiagnostic and plays it

@simStudioVideoAIDiagnosticSimStudioUser
Scenario: Tc002 Verify the complete flow of AI Diagnostic Video Gametype creating and play it
     When user clicks on scenario bank and clicks on create scenario
   And user fills all the details in the video scenario for the creation
    When user clicks on create module
    Then user should able to see create module page
    When user fill the module details in the step one and clicks on save and next in the AI Diagnostic Gametype
      And user fills the atom setup details in atom set up step1b
    Then user should able to see module content
    When user fill the details in step three clicks on pubhish it for testing for creating AI Diagnostic Gametype
    When user clicks on modules and searchs for the just created module and published it in Video AIDiagnostic and plays it in simstudio user profile

 @userProfileAiDiagnosticPlay
 Scenario: Tc003 Verify the AI Diagnostic flow from the sim studio user profile
   When user enters the Ai diagnostics in the search bar and clicks on play button
   And user plays the AI diagnostic sim

 @catalyxuserprofileAIDiagnosticPlay
 Scenario: Tc004 Verify the AI Diagnostic flow from the catalyx user profile
   Given User opens admin login page
   When user clicks on sign in with google button and enters valid user credentials in the already signedin account
   Then user should able to see catalyx admin homepage
   When user clicks on cohort management and create user
   And user selects cohort and company for Ai diagnosticsss
   And user enters valid details for Ai diagnosticsss
   When user clicks on Post Rollout
   And user clicks on Usermanagement
   And user verifies the details of user name and email for aid
   Then user clicks on MagicLink and clicks on copy magic Link and plays the game

 @TextScenarioBank
 Scenario: Tc005 Verify the creation of text scenario in the scenario bank
   When user clicks on scenario bank and clicks on create scenario
   And user fills all the details in the text scenario for the creation

 @VideoScenarioBank
 Scenario: Tc006 Verify the creation of video scenario in the scenario bank
   When user clicks on scenario bank and clicks on create scenario
   And user fills all the details in the video scenario for the creation


   @TextAIDiagnosticCreatingAndPlaysCatalystUser
   Scenario: Tc007 Creating Text AI Diagnostic and playing it from catlyst admin user
     When user clicks on scenario bank and clicks on create scenario
     And user fills all the details in the text scenario for the creation
     When user clicks on create module
     Then user should able to see create module page
     When user fill the module details in the step one and clicks on save and next in the AI Diagnostic Gametype
     And user fills the atom setup details in atom set up step1b
     Then user should able to see module content
     When user fill the details in step three clicks on pubhish it for testing for creating AI Diagnostic Gametype
     And user enters module name in the search and clicks on publish
     Given User opens admin login page
     When user clicks on sign in with google button and enters valid user credentials in the already signedin account
     Then user should able to see catalyx admin homepage
     When user clicks on path management, create path and clicks on static and selects Path1
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
     When user clicks on cohort management and create user1
#    When user clicks on create user
     And user selects cohort and company for creating learner user in gametype
     And user enters valid details for the learning profile
     When user clicks on Post Rollout
     And user clicks on Usermanagement
     And user verifies the details of user name and email
     Then user clicks on MagicLink and clicks on copy magic Link2 and plays the game

     @VideoAIDiagnosticCreatingAndPlaysCatalystUser
   Scenario: Tc008 Creating Video AI Diagnostic and playing it from catlyst admin user
    When user clicks on scenario bank and clicks on create scenario
   And user fills all the details in the video scenario for the creation
    When user clicks on create module
    Then user should able to see create module page
    When user fill the module details in the step one and clicks on save and next in the AI Diagnostic Gametype
      And user fills the atom setup details in atom set up step1b
    Then user should able to see module content
    When user fill the details in step three clicks on pubhish it for testing for creating AI Diagnostic Gametype
     And user enters module name in the search and clicks on publish
   Given User opens admin login page
     When user clicks on sign in with google button and enters valid user credentials in the already signedin account
     Then user should able to see catalyx admin homepage
    When user clicks on path management, create path and clicks on static and selects Path1
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
    Then user clicks on MagicLink and clicks on copy magic Link2 and plays the game


  @TextScenarioBankNegative
 Scenario Outline: <Tc> Verify the creation of text scenario in the scenario bank with empty <Descp>
   When user clicks on scenario bank and clicks on create scenario
   And user fills empty values like "<SceHeading>", "<SceDescrip>", "<SceQuestion>", "<SceHint>", "<SceIdealResp>", "<MetaTags>", and "<Atoms>" in the text scenario for the creation
    Then user should able to see the respective error messages for scenario creation
    Examples:
    | Tc     | SceHeading       | SceDescrip     | SceQuestion | SceHint | SceIdealResp       | MetaTags   | Atoms    | Descp            |
    | Tc009  | ""               | Scenario Descp | sc question | sechint | Scenario IdealResp | selMetTag  | selAtom  | heading          |
    | Tc010  | Scenario Heading | ""             | sc question | sechint | Scenario IdealResp | selMetTag  | selAtom  | Description      |
    | Tc011  | Scenario Heading | Scenario Descp | ""          | sechint | Scenario IdealResp | selMetTag  | selAtom  | Question         |
    | Tc012  | Scenario Heading | Scenario Descp | sc question | ""      | Scenario IdealResp | selMetTag  | selAtom  | Question         |
    | Tc013  | Scenario Heading | Scenario Descp | sc question | sechint | ""                 | selMetTag  | selAtom  | Ideal Response   |
    | Tc014  | Scenario Heading | Scenario Descp | sc question | sechint | Scenario IdealResp | empMetTag  | selAtom  | Meta Tag         |
    | Tc015  | Scenario Heading | Scenario Descp | sc question | sechint | Scenario IdealResp | selMetTag  | empAtom  | Atom             |


     @VideoScenarioBankNegative
 Scenario Outline: <Tc> Verify the creation of video scenario in the scenario bank with empty <Descp>
   When user clicks on scenario bank and clicks on create scenario
   And user fills empty values like "<SceHeading>", "<SceDescrip>", "<VideoRefName>", "<Thumbnail>", "<Video>", "<SceQuestion>", "<SceHint>", "<SceIdealResp>", "<MetaTags>", and "<Atoms>" in the video scenario for the creation
    Then user should able to see the respective error messages for scenario creation
    Examples:
    | Tc     | SceHeading       | SceDescrip     | VideoRefName | Thumbnail | Video | SceQuestion | SceHint | SceIdealResp       | MetaTags   | Atoms    | Descp            |
    | Tc016  | ""               | Scenario Descp | reference    | selthumnl | selvd | sc question | sechint | Scenario IdealResp | selMetTag  | selAtom  | heading          |
    | Tc017  | Scenario Heading | ""             | reference    | selthumnl | selvd | sc question | sechint | Scenario IdealResp | selMetTag  | selAtom  | Description      |
    | Tc018  | Scenario Heading | Scenario Descp | ""           | selthumnl | selvd | sc question | sechint | Scenario IdealResp | selMetTag  | selAtom  | reference        |
    | Tc019  | Scenario Heading | Scenario Descp | reference    | empthumnl | selvd | sc question | ""      | Scenario IdealResp | selMetTag  | selAtom  | hint             |
    | Tc023  | Scenario Heading | Scenario Descp | reference    | selthumnl | selvd | sc question | sechint | Scenario IdealResp | selMetTag  | selAtom  | thumbnail        |
    | Tc020  | Scenario Heading | Scenario Descp | reference    | selthumnl | empvd | sc question | sechint | Scenario IdealResp | selMetTag  | selAtom  | Video            |
    | Tc021  | Scenario Heading | Scenario Descp | reference    | selthumnl | selvd | ""          | sechint | Scenario IdealResp | selMetTag  | selAtom  | Question         |
    | Tc022  | Scenario Heading | Scenario Descp | reference    | selthumnl | selvd | sc question | sechint | ""                 | selMetTag  | selAtom  | Ideal Response   |
    | Tc024  | Scenario Heading | Scenario Descp | reference    | selthumnl | selvd | sc question | sechint | Scenario IdealResp | empMetTag  | selAtom  | Meta Tag         |
    | Tc025  | Scenario Heading | Scenario Descp | reference    | selthumnl | selvd | sc question | sechint | Scenario IdealResp | selMetTag  | empAtom  | Atom             |



    @SearchSceBank
    Scenario Outline: <Tc> Verify the search functionality in the scenario bank
      When user clicks on scenario bank and clicks on search scenario text box
      And user enters <PossibleSearch> search input
      Then user should able to be see the search outcome
      Examples:
      | Tc    | PossibleSearch |
      | Tc026 | A Sudden Presentation |
      | Tc027 | a sudden presentation |
      | Tc028 | sudden                |
      | Tc029 | dden                  |



      @EditScenario
      Scenario: Tc030 Verify the edit functionality in the scenario bank
        When user clicks on scenario bank and clicks on edit button
        And user edit some for the scenario details


      @NonExistingScenario
      Scenario: Tc031 Verify the search functionality with non existing scenario in scenario bank
        When user clicks on scenario bank and clicks on search scenario text box
        And user enters non existing scenario
        Then user should not able to be see the search outcome

      @ScenarioBankEditEmpty
   Scenario Outline: <Tc> Verify the edit functionality of scenario bank with empty <Descp>
     When user clicks on scenario bank and clicks on edit button1
     And user clears and fills empty values like "<SceHeading>", "<SceDescrip>", "<SceQuestion>", "<SceHint>", "<SceIdealResp>", "<MetaTags>", and "<Atoms>" in the text scenario for the creation
     Then user should able to see the respective error messages for scenario creation
    Examples:
    | Tc     | SceHeading       | SceDescrip     | SceQuestion | SceHint | SceIdealResp       | MetaTags   | Atoms    | Descp            |
    | Tc032  | ""               | Scenario Descp | sc question | sechint | Scenario IdealResp | selMetTag  | selAtom  | heading          |
    | Tc033  | Scenario Heading | ""             | sc question | sechint | Scenario IdealResp | selMetTag  | selAtom  | Description      |
    | Tc034  | Scenario Heading | Scenario Descp | ""          | sechint | Scenario IdealResp | selMetTag  | selAtom  | Question         |
    | Tc035  | Scenario Heading | Scenario Descp | sc question | ""      | Scenario IdealResp | selMetTag  | selAtom  | Question         |
    | Tc036  | Scenario Heading | Scenario Descp | sc question | sechint | ""                 | selMetTag  | selAtom  | Ideal Response   |
    | Tc037  | Scenario Heading | Scenario Descp | sc question | sechint | Scenario IdealResp | empMetTag  | selAtom  | Meta Tag         |
    | Tc038  | Scenario Heading | Scenario Descp | sc question | sechint | Scenario IdealResp | selMetTag  | empAtom  | Atom             |

        @DeleteSce
        Scenario: Tc039 Verify the delete funtionality in the scenario bank
           When user clicks on scenario bank and clicks on create scenario
           And user fills all the details in the text scenario for the creation
           And user searches for the newly created scenario and delete the scenario

    @VerifyProperTextsareReflecting
    Scenario: Tc040 Verifying that all module creation fields, such as module name, heading etc are accurately displayed in the user profile.
     When user clicks on search bar and enters module name
     Then user should able to see the searched module
      When user clicks on play and verifies all the fileds are sccureately displayed are not in the user profile

      @VerifyProperModuleFields
      Scenario: Tc041 Verifying that all module creation fields, such as module name, heading etc are accurately displayed in the Catalyst admin path.
        Given User opens admin login page
        When user clicks on sign in with google button and enters valid user credentials in the already signedin account
        Then user should able to see catalyx admin homepage
        When user clicks on path management, create path and clicks on static and selects Path for Sim's-1@ Sim's-2 module
        Then user should able to see edit path details page
        When user fills all the path details and click on save and next button
        Then user should able to see edit module details page and verifies whether module details are properly displayed are not








