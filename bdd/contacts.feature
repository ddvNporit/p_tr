Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <address>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact


  Examples:
  | firstname| lastname  | address            |
  | fgfg     | ddfdsasA  | fjfgjfj jfjfnnjfjd |
  | fkkfkkf  | fjfjfj    | khkhkkh fkj        |

Scenario Outline: Edit a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname> and <address>
  When I edit the contact from the list according to given contact
  Then the new contact list is equal to the old list with the edited contact

    Examples:
  | firstname   | lastname    | address     |
  | nррmeUP1    | lastрUро1    | ad33essUP54 |