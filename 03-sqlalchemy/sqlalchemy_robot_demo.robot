*** Settings ***
Documentation     Example Robot tests using SQLAlchemy keywords for a Customer table.
Library           db.py

*** Test Cases ***
Add And Query Customer
    ${cust_id}=    Add Customer    Jane Doe    jane@example.com    020-123-4567
    Log To Console    Inserted customer with id: ${cust_id}
    ${cust}=        Get Customer By Email    jane@example.com
    Should Be Equal As Strings    ${cust['name']}    Jane Doe
    Should Be Equal As Strings    ${cust['email']}   jane@example.com

Delete Customer
    ${deleted}=     Delete Customer By Email    jane@example.com
    Should Be Equal As Integers   ${deleted}    1
    ${cust}=        Get Customer By Email    jane@example.com
    Should Be Equal    ${cust}    ${None}
