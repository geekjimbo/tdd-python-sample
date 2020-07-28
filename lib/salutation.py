class salutation(object):
    def hello_world(self, param=None):
      payload = "Hello World"
      if param is not None:
         payload = "Hello World to you {} !".format(param)
      return {"status": 200, "message": "Success", "payload": payload}

