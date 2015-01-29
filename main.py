#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" xml:lang="en-us" lang="en-us"><!-- InstanceBegin template="/Templates/_main.dwt.php" codeOutsideHTMLIsLocked="true" --><head><title>MEAT&CO.</title><link href="/css/bootstrap.css" rel="stylesheet"></head><body background="/meat.png" style="background-position: -250px 0px"><h1>Hello</h1></body></html>')


import logging
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" xml:lang="en-us" lang="en-us"><!-- InstanceBegin template="/Templates/_main.dwt.php" codeOutsideHTMLIsLocked="true" --><head><title>MEAT&CO.</title><link href="/css/bootstrap.css" rel="stylesheet"></head><body><div class="container-fluid"><div class="row"><div class="col-md-4"></div><div class="col-md-4"><h1 align="center">Meat&Co.</h1></div><div class="col-md-4"></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/1.JPG"/></div><div class="col-md-4"><img src="/lipstick-gif.gif"/></div><div class="col-md-4"><img src="/20.JPG"/></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/2.JPG"/></div><div class="col-md-4"><img src="/armpits-gif.gif"/></div><div class="col-md-4"><img src="/19.JPG"/></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/3.JPG"/></div><div class="col-md-4"><img src="/2.gif"/></div><div class="col-md-4"><img src="/18.JPG"/></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/4.JPG"/></div><div class="col-md-4"><img src="/Julia-Apples-GIF.gif"/></div><div class="col-md-4"><img src="/17.JPG"/></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/5.JPG"/></div><div class="col-md-4"><img src="/hands-gif.gif"/></div><div class="col-md-4"><img src="/16.JPG"/></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/6.JPG"/></div><div class="col-md-4"><img src="/1.gif"/></div><div class="col-md-4"><img src="/15.JPG"/></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/7.JPG"/></div><div class="col-md-4"><img src="/buns-for-site.gif"/></div><div class="col-md-4"><img src="/14.JPG"/></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/8.JPG"/></div><div class="col-md-4"><img src="/2.gif"/></div><div class="col-md-4"><img src="/13.JPG"/></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/9.JPG"/></div><div class="col-md-4"><img src="/Julia-Apples-GIF.gif"/></div><div class="col-md-4"><img src="/12.JPG"/></div></div><div class="row"><div style="height:55px;" class="col-md-4"></div><div class="col-md-4"></div><div class="col-md-4"></div></div><div class="row"><div class="col-md-4"><img src="/10.JPG"/></div><div class="col-md-4"><img src="/lipstick-gif.gif"/></div><div class="col-md-4"><img src="/11.JPG"/></div></div></div></body></html>')
	def handle_404(request, response, exception):
	    logging.exception(exception)
	    response.write('Oops! I could swear this page was here bro!')
	    response.set_status(404)

	def handle_500(request, response, exception):
	    logging.exception(exception)
	    response.write('A server error occurred!')
	    response.set_status(500)

	app.error_handlers[404] = handle_404
	app.error_handlers[500] = handle_500


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
