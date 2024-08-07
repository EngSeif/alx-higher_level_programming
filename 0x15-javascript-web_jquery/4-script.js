/* global $ */
$('#toggle_header').click(
  function () {
    if ($('#toggle_header').hasClass('red')) {
      $('#toggle_header').removeClass('red').addClass('green');
    } else {
      $('#toggle_header').removeClass('green').addClass('red');
    }
  });
