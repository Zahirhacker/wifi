<!DOCTYPE html>
<html lang="en" class="">
    <title>Hackerzahir Wifi</title>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=1020">
  </head>
  <style>
    table { border-spacing: 2px; border: 1px; }
    td { padding: 6px; }
  </style>
  <script type="text/javascript">
    function fill(data) {
      data.places.forEach(function logArrayElements(element, index, array) {
        var locationName  = document.createTextNode(element.name)
        var ssid  = document.createTextNode(element.SSID)
        var password  = document.createTextNode(element.password)

        var tableRef = document.getElementById('wifi-data').getElementsByTagName('tbody')[0];
        var newRow   = tableRef.insertRow(tableRef.rows.length);
        var newCellName  = newRow.insertCell(0);
        var newCellSSID  = newRow.insertCell(1);
        var newCellPassword  = newRow.insertCell(2);
        newCellName.appendChild(locationName);
        newCellSSID.appendChild(ssid);
        newCellPassword.appendChild(password);
      });
    }

    var request = new XMLHttpRequest();
    request.open('GET', 'https://raw.githubusercontent.com/beanieboi/hackerbeach-wifi/master/canoa.json', true);

    request.onload = function() {
      if (request.status >= 200 && request.status < 400) {
        // Success!
        var data = JSON.parse(request.responseText);
        fill(data);
      } else {
        // We reached our target server, but it returned an error

      }
    };

    request.onerror = function() {
      // There was a connection error of some sort
    };

    request.send();
  </script>
  <body>
    <table id="wifi-data">
      <thead>
        <tr>
          <th>Location</th>
          <th>SSID</th>
          <th>Password</th>
        </tr>
      </thead>
      <tbody>
      </tbody>
    </table>
  </body>
</html>
