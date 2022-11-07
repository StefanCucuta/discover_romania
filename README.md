![](screenshot/responsive.PNG)


**[LIVE DEMO - Click Here]()**


# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [UX](#ux)
    - [User Stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Features](#features)
      - [Existing Features (Photo Links)](#existing-features-photo-links)
      - [Homepage](#homepage)
      - [Navbar](#navbar)
      - [Login](#login)
      - [Logout](#logout)
      - [Posts](#posts)
      - [Register as a User](#register-as-a-user)
      - [Upload New Post](#upload-new-post)
      - [Update a Post](#update-a-post)
      - [Comments](#comments)
      - [Wish list](#wish-list)
      - [Site Admin Panel](#site-admin-panel)
      - [Future Features](#future-features)
      - [Footer](#footer)
    - [Structure](#structure)
      - [Colour Palette](#colour-palette)
    - [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
      - [Mobile](#mobile)
      - [Desktop](#desktop)
      - [Technology Used](#technology-used)
        - [Programming Languages](#programming-languages)
      - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
    - [Testing](#testing)
      - [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-ux-section)
      - [Functionality Testing](#functionality-testing)
    - [Deployment](#deployment)
      - [Deploy to Heroku](#deploy-to-heroku)
    - [Credits](#credits)
      - [Media](#media)
      - [Images, Logo and Video](#images-logo-and-video)
      - [Code](#code)
      - [Acknowledgements](#acknowledgements)


  ## Introduction
  This is a community Discover Romania Blog website that promotes Romanian places and encourage people to share their storyes and to create bucket lists. 

  ## UX
  ### User Stories 
  - As a site User I can : 
    - register an account so that I can comment and interact with the posts
    - be involved in the conversation when I leave comments on posts
    - read full text when I am pressing on post
    - select one post from the list with all posts
    - like a post and interact with the post 
    - view a paginated list of posts so that easily select a post to view
    - update my profile so that other users can view my details
    - create draft posts and writing the content later
    - create wish list in bucket list 
    - I can see my and other users wish list in bucket list 
    - make changes to the post by editing the post
    - remove / delete my post if I want
    - remove / delete a comments from posts if I want
    - upload photos to my posts
  - As a site Admin I can : 
    - edit posts so that I can make changes to the post
    - confirm to users that the post is waiting approval
    - filter, approve or disapprove comments and posts
    - manage my blog content by creating ,reading,updating and deleting posts
    - manage and interact with the blog content as a superuser 
  - As a User/Admin I can :
    - read conversations and view comments on individual post
    - view the number of likes on individual post and see which is the most popular
  

  ### Strategy 

- This is a website where users that love to travel can share photos and stories : 
   - users that want to travel in Romania
   - users that travelled already
  
  ### Scope 

  - The website provides for the user an easy navigation , photos and content with regards to location from the photos.

  ### Features

  
  #### Existing Features (Photo Links)


  #### Homepage 

  - Hompage displays the Navbar and logo, posts with description and footer with social network links.
  
     [Hompage - photo 1](screenshot/home_page1.PNG)

     [Hompage - photo 2](screenshot/home_page2.PNG)

  #### Navbar

  - In loading mode Navar displays : Home, Register and Login

     [Navbar Logged Out - photo ](screenshot/navbar_1.PNG)

  - In user logged mode Navar displays : Home, Logout and Add Post

     [Navbar Logged In - photo ](screenshot/navbar_2.PNG)

  #### Login

  - When a user presses the Login link a new section will apear at the bottom of the page where he can insert his  account details.
  
     [Login - photo ](screenshot/sign_in.PNG)

  #### Logout

  - When a user presses the Logout link a new section will apear at the bottom of the page where he is asked to confirm his action by pressing the Sign Out button .

     [Logout - photo ](screenshot/sign_out.PNG)

  #### Posts

  - There are 6 post with short content  displayed on the home page 
  - When users are adding more posts a new page will be available by pressing the Next button at the bottom of the page.
  - Confirm to users with a message that the post is waiting approval from the admin.

     [Blog Cards - photo ](screenshot/blog_cards.PNG)

  #### Register as a User

  - When a user presses the Register link a new section will appear at the bottom of the page where is asked to introduce their ditails.

     [Register as User - photo ](screenshot/register.PNG)

  #### Upload New Post

  - When a user decide to upload a new post with content and press the New post link a a new section will appear at the bottom of the page where is asked to introduce the content , to upload a photo and press the New Post button to send the post to be approved by the admin.
  - If a photo will not be uploaded a default photo (logo will appear instead).

     [Upload New Post - photo ](screenshot/new_post.PNG)

  #### Update a Post

  - When a user decide to update a post uploaded by himself and press the chosen post a new page will appear where is asked to choose to update or delete the post.

     [Update a Post - photo ](screenshot/update_post.PNG)

  #### Comments

  - When a user decide to comment a post and press the chosen post a new page will appear where has only the option to add a comment to the post.

     [Comments Section - photo ](screenshot/comments.PNG)
  
  #### Wish list

  - When a user decide to add a place where he want to go and to see othes wish list is pressing on Bucket list in the navbar.

     [Comments Section - photo ](screenshot/wish.PNG)

  #### Site Admin Panel

  - As a site Admin : 
    - I can approve or dissapprove comments or post.
    - I can create drafts and continue to add content later to the posts
    - I can edit and make changes to posts

     [Admin Page - photo ](screenshot/admin.PNG)

  #### Future Features 

  - User profile
  - Google map - location of the post
  - Link location to Trip Advisor
  - Link location to Skyscanner to book a trip.

  #### Footer

  - The footer shows the social network links and Copy Rights 
  
     [Footer - photo ](screenshot/footer.)


  ### Structure

  - Navbar is fixed on top to facilitate users to scroll the page 
  and  also have the possibility to access the links in the navbar
  - On small screens  a dropdown menu navigation will be available on all pages
  - The pages have a straightforward layout in place to ensure users can navigate easily.
    
  #### Colour Palette
 -  [Abode Color]( https://color.adobe.com/search?q=897B70&t=hex) was used to extract the main colours for the website:
  
    ![](screenshot/colors.PNG)

  ### Skeleton
  - Wireframes created with Balsamiq
  - The project was developed from initial wireframes, and some modifications were made during the development process in response to user feedback.

  #### Wireframes

  <details>

  <summary>Click to see the Wireframes</summary>

  #### Mobile


  ![Mobile](wireframes/mobile_home.PNG)

  ![Mobile](wireframes/mobile_newpost.PNG)

  ![Mobile](wireframes/mobile_register.PNG)

  ![Mobile](wireframes/mobile_signin.PNG)

  ![Mobile](wireframes/mobile_signout.PNG)

  #### Desktop

  ![Desktop](wireframes/desk_signout.PNG)

  ![Desktop](wireframes/desk_signin.PNG)

  ![Desktop](wireframes/desk_register.PNG)

  ![Desktop](wireframes/desk_hompage.PNG)
  
  ![Desktop](wireframes/desk_newpost.PNG)

  </details>


  
  #### Technology Used

  ##### Programming Languages 

  - Python
  - HTML
  - CSS
  
  #### Frameworks, Libraries & Programs Used

  - [Balsamiq](https://balsamiq.cloud/) - Was used to create the wireframes
  - [Bootstrap](https://getbootstrap.com/) - Was used to contribute to responsiveness and styling of the site
  - [TinyJPG](https://tinyjpg.com/) - Was used to compress images before uploading
  - [GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku
  - [GitPod](https://gitpod.io/) - Connected to GitHub, GitPod hosted the coding space,
   allowing the project to be built and then committed to the GitHub repository.
  - [Heroku](https://heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used 
   to deploy this project so the backend language can be utilised/tested.
  - [Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project
  - [Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.
  - [DjDatabaseURL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL 
   environment variable to configure your Django application.
  - [Cloudinary](https://cloudinary.com/) - Used to store images online for the recipe posts.
  - [Summernote](https://summernote.org/) - Used to add a text area field to the admin setup to enable 
   a list of ingredients and method steps.
  - [GoogleFonts](https://fonts.google.com/) - Provide fonts for the website.
  - [FontAwesome](https://fontawesome.com/) - Was used for icons.
  - [AmIResponsive](https://ui.dev/amiresponsive) - To check if the site is responsive on different screen sizes.
  - [Pixabay](https://pixabay.com/) and [Pexel](https://www.pexels.com/) - Were used for all the images.
  - [W3CMarkupValidator](https://jigsaw.w3.org/) - Was used to validate HTML.
  - [Coolors](https://coolors.co/) - To make color palette


  ### Testing
  - The project was manually tested by fallowing the steps :
    - Code was run trough the validator resulting no issues
    - Deploying the project from gitpod workspace trough Heroku
    - The site was also tested on I-Pad , I-Phone and Laptop.
  
  #### Testing User Stories from User Experience (UX) Section

  - All user stories in the list [above](#user-stories) has been tested and confirmed after implementation.
  #### Functionality Testing 

   - Lighthouse 
  
  ![](screenshot/accessibility.PNG)

  * HTML
  
    - No errors were returned when passing through the official [w3c html validator](https://validator.w3.org/).
  
  ![](screenshot/w3errors2.PNG)

  * CSS
  
    - No errors were returned when passing through the official [w3c jigsaw validator](https://jigsaw.w3.org/css-validator/).
  
  ![](screenshot/css_validator.PNG)

  * Accessability

    - Accessibility was tested with both Chrome Lighthouse [a11y contrast checker](https://color.a11y.com/)  and no issues were found.
    
   ![](screenshot/contrast.PNG)


  * PEP8 - No bugs found

  <details>
  <summary>Click to see the Screenshots</summary>

  ![](screenshot/pep81.PNG)

  ![](screenshot/pep82.PNG)

  ![](screenshot/pep38.PNG)
  
  </details>




  ### Deployment

  #### Deploy to Heroku 

  - To deploy this page to Heroku from its GitHub repository, the following steps were taken:
  
    - Start by installing everything in the requirements.txt file.
    - You should have the corect requirements.txt and Procfile before moving on with the deployment.
    - Log in to [Heroku apps](https://heroku.com/)
    - On Heroku page go to dashboard then to the "New" menu and choose "Create new app"
    - Create a unique name for your app , select your region and click "Create app".
    - Now the new app's dashboard is opened. Click on the resources tab.
    - Add the Heroku Postgres Add-on.
    - Go to the settings tab and reveal the Config Vars and add :
      - CLOUDINARY_URL
      - DATABASE_URL
      - SECRET_KEY
    - Click on "Deploy" and select your deploy method and repository.
    - Click "Connect" on selected repository
    - Click "Deploy Branch" in the manual deploy section. -> Heroku will now deploy the App.
  
   - Development Environment
  
    - Create an env.py that contains these variables :
      - os.environ["DATABASE_URL"] = "postgres://....."
      - os.environ["SECRET_KEY"] = ".."
      - os.environ["CLOUDINARY_CLOUD_NAME"] = ".."
      - os.environ["CLOUDINARY_API_KEY"] = ".."
      - os.environ["CLOUDINARY_API_SECRET"] = ".."
      - os.environ["CLOUDINARY_URL"] = ".."
      - os.environ["DEVELOPMENT"] = "True"
       
  
   - Create requirements.txt by typing in terminal :
      - pip3 freeze --local > requirements.txt


  ### Credits

 - [Code Institute](https://codeinstitute.net/ie/) - 'I think therefore I blog' project helped me with the fundation of the website
 - Icons were taken from Font Awesome
 - Images and video where taken from Pexel and Pixbay
 - Informational text was taken from Google
  
  #### Media

  #### Images, Logo and Video

- Images and video used were taken from :

- [Logo - photo]( )
  
- []()
  
- []()
  
- [](/)
 
- [ ]()

- []()
  
- []()
  
- []()

- All images have been resized and compressed in order to boost the UX flow.

  
#### Code

- [I Think Therefore I Blog ](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/) by Code Institute as a general resource.

- [Codegrepper](https://www.codegrepper.com/code-examples/python/jinja+get+current+url+django) as a general resource.

- [W3School](https://www.w3schools.com/) as a general resource.

#### Acknowledgements

- As usual the Slack crowd can't be thanked enough.

  [Back to the top](#table-of-contents)