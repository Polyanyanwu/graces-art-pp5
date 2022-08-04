document.addEventListener("DOMContentLoaded", startUp);

// Timeout function to delay when a message is displayed 
// to user before removing it from the screen

const toastRemove = function () {
    "use strict";
    const toast = document.querySelector('.custom-toast');
    if (toast != null) {
        if (toast.classList.contains('show')) {
            setTimeout(function () {
                toast.classList.remove('show')
            }, 5000); // 10 seconds
        }
    }
};


// Function to run the confirmation modal window
const Confirmation = function (message, yesFunction, noFunction) {
    "use strict";
    const confirmBox = $("#confirmModal");
    confirmBox.find("#confirm-message").text(message);
    confirmBox
        .find(".confirm-yes,.confirm-no")
        .unbind()
        .click(function () {
            confirmBox.hide();
        });
    confirmBox.find(".confirm-yes").click(yesFunction);
    confirmBox.find(".confirm-no").click(noFunction);
    confirmBox.show();
};

// confirmation for single row of data
if (document.getElementById('confirm-single')) {
    document.getElementById('confirm-single').addEventListener('click', function (e) {
        "use strict";
        const msg = document.getElementById('confirm-single').dataset.message;
        Confirmation(msg,
            function yes() {
                const rec_id = e.target.dataset.record_id;
                console.log("record id======", rec_id);
                document.getElementById("confirm-id").value = rec_id;
                document.getElementById('confirm-action-btn').click();
            },
            function no() {
                return;
            });
    });
}


// Confirmation for multiple rows
if (document.querySelectorAll('.confirm-many')) {
    const rec_btn = document.querySelectorAll('.confirm-many');
    rec_btn.forEach(btn => btn.addEventListener('click', function (e) {
        "use strict";
        const msg = e.target.dataset.message;
        Confirmation(msg,
            function yes() {
                const rec_id = e.target.dataset.record_id;
                document.getElementById("confirm-id").value = rec_id;
                document.getElementById('confirm-action-btn').click();
            },
            function no() {
                return;
            });
    }));
}


function copyDiscountCode() {
    "use strict";
    const welcomeCodeEl = document.getElementById('welcome-code');
    const thresholdCodeEl = document.getElementById('threshold-code');
    const welcomeCodeBtn = document.getElementById('welcome-code-btn');
    const thresholdCodeBtn = document.getElementById('threshold-code-btn');

    welcomeCodeBtn.addEventListener('click', (e) => {
        e.preventDefault();
        navigator.clipboard.writeText(welcomeCodeEl.value);
        alert("Copied the text: " + welcomeCodeEl.value);
    });

    thresholdCodeBtn.addEventListener('click', (e) => {
        e.preventDefault();
        navigator.clipboard.writeText(thresholdCodeEl.value);
        alertMe("Copied the text: " + thresholdCodeEl.value);
    });
}

function startUp() {
    toastRemove();
    if (document.querySelector('.discount-header')){
        copyDiscountCode()
    }

    // If back to top link is on the page, listen for click events
    if (document.querySelector('.back-to-top-btn')){
        document.querySelector('.back-to-top-link').addEventListener('click', function(e){
            document.querySelector('.container-main').scrollIntoView();
        })
        }
}

(function ($) {
    window.fnames = new Array();
    window.ftypes = new Array();
    fnames[0] = 'EMAIL';
    ftypes[0] = 'email';
    fnames[1] = 'FNAME';
    ftypes[1] = 'text';
    fnames[2] = 'LNAME';
    ftypes[2] = 'text';
    fnames[3] = 'ADDRESS';
    ftypes[3] = 'address';
    fnames[4] = 'PHONE';
    ftypes[4] = 'phone';
    fnames[5] = 'BIRTHDAY';
    ftypes[5] = 'birthday';
}(jQuery));
var $mcj = jQuery.noConflict(true);
