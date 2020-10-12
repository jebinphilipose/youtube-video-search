$(document).ready(function () {
  // For select input
  $('select').formSelect();

  // For sidenav
  $('.sidenav').sidenav();

  // Filter Form
  $("#filter-form select").on('change', function (e) {
      $("#filter-form").submit();
  });
});
