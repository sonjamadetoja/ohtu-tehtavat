*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***

Register With Valid Username And Password
    Input Credentials  testuser  testpassword1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  testpassword1
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  testuser  word
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testuser  password
    Output Should Contain  Password doesn't contain a non-letter character

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command