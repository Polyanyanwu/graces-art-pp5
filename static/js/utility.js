/*jshint esversion: 6 */

// Disable the selection of the code from the choice list of system preference
// and only change when user clicks on the edit button

function startUp() {
    "use strict";

    if (document.querySelector('#sys_pref_update')) {
        document.querySelector('#id_code').setAttribute('disabled', '');
        document.querySelector('#id_data_type').setAttribute('disabled', '');
        const select_btn = document.querySelectorAll('.select-pref');
        select_btn.forEach(btn => btn.addEventListener('click', function (e) {
            e.preventDefault();
            const btn_code = e.target.dataset.code;
            document.getElementById('clicked-code').value = btn_code;
            document.querySelector('#select-pref-btn').click();
        }));
    }

    if (document.querySelector('#gen_info_update')) {
        // General information form
        const idCode = document.querySelector('#id_code');
        idCode.addEventListener('change', function (e) {
            document.getElementById('clicked-code').value = e.target.value;
            document.querySelector('#select-info-btn').click();
        });
    }

    // User Group Update
    if (document.querySelector("#group-update-form")) {
        // force selection of first user
        if (!document.querySelector("#id_user").value) {
            document.querySelector("#id_user").value = document.querySelector("#user_id").value;
        }
        document.querySelector("#id_group_name").required = false;
        document.querySelector("#id_user").addEventListener('change', (e) => {
            e.preventDefault();
            document.getElementById('user-change-button').click();
        });

        const rec_btn = document.querySelectorAll('.remove-group');
        rec_btn.forEach(btn => btn.addEventListener('click', function (e) {
            document.getElementById("user_group_name").value = e.target.dataset.group;
            document.getElementById('action_button').click();
            }));

    }

}
document.addEventListener("DOMContentLoaded", startUp);