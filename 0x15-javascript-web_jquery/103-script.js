/* global $ */
$(document).ready(function () {
  function fetchtrans () {
    const code = $('#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + code,
      success: function (data) {
        $('#hello').html(data.hello);
      }
    });
  }
  $('#btn_translate').click(fetchtrans);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        fetchtrans();
      }
    });
  });
});
