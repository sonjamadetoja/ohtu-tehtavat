*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***

Register With Valid Username And Password
    Create User  testuser  testpassword1
    Output Should Contain  New user registered

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command