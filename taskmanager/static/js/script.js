document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });
  
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmm, yyyy",
      i18n: {done: "Select"}
    });

    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    document.addEventListener('DOMContentLoaded', function() {
      let collapsibles = document.querySelectorAll('.collapsible');
      M.Collapsible.init(collapsibles);
    });
