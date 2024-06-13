// cart.js
var updateBtns = document.getElementsByClassName("update-cart");

for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function(){
    var yerbaId = this.dataset.yerba;
    var action = this.dataset.action;
    console.log("yerbaId:", yerbaId, "action:", action);

    console.log("USER:", user);
    if (user === "AnonymousUser") {
      console.log("Not logged in");
    } else {
      updateUserOrder(yerbaId, action);
    }
  });
}

function updateUserOrder(yerbaId, action) {
  console.log("User is logged in, sending data...");

  var url = '/update_item/';

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ 'yerbaId': yerbaId, 'action': action })
  })
  .then((response) =>{
      return response.json();
    })
  .then((data) =>{
      console.log('data:', data);
      location.reload();
    });
}
