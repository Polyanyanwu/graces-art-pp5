/*jshint esversion: 6 */


function startUp() {
    "use strict";
    artDetails();
    getSkuPrefix();
    sort_selection();
    artDetails();
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
            if (artist) {
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


function sort_selection() {
    $('#select-sort').change(function () {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if (selectedVal != "reset") {
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");
            window.location.replace(currentUrl);
        }
    })
}

function artDetails() {

    if (document.querySelector('#select_frame')) {
        const frameCost = document.querySelector('#frame-cost');
        const selectFrame = document.querySelector('#select_frame');
        const selectedImg = document.querySelector('#selected-img');
        const frameHref = document.querySelector('#frame_href');
        const artFrameCost = document.querySelector('#art-and-frame');
        const totalCostEl = document.querySelector('#total-cost');
        const qtyEl = document.getElementById('quantity');
        const frameIdEl = document.getElementById('frame-id');
        selectFrame.addEventListener('change', function (e) {

            const frameDetail = selectFrame.options[selectFrame.selectedIndex].value;
            const frameId = frameDetail.split(":")[0];
            console.log(frameId);
            frameIdEl.value = frameId;
            const costVal = frameDetail.split(":")[1];
            imgVal = frameDetail.split(":")[2];
            selectedImg.src = imgVal;
            frameHref.href = imgVal;
            frameCost.textContent = "€" + costVal;
            if (document.querySelector('#sale-price')) {
                artFrameCost.textContent = "€" + (parseFloat(costVal) + parseFloat(document.querySelector('#sale-price').textContent)).toFixed(2);
            } else {
                artFrameCost.textContent = "€" + (parseFloat(costVal) + parseFloat(document.querySelector('#price').textContent)).toFixed(2);
            }
            const totalCost = getTotalDetailCost(costVal);
            totalCostEl.textContent = "€" + totalCost.toFixed(2);

        })

        qtyEl.addEventListener('change', function (e) {

            frameDetail = selectFrame.options[selectFrame.selectedIndex].value;
            if (frameDetail !== "0") {
                // if a frame has been selected 
                costVal = frameDetail.split(":")[1];
                const totalCost = getTotalDetailCost(costVal);
                totalCostEl.textContent = "€" + totalCost.toFixed(2);
            }
        })
    }
}

function getTotalDetailCost(frameCost) {
    const salePrice = document.getElementById('sale-price');
    const price = document.getElementById('price');
    const qtyEl = document.getElementById('quantity');
    const qty = parseInt(qtyEl.options[qtyEl.selectedIndex].value);
    let total = 0;
    if (salePrice) {
        total = parseFloat(frameCost) + parseFloat(salePrice.textContent) * qty;
    } else {
        total = parseFloat(frameCost) + parseFloat(price.textContent) * qty;
    }
    return total;
}