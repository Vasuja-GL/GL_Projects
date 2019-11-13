*** Settings ***
Documentation     This test case will navigate to "https://www.eurosportplayer.com/" and verify the fields
#...               dev-Vasuja
#...               Comments: This testcase login to www.eurosportplayer.com and play one video

#Suite Setup and Teardown
Suite Setup       Set Init Env
Suite Teardown    Close The Browsers


#Keywords Definition file
Resource           ../../RobotKeywords/EuroKeywords.robot

#Variable files
Resource           ../../Variables/EnvVariables.robot


#Discovery Component
Library			  ../../lib/EuroComponent.py    browser=${BROWSER}    profile_path=${Firefox_Profile_path}
Library  String

*** Test Cases ***
Verify the favorites status in Discovery.com
    [Tags]  Euro
    When I open the web page with ${URL}
    sleep  10s
    Set to Dictionary    ${login_details}    cookie_policy    True
    Set to Dictionary    ${login_details}    Username    ${Username}
    Set to Dictionary    ${login_details}    Password    ${Password}
#
#
    #Then I login to home page  &{login_details}
    When I switch to "on_demand" page
    Set to Dictionary    ${video_details}    play_button_xpath    First_video_play_button
    And I play the video  &{video_details}

    sleep  5s


*** Keywords ***
Set Init Env
    ${login_details}=    create dictionary

    Set suite variable    ${logindetails}

    ${video_details}=    create dictionary

    Set suite variable    ${video_details}