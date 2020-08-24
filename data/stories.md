## Order event Story

* greet
  - utter_greet
* user_wants_to_see_cities
  - utter_display_cities
* user_chose_events
  - display_event_menu
* user_chose_events_items
  - order_received_from_user
  - utter_proceed_booking
* user_wants_to_book_ticket
  - utter_no_of_ticket
* user_choose_no_of_ticket
  - final_order_from_user
* user_email
  - confirmation_to_user
  - utter_goodbye



## User does not want to book

* greet
  - utter_greet
* user_does_not_want_to_book
  - utter_thanking_message
  - utter_goodbye
