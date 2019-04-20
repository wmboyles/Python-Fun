from urllib.parse import urlencode

try: import urllib.request as urllib2
except ImportError: import urllib2


class WolframCloud:

    def wolfram_cloud_call(self, **args):
        arguments = dict([(key, arg) for key, arg in args.items()])
        result = urllib2.urlopen("###Mathematica-generated URL", urlencode(arguments).encode("utf8"))
        return result.read()

    def call(self, s):
        textresult = self.wolfram_cloud_call(s=s)
        return textresult
