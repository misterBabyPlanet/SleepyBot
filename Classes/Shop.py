import Classes.Object as Object


class ShopObject:
    """ Shop object"""

    def __init__(self, json_object):
        self.JSON_objects = json_object

        def listObjects():
            objects_list = []
            for object in json_object.values():
                objects_list.append(Object.Object(object['name'], object['price'], object['picture_path']))

            return objects_list

        self.objectsList = listObjects()

    def getJSONObjects(self):
        return self.JSON_objects

    def setJSONObjects(self, new_json):
        self.JSON_objects = new_json

    def getObjectsList(self):
        return self.objectsList

    def setObjectsList(self, new_list):
        self.objectsList = new_list

    ###

    def printObjectsInformations(self):
        for shop_object in self.objectsList:

            dico_infos = {
                'name': shop_object.getName(),
                'price': shop_object.getPrice(),
                'picture_path': shop_object.getPicture_path()
            }

            print(f"{dico_infos['name']}\nprice : {dico_infos['price']}\npicture emplacement : {dico_infos['picture_path']}\n\n")