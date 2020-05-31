# API for foodlink android app
API

Models:

  User:
    email string
    password secret
    name - username string
    location - street and city. String
    card_number string
    phone_number string
    is_active bool
    is_chef bool
    is_first bool
    current_money float
    code String
  Food:
    name string
    price float
    portion string
    products string
    time_of_cooking time
  Order:
    user
    status string
    total_price float
    time - time
    foods - list of foods in order
    chef
  Chef:
    user
    rating
    total_money
  Menu:



User API

foodlink.pythonanywhere.com/api/user/create - POST

-email

Create User.

foodlink.pythonanywhere.com/api/user/token - POST

-email
-code

Login, return token for authorization. Token must be using in header like:
Authorization :  Token “token_string”

foodlink.pythonanywhere.com/api/user/checkmail - POST
-email

check if there is a user with this email. If not create user

foodlink.pythonanywhere.com/api/user/me - PATCH

- any field from user model

change certain parameters 

foodlink.pythonanywhere.com/api/user/me - PUT

-all field from user model

change all params

Food

foodlink.pythonanywhere.com/api/user/me - GET

return user information

foodlink.pythonanywhere.com/api/food - POST

fields = ('id','name','price','portion','products','time_of_cooking')

create Food object for menu

foodlink.pythonanywhere.com/api/food - GET

return all food objects


Chef

foodlink.pythonanywhere.com/api/chef - POST

-user

crete chef user



 
