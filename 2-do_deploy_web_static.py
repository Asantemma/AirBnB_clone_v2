#!/usr/bin/python3
"""A fabric script that distributes an archive to my web servers"""

import os
from fabric.api import *

env.hosts = ['100.26.225.229', '100.25.144.170']

def do_deploy(archive_path):
    """Shares archive to web servers"""
    try:
        try:
            if os.path.exists(archive_path):
                arc_tgz = archive_path.split("/")
                arg_save = arc_tgz[1]
                arc_tgz = arc_tgz[1].split('.')
                arc_tgz = arc_tgz[0]

                """Uploads archive to the server"""
                put(archive_path, '/tmp')

                """Saves the folder paths in variables"""
                uncomp_fold = '/data/web_static/releases/{}'.format(arc_tgz)
                tmp_location = '/tmp/{}'.format(arg_save)

                """Runs remote commands on the server"""
                run('mkdir -p {}'.format(uncomp_fold))
                run('tar -xvzf {} -C {}'.format(tmp_location, uncomp_fold))
                run('rm {}'.format(tmp_location))
                run('mv {}/web_static/* {}'.format(uncomp_fold, uncomp_fold))
                run('rm -rf {}/web_static'.format(uncomp_fold))
                run('rm -rf /data/web_static/current')
                run('ln -sf {} /data/web_static/current'.format(uncomp_fold))
                run('sudo service nginx restart')
                return True
            else:
                print('File does not exist')
                return False
        except Exception as err:
            print(err)
            return False
    except Exception:
        print('Error')
        return False
