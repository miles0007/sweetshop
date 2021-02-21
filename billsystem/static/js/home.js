// global variables
var productEls = document.querySelectorAll('.product');
var rightBarName = document.getElementsByName('product')[0];
var priceProduct = document.getElementById('el_price');
var minUnit = document.getElementById('min_unit');
var formEl = document.getElementById('fixerForm');
var formBtn = formEl.querySelector('button');
var itemID = formEl.querySelector('#item_id');

document.addEventListener('DOMContentLoaded', function() {
    // set inital status of the name bar to No Value.
    requestProducts(productEls)
    rightBarName.setAttribute('value', "No Element selected.")
    
    // set inital status of button as disabled
    formBtn.disabled = true;
});

function requestProducts(productEls){
    productEls.forEach(product => {
        product.addEventListener('click', function(e) {
            // get parentElement of click attribute and its Name in HTML ele.
            let parentEle = (e.target.parentNode);
            let namingEls = parentEle.querySelector('h4');
            let priceEl = parentEle.querySelector('h5>.price');
            let minEl = parentEle.querySelector('h6');
            console.log(parentEle.id);
            rightBarName.setAttribute("value", namingEls.innerHTML);
            priceProduct.innerHTML = priceEl.innerHTML; // show pricing
            minUnit.innerHTML = minEl.innerHTML;        // show minimum Unit of Product
            itemID.setAttribute("value", parentEle.id);
            // button gone to show state
            formBtn.disabled = false;
        });
    });
}

// form validation 
formEl.addEventListener('submit', function(event) {
    event.preventDefault()
    let elWeight = document.forms['fixerForm']['weight'].value;
    let elName = document.forms['fixerForm']['product'].value;
    let elID = document.forms['fixerForm']['item_id'].value;
    let elUnit = document.forms['fixerForm']['unit'].value;
    
    elCalPrice = Number(priceProduct.innerHTML)*elWeight;
    if (elWeight == "") {
        alert("Please Fill out the weight to add..");
        return false;
    }
    console.log(elName, 'product ID:', elID, 'weight',elWeight, elUnit);
    // clear form
    $('#fixerForm').trigger('reset');
    tableInsert(elWeight, elName, elID, elUnit, elCalPrice);
    
});

function tableInsert(elWeight, elName, elID, elUnit, calPrice){
    // Retrieve the template data from the HTML (jQuery is used here).
    var template = $('#table-inserter').html();

    // Compile the template data into a function
    var templateScript = Handlebars.compile(template);

    var context = {"product" : elName, "quantity" : elWeight+" "+elUnit, "price":calPrice, "product_id":elID};
    var html = templateScript(context);
    $('#products_table').append(html);
    priceUpdate()
}


function priceUpdate() {
    let total = 0;
    let prices = document.querySelectorAll('.table_price');
    let elPrice = document.getElementById('total_price');
    prices.forEach(price => {
        total += Number(price.innerHTML);
    });
    elPrice.innerHTML = total;
}


var product_ele = document.getElementById("category-products");
product_ele.addEventListener('DOMNodeInserted', () => {
    let newProdcuts = document.querySelectorAll('.product');
    requestProducts(newProdcuts)
});