
from google.appengine.ext import ndb

class SunScore(ndb.Model):
    """ A team's score from the Solar Farm Timer. """
    team = ndb.StringProperty()
    sun_average_during_run = ndb.FloatProperty()
    final_sun_power = ndb.FloatProperty()
    sun_score = ndb.FloatProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    