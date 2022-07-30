

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

function startUp(){
    toastRemove();
}