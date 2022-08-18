/*jshint esversion: 6 */

document.addEventListener("DOMContentLoaded", startUp);

// Timeout function to delay when a message is displayed 
// to user before removing it from the screen if the user did not do so after 15 seconds

const toastRemove = function () {
    "use strict";
    const toast = document.querySelector('.custom-toast');
    const toastPersist = document.querySelector('#toast-persist');

    if (toast != null && toastPersist == null) {
        if (toast.classList.contains('show')) {
            setTimeout(function () {
                toast.classList.remove('show');
            }, 15000); // 15 seconds
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
                document.getElementById("confirm-id").value = rec_id;
                document.getElementById('confirm-action-btn').click();
                const modal_backdrop = document.querySelector(".modal-backdrop");
                modal_backdrop.hide();
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
                const actionBtn = document.getElementById('confirm-action-btn');
                let btnName = "";
                if(e.target.dataset.btnName) btnName = e.target.dataset.btnName;
                if(document.getElementById("confirm-id"))
                    document.getElementById("confirm-id").value = rec_id;
                if (btnName){
                    actionBtn.setAttribute('name', btnName);
                    actionBtn.setAttribute('value', rec_id);
                }
                actionBtn.click();
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
        alert("Copied the text: " + thresholdCodeEl.value);
    });
}

function startUp() {
    toastRemove();
    if (document.querySelector('.discount-header')){
        copyDiscountCode();
    }

    // If back to top link is on the page, listen for click events
    if (document.querySelector('.back-to-top-btn')){
        document.querySelector('.back-to-top-link').addEventListener('click', function(e){
            document.querySelector('.container-main').scrollIntoView();
        });
        }
}

