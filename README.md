Environment variables in Django Lightsail instances are stored in 
cd /opt/bitnami/scripts/apache-env.sh at the bottom and make sure to run
source /opt/bitnami/scripts/apache-env.sh so Django looks for the env variables
there
Use os.getenv("MY_ENV_VARIABLE") or another python native way because I couldn't
get 3rd party packages to work

TODO:
While SSHed into server, make a deployment script to:

cd /home/bitnami/stack/projects/backend
source /opt/bitnami/scripts/apache-env.sh
git pull
sudo /opt/bitnami/ctlscript.sh restart apache
