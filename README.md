# Plugged In
Enter your location, find chargers near you. Leave reviews for others. 


![main](https://i.imgur.com/t4Dt5Cm.png)


Plugged In is a personal project where users can find EV chargers around the area they specify. They can also create an account and leave reviews for the chargers they have visited. 

[Live Link](https://plugged-in-proj.herokuapp.com/)

## Composition 
### Technologies Used

* BackEnd
    * Python (Flask)
    * SQLAlchemy / PostgreSQL
    * BCrypt (password Hashing)
* Front End
    * CSS
    * JQuery

### APIs

[Open Charge Map](https://openchargemap.org/site/develop/api#/) - API used to find EV chargers based on location. With every search, the list of chargers are saved to our database with all relevant information about the charging stations. 

[Google Maps Places API](https://developers.google.com/maps/documentation/places/web-service/overview) - this API is used to help make user's search easier. Can easily enter a place and is autocompleted. On the backend I take the longitude and latitude provided from the API to use as my location search argument to find chargers. 

[Google Maps Javascript API](https://developers.google.com/maps/documentation/javascript/overview) - this API was used to create custom maps where the list of chargers are marked for a user friendly view of charging locations. 

## How it Works
The backend is implemented with python and flask.  Users will fill out a form which takes in a location, the charging ports and search result amounts. Using the form inputs, a GET request is sent to the Open Charge Map API. <br>
The GET request responses is comprised of a list of charging stations. For each charging station, we check if the charging station is already on our database. If it is then we use our DB data to push to the user, else we will add the charging station including it's information to our DB. <br>

<p align="center">
  <img src="https://media1.giphy.com/media/VOJwoHS0ArzmEuf4Bu/giphy.gif" alt="animated" />
</p>


Users are also able to create an account. Through this account they may leave reviews on charging stations for others to view. All users can view active users and the reviews they have left. Users with a created account may also edit both their profile information as well as any reviews they have left. 


<p align="center">
  <img src="https://media0.giphy.com/media/3pw7xFvPyNfzR5hBbv/giphy.gif?cid=790b7611a72e72e9629fc7a2f290b109d4ec2f21f7ebac30&rid=giphy.gif&ct=g" alt="animated" />
</p>

<p align="center">
  <img src="https://media2.giphy.com/media/TvHFN0KZ7VRUxvumcR/giphy.gif?cid=790b7611461de07b071845e252fe02a557b1ce2ac4d6c567&rid=giphy.gif&ct=g" alt="animated" />
</p>