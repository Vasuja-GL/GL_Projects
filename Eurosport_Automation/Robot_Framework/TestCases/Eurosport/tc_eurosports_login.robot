*** Settings ***
Documentation     This test case will navigate to "https://www.eurosportplayer.com/" and play the video
#...               dev-Vasuja

#Suite Setup and Teardown
Suite Setup       Set Init Env
Suite Teardown    Close The Browsers


#Keywords Definition file
Resource           ../../RobotKeywords/EuroKeywords.robot

#Variable files
Resource           ../../Variables/EnvVariables.robot


#Eurosports Component
Library			  ../../lib/EuroComponent.py

*** Test Cases ***
Testcase 1: Login to Eurosport and play video
    [Tags]  playback_video
    When I open the web page with ${URL}
    sleep  3
    When I switch to "OnDemand" page
    sleep  3
    Set to Dictionary    ${video_details}    play_button_xpath    First_video_play_button
    And I play the video  &{video_details}

    sleep  10s


*** Keywords ***
Set Init Env
    ${login_details}=    create dictionary

    Set suite variable    ${logindetails}

    ${video_details}=    create dictionary

    Set suite variable    ${video_details}

    I launch the browser  &{Browser_info}