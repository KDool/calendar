*** Settings ***
Documentation     Template robot main suite.
Library           Collections
Library           MyLibrary
Resource          keywords.robot
Variables         MyVariables.py
Library           RPA.Windows
Library    RPA.Desktop
# Library    RPA.Desktop
# Library    RPA.Desktop.Windows
# Variables
*** Tasks ***
Task1
    
    ${mlist}    Read File    lichTuanBanHanh_18042022_1017.xlsx
    FOR    ${element}    IN    @{mlist}
        Log    ${element}
    END
    # Event to Calendar    ${element}
    Windows Search    Calendar
    FOR    ${element}    IN    @{mlist}
        Event to Calendar    ${element}
        Sleep    0.5
    END
    
    Press Keys    alt  f4
    # Add An Event to Calendar    ${mlist}[0]   


*** Keywords ***

Event to Calendar
    
    [Arguments]    ${element}
    Press Keys    ctrl  n
    RPA.Windows.Click    name:"Event description"
    Type Text    ${element}[4]
    Sleep    1.5
    RPA.Windows.Click    name:"Start Date"
    Type Text    ${element}[0]
    Sleep    1.5
    RPA.Windows.Click    name:"Start time"
    Type Text    ${element}[1]
    Sleep    1.5
    RPA.Windows.Click    name:"Location"
    Type Text    ${element}[3]
    Sleep    1.5
    RPA.Windows.Click    name:"Event name"
    Type Text    ${element}[2]
    Sleep    1.5
    Press Keys    ctrl  s
