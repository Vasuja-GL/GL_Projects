*** Settings ***
Documentation     Keywords supported for Discovery portal
...               dev- Vasuja
...               Comments:

Library    Collections

*** Keywords ***
I open the web page with ${url}
    Run Keyword      Open Url     ${url}

Close The Browsers
	Run Keyword     Close The Browser

I switch to "${myNewPage:[^"]+}" page
	&{pageSwitch}=    Create Dictionary       page=${myNewPage}
	Run Keyword       Switch Page      &{pageSwitch}

I select the show and return title
    [Arguments]  &{show_info}
    ${show_title_list}  ${result} =    Run Keyword    select_show_and_return_title  &{show_info}
    Should be true  ${result}
    [Return]  ${show_title_list}

I add show to favorite list
    [Arguments]  &{favorite_button_info}
    ${show_title_list}  ${result} =    Run Keyword       add_show_to_favorite_list    &{favorite_button_info}
    Should be true  ${result}
    [Return]  ${show_title_list}

I verify favorites status
    Run Keyword       verify_favorites_status

I verify favorites shows
    [Arguments]    &{show_list}
    ${result} =    Run Keyword    verify_favorites_shows    &{show_list}
    Should be true  ${result}
