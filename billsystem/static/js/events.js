var category_items = document.getElementsByClassName('category-item');

for(var i=0; i<category_items.length; i++) {
    category_items[i].addEventListener('click', (e)=>{
        let ele_name =(e.target.id);
        let elId = ele_name.split('_');
        if (elId != null) {
            let queryId = elId[1];
            console.log(`getting api from query Id ${queryId}`);
            fetchProduct(queryId)
        }
        return null;
    });
}

async function fetchProduct(productId) {
    let response_call = await fetch(`/category/${productId}`)
    let data = await response_call.json();

    // parse the returned data
    if (response_call.status === 200) {
        let products = (data['commodity_set']);
        if (products.length == 0) { return}
        products.forEach(item => console.log(item))
        return insertProducts(products)

    }
    
    else {
        console.error("Returned 400 ERR.")
    }
}


function insertProducts(items){
    var product_template = $('#product-create').html();
    var ProductTemplateScript = Handlebars.compile(product_template);

    var context = {"items":items}
    var html = ProductTemplateScript(context)
    $("#category-products").empty();
    $('#category-products').append(html);
}