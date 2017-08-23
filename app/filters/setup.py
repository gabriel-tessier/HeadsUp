# -*- coding: utf8 -*-

from app import app
from app.helpers import PaginationHelper
import config
import datetime

# Setup trim and strip for blocks
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.context_processor
def utility_processor():
    # Send the current date & time
    today = datetime.date.today()

    return dict(pag=PaginationHelper.pag,
                today=today,
                config=config,
                site_name=config.SITE_NAME)
