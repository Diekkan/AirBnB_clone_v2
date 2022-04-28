#!/usr/bin/python3
""" all steps done before"""


from fabric.api import run, put, local
import os.path
import datetime


env.hosts = ['100.26.47.97', '104.196.100.253']
env.user = 'ubuntu'


def do_pack():
    """ makes tgz compressed file """
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file = local("tar -czvf versions/web_static_{}.tgz web_static".format(now))
    if file:
        return("versions/web_static_{}".format(now))
    else:
        return None


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


def deploy():
    """ Both processes """
    filepath = do_pack()
    if filepath is None:
        return False
    return do_deploy(filepath)
