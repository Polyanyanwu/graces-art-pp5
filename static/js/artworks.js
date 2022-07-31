/*jshint esversion: 6 */


function startUp() {
    "use strict";
    getSkuPrefix();
    // User Group Update
    const rec_btn = document.querySelectorAll('.edit-btn');
    rec_btn.forEach(btn => btn.addEventListener('click', function (e) {
        e.preventDefault();
        document.getElementById("name_selected").value = e.target.dataset.name;
        document.getElementById('select-action-btn').click();
    }));
}

document.addEventListener("DOMContentLoaded", startUp);

function getSkuPrefix() {
    if (document.getElementById('add-artwork-form')) {
        sku = document.querySelector('#id_sku');
        genre = document.querySelector('#id_genre');
        artist = document.querySelector('#id_artist');
        style = document.querySelector('#id_style');

        artist.addEventListener('change', function (e) {
            processSku();
        });

        genre.addEventListener('change', function (e) {
            processSku();
        });
        style.addEventListener('change', function (e) {
            processSku();
        });
        const processSku = function () {
            sku_txt = "ART";
            if (artist){
                val = artist.options[artist.selectedIndex].value;
                if (val.length < 2) val = '0' + val;
                sku_txt += val;
            }
            if (genre) {
                val = genre.options[genre.selectedIndex].value;
                if (val.length < 2) val = '0' + val;
                sku_txt += val;
            }
            if (style) {
                val = style.options[style.selectedIndex].value;
                if (val.length < 2) val = '0' + val;
                sku_txt += val;
            }
            sku.value = sku_txt;
        }
    }
}