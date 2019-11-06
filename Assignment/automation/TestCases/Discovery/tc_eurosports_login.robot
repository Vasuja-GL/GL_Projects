*** Settings ***
Documentation     This test case will navigate to "https://go.discovery.com/" and verify the fields
#...               dev-Vasuja
#...               Comments: This is Discovery Take Home Assessment

#Suite Setup and Teardown
Suite Setup       Set Init Env
Suite Teardown    Close The Browsers


#Keywords Definition file
Resource           ../../RobotKeywords/DiscoveryKeywords.robot

#Variable files
Resource           ../../Variables/EnvVariables.robot


#Discovery Component
Library			  ../../lib/DiscoveryComponent.py    browser=${BROWSER}
Library  String

*** Test Cases ***
Verify the favorites status in Discovery.com
    [Tags]    Discovery
    Given I open the web page with ${URL}
    When I switch to "see_all_shows" page
    Set to Dictionary    ${show_details}    show_name    ${show_name}
    And I select the show and return title  &{show_details}
    Then I verify favorites status

    #To verify the favorites shows in Discovery.com
    @{favorite_show_list}=  copy list  ${favorite_show_list}
    :FOR    ${show}    IN    @{favorite_show_list}
    \    When I switch to "see_all_shows" page
    \    Set to Dictionary    ${show_details}    show_name    ${show}
    \    ${show_title_list}=    Then I add show to favorite list    &{show_details}
    \    @{favorite_selected_list}=    Combine Lists    ${favorite_selected_list}    ${show_title_list}
    log  ${favorite_selected_list}

    When I switch to "my_vedios" page
    :FOR    ${show}    IN    @{favorite_show_list}
    \    Set to Dictionary    ${show_details}    show_name    ${show}
    \    I verify favorites shows    &{show_details}



*** Keywords ***
Set Init Env
    ${show_details}=    create dictionary
    ${favorite_selected_list}=    Create list

    Set suite variable    ${show_details}
    Set suite variable    ${favorite_selected_list}
