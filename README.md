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

sudo pip install -r requirements.txt fixed importing pip packages breaking the server

New superuser is kennylightsail
!iV4p@b$awe!rakI_r6w

Generated token fa76a0f8bb12b546fa56652bc7b667d15c68df56 for user kennylightsail

Bitnami-ssl.conf and Bitnami.conf need this:
<IfModule mod_headers.c>
Header set Access-Control-Allow-Headers "Authorization"
</IfModule>

And check:
https://community.bitnami.com/t/aws-lightsail-django-authentication-credentials-were-not-provided/100382
