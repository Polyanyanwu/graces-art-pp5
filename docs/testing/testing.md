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
      - [P7. Public user can sort a specific genre, artist or style](#p7-public-user-can-sort-a-specific-genre-artist-or-style)
      - [P8. Public user can search for an artwork by name to find a specific artwork to purchase](#p8-public-user-can-search-for-an-artwork-by-name-to-find-a-specific-artwork-to-purchase)
      - [P9. Public user can easily select the frame, size and quantity for an artwork print](#p9-public-user-can-easily-select-the-frame-size-and-quantity-for-an-artwork-print)
      - [P10. Public user Update the quantity and frame of individual items shopping bag](#p10-public-user-update-the-quantity-and-frame-of-individual-items-shopping-bag)
      - [P11. Public user Input payment information](#p11-public-user-input-payment-information)
      - [P12. Public user View a confirmation of an order after checkout](#p12-public-user-view-a-confirmation-of-an-order-after-checkout)
      - [P13. Public user Give a review of an artwork/services of site owner](#p13-public-user-give-a-review-of-an-artworkservices-of-site-owner)
      - [P14. Public user View privacy policy of the website](#p14-public-user-view-privacy-policy-of-the-website)
      - [P15. Public user Subscribe to newsletter](#p15-public-user-subscribe-to-newsletter)
      - [P16. Public user Contact the site owner](#p16-public-user-contact-the-site-owner)
      - [P17. Public user See the About Us information](#p17-public-user-see-the-about-us-information)
      - [P18. Public user See the Terms and Conditions](#p18-public-user-see-the-terms-and-conditions)
      - [P19 Customer View Order History](#p19-customer-view-order-history)
      - [P20 Customer Request Return Order](#p20-customer-request-return-order)
      - [P21 Customer View Notifications](#p21-customer-view-notifications)
      - [P23 Customer Cancel Order](#p23-customer-cancel-order)
      - [P24 Customer Save items to my wish list](#p24-customer-save-items-to-my-wish-list)
      - [FAQ](#faq)
      - [O1. Operator user View requests for return of delivered artwork](#o1-operator-user-view-requests-for-return-of-delivered-artwork)
      - [O2. Operator user Update order status](#o2-operator-user-update-order-status)
      - [O3. Operator user Make enquiry on orders by date range and order status](#o3-operator-user-make-enquiry-on-orders-by-date-range-and-order-status)

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

3. **Feedback on user actions are given**

- Login as public user
- When you successfully sign in, a message at the top right of the page is displayed informing your of the successful sign in.
- Giving feedback to the user is built into any places where they are needed in the application.

![Sign In Success](/docs/testing/succes_sign_in.png)

Similarly when a user adds an artwork to the shopping bag, a feedback on the contents of the bag is given on the message corner at the top right.

![Add to Bag Success](/docs/testing/success_add_to_bag.png)

[<< Back to README](/README.md) [>> Bact to TOC](#testing-of-graces-art-print-website)

4. User finds links to navigate to other functions easy

- Open the website
- THe menu bar is accessible from all pages with dropdown items to chose from in most cases. The shopping bag is equally visible at all times.

![Nav Bar](/docs/testing/page_header.png)

5. Font is legible

All fonts are legible when any page is displayed. Accessibility report from Lighthouse shows an average of 95% on each of the pages of the website.

![Accessibility Report](/docs/testing/lighthouse.png)

6. Color contrast is effective

The contrast was okay as the accessibility report above shows.

[<< Back to README](/README.md) [>> Bact to TOC](#testing-of-graces-art-print-website)

#### P2. Public user want to be able to access the website using different devices for same friendly experience

1. Website is accessible on different sized devices

This requirements were met with tests reported on P1 2. above.

2. Information is easy to find both on small and large screens

This requirements were met with tests reported on P1 2. above.

#### P3. Public user wants to view list of artworks so as to select some to purchase

1. List of artwork is visible on home page

- Open the Graces Art Print website
- Click Shop Now and a display of all artworks is shown.
- User can also select any of the categories on the menu bar or click on the Sales link to see items meeting the selected criteria.
- Click on any of the displayed artwork and the page for adding a frame for the printing is presented. From there the user can add to shopping bag.

![Artwork Image](/docs/testing/artwork_image.png)

2. Each artwork displayed has properties- genre, artist, style

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
A list of artworks are displayed meeting the criteria you selected, the total number of artworks selected is also shown.
- From the displayed list, a "Sort by.." dropdown is visible on the right side of the page.

![Sort Artwork](/docs/testing/sort_by.jpg)

2. Selecting a criteria from the dropdown sorts the displayed artworks accordingly

- After step 1 above, clicking any of the sort criteria will rearrange the list as appropriate.

#### P7. Public user can sort a specific genre, artist or style

1. Sorting dropdown is visible on pages displaying list of artwork

- Open the Graces Art Print website
- The Artist and Genre dropdown is visible on the menu bar (I decided to keep it less crowded by not putting the Style dropdown on the menu bar, however the user can click on the style on an displayed artwork and the category will change to that style).
- Click on any item in the chosen dropdown menu and the list of artworks will change to the selected item criteria.
- Click on the Genre or Artist or Style of any displayed image and the list criteria is changed to the clicked criteria.

2. Selecting a criteria from the dropdown sorts the displayed artworks accordingly

- From step 1, it is observable that the list indeed changes according to the selected Artist, Genre or clicked Style.
A typical list displayed when user selects the Landscape genre is shown below:

![Genre list](/docs/testing/selecting_genre.jpg)

#### P8. Public user can search for an artwork by name to find a specific artwork to purchase

1. Input form visible to accept name of artwork on home page

- Open the Graces Art Print website
- Notice the input form with the placeholder "search artwork by name" at the top of the page. It is part of the header accessible from all pages of the website.
- Input any part of the artwork name or even the artist name
- Click on the google search icon
A list of the artworks which has names matching any part of your input string is listed. E.g, see below result of entering "pab" as the search criteria before clicking the search icon:

![Search](/docs/testing/search.jpg)

2. Clicking on search button returns a list of matching names and total artwork found

- From the image displayed above, it is evident that the artworks are listed and the total number found is stated at the left side of the page.

#### P9. Public user can easily select the frame, size and quantity for an artwork print

1. Clicking on an artwork opens a details page with frame, size and quantity available for selection

- Open the Graces Art Print website
- Click Shop Now or select any of the criteria from the menu bar to display a list of artworks
- Click on any artwork
A details page having a selection field for Frame and one for Quantity is shown

- Select any frame form the dropdown and the price and image of the frame is displayed. Also the total cost of the frame and the artwork is computed and shown
- Select a different quantity and observe that the cost is recomputed and displayed
- Select a different quantity and observe the recomputed costs too
To observe the effect of the quantities on the stock availability, login with a user that belongs to Administrator group and change the frame quantities to small number. The system will not allow you complete add to bag if the frame quantity is not available. Also observe the increase/decrease of the quantity in the Frame table as you increase/decrease the quantity at this shopping page.

![Artwork Details](/docs/images/artwork_details.png)

2. Available frames are indicated

- During development and engagement with the Site Owner, it was advised that best practice is not to display the quantity available but rather indicate if the customer want to order a quantity that is out of stock. So this feature was replaced with advising the customer if a quantity requested is out of stock.

#### P10. Public user Update the quantity and frame of individual items shopping bag

1. Shopping bag details visible when shopping bag icon is clicked
2. Shopping bag permits update of frame and quantity for each bag item

The test done in [Public User View purchases suffices](#p4-public-user-want-to-easily-view-purchases-at-any-time)

#### P11. Public user Input payment information

1. User address form available on checkout page
2. Payment card form available on checkout page
3. Payment accepted or error message displayed

#### P12. Public user View a confirmation of an order after checkout

1. Order confirmation page available after successful checkout
2. Confirmation page has correct details of the order placed

#### P13. Public user Give a review of an artwork/services of site owner

1. Reviews are visible through a link at the footer
2. Authenticated user that have purchased artwork in the past could write a review

#### P14. Public user View privacy policy of the website

1. Privacy policy is accessible through a link at the footer

#### P15. Public user Subscribe to newsletter

1. Subscribe button is available at the home page footer
2. Logged in user will have email input prefilled

#### P16. Public user Contact the site owner

1. Contact us button is available at the footer
2. Contact us form opens for the user to input the details
3. If user is authenticated, copy of the message is saved in the notifications page

#### P17. Public user See the About Us information

About us button is available at the footer
About us page opens for the user to view

#### P18. Public user See the Terms and Conditions

1. Terms & Conditions button is available at the footer
2. Terms & Conditions page opens for the user to view when the button is clicked

#### P19 Customer View Order History

1. Menu item available to view Order History
2. Clicking the menu after sign in, the details of my previous orders are available

#### P20 Customer Request Return Order

1. Menu item to request return order available to logged in user
2. List of qualifying orders are presented when user selects the return order menu
3. Acknowledgment email is sent to the requesting user

#### P21 Customer View Notifications

1. Menu item for notifications available to user
2. Clicking on notifications displays the list of notifications and their details

#### P23 Customer Cancel Order

1. User has option to cancel an order using the order number
2. Order status changes to cancelled if user submits the cancel order form within a given time frame

#### P24 Customer Save items to my wish list

1. Wish list menu item is visible on profile menu
2. Wish list button is available from artwork details page
3. Clicking the button adds an item to the wish list

#### FAQ

#### O1. Operator user View requests for return of delivered artwork

1. Menu option for order return available
2. Ability to select all returned orders
3. Button to pick and update the order status
4. Confirmation to proceed with the change of status
5. Feedback message on successful acceptance of the return
6. Updated list of returned orders

#### O2. Operator user Update order status

1. Menu option for update Order Status is available
2. A page is provided where active orders are displayed
3. Buttons are provided to click and select to update status
4. Status of order changes after confirmation of status change

#### O3. Operator user Make enquiry on orders by date range and order status

1. Order history enquiry available
2. Query has options to select date range and Order status
3. List of data is displayed meeting the given criteria

