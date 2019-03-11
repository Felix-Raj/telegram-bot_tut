### Deploying on Heroku
* Create an `Heroku` app - `heroku create` [^1]
* Push to `Heroku` master - `git push heroku master`
* As we are using a worker process, the process may not have been started 
automatically ( `web` process automatically starts when accessing the site 
). Scale the dynamo to start the process - `heroku ps:scale worker=1`


### References for `Heroku`
* [Find the process type for `Procfile`](https://devcenter.heroku.com/articles/process-model#mapping-the-unix-process-model-to-web-apps)

[^1] Foot node sample