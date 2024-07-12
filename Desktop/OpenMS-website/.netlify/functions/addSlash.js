const fetch = require("node-fetch");

exports.handler = function (event, context, callback) {
  if (event.path.endsWith("documentation/") || event.path.endsWith("current_doxygen/")) {
    // Return the page root
    fetch("https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/release/latest/")
      .then((response) => response.text())
      .then((body) => {
        callback(null, {
          statusCode: 200,
          body,
        });
      });
  } else if (event.path.endsWith("develop_doxygen/")) {
    // Return the page root
    fetch("https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/nightly/")
    .then((response) => response.text())
    .then((body) => {
        callback(null, {
        statusCode: 200,
        body,
        });
    });
  } else {
    // Return a redirect to /page/
    const location = event.path + "/";
    callback(null, {
      statusCode: 301,
      headers: { location },
    });
  }
};