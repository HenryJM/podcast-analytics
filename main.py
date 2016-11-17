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
#
import os
import webapp2
import jinja2
import logging
import json
import urllib
import analytics
import idnamemethod

JINJA_ENVIRONMENT_AE = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT_AE.get_template('templates/main.html')
        self.response.write(template.render({
			'chart_names': idnamemethod.NAMES,
			'chart_name_to_method': idnamemethod.NAME_TO_METHOD,
            'example_podcasts' : idnamemethod.EXAMPLE_PODCASTS
		}))
        
class PlotHandler(webapp2.RequestHandler):
    def get(self):
        rssUrl = (self.request.GET['rssUrl']).encode('utf-8')
        rssUrl = urllib.unquote(urllib.unquote(rssUrl))
        charts = self.request.GET.getall('charts[]')
        self.response.write(json.dumps(analytics.make_plots(rssUrl, charts)))
        
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/plot', PlotHandler)
], debug=True)
