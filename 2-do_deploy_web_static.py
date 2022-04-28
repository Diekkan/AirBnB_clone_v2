#!/usr/bin/python3
""" a Fabric script that distributes an archive to your
web servers, using the function do_deploy """

from fabric.api import run, put, local
import os.path

env.hosts = ['100.26.47.97', '104.196.100.253']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ do_deploy deploys a file onto the servers """
    if (os.path.exists(archive_path)):
        new_path = archive_path.replace('versions/', '')
        file_name = new_path[:-4]
        arc_folder = "/data/web_static/releases/{}".format(new_path)
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(file_name))
        run('tar -xzf /tmp/{} -C {}'.format(new_path, arc_folder[:-4]))
        run('rm /tmp/{}'.format(new_path))
        run('mv {}/web_static/* {}/'.format(arc_folder[:-4], arc_folder[:-4]))
        run('rm -rf {}/web_static'.format(arc_folder[:-4]))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(arc_folder[:-4]))
        return True
    else:
        return False
