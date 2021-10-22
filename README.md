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

Bitnami-ssl.conf and Bitnami.conf need this (May only need to edit Bitnami-ssl.conf if using an SSL Certificate):
<IfModule mod_headers.c>
Header set Access-Control-Allow-Origin "*"
Header set Access-Control-Allow-Methods "GET, OPTIONS, POST"
Header set Access-Control-Allow-Headers "origin, x-requested-with, content-type, accept, Authorization"
</IfModule>

When debugging can use: Header set Access-Control-Allow-Headers "*" 

And check:
https://community.bitnami.com/t/aws-lightsail-django-authentication-credentials-were-not-provided/100382


TODO: Make npm run deploy exclude deleting certain directories

Go here for the set up after using the bncert-tool: C:\Users\kenny\OneDrive\Desktop\LightsailSSLNotes