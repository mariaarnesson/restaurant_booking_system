# Restaurant Le chère

[View the live project here]()
Here is the reservation system for Le chère Restaurant created in Django for Portfolio Project 4 - Python + Django Essentials for Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/se/). 

The user has the ability to book one or more guests for a meal at the restaurant for a specific time and date, and has the ability to edit or delete reservations.
The website owner has the ability to accept online reservations for this restaurant.


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



