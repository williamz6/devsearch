const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//suppose the `id` attribute of element is `message`
  setTimeout(function() {
    $('#message').fadeOut('slow'); 
  }, 3000);
  // Timeout is 3 sec