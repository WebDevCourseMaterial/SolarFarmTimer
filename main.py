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

from google.appengine.ext import ndb
import jinja2
import webapp2

from models import SunScore

# Jinja environment instance necessary to use Jinja templates.
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), autoescape=True)

# Generic key used to group SunScores into an entity group.
_PARENT_KEY = ndb.Key("Entity", 'sunscore_root')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        sunscores = SunScore.query(ancestor=_PARENT_KEY).order(-SunScore.sun_score).fetch()
        template = jinja_env.get_template("templates/solarfarmtimer.html")
        self.response.out.write(template.render({'sunscores': sunscores}))

    def post(self):
        new_score = SunScore(parent=_PARENT_KEY,
                               team=self.request.get('team'),
                               sun_average_during_run=self.request.get('sun_average_during_run'),
                               final_sun_power=self.request.get('final_sun_power'),
                               sun_score=self.request.get('sun_score'))
        new_score.put()
        self.redirect(self.request.referer)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)