
import centreonapi.webservice.configuration.factory.contactfactory as contactfactory
import centreonapi.webservice.configuration.factory.contactgroupfactory as contactgroupfactory



class ContactGroup(contactgroupfactory.ObjContactGroup):

    def __init__(self, properties):
        self.id = properties.get('id')
        self.name = properties.get('name')


class Contact(contactfactory.ObjContact):

    def __init__(self, properties):
        self.id = properties.get('id')
        self.name = properties.get('name')