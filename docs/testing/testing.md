# **Testing of Graces Art Print Website**

[<< Back to README](/README.md)

- [**Testing of Graces Art Print Website**](#testing-of-graces-art-print-website)
  - [**Code Validation**](#code-validation)
    - [**W3C Validation for HTML**](#w3c-validation-for-html)
    - [**W3C Validation for CSS**](#w3c-validation-for-css)
    - [**JSHint**](#jshint)
    - [**PEP8**](#pep8)
    - [**Lighthouse**](#lighthouse)
  - [**Manual Tests**](#manual-tests)
    - [**Public User Acceptance Test**](#public-user-acceptance-test)
      - [P1. Public user want a user-friendly interactive website](#p1-public-user-want-a-user-friendly-interactive-website)
      - [P2. Public user want to be able to access the website using different devices for same friendly experience](#p2-public-user-want-to-be-able-to-access-the-website-using-different-devices-for-same-friendly-experience)
      - [P3. Public user wants to view list of artworks so as to select some to purchase](#p3-public-user-wants-to-view-list-of-artworks-so-as-to-select-some-to-purchase)
      - [P4. Public user want to easily view purchases at any time](#p4-public-user-want-to-easily-view-purchases-at-any-time)
      - [P5. Public user can easily identify deals and special offers to take advantage of savings on items to be purchased](#p5-public-user-can-easily-identify-deals-and-special-offers-to-take-advantage-of-savings-on-items-to-be-purchased)
      - [P6. Public user can sort the list of available artworks](#p6-public-user-can-sort-the-list-of-available-artworks)

## **Code Validation**

Code validations have been thoroughly done on all files in the application: HTML, CSS, Javascript and Python and all have been very successful. Below are evidence of the tests.

### **W3C Validation for HTML**

The [W3C Markup Validation Service](https://validator.w3.org/) was used to check the website for validation errors using the live URL ```(https://graces-art.herokuapp.com/)```. The results show no errors and the html codes are valid.

![HTML Validation](/docs/testing/html_validation_ok.png)

Furthermore, I was curious when the using the URL was not producing an error on a tag I used as a test case, I had to resort to copy page source and paste the codes on the validator. Then loads of issues were reported and I cleared all of them. There are exceptions noted below due to my use of Django-Summernote. The exceptions are:

1. The ```https://graces-art.herokuapp.com/utility/info/```, the page for Maintain General information, where the Django-Summernote caused 8 errors that I couldn't rectify though it doesn't disturb the page functionality. The Django-summernote was very important to be used for that page as it is used to maintain formatted messages for About Us, Privacy Policy, etc instead of hard coding them.
2. Similar issue with ```https://graces-art.herokuapp.com/faqm/``` coming up with the same 8 Summernote validation errors.

The validation error is shown below:

![HTML Validation Exception](/docs/testing/maintain_faq_html_error.png)

These issues occurred at the pages where I used Summernote to capture input data. The other pages where I Used Summernote to display data did not return validation errors.

### **W3C Validation for CSS**

The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to check the CSS for any errors. The test showed no errors in the CSS text.

![CSS Validation](/docs/testing/css_validation.png)

[<< Back to README](/README.md) [>> Bact to TOC](#testing-of-graces-art-print-website)

### **JSHint**

The [JSHint](https://jshint.com/) was used to validate codes from the four JavaScript files for semantic and syntax errors. No errors were found.

| JavaScript File                            | Result    |
|--------------------------------------------|-----------|
| General Javascript File (base.js)          | ![Base](/docs/testing/base_js_validation.png) |
| Checkout App Javascript File (checkout.js) | ![Checkout](/docs/testing/checkout_js_validation.png) |
| Artworks Javascript File (artworks.js)     | ![Artwork](/docs/testing/artworks_js_validation.png) |
| Utility Javascript File (utility.js)       | ![Utility](/docs/testing/utility_js_validation.png) |

[<< Back to README](/README.md) [>> Bact to TOC](#testing-of-graces-art-print-website)

### **PEP8**

[PEP8 online](http://pep8online.com/) was used to validate all the the Python codes for semantic and syntax errors. No errors were reported and few warnings were rectified leading to no errors or warnings on all the Python codes.
I attach evidence of two out of all the PEP8 tests done.

PEP8 result for the checkout.views.py (the biggest view code in the system)
![PEP8 for Checkout View](/docs/testing/pep8_checkout_view.png)

PEP8 result for the checkout.models.py
![PEP8 for Checkout Model](/docs/testing/pep8_orders.png)

### **Lighthouse**

[Lighthouse](https://developers.google.com/web/tools/lighthouse/?utm_source=devtools) available in Google Chrome DevTools and Microsoft Edge were used to test the deployed site performance, accessibility and user experience. The outcome of the tests on some of the pages is shown below:

![Lighthouse](/docs/testing/lighthouse.png)

[<< Back to README](/README.md) [>> Bact to TOC](#testing-of-graces-art-print-website)

## **Manual Tests**

The application was thoroughly tested at each step of the development process and guided by the agreed Acceptance Criteria for each user story.  Below are the result and evidence of the manual testing of all aspects of the application, some done at development stage and others after deployment. The tests cover all the user stories developed at the beginning of the project and those that came in the process of the development.

For the core of the online shop which is the shopping bag and the checkout, I developed a Test Script which was followed and used to test the functionalities of the shopping bag and checkout.

[The Shopping Bag test script is here](/docs/testing/shopping_bag.md) while [the Checkout test script is here](/docs/testing/checkout.md)

Other Manual Tests done following the Acceptance Criteria established at the commencement of the project are detailed below:

### **Public User Acceptance Test**

#### P1. Public user want a user-friendly interactive website

1. **Artworks are visible on home page**

- Open a web browser
- Input the Graces Art Print url ```(https://graces-art.herokuapp.com/)```
- Links to various categories of artworks are visible. (A slight change was made at development stage to have a welcome page before the artworks display and agreed with the site owner)

[<< Back to README](/README.md) [>> Bact to TOC](#testing-of-graces-art-print-website)

2. **Responsive in mobile and desktop browsers**

- Open the URL address of the website in desktop computer, laptop computer, iphone, ipad, samsung phone.
- The application is responsive and user can effectively shop around and complete an order
- The responsiveness was well tested using the Google Chrome developer tools to simulate different screen widths. See also the [mockup image at the start of the README.](/docs/images/graces_art_main.png)

1. **Feedback on user actions are given**

- Login as public user
- When you successfully sign in, a message at the top right of the page is displayed informing your of the successful sign in.
- Giving feedback to the user is built into any places where they are needed in the application.

![Sign In Success](/docs/testing/succes_sign_in.png)

Similarly when a user adds an artwork to the shopping bag, a feedback on the contents of the bag is given on the message corner at the top right.

![Add to Bag Success](/docs/testing/success_add_to_bag.png)

[<< Back to README](/README.md) [>> Bact to TOC](#testing-of-graces-art-print-website)

1. User finds links to navigate to other functions easy

- Open the website
- THe menu bar is accessible from all pages with dropdown items to chose from in most cases. The shopping bag is equally visible at all times.

![Nav Bar](/docs/testing/page_header.png)

1. Font is legible

All fonts are legible when any page is displayed. Accessibility report from Lighthouse shows an average of 95% on each of the pages of the website.

![Accessibility Report](/docs/testing/lighthouse.png)

1. Color contrast is effective

The contrast was okay as the accessibility report above shows.

[<< Back to README](/README.md) [>> Bact to TOC](#testing-of-graces-art-print-website)

#### P2. Public user want to be able to access the website using different devices for same friendly experience

1. Website is accessible on different sized devices

This requirements were met with tests reported on P1 2. above.

1. Information is easy to find both on small and large screens

This requirements were met with tests reported on P1 2. above.

#### P3. Public user wants to view list of artworks so as to select some to purchase

1. List of artwork is visible on home page

- Open the Graces Art Print website
- Click Shop Now and a display of all artworks is shown.
- User can also select any of the categories on the menu bar or click on the Sales link to see items meeting the selected criteria.
- Click on any of the displayed artwork and the page for adding a frame for the printing is presented. From there the user can add to shopping bag.

![Artwork Image](/docs/testing/artwork_image.png)

1. Each artwork displayed has properties- genre, artist, style

- The artworks listed in Item P3.1 above have the genre, artist, style and store rating shown under the image of the artwork.

#### P4. Public user want to easily view purchases at any time

1. On any page the shopping bag is visible and accepting clicks when not empty

- Open the Graces Art Print website
- Click Shop now
- Click on any artwork displayed
- Select Frame and quantity
- Click Add to Bag
Notice that the Bag icon on the right is now having a different color with the total cost of items in it shown under the icon.
![Bag Icon](/docs/testing/bag_icon.png)

2. Clicking the shopping bag opens the shopping bag details page

- click on the bag icon from any page and it will open the shopping bag page. If the bag is empty instead of disallowing clicks, it was designed to open a bag page and give the information that the bag is empty with links to continue shopping
![Shopping Bag](/docs/images/shopping_bag.png)

3. Shopping bag has total cost of all items and delivery cost.
  
- Click on the shopping bag icon after you have added some items to the bag
- Observe that the delivery cost and total cost of all items are displayed
- You can click on the quantity dropdown to increase or decrease the quantity and the cost is recalculated and shown immediately
- If the quantity you selected is not available the message will be given that includes the quantity available (simulate this by logging in as Administrator and updating the quantity of a frame to a small number, return to shopping bag and request a quantity more than the available frame number). The quantity relate to frames as it is assumed the artworks are already in digital form.

![Stock quantity alert](/docs/testing/stock_qty_warning.png)

[<< Back to README](/README.md) [>> Bact to TOC](#testing-of-graces-art-print-website)

#### P5. Public user can easily identify deals and special offers to take advantage of savings on items to be purchased

1. Deals/ special offer information is visible on most pages

- Open the Graces Art Print website
- Click on the Sales link available at the menu bar
- List of all artworks on sale offer is displayed. The original price and the sale price is displayed beside each other.
- The menu bar is accessible from all pages.

![Sales Page](/docs/testing/sales.jpg)

Note the names of the sales is changeable by the Administrator and the sales percentage too.

#### P6. Public user can sort the list of available artworks

1. Sorting dropdown is visible on pages displaying list of artwork

- Open the Graces Art Print website
- Click on All Artworks, select any of the criteria listed or select from any of Artist, Genre, or sales

1. Selecting a criteria from the dropdown sorts the displayed artworks accordingly