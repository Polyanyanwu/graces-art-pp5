# **GRACES ART PRINT WEBSITE**

The Graces Art Print is a web application that enables users to purchase an artwork and frame for printing. The purchased artwork and frame would be used to produce a framed artwork delivered to the user's supplied address.  

![Graces Art Print](/docs/images/graces_art_main.png)

## Live Site

[Graces Art Print Live](https://graces-art.onrender.com)

For purposes of payments on this project the use of Stripe's test functionality is implemented. It is not intended to collect real live payments.
You can make use of the following test card details to make payments on the site:

| NUMBER                | BRAND            | CVC          | DATE            | ZIP CODE     |
| --------------------- |----------------- | ------------ | --------------- | ------------ |
| 4242424242424242      | Visa             | Any 3 digits | Any future date | Any 5 digits |
| 5555555555554444      | Mastercard       | Any 3 digits | Any future date | Any 5 digits |
| 378282246310005       | American Express | Any 4 digits | Any future date | Any 5 digits |

## Repository

[View Repository Here](https://github.com/Polyanyanwu/graces-art-pp5)

## Table of Contents

- [**GRACES ART PRINT WEBSITE**](#graces-art-print-website)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Table of Contents](#table-of-contents)
  - [**Objectives of the Site**](#objectives-of-the-site)
  - [**User Experience Design**](#user-experience-design)
    - [**Initial Design Features**](#initial-design-features)
      - [**User Interaction**](#user-interaction)
    - [**User Roles**](#user-roles)
      - [**A. Admin user**](#a-admin-user)
      - [**B. Operator**](#b-operator)
      - [**C. Public**](#c-public)
    - [**Agile Initiative**](#agile-initiative)
      - [**Epics**](#epics)
    - [**User Stories**](#user-stories)
    - [GitHub Projects](#github-projects)
    - [**Wireframes**](#wireframes)
    - [**Color Scheme**](#color-scheme)
    - [**Fonts**](#fonts)
  - [**Database Design**](#database-design)
  - [**Flowchart**](#flowchart)
  - [**Technologies Used**](#technologies-used)
    - [**Frameworks and Libraries**](#frameworks-and-libraries)
    - [**Ancillary Technologies**](#ancillary-technologies)
    - [**VSCode Extensions Used**](#vscode-extensions-used)
  - [**Search Engine Optimization**](#search-engine-optimization)
    - [**Keywords Research**](#keywords-research)
  - [**E-commerce Business Model**](#e-commerce-business-model)
    - [**Web Marketing Strategies**](#web-marketing-strategies)
      - [**Search Engine Optimization (SEO)**](#search-engine-optimization-seo)
      - [**Content Marketing**](#content-marketing)
      - [**Social Media**](#social-media)
      - [**Email Marketing**](#email-marketing)
      - [**Paid Advertising and Influencer Marketing**](#paid-advertising-and-influencer-marketing)
    - [Facebook Page](#facebook-page)
  - [**Features Implemented**](#features-implemented)
    - [**Sign Up \& Login**](#sign-up--login)
      - [Reset Password](#reset-password)
      - [Update Email Address](#update-email-address)
    - [**The Landing Page**](#the-landing-page)
    - [Public User Functionalities](#public-user-functionalities)
      - [**List of Artworks**](#list-of-artworks)
      - [**Artwork Details**](#artwork-details)
      - [**Shopping Bag**](#shopping-bag)
      - [**Discount Vouchers**](#discount-vouchers)
      - [**Checkout/Payment**](#checkoutpayment)
    - [**My Account Menu**](#my-account-menu)
      - [My Profile](#my-profile)
      - [Order History](#order-history)
      - [Return Order](#return-order)
      - [Cancel Order](#cancel-order)
      - [My Wishlist](#my-wishlist)
      - [Notifications](#notifications)
    - [Operator User Functionalities](#operator-user-functionalities)
      - [Update Order Status](#update-order-status)
      - [Review Return Order](#review-return-order)
      - [Order Details List](#order-details-list)
    - [Administrator User Functionalities](#administrator-user-functionalities)
      - [Maintain General Information](#maintain-general-information)
      - [Maintain System Preferences](#maintain-system-preferences)
      - [Assign User Roles/Groups](#assign-user-rolesgroups)
      - [Maintain FAQs](#maintain-faqs)
      - [Maintain Artists](#maintain-artists)
      - [Maintain Art Styles](#maintain-art-styles)
      - [Maintain Art Genre](#maintain-art-genre)
      - [Add Artwork](#add-artwork)
      - [Edit / Delete Artworks](#edit--delete-artworks)
      - [Maintain Art Frames](#maintain-art-frames)
    - [The Footer Information](#the-footer-information)
      - [Newsletter Subscription Form](#newsletter-subscription-form)
      - [Contact Us](#contact-us)
      - [Reviews](#reviews)
    - [Future Features to Implement](#future-features-to-implement)
  - [**Testing**](#testing)
  - [**Bugs**](#bugs)
    - [**Current Bugs**](#current-bugs)
    - [**Resolved Bugs**](#resolved-bugs)
  - [**Deployment**](#deployment)
  - [**Credits**](#credits)
    - [**Content**](#content)
    - [**Code**](#code)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

## **Objectives of the Site**

The site has objective of providing easy to use application for selection of famous artwork images for printing. The user desires to select an artwork, chose a frame and size for the production, view the resultant cost of the artwork and get the produced work shipped to the desired location. The site owner wants to manage available frames, receive online payments for the user choices and ship the artwork once it has been produced. The application will provide historical and statistical reports to the validated user, the operator and the admin user.

## **User Experience Design**

### **Initial Design Features**

- The application will enable the user to select an artwork to print based on various criteria – genre, artist, style or generally by the name of the artwork.
- Different frame types will be displayed for the user to choose from.
- The print sizes will be listed to enable the user indicate the preferred print size.
- The quotation for the print is generated automatically after factoring in the frame and size of the picture.
- A shopping bag and wish list are maintained for the user. An item could be moved to the shopping bag from the wish list.
- A checkout process will enable the user add the delivery details, discounts applied where available and final cost to pay is determined. When payment is received, an email is sent to the user confirming payment and providing details of expected delivery date depending on shipping method selected.
- An order could be canceled before shipment and within a specified period. After the given period the order can no longer be cancelled. Defective prints could be returned and replaced within a given period at no extra cost to the customer.
- The item is marked as shipped by the site operator when shipped, and updated as delivered by the site operator when customer has received the item (name and date/time is entered to indicate who received the item).
- Authenticated customers can view messages and alerts sent to them regarding progress of their order and could choose to archive or delete such messages.
- Discount Vouchers are available to:

1. A given percentage to first time visitors who registers with the site and chose to complete a purchase.
2. Customers who purchase items above a stated sum of money.
The vouchers will be applied at checkout.

- The access to the application will be role based and user views only menu options that are available to the assigned role for the user.
- Product ratings will display besides the product listing. Clicking on the ratings will navigate the user to the testimonials for details of customer ratings on our services. Only customers that have purchased an item previously are permitted to write reviews.
- The Site Administrator will be able to add or delete an artwork; add, delete and update quantities of frames available for print job. A customer may not select a frame that is out of stock.

#### **User Interaction**

- A user will need to login to complete a purchase. Initially the artwork and shopping bag will be available. User could decide to put items into the shopping bag first but to complete the purchase, the user needs to create an account and provide delivery address.
- An email address and password would be sufficient to create an account, but the email has to be confirmed. A user remains signed in until user choses to sign out, in line with current UX design.
- When a user places an order successfully, it will appear on the order list, any cancellation will appear on the update messages dropdown.
- Confirmation of order, cancellations or request for return will fire an email to the user informing them accordingly. Admin could disallow a return of a delivered artwork giving the user valid reasons for the refusal.
- Login button will change to Logout when a user successfully logged in. The name of the logged in user will be displayed.

Please note the slight change in implementation of user interaction to allow anonymous user to complete an order instead of requiring login as initially designed. However, full benefits come with logged in users.

[>> Bact to TOC](#table-of-contents)

### **User Roles**

There shall be three roles for the application:

#### **A. Admin user**

1. Assign user role to signed-in users
2. Set system preferences
3. Update order status – change status to shipped after artwork has been shipped or delivered after customer has received artwork
4. Maintain artwork, add/delete artwork, add/delete genre, add/delete artist, add/delete art styles.
5. Maintain frame types and quantities available
6. Maintain discount vouchers and percentage discounts on them
7. Maintain reason for return of order
8. Maintain reason for cancellation of order.

#### **B. Operator**

1. Review request for return of artwork and take action.
2. Update order status – change status to shipped after artwork has been shipped or delivered after customer has received artwork
3. Enquiry on the details of orders for a given period

#### **C. Public**

1. Sign-in to the site
2. Make orders
3. Cancel orders
4. Enquiries on order history
5. Return defective prints
6. View/delete messages

Only the Admin will use the Admin portal, while Operator and Public will use the application main page. Accessible menu items will depend on the role assigned to the user by the administrator.

[>> Bact to TOC](#table-of-contents)

### **Agile Initiative**

The project will consist of one initiative which is to provide an intuitive user-friendly online store for the sale of artwork to the public.

#### **Epics**

The functionalities in the application shall be provided through two user epics:

1. The application shall provide a role-based access control enabling users to register with the site, maintain passwords, and possibly integrate with social media for authentication.
2. The application shall provide online selection of artwork, frame and dimension for the printing of the work and delivery to the user after payment.

### **User Stories**

The User Stories for the application was developed before commencement of the application and guided the process. The User Stories were entered as Issues on GitHub repository for the application and used to guide the management of the project. The User Stories were grouped into four:

- Customer Stories
- Operator Stories
- Authentication stories
- Site Owner/Admin stories
  
Detailed User Stories are [provided HERE](/docs/user_stories.md)

### GitHub Projects

Two projects were used in the GitHub to manage the project. There were two iteration timeboxes implemented with Milestones/Sprints of two weeks duration each. The links to the projects are given below:

[First Iteration: Graces Art](https://github.com/users/Polyanyanwu/projects/6)  
[Final Iteration: Graces Art](https://github.com/users/Polyanyanwu/projects/7)

MoSCow prioritization was used and the User Stories were categorized into "Must Have", "Could Have" and "Should Have". The categories were implemented as labels on GitHub.

Major bugs encountered in the course of the development were raised on GitHub as issues and closed when resolved.

[>> Bact to TOC](#table-of-contents)

### **Wireframes**

Wireframes were designed at the onset of the project and guided the development of the application. The full wireframes are [provided HERE](/docs/wireframe.md)

### **Color Scheme**

In order to enhance the user experience and have consistent look and feel throughout the website, I chose a color scheme through the [Colors.co](https://coolors.co/). The color palette used is shown below:

![Color Pallet](/docs/pp5_color.png)

### **Fonts**

The font for the website is "Exo" and "Edu NSW ACT Foundation', cursive", which was chosen from [Google fonts](https://fonts.google.com/specimen/Exo?query=exo). This font looks great to me for a website where the user need not struggle to see details of the site. THe Edu cursive was used for the logo and banner while the Exo was used for the body.

![Font](/docs/pp5_fonts.png)

## **Database Design**

The database used in this project is a relational database, Postgres provided by Heroku.

The initial design database Entity Diagram is given below:

![Database Entity Diagram](/docs/graces_art_ed.png)

There were few modifications to the initial database model leading to the final implemented model shown below:

![Final Entity Diagram](/docs/graces_art_db.png)

## **Flowchart**

The initial flowchart for the user interaction with the website has been produced to guide the application development. As the site unfolds, it may differ slightly as requirements may change in the course of development.

![Flowchart](/docs/graces_art_flowchart.png)

Please note the slight change in implementation of the flowchart to allow anonymous user to complete an order instead of requiring login as initially designed.

## **Technologies Used**
  
  The main technologies used are:

  1. Python3 (Django is a framework based on Python, which was used extensively in the views to deliver the application logic)
  2. HTML (used to display the pages - Django templates make use of HTML)
  3. Jinja template language
  4. CSS (used in styling some of the HTML)
  5. Javascript

### **Frameworks and Libraries**

- Django framework, which is a very powerful open source project. The documentation of Django is on the [Official Django Site](https://www.djangoproject.com/).
- [Django Allauth Package](https://django-allauth.readthedocs.io/en/latest/installation.html) was used for the user signup, password management and related functionality.
- [Bootstrap V5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/) was used in styling and positioning the HTML elements on the pages.
- [jQuery 3.6](https://jquery.com/) for rendering the modal confirmation of actions on the application and the checkout page.
- [Font Awesome - fontawesomefree V 5.15.3](https://fontawesome.com/) was used to deliver the icons in the pages.
- [Stripe Payments infrastructure for the internet](https://stripe.com/en-ie) enabled use of their test payment system for this development.
- [Amazon S3 Object Storage](https://aws.amazon.com/s3/) was used in rendering static files and images on the website.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/)  which is a collection of custom storage backends for Django enabled connecting to the Amazon S3 storage.
- [Boto3 Amazon SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Strip](https://dashboard.stripe.com) was used for card payment collection.
- [Summernote](https://summernote.org/) enabled the Admin to create WYSIWYG Terms of Use, Privacy Policy, FAQ, landing page message, About Us, etc which makes them become dynamic and loaded form database records.
- [Django Crispy Forms)(https://django-crispy-forms.readthedocs.io/en/latest/) was helpful to display some of the forms on the pages.
- [Dj-database-url](https://pypi.org/project/dj-database-url/) assisted with accessing the database.
- [Psycopg2](https://pypi.org/project/psycopg2/) was the PostgreSQL database adapter for the Python programming language that was used in the project.
- [Django Extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html) enabled auto generation of database model graph.
- [Graphviz](http://www.graphviz.org/) and Pydoc used to generate database model graph

### **Ancillary Technologies**

- [Balsamiq](https://balsamiq.com/) was used to create  the Wireframes for the application.
- [Google Fonts](https://fonts.google.com/) was used for the fonts in the application.
- [TinyPNG](https://tinypng.com/) for resizing all the images.
- [Am I Responsive](https://ui.dev/amiresponsive?url=https://graces-buffet.herokuapp.com/) was used to create the Mockup image at the top of the README.
- [PEP8 validation](http://pep8online.com/) : A Python code online validation application.
- [JShint](https://jshint.com/) : for validation of the Javascript used.
- [W3C Markup Validation Service](validator.w3.org) : A free application that was used to check the HTML and CSS files for errors.
- [Visual Studio Code](https://code.visualstudio.com/): The code editor used for the application development. With numerous [extensions](#vscode-extensions-used) available it is an excellent environment for writing efficient codes.
- [Git](https://git-scm.com/) : For Version control.
- [GitPod](https://www.gitpod.io/) : the Integrated Development Environment.
- [GitHub](https://github.com/)  for hosting the repository.
- [Heroku](https://www.heroku.com/home) : hosting the live website.

### **VSCode Extensions Used**

Some VSCode extensions were used during the development of the application. They are:

- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)
This extension assisted to give meaningful messages on the Python code regarding structure and syntax.
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
This assisted with production of this README with Table of Contents in particular.
- [markdown lint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
This extension assisted with the structure of README content.
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
This was very useful to check spelling errors in the code.

[>> Bact to TOC](#table-of-contents)

## **Search Engine Optimization**

### **Keywords Research**

I initially did a brainstorming session and listed the following keywords I consider relevant to the application for the purpose of search engine optimization.

- Art gifts
- Printed arts
- Classical artwork
- Print classical artwork
- Buy printed artwork
- Buy classical printed artwork

I then went to Google and looked up the above keywords and got suggestions while typing. Also considered the  “People also ask” and “Related searches”  sections on the google results page and came up with the following keywords:

- Artwork for sale
- Print ready artwork
- Buy album artwork
- Buy printed artwork
- Where can I buy art prints for sale?
- Buy classical art
- Classical art prints
- Classical art prints framed
- Famous art prints
- Famous paintings
- Buy prints of famous artists
- Framed prints online Ireland

The next step was on [WordTracker](https://www.wordtracker.com/)  to have a feel of the relevance and authoritativeness of the data available on keyword volume and competition.

I searched “classical art”,  “art print” and “famous paintings” on [WordTracker](https://www.wordtracker.com/) and came up with the following considering the volume and competition:

![WordTracker Result](/docs/seo_keywords.png)

- Classical art
- Classical artwork
- Framed prints
- Art print
- Framed photos
- Famous painting
- Famous artist

In view of the above, my keywords for the Graces Art Prints website is given below:

| Short-tail Keywords            | Long-tail Keywords                      |
|--------------------------------|-----------------------------------------|
| Classical art prints           | Framed photos of classical art          |
| Classical artwork              | Buy prints of famous artists            |
| Famous artists                 | Framed classical art prints             |
| Famous paintings               | where can I buy classical art in Dublin |
| Buy printed artwork            | Buy classical art printed               |

The above keywords would be included in the meta of the website and be considered in the relevant pages as they form the core of the product that is being marketed by the website.

## **E-commerce Business Model**

The business is an online shop where users browse and select classical artwork and a frame to print the artwork on. The shipping cost is a percentage of the total but has an upper limit. There are selected items on sale at each time available at the Sales page that has link visible at all pages. There are also discount codes which any visitor to the site can download and use at checkout. The footer contains links to information about us, frequently asked questions and other relevant information including a Mailchimp email subscription form. We intend to take online orders, produce the work and ship to customers.

### **Web Marketing Strategies**

I considered different approaches to web marketing and visited sites of similar online shops taking cognisance of the Code Institute course notes on WEb Marketing. Below is my marketing strategies.

#### **Search Engine Optimization (SEO)**

The e-commerce business is an online retail type and search engine optimization will enable users easily find it online. I researched on relevant keywords for the business and developed both short-tail and long-tail keywords that was included at the header of all the pages and in the relevant content. For example I included the keywords “classical art framed”, “famous artists” in the welcome message on the landing page.

#### **Content Marketing**

Providing enticing content to my prospects is very essential since my customers are lovers of art and beauty. I intent to record videos of previous work done by the company and some on the production process.  These videos would be made available through the Facebook and YouTube pages to reach a greater audience. Pages on the website could also have such information for visitors. The site runs sales most of the time. The items on sale are available via a click of a link on all pages. Discounts vouchers are available for all users to view and copy from the site.

#### **Social Media**

The business will use organic social media marketing as it is quite suitable for new businesses like this that is digital online shop. This will enable the business interact with prospects and put a human touch to the marketing effort. The site has a [Facebook page](https://www.facebook.com/Graces-Art-Print-110351491783521), which will be monitored for users comments and feedback and responded to accordingly. If short videos or images of latest work work are produced at any time, it will be posted on the Facebook page. Additionally, the business will use WhatsApp platform to chat with users that need special attention or clarifications. When the business picks up paid Facebook promotions will be added.

#### **Email Marketing**

The business will use email marketing and is collecting email addresses on the website using the Mailchimp plugin. Emails will be sent to subscribers as the need arises and when new offers are available. To avoid spam, the emails will not be too frequent.

#### **Paid Advertising and Influencer Marketing**

Paid advertising and influencer marketing is not part of the strategy at the beginning since they could be expensive to run. Moreover the target customers may not be influenced by paid adverts or someone else saying much about us and our products. What will speak more for the business is showcasing previous work on videos, images on social media and web pages where customers could be attracted watching such content.

Affiliate marketing is not feasible at the onset. However, I have included link to another online shop [(BGA)](https://www.bgastore.ie/) where our users can see other frame options. As the business unfolds, we can earn commission from such referral and also engage that organization to refer people to us for print jobs.

### Facebook Page

A Facebook business page was created for the e-commerce business available at [Facebook](https://www.facebook.com/Graces-Art-Print-110351491783521). The Facebook page features the logo, landing page, link to the website, location city of the business, brief description of the business where some of the keywords were used. The type of business was put as Arts & Crafts and an initial post introducing the business was made. Find below screenshots of the Facebook page.

![Facebook Page1](docs/facebook1.png)

![Facebook Page2](docs/facebook2.png)

## **Features Implemented**

The website enables visitors order the printing of artwork using desired frame. Although it is not required to sign-up with the website to complete a purchase, functionalities like "Return or Cancellation of Order" requires a login at the time of ordering. To login successfully a user need to sign-up with a valid email address. There are three roles for the application public, operator and administrator. We shall discuss the features under these three roles in addition to the sign up process.

### **Sign Up & Login**

When the website opens to a new user, My Account and bag icon is displayed on the right edge. Clicking the My Account will open the menu having "Register" and "Login" items.
![Signup](/docs/images/welcome.png)

Click on the Register menu item will display the "Create an Account" page where the user details and email are inputted. All the fields are required and the email will be verified before a user is able to login.

![Register Profile](/docs/images/register.png)

Once the form is completed, the user is informed that an email has been forwarded to the given address for verification. The email will usually be received within few minutes depending on the network situation.

![Verify Email](/docs/images/verify_email.png)

Clicking on the link provided in the email verification will direct the user to a page to click to verify the email. Once the user clicks on the Confirm button, the user is routed to the Login page.

The user can login with either the username or email address provided during the register account. If the credentials inputted are correct, an acknowledgement of the successful login is given at the top right edge. My Account icon only will display if the user is public or My Account and Admin/Ops icon is additionally displayed if the user belong to the Administrator or Operator group.

![Success Login](/docs/images/success_signin.png)

If the username/email and password provided do not match, a message is displayed to the user and login is not permitted.

[>> Bact to TOC](#table-of-contents)

#### Reset Password

From the "My Account" menu, the user can select "Reset Password" which opens a form for the user to enter the email address and click Reset My Password button.
![Reset Password](/docs/images/password_reset_input.png)

The user will receive a confirmation message that the password reset link has been sent by email and will follow the instructions to complete the password reset.

![Reset Password Confirmation](/docs/images/password_reset.png)

#### Update Email Address

From the "My Account" menu, the user can select "Update Email" and the E-mail Addresses page will open with a list of all email addresses associated with the user account. The user can add additional emails or remove.

![Update Email](/docs/images/add_email.png)

If the email to add is already in use by any user in the system, the addition is disallowed with an error message. If the email address is okay, an email is sent to it for the user to confirm.

Clicking on the link in the email sent will open a page for the user to click "Confirm" after which the email is added in the list of the users email and could be used as username to login to the application.

### **The Landing Page**

The landing page of the website presents the user with a welcome message and Shop Now button. The footer section shows four columns: Information (about us, FAQ, Contact US, and Reviews); the Legal colum has Terms & Conditions and Privacy Policy. The Social Media column has links to Facebook page of the website, the Github page of the developer and an Instagram icon not linked yet. The right edge has the "My Account" only for public users or "My Account" and "Admin/Ops" for Administrator and Operator group members.

![Public User Welcome](/docs/images/main_page.png)

 In addition dropdown menus give the user the option of browsing the collection of artworks. Clicking the "All Products" dropdown menu will display the options for sorting By Price, Rating, Style or All Artworks without sorting. Clicking on the Artist dropdown menu will give a list of all artist whose artworks are being sold. The list is dynamically generated from the database. Clicking on the Genre dropdown menu will present all art genre for the user to select the one of interest. Selecting any of the sort or filter categories will display a page of the artworks meeting the selected criteria.

 On the landing page too is the Discount coupons and Sales menu items. Clicking the Discount Coupons will open a page where the user can copy the relevant discount coupon that could be used on the site. The coupons could also be displayed by clicking the banner thats speaks to "Fabulous discounts.." on all pages.

A "search artwork by name" form is at the top for the user to enter any substring of the artwork name or the artist name and have the site respond with a page containing the list of artworks matching the entered criteria.

![Public Menu Items](/docs/images/public_menu.png)

### Public User Functionalities

#### **List of Artworks**

After a user has clicked on any of the menu items (All Products, Artist, Genre or Sales) or inputted and clicked on the search icon, a list of matching artworks are displayed to the user.

![Artwork List](/docs/images/artwork_list.png)

Each artwork has an image, the price, artist, genre, style and store rating of the artwork. If the user is in the administrator group, an Edit/Delete link is visible and could direct the administrator to the edit/delete artwork page. Artworks that are on sale have the original and sale price displayed side by side.

The artworks displayed could be sorted by clicking on the "Sort by.." dropdown list. The options are as shown below:
![Artwork Sort Criteria](/docs/images/sort_main.png)

Selecting any of the sort criteria will sort the displayed artworks accordingly.

#### **Artwork Details**

Clicking on the artwork image displayed in the list of artworks will open the detail display where the user is able to select a frame to use for the printing job.
Selecting a different frame recomputes the total cost taking note of the quantity selected. The user can change the quantity or frame before choosing to click on "Add to Bag", "Add to Wishlist" or "Keep Shopping". Clicking on wishlist will add the artwork to the users wishlist if the user is logged in, if not a message is given to the user that "You need to login to use this feature".

![Artwork detail](/docs/images/artwork_details.png)

Clicking on "Keep Shopping" will return the user to the list of artworks. Clicking on "Add to Bag" will add the artwork with the chosen frame to the shopping bag and display a summary of the current contents of the bag. Validations are executed to ensure user doesn't add artwork with no frame. The quantity is 1 by default.

![Add to Bag Success](/docs/images/add_bag_success.png)

The summary bag shown above has an advise at the bottom for the user to buy more and qualify to use discount voucher or if the total is already above the discount voucher minimum, a reminder to use the voucher at checkout is given. The bag also has the delivery cost computed and displayed. The delivery cost maximum is setup by the Admin in the config (System Preferences). The bag icon at the top right edge of the page will display the total cost of existing items in the bag at anytime. The color of the icon will change from grey to orange-red when the bag total is greater than zero.

#### **Shopping Bag**

The shopping bag keeps track of artwork and frame that a user has added to the shopping bag. It could be accessed either from the artwork details page (by clicking an artwork from the list) or clicking on the bag icon at the top right edge of every page. If the bag has no items in it clicking the bag icon will display the Shopping Bag page with the message "Your bag is empty" and a button for "Keep Shopping"

If the bag has items in it the shopping items are displayed with the artwork, frame, quantity and sub-total of each line item. A user may decide to change the frame or quantity, move the artwork to wishlist or remove the artwork and its line items from the shopping bag.

![Shopping Bag](/docs/images/shopping_bag.png)

If the artwork is moved to wishlist or removed, the line item will be removed from the shopping bag. Below the line items, the total price, delivery cost and Grand total is computed and displayed. A message reminding the user to get discount voucher if the shopping is above the threshold amount is displayed or a message suggesting increasing the shopping to reach the discount threshold is displayed.

The user may finally opt to "proceed to checkout" where payment is made and the order is placed or click on "keep shopping" to return to the artworks list.

#### **Discount Vouchers**

The site provides discount coupon codes that the user can copy available either by clicking the banner or the discount link on the menu bar. 

![Discount Codes](/docs/images/discount.png)

The code is used at checkout to obtain necessary discounts.

#### **Checkout/Payment**

The Checkout page opens when a user clicks "Proceed to Checkout" from the Shopping Bag page or from the Add to Bag success summary display. The checkout page invites the user to fill out the form for the delivery details and the card number for the payment. The discount field is also open for the user to put a discount code copied from the discount available at the banner of every page. If the discount code is correct and the conditions are met, the discount is applied.

![Checkout](/docs/images/checkout_login.png)

Two types of discount codes are published on the site - a welcome code usable only once and a threshold code for purchases up to an amount set by the administrator of the site. Validation is done for correctness of the code and the limits and appropriate messages displayed to the user.

If the user logged in, a checkbox is available under the delivery details for the user to request updating the details on the profile with the information entered on the form. If the user is not logged, a link is provided requesting the user to create an account or login to save the delivery information.

![Checkout Not Logged in](/docs/images/checkout_no_login.png)

To make payment the user will enter data in all the mandatory fields, which are indicated by a * in the placeholder of the fields. To test the payment flow use the Stripe test card "4242 4242 4242 4242", enter a month and year in future and 5-digit usa zip code. The payment will be accepted and a confirmation page is displayed.

![Successful Checkout](/docs/images/checkout_success_msg.png)

An email is also forwarded to the email address filled on the checkout details. The Notifications is updated if the user logged in during the order placement process.

If there are errors on the card, it is displayed under the card for the user to see and correct.
E.g "Your postal code is incomplete", "Your card number is invalid", etc

### **My Account Menu**

Apart from the shopping and checkout described above, the logged in user has other features accessible through the My Account menu shown below:

![My Account Menu](/docs/images/public_dropdown.png)

#### My Profile

Clicking on "My Profile" will open the Update Your Profile Details form.

![Profile Details Form](/docs/images/update_profile.png)

The form gives the user the ability to update contact information that will be suggested by default during checkout. Click "Save" button to save the details entered or cancel to return to the landing page or any menu item to navigate elsewhere.

#### Order History

The logged in user can select "Order History" from the "My Account" menu and a list of the orders placed by the user is displayed.

![Order History](/docs/images/order_history_public.png)

The user can filter the list by date, order number, status or artwork/frame name. Pagination is provided to navigate between pages of the list where there is enough orders for that. Apart from the order number that is unique and returns a single record where it exists, the user can combine any of the other filter criteria like date and status.

#### Return Order

The logged in user can select "Return Order" from the "My Account" menu and the "Request Return Order" page opens.

![Customer Return Order](/docs/images/request_return_order.png)

A list of existing orders for the user is displayed with only orders that have status as "Ordered". The list could be filtered by Order Number, Email or Order date.

Orders can only be returned before a given number of days has elapsed. Selecting an order that is no longer within the date will display an error message informing the user that they can no longer return the order.

![Customer Return Order Feedback](/docs/images/return_feedback.png)

Click on the select button to load the Order details on the left side of the page and afterwards enter the reason for the return and click "Send Request". A success message is displayed and an email is forwarded to the user's email.
The request will be reviewed bya user with Operator group membership and email sent to the user with instructions on returning the order.

#### Cancel Order

The logged in user can select "Cancel Order" from the "My Account" menu and the "Cancel Order Request" page opens.

![Customer Cancel Order](/docs/images/cancel_order_req.png)

A list of existing orders for the user is displayed with only orders that have status as "Ordered". The list could be filtered by Order Number, Email or Order date.

Orders can only be cancelled before a given number of days has elapsed. Selecting an order that is no longer within the date will display an error message informing the user that they can no longer cancel the order.

![Customer Return Order Feedback](/docs/images/cancel_order_feedback.png)

Click on the select button to load the Order details on the left side of the page and afterwards enter the reason for the cancellation and click "Send Request". A success message is displayed and an email is forwarded to the user's email and the order will be cancelled.

#### My Wishlist

The logged in user can select "My Wishlist" from the "My Account" menu and the "My Wishlist" page opens. It displays a list of all artworks the user has added to the wishlist either from the Artwork Details page or the Shopping Bag.

![Wishlist](/docs/images/my_wishlist.png)

The user can delete any item from the wish list after confirming Okay when the confirmation modal window opens following clicking the "Delete" button beside a wishlist item.

#### Notifications

The logged in user can select "Notifications" from the "My Account" menu and the "My Notifications" page opens. It displays a list of copy of emails regarding return and cancellation of orders and an acknowledgement that order was placed or order status changed.

![Notifications](/docs/images/notifications.png)

The user can delete any item from the Notifications after confirming Okay when the confirmation modal window opens following clicking the "Delete" button beside a notification item.

### Operator User Functionalities

Apart from the "My Account" menu available to all users of the application, the user that belongs to the Operator group has access to the "Admin/Ops" menu and under the menu the user can:

1. Update Order Status
2. Review Return Order
3. Order Details List

#### Update Order Status

Selecting this menu option from the Admin/Ops menu will display a list of all existing orders. The list could be filtered by Order Number, Email, Status, Order Date, artwork/frame name and any one or more combinations of the criteria.

![Update Order Status](/docs/images/update_order_status.png)

To update an order status, the user clicks on "Select" button at the right edge of the row of the orders listed. Further details of the order is show on the form at the left. The user will then select the status to change to from the dropdown Order Status. The user then clicks Update button, a confirmation modal is displayed for the user to confirm or cancel the request. If Ok is clicked, validations will be carried out to ensure that an order was selected and that the status is different from the current status of the Order.

#### Review Return Order

When customers request to return orders, the Operator will use this menu item to display existing requests from customers.
Selecting this menu option from the Admin/Ops menu will display a list of all existing request for return of orders. The list could be filtered by Order Number, Email or Order Date range.

![Review Return Order](/docs/images/review_return_order.png)

Clicking the "Select" button will display details of the order for that request and the reason given by the Order owner. The Operator could decide to click "Reject" or "Approve". Comments of the reviewer is required on the form before the buttons. When any of the decision buttons are clicked, a confirmation modal window will be displayed for the user to click Okay to proceed or Cancel to discontinue. Validations are carried out and if the form is okay, the request is accordingly rejected or approved and an email is sent to the user plus a notification record created for the user.

#### Order Details List

This menu option enables the Operator user to query the application for details of any order. Selecting this menu option from the Admin/Ops menu will display a list of all existing orders. The list could be filtered by Order Number, Email, Status, Order Date, artwork/frame name and any one or more combinations of the criteria.

![Order Enquiries](/docs/images/order_enquiries.png)

The report shows each line item on the right edge with details of its artwork, frame and quantity. The date, order number, order total, delivery cost, discount, status and grand total are displayed for each of the Orders on the list.

### Administrator User Functionalities

The members of the Administrator group are responsible to maintain the configuration of the system for efficient operation of the application. A user with administrator group membership will see the below menu when the Admin/Ops icon is clicked:

![Administrator menu](/docs/images/admin_menu.png)

#### Maintain General Information

This option enables the administrator to input and maintain information needed on the footer of the website and the welcome message on the landing page. Information like About Us, FAQ, Privacy Policy, etc. The page uses Django Summernote which enables formatting of the text.

![Maintain General Information](/docs/images/maintain_gen_info.png)

The code is a dropdown selection field for the information to maintain and changes the content accordingly when selected. Clicking the save button will update the contents. The home button takes the user back to the landing page while the Cancel button will discard the current changes on the information panel.

#### Maintain System Preferences

The System Preferences page is used to maintain the configuration of the system. It is used to maintain config details like Sales Percentage, Maximum Delivery Cost, Cancellation of order valid days, etc. All the config settings on this page affect the operations of the whole website and is only administrators that have access to this page.

![Maintain System Preferences](/docs/images/sys_pref.png)

Clicking on the Select button loads the record on the upper section of the page for the administrator to update the Data field. The expected type of data is shown and validation is carried out to ensure the valid data type is entered by the administrator.

#### Assign User Roles/Groups

The administrator can use this option to put or remove any user from any group. The form that is displayed is shown below:

![Assign User Roles/Groups](/docs/images/user_role.png)

The administrator first selects a user and the groups the user belongs to is displayed, if any. To remove existing group click Remove button. To add a group select the group from the group dropdown and click Add.

[>> Bact to TOC](#table-of-contents)

#### Maintain FAQs

This page is used to maintain the Frequently Asked Questions displayed via a link at the footer. The Administrator can create new question and provide the answer in the content panel.

![Maintain FAQs](/docs/images/maintain_faq.png)

New record can be created by clicking New button, the Cancel button discards the current editing, Save button saves the currently edited record. A record can be deleted by clicking the Delete button and responding to the confirmation modal which prompts up. To edit an existing record click on the Edit button, which loads the contents on the panel for editing.

#### Maintain Artists

This option enables the addition, deletion or editing of Artists data in the system. Each artwork has an artist attached to it and the data is maintained here.

![Maintain Artists](/docs/images/maintain_artist.png)

A record can be deleted by clicking the Delete button and responding to the confirmation modal which prompts up. To edit an existing record click on the Edit button, which loads the contents on the panel for editing. The New button creates a blank record. The Cancel button discards the current editing and repositions the data to the first record on the list.

#### Maintain Art Styles

This option enables the addition, deletion or editing of Art Styles data in the system. Each artwork has an art style attached to it and the data is maintained here.

![Maintain Art Styles](/docs/images/maintain_style.png)

A record can be deleted by clicking the Delete button and responding to the confirmation modal which prompts up. To edit an existing record click on the Edit button, which loads the contents on the panel for editing. The New button creates a blank record. The Cancel button discards the current editing and repositions the data to the first record on the list.

#### Maintain Art Genre

This option enables the addition, deletion or editing of Art Genre data in the system. Each artwork has an art genre attached to it and the data is maintained here.

![Maintain Art Genre](/docs/images/maintain_genre.png)

A record can be deleted by clicking the Delete button and responding to the confirmation modal which prompts up. To edit an existing record click on the Edit button, which loads the contents on the panel for editing. The New button creates a blank record. The Cancel button discards the current editing and repositions the data to the first record on the list.

#### Add Artwork

This page is used to add new artwork to the site. The first 9 characters of the SKU is generated automatically as data on the artist, genre and style is entered. The user is expected to complete the last 3 characters. The SKU is validated to ensure it is 12 characters and unique.

![Add Artwork](/docs/images/add_artwork.png)

#### Edit / Delete Artworks

This option enables the editing or deletion of an existing artwork.

![Edit / Delete Artworks](/docs/images/edit_artwork.png)

A list of existing artworks is displayed on the right side of the page including small image of the artwork. Click on the Edit button to load the record on the form by the left for editing. Click Save button to save the record after changes. The user can find an artwork to edit by entering the SKU or any substring of the Name and clicking the google search icon. The filtered records are displayed for the user to select the desired one to edit or delete. Validations are done before saving and errors encountered are reported to the user.

Clicking the Delete button will prompt for the confirmation of the deletion before effecting the deletion.

#### Maintain Art Frames

This option enables the addition, deletion or editing of Art Frame data in the system. Purchase of an artwork requires an associated art frame.

![Maintain Art Frame](/docs/images/maintain_artframe.png)

A record can be deleted by clicking the Delete button and responding to the confirmation modal which prompts up. To edit an existing record click on the Edit button, which loads the contents on the panel for editing. The New button creates a blank record. The Cancel button discards the current editing and repositions the data to the first record on the list.

### The Footer Information

The footer is available on every page and contains information on:

- About Us
- Frequently asked questions
- Contact Us form
- Reviews by users of the website
- Terms & Conditions
- Privacy Policy
- Social Media icons with links to the Facebook page of the business, my Github address and Instagram link not yet active.
- Subscribe form for users to subscribe for newsletters
  
![Footer](/docs/images/footer.png)

The About Us, FAQ, Terms & Conditions and Privacy Policy are information displayed for the users education. Example is the FAQ shown below:

#### Newsletter Subscription Form

The footer has a form to collect email addresses of visitors to the site who opts to subscribe to receive newsletters/offers information via email. Entering a valid email addresses (meeting email format not necessarily verified) is accepted and entered into the Mailchimp data for the website.

![FAQ](/docs/images/faq.png)

The information in the About Us information (and other footer information) displayed below and accessible by clicking the About Us link at the footer was read from the DB as entered by the Administrator via the Maintain General Information page.

![About Us](/docs/images/aboutUs.png)

#### Contact Us

The Contact Us page accessible by clicking Contact Us at the footer enables the user to send any message to the site owner.

![Contact Us](/docs/images/contactUs.png)

Login is not required but if the user is logged in, the email address is entered by default. A copy of the message is sent to the email address of the person that filled the form.

#### Reviews

The users may decide to view reviews of the services of the site owner by clicking the Reviews link at the footer or clicking the star icons below artwork images.

![Reviews](/docs/images/reviews.png)

Viewing a review doesn't require user login but writing a review does. To write a review, the logged in user will click on "Write a Review" from the Customer Reviews page and if logged in, the Customer Reviews page is opened with a form to the left for the user to write a review. If the user is not logged in, the Sign In page is opened for the user to login before the Reviews page is opened.

### Future Features to Implement

- It will be desirable to include social authentication to ease the user experience.
  
- I did not have time to include summary performance reports for the store owner to know some statistics on the sales of artworks and frames, which artworks and frames sell the most. This information could then be displayed to the visitors to the site to know which products the public buy the most.
  
- The list of messages sent by users through Contact Us form could be made available to the administrator via the UI instead of through the Admin Panel. Again this was not feasible due to time constraints of the project.

[>> Bact to TOC](#table-of-contents)

## **Testing**

Manual tests were continuously done on the application during development and as new features are added. Test scripts were developed and used in carrying out most of the manual tests. Being an Agile approach project, I concentrated on delivering the user stories and testing them while the documentation of some of the tests is coming at the close of the project. The code has been validated for syntactic correctness using industry standard methods like W3C, JSHint, PEP8.

Two sets of manual tests documented with Text Scripts **during development** are:

1. [Shopping Bag Tests](/docs/testing/shopping_bag.md)
2. [Checkout Tests](/docs/testing/checkout.md)

Seven Automated tests were carried out on some of the requirements of the application including 3 tests in Checkout models, 2 in Checkout views and 2 in artworks forms and were successful.

The full details of the other tests carried out is available at [Tests Carried Out](/docs/testing/testing.md)

## **Bugs**

### **Current Bugs**

There is no known current bugs in the system after an exhaustive testing.

### **Resolved Bugs**

- The app was not giving a feedback to user when an invalid discount code is entered at checkout and the app required the user to fill all mandatory fields on the delivery details before processing the discount code. This was resolved at commit[a94d1c](https://github.com/Polyanyanwu/graces-art-pp5/commit/a94d1c12bad5fc1994131abfabe0e02a71acc681) through giving the message when the code is wrong and disabling form validation when the apply button is clicked.

- When a user selects Update Email from the My Account menu, the existing email address was not being listed. This was caused by ```.form-inner-content label:not([for='id_remember']) {
    display: none;
}``` that was used to hide Allauth labels for Profile and login forms. But the email addresses needs the label to display existing emails. I had to introduce a class for the label and enabled the display via commit [4aba12](https://github.com/Polyanyanwu/graces-art-pp5/commit/4aba12235e88ec9b6cfe9092bee27af1ccfc37b2)

- The public user on small device screens could see "Admin/Ops" icon. It was resolved by checking for the user group before displaying the icon via commit [d763d](https://github.com/Polyanyanwu/graces-art-pp5/commit/d763da907d41f33ca7d65150bd901f4fee942e0d).

- The Update order status page returns error 500 when user clicks Update without first selecting an Order to update. Fixed by checking that an order number has been selected before searching the order table for the order, commit code [ea6b8](https://github.com/Polyanyanwu/graces-art-pp5/commit/ea6b873df9a8403d3ef12db154215afe4e593cd9).

- Edit artwork gives Error 500 when SKU is edited. Fixed by using the Artwork ID to fetch the record and passing the ID properly through a context variable. See Commit [dbabea](https://github.com/Polyanyanwu/graces-art-pp5/commit/dbabeae8be439caebfcaf5d8bc1a231539a3714f)

- Edit?Delete artwork gives Error 500 when Edit button is clicked. Caused by a JavaScript crash when looking for sort element not on current page. Resolved by enclosing the offending function in an if statement to check the existence of the element before proceeding with setting the event listener. It was hard to notice because the sort element involved only goes away when on mobile devices. Resolved through [Commit 38e09d](https://github.com/Polyanyanwu/graces-art-pp5/commit/38e09daf9259f0ed83de95be9ddb7fd2766f2ee2)

- User was able to save a new record multiple times in pages where I have New, Update, Edit and Delete on the same page. It was resolved by obtaining the new ID of the saved record and putting it in a session variable which effectively puts it in edit mode as if it was clicked for editing. See [Commit 834fdc](https://github.com/Polyanyanwu/graces-art-pp5/commit/834fdc6dc3687893fa2102bd74b446e3c7f18171)

## **Deployment**

The application was deployed to [Heroku](https://heroku.com) where all the code and database is hosted. The static files were hosted on [Amazon S3 Object Storage](https://aws.amazon.com/s3/). [Strip](https://dashboard.stripe.com) was used for card payment collection. Details of the fork, clone and deployment process [is available here](/docs/deploy/deployment.md)

## **Credits**

### **Content**

- The terms of use was adapted from the Terms and Conditions of [Opentable.ie](https://www.opentable.ie/legal/terms-and-conditions). 

- The idea of the landing page and search functions were borrowed from [Code Institute](https://codeinstitute.net/ie/) student walk-through project (Boutique Ado).

- The privacy policy on the main page was an adaptation of [Milano.ie](https://milano.ie/about-us/privacy-policy)

- The Frequently Asked questions were inspired from [BGA Ireland](https://www.bgastore.ie)
  
### **Code**

- Online [books by Agiliq](https://books.agiliq.com/en/latest/README.html) was a very good resource for getting better ideas of Django ORM.
  
- Numerous [Stack Overflow](https://stackoverflow.com/) postings furnished ideas leading to my figuring out how to overcome some challenges.

- [Coderwall](https://coderwall.com/p/itb2hq/cancel-button-on-a-form-with-required-fields) code for Cancel button without validation.

- [Sven Marnach](https://stackoverflow.com/questions/11433886/sorting-a-list-comprehension-in-one-statement) for the idea of Sorting a List Comprehension in one Statement
  
- [Brian Neal](https://groups.google.com/g/django-users/c/J2FUloVUlzk) for the idea of removing empty selection option from a select field.

- [Stack Overflow](https://stackoverflow.com/questions/7682804/django-model-forms-setting-a-required-field) make a field required on a form.

- [Stack Overflow - Tariq Ahmed](https://stackoverflow.com/questions/70254873/django-summernote-settings) for the fix of Summernote dropdowns not working

- [Stack Overflow - Tiago Martins Peres](https://stackoverflow.com/questions/6069070/how-to-use-permission-required-decorators-on-django-class-based-views) for the information on resolving login required to class based view.

- [Stack Overflow - Mark Dickinson](https://stackoverflow.com/questions/6681743/splitting-a-number-into-the-integer-and-decimal-parts) for the code on Splitting a number into the integer and decimal parts

- [Stack Overflow](https://stackoverflow.com/questions/27325505/how-to-get-the-previous-url-from-a-post-in-django) for how to get the URL that called a view.

- [Stack Overflow - Ayman Hourieh](https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists) assisted in answering the question "How do I check if a variable exists?"

- [Seobility](https://www.seobility.net/en/wiki/Robots.txt guide on robots.txt) had a good and brief guide on robots.txt

- [W3schools](https://www.w3schools.com/)  

- [W3docs](https://www.w3docs.com/)
  
- [GeeksforGeeks](https://www.geeksforgeeks.org/)

- [Codegrepper](https://www.codegrepper.com/)

- Credit to Google for its search engine easily showing useful search results all of the time.

### **Media**

- The landing page image of a wooden frame was downloaded from [Freepik](https://www.freepik.com/free-psd/wooden-picture-frame-mockup-psd-with-colorful-painting_17609593.htm?query=photo%20frame).

- The images of all the artworks were [WikiArt.org](https://www.wikiart.org/), downloaded from [BryanB](https://www.kaggle.com/datasets/bryanb/abstract-art-gallery) while the csv files that had the image classification into genre, style, artist was downloaded from  in the site was downloaded from [ArtGAN](https://github.com/cs-chan/ArtGAN/tree/master/WikiArt%20Dataset).

- The 403 error message image was downloaded from [gsatatic](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3Crb5tO7_ixFPKD62WWLao6lOdPyl-vzd7w&usqp=CAU)

- The 404 Page not found image was downloaded from [CCM.net](https://ccm.net/contents/1079-page-not-found-where-is-the-404-error-coming-from)
  
### **Acknowledgements**

- Many thanks to my mentor [Brian O'Hare](https://code-institute-room.slack.com/team/U02H67B6DS6) for the encouragement.

- Many thanks to the Code Institute's team (Lecturers and Tutors) for the excellent job of making me a better.
  
- I'm grateful to my family for their support and prayers through the last year I have been on this up-skilling.

- Really grateful to Code Institute's team (Lecturers and Tutors) for the style of transferring this knowledge in a short time.

- Thanks to the [Slack Community](code-institute-room.slack.com) that serve as first line of help and support.

- Thanks to [Simen Daehlin](https://code-institute-room.slack.com/team/U4MVA9YQP) for pointing out the proper way of validating the HTML codes from a Django project like this.

[>> Bact to TOC](#table-of-contents)
