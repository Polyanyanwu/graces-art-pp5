/*jshint esversion: 6 */


function startUp() {
    "use strict";

    // User Group Update
        const rec_btn = document.querySelectorAll('.edit-btn');
        rec_btn.forEach(btn => btn.addEventListener('click', function (e) {
            e.preventDefault();
            document.getElementById("name_selected").value = e.target.dataset.name;
            document.getElementById('select-action-btn').click();
            }));
    }

document.addEventListener("DOMContentLoaded", startUp);