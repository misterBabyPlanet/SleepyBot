import Classes.Object as Object


class ShopObject:
    """ Shop object"""

    def __init__(self, JSON_objects):
        self.JSON_objects = JSON_objects

        def listObjects():
            list = []
            for object in JSON_objects.values():
                list.append(Object(object['name'], object['price'], object['picture_path']))

            return list

        self.objectsList = listObjects()

    def getJSONObjects(self):
        return self.JSON_objects

    def setJSONObjects(self, new_JSON):
        self.JSON_objects = new_JSON

    def getObjectsList(self):
        return self.objectsList

    def setObjectsList(self, new_list):
        self.objectsList = new_list

    ###

    def printObjectsInformations(self):
        for object in self.objectsList:

            dico_infos = {
                'name': object.getName(),
                'price': object.getPrice(),
                'picture_path': object.getPicture_path()
            }

            print(f"{dico_infos['name']}\nprice : {dico_infos['price']}\npicture emplacement : {dico_infos['picture_path']}\n\n")