*** Settings ***
Documentation     Demonstration of using factory_boy via a custom Robot Framework library.
Library           02-factory_boy/factory_keywords.py

*** Test Cases ***
Create Single User And Log
    ${user}=    Create User  name=Jisoo
    Log To Console    Generated user: ${user}
    Should Be Equal As Strings    ${user.name}    Jisoo


Create Multiple Users And Validate Count
    ${users}=   Create Users    3  name=John
    Length Should Be    ${users}    3
    Log To Console    Users: ${users}
    
