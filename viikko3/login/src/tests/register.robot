*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Lucy
    Set Password  lucy12345678
    Set Password_confirmation  lucy12345678
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password And Confirmation
    Set Username  Lucy
    Set Password  lucy12345678
    Set Password_confirmation  lucy12345678
    Click  button >> text=Register
    Register Should Succeed

Register With Different Password And Confirmation
    Set Username  Lucy
    Set Password  lucy12345678
    Set Password_confirmation  lucy87654321
    Click  button >> text=Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Password Containing Numbers
    Set Username  Lucy
    Set Password  kalle123
    Set Password_confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Characters
    Set Username  Lucy
    Set Password  kalle#abc
    Set Password_confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Only Lowercase Letters
    Set Username  Lucy
    Set Password  kallekalle
    Set Password_confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  Lucy
    Set Password  KalleKalle
    Set Password_confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Too Short Username And Valid Password
    Set Username  L
    Set Password  lucy12345678
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  Lucy
    Set Password  lucy
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle12345678
    Click  button >> text=Register
    Register Should Fail With Message  Username already exists

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Text  id=password  ${password}

Set Password_confirmation
    [Arguments]  ${password_confirmation}
    Fill Text  id=password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle12345678
    Go To Register Page
