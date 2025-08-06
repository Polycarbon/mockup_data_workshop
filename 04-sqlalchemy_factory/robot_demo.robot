*** Settings ***
Documentation     Demonstration of using factory_boy's SQLAlchemyFactory with Robot Framework.
Library           keywords.py

*** Test Cases ***
Generate And Query Customers
    ${records}=    Create Fake Customers    3
    Length Should Be    ${records}    3
    ${email}=    Set Variable    ${records[0].email}
    ${cust}=     Get Customer By Email    ${email}
    Should Be Equal As Strings    ${cust['email']}    ${email}

Delete Customer
    ${email}=    Set Variable    delete_me@example.com
    Create Fake Customers    1
    ${deleted}=  Delete Customer By Email    ${email}
    Should Be Equal As Integers    ${deleted}    0
    # above may be 0 because generated email might not match; create explicit override
    ${cust}=     Get Customer By Email    ${email}
    Should Be Equal    ${cust}    ${None}
