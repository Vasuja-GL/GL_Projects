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
    When I open the web page with ${URL}
    sleep  10s
#    Set to Dictionary    ${login_details}    cookie_policy    True
#    Set to Dictionary    ${login_details}    Username    ${Username}
#    Set to Dictionary    ${login_details}    Password    ${Password}
#
#
#    Then Login to home page  &{login_details}


*** Keywords ***
Set Init Env
    ${login_details}=    create dictionary

    Set suite variable    ${logindetails}
