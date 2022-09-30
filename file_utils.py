import gridfs
from database import img
import os

fs = gridfs.GridFS(img)

def store_img(filepath):
      with open(filepath, 'rb') as f:
            contents = f.read()
      file_name = os.path.basename(filepath)
      file_id = fs.put(contents, filename=file_name)
      return file_id

def get_img(file_id):
      img_obj = fs.put(file_id)
      out = fs.get(img_obj)
      out.read()
      print(out)

if __name__=='__main__':
      id = store_img("static/product-images/fs.png")
      print(get_img(id))
