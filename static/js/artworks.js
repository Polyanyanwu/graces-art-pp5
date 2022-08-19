/*jshint esversion: 6 */
// Artworks app JavaScript codes

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

// After page loads run the startUp function
document.addEventListener("DOMContentLoaded", startUp);

function getSkuPrefix() {
    if (document.getElementById('add-artwork-form')) {
        const sku = document.querySelector('#id_sku');
        const genre = document.querySelector('#id_genre');
        const artist = document.querySelector('#id_artist');
        const style = document.querySelector('#id_style');

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
            let sku_txt = "ART";
            let val;
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
        };
    }
}


function sort_selection() {
    if (document.getElementById('#select-sort')) {
        document.getElementById('#select-sort').change(function () {
            const selector = $(this);
            const currentUrl = new URL(window.location);

            const selectedVal = selector.val();
            if (selectedVal != "reset") {
                const sort = selectedVal.split("_")[0];
                const direction = selectedVal.split("_")[1];

                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);

                window.location.replace(currentUrl);
            } else {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");
                window.location.replace(currentUrl);
            }
        });
    }
}

function artDetails() {

    if (document.querySelector('#select_frame')) {
        const frameCost = document.querySelector('#frame-cost');
        const selectFrame = document.querySelector('#select_frame');
        const totalCostEl = document.querySelector('#total-cost');
        const qtyEl = document.getElementById('quantity');
        const frameSelectActionBtn = document.getElementById('frame-action-btn');

        selectFrame.addEventListener('change', function (e) {

            const frameDetail = selectFrame.options[selectFrame.selectedIndex].value;
            if (frameDetail.split(":")[0] == '0') {
                totalCostEl.textContent = "";
                frameSelectActionBtn.setAttribute('value', "None" + ":" + '0');
                frameSelectActionBtn.click();
                return;
            }

            const frameId = frameDetail.split(":")[0];
            const costVal = frameDetail.split(":")[1];
            frameCost.textContent = "€" + costVal;
            const totalCost = getTotalDetailCost(costVal);
            totalCostEl.textContent = "€" + totalCost.toFixed(2);
            frameSelectActionBtn.setAttribute('value', frameId + ":" + qtyEl.options[qtyEl.selectedIndex].value);
            frameSelectActionBtn.click();

        });

        qtyEl.addEventListener('change', function (e) {
            const artFrameCost = document.querySelector('#art-and-frame');
            if (artFrameCost.textContent) {
                const totalCost = getTotalDetailCost();
                totalCostEl.textContent = totalCost.toFixed(2);
            }
        });
    }
}

// When quantity changes recalculate total price
function getTotalDetailCost() {
    const qtyEl = document.getElementById('quantity');
    const artFrameCost = document.querySelector('#art-and-frame').textContent;
    const qty = parseInt(qtyEl.options[qtyEl.selectedIndex].value);
    let total = 0;
    if (artFrameCost) {
        total = parseFloat(artFrameCost) * qty;
    }
    return total;
}

if (document.querySelector('#update-bag-form')) {

    // Select quantity change on bag display
    const qtyEl = document.querySelectorAll('.quantity');
    qtyEl.forEach(btn => btn.addEventListener('change', function (e) {
        const qtySelected = e.target;
        const qty_changed = qtySelected.options[qtySelected.selectedIndex].value;
        const rec_id = qtySelected.dataset.record_id;
        document.getElementById("change-qty-btn").value = rec_id + ":" + qty_changed;
        document.getElementById('change-qty-btn').click();
    }));

    // Select frame change on bag display
    const frameEl = document.querySelectorAll('.select-frame');
    frameEl.forEach(btn => btn.addEventListener('change', function (e) {
        const frameSelected = e.target;
        const new_frame = frameSelected.options[frameSelected.selectedIndex].value;
        const rec_id = frameSelected.dataset.record_id;
        document.getElementById("change-frame-btn").value = rec_id + ":" + new_frame;
        document.getElementById('change-frame-btn').click();
    }));

}