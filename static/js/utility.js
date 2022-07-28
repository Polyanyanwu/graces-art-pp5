/*jshint esversion: 6 */

// Disable the selection of the code from the choice list of system preference
// and only change when user clicks on the edit button

function startUp() {
    "use strict";
    document.querySelector('#id_code').setAttribute('disabled', '');
    const select_btn = document.querySelectorAll('.select-pref');
    select_btn.forEach(btn => btn.addEventListener('click', function (e) {
        e.preventDefault();
        const btn_code = e.target.dataset.code;
        document.getElementById('clicked-code').value = btn_code;
        document.querySelector('#select-pref-btn').click();
    }));
}
document.addEventListener("DOMContentLoaded", startUp);