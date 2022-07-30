

document.addEventListener("DOMContentLoaded", startUp);

// Timeout function to delay when a message is displayed 
// to user before removing it from the screen

const toastRemove = function () {
    "use strict";
    const toast = document.querySelector('.toast');
    if (toast != null){
        if (toast.classList.contains('show')){
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
if(document.getElementById('confirm_single')){
    document.getElementById('confirm_single').addEventListener('click', function () {
        "use strict";
        const msg = document.getElementById('confirm_message').dataset.message;
        Confirmation(msg,
            function yes() {
                document.getElementById('confirm-action-btn').click();
            },
            function no() {
                return;
            });
    });
}


// Confirmation for multiple rows
if(document.querySelectorAll('.confirm-many')){
    const rec_btn = document.querySelectorAll('.confirm-many');
    rec_btn.forEach(btn => btn.addEventListener('click', function(e){
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


function startUp(){
    toastRemove();
}