# CI-MS3-Floral-Reef

<h2 align="center"><img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Floral_Reef_Mockup.PNG?raw=true"></h2>

This is the repository for Floral Reef, the only Irish Community-Driven Flower Encyclopedia. It is designed to be a contemporary take on a typical encyclopedia/text-heavy website by presenting the information in a clean, minimal and spacious display.

[View live project here.](https://ci-ms3-floral-reef.herokuapp.com/)

## User Experience (UX)

-   User Stories
    
    1.  First Time Visitor Goals
    
        -   As a First Time Visitor, I want to easily understand the main purpose of the site and easily navigate to where I want.
        -   As a First Time Visitor, I want to see what flowers are currently available on the website.
        -   As a First Time Visitor, I want to find information about a particular flower.
        -   As a First Time Visitor, I want to see photos of a specific flower.
    
    2.  Returning Visitor Goals
        
        -   As a Returning Visitor, I want to register and join the community/log into my account/edit my account details.
        -   As a Returning Visitor, I want to share my own photos to different flowers.
        -   As a Returning Visitor, I want to contribute to the community by adding flowers not currently on the website.
    
    3.  Frequent Visitor Goals
    
        -   As a frequent visitor, I want to be able to easily edit and delete the content that I contribute.
        -   As a frequent user, I want to see new content that has been added by users.

-   Design

    -   Colour Scheme
    
        -   The colours used throughout the website are: #EAEAE5 (background), #c7ae6b (links), #DDDEBD (buttons), #C9AD5D (buttons), HTML Crimson (delete button), #1E453C (navbar background) and #3a8573 (flower info).
        -   The navbar's dark green (#1E453C) was chosen to represent the richness of the Irish landscape. All other colours were based around this.
    
    -   Typography
    
        -   Two primary front are used throughout the website: 'Bellefair' and 'Crimson Text'. 'Bellefair' was chosen for headings as it's taller than normal vertical lines are reminiscent of the ancient Ogham stone found throughout the natural landscape of Ireland. 'Crimson Text' wsa chosen for all non-heading and non-link text to complement 'Bellfair' as a more subtle, but still sophisticated, font.

    -   Imagery
    
        -   The vast majority of imagery on Floral Reef is user-submitted via HTTP links. The only exception is the homepage background image, which is intended to provide an idealistic view of the landscape so that visitors get a positive impression of the website.
    
-   Wireframes

    -   Homepage
        
        -   [Mobile]()
        -   [Tablet]()
        -   [Desktop]()
    
    -   All Flowers
        
        -   [Mobile]()
        -   [Tablet]()
        -   [Desktop]()
    
    -   Individual Flower
        
        -   [Mobile]()
        -   [Tablet]()
        -   [Desktop]()
    
    -   Register/Add or Edit Flower/Edit Profile
        
        -   [Mobile]()
        -   [Tablet]()
        -   [Desktop]()
    
    -   Login
        
        -   [Mobile]()
        -   [Tablet]()
        -   [Desktop]()
    
    -   User Profile
        
        -   [Mobile]()
        -   [Tablet]()
        -   [Desktop]()

## Features

-   Responsive on all device sizes
-   Interactive elements
-   User accounts
-   Allows users to perform CRUD operations with a MongoDB database.
-   'Get Inspired' button which returns and displays a random flower from the database.
-   Search functionality
-   Image sharing

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python 3.7](https://www.python.org/)
-   [Javascript](https://www.javascript.com/)

### Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
    -   Google fonts were used to import the 'Bellefair' and 'Crimson Text' font into the project, both of which are used on all pages of the website.
    
2. [MDBootstrap:](https://mdbootstrap.com/)
    -   Material Design Bootstrap was used to assist with the responsiveness and styling of the website.
    
3. [Font Awesome:](https://fontawesome.com/)
    -   Font Awesome was used to import the magnifying glass for the search bar.
    
4. [jQuery:](https://jquery.com/)
    -   jQuery was used both to speed up JavaScript development, and because it was a requirement for MDBootstrap.
    
5. [Flask:](https://flask.palletsprojects.com/en/1.1.x/)
    -   Flask was used to develop the website to allow integration with an external database, as well as to reduce repetition in code as much as possible.
    
6. [Jinja:](https://palletsprojects.com/p/jinja/)
    -   The Jinja templating language came installed with flash and allows for quick editing of elements common to multiple, or all, pages.
    
7. [Werkzeug:](https://pypi.org/project/Werkzeug/)
    -   Werkzeug was used for debugging the project when error occurred. Werkzeug's password hashing was also used as an additional level of security when a user is logging in.

8. [MongoDB:](https://www.mongodb.com/)
    -   MongoDB was used to create a database to store information about the flowers, users and user images.

9. [Pymongo:](https://pypi.org/project/pymongo/)
    -   Pymongo was used for its ability to easily communicate between the web app and the MongoDB database.
    
10. [Python.OS:](https://docs.python.org/3/library/os.html)
    -   The Python OS module was used during the development process to create the following environment variables: 'IP', 'PORT', 'Secret Key', 'MONGO_URI', and 'MONGO_DBNAME'.
    
11. [Python.Random](https://docs.python.org/3/library/random.html)
    -   The Python Random module was used for an initial cersion of the 'Get Inspired' button which finds and return and random flower from the database. This was later replaced by the MONGODB query, "{$sample: {size: 1}}".
    
12. [BSON.ObjectId](https://docs.mongodb.com/manual/reference/method/ObjectId/)
    -   The ObjectId method was imported from BSON in order to verify MONGODB's object ids for multiple Flask functions.
    
13. [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.
    
14. [Git](https://git-scm.com/)
    -   Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

15. [GitHub](https://github.com/)
    -   GitHub is used to store the projects code after being pushed from Git.
    
16. [VSCode]()
    -   VSCode was the text editor used for this project. All installed addons can be found in the 'requirements.txt' file.
    
## Development

### Setting Up MongoDB Shell

1. A free account was set up on [cloud.mongodb.com](cloud.mongodb.com)
2. A new cluster and database were created.
3. Network Access was temporarily set to 'Allow Access From Anywhere'.
4. The MongoDB shell was downloaded and installed from [this link](https://downloads.mongodb.org/windows/mongodb-shell-windows-x86_64-4.4.2.zip).
5. The PATH environment variable was updated to include the MongoDB "/bin" folder, that was created by the installation of the shell.
6. "C:\mongodb" was also added to the PATH environment variable to allow access to 'mongod.exe' from anywhere outside the '/bin' directory.
7. A new terminal was created in VS Code, where 'mongod' was run.
8. Back on the mongodb website, the cluster's "Connect" button was run.
9. The connection string was copied from step 3.
10. Then another new terminal was created inside VS Code where the copied code was pasted, edited to include database name and then run.
11. The password for the database was inputted.

### Setting Up MongoDB within Python

1. Performed steps 1-8 from above.
2. Selected 'Connect your application' as the connection method.
3. Python was selected as the driver and version 3.6 or later was chosen.
4. Connection string was copied.
5. A .gitignore and env.py file were created, and the env.py file was added to the .gitignore file to prevent any sensitive information being uploaded to GitHub.
6. An os environment default variable called "MONGO_URI" was declared with a value of the Connection String.
7. A 'mongo_project.py' file was created, and the following code was added:

   ```python
    # Imports relevant libraries
    import os
    import pymongo
    if os.path.exists("env.py"):
        import env


    # Creates variables to store credentials
    MONGO_URI = os.environ.get("MONGO_URI")
    DATABASE = "myFirstDB"
    COLLECTION = "flowers"

    # Connects to MongoDB using above variables
    def mongo_connect(url):
        try:
            conn = pymongo.MongoClient(url)
            print("Mongo is connected!")
            return conn
        except:
            print("Could not connect to MongoDB: %s") % e


    conn = mongo_connect(MONGO_URI)

    # Puts collection into variable
    coll = conn[DATABASE][COLLECTION]

    # Creates variable to store all entries in collection
    documents = coll.find()

    # Prints all entries to the console
    for doc in documents:
        print(doc)
   ```

### Setting Up MongoDB Database

1. A new database called 'floral_reef' was created.
2. It was then populated with collections called 'flowers', 'user_images' and 'users'.
3. Test records were added to each collection to verify functionality.
4. The flower records were given the following fields: 'flower_name', 'latin_name', 'irish_name', 'family', 'created_by', 'is_wildflower', 'flowering_time', 'image_url', 'description', 'location', 'affiliate_1' and 'affiliate_2'.
5. The user_images records wer given the following fields: 'flower_id', 'image_source' and 'description'.
6. The users records were given the following fields: 'email', 'password', 'first_name', and 'last_name'.

### Creating a MongoDb Index

A MongoDB index was created in order to allow the database to be queried through user search.

1. A new terminal was opened within VSCode.
2. Python was initialised by typing ```python3```.
3. The instance of our app, 'mongo', was imported from the app file using: ```from app import mongo```.
4. A new index was created by typing: ```mongo.db.flowers.create_index([("flower_name", "text"), ("latin_name", "text"), ("irish_name", "text"), ("family", "text")])```

## Testing

### Code Validation

-   CSS W3C Validator [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-ms3-floral-reef.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    -   The W3C CSS Validator was used to validate all CSS used in the project. The validator found errors with some of MDBootstrap's CSS, as well as with custom use of the backdrop-filter property. As the backdrop-filter property is being used appropriately in this project and can be found on [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter), as well as many other sites such as [CSS Tricks](https://css-tricks.com/almanac/properties/b/backdrop-filter/), I can only assume that the Validator has yet to implement the property into it's checks.
    
-   HTML W3C Validator [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms3-floral-reef.herokuapp.com%2F)
    -   The E3C HTML validator was used via 'Validate by URI' to validate the HTML.
    
-   ExtendsClass [Python Tester](https://extendsclass.com/python-tester.html)
    -   The ExtendsClass Python Tester was used to check for syntax errors in the Python code. 
    
### Testing User Stories from User Experience (UX) Section

- First Time Visitor Goals

    1.  As a First Time Visitor, I want to easily understand the main purpose of the site and easily navigate to where I want.
        
        -   Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath, there is a hero image with text and a "Get Inspired" call-to-action button that shows the user a random flower.
        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Homepage.PNG?raw=true" alt="homepage">
        -   The text within the hero image on the homepage clearly defines what the website is and isn't, in order to set users' expectations accordingly.
        -   The intended path for the user to go down is to click he 'Get Inspired' button to see how the primary data is laid out. From there, they can either create an account and start contributing or view more flowers via the navbar.
        -   There is a search bar and responsive navbar that facilitate simple and quick user navigation.
        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Search_Bar.PNG?raw=true" alt="search bar">
        
    2.  As a First Time Visitor, I want to see what flowers are currently available on the website.

        -   From the homepage, users can click on the 'Get Inspired' button to be taken to a random flower.

        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Get_Inspired_Button.PNG?raw=true" alt="get inspired button">

        -   Users can view all the flowers on the website by clicking on the 'Flowers' tab in the navbar.

        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Navbar.PNG?raw=true" alt="navbar not logged in">

    3.  As a First Time Visitor, I want to find information about a particular flower.
        
        -   There is a search bar and responsive navbar that facilitate simple and quick user navigation, allowing users to find a flower by name, latin name, irish name or by the date it was uploaded to the website.
        -   Each flower profile contains multiple information fields about the flower, including its flowering time, whether it's considered a wildflower, locations it can be found in, and occasions it is typically used for.
        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Flower_Profile.PNG?raw=true" alt="flower profile">

    4.  As a First Time Visitor, I want to see photos of a specific flower.

        -   Each flower has a main image by which it can be identified. This is displayed both on the 'Flowers' page, and in each flower's profile page.
        -   Each flower profile has space below the flower information for users to upload and share their own images of the relevant flower.
        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/User_Images.PNG?raw=true" alt="user images">

-   Returning Visitor Goals
    
    1.  As a Returning Visitor, I want to register and join the community/log into my account/edit my account details.
        
        -   The navbar contains a 'Register' and 'Log In' buttons that displays whe no user is logged in.
        -   The 'Log In' page contains a link to the 'Register' page, in case the user hasn't created an account yet.
        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Log_In.PNG?raw=true" alt="login">
        -   The 'Register' page contains a link to the 'Log In' page in case the user already has an account.
        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Register.PNG?raw=true" alt="register">
        -   Each flower profile displays a link to the 'Log In' page when no user in logged in, so a user can log in to their account and start contributing.

        -   The profile page contains a button that allows the user to edit their profile details via a pre-populated form.
        
        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Edit_Profile_Button.PNG?raw=true" alt="edit profile button">
        
        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Edit_Profile.PNG?raw=true" alt="edit profile page">
        
    2.  As a Returning Visitor, I want to share my own photos to different flowers.
        
        -   Each flower profile has space below the flower information for users to upload and share their own images of the relevant flower.
        -   Each flower profile displays a link to the 'Log In' page when no user in logged in, so a user can log in to their account and start contributing.
    
    3.  As a Returning Visitor, I want to contribute to the community by adding flowers not currently on the website.

        -   There is a dedicated 'Add Flower' button within the navbar, that allows logged-in users to add a flower to the website/database via a form.
        <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Navbar_Logged_In.PNG?raw=true" alt="navbar logged in">
    
-   Frequent Visitor Goals

    1.  As a frequent visitor, I want to be able to easily edit and delete the content that I contribute to the site.

    -   Flowers can be edited by the user who created the flower. This prevents any user from changing another user's contribution.
    <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/Edit_Delete_Flower_Buttons.PNG?raw=true" alt="edit and delete flower buttons">
    -   Flowers can be deleted by the user who created it from the flower's profile page, using the 'Delete Flower' button.
    -   Each user-submitted image contains a delete button that only displays for the user who submitted the image, allowing them to delete the image at their behest.
    <img src="https://github.com/RichardByrne95/CI-MS3-Floral-Reef/blob/main/static/images/User_Image_Delete_Button.png?raw=true" alt="user image delete button">
        
    2.  As a frequent user, I want to see new content that has been added by users.
    
        -   The user would already be comfortable with the website layout and can easily navigate to the list of all the flowers where new flowers would be displayed.
        -   The user would already be comfortable with the website layout and can easily navigate to each of the individual flowers and view the user-submitted images.
    
### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Deployment

### Source Control Process

This project was developed using Visual Studio Code, Phaser Game Engine, Git and GitHub using the following steps:

1.  Logged into Github Desktop App
2.  A new repository called 'CI-MS2-Mintendo-PLAYCHILD' was created locally for this project.
3.  This repsoitory was initalised with a blank README.md file.
4.  This repository was then published from Github Desktop to the remote Github server using 'Ctrl + P'.
5.  The project folder was opened in Visual Studio Code where the initial files were created.
6.  A new terminal in Visual Studio Code (Ctrl + Shift + ') was opened to begin the git commit process.
7.  Files were added to the local git staging area using 'git add <'filename'>' and 'git add \*' where applicable.
8.  Local commits were made using the 'git commit -m <'message'>' command.
9.  These local commits were then periodically pushed to the remote Github server using the 'git push' command.
10. A local server was run throughout the development process using the [Live Server Extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) to test, in real time, changes made to the game and HTML page.

### Heroku

The project was deployed to Heroku using the following steps...

1.  Create a file named 'Procfile' in the project directory and paste the following code: ```web: python app.py```
2.  A requirements.txt file wsa created by using the command: ```pip3 freeze --local > requirements.txt```
3.  Log into Heroku and crete a new Heroku app.
4.  Name the app 'ci-ms3-floral-reef' and select local region.
5.  Connect Heroku to GitHub by following the on-screen prompts.
6.  Select the repository from which you want to deploy your code and click 'Connect'.
7.  Enable automatic deploys from the master branch.
8.  Go to the 'Settings' tab and reveal the 'Config Vars'.
9.  Copy the following keys and values from your 'env.py' file that was used for development and paste them into your config vars: IP, MONGO_DBNAME, MONGO_URI, PORT and SECRET_KEY.
10. The project will automatically be deployed by Heroku after a short time. A manual deployment can also be forced by clicking 'Deploy Branch' in the 'Deploy' tab.

### Roadmap

-   A system that displays the newest content at the top of the page, with a 'NEW' badge will be implemented.
-   A more sophisticated security system will be integrated into all CRUD actions and user account systems.

### Project Status

-   This project's development has paused while the grading for this project is being completed. This status will change once the course has been completed.

## Credits

### Code

-   [Code Institue - Full Stack Software Development Course](https://codeinstitute.net/): Coding skills learned in this course allowed the developer to create all the pages on this web-app.
-   [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web): Referenced for best practices for lists and images, as well as the smooth scrolling functionality.

### Content

-   The descriptions and irish names for the flowers were gotten from [irishwildflowers.ie](https://www.irishwildflowers.ie/) and [Wikipedia](https://www.wikipedia.org/).
-   All other content, unless states so, was written by the developer.

### Media

-   The Hero Image on the homepage comes from [Unsplash.](https://images.unsplash.com/photo-1511219096939-ce77f5f44cc8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw=&ixlib=rb-1.2.1&auto=format&fit=crop&w=1489&q=80)
-   The current images of the flowers, as of the time of writing, are all copyright compliant.
-   All placeholder images for the project are displaying correctly as of the date of submission. I am not responsible for any images not being loaded due to an issue on the image hosting side once this project has been submitted.

### Acknowledgements

-   My mentor, Spencer Bariball, for continuous helpful feedback and encouragement.
-   Code Institute for giving me skills to create this project.

### Support

Further information can be gotten by contacting the developer at richardbyrne1995@gmail.com
