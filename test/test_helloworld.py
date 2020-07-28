import pytest
import logging
from lib.salutation import salutation

@pytest.mark.test_display_helloworld
def test_display_hw():
    logger = logging.getLogger("helloworld")
    hw = salutation()
    resp = hw.hello_world()

    # TODO: refactor this with dynamic schema validation: {"status": 200, "message": "", "payload": ""} 
    # TODO: refactor to extract err messages into files
    if "status" not in resp or "message" not in resp or "payload" not in resp:
       logger.debug("ERROR: returning message not in expected format")

    if resp["status"] != 200:
       logger.debug("ERROR: exception thrown {}".format(resp["message"]))

    assert  "hello world" in resp["payload"].lower()
