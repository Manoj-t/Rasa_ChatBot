## happy path
* greet
- utter_greet
* restaurant_search{"cuisine": "chinese"}
- utter_restaurant
* thankyou
- utter_thankyou

## sad path 1
* greet
- utter_greet
* mood_unhappy
- utter_cheer_up
- utter_did_that_help
* mood_affirm
- utter_happy

## sad path 2
* greet
- utter_greet
* mood_unhappy
- utter_cheer_up
- utter_did_that_help
* mood_deny
- utter_goodbye

## say goodbye
* goodbye
- utter_goodbye

## active
* greet
- utter_greet
* behavioral_greet
- utter_behavior
* restaurant_search{"cuisine": "chinese", "location": "18328"}
- utter_restaurant
* thankyou
- utter_thankyou

## search
* greet
- utter_greet
* behavioral_greet
- utter_behavior
* restaurant_search{"cuisine": "chinese"}
- utter_restaurant
* thankyou
- utter_thankyou

## search
* greet
- utter_greet
* behavioral_greet
- utter_behavior
* restaurant_search{"location": "north"}
- utter_restaurant
* thankyou
- utter_thankyou
