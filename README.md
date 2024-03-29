# Scottish Private Nursery Association SPNA

The Scottish Private Nursery Association is an association for private nurseries operating in Scotland. 
The SPNA provides a body to the Private nursery owners and staff that they can rely on and to help and support when required. 
I was approached by the Client, one of the SPNA founders to see if I could make their updated website a bit more admin user friendly.

This site has been designed and created with the end user (the Client) in mind. In conjunction with the Client many new features have 
been added and some removed as the design process progressed. 

![live site screenshot](media/readme-images/live_site.jpeg)

The live site can be viewed [here!](https://scottishpna.herokuapp.com/)

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
    * [Wireframes](<#wireframes>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)
        *  [Typography](<#typography>)
        *  [Colour Scheme](<#colour-scheme>)
* [**Data Model**](<#data-model>)
* [**Design Development**](<#design-progress-notes>)
* [**Features**](<#features>)
    * [**Existing Features**](<#existing-features>)
        * [**Base Template**](<#base-template>)
            * [Navigation bar](<#navigation-bar>)
            * [Footer](<#footer>)
        * [**Home**](<#home-page>)
        * [**About Us**](<#about-us-page>)
        * [**News Page**](<#news-page>)
        * [**Initiatives and Campaigns**](<#initiatives-and-campaigns-page>)
        * [**Contact Modal**](<#contact-modal>)
        * [**Members Area**](<#members-area-page>)
        * [**SPNA Admin Page**](<#spna-admin-page>)
        * [**Profile Page**](<#profile-page>)
        * [**Error Page**](<#error-page>)
    * [**Future Features**](<#future-features>)
* [**Social Links**](<#social-links>)
* [**Business Model**](<#business-model>)
* [**Technologies Used**](<#technologies-used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
* [**Acknowledgements**](<#acknowledgements>)

# User Experience (UX)

## User Stories

As a **USER** I want to **GOAL** so that I can **RESULT**.

* As a **USER** I want to **KNOW MORE ABOUT THE SPNA** so that I can **DETERMINE IF I WANT TO JOIN**.
* As a **USER** I want to **JOIN THE SPNA** so that I can **BENEFIT FROM MEMBER PRIVILAGES**.
* As a **USER** I want to **SEE WHAT NEWS ARITCLES RELATING TO THE SPNA** so that I can **BE MORE INFORMED ABOUT THEIR ACTIVITIES**.
* As a **USER** I want to **KNOW WHAT CAMPAIGNS THE SPNA ARE INVOLVED WITH** so that I can **LEARN AND VIEW THEIR CAUSES**.
* As a **USER** I want to **KNOW WHAT INITIATIVES THE SPNA ARE RUNNING** so that I can **DO MY PART AND HELP**.
* As a **USER** I want to **CONTACT THE SPNA** so that I can **DIRECT ANY ENQUIRES APPROPRIATELY**.

* As an **ADMIN** I want to **TAKE PAYMENTS** so that I can **BUILD UP A REVENUE STREAM FROM MEMBERS**.
* As an **ADMIN** I want to **COLLECT MEMBER DETAILS** so that I can **CONTACT THEM REGARDING UPDATES AND NEWS**.
* As an **ADMIN** I want to **UPDATE THE NEWS ARTICLES** so that I can **KEEP THE WEBSITE NEWS PAGE CURRENT**.
* As an **ADMIN** I want to **UPDATE THE MEMBER DOCUMENTS** so that I can **LET THE MEMBERS KNOW THE LATEST INFORMATION**.
* As an **ADMIN** I want to **LINK TO SOCIAL MEDIA SITES** so that I can **INCREASE THE MEMBERSHIP**.

The above user stories were created in conjunction with the Client and their deveopment progress monitored in an agile environment. The project tab of github was used to help with this task. The MoSCoW method was used to define acceptance criteria for each user story. This gave some guidance as to what was going to be required at each stage of the applications development. 

[Back to top](<#contents>)

## Wireframes

* Home page 

    <details><summary>Screenshots</summary>

    ![home page wireframe](media/readme-images/home.png)
    </details>

* About Us page

    <details><summary>Screenshots</summary>

    ![About us page wireframe](media/readme-images/about-us.png)
    </details>    

* News page

    <details><summary>Screenshots</summary>

    ![News page wireframe](media/readme-images/news.png)
    </details>    

* Initiatives|Campaigns page

    <details><summary>Screenshots</summary>

    ![campaigns page wireframe](media/readme-images/init.png)
    </details>    

* Contact page

    <details><summary>Screenshots</summary>
    
    ![contact page wireframe](media/readme-images/contact.png)
    </details>

* Members page

    <details><summary>Screenshots</summary>

    ![members page wireframe](media/readme-images/member.png)
    </details>

* SPNA Admin page

    <details><summary>Screenshots</summary>

    ![SPNA Admin page wireframe](media/readme-images/spna-admin.png)
    </details>
    
* Sign Up page

    <details><summary>Screenshots</summary>

    ![Sign Up page wireframe](media/readme-images/signup.png)
    </details>
    
* Tablet Wireframes

    The SPNA website is fully responsive. There are minimal changes when viewed on a table (iPad) sized display. The major change is with the navigation bar (navbar) on the smaller tablets and mobile devices. I have attached an example wireframe of how the navbar will look on these smaller screens. 

   <details><summary>Screenshots</summary>

    ![home page tablet wireframe](media/readme-images/home-tablet.png)
    </details>
    
* Mobile Wireframes

    In addition to the above navbar there are minor differences on a few pages and I have included them below. It mainly involves the arranging of news articles and SPNA Admin forms. 

    <details><summary>Screenshots</summary>

    * News:
    ![News page wireframe](media/readme-images/news-mobile.png)

    * SPNA Admin:
    ![Admin page wireframe](media/readme-images/spnaadmin-mobile.png)

    * Member Area:
    ![Member-mobile page wireframe](media/readme-images/member-mobile.png)
    </details>

[Back to top](<#contents>)

## Site Structure

* Layout
    - The SPNA site is designed to be user friendly. All of the publically viewable pages are easily accessed from the navigation menu at the top of each page. There is an additional menu in the form of a dropdown on the right hand side of the navigation bar.
    - A non registered user is able to contact the admin of the site with the contact form.
* Access
    - To gain access to the member area and the profile page you will need to be registered and paid up. This is a process initiated from the 'Sign Up' page. This can be accessedd from the dropdown menu or the navigation bar once it has been compressed onto a smaller screen.
    - This is the only point to access the payment system. If the user navigates away from the page without completing the full process, there is no way to reinstate this and it has to be commenced from the start again.
    - Once the payment has been successfully processed the Member is then created and access is then granted to the Member Area. The Member can also view their Profile page from the dropdown menu on the right hand side of the navigation bar. They can also do ancillary tasks such as; change email address, change password, and modify their subscription (based on their experience with the current memebers, the Client doesn't expect this feature to be used but they have said that it is a nice feature to have available.). 

[Back to top](<#contents>)

## Design Choices

 * ### Typography
    - The fonts chosen for the SPNA were:
        - Title and sub title - Caveat, cursive.
        - Body is Raleway, sans-serif.
    
        These both give a relaxed and welcoming appearance to the page whilst being easily readable. 'Moon dance' was used initially as the title font but upon consultation with the client was changed to 'Caveat'.

 * ### Colour Scheme
    - The color schemes were compiled from [colorpeek](https://colorpeek.com/) based on the existing SPNA site colours with addition of some of my own from [mycolorspace](https://mycolor.space/).
    ![Color peek palate](media/readme-images/peek.png)
    ![MyColor space palate](media/readme-images/space.png)

[Back to top](<#contents>)

# Data Model
- The models are as follows;
    * Custom user model (SPNAMember)
        - Builds on the Django user model but with specific nursery, SPNA and stripe details relating to payment.
    * Plan (Plan)
        - Ensures the subscription plan details are in the backend for enhanced security (changing price, expiry etc).
    * Contact details (Contact)
        - Adds the contact details from the contact form to the database.
    * Articles (Articles)
        - Adds articles for the news page into the database.
    * Documents (Documents)
        - Adds member documents for the members' area.
  
![Data Model](media/readme-images/data-model.jpeg)

[Back to top](<#contents>)

# Design progress notes
- During the design and development phases the client had wished for the Initiatives and Campaigns page to be as one. This was easy to implement and didn't detract from other important features. They also expressed a wish for a profile page for the User to access and change their information. With further discussion we agreed a list of must have, could have and won't have features at the initial release. 
- The list comprised: Address and nursery details, subscription detail as must have. A could have feature was the ability to update payment details. These features I managed to implement and in addition, with consultation with the client I also created a way to cancel and then renew the subscription. The client liked this idea so it has remained. 
- As the project has progressed the Client and I weren't too happy with the amount of screen real estate the footer was taking up. I deceided to remove some of the elements at the screen size is reduced. It retains all of the features (minus the logo) but takes up alot less room.
- Nearing the end of development a few inefficiencies crept into the site. On the News page with lots of article there was a lot of scrolling and certainly on a mobile device this didn't create a positive experience. One way around this was to remove the scroll element and content from the articles themselves and just incorporate a button to encourage the user to click to display a modal with the full content. Similarly in the members' area the documents were often hidden and mis-represented. the user can now click on the title and the document opens in a new window. The option to download the document remains. 
- I have also added a FAQ section in the footer. This will open a modal with appropriate questions inside.
- Initially the applicataion was set up with email authentication for new members. The Client thought this wasn't appropriate for the SPNA and asked for it to be removed. I explained that the process was for security and to prevent erronious accounts,. A modified version will be reinstated in the next release.

    ![FAQ Modal](media/readme-images/faq.png)

[Back to top](<#contents>)

# Features

## Existing Features

### Base Template
- All pages contain:
  * #### Navigation Bar

    * A basic, responsive navbar is included. It contains all the pertinent pages for users, logged in users and admin.
    <details><summary>Screenshots</summary>

    * Navigation Bar
    ![Navbar](media/readme-images/navbar.jpeg)

    * Navigation Bar open
    ![Navbar Open](media/readme-images/navbar-open.jpeg)
    
    * Navigation Responsive Expanded (Admin logged in)
    ![Navbar Expanded](media/readme-images/navbar-expanded.jpeg)
    </details>

  * #### Footer
    * A basic footer showing the SPNA logo, SPNA email address for instant communications, a link to the social sites and copyright information.

### Home Page
* Contains some basic introductory information about the SPNA.
   <details><summary>Screenshots</summary>

    ![Spna Home](media/readme-images/home.jpeg)
    </details>

[Back to top](<#contents>)

### About Us page
* The About us page contains information about the SPNA. It also has an animated section on the guiding principles of the SPNA.

    <details><summary>Screenshots</summary>

    ![About page](media/readme-images/about.jpeg)
    </details>

[Back to top](<#contents>)

### News page
* Contains articles uploaded by the admin for any site user to view. The articles are informative and specific to the SPNA or early years learning. 
Each article is displayed in a card that expands into a large modal for ease of viewing when clicked on.

<details><summary>Screenshots</summary>

![News page](media/readme-images/news.jpeg)
![News article modal](media/readme-images/news-open.jpeg)
</details>

[Back to top](<#contents>)

### Initiatives and Campaigns page
* This page has all the information on the initiatives and campaigns that the SPNA are undertaking. It has a card that expands on hover for each of the initiatives and campaigns. Initially the campaigns were made to be changed frequently but on futher consultation with the client they deemed this unnessessary as there wont be many changes. 

    <details><summary>Screenshots</summary>

    ![Initiative Page](media/readme-images/initiatives.jpeg)
    </details>

[Back to top](<#contents>)

### Contact Modal
* When a User submits a contact request the application does a number of things. It logs the contact to the database for a record and it also emails the Admin with the details of the contact. Initially all contacts are marked as 'unreplied' (not replied). This gives the Admin a quick reference to see the status of the contact.
* The contact modal also holds the newsletter signup form. It isn't ideal not being initially visible on the site, however the client didn't want the newsletter form at all. This is the compromise we came up with for now. The newsletters are all managed by the admin (Client) and actioned through another email database that they have access to.

    <details><summary>Screenshots</summary>

    ![Contact Modal](media/readme-images/contact.jpeg)
    </details>

[Back to top](<#contents>)

### Members Area page
* The members' area is populated with documents that would be of interest to the members. The documents have been split into three categories (at the Client's request) to represent their type. They are, Media releases, Media mentions and Letters to and from government. The documents are visible in the browser with a pdf viewer and are downloadable.
The documents are stored in the database as an instance of a Document model and are uploaded by admin from either the SPNA Admin page (Client) or the Django admin page (Developer).

<details><summary>Screenshots</summary>

![Members area](media/readme-images/members_area.jpeg)
</details>

[Back to top](<#contents>)

### SPNA Admin Page
* The SPNA Admin page is a custom made page to enable the client to manage the site with ease. It contains all the admin features in one location for enhanced UX.
The SPNA admin page has:
    * A members list containing;
        * Full name
        * Nursery
        * Email (expandable if not visible)
        * Phone (expandable if not visible)
        * Expiry date
        * Select box (selects the member's email address and populates the 'To' field in the email interface)
    * A contact list containing;
        * Date
        * Name
        * Email (expandable if not visible)
        * Phone (expandable if not visible)
        * Message (expandable if not visible)
        * Delete button (Deletes the contact from the database)
        * Select box (selects the member's email address and populates the 'To' field in the email interface)
        - The contact list initially populates a contact with a red background signalling that the contact has not been replied to. Once an email has been send to the contact's email address through the email interface the background changes to green. This is to enhance the awareness of the admin to the contact status.
    * A button to download the members list as a CSV.
    * An email interface to allow the admin to send emails to either selected addresses or manually populated ones.
    * Add an Article (News) field
        * Title field
        * Content field
        * Image field.
    * Add a Member's document field.
        * Document title field
        * Document category selection
        * An upload field for the admin as all members' documents are produced offline in pdf format.
These features were discussed at length with the client and implemented with the optimum ease of useage in mind. This page is only visible to the admin or other superusers (currently none).

<details><summary>Screenshots</summary>

![Spna Admin](media/readme-images/spna_admin.jpeg)
</details>

[Back to top](<#contents>)

### Profile Page
The Profile page is viewable for members to view their own membership details. It contains:
    * Current Details
        * Nursery, Email, Address, Subscription and renewal date.
    * Update details 
        * A form to update Nursery, Name, Address and Phone details
        * The form has buttons to change their email and to cancel the subscription. When cancel subscription is selected it will end the access once the payment period has ended (end of the month, 6 months or year). Access to the site will be granted whilst within the payment period.
    * Change their current subscription button.
        * This form sends a request to Stripe and automatically bills the customer pro-rata.
    * Current payment card display
        * Displays the last 4 digits and expiry date
    * Update payment details form
        * Essentially creates a new payment method for the member and updates the Stripe user profile for the next billing sequence.

<details><summary>Screenshots</summary>

![Profile page](media/readme-images/profile.jpeg)
</details>

[Back to top](<#contents>)

### Error Page
There are two custom error pages. One for the 404 Page not found error and one for the 500 Server error.
They give the user notification of an error and links to all the main pages of the SPNA site.
The photo below is from the Page not found error page.
<details><summary>Screenshots</summary>

![Error page](media/readme-images/error-page.jpeg)
</details>

[Back to top](<#contents>)

## Future Features 
* The client would like to have the ability to hide the email addresses from the other members. This is something that due to currnet time contraints just wasn't possible in this release. It will be implemented in the next release. 

[Back to top](<#contents>)

# Social Links
The Scottish PNA has a Facebook business site managed my myself. [SPNA Facebook](https://www.facebook.com/ScottishPNA). It is accessible through the link in the footer. Or at the time of writing, by searching on Facebook for ScottishPNA.

![Facebook SPNA page](media/readme-images/facebook.jpeg)

# Business Model
The SPNA business model is based on a Business to Consumer (B2C) interaction. The consumer wants to become a member of the association (SPNA) to gain insight into the support available and to join an officially recognised association in the childcare field.
<br>
The membership is based on a subscription model using Stripe payments. There are three durations of membership to choose from; monthly, 6 monthly and yearly with an appropriate pricing structure. The membership is set to automatically renew at the end of the period. <br>
Through publically available records the SPNA has contacted the owners and management of Private Nurseries in Scotland to make them aware of the SPNA and encourage them to join and take advantage of the power achieved through a joint body of members. This has proven successful so far and will continue to raise the profile of the SPNA. In addition there is the Facebook page and there are plans for an Instagram page in the near future.


[Back to top](<#contents>)

# Technologies Used
* [Python](https://docs.python.org/3/contents.html) - primary language of the application.
* [HTML5](https://html.spec.whatwg.org/) - provides the content and structure for the website.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) - provides the styling.
* [Django](https://www.djangoproject.com/) - Django framework for the project.
* [Heroku](https://www.heroku.com/) - For project deployment.
* [Bootstrap](https://getbootstrap.com/) - Design toolkit.
* [GitHub](https://github.com/) - to host the repositories.
* [Gitpod](https://www.gitpod.io/) - as the IDE for the application.
* [Lucid Charts](https://www.lucidchart.com/) - to create the flow diagram and wireframes.
* [PEP8](http://pep8online.com/) - for testing and validating the code.
* [W3C Validator](https://validator.w3.org/) - test and code validation.
* [DrawSQL](https://drawsql.app/) - for the database diagram.
* [IconFinder](https://www.iconfinder.com/) - for favicon.
* [Jest](https://jestjs.io/) - Testing framework for JavaScript.
* [Facebook](https://facebook.com) - Creating the SPNA business page.
* [MailChimp](https://mailchimp.com/) - Creating the newsletter form.

[Back to top](<#contents>)

# Testing

Please refer to [**_here_**](TESTING.md) for more information on testing.

[Back to top](<#contents>)

# Deployment

### **To deploy using [Heroku](https://www.heroku.com/):**

1. Ensure your requirements.txt file has the required dependencies. To do this you can use the following code in your IDE:
    > pip3 freeze > requirements.txt
    - Heroku will use this file to import the dependencies that are required.
3. Create or Login to your Heroku account.
4. Navigate to Dashboard. 
5. Click "New" and select "create new app" from the drop-down menu. This is found in the upper right portion of the window. 
6. Provide a unique name for your application and select your region.
7. Click "Create App".
![New app image](media/readme-images/new-app.jpeg)

### **To use the Heroku Postgres database:**

1. Navigate to the "Resources" tab. Once there, in the search box type "Postgres". 
2. You will then be able to attach this to the App you have just created.
![Heroku Postgres image](media/readme-images/database-heroku.jpeg)

### Setting up the App within Heroku:

1. Navigate to "Settings" and scroll down to "config vars".
2. There are a number of config vars for this project, USE_AWS, DATABASE_URL, SECRET_KEY and numerous Stripe Variables:
    - [
        STRIPE_PUBLISHABLE_KEY,
        STRIPE_SECRET_KEY,
        STRIPE_WEBHOOK_SIGNING_KEY,
        STRIPE_PLAN_MONTHLY_ID,
        STRIPE_PLAN_SIXMONTHLY_ID,
        STRIPE_PLAN_YEARLY_ID,
    ].
3. The config vars are specific to the local project. They are usually unique and often provided by the respective API in use.
![Config Vars](media/readme-images/config-vars.jpeg)

### App Deployment:

1. Navigate to the "Deploy" section.
2. Scroll down to "Deployment Method" and select "GitHub".
3. Authorise the connection of Heroku to GitHub.
4. Search for your GitHub repository name, and select the correct repository.
5. For Deployment there are two options, Automatic Deployments or Manual.
    - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
    - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so. 
6. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire.
![Heroku deployment](media/readme-images/deploy.jpeg)

#### *App Deployment* **UPDATED** 
Heroku have recently (early 2022) changed their deployment methods due to a security breach. At the time of writing the method above was reinstated, however there is also a way to deploy using the Heroku CLI. There is more information [here](https://devcenter.heroku.com/articles/git#prerequisites-install-git-and-the-heroku-cli)

### **To fork the repository on GitHub:**
A copy of the GitHub Repository can be made by forking the repository. This copy can be viewed and changes can be made to the copy without affecting the original repository. Take the following steps to fork the repository;
1. Log in to **GitHub** and locate the [repository](https://github.com/EwanColquhoun/spna).
2. On the right hand side of the page inline with the repository name is a button called **'Fork'**, click on the button to create a copy of the original repository in your GitHub Account.
![GitHub forking process image](media/readme-images/forking.jpeg)

### **To create a local clone of this project:**
The method for cloning a project from GitHub is below:

1. Under the repository’s name, click on the **code** tab.
2. In the **Clone with HTTPS** section, click on the clipboard icon to copy the given URL.
![Cloning image](media/readme-images/cloning.jpeg)
3. In your IDE of choice, open **Git Bash**.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type **git clone**, and then paste the URL copied from GitHub.
6. Press **enter** and the local clone will be created.

### Initialising the Application locally from the clone:

* Once the clone is accessed locally you need to set up the database, create a superuser, create the environmental variables, migrate the models into the database and install the dependencies from the requirements.txt file. 
1. The default database included with Django is a SQLite variation of MYSQL. If you have preferred database you will need to edit the location of the Database in the settings file of your app.
![Database setup](media/readme-images/database.jpeg)

2. To install all the required libraries and modules for the project you will need to install those listed in the requirements.txt file. This is achieved using the following prompt;
    > pip install -r requirements.txt

3. There are a number of environmental variables for this project, API_KEY, DATABASE_URL, SECRET_KEY and the Stripe variables.
    
    To set these up locally, create a file called env.py (will contain sensitive information so ensure the data is not publically viewable). Within that file you will need to import os and create the respective variables. The variables can then be accessed within your local code.

4. Once you have the database set up you will need to mirgate the models over to it. This is done with the following command line prompts;
    > python3 manage.py makemigrations --dry-run 
    
    (optional, can be used to see what the migrations are going to be.)
    > python3 manage.py makemigrations

    > python3 manage.py migrate

5. Now you will need to create a super user to access the Admin site of Django and The Flying Scotsmen.
    Again, using the command line, enter the following and follow the prompts;
    > python3 manage.py create superuser

    It will ask you for a username and email - take note of these for future admin use.
    
6. You are set up and should be able to run the project with the following command;
    > python3 manage.py runserver

[Back to top](<#contents>)

# Credits
### Content
* The font came from [Google Fonts](https://fonts.google.com/).
* [Stack Overflow](https://stackoverflow.com/) for general hints and tips.
* The colour selection was compiled by [MyColorSpace](https://mycolor.space/) and [colorpeek](https://colorpeek.com/).
* The icons came from [Font Awesome](https://fontawesome.com/).
* Non custom code has been credited in situ.
* Highlghted navigation menu from [Stack Overflow](https://stackoverflow.com/questions/340888/navigation-in-django).
* Text from [scottishpna.org](scottishpna.org). See Plagiarism note below.

### Media
* [Unsplash](https://unsplash.com/) - Stock Nursery Photos

[Back to top](<#contents>)

# A note on Plagiarism
The project conception began when the developer was approached by the Client to produce a more user friendly version of a current website. As such, the developer has express permission of the Client to use the text from the current website. The text was written by the Client and the IP is owned by the Client. The Client specifically wanted the same text and similar color scheme on the new SPNA application.

# Acknowledgements
The site was completed as a Portfolio 5 Project piece for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/). I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/), the Slack community, and all at the Code Institute for their help and support. I would like to thank the team of testers (Family and friends, you know who you are!) for their help and and keen eye for spelling and grammar errors. I would also like to thank the Client, The Scottish Private Nursery Association for the opportunity to work on this project together.

Ewan Colquhoun 2022.

[Back to top](<#contents>)