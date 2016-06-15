import webapp2
import simplejson as json
import urllib2

urlb = "http://api.wunderground.com/api/Your_api_key/conditions/q/"
urle = ".json"
MAIN_PAGE_HTML = """\
<!doctype html>
 <html>
  <head>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

  <!-- Optional theme -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

  <!-- Latest compiled and minified JavaScript -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
    <script>
        function myFunction(){
        var d = new Date();
        var time = d.getHours();
        if (time >= 4 && time < 12) {
         document.body.style.backgroundImage = "url('img/mng.jpg')";
         document.body.style.color = "#fff";
         document.body.style.backgroundRepeat = "no-repeat";
         }
         if (time >= 12 && time < 18)  {
         document.body.style.backgroundImage = "url('img/aft.jpg')";
         document.body.style.backgroundRepeat = "no-repeat";
         }
         if (time >= 18) {
         document.body.style.backgroundImage = "url('img/ngt.jpg')";
         document.body.style.color = "#fff";
         document.body.style.backgroundRepeat = "no-repeat";

         }
         if(time>=0 && time<4)
         {
          document.body.style.backgroundImage = "url('img/ngt.jpg')"
          document.body.style.backgroundRepeat = "no-repeat";
         }
        }
    </script>
  </head>
  <body onLoad = "myFunction()">
    <center><h1 style="padding-top:10%"><i>Weather</i> on <i>ZipCode</i></h1>
      <p>(Note: Only Valid for US)</p>
      <form method="post" class="form-group">
        <h3>Enter valid Zipcode</h3><br>
        <p><input class="form-control" style="width:25%" type="textarea" name="ezip" placeholder="Enter Valid ZipCode" required></input></p><br>
        <p><input type="submit" class="btn btn-success"></input></p>
      </form>
    </center>
  </body>
 </html>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
        # Create the FORM
        self.response.write(MAIN_PAGE_HTML)

    def post(self):
        symbol_entered = self.request.get('ezip')
        url = urllib2.urlopen(urlb + symbol_entered + urle)

        parsed_json = json.loads(url.read())
        location = parsed_json['current_observation']['display_location']['city']
        temp_f = parsed_json['current_observation']['temp_f']
        temp_c = parsed_json['current_observation']['temp_c']
        humidity = parsed_json['current_observation']['relative_humidity']
        wind = parsed_json['current_observation']['wind_string']
        wind_mph = parsed_json['current_observation']['wind_mph']
        time = parsed_json['current_observation']['observation_time_rfc822']
        local_time = parsed_json['current_observation']['local_time_rfc822']
        weather = parsed_json['current_observation']['weather']
        feels_f = parsed_json['current_observation']['feelslike_f']
        feels_c = parsed_json['current_observation']['feelslike_c']
        visibility = parsed_json['current_observation']['visibility_mi']
        ICON = parsed_json['current_observation']['icon']




        self.response.write('<html><head><link rel="stylesheet" href="css/style.css"><link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script><script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script><script src="js/style.js"></script></head>')
        self.response.write('<body style="padding-top:100px"><center><table style="width:750px"><thead><tr><th colspan="3" style="text-align:center"><h2>Current Temperature of %s </h2>  </th></tr></thead>' % (location))
        self.response.write('<tr><td style="text-align:center">weather </td><td style="text-align:center"> %s </td>' % (weather))
        self.response.write('<td style="text-align:center"><img src="http://icons.wxug.com/i/c/k/%s.gif"/></td></tr> ' % (ICON))
        self.response.write('<tr><td style="text-align:center">Temperature</td> <td style="text-align:center"> %s F </td><td style="text-align:center"> %s C</td>' % (temp_f, temp_c))
        self.response.write('<tr><td style="text-align:center">Feels Like</td> <td style="text-align:center"> %s F </td><td style="text-align:center"> %s C</td>' % (feels_f, feels_c))
        self.response.write('<tr><td style="text-align:center">Wind</td><td style="text-align:center"> %s</td> <td style="text-align:center"> %s mph</td></tr>' % (wind,wind_mph))
        self.response.write('<tr><td style="text-align:center">Humidity</td><td colspan="2" style="text-align:center">%s</td></tr>' % (humidity))
        self.response.write('<tr><td style="text-align:center">visibility</td><td colspan="2" style="text-align:center">%s</td></tr>' % (visibility))
        self.response.write('</table></center></body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
