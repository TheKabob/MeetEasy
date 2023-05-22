# MeetEasy
Simple video conferencing web app using jitsi-meet
## Project Structure

There are 2 folders Front-end and Backend
### Front-End
1. Index.html is the login page
2. register.html is the register page
3. jitse-meet.html is a basic html page which you get once you register for jaas [jitsi-as-as-service](https://jaas.8x8.vc/#/)
4. forgot.html and reset.html can be configured accordingly
5. Inside /Landing folder you have index.html which is the primary landing page. If you click on "Try now" button from ths landing page, it will redirect you to logim page

### Backend
#### Backend for this project is implemented on python using FastApi and Postgres database to store user data
1. The backend folder is structured in Model, service, controller fashion
2. Model folder has model.py which has classes which create the required models
3. In Dao (Data access layer) we have the actual implementation logic of login and register functionality
4. login_register_service.py has the endpoint logic for login and register
5. settings.py is used to fetch the environment variables, we need some enviroment variables which will be used to create a connection between backedn and database.

### Databse 
setup a local postgres database or any SQL database of your choice, create a "users" table which can store user data in it.
```sql
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  name VARCHAR(20) NOT NULL,
  email VARCHAR(30) NOT NULL,
  password VARCHAR(20) NOT NULL
);
```


