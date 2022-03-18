console.log('heyyyyy')

const bar = document.getElementById('bar');
const nav = document.getElementById('navbar');
const close = document.getElementById('close');

if (bar) {
    bar.addEventListener('click', () => {
        nav.classList.add('active');

    })

}

if (close) {
    close.addEventListener('click', () => {
        nav.classList.remove('active');

    })

}


$(document).ready(function () {
    console.log('this is me');

    // + and - button
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);

        }

    })
    $('.decrement-btn').click(function (e) {
        e.preventDefault();

        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);

        }

    });

    $('.addToCartBtn').click(function (e) { 
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status)
            }
        });
        
    });

    // change quantity in cart


    $('.changeQuantity').click(function (e) {
        e.preventDefault();


        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                // alertify.success(response.status)
            }
        });


    });

    //    delete cart item
    $(document).on('click', '.delete-cart-item', function (e) {
        e.preventDefault();


        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-cart-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status)
                $('.cartdata').load(location.href + " .cartdata");
            }
        });

    });


    // add wishlist
    $('.addToWhisList').click(function (e) {
        e.preventDefault();


        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status)
            }
        });


    });


    // delete wishlist item

    $('.delete-wishlist-item').click(function (e) { 
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status)
                $('.wishdata').load(location.href + " .wishdata");
            }
        });
        
    });

    $('.payWithRazorPay').click(function (e) {
        e.preventDefault();

        var fname=$("[name='fname']").val();
        var lname=$("[name='lname']").val();
        var email=$("[name='email']").val();
        var phone=$("[name='phone']").val();
        var address=$("[name='address']").val();
        var city=$("[name='city']").val();
        var state=$("[name='state']").val();
        var country=$("[name='country']").val();
        var pincode=$("[name='pincode']").val();
        var token=$('[name="csrfmiddlewaretoken"]').val();

        if(fname==""|| lname=="" ||email==""|| phone=="" ||address==""|| city=="" ||state==""|| country=="" || pincode=="" )
        {
           
            swal("Alert!", "All Fields are mandatory!", "warning");

            return false;
        }
        else{
            $.ajax({
                method: "GET",
                url: "/proceeed-to-pay",
                success: function (response) {
                    // console.log(response);
                    var options = {
                        "key": "rzp_test_mVpsF9hHbHFTrw", // Enter the Key ID generated from the Dashboard
                        "amount":response.total_price * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Stone Store",
                        "description": "Thank you for buyin Shirto",
                        "image": "{% static 'media/logo.png' %}",
                        //"order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);
                            data={
                                 "fname" :fname,
                                 "lname": lname,
                                 "email":email,
                                 "phone":phone,
                                 "address" : address,
                                 "city":city,
                                 "state":state,
                                 "country": country,
                                 "pincode":pincode,
                                 "payment_mode":"Paid by Razorpay",
                                 "payment_id":responseb.razorpay_payment_id,
                                 csrfmiddlewaretoken:token
                            }
                            $.ajax({
                                type: "POST",
                                url: "/placeorder   ",
                                data: data,
                                success: function (responsec) {
                                    swal("Congratulations!",responsec.status, "success").then((value) => {
                                       window.location.href='/my-order'
                                    });
                                
                                }
                            });
                           
                        },
                        "prefill": {
                            "name": fname+" "+lname,
                            "email": email,
                            "contact": phone
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
        
                    
                }
            });
         
        }
        
    });






});
