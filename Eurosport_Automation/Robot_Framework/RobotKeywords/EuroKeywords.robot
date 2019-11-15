*** Settings ***
Documentation     Keywords supported for Discovery portal
...               dev- Vasuja
...               Comments:

Library    Collections

*** Keywords ***
I open the web page with ${url}
    Run Keyword      Open_Url     ${url}

I login to home page
    [Arguments]  &{login_info}
    ${result} =    Run Keyword    euro_login  &{login_info}
    Should be true  ${result}

Close The Browsers
	Run Keyword     Close The Browser

I switch to "${myNewPage:[^"]+}" page
	&{pageSwitch}=    Create Dictionary       page=${myNewPage}
	Run Keyword       Switch Page      &{pageSwitch}

I play the video
    [Arguments]  &{video_details}
    ${result} =    Run Keyword    play video  &{video_details}
    Should be true  ${result}



