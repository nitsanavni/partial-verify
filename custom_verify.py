from approvaltests import verify, Options
from functools import partial


custom_options = Options().with_scrubber(lambda s: s.lower())

verify = partial(verify, options=custom_options)
