create folder named monitoring demo where want to setup 
prometheus, grafana for Python App

inside this folder set up
app.py (for python code and prometheus-metrics)
Dockerfile to create image of app
prometheus.yml to configure targets in prometheus
requirements.txt to set up dependencies
docker-compose.yml to set up 3 services

To run the same:
    docker-compose up -d --build
check result
    docker ps 
3 services running now
    localhost:9090 prometheus dashboard
    localhost:3000 grafana dashboard
    localhost:5000 python app

localhost:9090/targets (you can see the services ups or not)
localhost:5000/ - trigger to send req to your web app
localhost:5000/metrics (see prometheus metrics)

refresh multiple times: localhost:5000 to send req

in prometheus query: http_requests_total -- Execute
(below you can see the results)

to send contiue req per second:
while true; do curl -s http://localhost:5000> /dev/null; sleep 1; done
(run in terminal)

you can see the results in prometheus

Let's Setup Grafana dashboard
localhost:3000

will open login page where you can enter credentials mentioned in docker
compose file which is admin, admin.

skip the password change and you will be redirected to dashboard.

Now let's configure prometheus in grafana.

connections --> Add new connection --> search for the prometheus in
data source --> select prometheus --> click on add new Data Source -->

give datasource name: prometheus
URL: http://prometheus:9090

click on save and test

if its gives successfully queries prometheus API
then you can start creating your dashboard.

click on building a dashboard and you can see dashboard screen.

click on Add Visualization
select datasource as prometheus

you can add query below promQL tag 
click on run queries and above you can see the graph.
click on refresh and check

to increase more load:
-- sudo apt install apache2-utils
-- brew install httpd (in mac)

load the traffic send per second 100 req for 30 seconds.

ab -n 3000 -c 100 http://localhost:5000/

see the graph updates in grafana.