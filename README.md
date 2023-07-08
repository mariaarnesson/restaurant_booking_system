# Restaurant Le chère

[View the live project here]()
Here is the reservation system for Le chère Restaurant created in Django for Portfolio Project 4 - Python + Django Essentials for Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/se/). 

The user has the ability to book one or more guests for a meal at the restaurant for a specific time and date, and has the ability to edit or delete reservations.
The website owner has the ability to accept online reservations for this restaurant.

![Responsive](media/responsive.png)

# Table of content

- [User Experience (UX)]
- [Features]
    - [Existing Features]
    - [Features Left to Implement]
- [Design]
    - [Wireframe]
- [Testing]
- [Deployment]
- [Technologies Used]
    - [Languages Used]
    - [Frameworks, Libraries and Programs Used]
- [Credits]
    - [Code]
    - [Media]


# User Experience (UX)
## USER STORIES:
- USER STORY: Navigation bar #1
    - As a **Site User** I can **use navigation menu ** to **switch to other options.**
- USER STORY: Button Home #2
    - As a **Site User** I can **select the home option** to **find out more information about the restaurant**, like **restaurant story** and **satisfied customer reviews.**
- USER STORY: Online Booking Button #3
    - As a **Site User** I can **select the online booking option** to **make table reservations.**
- USER STORY: My Bookings Button #4
    - As a **Site User** I can **select my bookings option** to check **my booking history**
- USER STORY: Log in / Log out Button #5
    - As a **Site User** I can **select the option log in/ log out** to be able **to log in or out of the site.**
- USER STORY: Our Menu #6
    - As a **Site User** I can **use the our menu option** to check **the current menu.**
- USER STORY: Admin account #7
    - As a **Admin** I can **access to all table reservations**
- USER STORY: Edit reservation #8
    - As a **logged in Site User** I can **edit/delete existing bookings** so that **I can make changes online if needed.**
- USER STORY: Account registration #9
    - As a **Site User** I can **register an account**
- USER STORY: Log in #10
    - As a **Site User** I can **register or log in** to **make table reservations**
- USER STORY: Registration #11
    - As a **Site User** I can **register** by **entering my email, password** and **confirming my password.**
- USER STORY: Password #12
    - As a **Site User** I can **easily recover my password** in case **I forget it.**     
- USER STORY: Footer layout #13
    - As a **Site User** I can **use the footer** to switch to **other options** and check **restaurant locations on the map.**
- USER STORY: Basic information on the homepage. #14
    - As a **Site User** I can **use information from the home page** so that **I will get basic information.**
- USER STORY: Lower priced meal suggestions are available on the home page. #15
    - As a **Site User** I would like to have **access to the lower priced meals shown on the home page** so that **I can take advantage of the promotion.**
- USER STORY: Icons showing customer and meal information. #16
    - As a **Site User** I am aware of the **number of guests** and **the number of meals in the restaurant** so that **I know if the restaurant has good reviews.**
- USER STORY: Chef information and photo. #17
    - As a **Site User** I want **access to information about the chef** so that **I can find out more about the restaurant.**               
- USER STORY: Create booking #18
    - As a **Site User** I can **choose the online booking option** to **reserve a table**
- USER STORY: Check reservations #19
    - As a **Site User** I can **select my bookings option** to check **my bookings history.**

# Features
## Existing Features
- Navigation bar
    - The navigation bar is easy to read and looks pleasent. The full responsive navigation bar includes links the Logo, Home page, Online booking, Our Menu and it is possible to log in and check the booking's history. The navigation bar is identical in each page to allow for easy navigation.
    The navigation bar is responsive on the iPod screen, the sites in the navigation bar on smallare screen are covered to the 'burger' style.

    ![Navigation bar logged out user ipad](media/navbar_ipad_login.png)
    ![Navigartion bar logged in user ipad](media/navbar_ipad_logout.png)

    When a user is not logged in, it is possible to register or log in:

    ![Navigation bar logged out user](media/navbar_logout.png)

    The logged in user has the ability to make a reservation and check the reservations in the booking history, and the ability to log out:
    ![Navigation bar logged in user](media/navbar_login.png)

      The navigation bar will allow the user to easily navigate from page to page on all devices without returning to the previous page using the "Back" button.

- Home Page
    - After the page loads, a picture of a women with a cup is shown as the main picture that introduces the text about the restaurant.

    ![Home Page](media/home_page.png)

        - Introduction text
    - Scrolling down a few words from the author is introducing and setting out what the website is presenting and the general information about the restaurant is being told.



    - Home Page Photos of foods
    - The next part of the main page shows four photos of food nicely arranged  one above the other. The photos present meals served in the restaurant.

    ![Special offers](media/special_offers_homepage.png)

    - Home Page Introduction Text

    ![introduction_text](media/french_restaurant_hompage.png)

    - Home Page - short description about the restaurant

    ![About the restaurant](media/about_restaurant.png)

    - Home Page - about a chef to the restaurant

    ![Chef Home Page](media/our_chef_homepage.png)

- Footer
    - The footer includes restaurant's location, address and opening hours are presented.

    - The background of the footer is slightly darker to show the contrast between the text in a distinctive way.

    ![Fotter](media/footer.png)


- Menu
    - The menu page gives a list of meals served in the restaurant. There is described the meals, drinks and the price of them.

    - Menu- main dishes

    ![Menu main dishes](media/menu_main_dishes.png)

    - Menu- drinks

    ![Menu drinks](media/menu_drinks.png)

    - Menu- desserts

    ![Menu desserts](media/menu_desserts.png)

    - Booking Online Page
    - The user has to be logged in to reserve a table. There is a possibility to book a table on the online booking website. The user selects the date/time of the reservation from the drop-down list and can select the number of guests from 1 to 5 to indicate how many people they want to include in their booking, and select a occassion from existing in the form. The user then clicks the Add reservation button to complete the booking and is redirected to the My Bookings page to see all upcoming and past bookings.

    - Booking Online Page:

    ![Booking Online Page](media/booking_online_page.png)

    - Booking Online Page on small screen:
    ![Booking Online Page on small screen](media/booking_online_page_small_screen.png)


- My Bookings Page

    ![my_bookings](media/my_bookings.png)  

    - Remove booking.

    ![delete_booking](media/delete_reservation.png)

- Sign up/ Log in / Log out
    - Sign Up Page
       - After opening the sign up page, a photo and a form to fill out are displayed. For this purpose, the user should fill in his contact details, such as: username, email and password.

       ![Sign Up Page](media/sign_up.png)

    - Log In Page
       - After opening the login page, a photo and a form to fill out are displayed. The user should fill in the username and password for this purpose.

       ![Log In Page](media/log_in.png)

    - Log Out Page
        - When the log out page is opened, a message is displayed asking if the user is sure that he/ she wants to log out, and a button: "log out" is displayed.

        ![Log Out Page](media/sign_out.png)   

## Features which could be implemented in the future:
- video supporting the facts:
    - By adding a video about the restaurant, the user could learn more about restaurant and localisation.
- video as a background to the online booking page.
# Design
## Wireframe: 
- Wireframe Desktop:
    - Home Page
        
    ![wireframes_desktop_home](media/wireframes_desktop_home.png)


    - Menu Page

    ![wireframes desktop menu](media/wireframes_desktop_menu.png)

    - Booking Online Page

    ![wireframes desktop online booking](media/wireframes_desktop_online_booking.png)

    - My Bookings Page

    ![wireframes desktop my bookings](media/wireframes_desktop_mybookings.png)

    - Log In Page

    ![wireframes desktop log in page](media/wireframes_login_desktop.png)

    - Sign Up Page

    ![wireframes desktop sign up page](media/wireframes_desktop_signup.png)

    - Log Out Page

    ![wireframes log out page](media/wireframes_desktop_logout.png)

- Wireframe on smaller screen

    - Home Page
    ![wireframes ipad home nav hidden](media/wireframes_home_ipad.png)

    - Menu Page

    ![wireframes ipad manu page](media/wireframes_ipad_menu.png)

    - Online Booking

    ![wireframes ipad online booking page](media/wireframes_ipad_online_booking.png)

    - My bookings Page

    ![wireframes ipad my bookings page](media/wireframes_ipad_mybookings_page.png)



## Diagram

The presented diagram shows a logical data model. 
- Thanks to the 'No of guest' class, each user can select the number of people booking one table. 
- The ability to choose the time of the booked table is marked as TIME CHOICES. 
- The opportunity to choose the occasion of the booked table is marked as OCCASSION CHOICES. 
- The choice of table type is marked as TABLE CHOICES.

![diagram_reservation](media/diagram_reservation.png)
# Testing 

Testing information can be found in separate TESTING.md file.


# Deployment:
- The site was deployed to GitHub pages. The steps to deploy are as follows:
   
    - Login to Heroku
    - In the Heroku, select: Create new app
    - Enter name of the app
    - Enter region of the app
    - Navigate to the Settings tab.
    - In 'Config Vars' select 'PORT' as a key to and '8000' as a value
    - In 'Config Vars' select 'DATABASE_URL' as a key and select value
    - In 'Config Vars' select 'SECRET_KEY' as a key and select value
    - In 'Config Vars' select 'CLOUDINARY_URL' as a key and select value
    - From the tab on the top, select: Deploy.
    - Afrerword select Github and connect.
    - Enter the respository name on Github and select: Search
    - Click connect button.
    - In Manual deploy, select the 'Deploy Branch' option
    - Select 'Open app' on the right hand side of the screen
    - The app should appear in a new tab on the web browser
    - The live link can be found here - [View the live project here]()
# Planning
## Technologies Used
### Languages Used
- [HTML](https://sv.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language))
- [JQUERY](https://en.wikipedia.org/wiki/JQuery)

### Frameworks, Libraries and Programs Used:

- [Balsamiq](https://balsamiq.com/) was used to create wireframes.
- [Font Awesome](https://fontawesome.com/) was used to create icons to footer and home page, logo.
- [Google Fonts](https://fonts.google.com/?preview.text=Love%20Running&preview.text_type=custom) was used to import 'Caveat', 'Courier New' och 'Lato' that have been used for each page.
- [Git](https://git-scm.com/) was used  by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used as a repository for code of the project. 
- [Django](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application.
- [Bootstrap](https://getbootstrap.com/) was used to build responsive webbpages.

# Credits
## Code:

- meals
[Traditional French dish of fried frog legs.](https://www.tasteatlas.com/cuisses-de-grenouilles#:~:text=Cuisses%20de%20grenouilles%20is%20a,and%20parsley%20until%20well%20done.)
- This page was used to help bild a lay out to Log in, Log out, Sign up, Online booking and Our menu - [MDB](https://mdbootstrap.com/docs/standard/extended/login/)
- [French soup descrition](https://www.deliciousmagazine.co.uk/recipes/soupe-de-poissons/)
- [Warm French Goat’s Cheese Salad](https://www.recipetineats.com/warm-french-goats-cheese-salad-salade-de-chevre-chaud/)
- [Classic Tomates Farcies](https://www.pardonyourfrench.com/classic-tomates-farcies-baked-ground-meat-stuffed-tomatoes/)
- [French Roast Leg of Lamb](https://www.curiouscuisiniere.com/french-roast-leg-of-lamb/)
- [Cuisses de Grenouille](https://www.tasteatlas.com/poulet-basquaise)
- [desserts- Crème brûlée](https://fernweheditions.com/blogs/scent-stories/creme-brulee#:~:text=Creme%20br%C3%BBl%C3%A9e%20is%20a%20French,and%20crunch%20to%20the%20dessert.)
- [Macarons](https://bakerpedia.com/processes/macaron/#:~:text=Macarons%20are%20small%2C%20delicate%20and,base%20known%20as%20the%20foot.)
- This page was used to help me include testing in correctly way - [TESTING.md](https://github.com/AJGreaves/familyhub/blob/master/testing.md)

- My codes were based on information from that site [ModelForm](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/)
## Media:
All pictures was taken from [Freepik](https://www.freepik.com/).



