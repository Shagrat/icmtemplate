from __future__ import with_statement
from fabric.api import sudo, env, run, get, local, cd, prefix, put
from contextlib import contextmanager as _contextmanager
from fabric.decorators import hosts

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env.hosts = ['s1.icmconsulting.com']
env.shell = 'bash -c'
env.directory = '/usr/home/{{ project_name }}/{{ project_name }}'
env.activate = 'source /usr/home/{{ project_name }}/env/bin/activate'
dbname = dbuser = '{{ project_name }}'
hostuser = hostgroup = '{{ project_name }}'
project = '{{ project_name }}'
wsgifilename = '{{ project_name }}'


@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield


def pull():
    with virtualenv():
        sudo('git pull origin master')
        sudo('chown -R %s:%s .' % (hostuser, hostgroup))


def initdb(islocal=False):
    if not islocal:
        run('/usr/pgsql-9.3/bin/createuser -U postgres -d %s' % dbuser)
        run('/usr/pgsql-9.3/bin/createdb -U %s %s' % (dbuser, dbname))
    local('createuser -U postgres -d %s' % dbuser)
    local('createdb -U %s %s' % (dbuser, dbname))


def servmigrate():
    with virtualenv():
        sudo('python manage.py migrate')
        # sudo('python manage.py buildwatson')


def getdb():
    run('/usr/pgsql-9.3/bin/pg_dump -U %s %s > /tmp/%s.sql' % (dbuser, dbname, dbname))
    get('/tmp/%s.sql' % dbname, '/tmp/%s.sql' % dbname)
    run('rm /tmp/%s.sql' % dbname)


def updatedb():
    local('dropdb -U %s %s' % (dbuser, dbname))
    local('createdb -U %s %s' % (dbuser, dbname))
    local('psql -U %s %s < /tmp/%s.sql' % (dbuser, dbname, dbname))
    local('rm /tmp/%s.sql' % dbname)


def syncdb():
    getdb()
    updatedb()


def pushdb():
    local('pg_dump -U %s %s > /tmp/%s.sql' % (dbuser, dbname, dbname))
    put('/tmp/%s.sql' % dbname, '/tmp/%s.sql' % dbname)
    local('rm /tmp/%s.sql' % dbname)
    sudo('/usr/pgsql-9.3/bin/dropdb -U %s %s' % (dbuser, dbname))
    sudo('/usr/pgsql-9.3/bin/createdb -U %s %s' % (dbuser, dbname))
    sudo('/usr/pgsql-9.3/bin/psql -U %s %s < /tmp/%s.sql' % (dbuser, dbname, dbname))
    sudo('rm /tmp/%s.sql' % dbname)


def syncmedia():
    # local('rsync -avzP --delete --rsync-path="sudo rsync" -e ssh %s:%s/media/ ./media/' % (env.host, env.directory))
    local('rsync -avzP --delete -e ssh %s:%s/media/ ./media/' % (env.host, env.directory))


def pushmedia():
    local('tar -czf /tmp/media.tar media')
    # sudo("rm /tmp/media.tar")
    put('/tmp/media.tar', '/tmp/media.tar')
    with virtualenv():
        sudo("tar -xf /tmp/media.tar")


def deploy():
    pull()
    with virtualenv():
        sudo('python manage.py collectstatic --noinput')
        sudo('touch %s.wsgi' % wsgifilename)


def updateenv():
    pull()
    with virtualenv():
        sudo('pip install -r requirements.txt')
