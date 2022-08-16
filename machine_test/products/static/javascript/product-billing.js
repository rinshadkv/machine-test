// $(document).ready(function(){


    function update_quantity(qty, id, amount,) {
        totalprice = parseInt(amount) * parseInt(qty.value);
       
        $.ajax({
            url: '/products/updateQuantity',
            type: 'get',
            data: {
                qty: parseInt(qty.value),
                id: id,
            },
            success: function(response) {
                console.log(response.price);
                $("#total_ammount").val(response.price);
            }
        })
    }
   

// })