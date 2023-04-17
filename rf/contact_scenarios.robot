*** Settings ***
Library  Collections
Library  rf.AddressBook
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  ffgfgfg  ffgffg
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should be Equal  ${new_list}  ${old_list}


Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should be Equal  ${new_list}  ${old_list}


Modify contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length    ${old_list}
    ${index}=  Evaluate    random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    ${new_contact}=  New Contact  gghghJ  Kghghghg
    Modify Contact  ${contact}  ${new_contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Append To List  ${old_list}  ${new_contact}
    Contact Lists Should be Equal  ${new_list}  ${old_list}