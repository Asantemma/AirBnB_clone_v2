#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the
contents of the web_static folder using the function do_pack."""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Packs all the contents in the web_static folder
    as a .tgz archive"""

    try:
        local("mkdir -p versions")
        time = datetime.now()
        date_string = '%Y%m%d%H%M%S'
        date = time.strftime(date_string)

        file_path = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(file_path))
        return file_path

    except Exception:
        return None
