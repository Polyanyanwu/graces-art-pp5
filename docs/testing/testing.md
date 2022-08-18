# **Testing of Graces Art Print Website**

[<< Back to README](/README.md)

- [**Testing of Graces Art Print Website**](#testing-of-graces-art-print-website)
  - [**Code Validation**](#code-validation)
    - [**W3C Validation for HTML**](#w3c-validation-for-html)
    - [**W3C Validation for CSS**](#w3c-validation-for-css)
    - [**JSHint**](#jshint)
    - [**PEP8**](#pep8)
    - [**Lighthouse**](#lighthouse)

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
