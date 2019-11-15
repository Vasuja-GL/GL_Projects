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
Login to Eurosport and play video
    [Tags]  playback_video
    When I open the web page with ${URL}
    When I switch to "OnDemand" page
    Set to Dictionary    ${video_details}    play_button_xpath    First_video_play_button
    And I play the video  &{video_details}

    sleep  10s


*** Keywords ***
Set Init Env
    ${login_details}=    create dictionary

    Set suite variable    ${logindetails}

    ${video_details}=    create dictionary

    Set suite variable    ${video_details}