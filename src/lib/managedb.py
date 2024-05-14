import pathlib
import json


class ManageDB:
  __file_address = "{0}/src/db/data.json".format(pathlib.Path().absolute())
  
  def read_products(self):
    with open(self.__file_address, "r") as file:
      return json.loads(file.read())
    
  def write_products(self, product):
    with open(self.__file_address, "w") as file:
      file.write(json.dumps(product))