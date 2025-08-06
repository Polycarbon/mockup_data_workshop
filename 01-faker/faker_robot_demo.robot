*** Settings ***
Documentation     Example Robot Framework test that demonstrates generating fake data using FakerLibrary.
Library           FakerLibrary

*** Test Cases ***
Generate Fake Data And Log
    ${name}=      FakerLibrary.Name
    ${email}=     FakerLibrary.Email
    ${address}=   FakerLibrary.Address
    Log To Console    Name: ${name}
    Log To Console    Email: ${email}
    Log To Console    Address: ${address}

Generate Custom Locale Data
    [Documentation]   Generate data in Thai locale.
    ${phone}=          FakerLibrary.Phone Number
    Log To Console     Thai phone number: ${phone}
