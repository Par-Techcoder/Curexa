console.log("Toast script loaded!");
(function() {
  // ----- Override window.fetch -----
  const originalFetch = window.fetch;
  window.fetch = function(...args) {
    return originalFetch(...args).then(response => {
      // Clone response so we can safely read its JSON
      const clonedResponse = response.clone();
      clonedResponse.json().then(data => {
        if (data && (data.success || data.error) && data.message) {
          if (data.redirect) {
            // Store message details for later display after redirect
            sessionStorage.setItem('loginToastMessage', JSON.stringify({
              message: data.message,
              icon: data.success ? "success" : "error"
            }));
          } else {
            let icon = "info";
            if (data.success) {
              icon = "success";
            } else if (data.error) {
              icon = "error";
            }
            Swal.fire({
              toast: true,
              position: 'top-end',
              icon: icon,
              title: data.message,
              timer: 3000,
              timerProgressBar: true,
              showConfirmButton: false
            });
          }
        }
      }).catch(error => {
        // If not JSON, do nothing.
      });
      return response;
    });
  };

  // ----- Override jQuery's $.ajax -----
  if (window.jQuery) {
    const originalAjax = $.ajax;
    $.ajax = function(options) {
      // Save original callbacks.
      const originalSuccess = options.success;
      const originalError = options.error;

      // Wrap the success callback.
      options.success = function(data, textStatus, jqXHR) {
        if (data && (data.success || data.error) && data.message) {
          if (data.redirect) {
            sessionStorage.setItem('loginToastMessage', JSON.stringify({
              message: data.message,
              icon: data.success ? "success" : "error"
            }));
          } else {
            let icon = "info";
            if (data.success) {
              icon = "success";
            } else if (data.error) {
              icon = "error";
            }
            Swal.fire({
              toast: true,
              position: 'top-end',
              icon: icon,
              title: data.message,
              timer: 3000,
              timerProgressBar: true,
              showConfirmButton: false
            });
          }
        }
        if (originalSuccess) {
          originalSuccess(data, textStatus, jqXHR);
        }
      };

      // Wrap the error callback.
      options.error = function(jqXHR, textStatus, errorThrown) {
        let data = null;
        try {
          data = jqXHR.responseJSON;
        } catch (e) {
          data = null;
        }
        if (data && (data.success || data.error) && data.message) {
          if (data.redirect) {
            sessionStorage.setItem('loginToastMessage', JSON.stringify({
              message: data.message,
              icon: data.success ? "success" : "error"
            }));
          } else {
            let icon = "info";
            if (data.success) {
              icon = "success";
            } else if (data.error) {
              icon = "error";
            }
            Swal.fire({
              toast: true,
              position: 'top-end',
              icon: icon,
              title: data.message,
              timer: 3000,
              timerProgressBar: true,
              showConfirmButton: false
            });
          }
        }
        if (originalError) {
          originalError(jqXHR, textStatus, errorThrown);
        }
      };

      return originalAjax(options);
    };
  }

  // ----- Display stored toast message and Django Messages on full page loads -----
  document.addEventListener('DOMContentLoaded', function() {
    // Check for stored toast message from sessionStorage
    const storedToast = sessionStorage.getItem('loginToastMessage');
    if (storedToast) {
      const toastData = JSON.parse(storedToast);
      Swal.fire({
        toast: true,
        position: 'top-end',
        icon: toastData.icon,
        title: toastData.message,
        timer: 3000,
        timerProgressBar: true,
        showConfirmButton: false
      });
      sessionStorage.removeItem('loginToastMessage');
    }

    if (window.djangoMessages && Array.isArray(window.djangoMessages)) {
      window.djangoMessages.forEach(function(msg) {
        let icon = "info";
        if (msg.tags.indexOf("success") !== -1) {
          icon = "success";
        } else if (msg.tags.indexOf("error") !== -1) {
          icon = "error";
        } else if (msg.tags.indexOf("warning") !== -1) {
          icon = "warning";
        }
        Swal.fire({
          toast: true,
          position: 'top-end',
          icon: icon,
          title: msg.message,
          timer: 3000,
          timerProgressBar: true,
          showConfirmButton: false
        });
      });
    }
  });
})();
