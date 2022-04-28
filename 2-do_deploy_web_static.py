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
        newpath = archive_path.replace('versions/', '')
        filename = newpath[:-4]
        filefolder = "/data/web_static/releases/{}".format(newpath)
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(filename))
        run('tar -xzf /tmp/{} -C {}'.format(newpath, arcfolder[:-4]))
        run('rm /tmp/{}'.format(newpath))
        run('mv {}/web_static/* {}/'.format(filefolder[:-4], filefolder[:-4]))
        run('rm -rf {}/web_static'.format(filefolder[:-4]))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(filefolder[:-4]))
        return True
    else:
        return False
