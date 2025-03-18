@udtGametype @simpath
Feature: simstudio Admin Login feature

Background: Login functionality with valid credentials
Given user is in simstudio admin login page
When user clicks on sign in with google button and enters valid credentials
Then user should able to see simstudio dashboard page

  @AlreadyUDTGametypeSimUser1
  Scenario: Tc001 Verify flow of already udt Gametype created play it from sim user profile
    When user searches for already created universal DT module
    And user clicks on play button and plays it from the user profile

  @AlreadyUDTCatlyxAdminUser
  Scenario: Tc002 Verify flow of already udt Gametype created play it from catalyx admin user
    Given User opens admin login page
    When user clicks on sign in with google button and enters valid user credentials in the already signedin account
    Then user should able to see catalyx admin homepage
    When user clicks on cohort management and create user
    And user selects cohort and company for udt
    And user enters valid details for udt
    When user clicks on Post Rollout
    And user clicks on Usermanagement
    And user verifies the details of user name and email for udt
    Then user clicks on MagicLink and clicks on copy magic Link and plays the udt game


    @UDTModuleCreation
    Scenario: Tc003 Verify the creation of UDT module and plays it from sim studio admin user
      When user clicks on create module
      Then user should able to see create module page
      When user fill the module details in the step one and clicks on save and next in the Universal DT Gametype
      And user fills parameter settings in module steup in udt module
      Then user should able to see module content
      When user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype
      When user clicks on modules and searchs for the just created udt module and published it  and plays it in simstudio user profile


    @OptingDifOpts
    Scenario: Tc004 Verify the report after opting the different options
       When user searches for already created universal DT module
       And user opts the different options and see the report

    @VerifyingLifeLine
    Scenario: Tc005 Verify the functionality of lifeline in the sim while playing
      When user searches for already created universal DT module
      Then user should able to see the search outcome
      When user clicks on play button
      And user starts the play the game
      Then user should able to see enabled all three lifeline options
      And user should able to see the text when hovering on the lifelines
      When user clicks on preditcion button
      Then user should able to see a prediction message appearing
      When user clicks on any option of the choices
      Then user should able to prediction text on the option which we clicked
      And user should able to see disabled all three lifeline option
      When user clicks on submit button
      Then user should able to see disabled prediction button and enabled clarity and popularity button in step 2
      And user should be to see prediction text over the option
      When user clicks on clarity button
      Then user should able to see a clarity message appearing
      And user should able to see enabled clarity button and disabled prediction and popularity button
      When user clicks on any option and clicks on submit button
      Then user should able to see enabled popularity button and disabled prediction and clarity button in step 3
      When user clicks on popularity button
      Then user should able to be popularity icon over the options
      When user clicks on any option in step 3 and submit button
      Then user should able to see disabled all three lifeline option in step 4
      When user clicks on info icon on the right top corner
      Then user should able to be see udt scenario name and udt scenario description
      When user closes that popup and clicks on any option in the step 4
      And user clicks on submit button
      Then user should able to see disabled all three lifeline option in step 5
      When user clicks on any option and submit button in step 5
      Then user clicks on next buttons and able to end text


     @UDTModuleDebriefVideoCreation
    Scenario: Tc006 Verify the creation of UDT module with enabling debrief video and plays it from sim studio admin user
      When user clicks on create module
      Then user should able to see create module page
      When user fill the module details in the step one and clicks on save and next in the Universal DT Gametype
      And user fills parameter settings in module steup in udt module
      Then user should able to see module content
      When user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype with enabling debrief video
      When user clicks on modules and searchs for the just created udt module with debrief video and published it  and plays it in simstudio user profile


      @UDTModuleCreationPlaysfromCataylxAdminuser
    Scenario: Tc007 Verify the creation of UDT module and plays it from catalyx admin user
      When user clicks on create module
      Then user should able to see create module page
      When user fill the module details in the step one and clicks on save and next in the Universal DT Gametype
      And user fills parameter settings in module steup in udt module
      Then user should able to see module content
      When user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype
      When user clicks on modules and searchs for the just created udt module and published it for udt
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

        @UDTModuleDebriefVideoCreationPlayaCatalyxAdminUser
    Scenario: Tc008 Verify the creation of UDT module with enabling debrief video and plays it from sim studio admin user
      When user clicks on create module
      Then user should able to see create module page
      When user fill the module details in the step one and clicks on save and next in the Universal DT Gametype
      And user fills parameter settings in module steup in udt module
      Then user should able to see module content
      When user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype with enabling debrief video
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



     @UDTModuleEnableToggles
    Scenario: Tc009 Verify the creation of UDT module with enabling Disable Reports,Simulation,Disable Rewatch video and plays it from sim studio admin user
      When user clicks on create module
      Then user should able to see create module page
      When user fills the module details on step one
      And user enables toggles for Disable Reports,Simulation,Disable Rewatch video
      And clicks on save and next in the Universal DT Gametype
      And user fills parameter settings in module steup in udt module
      Then user should able to see module content
      When user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype
      When user clicks on modules and searchs for the just created udt module and published it and plays it in simstudio user profile
      Then user should be able to see the Reports and Rewatch video disabled while playing


 @VerifyProperTextsReflectionsforUDTT
    Scenario: Tc0010 Verifying that all udt module creation fields, such as module name, heading etc are accurately displayed in the SimStudio profile.
      #When user clicks on Modules search bar and enters UDT module name
     When user searches for already created universal DT module
     Then user should able to see the searched UDT module in Modules section
     When user clicks on play and verifies if all the fileds are accurately displayed in the simstudio user profile

   @VerifyProperModuleFieldsUDTT
      Scenario: Tc0011 Verifying that all udt module creation fields, such as module name, heading etc are accurately displayed in the Catalyx admin path.
        Given User opens admin login page
        When user clicks on sign in with google button and enters valid user credentials in the already signedin account
        Then user should able to see catalyx admin homepage
        When user clicks on path management, create path and clicks on static and selects Path for UDT's-1@ UDT's-2 module
        Then user should able to see edit path details page
        When user fills all the UDT path details and click on save and next button
        Then user should able to see edit module details page and verifies if UDT module details are properly displayed

  @VerifyDeleteScenariosUDT
      Scenario: Tc0012 Verifying Delete functionality UDT
        When user searches for already created universal DT module
        Then user should able to see the searched UDT module in Modules section
        When user clicks on edit icon in simstudio user profile
        Then user should be directed to Module Content Page
        When user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype
        When user clicks on delete icon on Module content Page and clicks on 'Yes delete it!'
        When user clicks on Modules search bar and enters UDT module name
        Then user should not be able to see the searched UDT module in Modules section


  @VerifyDeleteScenariosUDT1
      Scenario: Tc00122 Verifying Delete functionality UDT1
        When user clicks on create module
        Then user should able to see create module page
        When user fill the module details in the step one and clicks on save and next in the Universal DT Gametype
        And user fills parameter settings in module steup in udt module
        Then user should able to see module content
        When user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype
        When user clicks on delete icon on Module content Page and clicks on 'Yes delete it!'
        Then user should not be able to see the content pages in ModuleContent page


 @UDTModuleEnableVersionVariantToggle
    Scenario: Tc001312 Verify the Version/Variant Toggle functionality UDT
      When user clicks on create module
      Then user should able to see create module page
      When user fills the module details on step one
      When user enables toggle for Version/Variant
      Then user should see the Module Name same as selected parent module name along with version number

   @VerifyEditScenariosUDT
      Scenario: Tc0013 Verifying Edit functionality UDT
        When user clicks on Modules search bar and enters UDT module name
        Then user should able to see the searched UDT module in Modules section
        When user clicks on edit icon in simstudio user profile
        Then user should be directed to Module Content Page
        When user clicks on edit icon on Module content Page
        When user edits the Heading , Sub Heading , Content on Module Content Page and clicks on Save and Next
        When user clicks on Modules search bar and enters the same UDT module name and plays it
        Then user should be able to see the same edited fields on this page in SimStudio profile

   @VerifyInputOutputParametersOnCheckYourFocusPageUDTwithoutDebrief
      Scenario: Tc0014 Verifying display of InputParameters in ModuleSetup on Check Your Focus Page
        When user clicks on create module
        Then user should able to see create module page
        When user fill the module details in the step one and clicks on save and next in the Universal DT Gametype
        And user clicks on Step2 Module Setup and adds one more input and output parameter clicks on save&next
        When user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype
        When user clicks on modules and searchs for the just created udt module with debrief video and published it  and plays it in simstudio user profile
        #When user clicks on next buttons
        Then user should be able to see the input and output parameters on check your focus page same as those entered in Module Setup

   @VerifyFocusPageInputOutputParametersOnStep3ModuleContentPage
      Scenario: Tc0015 Verifying display of Parameters in ModuleSetup on step3 and Reflect Page without debrief enabled
        When user clicks on create module
        Then user should able to see create module page
        When user fill the module details in the step one and clicks on save and next in the Universal DT Gametype
        And user clicks on Step2 Module Setup and adds one more input and output parameter clicks on save&next
        When user fill the details in step three and verify step3 and step2 parameters UDT
        Then user clicks on step3 Module Content page and verify the given parameters in ModuleSetup Page

   @UDTModuleDebriefVideoOnParameterCheck
      Scenario: Tc0016 Verify the creation of UDT module with  debrief video enabled and check the input parameter and chkbox qstn on simstudio userprofile page
        When user clicks on create module
        Then user should able to see create module page
        When user fill the module details in the step one and clicks on save and next in the Universal DT Gametype
        And user fills parameter settings in module steup in udt module
        Then user should able to see module content
        When user fills the details in step3 validates output parameters of UDT Gametype with enabling debrief video from step2 and step3 and clicks on publish
        Then user seacrhed the module in Modules tab and validates input parameters and debrief titles with debrief enabled on simstudio Play Page

   @VerifySelectedOptionsCorrectlyDisplayedwhileSimstudioAdminProfile
      Scenario: Tc0017 Verifying display of Narrator Options in Deepdive Page
        When user clicks on create module
        Then user should able to see create module page
        When user fill the module details in the step one and clicks on save and next in the Universal DT Gametype
        And user clicks on Step2 Module Setup and adds one more input and output parameter clicks on save&next
        When user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype
        When user clicks on modules and searchs for the just created udt module with debrief video and published it  and plays it in simstudio user profile
        Then user should be able to see the selected narrator options in the simstudio complete deepdive page

