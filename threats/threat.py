import urllib2
import json
from helpers import is_valid_ipv4_address


class IPDetails(object):
    def __init__(self, *args, **kw):
        ip = args[0]

        self.id = ""
        self.reputation_val = 0
        self.first_activity = ""
        self.last_activity = ""
        self.activities = []
        self.activity_types = ""
        self.is_valid = False
        self.error_status = ""

        r = Reputation().get_details(ip)

        if r is None:
            self.error_status = "no_ip_given"
        elif r == "ip_error":
            self.error_status = "invalid_ip_given"
        elif r == "fetch_error":
            self.error_status = "ip_fetch_failed"
        else:
            self.is_valid = True

        # parse out any valid information from the response now
        if type(r) is dict:
            self.address = ip

            activities = []
            a_types = set()
            f_date = "0"
            l_date = "0"

            for k, v in r.iteritems():
                if k == "_id":
                    self.id = v["$id"]
                elif k == "reputation_val":
                    self.reputation_val = v
                elif k == "activities":
                    for l in v:
                        if "name" in l:
                            name = l["name"]
                        else:
                            name = ""
                        if "first_date" in l:
                            first_date = l['first_date']['sec']
                            if int(f_date) == 0:
                                f_date = first_date
                            else:
                                if int(first_date) < int(f_date):
                                    f_date = first_date
                        else:
                            first_date = ""
                        if "last_date" in l:
                            last_date = l['last_date']['sec']
                            if int(last_date) > int(l_date):
                                l_date = last_date
                        else:
                            last_date = ""
                        d = {"activity_type": name, "first_date": first_date, "last_date": last_date}
                        activities.append(d)
                        a_types.add(name)

            self.activities = activities
            self.activity_types = list(a_types)
            self.first_activity = f_date
            self.last_activity = l_date
        else:
            self.input = ip  # no response, use input instead of address
        return


class Reputation(object):
    @staticmethod
    def get_details(ip):
        if ip:  # check for an ip address (negated w/ url dispatcher)
            if is_valid_ipv4_address(ip):  # validate the ip address
                try:
                    # fetch the results from the alienvault source
                    url = "http://reputation.alienvault.com/panel/ip_json.php?ip=" + ip
                    response = urllib2.urlopen(url)
                    try:
                        return json.load(response)
                    except:
                        return ""  # no json object return empty string
                except:
                    return "fetch_error"
            else:
                return "ip_error"
        else:
            return None
