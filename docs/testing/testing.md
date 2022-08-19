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
      - [P25 Frequently Asked Questions is available to the Public](#p25-frequently-asked-questions-is-available-to-the-public)
    - [**Authentication Acceptance Test**](#authentication-acceptance-test)
      - [U1. Create an account](#u1-create-an-account)
      - [U2. Have an effective interface to login and logout](#u2-have-an-effective-interface-to-login-and-logout)
      - [U3. Change my password](#u3-change-my-password)
      - [U4. Update information on my profile](#u4-update-information-on-my-profile)
      - [U5. Recover my password if I forgot it](#u5-recover-my-password-if-i-forgot-it)
    - [**Operator Acceptance Test**](#operator-acceptance-test)
      - [O1. Operator user View requests for return of delivered artwork](#o1-operator-user-view-requests-for-return-of-delivered-artwork)
      - [O2. Operator user Update order status](#o2-operator-user-update-order-status)
      - [O3. Operator user Make enquiry on orders by date range and order status](#o3-operator-user-make-enquiry-on-orders-by-date-range-and-order-status)
    - [**Administrator Acceptance Test**](#administrator-acceptance-test)
      - [A1. Assign user role to registered users](#a1-assign-user-role-to-registered-users)
      - [A2. Set system preferences](#a2-set-system-preferences)
      - [A3. Add new artwork](#a3-add-new-artwork)
      - [A4. Edit/update artwork](#a4-editupdate-artwork)
      - [A5. Delete artwork](#a5-delete-artwork)
      - [A6. Edit/update photo frames](#a6-editupdate-photo-frames)
      - [A7. Delete photo frames](#a7-delete-photo-frames)
      - [A8. Add/update general information](#a8-addupdate-general-information)

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

- Open the Graces Art Print website
- Click Shop Now
- Click on any Artwork
- Select a frame and quantity from the selected artwork details page
- Click Add to Bag
- From the Success Message, click Proceed to Checkout
- Checkout Form opens and Name and Address fields are available

![Checkout address](/docs/testing/checkout.md)

2. Payment card form available on checkout page

- Payment card form is visible if you scroll down the page below the name and address fields.

![Checkout address](/docs/testing/checkout2.md)

2. Payment accepted or error message displayed

- Fill the form with the necessary data. Mandatory fields have * beside the placeholders
- First enter an invalid card number (any 16 digits, only numbers are accepted)
The error "Your Card number is invalid is displayed to the user
- Enter the Stripe test valid number 4242 4242 4242 4242 and date in future but 3 digits for postal code
THe error message "Your postal code is incomplete." is displayed.
- Enter a date in the past like "04/22" and the error message " Your card's expiration date is in the past." is displayed.
- Enter the failed payment simulation card number 4000 0025 0000 3155 and you will be prompted to either complete authentication of fail authentication.
- Click the Fail Payment and you will receive a message "we are unable to authenticate your payment method.."

![Failed Payment](/docs/testing/failed_payment_msg.png)

- Enter a successful payment with card number 4242 4242 4242 4242, date 0425,  cvv 456 and zip code 67546
- Click complete order
- A spinner will be shown on the page while you card is being verified.
- Your payment is accepted and a success page is displayed with your order details.

#### P12. Public user View a confirmation of an order after checkout

1. Order confirmation page available after successful checkout

- Follow the steps in P11.2 above and enter the valid card number 4242 4242 4242 4242 with a date in future, etc
The following success message is displayed once the payment has been accepted.

![Payment success](/docs/images/checkout_success_msg.png)

1. Confirmation page has correct details of the order placed

- Follow the steps in 1 above and note the artwork and frame you chose
- Compare with the details in the Thank You success message
- Confirm that the details match your order.

#### P13. Public user Give a review of an artwork/services of site owner

1. Reviews are visible through a link at the footer

- Open the Graces Art Print website
- Find the Reviews link at the footer of the page, and indeed every page.

1. Authenticated user that have purchased artwork in the past could write a review

- Open the website and locate the Reviews link at the footer
- Click on the Reviews link
The reviews page opens with any existing customer review. There was a change request from the Store Owner to restrict writing reviews to logged in users even if they have not made purchases and thats what was implemented. The reviews page has Write Review button that leads to the Reviews page that can allow you to write a review.

![Reviews](/docs/images/reviews.png)

- Click on the Write Reviews link inside the Reviews Page.
If you are logged in the Reviews page with a Form to accept your review is opened. If you are not logged it, the sign in page is opened.

#### P14. Public user View privacy policy of the website

1. Privacy policy is accessible through a link at the footer

- Open the Graces Art Print website
- Find the Privacy Policy link at the footer of the page, and indeed every page.

#### P15. Public user Subscribe to newsletter

1. Subscribe button is available at the home page footer

- Open the Graces Art Print website
- Find the "Subscribe for exclusive discounts straight to your inbox" message at the footer and an email address form.
- Enter a valid email address and the message "Thank you for subscribing!" is displayed below the email address.
The email subscription is embedded from Mailchimp.

![Footer](/docs/images/footer.png)

2. Logged in user will have email input prefilled

This was no longer desirable as the email subscription was embedded at the footer. If I was to do that it will look noisy for the user to see his/her email non stop at the footer.

#### P16. Public user Contact the site owner

1. Contact us button is available at the footer

- Open the Graces Art Print website
- Find the Contact Us link at the footer of the page, and indeed every page.

2. Contact us form opens for the user to input the details

- Click on the Contact Us link at the footer
The Contact Us form opens. If the user is logged in, the email address is prefilled on the form.
- Enter some message on the form
- Click submit to send the message.

![Contact Us](/docs/images/contactUs.png)

3. If user is authenticated, copy of the message is saved in the notifications page

- Sign into the website
- Locate the Contact Us at the footer
- Type some message and click Save button
A copy of your message is sent to your email and saved at your Notifications page under My Account when you sign in.

#### P17. Public user See the About Us information

1. About us button is available at the footer

- Open the Graces Art Print website
- Find the About Us link at the footer of the page, and indeed every page.

2. About us page opens for the user to view

- Open the Graces Art Print website
- Find the About Us link at the footer of the page.
- Click on the About Us link.
The informative about us page opens to the user.
![About Us](/docs/images/aboutUs.png)

#### P18. Public user See the Terms and Conditions

1. Terms & Conditions button is available at the footer

- Open the Graces Art Print website
- Find the Terms & Conditions link at the footer of the page.

1. Terms & Conditions page opens for the user to view when the button is clicked

- Open the Graces Art Print website
- Find the Terms & Conditions link at the footer of the page.
- Click on the Terms & Conditions link.
The informative Terms & Conditions page opens to the user.
![About Us](/docs/testing/terms.jpg)

#### P19 Customer View Order History

1. Menu item available to view Order History

- Open the Graces Art Print website
- Sign in with your username and password, create a user name if you have not done so
- Click on the My Account icon at the top right of any page
The Order History menu item is visible to the user.

![Order History](/docs/images/order_history_public.png)

2. Clicking the menu after sign in, the details of my previous orders are available

- Follow the process in P11 to place an order
- Click on My Account at the top right edge of any page
- Click on Order History from the dropdown menu
If you have placed an order successfully from P11 above, a list of the orders placed an their details will be displayed.
- Click on All Status dropdown and select a status to filter the order and display only the ones with the selected status
- click on the red search icon to filter the displayed records by any of the criteria you entered on the first row (date, order number, status or artwork name / frame name)

#### P20 Customer Request Return Order

1. Menu item to request return order available to logged in user

- Open the Graces Art Print website
- Sign in with your username and password, create a user name if you have not done so
- Click on the My Account icon at the top right of any page
The Return Order menu item is available to the user.

**2. List of qualifying orders are presented when user selects the return order menu**

- Click on the Return Order, after sign in successfully.
- From the displayed list of orders notice that only orders that are active are displayed (orders with status "Ordered").

![Request Return Order](/docs/images/request_return_order.png)

- Confirm that orders that are older than the store permitted return days are disallowed from being returned by signing in as administrator and reduce the "Order return days" from the System Preferences
- Click select and observe the message that you can no longer request return of this order.
(the application could have also removed such order that are already past due for return, but if done the user may be thinking that something is wrong when the order can't be seen on the list. I decided to list the order and give the user the feedback if that order is selected).
- Select an Order that the date falls within the set return date (now fixed at 4 days)
- Input a reason for the return into the Form at the left
- Click the Send Request button
- Click Okay when the confirmation prompt is displayed
- The success message is displayed at the message corner at the right.

![Request Return Order](/docs/images/return_feedback.png)

 3. **Acknowledgment email is sent to the requesting user**

- Send a successful Return Request following process in 2 above.
- Within a few minutes, depending on network, you will receive an email resembling the one below acknowledging your request.
- Notice the order is no longer in the list of orders available for return
- Open the Order History report following the process in  **P19**.
Observe that the order status has changed to "Returned". The store owner will approve or reject the request and you will receive another email conveying the decision.

![REturn Request Email](/docs/testing/return_request_email.jpg)

#### P21 Customer View Notifications

1. **Menu item for notifications available to user**

- Open the Graces Art Print website
- Sign in with your username and password, create a user name if you have not done so
- Click on the My Account icon at the top right of any page
The Notifications menu item is available to the user.

2. **Clicking on notifications displays the list of notifications and their details**

- Click on Notifications from the My Account menu.
- Observe the My Notifications page opens with a list of notifications on major actions you have taken in the website - order placement, return request, order status change, etc.
- Click Details button on the notification of interest and the details is displayed on the left column.
- Click on Delete button from the row you intend to delete, click Okay when the confirmation prompt is displayed.
The notification record is deleted.

![Notifications](/docs/images/notifications.png)

#### P23 Customer Cancel Order

1. **User has option to cancel an order using the order number**

- Open the Graces Art Print website
- Sign in with your username and password, create a user name if you have not done so
- Click on the My Account icon at the top right of any page
The **Cancel Order** menu item is available to the user.
- Click on the Cancel Order menu item
The Cancel Order Request page opens with a list of orders that has status "Ordered". The first row of the table has input fields for Order Number, Email Address and Date which you can use to search for a particular order to cancel.

![Cancel Order Page](/docs/images/cancel_order_req.png)

1. **Order status changes to cancelled if user submits the cancel order form within a given time frame**

- Click on the Cancel Order, after sign in success.
- From the displayed list of orders notice that only orders that are active are displayed (orders with status "Ordered").

- Confirm that orders that are older than the store permitted cancellation days are disallowed from being cancelled by signing in as administrator and reduce the "Cancellation Valid Days" from the System Preferences
- Click select and observe the message that you can no longer cancel the order.
- Select an Order that the date falls within the set Cancellation date (now fixed at 3 days)
- Input a reason for the Cancellation into the Form at the left
- Click the Send Request button
- Click Okay when the confirmation prompt is displayed
- The success message is displayed at the message corner at the right.
An email is also sent to your email address and a Notification record is created.

![Cancellation Feedback](/docs/images/cancel_order_feedback.png)

#### P24 Customer Save items to my wish list

1. **Wish list menu item is visible on profile menu**

- Open the Graces Art Print website
- Sign in with your username and password, create a user name if you have not done so
- Click on My Account and notice the "My Wishlist" menu item is available.

2. Wish list button is available from artwork details page

- Follow process in 1 above
- Click Shop Now from the landing page or select any of the artwork criteria available at the menu bar
- Click on an artwork and the details of the artwork is displayed
Observe that the "Add to Wishlist" button is available on the page.

![Artwork detail](/docs/images/artwork_details.png)

1. Clicking the button adds an item to the wish list

- Click on "Add to Wishlist" button
If the artwork is not in your wishlist already, it is added; if not a message is given that the artwork is already in your wishlist. The "Move to Wishlist" is also available from the Shopping Bag page to add artwork to the wishlist.

![Wishlist Feedback](/docs/images/already_in_wishlist.png)

- From My Account click on wishlist
The wishlist details is displayed with a list of all artworks in your wishlist.

![Wishlist details](/docs/images/my_wishlist.png)

- click on "Buy Now" button to open the details page for the selected artwork where you can select a frame and add to shopping bag.
- click on "Delete" button to remove the artwork from the wishlist.

#### P25 Frequently Asked Questions is available to the Public

1. Frequently Asked Questions is accessible through a link at the footer

- Open the Graces Art Print website
- Find the  Frequently Asked Questions link at the footer of the page, and indeed every page.
- Click on the  Frequently Asked Questions link
The Help Centre page is opened for the users information.

![FAQ](/docs/images/faq.png)

### **Authentication Acceptance Test**

#### U1. Create an account

**1. Sign up option is available to user on the home page and when trying to complete a purchase**

- Open the Graces Art Print website
- Click on "My Account"
- The "Register" and "Login" options are available on the dropdown menu of the My Account icon.
- Follow the process of P11 above and get to the Checkout Page
- Look below the delivery details for an option to "Create an account or login to save this information"
- Click on Create Account to proceed with creating an account or click on Login to open the Sign in page.
- When the Create an Account page opens, enter the email address, username and password to be used in the site
- Click create account
Message will be displayed informing you to check your mail and confirm the email address.
Confirming the email address from the link sent in the email will enable you login

2. **Successful sign up will enable user login with the created email and password**

- Create an account as in process 1. above
- From the My Account icon at the top right of the page, select login
- Enter either the username or email address that you used at account creation
- The login is successful
- A feedback message is given and the My Account menu now has the full set of menu items for signed in user.

#### U2. Have an effective interface to login and logout

1. Sign-in link available on home page

- Open the Graces Art Print website
- Click on "My Account"
- The Login and Register links are available

**2. Sign-in page opens when link is clicked**

- Open the Graces Art Print website
- Click on "My Account"
- Click the Login menu item
The Sign in page opens for you to enter username/email address and password.

![Sign in](/docs/images/sign_in.png)

#### U3. Change my password

1. Reset password link available at sign-in page and on user profile menu
2. Reset password page opens and enables user successfully reset password

- Follow the process in U2 above and open the Sign In page
- Observe that there is "Forgot Password?" link beside the "Sign In" button.
- Click the Forgot Password and you will redirected to a page to enter your email address
- Enter the email address at the Password Reset page that opened
An email will be sent to the email address with the instructions to follow to reset the password

#### U4. Update information on my profile

1. Profile option available to signed in user
2. Profile page opens and enables user to change names/phone, address as needed

- Open the Graces Art Print website
- Click on "My Account"
- Click the Login
- Enter your username and password and login to the site
- Click "My Account" again and observe that there is now an option for My Profile.
- Click on the "My Profile"
The page below opens for the user to update the profile as desired.

![Profile](/docs/images/update_profile.png)

#### U5. Recover my password if I forgot it

1. The login form displays a link to reset password
2. The reset password form opens requesting email address

- Follow the process in U2 above and open the Sign In page
- Observe that there is "Forgot Password?" link beside the "Sign In" button.
- Click the Forgot Password and you will redirected to a page to enter your email address

![Password Reset](/docs/images/password_reset_input.png)

- Enter the email address at the Password Reset page that opened
An email will be sent to the email address with the instructions to follow to reset the password

### **Operator Acceptance Test**

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

### **Administrator Acceptance Test**

#### A1. Assign user role to registered users

Options for user role is available on the user profile
Setting the user role restricts the user to the assigned role

#### A2. Set system preferences

System preferences available in the Admin panel
Changes made affect the working of the application

#### A3. Add new artwork

Menu item to Add artwork is available on Admin menu
Admin is able to successfully add an artwork

#### A4. Edit/update artwork

Menu item to Edit artwork is available on Admin menu
Admin is able to search and locate artwork to update
Update is successful

#### A5. Delete artwork

Menu item to delete artwork is available on Admin menu
Admin is able to search and locate artwork to delete
Delete is successful

#### A6. Edit/update photo frames

Menu item to Edit photo frames is available on Admin menu
Admin is able to locate photo frame to update
Update is successful

#### A7. Delete photo frames

Menu item to delete photo frame is available on Admin menu
Admin is able to locate photo frame to delete
Delete is successful

#### A8. Add/update general information

Menu option to maintain general information available to Admin menu
Admin user is able to update the general information like About Us, Terms of Use, etc
