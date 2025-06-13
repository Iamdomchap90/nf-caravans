(function () {
    // Use Django CMS modal hooks
    CMS.$(document).on('cms-ready', function () {
      const textarea = document.querySelector('#rich-text'); // Adjust if your field has a different ID
      if (textarea && !textarea.dataset.initialized) {
        textarea.dataset.initialized = true;
  
        ClassicEditor
          .create(textarea)
          .catch(error => console.error(error));
      }
    });
  })();
  