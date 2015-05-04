import logging
import logstash
import sys

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler("localhost", 5000, version=1))

logger.error("python-logstash: test logstash error message.")
logger.info("python-logstash: test logstash info message.")
logger.warning("python-logstash: test logstash warning message.")

# add extra field to logstash message
extra = {
    "test_string": "python version: " + repr(sys.version_info),
    "test_boolean": True,
    "test_dict": {"a": 1, "b": "c"},
    "test_float": 1.23,
    "test_integer": 123,
    "test_list": [1, 2, "3"],
}
logger.info('python-logstash: test extra fields', extra=extra)
