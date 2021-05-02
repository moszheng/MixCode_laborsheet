//--------same_name--------

const laborname = document.getElementById("id_labor_name");
const laborbankname = document.getElementById("id_labor_bankname");
var samename = document.getElementById("name_check");

samename.addEventListener("change", function () {

    if (this.checked) {

        laborbankname.setAttribute("value", laborname.value);

        laborname.addEventListener("input", function (e) { //follow change
            laborbankname.setAttribute("value", laborname.value);
        });
    }
});

//---------price_calculate---------

const price = document.getElementById("id_price");
const form = document.querySelector("#form");

price.addEventListener("input", function (e) {


    if (price.value > 17618) {

        netamount_num = Math.round(price.value / 0.8809);
        incometex_num = Math.round(netamount_num  * 0.1);
        premium_num = Math.round(netamount_num * 0.0191);
    }
    else {
        netamount_num = price.value;
        incometex_num = 0;
        premium_num = 0;
    }

    //const netamount_num = price.value + incometex_num + premium_num;

    document.getElementById("netamount").innerHTML = netamount_num;
    document.getElementById("incometax").innerHTML = incometex_num;
    document.getElementById("premium").innerHTML = premium_num;
    

});

/*form.addEventListener("submit", function (e) { 
    e.preventDefault();
});*/

//---------Flie Preview-------
var loadFile_bank = function (event) {
    var output = document.getElementById('ID_bank_output');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function () {
        URL.revokeObjectURL(output.src) // free memory
    }
};

var loadFile_front = function (event) {
    var output = document.getElementById('ID_front_output');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function () {
        URL.revokeObjectURL(output.src) // free memory
    }
};
var loadFile_back = function (event) {
    var output = document.getElementById('ID_back_output');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function () {
        URL.revokeObjectURL(output.src) // free memory
    }
};
//---------簽名------------------

var canvas = document.querySelector("canvas");

var signaturePad = new SignaturePad(document.getElementById('signature-pad'), {
    backgroundColor: '#FFF',
    penColor: '#000',
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

//-------------------------------------

(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
        form.addEventListener('submit', function (event) {

            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
                form.classList.add('invalid-feedback')
            }

            form.classList.add('was-validated')
        }, false)
    })
})()