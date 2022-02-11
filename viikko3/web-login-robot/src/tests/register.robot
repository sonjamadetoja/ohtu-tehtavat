*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  t
    Set Password  password1
    Set Password Confirmation  password1
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  pass
    Set Password Confirmation  pass
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  password1
    Set Password Confirmation  salasana2
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation don't match

Login After Successful Registration
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  testi
    Set Password  testi123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  testi
    Set Password  password1
    Set Password Confirmation  salasana2
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation don't match
    Go To Login Page
    Login Page Should Be Open
    Set Username  testi
    Set Password  password1
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}