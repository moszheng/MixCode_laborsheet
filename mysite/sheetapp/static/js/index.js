/*/--------same_address--------

const ResidentAddress = document.getElementById("ResidentAddress");
const CurrentAddress = document.getElementById("CurrentAddress");
var address_check = document.getElementById("address_check");

address_check.addEventListener("change", function () {

    if (this.checked) {
        CurrentAddress.setAttribute("value", ResidentAddress.value);
    }

});*/

//---------price_calculate---------

const price = document.getElementById("price");
const form = document.querySelector("#form");

price.addEventListener("input", function (e) {


    if (price.value > 20000) {
        incometex_num = Math.round(price.value * 0.1);
        premium_num = Math.round(price.value * 0.0191);
    }
    else {
        incometex_num = 0;
        premium_num = 0;
    }

    const netamount_num = price.value - incometex_num - premium_num;

    document.getElementById("incometax").innerHTML = incometex_num;
    document.getElementById("premium").innerHTML = premium_num;
    document.getElementById("netamount").innerHTML = netamount_num;

});



/*form.addEventListener("submit", function (e) { 
    e.preventDefault();
});*/

//---------Flie Preview-------

var loadFile = function (event) {
    var output = document.getElementById('ID_front_output');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function () {
        URL.revokeObjectURL(output.src) // free memory
    }
};

//---------簽名------------------

var canvas = document.querySelector("canvas");

var signaturePad = new SignaturePad(document.getElementById('signature-pad'), {
    backgroundColor: 'rgba(255, 255, 255)',
    penColor: 'rgb(0, 0, 0)',
    minDistance: 1
});

var saveButton = document.getElementById('save');
var cancelButton = document.getElementById('clear');

saveButton.addEventListener('click', function (event) {

    if (signaturePad.isEmpty()) {
        return alert("請簽名在上方");
    }

    var data = signaturePad.toDataURL('image/png');

    var signature_output = document.getElementById('labor_signature_output');

    signature_output.src = data;
    //document.getElementById("id_labor_signature").value = data;
    labor_signature.value = data;

    signature_output.onload = function () {
        URL.revokeObjectURL(signature_output.src) // free memory
        
    }

    console.log(data);

    //window.open(data);
});

cancelButton.addEventListener('click', function (event) {
    signaturePad.clear();
});