# encoding: utf-8
import cetacean

class Resource(object):

    """Respresents a HAL resource."""

    def __init__(self, raw):
        """Pass it a string containing HAL.

        :raw: A string containing a HAL document.

        """
        self._hal = cetacean._parse_hal(raw)


    def get_uri(self, rel):
        """Gets a URI from the document for a given rel.

        :rel: A string matching an expected rel
        :returns: A string that is the URI in question.

        """
        if unicode(rel) not in self.links: return None

        return self.links[unicode(rel)]['href']


    @property
    def links(self):
        """The links part of the HAL document.

        """
        return self._hal['_links'] if '_links' in self._hal else {}

    def __getitem__(self, attribute_name):
        """Access to the attributes of the resource. Like a dictionary.
        :returns: The value of the attribute.

        """
        return self._hal[attribute_name]

    def get(self, *args):
        """Access to the attributes of the resouse. Like a dictionary.
        :returns: The value of the attribute or None.

        """
        return self._hal.get(*args)
