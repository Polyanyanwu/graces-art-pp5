# **GRACES ART WEBSITE**

The Graces Art is a web application that enables users to purchase an artwork for printing. The purchased artwork would be delivered to the user's supplied address.  

![Graces Art](/docs/images/responsive.png)

## Live Site

[Graces Art Live](#)

## Repository

[View Repository Here](https://github.com/Polyanyanwu/graces-art-pp5)

## Table of Contents

- [**GRACES ART WEBSITE**](#graces-art-website)
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
  - [**Database Design**](#database-design)
  - [**Flowchart**](#flowchart)
  - [**Search Engine Optimization**](#search-engine-optimization)
    - [**Keywords Research**](#keywords-research)

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

## **Database Design**

The database used in this project is a relational database, Postgres provided by Heroku.

The initial design database Entity Diagram is given below:

![Database Entity Diagram](/docs/graces_art_ed.png)

## **Flowchart**

The initial flowchart for the user interaction with the website has been produced to guide the application development. As the site unfolds, it may differ slightly as requirements may change in the course of development.

![Flowchart](/docs/graces_art_flowchart.png)

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
