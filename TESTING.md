# Testing for SPNA

## Contents

* [Code Validation](<#code-validation>)
* [Automated Testing](<#automated-testing-with-jest-and-unittest>)
* [Responsiveness Test](<#responsiveness-test>)
* [Browser Compatibility](<#browser-compatibility>)
* [Testing User Stories](<#testing-user-stories>)
* [Known Bugs](<#known-bugs>)
* [Additional Testing](<#additional-testing>)


## Code Validation
The SPNA application has be throughly tested. All the code has been run through the [W3C html validator](https://validator.w3.org/), the [W3C CSS validator](https://jigsaw.w3.org/css-validator/) and the [JavaScript JSHint validator](https://jshint.com/). 
The code passed the W3C Validator barring all the django template tags. Outside of those, no errors were found.
The CSS passed the W3C Validator with no issues.
After some minor re-formatting the scripts passed the JSHint tests. There are some warnings about unused variables, however these are related to bootstrap (see image).

* CSS Validation

![W3C CSS Validation](media/readme-images/w3c-css.png)

* Pep8 Validation for member/wh_handler.py but similar results for all custom .py files.

![PEP8 Validation](media/readme-images/pep8.png)

* JSHint results

![JSHint Validation](media/readme-images/jshint.png)

[Back to top](<#contents>)
## Automated testing with Jest and Unittest
The automated testing for The SPNA was completed using the Django built in test library Unittest, more specifically the TestCase class. The tests cover forms, models, views and other specific custom functions. Overall test coverage is at 76% for the Python based files. There are a number of lines of code associate with Stripe payments. These haven't been tested with the application as they are verified internally to Stripe.

The automated testing for the Javascript files has been completed with Jest. There are minimal custom function for the SPNA. A number of the functions are Stripe specific and as above they haven't been tested within this application. Overall the tests cover 75% of the spna_admin.js file. 

* UnitTest for Django
    * UnitTest is built into Django. The documentation is located on the [Django](https://docs.djangoproject.com/en/4.0/topics/testing/overview/#running-tests) website. There is good documentaion for coverage located [here](https://docs.djangoproject.com/en/4.0/internals/contributing/writing-code/unit-tests/#code-coverage).
    * You can run the tests from the command line with the following:
    > coverage run --source='.' manage.py test

![Unittest Validation](media/readme-images/unittest.jpeg)

![Coverage report](media/readme-images/coverage.jpeg)

* Jest for JavaScript
    * Your application needs to be set up to use Jest for testing. There is good documentation on the [Jest](https://jestjs.io/docs/getting-started) website. 
    * You can run the tests from the command line with the following:
    > npm test

![Jest Validation](media/readme-images/jest.jpeg)

[Back to top](<#contents>)
## Responsiveness Test

The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/).

|        | Moto G4 | Galaxy S5 | iPhone 5 | iPad | iPad Pro | Display <1200px | Display >1200px |
|--------|---------|-----------|----------|------|----------|-----------------|-----------------|
| Render | pass    | pass      | pass     | pass | pass *   | pass            | pass            |
| Images | pass    | pass      | pass     | pass | pass     | pass            | pass            |
| Links  | pass    | pass      | pass     | pass | pass     | pass            | pass            |

* Testing responsiveness on the iPad pro raised some bugs with the scrolling of the modals. These were rectified with some different CSS. After testing I noticed that it wasnt't just restricted to the SPNA application and many other commercial sites have similar (unaddressed) issues.

[Back to top](<#contents>)
## Browser Compatibility
* The SPNA site has been tested on Chrome, Edge, Safari and Firefox. During development the various webkits were used with the existing CSS to help prevent browser compatability issues.

[Back to top](<#contents>)
## Testing User Stories

* As a **USER** I want to **KNOW MORE ABOUT THE SPNA** so that I can **DETERMINE IF I WANT TO JOIN**.
    - These is information on the *Admin Page* and the *Home page*. If more information is required there is the *Contact form* accessible from any page. 

* As a **USER** I want to **JOIN THE SPNA** so that I can **BENIFIT FROM MEMBER PREVILAGES**.
    - There is a *Join page* with a *Sign Up* form.

* As a **USER** I want to **SEE WHAT NEWS ARITCLES RELATING TO THE SPNA** so that I can **BE MORE INFORMED ABOUT THEIR ACTIVITIES**.
    - The latest news articles related to the SPNA are on the *News page*.

* As a **USER** I want to **KNOW WHAT CAMPAIGNS THE SPNA ARE INVOLVED WITH** so that I can **LEARN AND VIEW THEIR CAUSES**.
    - As well as the *News page* there is also the *Initiatives and Campaigns page, Initiatives section*.

* As a **USER** I want to **KNOW WHAT INITIATIVES THE SPNA ARE RUNNING** so that I can **DO MY PART AND HELP**.
    - As well as the *News page* there is also the *Initiatives and Campaigns page, Campaigns section*.

* As a **USER** I want to **CONTACT THE SPNA** so that I can **DIRECT ANY ENQUIRES APPROPRIATELY**.
    - The *Contact modal* is accessible on every page of the SPNA website.

* As an **ADMIN** I want to **TAKE PAYMENTS** so that I can **BUILD UP A REVENUE STREAM FROM MEMBERS**.
    - There is a payments system setup using *Stripe* payments. It allows the User to select their desired subscription plan.

* As an **ADMIN** I want to **COLLECT MEMBER DETAILS** so that I can **CONTACT THEM REGARDING UPDATES AND NEWS**.
    - The contact details of the members are accessible via the *SPNA Admin page*. There is also a downloadable list of member details in CSV format for ease of cross application use (mail merge, spreadsheets etc).

* As an **ADMIN** I want to **UPDATE THE NEWS ARTICLES** so that I can **KEEP THE WEBSITE NEWS PAGE CURRENT**.
    - On the *SPNA Admin page* there is the ability to add an article. As a superuser the Admin also has access to the *Edit an Article page*. This allows edited articles to be uploaded.

* As an **ADMIN** I want to **UPDATE THE MEMBER DOCUMENTS** so that I can **LET THE MEMBERS KNOW THE LATEST INFORMATION**.
    - On the *SPNA Admin page* there is the ability to upload documents for the members. Documents can be deleted by the Admin on the *Members page* by the means of a button on each document.

* As an **ADMIN** I want to **LINK TO SOCIAL MEDIA SITES** so that I can **INCREASE THE MEMBERSHIP**.
    - There are social links in the *Footer* to the SPNA Facebook business page.

[Back to top](<#contents>)
## Known Bugs
* ### Resolved

    1. During testing a console error relating to 'Module is not recognised'. After some investigation it was discovered that there were incompatibility issuse with the script.js and the spna_admin.test.js files.
    <br>
    Initially I attemped to remove 'module.exports = {myFunctions}' and replace it with 'export {myFunctions}'. This removed the console error but caused the test file to fail (see next bug!).

    2. Now that the module error was removed. The next task was to get the spna_admin.test.js file to run and pass all tests. This was a bit more complicated, the problem seems widespread and the fixes seem very dependent on the rest of the code setup. After trying numerous 'fixes' ranging from renaming the .js files to .mjs files to setting up jest.config.js files.
    The ultimate fix in this case was to create a babel.config.js file and to include the following;
    <br>
    <br>

    > // babel.config.js //
        module.exports = {
        presets: [
            [
            '@babel/preset-env',
            {
                targets: {
                node: 'current',
                },
            },
            ],
            ["@babel/preset-react"],
        ],
        };

    The issue seems to stem from the transferring of the common JS into a format readable by ES Modules. Jest/Babel seems to need configuring to accept the ES6 variation of JS.

    3. During testing there were a number of issues found with the summernote field on the contact form. To enhance page loading speeds and limit requests from the AWS S3 daatabase it was deceided to replace the summernote field with a regular text field on the contact form. This has minimal impact for the user but greatly enhances the efficiency of the application.

* ### Unresolved
    1. There is a known bug when initially signing up. Once the signup and payment are completed the user is redirected to the 'home' page. As they are paid and authenticated the menu link to the members area should be visible in the NavBar. It isn't visible until the page is reset. As a short term workaround there has been another link to the Members' area in the dropdown mini menu in the top right of the page.
    2. The second unresolved known bug is one on the profile page. When the user has a card that requires 3d Authentication the changing subscription and the update payment card views currently can't handle this. This is a fairly major limitation for certain cards but due to external factors with the application this hasn't been able to be resolved at this release. The main payment card page can accept 3d auth payments.

[Back to top](<#contents>)
## Additional Testing
### Lighthouse
The site was also tested using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Developer Tools to test each of the pages for:
* Performance - How the page performs whilst loading.
* Accessibility - Is the site acccessible for all users and how can it be improved.
* Best Practices - Site conforms to industry best practices.
* SEO - Search engine optimisation. Is the site optimised for search engine result rankings.

Here are the results from SPNA Application test;
 - The lower result for best practices appears to be caused by some external errors logged within google chrome issues panel.

![Lighthouse home](media/readme-images/lh.png)

<br>
This part of the testing process showed up that the site was slow to load. All the images were compressed and the 'prefetch' function was added to the link elements in the head of the BASE.html This sped up the loading time and increased the performance rating.

### Peer review
The SPNA site has been tested by many peers. Thank you to them all. They pointed out many bugs relevant to the specific device types and browsers they were using.

Back to [README.md](./README.md#testing).


[Back to top](<#contents>)