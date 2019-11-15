*** Settings ***

*** Variables ***
#Discovery portal info
#####Automation setup#####
${URL}                     https://www.eurosportplayer.com/
${Username}                ch@test.com
${Password}                testES1

${BROWSER}                firefox    #chrome  #canary
${Firefox_Profile_path}     /home/syam.s/.mozilla/firefox/t59w63h4.default
@{favorite_show_list}=    APOLLO    SAVAGE_BUILDS  #  SERENGETI
