// pkg.js
mergeInto(LibraryManager.library, {
  js_add: function (a, b) {
    return a + b;
  },

  js_console_log_int: function (param) {
    console.log("js_console_log_int: " + param);
  },
});
